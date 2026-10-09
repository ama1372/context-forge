import io, re, sys

DOC = 'PROJECT_CONTEXT.en.md'
SRC = 'run.py'

try:
    doc = io.open(DOC, 'r', encoding='utf-8', newline='').read()
    src = io.open(SRC, 'r', encoding='utf-8', newline='').read()
except IOError as e:
    print('FAIL: read: %s' % e); sys.exit(1)

changed = []

def sections(d):
    return sorted(set(re.findall(r'^## Section ([0-9][0-9A-Za-z\-]*)', d, re.M)))

print('Sections before: %s' % sections(doc))
print('ADRs before: %s' % sorted({int(m.group(1)) for m in re.finditer(r'\*\*ADR-(\d+):', doc)}))
print()

# (1) Fix 10-3..10-7 if corrupted
m103 = re.search(r'^### 10-3\. Update pattern\s*$', doc, re.M)
if m103:
    after = doc[m103.end():]
    mnext = re.search(r'^(?:### 13-2|## Section 1[1-3])\b', after, re.M)
    if mnext:
        end_pos = m103.end() + mnext.start()
        span = doc[m103.end():end_pos]
        if 'v1.1.6-en' in span and '<<<REPLACE>>>' not in span:
            fixed = '''

    ===== FILE: PROJECT_CONTEXT.md =====
    <<<FIND>>>
    ## Section 13 — Session Tracker

    ### 13-1. Session Tracker
    | Field | Value |
    |-------|-------|
    | **Last safe tag** | `step-XX-ok` |
    | **Last work** | <previous> |
    | **Next step** | <previous> |
    <<<REPLACE>>>
    ### 13-1. Session Tracker
    | Field | Value |
    |-------|-------|
    | **Last safe tag** | `step-YY-ok` |
    | **Last work** | <new> |
    | **Next step** | <new> |
    <<<END>>>

### 10-4. If you forget

The new AI doesn't know where we are, the user must re-explain from scratch, wasted time.

### 10-5. Golden rule

> **Every AI message = one code patch + one context patch.**
> If the context patch is missing, the message is incomplete.

### 10-6. CTX-DELTA, the anti-amnesia mechanism

Real problem: even with strong emphasis, the AI forgets to update the context in the message.

Solution: at the end of every message, the AI must write this block:

    [CTX-DELTA]
    TAG: step-XX-ok
    WORK: <one line describing what was done>
    NEXT: <one line describing the next step>
    ROADMAP:
      1. <step after the next>
      2. <step after that>
      3. <...>
    FILES: <list of changed files>
    [/CTX-DELTA]

**Hard rules:**

- Always at the end of the message.
- **Always include NEXT**, never leave it blank.
- **Always include ROADMAP**, at least 2 future steps. Even if the project is ending, write `ROADMAP: (none, release complete)`.
- Always list FILES, even if empty, write `FILES: (none)`.
- Big change: also update the context paragraphs.
- Small change: CTX-DELTA alone is enough.

**Why ROADMAP is mandatory:** the next chat may open with only this block. If it contains only `NEXT`, the AI after the next message loses the trail again. With a 3-step ROADMAP, three consecutive chats can bootstrap cleanly without ever asking the user "where were we?". This is the whole point of the anti-amnesia design, it must survive more than one message.

**What the AI must never do:**

- Never write `NEXT: (unspecified)`, if you don't know, guess a plausible next step and mark it with `?`.
- Never skip ROADMAP because "it's just a small patch".
- Never put the ROADMAP in prose instead of the block, `run.py` reads the block, not your prose.

**Benefits:**

- If the AI forgets the main context, this block is a lifesaver.
- The user sees at a glance whether the AI is working properly.
- In a new chat, CTX-DELTA alone can bootstrap continuation.
- `run.py` saves this block automatically to `_work/ctx_delta.txt` after every successful apply, so the user can retrieve it with `python run.py --ctx` at any time.

### 10-7. Complete AI message pattern

Every AI message has exactly four parts:

1. **One-line summary.**
2. **One `input.txt` block**, starting with `#@COMMIT:` and `#@TAG:`, then optionally `#@PUSH:`, `#@NEXT:`, `#@ROADMAP:`, `#@POST:`, `#@NEED:`, then the patch blocks.
3. **`[CTX-DELTA]` block**, with TAG, WORK, NEXT, ROADMAP, FILES.
4. **End-of-message reminder**, "If there was an error: ...".

**That is it. Nothing else.**

- No test command outside the block (it goes in `#@POST:`).
- No commit command outside the block (it goes in `#@COMMIT:`).
- No push command outside the block (it goes in `#@PUSH:`).
- No "check these after apply" list.
- No post-apply checklist the user must run manually.
- Optional one-line hints allowed, clearly marked optional.

**History note:** before run.py v1.0+, "test" and "commit" were separate shell commands in chat. That is superseded. The directives inside `input.txt` carry the entire workflow.

'''
            doc = doc[:m103.end()] + fixed + doc[end_pos:]
            changed.append('10-3 through 10-7 restored')

