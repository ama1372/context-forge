"""Finalize v1.1.4 (tracker + ADR-15) and v1.1.5 (embed run.py in Section 35).

Idempotent: safe to run more than once.
"""
import io
import re
import sys

DOC = 'PROJECT_CONTEXT.en.md'
SRC = 'run.py'

try:
    doc = io.open(DOC, 'r', encoding='utf-8', newline='').read()
    src = io.open(SRC, 'r', encoding='utf-8', newline='').read()
except IOError as e:
    print('FAIL: read: %s' % e)
    sys.exit(1)

changed = 0

# --- 1. Session Tracker: replace any v1.1.x-en tracker block ---
st_pat = re.compile(
    r'\| \*\*Last safe tag\*\* \| `[^`]+` \|'
    r'.*?'
    r'\| \*\*Open issues\*\* \|[^\n]*\n',
    re.DOTALL,
)
new_st = (
    '| **Last safe tag** | `v1.1.6-en` |\n'
    '| **Last commit** | after v1.1.6 patch |\n'
    '| **Last work** | v1.1.4-v1.1.6: single-document policy + embedded run.py in Section 35 |\n'
    '| **Next step** | First real test-project - end-to-end cycle with a small CLI |\n'
    '| **Current phase** | v1.1.6 - one-file distribution complete |\n'
    '| **Completion** | 100% EN (single self-contained rule doc) |\n'
    '| **Last error** | none |\n'
    '| **Open issues** | First real test-project; README.fa.md review |\n'
)
st_m = st_pat.search(doc)
if st_m:
    doc = doc[:st_m.start()] + new_st + doc[st_m.end():]
    print('OK: Session Tracker updated')
    changed += 1
else:
    print('WARN: Session Tracker pattern not found - skipped')

# --- 2. ADR-15 after ADR-14 ---
adr15_text = (
    '\n**ADR-15: Single-document policy - no translated rule documents (Section 33)**\n'
    '\n'
    '- **Decision:** `PROJECT_CONTEXT.en.md` is the only rule document. '
    'Translated rule documents (e.g. `PROJECT_CONTEXT.fa.md`) are **not maintained**. '
    'Only READMEs may be translated.\n'
    '- **Reason:** a translated rule document drifts out of sync within two patches; '
    'the reply-language is already handled by Section 0-C-9. Maintaining two rule '
    'documents duplicates effort for no benefit.\n'
    '- **Alternatives:** maintain a Persian rule document in parallel '
    '(rejected - proven drift in this project); auto-generate translations on every '
    'patch (rejected - token-heavy, fragile).\n'
)
if '**ADR-15:' in doc:
    print('SKIP: ADR-15 already present')
else:
    adr14_pat = re.compile(
        r'\*\*ADR-14:[^\n]*\n(?:[^\n]*\n)*?(?=\n\*\*ADR-15:|\n## |\Z)'
    )
    adr14_m = adr14_pat.search(doc)
    if adr14_m:
        insert_at = adr14_m.end()
        doc = doc[:insert_at].rstrip() + '\n' + adr15_text + doc[insert_at:]
        print('OK: ADR-15 inserted after ADR-14')
        changed += 1
    else:
        print('WARN: ADR-14 not found - ADR-15 skipped')

# --- 3. Embed run.py in Section 35 ---
m35 = re.search(r'^## Section 35\b.*$', doc, re.M)
m36 = re.search(r'^## Section 36\b.*$', doc, re.M)

if not m35:
    print('WARN: Section 35 header not found - embed skipped')
elif not m36:
    print('WARN: Section 36 header not found - embed skipped')
elif m36.start() <= m35.start():
    print('WARN: Section 36 before Section 35 - embed skipped')
elif 'Full `run.py` source (bootstrap)' in doc[m35.start():m36.start()]:
    print('SKIP: run.py already embedded in Section 35')
else:
    new_sec = (
        '## Section 35 - Full `run.py` source (bootstrap)\n'
        '\n'
        '> **One-file distribution.** This section contains the entire `run.py`. '
        'A newcomer who only has this document can be bootstrapped by an AI that '
        'emits the block below as `===== CREATE: run.py =====` inside `input.txt`.\n'
        '\n'
        '> **Never hand-copy this block.** Always let the AI emit it as a CREATE '
        'patch, so the protocol (Section 0-C-10) is respected.\n'
        '\n'
        '> **Mature projects:** Section 35 is only needed once. If the document '
        'feels too large for your chat, trim this section from your local copy '
        'after `run.py` exists. The rest of the document is unaffected.\n'
        '\n'
        '`````python\n'
        + src.rstrip('\n') + '\n'
        '`````\n'
        '\n'
        '### 35-1. Bootstrap procedure (what the AI does)\n'
        '\n'
        '1. Read the code block above.\n'
        '2. Emit it as a `===== CREATE: run.py =====` patch inside `input.txt`.\n'
        '3. Add `#@COMMIT: bootstrap run.py` and `#@TAG: bootstrap-runpy-ok` at the top.\n'
        '4. The user saves the block as `run.py` and runs `python run.py --init`.\n'
        '\n'
        '### 35-2. Bootstrap procedure (what the user does)\n'
        '\n'
        '1. Save the AI\'s block into a file called `run.py` in the project '
        'folder. This is the only manual save in the entire protocol - it '
        'happens once, before `input.txt` exists.\n'
        '2. Run `python run.py --init`.\n'
        '3. Done. From here on, follow Section 0-C-10-A: paste, run, send.\n'
        '\n'
        '---\n'
        '\n'
    )
    doc = doc[:m35.start()] + new_sec + doc[m36.start():]
    print('OK: run.py embedded in Section 35 (%d chars)' % len(src))
    changed += 1

if changed:
    io.open(DOC, 'w', encoding='utf-8', newline='').write(doc)
    print('OK: doc written (%d chars total)' % len(doc))
else:
    print('INFO: nothing changed')