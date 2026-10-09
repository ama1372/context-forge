# PROJECT_CONTEXT.md — Universal template for AI-assisted coding

> One document. Send it once per new chat. Works with any language, any AI.
> If you only have this file, the AI guides you through setup.

<!-- AUTO:START -->
## Last patch (auto - do not edit)

| Field | Value |
|-------|-------|
| Last patch | P36 |
| Last commit | `54e33dc` |
| Time | 2026-10-09 14:10 |
| MSG-SEED | `f524209c` |
<!-- AUTO:END -->

---

## 0 — Read this first (for the AI)

Your first reply, in order:

1. Detect the user's language from their greeting. Reply in the same language.
   Exceptions (always English): file names, commands, git tags, parser markers, code.

2. Empathy check. If the user seems confused ("I don't know", "start", "help",
   short reply, greeting with no context), before anything else:
   - Confirm what they sent: this file? this file + run.py? a full project?
   - Ask one question: "What are we building?" or "New project, or continue?"
   - Never say "this is a generic template" or "still not filled".
   - Never ask 3+ questions in one message.

3. If unclear what they have, ask: "What do you have — just this file, or also run.py?"

4. Never ask "where were we?" — the answer is in this file + _work/output.txt.

5. Never start from scratch.

Golden rule for every reply:
  one message = one copyable code block containing the entire _work/input.txt.
  No prose between blocks. At most one line of prose before the block.

End every message with: If errors: run python run.py and send _work/output.txt.

---

## 1 — Workflow

    AI writes a patch  -> user pastes into _work/input.txt
                       -> user runs: python run.py
                       -> tool applies patch, clears input, writes output.txt
                       -> user sends _work/output.txt to AI
                       -> AI reads state, sends next patch

Never ask the user to run two commands when one suffices.
Never ask them to copy files by hand when run.py can do it.

Pull, not push:
  Normal:   python run.py --status    (about 300 bytes)
  One file: python run.py --file src/x.py
  Full:     python run.py dump --full

Ask only for what you need.

---

## 2 — Patch syntax

Every patch is one or more blocks in _work/input.txt.