# (2) Insert Section 11 if missing
if not re.search(r'^## Section 11 [\-\u2014]', doc, re.M):
    anchor = re.search(r'^## Section 1[2-9]\b', doc, re.M)
    if anchor:
        sec11 = '''## Section 11 - The Big-Context Problem (solution)

### 11-1. The problem

If this document reaches 5000 lines, sending it every time itself burns tokens.

### 11-2. Solution: three layers

**Layer 1 - main document (this file):**
- This document is complete and stable.
- Only Sections 2, 13, 15, 16 change.
- Sending it once is enough.

**Layer 2 - separate CHANGELOG.md:**
- Full history of changes.
- The AI reads it only when needed.
- Included in `_work/output.txt`.

**Layer 3 - ADR.md (Architecture Decision Records):**
- Past architectural decisions.
- Only for a new AI that wants to understand the "whys".

### 11-3. Practical pattern

**Every new chat:**

    1. This document (PROJECT_CONTEXT.md)
    2. CHANGELOG.md (last 100 lines)
    3. python run.py --status
    4. If needed: python run.py --all

**Savings:** about 30% tokens compared to sending everything.

### 11-4. How big should the document be?

- Minimum: 500 lines (start).
- Ideal: 2000-3000 lines.
- Maximum: 5000 lines (beyond this, it burns tokens).

**If it grows past that:**
- Historical sections -> CHANGELOG.md
- ADRs -> ADR.md
- Only active rules stay in the main document.

---

'''
        doc = doc[:anchor.start()] + sec11 + doc[anchor.start():]
        changed.append('Section 11 inserted')

# (3) Insert Section 12 if missing
if not re.search(r'^## Section 12 [\-\u2014]', doc, re.M):
    anchor = re.search(r'^## Section 1[3-9]\b', doc, re.M)
    if anchor:
        sec12 = '''## Section 12 - Special Characters & Escape

### 12-1. The problem

Triple backticks, asterisks, and other markdown characters cause rendering issues.

### 12-2. Solution: the markers rule

**1. Parser markers (FILE, FIND, REPLACE, END, CONTENT, RUN) must never appear in a patch body as real markers.**

**2. If you must show a marker:**

- Wrap in quotes: "the END marker"
- Internal space: `< END >`
- Indent by 4 spaces: `    ===== FILE =====` (parser only sees column zero)

**3. If the file content contains triple backticks:**

Use the FIND / REPLACE blocks with no outer markdown.

### 12-3. Safe markdown template

If the patch contains markdown, always use the `===== FILE =====` shell, not triple backticks.

### 12-4. Pre-send test

Before sending a message, check:

- No unmatched triple-backtick fence in the text.
- No `===== ` inside a patch body.
- No `<<<` without a matching `>>>`.

### 12-5. If `run.py` reports a parser error

Read `_work/output.txt`. The `[FAIL]` line says exactly where and which block. `SUGGEST` shows the nearest text. If it is a parser error (not an anchor error), check `_work/input.txt` by hand, probably a marker at column zero inside content.

---

### 12-7. Never nest fences in the English document

> **New red line for `PROJECT_CONTEXT.en.md` itself.**

Forbidden: any triple-backtick or multi-backtick fence nested inside another fence in this document.

Reason: markdown collapses nested fences, the outer fence closes at the first inner fence whose length is greater or equal. The remaining content is then parsed as normal markdown, and backslashes and dollar signs and asterisks get eaten.

Rule: every embedded example inside this document uses 4-space indentation only, never a fence inside a fence.

If you must show a markdown fence as content, show it as a line of backticks with 4-space indent, not as a real fence.

### 12-8. Never nest fences, and how `--check-md` catches it

The single most painful bug in this project's history came from nested fences. When you embed a fence inside another fence, markdown closes the outer fence early and the content silently corrupts.

**Prevention:**

- In this document: never use fences inside fences (Section 12-7). Use 4-space indentation.
- In `input.txt` patches: the outer fence should be 4 or 5 backticks and the content must not contain a fence of equal or greater length at column zero. Indent embedded fences by 4 spaces.

**Detection:**

    python run.py --check-md

Scans every `.md` file in the project. Reports any nested or unclosed fence with file:line. Zero output beyond `[OK]` means the document is clean.

Use it before committing any change to a `.md` file.

### 12-6. Golden rule for the AI: `input.txt` output format

Every time the AI wants to give a patch, it must give the entire `input.txt` in a single code block, not piecemeal, not with prose in between.

**Hard rules:**

1. One single block from `===== FILE` to the last `<<<END>>>`.
2. If the content contains triple backticks, use four backticks for the outer fence.
3. No prose between blocks. If an explanation is needed, before or after the block, not inside.
4. If the anchor or CONTENT is very large, split into two separate blocks, but each block must be complete and self-contained.
5. No parser markers should appear in prose outside a block.

---

'''
        doc = doc[:anchor.start()] + sec12 + doc[anchor.start():]
        changed.append('Section 12 inserted')

