#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# run.py - single command project tool  (v2.0)
#
# استفاده‌ی پایه:
#   python run.py                 smart: input empty -> dump / input full -> apply
#
# فلگ‌های خواندن (بدون apply):
#   python run.py --status        خلاصه‌ی خیلی کوچک (شروع هر چت)
#   python run.py --tree          فقط درخت فایل‌ها
#   python run.py --hash          hash همه‌ی فایل‌ها
#   python run.py --git           git log + tag + status
#   python run.py --file X        محتوای یک فایل + hash
#   python run.py --files X Y Z   چند فایل مشخص
#   python run.py --errors        فقط خطاهای آخرین اجرا
#
# فلگ‌های رفتاری:
#   python run.py --auto-verify   hash mismatch → رد خودکار
#   python run.py --force         hash mismatch → اعمال بدون پرسش
#
# دستورهای صریح:
#   python run.py dump [--full]   dump کامل یا incremental
#   python run.py apply           اعمال پچ‌های input.txt
#   python run.py clean           پاک‌کردن _work/

import difflib, hashlib, json, os, re, secrets, shutil, subprocess, sys
from datetime import datetime
from pathlib import Path

WORK = Path('_work')
INPUT = WORK / 'input.txt'
OUTPUT = WORK / 'output.txt'
APPLIED = WORK / 'applied'
CACHE = WORK / 'cache.json'

SKIP_DIRS = {'target', '.git', '__pycache__', '.idea', '.vscode',
             'node_modules', 'data', 'assets', '_work', '_ctx',
             '.venv', 'venv', 'dist', 'build', '.pytest_cache'}
SKIP_EXTS = {'.exe', '.dll', '.pdb', '.zip', '.ttf', '.otf', '.png',
             '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.lock', '.bin',
             '.so', '.dylib', '.rlib', '.rmeta', '.pt', '.pkl', '.pyc',
             '.whl', '.tar', '.gz', '.7z', '.rar'}
SKIP_NAMES = {'run.py'}
MAX_SIZE = 2 * 1024 * 1024

HEADER_RE = re.compile(r'^={3,}\s*(FILE|CREATE|DELETE|CMD|MKDIR)\s*:\s*(.+?)\s*={3,}\s*$')
FIND, REPLACE, CONTENT, END = '<<<FIND>>>', '<<<REPLACE>>>', '<<<CONTENT>>>', '<<<END>>>'
RUN_MARKER = '<<<RUN>>>'
HASH_MARKER_RE = re.compile(r'^<<<EXPECTED_HASH>>>\s*(.+?)\s*<<<END>>>\s*$')
FENCE_RE = re.compile(r'^\s*```[a-zA-Z0-9_+\-]*\s*$')

VERSION = "3.0.0"

# فلگ‌های رفتاری (با آرگومان مقدار می‌گیرند)
AUTO_VERIFY = False
FORCE_APPLY = False


# ═══════════════════════════════════════════════════════════════════
# ابزارهای پایه
# ═══════════════════════════════════════════════════════════════════

