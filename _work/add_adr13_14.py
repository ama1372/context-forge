"""Insert ADR-13 and ADR-14 before ADR-15 if not already present. Idempotent."""
import io
import re
import sys

DOC = 'PROJECT_CONTEXT.en.md'

try:
    doc = io.open(DOC, 'r', encoding='utf-8', newline='').read()
except IOError as e:
    print('FAIL: read: %s' % e)
    sys.exit(1)

adr_nums = sorted({int(m.group(1)) for m in re.finditer(r'\*\*ADR-(\d+):', doc)})
print('INFO: ADR numbers present before: %s' % adr_nums)

need13 = 13 not in adr_nums
need14 = 14 not in adr_nums

if not need13 and not need14:
    print('SKIP: ADR-13 and ADR-14 already present')
    sys.exit(0)

anchor = re.search(r'\*\*ADR-15:', doc)
if not anchor:
    anchor = re.search(r'^## Section 14\b', doc, re.M)
if not anchor:
    print('FAIL: no anchor found (neither ADR-15 nor Section 14)')
    sys.exit(1)

add13 = (
    '**ADR-13: The user has exactly three actions (Section 0-C-10-A)**\n'
    '\n'
    '- **Decision:** the user only (1) pastes into `input.txt`, (2) runs '
    '`python run.py`, (3) sends `output.txt`. No other step is allowed.\n'
    '- **Reason:** every extra step is a chance for error, a token cost, and a '
    'break in the protocol. Verification, commits, pushes, and context updates '
    'belong inside `input.txt` as directives.\n'
    '- **Alternatives:** allow the AI to add per-message checklists '
    '(rejected - that is exactly the pattern that was silently pushing work '
    'back onto the user).\n'
    '\n'
)
add14 = (
    '**ADR-14: Verification runs inside `input.txt` via `#@POST:` - '
    'language-agnostic (Section 4-19)**\n'
    '\n'
    '- **Decision:** the language-specific build/test commands live in '
    '`_work/config.json`, triggered by `#@POST: check` / `#@POST: verify` '
    'inside the patch. The user still runs only `python run.py`.\n'
    '- **Reason:** this makes the same protocol work for Rust, Python, Node, '
    'Go, and any other language without ever leaving `input.txt`.\n'
    '- **Alternatives:** a different workflow per language (rejected - the '
    'protocol must be universal); asking the user to run the language\'s '
    'native command (rejected - violates Section 0-C-10-A).\n'
    '\n'
)

insert_at = anchor.start()
prefix = ''
if need13: prefix += add13
if need14: prefix += add14

doc = doc[:insert_at] + prefix + doc[insert_at:]
io.open(DOC, 'w', encoding='utf-8', newline='').write(doc)

adr_nums_after = sorted({int(m.group(1)) for m in re.finditer(r'\*\*ADR-(\d+):', doc)})
print('OK: ADR numbers present after: %s' % adr_nums_after)
print('OK: added ADR-13=%s ADR-14=%s' % (need13, need14))
print('OK: doc written (%d chars)' % len(doc))