# (4) Ensure Section 13 header + real 13-1 exist
if not re.search(r'^## Section 13 [\-\u2014] Session Tracker', doc, re.M):
    anchor = re.search(r'^### 13-2\. Update', doc, re.M)
    if anchor:
        sec13 = '''## Section 13 - Session Tracker

> **Note:** This section is for your real project. **Send the document as a template, this section is filled in** with the project's real state.
> If using the document as a template (new project), **clear this section** and fill it in again.

### 13-1. Session Tracker

| Field | Value |
|-------|-------|
| **Last safe tag** | `v1.2.0-en` |
| **Last commit** | after v1.2.0 patch |
| **Last work** | v1.2.0: doc structure fixed, run.py re-embedded |
| **Next step** | First real test-project, end-to-end cycle with a small CLI |
| **Current phase** | v1.2.0, structurally complete |
| **Completion** | 100% EN (single self-contained rule doc) |
| **Last error** | none |
| **Open issues** | First real test-project; README.fa.md review |

'''
        doc = doc[:anchor.start()] + sec13 + doc[anchor.start():]
        changed.append('Section 13 header + 13-1 inserted')

# (5) Re-embed run.py from disk
m35 = re.search(r'^## Section 35\b.*$', doc, re.M)
m36 = re.search(r'^## Section 36\b.*$', doc, re.M)
if m35 and m36 and m35.start() < m36.start():
    vm = re.search(r'VERSION = "([^"]+)"', src)
    ver = vm.group(1) if vm else '?'
    new_sec35 = (
        '## Section 35 - Full `run.py` source (bootstrap)\n'
        '\n'
        '> **One-file distribution.** This section contains the entire `run.py`. '
        'A newcomer who only has this document can be bootstrapped by an AI that '
        'emits the block below as a CREATE patch inside `input.txt`.\n'
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
        '2. Emit it as a CREATE patch inside `input.txt`.\n'
        '3. Add `#@COMMIT: bootstrap run.py` and `#@TAG: bootstrap-runpy-ok` at the top.\n'
        '4. The user saves the block as `run.py` and runs `python run.py --init`.\n'
        '\n'
        '### 35-2. Bootstrap procedure (what the user does)\n'
        '\n'
        '1. Save the AI block into a file called `run.py` in the project '
        'folder. This is the only manual save in the entire protocol, it '
        'happens once, before `input.txt` exists.\n'
        '2. Run `python run.py --init`.\n'
        '3. Done. From here on, follow Section 0-C-10-A: paste, run, send.\n'
        '\n'
        '---\n'
        '\n'
    )
    doc = doc[:m35.start()] + new_sec35 + doc[m36.start():]
    changed.append('Section 35 re-embedded (v%s)' % ver)

# (6) TOC fixes
toc_pairs = [
    ('- **Section 33** - Localization Guide',
     '- **Section 33** - Localization Policy (single document, multi-language replies)'),
    ('- **Section 33** \u2014 Localization Guide',
     '- **Section 33** \u2014 Localization Policy (single document, multi-language replies)'),
    ('- **Section 35** - Minimal `run.py`',
     '- **Section 35** - Full `run.py` source (bootstrap)'),
    ('- **Section 35** \u2014 Minimal `run.py`',
     '- **Section 35** \u2014 Full `run.py` source (bootstrap)'),
]
for old, new in toc_pairs:
    if old in doc and new not in doc:
        doc = doc.replace(old, new)
        changed.append('TOC: %s' % new[:50])

# (7) Section 32-2 Step 3
new_32_3 = 'The full `run.py` source is embedded in Section 35 of this document. If you don\'t have `run.py` yet, ask the AI: "Bootstrap `run.py` from Section 35." The AI emits it as a CREATE patch. Save it as `run.py` in the project root.'
for old in [
    "The full `run.py` reference is in the project root. If you don't have it yet, copy it from the project you obtained this document from \u2014 or ask the AI to help you bootstrap it from Section 35.",
    "The full `run.py` reference is in the project root. If you don't have it yet, copy it from the project you obtained this document from, or ask the AI to help you bootstrap it from Section 35.",
]:
    if old in doc:
        doc = doc.replace(old, new_32_3)
        changed.append('Section 32-2 Step 3 updated')

# (8) Section 0-B
if '| PROJECT_CONTEXT.md | The constitution' in doc:
    doc = doc.replace(
        '| PROJECT_CONTEXT.md | The constitution',
        '| PROJECT_CONTEXT.en.md | The constitution')
    changed.append('Section 0-B filename updated')

io.open(DOC, 'w', encoding='utf-8', newline='').write(doc)

print('CHANGES:')
for c in changed:
    print('  - ' + c)
if not changed:
    print('  (none)')
print()
print('Sections after: %s' % sections(doc))
print('ADRs after: %s' % sorted({int(m.group(1)) for m in re.finditer(r'\*\*ADR-(\d+):', doc)}))
print()
print('OK: doc %d chars, %d lines' % (len(doc), doc.count('\n')+1))