def read(p):
    for enc in ('utf-8', 'utf-8-sig', 'cp1256', 'latin-1'):
        try:
            return p.read_text(encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    return p.read_text(encoding='latin-1', errors='replace')


def write(p, t):
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
    """seed کوتاه یونیک برای هر پیام — ضد مسدود شدن اکانت"""
    return secrets.token_hex(4)


def walk(root):
    out = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in fns:
            p = Path(dp) / fn
            if p.name in SKIP_NAMES:
                continue
            if p.suffix.lower() in SKIP_EXTS:
                continue
            try:
                if p.stat().st_size > MAX_SIZE:
                    continue
            except OSError:
                continue
            out.append(p)
    return sorted(out, key=lambda p: str(p.relative_to(root)).lower())


def load_cache():
    if CACHE.exists():
        try:
            return json.loads(CACHE.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {}


def save_cache(c):
    WORK.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(c, indent=2, ensure_ascii=False),
                     encoding='utf-8')


def strip_fences(lines):
    lines = list(lines)
    if len(lines) < 2:
        return lines
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or not FENCE_RE.match(lines[i]):
        return lines
    j = len(lines) - 1
    while j >= 0 and not lines[j].strip():
        j -= 1
    if j <= i or not FENCE_RE.match(lines[j]):
        return lines
    return lines[:i] + lines[i+1:j] + lines[j+1:]


# ═══════════════════════════════════════════════════════════════════
# پارسر
# ═══════════════════════════════════════════════════════════════════

def parse(text):
    lines = text.splitlines()
    ops, i, n = [], 0, len(lines)
    while i < n:
        m = HEADER_RE.match(lines[i])
        if not m:
            i += 1
            continue
        kind, path = m.group(1).lower(), m.group(2).strip()
        i += 1

        if kind == 'delete':
            ops.append({'kind': 'delete', 'path': path})
            continue
        if kind == 'mkdir':
            ops.append({'kind': 'mkdir', 'path': path})
            continue

        if kind == 'cmd':
            while i < n and lines[i].rstrip() != RUN_MARKER:
                if HEADER_RE.match(lines[i]):
                    break
                i += 1
            if i >= n or lines[i].rstrip() != RUN_MARKER:
                ops.append({'kind': 'cmd', 'desc': path, 'script': ''})
                continue
            i += 1
            block = []
            while i < n and lines[i].rstrip() != END:
                if HEADER_RE.match(lines[i]):
                    break
                block.append(lines[i])
                i += 1
            if i < n and lines[i].rstrip() == END:
                i += 1
            ops.append({'kind': 'cmd', 'desc': path,
                        'script': '\n'.join(block)})
            continue

        if kind == 'create':
            while i < n and lines[i].rstrip() != CONTENT:
                if HEADER_RE.match(lines[i]):
                    break
                i += 1
            if i >= n or lines[i].rstrip() != CONTENT:
                ops.append({'kind': 'create', 'path': path, 'content': ''})
                continue
            i += 1
            block = []
            while i < n and lines[i].rstrip() != END:
                if HEADER_RE.match(lines[i]):
                    break
                block.append(lines[i])
                i += 1
            if i < n and lines[i].rstrip() == END:
                i += 1
            ops.append({'kind': 'create', 'path': path,
                        'content': '\n'.join(strip_fences(block))})
            continue

        # kind == 'file' — استخراج EXPECTED_HASH اختیاری
        expected_hash = None
        j = i
        while j < n and not HEADER_RE.match(lines[j]):
            m_h = HASH_MARKER_RE.match(lines[j].strip())
            if m_h:
                expected_hash = m_h.group(1)
                break
            j += 1

        patches = []
        while i < n:
            if HEADER_RE.match(lines[i]):
                break
            if lines[i].strip().startswith('<<<EXPECTED_HASH>>>'):
                i += 1
                continue
            if lines[i].rstrip() == FIND:
                i += 1
                a = []
                while i < n and lines[i].rstrip() != REPLACE:
                    a.append(lines[i])
                    i += 1
                if i >= n or lines[i].rstrip() != REPLACE:
                    break
                i += 1
                r = []
                while i < n and lines[i].rstrip() != END:
                    r.append(lines[i])
                    i += 1
                if i < n and lines[i].rstrip() == END:
                    i += 1
                patches.append(('\n'.join(strip_fences(a)),
                                '\n'.join(strip_fences(r))))
                continue
            i += 1

        ops.append({'kind': 'file', 'path': path,
                    'patches': patches, 'hash': expected_hash})
    return ops


# ═══════════════════════════════════════════════════════════════════
# Anchor finding
# ═══════════════════════════════════════════════════════════════════

def find_exact(text, a):
    p = text.find(a)
    return (p, p + len(a), 1) if p >= 0 else None


def find_soft(text, a):
    flines = text.splitlines(keepends=True)
    alines = a.splitlines()
    while alines and not alines[-1].strip():
        alines.pop()
    if not alines:
        return None
    for lvl, tr in ((2, str.rstrip), (3, str.strip)):
        arr = [tr(x) for x in alines]
        m = len(arr)
        for s in range(len(flines) - m + 1):
            if tr(flines[s].rstrip('\n')) != arr[0]:
                continue
            ok = True
            for j in range(1, m):
                if tr(flines[s+j].rstrip('\n')) != arr[j]:
                    ok = False
                    break
            if ok:
                so = sum(len(l) for l in flines[:s])
                eo = sum(len(l) for l in flines[:s+m])
                return so, eo, lvl
    return None


def find_anchor(text, a):
    r = find_exact(text, a)
    if r:
        return r
    return find_soft(text, a)


def suggest(text, a):
    fl = text.splitlines()
    al = a.splitlines()
    while al and not al[-1].strip():
        al.pop()
    if not al or not fl:
        return None
    n = len(al)
    astr = '\n'.join(al)
    afirst = al[0].strip()
    best = (0.0, None, -1)
    for i in range(len(fl)):
        ln = fl[i].strip()
        if afirst and afirst not in ln and ln not in afirst and not ln:
            continue
        for d in (0, 1, -1, 2, -2, 3, -3):
            k = n + d
            if k <= 0 or i + k > len(fl):
                continue
            b = '\n'.join(fl[i:i+k])
            r = difflib.SequenceMatcher(None, astr, b).ratio()
            if r > best[0]:
                best = (r, b, i)
    return best if best[1] and best[0] >= 0.55 else None


# ═══════════════════════════════════════════════════════════════════
# Apply
# ═══════════════════════════════════════════════════════════════════

def apply_patch(path, patches, out):
    p = Path(path)
    if not p.exists():
        out.append(f"  [FAIL] file not found: {path}")
        return 0, len(patches), 0
    raw = read(p)
    fe = eol(raw)
    text = lf(raw)
    ok = fail = skip = 0
    for i, (a, r) in enumerate(patches, 1):
        al, rl = lf(a), lf(r)
        if not al:
            out.append(f"  [FAIL] [{i}/{len(patches)}] empty anchor")
            fail += 1
            continue
        if rl and rl in text and not find_anchor(text, al):
            out.append(f"  [SKIP] [{i}/{len(patches)}] already applied")
            skip += 1
            continue
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
                for x in blk.splitlines():
                    out.append(f"         | {x}")
                out.append("         " + "-" * 60)
            fail += 1
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


def do_apply():
    content = INPUT.read_text(encoding='utf-8-sig')
    patch_id = None
    if content:
        first_line = content.split('\n', 1)[0].strip()
        m = re.match(r'^#@ID:\s*(\d+)', first_line)
        if m:
            patch_id = int(m.group(1))
            content = content.split('\n', 1)[1] if '\n' in content else ''
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
    out = [f"# MSG-SEED: {seed}",
           f"# PATCH_ID: {patch_id}",
           "[APPLY]",
           ""]
    if not ops:
        out.append("[FAIL] no valid patches")
        write(OUTPUT, '\n'.join(out))
        print('\n'.join(out))
        return 2

    ok = fail = skip = 0
    for op in ops:
        kind = op['kind']

        if kind == 'file':
            out.append(f"[P{patch_id}] [EDIT] {op['path']}")
            if not op['patches']:
                out.append("  [WARN] empty FILE block")
                continue

            # ─── Hash verification ───
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
                            skip += 1
                            continue
                        if not FORCE_APPLY:
                            out.append("  [WARN] hash mismatch - applying anyway")
                            out.append("         (use --auto-verify to reject, --force to silence)")
                        else:
                            out.append("  [INFO] --force: ignoring mismatch")

            a, b, s = apply_patch(op['path'], op['patches'], out)
            ok += a
            fail += b
            skip += s

        elif kind == 'create':
            p = Path(op['path'])
            existed = p.exists()
            out.append(f"[P{patch_id}] [NEW]  {op['path']}")
            write(p, lf(op['content']))
            out.append(f"  [OK]   {'updated' if existed else 'created'} ({len(op['content'])} chars)")
            ok += 1

        elif kind == 'delete':
            p = Path(op['path'])
            out.append(f"[P{patch_id}] [DEL]  {op['path']}")
            if p.exists():
                p.unlink()
            ok += 1

        elif kind == 'mkdir':
            p = Path(op['path'])
            out.append(f"[P{patch_id}] [MKDIR] {op['path']}")
            p.mkdir(parents=True, exist_ok=True)
            out.append("  [OK]   created")
            ok += 1

        elif kind == 'cmd':
            out.append(f"[P{patch_id}] [CMD]  {op['desc']}")
            script = op['script']
            if not script.strip():
                out.append("  [WARN] empty script")
                continue
            try:
                r = subprocess.run(
                    ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass',
                     '-Command', script],
                    capture_output=True, text=True, encoding='utf-8',
                    errors='replace', timeout=900
                )
                if r.stdout:
                    for ln in r.stdout.rstrip().splitlines():
                        out.append(f"  | {ln}")
                if r.stderr:
                    for ln in r.stderr.rstrip().splitlines():
                        out.append(f"  ! {ln}")
                if r.returncode == 0:
                    out.append("  [OK]   exit 0")
                    ok += 1
                else:
                    out.append(f"  [FAIL] exit {r.returncode}")
                    fail += 1
            except subprocess.TimeoutExpired:
                out.append("  [FAIL] timeout 900s")
                fail += 1
            except Exception as e:
                out.append(f"  [FAIL] {e}")
                fail += 1

    out.append("")
    out.append("=" * 60)
    out.append(f"PATCH_ID: {patch_id}  |  OK: {ok}  |  SKIP: {skip}  |  FAIL: {fail}")

    # ─── همیشه بایگانی + خالی کردن input.txt ───
    APPLIED.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    arch = APPLIED / f'P{patch_id:04d}-{ts}.txt'
    if INPUT.exists():
        try:
            INPUT.rename(arch)
        except Exception:
            shutil.copy(INPUT, arch)
    INPUT.write_text('', encoding='utf-8')
    out.append("")
    out.append(f"[ARCH] {arch}")
    if fail == 0:
        out.append("       input.txt emptied - ready for next patch")
    else:
        out.append(f"       {fail} patch(es) FAILED")
        out.append("       input.txt emptied anyway")
        out.append("       >>> FAILED parts shown above <<<")

    # ─── git commit اگر apply موفق بود ───
    if fail == 0:
        try:
            r0 = subprocess.run(['git', 'rev-parse', '--is-inside-work-tree'],
                                capture_output=True, text=True)
            if r0.returncode == 0 and r0.stdout.strip() == 'true':
                msg = f"patch {patch_id}: {ts}"
                subprocess.run(['git', 'add', '-A'], capture_output=True)
                r1 = subprocess.run(['git', 'commit', '-m', msg],
                                    capture_output=True, text=True)
                out.append("")
                if r1.returncode == 0:
                    out.append(f"[GIT] commit: {msg}")
                else:
                    combined = (r1.stdout or '') + (r1.stderr or '')
                    if 'nothing to commit' in combined:
                        out.append("[GIT] nothing to commit")
                    else:
                        out.append(f"[GIT] failed: {r1.stderr.strip()[:200]}")
        except FileNotFoundError:
            out.append("")
            out.append("[GIT] git not installed")
        except Exception as e:
            out.append("")
            out.append(f"[GIT] error: {e}")

    txt = '\n'.join(out)
    write(OUTPUT, txt)
    print(txt)
    return 0 if fail == 0 else 2


