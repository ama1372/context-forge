#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run.py - universal project tool for AI-assisted coding.

Commands:
  python run.py                 smart: input empty -> dump; input full -> apply
  python run.py --init          first-time setup
  python run.py --version       show version
  python run.py --capabilities  what this tool can do (for the AI)
  python run.py --status        tiny summary for new chats
  python run.py --tree          project file tree
  python run.py --hash          file hashes
  python run.py --git           git log + tags + status
  python run.py --file X [...]  dump one file (filters below)
  python run.py --files X Y Z   dump several files
  python run.py --errors        last-run errors only
  python run.py dump [--full]   project dump (incremental or full)
  python run.py check           run build_cmd from _work/config.json
  python run.py verify          run test_cmd from _work/config.json
  python run.py find-dup [...]  duplicate detection
  python run.py clean           wipe _work/ (dangerous)

File filters for --file or DUMP:
  --head N   --tail N   --lines A-B   --grep PAT   --grep-i PAT

Directives (in _work/input.txt, first lines):
  #@ID: N              set patch ID manually
  #@CMD: <args>        replace this run with args
  #@POST: <args>       after applying patches, run args and append output
  #@NEED: <args>       after applying patches, dump args and append output
                       (e.g. "status", "file X", "files X Y", "tree", "git",
                        "errors", "hash", "capabilities", "all", "check",
                        "verify", "find-dup")
  #@COMMIT: <message>  custom git commit message (default: "patch N: <ts>")
  #@TAG: <name>        git tag created after a successful commit
  #@NODUMP:            suppress AUTODUMP of failed files on the next run
  #@DUMP: <mode>       set AUTODUMP mode: compact (default), full, off
  #@NEXT: <line>       one-line "what's next" for _work/ctx_delta.txt
  #@ROADMAP: a | b | c pipe-separated roadmap for _work/ctx_delta.txt
  #@PUSH:              after a successful commit + tag, push to origin

