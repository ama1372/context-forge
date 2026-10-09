"""Add ADR-15 before Section 14 if not already present. Idempotent."""
import io
import re
import sys

DOC = 'PROJECT_CONTEXT.en.md'

try:
    doc = io.open(DOC, 'r', encoding='utf-8', newline='').read()
except IOError as e:
    print('FAIL: read: %s' % e)
    sys.exit(1)

if '**ADR-15:' in doc:
    print('SKIP: ADR-15 already present')
    sys.exit(0)

# Find the highest ADR-N number currently in the document
adr_nums = [int(m.group(1)) for m in re.finditer(r'\*\*ADR-(\d+):', doc)]
print('INFO: ADR numbers present: %s' % (sorted(set(adr_nums)) or '(none)'))

# Anchor: insert right before Section 14
sec14 = re.search(r'^## Section 14\b', doc, re.M)
if not sec14:
    print('FAIL: Section 14 not found')
    sys.exit(1)

adr15_text = (
    '**ADR-15: Single-document policy - no translated rule documents (Section 33)**\n'
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
    '\n'
)

insert_at = sec14.start()
doc = doc[:insert_at].rstrip() + '\n\n' + adr15_text + doc[insert_at:]
io.open(DOC, 'w', encoding='utf-8', newline='').write(doc)
print('OK: ADR-15 inserted before Section 14')
print('OK: doc written (%d chars)' % len(doc))