# ═══════════════════════════════════════════════════════════════════
# Dump
# ═══════════════════════════════════════════════════════════════════

def do_dump(full=False):
    root = Path('.').resolve()
    cache = load_cache()
    files = walk(root)
    manifest = []
    changed_files = []
    for p in files:
        rel = str(p.relative_to(root))
        h = hash_file(p)
        old = cache.get(rel, {}).get('hash')
        is_changed = (old != h)
        manifest.append((rel, is_changed))
        if is_changed or full:
            changed_files.append(p)
        cache[rel] = {'hash': h,
                      'last_seen': datetime.now().isoformat(timespec='seconds')}
    save_cache(cache)

    seed = msg_seed()
    L = [f"# MSG-SEED: {seed}",
         f"# PROJECT DUMP - {datetime.now().isoformat(timespec='seconds')}",
         f"# mode: {'full' if full else 'incremental'}",
         f"# {len(files)} files total, {len(changed_files)} included",
         "",
         "=" * 72,
         "MANIFEST",
         "=" * 72]
    for rel, ch in manifest:
        mark = "[CHANGED]" if ch else "         "
        L.append(f"{mark} {rel}")
    L.append("")

    if changed_files:
        L.append("=" * 72)
        L.append(f"CONTENT ({len(changed_files)} files)")
        L.append("=" * 72)
        for p in changed_files:
            rel = p.relative_to(root)
            L.append("")
            L.append("-" * 72)
            L.append(f"FILE: {rel}")
            L.append(f"HASH: {hash_file(p)}")
            L.append("-" * 72)
            L.append(read(p).rstrip())
    else:
        L.append("(no changed files)")
        L.append("")

    body = '\n'.join(L)
    new_hash = hashlib.sha256(body.encode('utf-8')).hexdigest()[:16]

    if OUTPUT.exists() and not full:
        old = read(OUTPUT)
        if f"# content_hash: {new_hash}" in old:
            print("[DUPLICATE] output.txt identical to previous run")
            print("            -> DO NOT send to assistant")
            print("            (nothing changed since last dump)")
            return

    L.insert(2, f"# content_hash: {new_hash}")
    txt = '\n'.join(L)
    write(OUTPUT, txt)
    print(f"[DUMP] {OUTPUT}")
    print(f"       mode: {'full' if full else 'incremental'}")
    print(f"       {len(files)} files total  |  {len(changed_files)} included")
    print(f"       size: {OUTPUT.stat().st_size:,} bytes")
    print()
    print(f"[NEW] send this file to assistant: {OUTPUT}")