Patch syntax (in _work/input.txt) — see PROJECT_CONTEXT.md section 2.
"""

import difflib, hashlib, json, os, re, secrets, shlex, shutil, subprocess, sys
from datetime import datetime
from pathlib import Path

VERSION = "1.1.7"

WORK       = Path('_work')
INPUT      = WORK / 'input.txt'
OUTPUT     = WORK / 'output.txt'
APPLIED    = WORK / 'applied'
CACHE      = WORK / 'cache.json'
CONFIG     = WORK / 'config.json'
LAST_RUN   = WORK / '.last_run'
RATE_WARN_SECONDS = 25

SKIP_DIRS = {
    '.git', '_work', '__pycache__', '.idea', '.vscode',
    'node_modules', 'target', 'dist', 'build', '.venv', 'venv',
    '.pytest_cache', '.mypy_cache', '.next', 'coverage'
}
SKIP_EXTS = {
    '.exe', '.dll', '.so', '.dylib', '.rlib', '.rmeta', '.pdb',
    '.zip', '.tar', '.gz', '.7z', '.rar', '.whl',
    '.png', '.jpg', '.jpeg', '.gif', '.ico', '.svg', '.webp',
    '.pdf', '.ttf', '.otf', '.woff', '.woff2',
    '.lock', '.bin', '.pt', '.pkl', '.pyc', '.pyo',
    '.mp3', '.mp4', '.wav', '.avi', '.mov'
}
SKIP_NAMES = {'run.py'}
MAX_SIZE = 2 * 1024 * 1024

HEADER_RE = re.compile(
    r'^={3,}\s*(FILE|CREATE|DELETE|CMD|MKDIR|DUMP)\s*:\s*(.+?)\s*={3,}\s*$'
)
MOVE_RE = re.compile(r'^={3,}\s*MOVE\s*:\s*(.+?)\s*->\s*(.+?)\s*={3,}\s*$')
FIND, REPLACE, CONTENT, END = '<<<FIND>>>', '<<<REPLACE>>>', '<<<CONTENT>>>', '<<<END>>>'
RUN_MARKER = '<<<RUN>>>'
HASH_MARKER_RE = re.compile(r'^<<<EXPECTED_HASH>>>\s*(.+?)\s*<<<END>>>\s*$')
FENCE_RE = re.compile(r'^\s*```[a-zA-Z0-9_+\-]*\s*$')

AUTO_VERIFY = False
FORCE_APPLY = False


def read(p):
    for enc in ('utf-8', 'utf-8-sig', 'latin-1'):
        try:
            return p.read_text(encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return p.read_text(encoding='latin-1', errors='replace')


DRY_RUN = False
BACKUP = False


def write(p, t):
    if DRY_RUN:
        print(f"  [DRY] would write {p} ({len(t)} chars)")
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(t, encoding='utf-8')


def lf(t):   return t.replace('\r\n', '\n').replace('\r', '\n')
def crlf(t): return lf(t).replace('\n', '\r\n')
def eol(t):  return '\r\n' if '\r\n' in t else '\n'


def hash_file(p):
    h = hashlib.sha256()
    try:
        with open(p, 'rb') as f:
            for c in iter(lambda: f.read(8192), b''):
                h.update(c)
    except OSError:
        return '0' * 12
    return h.hexdigest()[:12]


def msg_seed():
    return secrets.token_hex(4)


def walk(root):
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in fns:
            p = Path(dp) / fn
            if p.name in SKIP_NAMES: continue
            if p.suffix.lower() in SKIP_EXTS: continue
            try:
                if p.stat().st_size > MAX_SIZE: continue
            except OSError:
                continue
            out.append(p)
    return sorted(out, key=lambda p: str(p.relative_to(root)).lower())


def load_cache():
    if CACHE.exists():
        try: return json.loads(CACHE.read_text(encoding='utf-8'))
        except Exception: pass
    return {}


def save_cache(c):
    WORK.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(c, indent=2, ensure_ascii=False), encoding='utf-8')


def load_config():
    default = {"build_cmd": None, "test_cmd": None, "build_cwd": ".", "test_cwd": "."}
    if CONFIG.exists():
        try:
            default.update(json.loads(CONFIG.read_text(encoding='utf-8')))
        except Exception:
            pass
    return default


def strip_fences(lines):
    lines = list(lines)
    if len(lines) < 2: return lines
    i = 0
    while i < len(lines) and not lines[i].strip(): i += 1
    if i >= len(lines) or not FENCE_RE.match(lines[i]): return lines
    j = len(lines) - 1
    while j >= 0 and not lines[j].strip(): j -= 1
    if j <= i or not FENCE_RE.match(lines[j]): return lines
    return lines[:i] + lines[i+1:j] + lines[j+1:]


def filter_content(text, flags):
    if not flags: return text
    lines = text.splitlines()
    i = 0
    while i < len(flags):
        f = flags[i]
        try:
            if f == '--head':
                lines = lines[:int(flags[i+1])]; i += 2
            elif f == '--tail':
                lines = lines[-int(flags[i+1]):]; i += 2
            elif f == '--lines':
                a, b = flags[i+1].split('-', 1)
                a = max(1, int(a)); b = int(b)
                lines = lines[a-1:b] if b >= a else []
                i += 2
            elif f in ('--grep', '--grep-i'):
                pat = flags[i+1]
                if f == '--grep-i':
                    pats = [p.lower() for p in pat.split('|') if p]
                    lines = [l for l in lines if any(p in l.lower() for p in pats)]
                else:
                    pats = [p for p in pat.split('|') if p]
                    lines = [l for l in lines if any(p in l for p in pats)]
                i += 2
            else:
                i += 1
        except (ValueError, IndexError):
            i += 1
    return '\n'.join(lines)


def read_directives(text):
    lines = text.split('\n')
    patch_id = None
    cmd_args = None
    post_cmds = []
    needs = []
    commit_msg = None
    tag_name = None
    nodump = False
    dump_mode = None
    push = False
    idx = 0
    while idx < len(lines):
        s = lines[idx].strip()
        if not s:
            idx += 1; continue
        if not s.startswith('#@'):
            if s.startswith('#'):
                idx += 1; continue
            break
        m = re.match(r'^#@ID:\s*(\d+)', s)
        if m: patch_id = int(m.group(1)); idx += 1; continue
        m = re.match(r'^#@CMD:\s*(.+)$', s)
        if m:
            try: cmd_args = shlex.split(m.group(1).strip())
            except ValueError: cmd_args = m.group(1).strip().split()
            idx += 1; continue
        m = re.match(r'^#@POST:\s*(.+)$', s)
        if m:
            try: post_cmds.append(shlex.split(m.group(1).strip()))
            except ValueError: post_cmds.append(m.group(1).strip().split())
            idx += 1; continue
        m = re.match(r'^#@NEED:\s*(.+)$', s)
        if m:
            try: needs.append(shlex.split(m.group(1).strip()))
            except ValueError: needs.append(m.group(1).strip().split())
            idx += 1; continue
        m = re.match(r'^#@COMMIT:\s*(.+)$', s)
        if m: commit_msg = m.group(1).strip(); idx += 1; continue
        m = re.match(r'^#@TAG:\s*(\S+)', s)
        if m: tag_name = m.group(1); idx += 1; continue
        if s in ('#@NODUMP:', '#@NODUMP'):
            nodump = True; idx += 1; continue
        m = re.match(r'^#@DUMP:\s*(\S+)', s)
        if m: dump_mode = m.group(1).lower(); idx += 1; continue
        if s in ('#@PUSH:', '#@PUSH'):
            push = True; idx += 1; continue
        break
    return (patch_id, cmd_args, post_cmds, needs,
            commit_msg, tag_name, nodump, dump_mode, push,
            '\n'.join(lines[idx:]))


NEED_COMMANDS = {
    'status', 'tree', 'hash', 'git', 'errors', 'capabilities',
    'version', 'all', 'file', 'files', 'check', 'verify',
    'find-dup', 'dump',
}


def need_to_args(need_args):
    if not need_args:
        return []
    cmd = need_args[0].lower()
    if cmd in NEED_COMMANDS:
        return ['--' + cmd] + list(need_args[1:])
    return list(need_args)


def read_cmd_directive_only():
    if not INPUT.exists(): return None
    try:
        content = INPUT.read_text(encoding='utf-8-sig')
    except Exception:
        return None
    if not content: return None
    _, cmd_args, _, _, _, _, _, _, _, _ = read_directives(content)
    if not cmd_args: return None
    lines = content.split('\n')
    new_lines, removed = [], False
    for ln in lines:
        if not removed and re.match(r'^#@CMD:', ln.strip()):
            removed = True; continue
        new_lines.append(ln)
    INPUT.write_text('\n'.join(new_lines), encoding='utf-8')
    print(f"[run.py] #@CMD: {' '.join(cmd_args)}")
    return cmd_args


def parse(text):
    lines = text.splitlines()
    ops, i, n = [], 0, len(lines)
    while i < n:
        mv = MOVE_RE.match(lines[i])
        if mv:
            ops.append({'kind': 'move',
                        'src': mv.group(1).strip(),
                        'dst': mv.group(2).strip()})
            i += 1; continue
        m = HEADER_RE.match(lines[i])
        if not m:
            i += 1; continue
        kind, path = m.group(1).lower(), m.group(2).strip()
        i += 1

        if kind == 'delete':
            ops.append({'kind': 'delete', 'path': path}); continue
        if kind == 'mkdir':
            ops.append({'kind': 'mkdir', 'path': path}); continue
        if kind == 'dump':
            parts = path.split(None, 1)
            p = parts[0]
            flags = parts[1].split() if len(parts) > 1 else []
            ops.append({'kind': 'dump', 'path': p, 'flags': flags}); continue

        if kind == 'cmd':
            while i < n and lines[i].rstrip() != RUN_MARKER:
                if HEADER_RE.match(lines[i]): break
                i += 1
            if i >= n or lines[i].rstrip() != RUN_MARKER:
                ops.append({'kind': 'cmd', 'desc': path, 'script': ''}); continue
            i += 1
            block = []
            while i < n and lines[i].rstrip() != END:
                if HEADER_RE.match(lines[i]): break
                block.append(lines[i]); i += 1
            if i < n and lines[i].rstrip() == END: i += 1
            ops.append({'kind': 'cmd', 'desc': path, 'script': '\n'.join(block)})
            continue

        if kind == 'create':
            while i < n and lines[i].rstrip() != CONTENT:
                if HEADER_RE.match(lines[i]): break
                i += 1
            if i >= n or lines[i].rstrip() != CONTENT:
                ops.append({'kind': 'create', 'path': path, 'content': ''}); continue
            i += 1
            block = []
            while i < n and lines[i].rstrip() != END:
                if HEADER_RE.match(lines[i]): break
                block.append(lines[i]); i += 1
            if i < n and lines[i].rstrip() == END: i += 1
            ops.append({'kind': 'create', 'path': path,
                        'content': '\n'.join(strip_fences(block))})
            continue

        expected_hash = None
        j = i
        while j < n and not HEADER_RE.match(lines[j]):
            mh = HASH_MARKER_RE.match(lines[j].strip())
            if mh: expected_hash = mh.group(1); break
            j += 1

        patches = []
        while i < n:
            if HEADER_RE.match(lines[i]): break
            if lines[i].strip().startswith('<<<EXPECTED_HASH>>>'):
                i += 1; continue
            if lines[i].rstrip() == FIND:
                i += 1
                a = []
                while i < n and lines[i].rstrip() != REPLACE:
                    a.append(lines[i]); i += 1
                if i >= n or lines[i].rstrip() != REPLACE: break
                i += 1
                r = []
                while i < n and lines[i].rstrip() != END:
                    r.append(lines[i]); i += 1
                if i < n and lines[i].rstrip() == END: i += 1
                patches.append(('\n'.join(strip_fences(a)),
                                '\n'.join(strip_fences(r))))
                continue
            i += 1
        ops.append({'kind': 'file', 'path': path,
                    'patches': patches, 'hash': expected_hash})
    return ops


def find_exact(text, a):
    p = text.find(a)
    return (p, p + len(a), 1) if p >= 0 else None


def find_soft(text, a):
    flines = text.splitlines(keepends=True)
    alines = a.splitlines()
    while alines and not alines[-1].strip(): alines.pop()
    if not alines: return None
    for lvl, tr in ((2, str.rstrip), (3, str.strip)):
        arr = [tr(x) for x in alines]
        m = len(arr)
        for s in range(len(flines) - m + 1):
            if tr(flines[s].rstrip('\n')) != arr[0]: continue
            ok = True
            for j in range(1, m):
                if tr(flines[s+j].rstrip('\n')) != arr[j]:
                    ok = False; break
            if ok:
                so = sum(len(l) for l in flines[:s])
                eo = sum(len(l) for l in flines[:s+m])
                return so, eo, lvl
    return None


FUZZY = True


def find_anchor(text, a):
    r = find_exact(text, a)
    if r: return r
    if not FUZZY: return None
    return find_soft(text, a)


def suggest(text, a):
    fl = text.splitlines(); al = a.splitlines()
    while al and not al[-1].strip(): al.pop()
    if not al or not fl: return None
    n = len(al); astr = '\n'.join(al); afirst = al[0].strip()
    best = (0.0, None, -1)
    for i in range(len(fl)):
        ln = fl[i].strip()
        if afirst and afirst not in ln and ln not in afirst and not ln: continue
        for d in (0, 1, -1, 2, -2, 3, -3):
            k = n + d
            if k <= 0 or i + k > len(fl): continue
            b = '\n'.join(fl[i:i+k])
            r = difflib.SequenceMatcher(None, astr, b).ratio()
            if r > best[0]: best = (r, b, i)
    return best if best[1] and best[0] >= 0.55 else None


def apply_patch(path, patches, out, fail_files=None):
    p = Path(path)
    if not p.exists():
        out.append(f"  [FAIL] file not found: {path}")
        if fail_files is not None: fail_files.add(path)
        return 0, len(patches), 0
    raw = read(p); fe = eol(raw); text = lf(raw)
    ok = fail = skip = 0
    for i, (a, r) in enumerate(patches, 1):
        al, rl = lf(a), lf(r)
        if not al:
            out.append(f"  [FAIL] [{i}/{len(patches)}] empty anchor")
            fail += 1
            if fail_files is not None: fail_files.add(path)
            continue
        if rl and rl in text and not find_anchor(text, al):
            out.append(f"  [SKIP] [{i}/{len(patches)}] already applied")
            skip += 1; continue
        f = find_anchor(text, al)
        if not f:
            first = al.splitlines()[0] if al else ''
            out.append(f"  [FAIL] [{i}/{len(patches)}] anchor not found")
            out.append(f"         start: {first[:70]}")
            s = suggest(text, al)
            if s:
                rr, blk, sl = s
                out.append(f"         nearest: {rr*100:.0f}% match, line {sl+1}")
                out.append("         " + "-" * 60)
                for x in blk.splitlines(): out.append(f"         | {x}")
                out.append("         " + "-" * 60)
            fail += 1
            if fail_files is not None: fail_files.add(path)
            continue
        s_, e_, lvl = f
        if lvl > 1:
            out.append(f"  [SOFT] [{i}/{len(patches)}] matched level {lvl}")
        text = text[:s_] + rl + text[e_:]
        out.append(f"  [OK]   [{i}/{len(patches)}] applied")
        ok += 1
    if ok or skip:
        write(p, crlf(text) if fe == '\r\n' else text)
    return ok, fail, skip


def _autodump_block(fail_files, mode='compact'):
    if not fail_files or mode == 'off':
        return []
    L = ["", "=" * 60,
         "AUTODUMP (failed files - content for re-anchoring)",
         "=" * 60]
    MAX_FILES, HEAD, TAIL = 3, 25, 25
    for path in list(fail_files)[:MAX_FILES]:
        p = Path(path)
        if not p.exists():
            L.append(f"\nFILE: {path}  [not found]"); continue
        L.append("")
        L.append("-" * 60)
        L.append(f"FILE: {path}  (size: {p.stat().st_size} bytes)")
        L.append("-" * 60)
        raw = read(p)
        all_lines = raw.splitlines()
        total = len(all_lines)
        if mode == 'full' or total <= HEAD + TAIL:
            L.append(raw.rstrip())
        else:
            L.append(f"[total {total} lines; showing first {HEAD} + last {TAIL}]")
            L.append("")
            L.append(f"--- HEAD (first {HEAD} lines) ---")
            L.append('\n'.join(all_lines[:HEAD]))
            L.append("")
            L.append(f"--- TAIL (last {TAIL} lines) ---")
            L.append('\n'.join(all_lines[-TAIL:]))
    if len(fail_files) > MAX_FILES:
        L.append(""); L.append(f"... +{len(fail_files) - MAX_FILES} more failed files")
    return L


def _rate_warn_line():
    if not LAST_RUN.exists(): return None
    try:
        prev = datetime.fromisoformat(LAST_RUN.read_text().strip())
    except Exception:
        return None
    delta = (datetime.now() - prev).total_seconds()
    if delta < RATE_WARN_SECONDS:
        wait = int(RATE_WARN_SECONDS - delta) + 1
        return (f"RATE WARN: {int(delta)}s since last run. "
                f"Wait {wait}s before sending to the assistant.")
    return None


def _rate_warn_write():
    WORK.mkdir(parents=True, exist_ok=True)
    LAST_RUN.write_text(datetime.now().isoformat(timespec='seconds'),
                        encoding='utf-8')


def _git_head():
    try:
        r = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                           capture_output=True, text=True, timeout=5)
        return (r.stdout or '').strip() or '-'
    except Exception:
        return '-'


def _update_auto_block(patch_id, seed):
    ctx = Path("PROJECT_CONTEXT.md")
    if not ctx.exists(): return
    text = ctx.read_text(encoding="utf-8")
    START, END_MARK = "<!-- AUTO:START -->", "<!-- AUTO:END -->"
    if START not in text or END_MARK not in text: return
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    h = _git_head()
    block = (
        f"{START}\n"
        f"## Last patch (auto - do not edit)\n\n"
        f"| Field | Value |\n"
        f"|-------|-------|\n"
        f"| Last patch | P{patch_id} |\n"
        f"| Last commit | `{h}` |\n"
        f"| Time | {ts} |\n"
        f"| MSG-SEED | `{seed}` |\n"
        f"{END_MARK}"
    )
    before = text[:text.index(START)]
    after = text[text.index(END_MARK) + len(END_MARK):]
    ctx.write_text(before + block + after, encoding="utf-8")


def do_apply(patch_id=None):
    content = INPUT.read_text(encoding='utf-8-sig')
    rate_msg = _rate_warn_line()
    (did, _, post_cmds, needs,
     commit_msg, tag_name, nodump, dump_mode, push,
     remaining) = read_directives(content)
    if did is not None: patch_id = did
    content = remaining

    if patch_id is None:
        idfile = WORK / '.patch_id'
        try:
            cur = int(idfile.read_text().strip()) if idfile.exists() else 0
        except Exception:
            cur = 0
        patch_id = cur + 1
        WORK.mkdir(parents=True, exist_ok=True)
        idfile.write_text(str(patch_id), encoding='utf-8')

    ops = parse(content)
    seed = msg_seed()
    out = [f"# MSG-SEED: {seed}", "[APPLY]", "", f"# PATCH_ID: {patch_id}", ""]
    if BACKUP:
        _do_backup()
    if rate_msg:
        out.append(rate_msg)
        out.append("Hint: batch 2-3 patches per input.txt to reduce message count.")
        out.append("")

    if not ops:
        out.append("[FAIL] no valid patches")
        write(OUTPUT, '\n'.join(out)); print('\n'.join(out)); return 2

    ok = fail = skip = 0
    fail_files = set()
    for op in ops:
        kind = op['kind']

        if kind == 'file':
            out.append(f"[P{patch_id}] [EDIT] {op['path']}")
            if not op['patches']:
                out.append("  [WARN] empty FILE block"); continue
            exp = op.get('hash')
            if exp:
                p = Path(op['path'])
                if p.exists():
                    actual = hash_file(p)
                    if actual != exp:
                        out.append(f"  [HASH] expected: {exp}")
                        out.append(f"  [HASH] actual:   {actual}")
                        if AUTO_VERIFY:
                            out.append("  [SKIP] hash mismatch (auto-verify)")
                            skip += 1; continue
                        if not FORCE_APPLY:
                            out.append("  [WARN] hash mismatch - applying anyway")
            a, b, s = apply_patch(op['path'], op['patches'], out, fail_files)
            ok += a; fail += b; skip += s

        elif kind == 'create':
            p = Path(op['path']); existed = p.exists()
            out.append(f"[P{patch_id}] [NEW]  {op['path']}")
            write(p, lf(op['content']))
            out.append(f"  [OK]   {'updated' if existed else 'created'} ({len(op['content'])} chars)")
            ok += 1

        elif kind == 'delete':
            p = Path(op['path'])
            out.append(f"[P{patch_id}] [DEL]  {op['path']}")
            if p.exists(): p.unlink()
            ok += 1

        elif kind == 'mkdir':
            p = Path(op['path'])
            out.append(f"[P{patch_id}] [MKDIR] {op['path']}")
            p.mkdir(parents=True, exist_ok=True)
            out.append("  [OK]   created")
            ok += 1

        elif kind == 'move':
            src = Path(op['src']); dst = Path(op['dst'])
            out.append(f"[P{patch_id}] [MOVE] {op['src']} -> {op['dst']}")
            if not src.exists():
                out.append(f"  [FAIL] source not found: {op['src']}")
                fail += 1; continue
            if dst.exists():
                out.append("  [FAIL] dest exists (no overwrite)")
                fail += 1; continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            out.append("  [OK]   moved")
            ok += 1

        elif kind == 'cmd':
            out.append(f"[P{patch_id}] [CMD]  {op['desc']}")
            script = op['script']
            if not script.strip():
                out.append("  [WARN] empty script"); continue
            if re.search(r'python\s+run\.py', script, re.IGNORECASE):
                out.append("  [WARN] CMD calls python run.py (nested) - skipped")
                continue
            try:
                r = subprocess.run(
                    ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass',
                     '-Command', script],
                    capture_output=True, text=True, encoding='utf-8',
                    errors='replace', timeout=900)
                for ln in (r.stdout or '').rstrip().splitlines():
                    out.append(f"  | {ln}")
                for ln in (r.stderr or '').rstrip().splitlines():
                    out.append(f"  ! {ln}")
                if r.returncode == 0:
                    out.append("  [OK]   exit 0"); ok += 1
                else:
                    out.append(f"  [FAIL] exit {r.returncode}"); fail += 1
            except subprocess.TimeoutExpired:
                out.append("  [FAIL] timeout 900s"); fail += 1
            except Exception as e:
                out.append(f"  [FAIL] {e}"); fail += 1

    dumps = [op for op in ops if op['kind'] == 'dump']
    if dumps:
        out.append(""); out.append("=" * 60)
        out.append("REQUESTED FILE DUMPS"); out.append("=" * 60)
        for dop in dumps:
            dp = Path(dop['path'])
            out.append(""); out.append("-" * 60)
            out.append(f"FILE: {dop['path']}")
            if not dp.exists():
                out.append("[FAIL] not found"); continue
            out.append(f"SIZE: {dp.stat().st_size} bytes")
            raw = read(dp)
            filtered = filter_content(raw, dop.get('flags', []))
            out.append(f"FLAGS: {' '.join(dop.get('flags', [])) or '(none)'}")
            out.append(f"SHOWN: {len(filtered.splitlines())} of {len(raw.splitlines())} lines")
            out.append("-" * 60)
            out.append(filtered.rstrip())

    if fail_files:
        if nodump:
            ad_mode = 'off'
        elif dump_mode in ('full', 'compact', 'off'):
            ad_mode = dump_mode
        else:
            ad_mode = 'compact'
        out.extend(_autodump_block(fail_files, ad_mode))

    out.append(""); out.append("=" * 60)
    out.append(f"PATCH_ID: {patch_id}  |  OK: {ok}  |  SKIP: {skip}  |  FAIL: {fail}")

    APPLIED.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    arch = APPLIED / f'P{patch_id:04d}-{ts}.txt'
    if INPUT.exists():
        try: INPUT.rename(arch)
        except Exception: shutil.copy(INPUT, arch)
    INPUT.write_text('', encoding='utf-8')
    out.append("")
    out.append(f"[ARCH] {arch}")
    if fail == 0:
        out.append("       input.txt emptied - ready for next patch")
    else:
        out.append(f"       {fail} patch(es) FAILED")
        out.append("       input.txt emptied anyway")

    if post_cmds and fail == 0:
        for sub_args in post_cmds:
            out.append(""); out.append("=" * 60)
            out.append(f"POST: {' '.join(sub_args)}"); out.append("=" * 60)
            out.append("")
            sub_out = dispatch_capture(sub_args)
            if sub_out:
                out.append(sub_out)

    if needs:
        for need_args in needs:
            real_args = need_to_args(need_args)
            out.append(""); out.append("=" * 60)
            out.append(f"NEED: {' '.join(need_args)}"); out.append("=" * 60)
            out.append("")
            sub_out = dispatch_capture(real_args)
            if sub_out:
                out.append(sub_out)

    if fail == 0:
        try: _update_auto_block(patch_id, seed)
        except Exception: pass

    if fail == 0:
        try:
            r0 = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'],
                                capture_output=True, text=True)
            if r0.returncode == 0 and r0.stdout.strip() == 'true':
                msg = commit_msg if commit_msg else f"patch {patch_id}: {ts}"
                subprocess.run(['git', 'add', '-A'], capture_output=True)
                r1 = subprocess.run(['git', 'commit', '-m', msg],
                                    capture_output=True, text=True)
                out.append("")
                if r1.returncode == 0:
                    out.append(f"[GIT] commit: {msg}")
                    if tag_name:
                        r2 = subprocess.run(['git', 'tag', tag_name],
                                            capture_output=True, text=True)
                        if r2.returncode == 0:
                            out.append(f"[GIT] tag: {tag_name}")
                        else:
                            out.append(f"[GIT] tag failed: {r2.stderr.strip()[:200]}")
                else:
                    combined = (r1.stdout or '') + (r1.stderr or '')
                    if 'nothing to commit' in combined:
                        out.append("[GIT] nothing to commit")
                        if tag_name:
                            r2 = subprocess.run(['git', 'tag', tag_name],
                                                capture_output=True, text=True)
                            if r2.returncode == 0:
                                out.append(f"[GIT] tag: {tag_name}")
                    else:
                        out.append(f"[GIT] failed: {r1.stderr.strip()[:200]}")
        except FileNotFoundError:
            out.append(""); out.append("[GIT] git not installed")
        except Exception as e:
            out.append(""); out.append(f"[GIT] error: {e}")

    if push and fail == 0:
        try:
            r_b = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                                  capture_output=True, text=True, timeout=5)
            branch = (r_b.stdout or '').strip() or 'main'
            r_p = subprocess.run(['git', 'push', '--quiet', 'origin', branch],
                                  capture_output=True, text=True, timeout=120)
            out.append("")
            if r_p.returncode == 0:
                out.append(f"[GIT] pushed: origin {branch}")
            else:
                out.append(f"[GIT] push failed: {(r_p.stderr or '').strip()[:200]}")
            if tag_name:
                r_pt = subprocess.run(['git', 'push', '--quiet', 'origin', tag_name],
                                       capture_output=True, text=True, timeout=120)
                if r_pt.returncode == 0:
                    out.append(f"[GIT] pushed tag: {tag_name}")
                else:
                    out.append(f"[GIT] push tag failed: {(r_pt.stderr or '').strip()[:200]}")
        except Exception as e:
            out.append(""); out.append(f"[GIT] push error: {e}")

    if fail == 0:
        try:
            next_step = extract_next(content)
            roadmap = extract_roadmap(content)
            paths = []
            for op in ops:
                if op['kind'] in ('file', 'create', 'delete'):
                    paths.append(op.get('path', ''))
                elif op['kind'] == 'move':
                    paths.append(op.get('dst', ''))
            _write_ctx_delta(patch_id, tag_name, commit_msg, next_step, roadmap, paths)
            out.append("")
            out.append("[CTX] ctx_delta saved -> _work/ctx_delta.txt")
        except Exception as e:
            out.append(""); out.append(f"[CTX] save failed: {e}")

    _rate_warn_write()
    txt = '\n'.join(out)
    write(OUTPUT, txt); print(txt)
    return 0 if fail == 0 else 2


def do_dump(full=False):
    root = Path('.').resolve()
    cache = load_cache()
    files = walk(root)
    manifest, changed = [], []
    for p in files:
        rel = str(p.relative_to(root))
        h = hash_file(p)
        old = cache.get(rel, {}).get('hash')
        is_ch = (old != h)
        manifest.append((rel, is_ch))
        if is_ch or full: changed.append(p)
        cache[rel] = {'hash': h,
                      'last_seen': datetime.now().isoformat(timespec='seconds')}
    save_cache(cache)

    seed = msg_seed()
    L = [f"# MSG-SEED: {seed}",
         f"# PROJECT DUMP - {datetime.now().isoformat(timespec='seconds')}",
         f"# mode: {'full' if full else 'incremental'}",
         f"# {len(files)} files total, {len(changed)} included",
         "", "=" * 72, "MANIFEST", "=" * 72]
    for rel, ch in manifest:
        L.append(f"{'[CHANGED]' if ch else '         '} {rel}")
    L.append("")

    if changed:
        L.append("=" * 72)
        L.append(f"CONTENT ({len(changed)} files)")
        L.append("=" * 72)
        for p in changed:
            rel = p.relative_to(root)
            L.append(""); L.append("-" * 72)
            L.append(f"FILE: {rel}")
            L.append(f"HASH: {hash_file(p)}")
            L.append("-" * 72)
            L.append(read(p).rstrip())
    else:
        L.append("(no changed files)"); L.append("")

    body = '\n'.join(L)
    new_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()[:16]
    if OUTPUT.exists() and not full:
        old = read(OUTPUT)
        if f"# content_hash: {new_hash}" in old:
            print("[DUPLICATE] output.txt identical to previous run")
            print("            -> DO NOT send to assistant")
            return
    L.insert(2, f"# content_hash: {new_hash}")
    txt = '\n'.join(L)
    write(OUTPUT, txt)
    print(f"[DUMP] {OUTPUT}")
    print(f"       mode: {'full' if full else 'incremental'}")
    print(f"       {len(files)} files total  |  {len(changed)} included")
    print(f"       size: {OUTPUT.stat().st_size:,} bytes")
    print(); print(f"[NEW] send this file to assistant: {OUTPUT}")


def do_status():
    root = Path('.').resolve()
    out = [f"PROJECT: {root.name}"]
    try:
        r = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            out.append(f"LAST TAG: {r.stdout.strip()}")
    except Exception: pass
    try:
        r = subprocess.run(['git', 'status', '--short'],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            files = [ln[3:].strip() for ln in r.stdout.splitlines() if ln.strip()]
            out.append(f"MODIFIED: {len(files)} files")
            for f in files[:20]: out.append(f"  {f}")
    except Exception: pass
    out.append(f"TOTAL FILES: {len(walk(root))}")
    if OUTPUT.exists():
        try:
            for ln in read(OUTPUT).splitlines()[:40]:
                if 'FAIL' in ln:
                    out.append(ln.strip()); break
        except Exception: pass
    print('\n'.join(out))


def do_tree():
    root = Path('.').resolve()
    print(f"PROJECT: {root.name}")
    for p in walk(root):
        rel = p.relative_to(root)
        depth = len(rel.parts) - 1
        print(f"{'  ' * depth}{rel.name}")


def do_hash():
    root = Path('.').resolve()
    for p in walk(root):
        rel = p.relative_to(root)
        print(f"{hash_file(p)}  {rel}")


def do_git():
    for cmd in (['git', 'log', '--oneline', '-10'],
                ['git', 'tag'],
                ['git', 'status', '--short']):
        try:
            print(f"$ {' '.join(cmd)}")
            r = subprocess.run(cmd, capture_output=True, text=True,
                               encoding='utf-8', errors='replace', timeout=10)
            print(r.stdout)
        except Exception as e:
            print(f"[WARN] {e}")


def do_diff():
    root = Path('.').resolve()
    cache = load_cache()
    changed = []
    for p in walk(root):
        rel = str(p.relative_to(root))
        h = hash_file(p)
        old = cache.get(rel, {}).get('hash')
        if old != h:
            changed.append((rel, 'new' if old is None else 'modified'))
    if not changed:
        print("[DIFF] no changes since last dump")
        return
    print(f"[DIFF] {len(changed)} file(s) changed:")
    for rel, kind in changed:
        print(f"  [{kind}] {rel}")


def _do_backup():
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    tag = f"auto-backup-{ts}"
    try:
        r = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'],
                           capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip() == 'true':
            subprocess.run(['git', 'add', '-A'], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'auto-backup {ts}',
                            '--allow-empty'], capture_output=True)
            r2 = subprocess.run(['git', 'tag', tag],
                                capture_output=True, text=True)
            if r2.returncode == 0:
                print(f"[BACKUP] git tag: {tag}")
            else:
                print(f"[BACKUP] tag failed: {r2.stderr.strip()[:200]}")
            return
    except Exception:
        pass
    print("[BACKUP] no git - skipped")


def extract_next(content):
    for line in content.split('\n'):
        s = line.strip()
        if not s:
            continue
        m = re.match(r'^#@NEXT:\s*(.+)$', s)
        if m:
            return m.group(1).strip()
        if not s.startswith('#'):
            break
    return None


def extract_roadmap(content):
    for line in content.split('\n'):
        s = line.strip()
        if not s:
            continue
        m = re.match(r'^#@ROADMAP:\s*(.+)$', s)
        if m:
            return [x.strip() for x in m.group(1).split('|') if x.strip()]
        if not s.startswith('#'):
            break
    return []


def _write_ctx_delta(patch_id, tag_name, commit_msg, next_step, roadmap, paths):
    tag = tag_name or f'patch-{patch_id}'
    work = commit_msg or f'patch {patch_id}'
    for emoji in ('✨', '🐛', '🌍', '⚡', '🎉', '🧹', '📘', '📄', '🔍', '📌', '🚨'):
        if work.startswith(emoji + ' '):
            work = work[len(emoji) + 1:]
            break
    lines = [
        '[CTX-DELTA]',
        f'TAG: {tag}',
        f'WORK: {work}',
        f'NEXT: {next_step or "(unspecified)"}',
    ]
    if roadmap:
        lines.append('ROADMAP:')
        for i, step in enumerate(roadmap, 1):
            lines.append(f'  {i}. {step}')
    lines.append(f'FILES: {", ".join(paths) if paths else "(none)"}')
    lines.append('[/CTX-DELTA]')
    lines.append('')
    WORK.mkdir(parents=True, exist_ok=True)
    (WORK / 'ctx_delta.txt').write_text('\n'.join(lines), encoding='utf-8')


def do_file(name, flags=None):
    p = Path(name)
    if not p.is_absolute():
        p = Path('.').resolve() / name
    if not p.exists():
        print(f"[FAIL] file not found: {name}"); return
    raw = read(p)
    filtered = filter_content(raw, flags or [])
    print(f"FILE: {name}")
    print(f"HASH: {hash_file(p)}")
    print(f"SIZE: {p.stat().st_size} bytes")
    if flags:
        print(f"FLAGS: {' '.join(flags)}")
        print(f"SHOWN: {len(filtered.splitlines())} of {len(raw.splitlines())} lines")
    print("---CONTENT---")
    print(filtered)


def do_files(names):
    for i, name in enumerate(names):
        if i > 0: print()
        do_file(name)


def do_errors():
    if not OUTPUT.exists():
        print("[INFO] no output.txt yet"); return
    found = False
    for ln in read(OUTPUT).splitlines():
        if '[FAIL]' in ln or 'FAIL:' in ln:
            print(ln); found = True
    if not found:
        print("[INFO] no errors in last output.txt")


def do_check_md(files):
    if not files:
        files = [str(p) for p in walk(Path('.')) if p.suffix.lower() == '.md']
    if not files:
        print("[INFO] no markdown files found"); return 0
    issues = 0
    for path in files:
        p = Path(path)
        if not p.exists():
            print(f"[FAIL] not found: {path}"); issues += 1; continue
        text = read(p)
        lines = text.splitlines()
        stack = []
        for i, line in enumerate(lines, 1):
            m = re.match(r'^(\s*)(`{3,}|~{3,})', line)
            if not m: continue
            indent = len(m.group(1))
            if indent > 3: continue
            fence = m.group(2)
            kind = fence[0]
            count = len(fence)
            if not stack:
                stack.append((i, kind, count))
            else:
                top_line, top_kind, top_count = stack[-1]
                if kind == top_kind and count >= top_count:
                    stack.pop()
                else:
                    print(f"[WARN] {path}:{i}: nested fence inside "
                          f"{top_kind * top_count} opened at line {top_line}")
                    issues += 1
                    stack.append((i, kind, count))
        for line_no, kind, count in stack:
            print(f"[WARN] {path}:{line_no}: unclosed fence {kind * count}")
            issues += 1
    if issues == 0:
        print(f"[OK] no nested or unclosed fences in {len(files)} file(s)")
    return 0 if issues == 0 else 2


PERSIAN_DIGITS = '۰۱۲۳۴۵۶۷۸۹'
ARABIC_DIGITS  = '٠١٢٣٤٥٦٧٨٩'


def _norm_num(s):
    for i, c in enumerate(PERSIAN_DIGITS):
        s = s.replace(c, str(i))
    for i, c in enumerate(ARABIC_DIGITS):
        s = s.replace(c, str(i))
    return s


def _sections_of(p):
    text = read(p)
    out = []
    for line in text.splitlines():
        m = re.match(r'^##\s+(?:Section\s+)?([0-9][0-9A-Za-z\-\.]*)',
                     _norm_num(line.strip()))
        if m:
            out.append(m.group(1))
    return out


def do_check_sections(path_a, path_b):
    pa, pb = Path(path_a), Path(path_b)
    if not pa.exists():
        print(f"[FAIL] not found: {path_a}"); return 1
    if not pb.exists():
        print(f"[FAIL] not found: {path_b}"); return 1
    sa, sb = _sections_of(pa), _sections_of(pb)
    set_a, set_b = set(sa), set(sb)
    print(f"[A] {path_a}: {len(sa)} sections")
    print(f"[B] {path_b}: {len(sb)} sections")
    only_a = sorted(set_a - set_b)
    only_b = sorted(set_b - set_a)
    if only_a:
        print(f"\nOnly in A ({len(only_a)}):")
        for s in only_a: print(f"  Section {s}")
    if only_b:
        print(f"\nOnly in B ({len(only_b)}):")
        for s in only_b: print(f"  Section {s}")
    if not only_a and not only_b:
        print("[OK] section sets match")
    return 0 if not (only_a or only_b) else 1


def do_capabilities():
    print(f"run.py v{VERSION}")
    print("FLAGS: --version --init --capabilities --status --tree --hash "
          "--git --file --files --errors --diff --ctx "
          "--check-md --check-sections "
          "--auto-verify --force --fuzzy --no-fuzzy --dry-run --backup "
          "dump[--full] check verify find-dup apply clean")
    print("PATCH_TYPES: FILE CREATE DELETE MOVE MKDIR CMD DUMP")
    print("DIRECTIVES: #@ID #@CMD #@POST #@NEED #@COMMIT #@TAG #@NODUMP #@DUMP #@NEXT #@ROADMAP #@PUSH")
    print("FEATURES: MSG-SEED RATE-WARN AUTO-BLOCK AUTODUMP "
          "FUZZY-MATCH SUGGEST HASH-VERIFY GIT-AUTO-COMMIT")


def do_check(args):
    cfg = load_config()
    if not cfg.get('build_cmd'):
        print("[INFO] no build_cmd in _work/config.json")
        print('       example: {"build_cmd": ["cargo","check"], "build_cwd": "src-tauri"}')
        return 1
    quiet = any(a in ('quiet', '--q', '-q') for a in args)
    try:
        r = subprocess.run(cfg['build_cmd'], cwd=cfg.get('build_cwd', '.'),
                           capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=600)
    except subprocess.TimeoutExpired:
        print("[FAIL] build timeout (600s)"); return 2
    except FileNotFoundError:
        print(f"[FAIL] command not found: {cfg['build_cmd'][0]}"); return 2
    except Exception as e:
        print(f"[FAIL] {e}"); return 2
    combined = (r.stdout or '') + '\n' + (r.stderr or '')
    errs = [l for l in combined.splitlines()
            if 'error' in l.lower() and 'error_count' not in l.lower()]
    warns = [l for l in combined.splitlines()
             if 'warning' in l.lower() and 'warning_count' not in l.lower()]
    if quiet:
        print("clean" if not errs else f"{len(errs)} errors")
    else:
        print(f"exit: {r.returncode}")
        print(f"errors: {len(errs)}  warnings: {len(warns)}")
        if errs:
            print("\n## ERRORS"); print('\n'.join(errs[:50]))
        if warns and not errs:
            print("\n## WARNINGS (first 20)"); print('\n'.join(warns[:20]))
    return 0 if r.returncode == 0 else 2


def do_verify(args):
    cfg = load_config()
    if not cfg.get('test_cmd'):
        print("[INFO] no test_cmd in _work/config.json")
        print('       example: {"test_cmd": ["cargo","test"], "test_cwd": "src-tauri"}')
        return 1
    try:
        r = subprocess.run(cfg['test_cmd'] + list(args),
                           cwd=cfg.get('test_cwd', '.'),
                           capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=900)
    except subprocess.TimeoutExpired:
        print("[FAIL] test timeout (900s)"); return 2
    except FileNotFoundError:
        print(f"[FAIL] command not found: {cfg['test_cmd'][0]}"); return 2
    except Exception as e:
        print(f"[FAIL] {e}"); return 2
    if r.stdout: print(r.stdout.rstrip())
    if r.stderr:
        for ln in r.stderr.rstrip().splitlines():
            s = ln.strip()
            if s.startswith(('warning:', 'note:', '=', '|', '-->', 'help:')):
                continue
            print(ln)
    return 0 if r.returncode == 0 else 2


def cmd_find_dup(args):
    import collections
    min_len = 20 if ('--meaningful' in args or '-m' in args) else 6
    top_n = 60
    if '--top' in args:
        try: top_n = max(1, int(args[args.index('--top') + 1]))
        except (ValueError, IndexError): pass
    if '--min' in args:
        try: min_len = int(args[args.index('--min') + 1])
        except (ValueError, IndexError): pass

    exts = {'.py', '.js', '.ts', '.rs', '.go', '.rb', '.java', '.c', '.cpp', '.h',
            '.toml', '.yaml', '.yml'}
    line_map = collections.defaultdict(list)
    fn_map = collections.defaultdict(list)
    src_cache = {}
    for p in walk(Path('.')):
        if p.suffix.lower() not in exts: continue
        try: content = read(p)
        except Exception: continue
        rel = str(p).replace('\\', '/')
        src_cache[rel] = content.splitlines()
        for ln, line in enumerate(src_cache[rel], 1):
            s = line.strip()
            if not s or s.startswith('//') or s.startswith('#'): continue
            if len(s) < min_len: continue
            line_map[s].append((rel, ln))
            m = re.match(r'^(pub\s+)?(async\s+)?(fn|def|function)\s+([A-Za-z_]\w*)', s)
            if m: fn_map[m.group(4)].append((rel, ln))

    out = ["=" * 62, "FIND-DUPLICATES REPORT",
           f"  files scanned: {len(src_cache)}",
           f"  min line length: {min_len}",
           "=" * 62, ""]
    dup_fns = {k: v for k, v in fn_map.items() if len(v) >= 2}
    out.append(f"## DUPLICATE FUNCTION NAMES ({len(dup_fns)})"); out.append("")
    if not dup_fns: out.append("(none)")
    for name, locs in sorted(dup_fns.items(), key=lambda x: -len(x[1])):
        out.append(f"  fn {name}  ({len(locs)} locations)")
        for f, ln in locs: out.append(f"      {f}:{ln}")
        out.append("")
    dup_lines = {k: v for k, v in line_map.items() if len(v) >= 2}
    sorted_lines = sorted(dup_lines.items(), key=lambda x: (-len(x[1]), x[0]))
    out.append("")
    out.append(f"## DUPLICATE LINES ({len(dup_lines)} unique, top {top_n})")
    out.append("")
    for line, locs in sorted_lines[:top_n]:
        preview = line if len(line) <= 100 else line[:100] + '...'
        out.append(f"  [{len(locs)}x] {preview}")
        for f, ln in locs[:5]: out.append(f"      {f}:{ln}")
        if len(locs) > 5: out.append(f"      ... +{len(locs)-5} more")
        out.append("")
    txt = '\n'.join(out)
    write(OUTPUT, f"# MSG-SEED: {msg_seed()}\n# FIND-DUP\n\n{txt}\n")
    print(f"[FIND-DUP] {OUTPUT}")


def do_init():
    WORK.mkdir(parents=True, exist_ok=True)
    APPLIED.mkdir(parents=True, exist_ok=True)
    INPUT.write_text('', encoding='utf-8')
    OUTPUT.write_text('', encoding='utf-8')
    gi = Path('.gitignore')
    if not gi.exists():
        gi.write_text(
            "_work/input.txt\n_work/output.txt\n_work/applied/\n"
            "_work/cache.json\n_work/.patch_id\n_work/.last_run\n"
            "*.pyc\n__pycache__/\n.venv/\nvenv/\nbuild/\ndist/\n"
            "target/\nnode_modules/\n*.log\n.DS_Store\nThumbs.db\n",
            encoding='utf-8')
        print("[INIT] .gitignore written")
    else:
        print("[INIT] .gitignore already exists - skipped")
    if not CONFIG.exists():
        CONFIG.write_text(json.dumps({
            "build_cmd": None, "test_cmd": None,
            "build_cwd": ".", "test_cwd": "."
        }, indent=2), encoding='utf-8')
        print("[INIT] _work/config.json written (edit build_cmd/test_cmd)")
    print("[INIT] _work/ ready")
    print()
    print("Next steps:")
    print("  1. Put PROJECT_CONTEXT.md in the project root")
    print("  2. Edit _work/config.json - set build_cmd and test_cmd")
    print("  3. Run: python run.py --status")


def dispatch_capture(args):
    import io, contextlib
    backup = None
    if OUTPUT.exists():
        try: backup = OUTPUT.read_text(encoding='utf-8')
        except Exception: backup = None
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            dispatch(args)
    finally:
        if backup is not None:
            try: OUTPUT.write_text(backup, encoding='utf-8')
            except Exception: pass
    return buf.getvalue().rstrip()


def dispatch(args):
    global AUTO_VERIFY, FORCE_APPLY, FUZZY, DRY_RUN, BACKUP
    if not args: return None
    cmd = args[0]

    if cmd in ('--version', '-v'):     print(f"run.py v{VERSION}"); return 0
    if cmd == '--init':                 do_init(); return 0
    if cmd == '--capabilities':         do_capabilities(); return 0
    if cmd == '--ctx':
        _p = WORK / 'ctx_delta.txt'
        if _p.exists():
            print(_p.read_text(encoding='utf-8').rstrip())
        else:
            print('[INFO] no ctx_delta.txt yet')
        return 0
    if cmd == '--diff':                 do_diff(); return 0
    if cmd in ('--status', '-s'):       do_status(); return 0
    if cmd in ('--tree', '-t'):         do_tree(); return 0
    if cmd == '--hash':                 do_hash(); return 0
    if cmd in ('--git', '-g'):          do_git(); return 0
    if cmd == '--errors':               do_errors(); return 0
    if cmd == '--check-md':
        i = args.index('--check-md')
        return do_check_md(args[i+1:])
    if cmd == '--check-sections':
        i = args.index('--check-sections')
        rest = [a for a in args[i+1:] if not a.startswith('--')]
        if len(rest) >= 2:
            return do_check_sections(rest[0], rest[1])
        print("[FAIL] --check-sections needs two paths")
        return 1

    if cmd == '--file':
        i = args.index('--file')
        if i + 1 < len(args):
            rest = args[i+1:]
            do_file(rest[0], rest[1:]); return 0
        print("[FAIL] --file needs a path"); return 1
    if cmd == '--files':
        i = args.index('--files')
        names = [a for a in args[i+1:] if not a.startswith('--')]
        if names: do_files(names); return 0
        print("[FAIL] --files needs paths"); return 1

    if cmd == '--auto-verify':
        AUTO_VERIFY = True; return dispatch(args[1:]) if args[1:] else None
    if cmd == '--force':
        FORCE_APPLY = True; return dispatch(args[1:]) if args[1:] else None
    if cmd == '--fuzzy':
        FUZZY = True; return dispatch(args[1:]) if args[1:] else None
    if cmd == '--no-fuzzy':
        FUZZY = False; return dispatch(args[1:]) if args[1:] else None
    if cmd == '--dry-run':
        DRY_RUN = True; return dispatch(args[1:]) if args[1:] else None
    if cmd == '--backup':
        BACKUP = True; return dispatch(args[1:]) if args[1:] else None

    if cmd == 'dump':    do_dump(full=('--full' in args or '-f' in args)); return 0
    if cmd == 'apply':
        if not INPUT.read_text(encoding='utf-8').strip():
            print("[INFO] input.txt empty - nothing to apply."); return 0
        return do_apply()
    if cmd == 'check':    return do_check(args[1:])
    if cmd == 'verify':   return do_verify(args[1:])
    if cmd in ('find-dup', 'dup'): cmd_find_dup(args[1:]); return 0
    if cmd == 'clean':
        shutil.rmtree(WORK, ignore_errors=True)
        print(f"[CLEAN] {WORK} removed"); return 0

    print(f"[FAIL] unknown command: {cmd}")
    print("usage: python run.py [--version|--init|--capabilities|--status|"
          "--tree|--hash|--git|--file X|--files ...|--errors|dump [--full]|"
          "check|verify|find-dup|apply|clean]")
    return 1


def main():
    global AUTO_VERIFY, FORCE_APPLY, FUZZY, DRY_RUN, BACKUP
    WORK.mkdir(parents=True, exist_ok=True)
    if not INPUT.exists():
        INPUT.write_text('', encoding='utf-8')

    args = sys.argv[1:]
    if not args:
        cmds = read_cmd_directive_only()
        if cmds: args = cmds

    if args:
        if '--auto-verify' in args: AUTO_VERIFY = True
        if '--force' in args: FORCE_APPLY = True
        if '--fuzzy' in args: FUZZY = True
        if '--no-fuzzy' in args: FUZZY = False
        if '--dry-run' in args: DRY_RUN = True
        if '--backup' in args: BACKUP = True
        return dispatch(args)

    if INPUT.read_text(encoding='utf-8').strip():
        return do_apply()
    do_dump()
    return 0


if __name__ == '__main__':
    sys.exit(main())