Edit a file:

    ===== FILE: path/to/file.ext =====
    <<<FIND>>>
    [exact text from the user's file — copy verbatim]
    <<<REPLACE>>>
    [new text]
    <<<END>>>

Create, delete, move, mkdir:

    ===== CREATE: path/to/new.ext =====
    <<<CONTENT>>>
    [full content]
    <<<END>>>

    ===== DELETE: path/to/file.ext =====
    ===== MOVE: old/path.ext -> new/path.ext =====
    ===== MKDIR: path/to/dir =====

Run a shell command:

    ===== CMD: short description =====
    <<<RUN>>>
    [PowerShell or shell script]
    <<<END>>>

Note: python run.py inside a CMD is rejected (nested call).

Request a file dump in output:

    ===== DUMP: path/to/file.ext =====
    ===== DUMP: src/main.py --grep "def foo" --head 50 =====
    ===== DUMP: src/main.py --lines 20-80 =====

Anchor rules:
  - Copy the anchor character-for-character from the file the user sent.
  - Never from memory.
  - If unsure, dump the file first.
  - Never use ... or // ... in an anchor.
  - Prefer 3 to 6 lines. One line is fragile. Whole file is wasteful.
  - Match indentation exactly.

---

## 3 — Directives (first lines of input.txt)

    #@ID: 42              set patch ID manually
    #@CMD: check          replace this run with the given CLI args
    #@POST: check         after applying patches, run this command
    #@POST: verify
    #@POST: find-dup --top 20

Use #@POST: to chain build or test after a patch in one round-trip.

---

## 4 — Response rules (for the AI)

1. One message = one patch, one code block. The block contains complete input.txt.

2. Never rewrite a whole file unless the user asked.

3. Never invent. If you don't know an API, ask for --file X. If the spec is
   unclear, record it here as a TODO and skip. Don't guess.

4. Every code change updates this file too.

5. No maybe, no I think, no try it. Be exact. If unsure, say so and ask for data.

6. Never touch secrets, keys, credentials, or build artifacts unless asked.

7. Never add features, dependencies, or refactors the user didn't request.

8. After every successful patch, suggest a tag.

9. Persist decisions by patching this file.

---

## 5 — Rate limits and unique messages

Some providers throttle or ban when a user sends many similar messages in a
short window. run.py helps:

  - Every output starts with # MSG-SEED: hex — different every run.
  - Every output shows RATE WARN if the last run was less than 25s ago.

For the user:
  - Wait at least 25-30 seconds between runs whose output you send.
  - Batch: put 2-3 patches in one input.txt.
  - Mix structure: --status, --file X, #@POST: check.

For the AI:
  - Encourage batching.
  - Prefer one #@POST: over two separate runs.

---

## 6 — Context update (automatic + manual)

run.py maintains the auto block between the AUTO:START and AUTO:END markers at
the top of this file. It writes the last patch ID, last commit hash, timestamp,
and MSG-SEED before every successful git commit. Do not edit that block by hand.

Everything else is edited only by patching, exactly like code.

Section ownership:
  - Stable sections (usually changed by the user): workflow, patch syntax,
    response rules, rate limits.
  - Mutable sections (usually changed by the AI): project ID, session tracker,
    decisions, roadmap.

3-patch rule:
  If a section has received more than 3 patches in a row, rewrite it from
  scratch instead of stacking another patch. Stacked patches create contradictions.

---

## 7 — Handoff (new chat)

When the user opens a new chat, they send:

  1. This file (full text).
  2. _work/output.txt from the last run.
  3. Optionally, python run.py --status.

The AI must:
  1. Confirm reading (one line).
  2. Detect language and reply in it.
  3. Look at the AUTO block, the Session Tracker, and the last output.txt.
  4. Continue from the recorded next step. Never ask "where were we?".

If output.txt isn't sent: ask once — Please run python run.py and send
_work/output.txt — then wait.

---

## 8 — Bootstrap (first time)

If the user says they only have this file:

  1. Ask: Do you have run.py in the project root and have you run
     python run.py --init?
  2. If no: save the reference run.py as run.py in the project root.
  3. Then: python run.py --init — creates _work/, .gitignore, config.json.
  4. Edit _work/config.json to set build_cmd and test_cmd.
  5. python run.py --status — should print project name and file count.
  6. First patch can now be sent.

Never ask the user to mkdir, copy, or edit by hand if run.py can do it.

---

## 9 — Truth-seeking principle

When something is unclear (incomplete data, uncertain output, unreadable source):

  - Do not implement it.
  - Do not throw it away.
  - Record it. Add a note here: what is unclear, what data is needed, why.
  - Pick the safe default (usually: skip this branch and continue).

Guessing produces silent bugs. Silently dropping data loses knowledge.

---

## 10 — Project ID

Basics:

| Field | Value |
|-------|-------|
| Name | <name> |
| Version | <0.1.0> |
| Language | <e.g., Python 3.11> |
| Frameworks | <e.g., none> |
| Target OS | <e.g., Windows, Linux> |
| Dev env | <e.g., VS Code + venv> |
| Project root | <absolute path> |
| Git repo | <url or local> |

Goal (2-3 lines):
  <what the project does and for whom>

Red lines (things never to touch):

| # | What | Why |
|---|------|-----|
| 1 | <file/function/constant> | <reason> |

---

## 11 — Session tracker

| Field | Value |
|-------|-------|
| Last safe tag | <e.g., step-42-ok> |
| Last commit | <hash or summary> |
| Last work | <one line> |
| Next step | <one line> |
| Current phase | <name> |
| Open issues | <list> |
| Open questions | <list> |

Update every session. This is what the next chat reads first.

---

## 12 — Changelog (append-only)

| Tag | Description |
|-----|-------------|
| v0.1.0 | first commit |

If this grows beyond about 50 lines, split into CHANGELOG.md.

---

## 13 — Decisions (ADR-lite)

Short records of why we chose X. Add one per significant decision.

    ### YYYY-MM-DD — title
    Decision: <one line>
    Reason: <one line>
    Alternatives considered: <one line>

If this grows beyond about 10 entries, split into ADR.md.

---

## 14 — Cheat sheet (what to send in a new chat)

| Situation | Send |
|-----------|------|
| Start new chat | this file + --status |
| Change one file | this file + --file X |
| Change several files | this file + dump --full |
| Debug error | this file + --errors |
| Only this file | this file; AI guides setup |

Never send raw screenshots, binary files, or logs longer than the last output.txt.