# ═══════════════════════════════════════════════════════════════════
# فلگ‌های خواندن
# ═══════════════════════════════════════════════════════════════════

def do_status():
    root = Path('.').resolve()
    out = [f"PROJECT: {root.name}"]
    try:
        r = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0 and r.stdout.strip():
            out.append(f"LAST TAG: {r.stdout.strip()}")
    except Exception:
        pass
    try:
        r = subprocess.run(['git', 'status', '--short'],
                           capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            files = [ln[3:].strip() for ln in r.stdout.splitlines() if ln.strip()]
            out.append(f"MODIFIED: {len(files)} files")
            for f in files[:20]:
                out.append(f"  {f}")
    except Exception:
        pass
    files = walk(root)
    out.append(f"TOTAL FILES: {len(files)}")
    # آخرین خطای dump (اگر هست)
    if OUTPUT.exists():
        try:
            txt = read(OUTPUT)
            for ln in txt.splitlines()[:40]:
                if 'FAIL' in ln:
                    out.append(ln.strip())
                    break
        except Exception:
            pass
    print('\n'.join(out))


def do_tree():
    root = Path('.').resolve()
    print(f"PROJECT: {root.name}")
    for p in walk(root):
        rel = p.relative_to(root)
        depth = len(rel.parts) - 1
        indent = '  ' * depth
        print(f"{indent}{rel.name}")


def do_hash():
    root = Path('.').resolve()
    for p in walk(root):
        rel = p.relative_to(root)
        print(f"{hash_file(p)}  {rel}")


def do_git():
    cmds = [
        ['git', 'log', '--oneline', '-10'],
        ['git', 'tag'],
        ['git', 'status', '--short'],
    ]
    for cmd in cmds:
        try:
            print(f"$ {' '.join(cmd)}")
            r = subprocess.run(cmd, capture_output=True, text=True,
                               encoding='utf-8', errors='replace', timeout=10)
            print(r.stdout)
        except Exception as e:
            print(f"[WARN] {e}")


def do_file(name):
    p = Path(name)
    if not p.is_absolute():
        p = Path('.').resolve() / name
    if not p.exists():
        print(f"[FAIL] file not found: {name}")
        return
    print(f"FILE: {name}")
    print(f"HASH: {hash_file(p)}")
    print(f"SIZE: {p.stat().st_size} bytes")
    print("---CONTENT---")
    print(read(p))


def do_files(names):
    for i, name in enumerate(names):
        if i > 0:
            print()
        do_file(name)


def do_errors():
    if not OUTPUT.exists():
        print("[INFO] no output.txt yet")
        return
    txt = read(OUTPUT)
    found = False
    for ln in txt.splitlines():
        if 'FAIL' in ln or '[FAIL]' in ln:
            print(ln)
            found = True
    if not found:
        print("[INFO] no errors in last output.txt")


# ═══════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════

def main():
    global AUTO_VERIFY, FORCE_APPLY
    WORK.mkdir(parents=True, exist_ok=True)
    if not INPUT.exists():
        INPUT.write_text('', encoding='utf-8')

    args = sys.argv[1:]
    if args:
        if '--version' in args or '-v' in args:
            print(f"run.py v{VERSION}")
            return 0
        # فلگ‌های خواندن (بدون apply)
        if '--status' in args or '-s' in args:
            do_status()
            return 0
        if '--tree' in args or '-t' in args:
            do_tree()
            return 0
        if '--hash' in args:
            do_hash()
            return 0
        if '--git' in args or '-g' in args:
            do_git()
            return 0
        if '--errors' in args:
            do_errors()
            return 0
        if '--file' in args:
            i = args.index('--file')
            if i + 1 < len(args):
                do_file(args[i + 1])
                return 0
            print("[FAIL] --file needs a path")
            return 1
        if '--files' in args:
            i = args.index('--files')
            names = [a for a in args[i+1:] if not a.startswith('--')]
            if names:
                do_files(names)
                return 0
            print("[FAIL] --files needs paths")
            return 1

        # فلگ‌های رفتاری
        if '--auto-verify' in args:
            AUTO_VERIFY = True
        if '--force' in args:
            FORCE_APPLY = True

        # دستورهای صریح
        cmd = args[0]
        if cmd == 'dump':
            do_dump(full=('--full' in args or '-f' in args))
            return 0
        if cmd == 'apply':
            if not INPUT.read_text(encoding='utf-8').strip():
                print("[INFO] input.txt empty - nothing to apply.")
                return 0
            return do_apply()
        if cmd == 'clean':
            shutil.rmtree(WORK, ignore_errors=True)
            print(f"[CLEAN] {WORK} removed")
            return 0
        if cmd not in ('--auto-verify', '--force'):
            print(f"[FAIL] unknown command: {cmd}")
            print("usage: python run.py [--status|--tree|--hash|--git|--file X|--files X Y|--errors|dump [--full]|apply|clean|--auto-verify|--force]")
            return 1

    # حالت هوشمند بدون آرگومان
    if INPUT.read_text(encoding='utf-8').strip():
        return do_apply()
    do_dump()
    return 0


if __name__ == '__main__':
    sys.exit(main())