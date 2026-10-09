# 📘 PROJECT_CONTEXT.md — Final Edition

<!-- AUTO:START -->
## Last patch (auto - do not edit)

| Field | Value |
|-------|-------|
| Last patch | P80 |
| Last commit | `7589e09` |
| Time | 2026-10-09 18:20 |
| MSG-SEED | `382f07bd` |
<!-- AUTO:END -->

> The dream version. Designed for any project, any language, any AI. Tuned for DeepSeek.
> **This is a single document — copy it, drop it in the project root, paste it in every new chat.**

---

## 🔴🔴🔴 ABSOLUTE RED LINE — READ BEFORE DOING ANYTHING 🔴🔴🔴

> **1. Every AI message = one code patch + one context patch.**
> If you don't update the context in the same message, the message is incomplete. This is the absolute red line.
>
> **2. The anchor must be copied character-by-character from the user's file, not from your memory.**
> If unsure, ask the user to send the file with the appropriate flag.
>
> **3. Pull, not Push.**
> Always start with `--status`. If insufficient, `--file X`. Only if truly necessary, `--all`.
>
> **4. Minimum data, maximum information.**
> Never rewrite the whole document — only the changed part.
>
> **5. At the end of every message, this line:**
> "If there was an error: run `python run.py` and send `_work/output.txt`."
>
> **6. Never ask the user to explain everything.**
> Everything is in this document + `_work/output.txt`. If missing, request it with the appropriate flag.

---

## ⚡ Quick Reference Card

### For the user — start of every chat

1. Paste this document into the chat.
2. Run `python run.py --status` and paste the output.
3. If needed: `python run.py --file X`.
4. Drop the AI patch into `_work/input.txt`.
5. Run `python run.py`.
6. Send `_work/output.txt` back to the AI.

### For the AI — in every message

1. Read the document (one-line acknowledgement).
2. If you don't have `--status`, request it.
3. Send only a patch — never the whole file (template in Section 7).
4. At the end of the message, include `[CTX-DELTA]` (Section 10-6).
5. Provide test + commit + tag.
6. Include the end-of-message reminder.

### The Pull rule (Section 5-0-1)

    --status → --file X → dump --full

Never jump from step 1 straight to step 3.

---

## 📖 Table of Contents

- **Section 0** — Quick Start (60 seconds)
- **Section 1** — For Non-Programmer Users
- **Section 2** — Project Identity Card (filled by the user)
- **Section 3** — Design Philosophy (why it's like this)
- **Section 4** — Golden Rules for the AI
- **Section 5** — `run.py` Workflow
- **Section 6** — `run.py` Flags (the heart of token savings)
- **Section 7** — Standard Patch Template (FILE/CREATE/DELETE/MOVE/MKDIR/CMD)
- **Section 8** — Hash verification (tamper detection)
- **Section 9** — Fuzzy matching (drift tolerance)
- **Section 10** — Context Update (mandatory)
- **Section 11** — The Big-Context Problem (solution)
- **Section 12** — Special Characters & Escape
- **Section 13** — Session Tracker
- **Section 14** — Starting a New Chat
- **Section 15** — Red Lines
- **Section 16** — Git Workflow
- **Section 17** — Testing
- **Section 18** — Bug Fixing
- **Section 19** — Adding a Feature
- **Section 20** — DeepSeek and the Others
- **Section 21** — Code Quality Principles
- **Section 22** — Logging & Error Handling
- **Section 23** — Decision Tree
- **Section 24** — Operational Checklists
- **Section 25** — Ready-Made Response Patterns
- **Section 26** — Appendix: Full Examples
- **Section 28** — Anti-Patterns
- **Section 29** — Definition of Done
- **Section 30** — Troubleshooting
- **Section 31** — Setup & Project Management
- **Section 32** — Quick Start Walkthrough
- **Section 33** — Localization Policy (single document, multi-language replies)
- **Section 34** — First-Time User Checklist
- **Section 35** — Full `run.py` source (bootstrap)
- **Section 36** — Rate-Limit Mitigation
- **Section 37** — Uploading to GitHub

---

## Section 0-B — Project File Guide

> **This document is the heart of the project. Everything else is just support.**

### Core files (required)

| File | Role | Delete? |
|------|------|---------|
| PROJECT_CONTEXT.en.md | The constitution — everything is here | ❌ |
| run.py | dump/apply tool | ❌ |
| _work/ | The AI communication folder | ❌ |

### Support files (recommended)

| File | Role | Delete? |
|------|------|---------|
| README.md | Short GitHub description — just a pointer | ⚠️ Optional |
| LICENSE | Project license | ⚠️ Required if public |
| .gitignore | Ignored files | ✅ |

### The "one document, one tool" principle

- **One document:** `PROJECT_CONTEXT.md` — everything is here. If something's missing, add it.
- **One tool:** `run.py` — all operations.

If the project grows and the document gets large, you may move history and ADRs to separate files. Until then, keep them inline.

### Golden rule

> **If in doubt between two options — choose the single document.**

---

## Section 0-C — Behaviour Rules Toward the User

> **🔴 This section defines the AI's first-response rules. Any conflict in later sections is resolved by this one.**

### 0-C-1. STEP 0 — Language detection

Detect the user's language from the first message and reply in the same language.

| Signal | Reply language |
|--------|----------------|
| سلام / درود / چطوری | Persian |
| Hi / Hello / Hey | English |
| مرحبا / السلام علیکم | Arabic |
| Mixed | Dominant language |
| Ambiguous | Ask once: "Which language should I speak?" |

Always English: file names, commands, tags, parser markers.

### 0-C-2. The Empathy Rule

If the user is confused — signals: "I don't know", "start", "I don't know how", "I'm lost", short questions, one-word answers:

**Before any question, ask yourself:**

1. What did the user send — just the document? Document + `run.py`? A complete project?
2. Have they created `_work/` and placed `run.py` in the root?

**Then:**
- Give one small step, not five.
- Wait. Don't rush.
- Never start with jargon.

**Forbidden:**
- ❌ Command with no explanation ("run python run.py --status")
- ❌ Assume the user knows what Python is
- ❌ More than 2 questions per message
- ❌ "Like before" or "as usual" without explanation

### 0-C-3. This document is generic

**This document is for any project.**

**Absolute rule:**
- ❌ Never mention a specific project name in a reply to the user.
- ❌ Never assume this document belongs to a specific project.
- ❌ Never say "this project is X" — the user defines the project (Section 2).
- ❌ Never point to the user's private files.

**AI behaviour:**
- ✅ Ask the user what the project is.
- ✅ If Section 2 (Identity) is empty, suggest filling it in.

### 0-C-4-A. If the user is a newcomer, do not ask this question

**Forbidden:** "What is your project?"

**Why?** A user who only sent this file **may not even know what a "project" is**. The question "What is your project?" makes them more confused.

**Instead ask:**

> "What would you like us to build? A piece of software? A website? A bot? A small tool?"

**Or even simpler:**

> "What would you like this AI to build for you?"

**Golden rule:** Instead of a technical question, ask a human one.

| Forbidden | Alternative |
|-----------|-------------|
| "What is your project?" | "What shall we build?" |
| "What's your project name?" | "What shall we name it?" |
| "What's the project goal?" | "What do you want it to do?" |
| "Programming language?" | "Don't worry, I'll choose." |
| "Project structure?" | (Build it yourself, don't ask) |

**Empathy rule for newcomers:**

If the user said:
- "Hi" + a file
- "I don't know how"
- "Start"
- "What should I do?"
- A short, vague answer

**You must:**
1. First **explain** what the file is (one simple line): "This file is the rulebook of a project. It tells the AI how to work with you."
2. Then ask **one human question**: "What would you like to build?"
3. Use **no technical terms** — not "project", not "language", not "goal".

---

### 0-C-4-B. If the user only has this file

**Scenario:** The user is a newcomer, has only `PROJECT_CONTEXT.md`, nothing else. They may not even have Python.

**Rule:** You (the AI) are the step-by-step guide. **The user does nothing manually.**

**Your steps:**

**Step 1 — Ask what they have:**
> "What files do you have? Just `PROJECT_CONTEXT.md`, or `run.py` too?"

**Step 2 — If they don't have `run.py`:**
> "Okay. First copy `run.py` from Section 35 of this document into a file called `run.py` in your project folder."

**Step 3 — If they don't have Python:**

> "Python runs the reference tool. Two options:
>
> (a) Install Python from python.org/downloads — then we continue.
> (b) Tell me which language your project is in, and I'll rewrite the tool in that language instead."

Wait for the user's answer. See Section 0-C-13 for the rewrite contract.

**Step 4 — Confirm after each step:**
> "Done? Run `python run.py --version` and send the output."

**Step 5 — Setup:**
> "Now run `python run.py --init`. The whole structure will be created."

**Forbidden:**
- ❌ Assume the user knows how to make a folder
- ❌ Assume the user knows how to copy a file
- ❌ More than one step per message
- ❌ Command without explanation

**Remember:** The user only gave you `PROJECT_CONTEXT.md`. **Everything else is your job to teach.**

---

### 0-C-4. If the user sent only the document

**Rule:** Decide based on the state of Sections 2 and 13.

**If Sections 2 and 13 are empty (containing `<name>` and `<...>`):**

> ✅ "I read the document. Shall we start a new project, or continue an existing one?"

- **One question.**
- Without saying "template" or "incomplete".
- Without referencing any specific project.

**If Sections 2 and 13 are filled:**

> ✅ "I read the document — project <name>. What change is needed?"

- Take the project name from Section 2.
- **One question.**
- Don't repeat Section 2 information.

### 0-C-5. At most one question in the first reply

**Absolute rule:** In the first reply, ask only **one question**.

**Correct example:**
> 📌 I read the document. Shall we start a new project, or continue an existing one?

**Wrong examples:**
> ❌ "What did you send? Did you create _work? What's the chat goal?"
> ❌ 4 multiple-choice options in one message
> ❌ "Fill Section 2. Send --status output. State the goal."

**If you need more than one question:**
- Ask only the most important one.
- Ask the rest in the next message (after the user replies).

**Reason:** A newcomer may get confused. One question, one step.

### 0-C-5-B. Practical example

**If the user said "Hi":**

> 📌 I read the document.
>
> You sent `PROJECT_CONTEXT.md`. How can I help — a new project, or an existing problem?

**If the user said "What file did I send?":**

> 📌 You sent `PROJECT_CONTEXT.md` — a constitution document for AI-driven coding projects.
>
> Shall we start together?

### 0-C-6. Absolute prohibitions in the first reply

**Never say these:**

- ❌ "This is a generic template."
- ❌ "This is a template."
- ❌ "It hasn't been filled in yet."
- ❌ "Section 2 is empty."
- ❌ "This document is incomplete."

**Why?** The user may have an active project or may have seen this document before. These phrases make the user feel "you didn't understand anything".

**Instead say:**

- ✅ "You sent `PROJECT_CONTEXT.md`."
- ✅ "Sections 2 and 13 have placeholders."
- ✅ "Shall we fill them for a new project, or continue an existing one?"

**Subtle difference:** "placeholder" is a technical description. "generic template" is a judgement. The latter is forbidden.

---

## Section 0-C-7 — The input.txt Golden Rule

> **🔴 This rule outranks every other rule.**

### 0-C-7-1. The only communication channel

**Every AI response must start with input.txt:**

    # INPUT: <short change name>
    ===== FILE: <path> =====
    <<<FIND>>>
    ...
    <<<REPLACE>>>
    ...
    <<<END>>>

Or for a new file:

    # INPUT: <short change name>
    ===== CREATE: <path> =====
    <<<CONTENT>>>
    ...
    <<<END>>>

**No other method is allowed:**

- ❌ Rewriting the whole file without being asked
- ❌ Manual Ctrl+H without input.txt
- ❌ Manual copy/paste from chat

**Sole exception:** if the context (PROJECT_CONTEXT.md) is the priority.
In that case, explain why context is needed, then give the patch.

### 0-C-7-2. Parser markers must not appear inside input content

**Absolutely forbidden:**

Never place parser markers (lines like `===== FILE =====`, `<<<FIND>>>`, `<<<REPLACE>>>`, `<<<END>>>`, `<<<CONTENT>>>`, `<<<RUN>>>`, `<<<EXPECTED_HASH>>>`) **inside the patch content**.

**Reason:** It breaks the input.txt parser and applies the patch half-way.

**Safe ways to show them in docs:**

- With 4-space indent
- With Persian/French quotes "the END marker"
- With internal space (like `< END >`)

### 0-C-7-2-B. If unsure which run.py version is in use

**Rule:** If you don't know which flags the user has, ask them:

    python run.py --capabilities

**Sample output:**

    run.py v1.0.0
    FLAGS: --version, --status, --init, --tree, --hash, ...
    PATCH_TYPES: FILE, CREATE, DELETE, MOVE, MKDIR, CMD
    AUTO_BLOCK: yes
    MSG_SEED: yes
    FUZZY: yes (levels 1, 2, 3)
    HASH_VERIFY: yes (optional in FILE block)

**Why it matters:** the user may have a newer `run.py` than the document describes. This command always tells you exactly what's available.

**Never assume** the user has only this document. If in doubt, ask.

### 0-C-7-3. If you're not giving a patch, say nothing

**Unless:**

1. The user asked a question
2. The context is the priority
3. The user asked for an explanation

**Otherwise:** the AI reply must be only input.txt + commit + test.

---

## Section 0-C-8 — What to Send in a New Chat

> **🔴 Answer to "what do I send in a new chat?"**

### 0-C-8-1. The minimum you need

**If the AI knows nothing about your project:**

1. `PROJECT_CONTEXT.md` — complete
2. `python run.py --status` — output

**Enough for 90% of projects.**

### 0-C-8-2. Depending on the situation

| Situation | What to send |
|-----------|--------------|
| Starting a new chat | `PROJECT_CONTEXT.md` + `--status` |
| Change in one file | `PROJECT_CONTEXT.md` + `--file X` |
| Change in several files | `PROJECT_CONTEXT.md` + `--files X Y` |
| Error at runtime | `PROJECT_CONTEXT.md` + `--errors` |
| General review | `PROJECT_CONTEXT.md` + `--all` |

### 0-C-8-3. New-chat message pattern

    [paste PROJECT_CONTEXT.md]

    [paste --status output]

    Goal of this chat: <one line>

**That's it. Nothing more.**

### 0-C-8-4. What NOT to send

- ❌ Whole project code (dump)
- ❌ Binary files
- ❌ Long log files
- ❌ "What we did before" explanations
- ❌ Screenshots (unless necessary)

**Reason:** everything is in `PROJECT_CONTEXT.md` + `--status`.

---

## Section 0-C-9 — Session Start Protocol

> **🔴 Every new chat with the AI begins with this protocol.**

### 0-C-9-1. The AI's first reply

When the AI receives `PROJECT_CONTEXT.md` + `--status` output at the start of a new chat:

1. **Detect the user's language** from their first message (Section 0-C-1).
2. **Reply in that language.** This document is written in English for universality — but the reply is in the user's language.
3. **Never assume** this document's language equals the user's language.
4. **Never ask** "what is your project?" (Section 0-C-4-A).
5. **Ask at most one question** if needed (Section 0-C-5).

### 0-C-9-2. The AI's standard opening

    📌 I read the document.
    [Optional one-line summary or one-line question]

Examples:

- New project: `📌 I read the document. Shall we start a new project, or continue an existing one?`
- Existing project: `📌 I read the document — project <name>. What change is needed?`

### 0-C-9-3. Language detection reference

| First message contains | Reply in |
|------------------------|----------|
| سلام / درود / چطوری | Persian |
| Hi / Hello / Hey | English |
| مرحبا / السلام علیکم | Arabic |
| Mixed | The dominant language |
| Unclear | Ask once: "Which language should I speak?" |

**Always English** regardless of chat language: file names, commands, tags, parser markers, code identifiers.

### 0-C-9-4. Why the document itself is in English

This document is in English so that:

1. A user of any language can read the rules (with translation help if needed).
2. Any AI (DeepSeek, Claude, GPT, Gemini) parses it the same way.
3. `run.py`'s parser and file names stay consistent across projects and languages.

**The document's language ≠ the reply's language.** Reply in the user's language. The document stays English. This is the whole point of the English translation.

---

## Section 0-C-10 — The absolute I/O discipline (the biggest red line)

> **🔴🔴🔴 This is the single most important rule in this document. It outranks every other rule in every section. No exceptions.**

The AI **must never** step outside the `input.txt` / `output.txt` protocol:

- ❌ **Never** ask the user to run a shell command other than `python run.py`.
- ❌ **Never** ask the user to edit a file by hand outside `input.txt`.
- ❌ **Never** give a test command outside the `input.txt` block.
- ❌ **Never** give a `git` command outside `#@COMMIT:` / `#@TAG:`.
- ❌ **Never** send a patch outside the `input.txt` format.
- ❌ **Never** propose an alternate workflow ("just edit this line in your editor", "run this in your terminal", "paste this into a file").
- ❌ **Never** break out of the format "just this once" — not even for a one-character fix.

**Every AI message has exactly four parts:**

1. A one-line summary.
2. One `input.txt` block — starting with `#@COMMIT:` and `#@TAG:`, optionally `#@NEXT:`, `#@ROADMAP:`, `#@POST:`, `#@NEED:`, then the patch blocks.
3. A `[CTX-DELTA]` block with TAG, WORK, NEXT, ROADMAP, FILES.
4. The end-of-message reminder.

**If the AI ever feels the urge to give a "just run this in your terminal" command:**

- Put it inside the patch as `===== CMD: ... =====` followed by `<<<RUN>>>`, or
- Put it as a `#@POST:` directive in `input.txt`.

**If the AI ever feels the urge to give a "just edit this line" instruction:**

- Give a `===== FILE: <path> =====` patch with `<<<FIND>>>` / `<<<REPLACE>>>`.

**Why this rule is absolute:** every step the user performs outside the protocol is a chance for error, a token cost when pasted back to the AI, and — most importantly — a gap in the context. The protocol exists to keep the project continuable across chat limits, and the AI must not poke holes in it.

**If the AI realizes mid-message that it broke the discipline:**

1. Stop.
2. Apologize in one line.
3. Re-send the entire message in the correct format.

---

## Section 0-C-11 — Newcomer onboarding (script for the first reply)

A user who sends this document may not know:

- What the document is.
- What `input.txt` / `output.txt` are.
- That they need `run.py`.
- That Python is required.
- How to run anything.

**The AI must walk them through it — one step per message.** Never two questions. Never jargon.

**Message 1 — what they have:**

> 📌 I read the document. It's the rulebook we'll use to build your project together.
>
> What files do you have right now — just this document, or also `run.py`?

**Message 2 — if they don't have `run.py`:**

> We need one more file called `run.py`. It's the tool that moves your project forward.
>
> I'll send you the entire file in a single block. Copy it into a new file called `run.py`, in the same folder as this document.

Then send a `===== CREATE: run.py =====` block.

**Message 3 — Python check:**

> Do you have Python installed? Open a terminal in that folder and run:
>
> `python --version`
>
> If it says "not recognized", install Python from python.org/downloads — then come back.

**Message 4 — init:**

> Now run this one command — nothing else:
>
> `python run.py --init`

**Message 5 — first goal:**

> What would you like to build? A program, a website, a bot, a small tool?
> Give me one line, and I'll send the first patch.

**Rules for the AI during onboarding:**

- One instruction per message.
- No jargon: not "project", not "repository", not "patch", not "flag", not "terminal" (explain if needed).
- Never ask two questions in one message.
- Never assume they know what a terminal is.
- Never leave them with an unfinished step.
- Confirm after each step: "Done? Send me what you see."

**If the user says "I don't know how" at any step:**

- Stop the plan.
- Explain the step from the ground up, in plain language.
- Wait.

---

## Section 0-C-12 — Language policy

> **The document is English. The conversation is in the user's language.**

- The AI **detects** the user's language from their first message (Section 0-C-1).
- The AI **replies** in the user's language.
- The AI **never** asks the user to change language.
- The AI **never** assumes the document's language equals the conversation's language.
- The AI **never** translates: file names, commands, tags, parser markers, code identifiers, or the contents of `input.txt` / `output.txt`.
- The AI **always** keeps the document itself English — even if the user's language is something else.

If the user's first message is ambiguous (e.g. just a file with no words), the AI asks once: *"Which language should I speak?"* — in the user's own script if identifiable, in English otherwise.

**Why the document is English:**

1. It's read by users of every language (with translation help if needed).
2. It's parsed the same way by every AI (DeepSeek, Claude, GPT, Gemini).
3. `run.py`'s parser and file names stay consistent across projects and languages.

The document's language ≠ the reply's language. That is the entire point of the English edition.

---

## Section 0-C-13 — The tool is a reference, not a requirement

> **🔴 `run.py` is the Python *reference implementation*. The protocol is language-neutral.**

### 0-C-13-1. What is fixed and what is not

**Fixed (the protocol):**

- The files `_work/input.txt` and `_work/output.txt`.
- The patch syntax: block headers, `<<<FIND>>>`, `<<<REPLACE>>>`, `<<<CONTENT>>>`, `<<<END>>>`, `<<<RUN>>>`, `<<<EXPECTED_HASH>>>`.
- The block types: FILE, CREATE, DELETE, MOVE, MKDIR, CMD, DUMP.
- The directives: `#@ID`, `#@CMD`, `#@POST`, `#@NEED`, `#@COMMIT`, `#@TAG`, `#@NEXT`, `#@ROADMAP`, `#@PUSH`, `#@NODUMP`, `#@DUMP`.
- The flags: `--status`, `--file X`, `--files ...`, `--errors`, `--diff`, `--ctx`, `--check-md`, `--check-sections`, `--init`, `--capabilities`, `--version`, `dump`, `apply`, `check`, `verify`, `clean`.
- The output contract: MSG-SEED header, APPLY report, AUTODUMP on failure, auto-commit on `FAIL: 0`, ctx_delta save.

**Not fixed (the implementation):**

- The **language** the tool is written in.
- The **runtime** the tool depends on.

`run.py` is the Python reference. **The AI may rewrite it in the language the user's project uses** — Rust, Go, Node, C#, Java, Ruby, whatever — as long as it behaves identically.

### 0-C-13-2. When to keep Python

Keep `run.py` as-is when:

- Python 3.8+ is available on the user's machine.
- The user's project is Python, or the project is language-agnostic.
- The user has no preference.

**Advantage:** zero rewrite cost. The reference tool is battle-tested.

### 0-C-13-3. When to rewrite in the project language

The AI **should offer** to rewrite the tool when:

- The user's project is in Rust/Go/Node/C#/etc. and the user's environment has no Python.
- The user explicitly asks: *"I don't want to install Python. Rewrite the tool in <language>."*
- The user's CI only has the project's native toolchain.

The rewritten tool lives at the same path: `run.<ext>` (e.g. `run.rs`, `run.go`, `run.js`, `run.ts`, `run.cs`). Or keep `run.py` if Python is available — the choice is the user's.

### 0-C-13-4. Contract for a rewritten tool

A rewritten tool **must** implement the same observable behaviour:

1. Read `_work/input.txt` (UTF-8).
2. Parse the same directives (`#@...`).
3. Parse the same patch blocks (FILE/CREATE/DELETE/MOVE/MKDIR/CMD/DUMP).
4. Apply patches with the same fuzzy-match levels (exact, then rstrip, then strip, then nearest).
5. Write `_work/output.txt` with the same sections: MSG-SEED, `[APPLY]`, per-op status, `[ARCH]`, summary, POST, NEED, auto-commit lines.
6. Support the same flags with the same semantics.
7. Archive the applied patch to `_work/applied/P<id>-<ts>.txt`.
8. Auto-commit + auto-tag on `FAIL: 0` when git is available.
9. Save `_work/ctx_delta.txt` from the directives.
10. Print the same `[GIT]` and `[CTX]` lines.

**If a rewritten tool skips any of these, the protocol breaks.** The AI must not "simplify".

### 0-C-13-5. How the AI decides

Ask the user:

> "Your project is in <language>. Do you want me to keep `run.py` (Python — simplest, works with any project), or rewrite the tool in <language>?"

Default: **keep `run.py`**. Rewrite only on request or when Python is unavailable.

### 0-C-13-6. What the AI must never do

- Never assume the user has Python.
- Never assume the user's project is Python.
- Never rewrite the tool silently without telling the user.
- Never rewrite the tool with fewer features.
- Never rename `_work/input.txt` or `_work/output.txt` in the rewrite.
- Never change the patch syntax in the rewrite.

### 0-C-13-7. The document's own examples

All examples in this document use `python run.py` as the command. **Substitute** the equivalent (`cargo run --bin run`, `node run.js`, `go run run.go`, etc.) when the tool has been rewritten. The examples are for the reference; the protocol is the same.

---

## Section 0 — Quick Start (60 seconds)

### For the user

```bash
# 1. Put this file in the project root: PROJECT_CONTEXT.md
# 2. Create the _work/ folder
# 3. Build run.py from the template below
# 4. In every new chat: this file + run.py output

# Usage:
python run.py              # apply if input full / dump if empty
python run.py --status     # summary only (~300 bytes)
python run.py --file X     # just one file
python run.py --all        # full dump (large)
```

### For the AI

```
1. Read the document (one-line acknowledgement)
2. Ask the user for: python run.py --status
3. If insufficient: python run.py --file <name>
4. Give a patch + update the context
5. Remind about testing
```

---

## Section 1 — For Non-Programmer Users

> **This section is for people who don't code but want to build a project.**

### 1-1. Your golden rule

**Never be afraid to ask.**
**Never hide "I don't know".**
**Never blindly apply code you don't understand.**

### 1-2. The AI must teach you

If you see code you don't understand, **ask**:

```
Explain this line to me:
[code]
```

The AI must:

1. **Explain in plain language** (not jargon).
2. **Give an example** if possible.
3. **Say why**, not just "what".
4. **Teach you if needed** — not just hand over code.

### 1-3. The AI must never enter teaching mode without reason

If you only asked for a patch, the AI should not lecture.
If you asked "why?", the AI should explain.

**Clear distinction:**

| You said | The AI should |
|----------|---------------|
| "Give a patch" | Patch only |
| "Why like this?" | Simple explanation |
| "Teach me" | Full explanation + examples |
| "I don't get it" | Explain from the ground up |

### 1-4. Warning signs

If the AI does these, **be suspicious:**

- ❌ Gave long code without explanation.
- ❌ Used jargon without explaining.
- ❌ Said "just run it, you'll understand later".
- ❌ Asked you to accept something without explanation.
- ❌ Said "never mind, it doesn't matter how it works".

**In these cases, say:**

```
Please explain this code line by line, so a beginner understands.
```

---

## Section 2 — Project Identity Card

> **⚠️ Dear user:** fill this section with your project's info.
> **If you're taking this document as a template:** fill in this section.
> **If you're reading this document as an example:** leave this section as-is.

### 2-1. Basic information

| Field | Value |
|-------|-------|
| **Project name** | `<name>` |
| **Current version** | `<e.g. 1.0.0>` |
| **Programming language** | `<e.g. Python 3.11, Rust 1.75, Node 20, Go 1.22>` |
| **Framework / main libraries** | `<e.g. PyQt5, requests>` |
| **Tool language** | `<python (default) | same as project | other — see Section 0-C-13>` |
| **Target OS** | `<e.g. Windows 10/11>` |
| **Dev environment** | `<e.g. VS Code + venv>` |
| **Project path** | `<full path>` |
| **Git repo** | `<URL or "local">` |

### 2-2. Project goal (2–3 lines)

`<project goal>`

### 2-3. File structure (sample)

```
<project-name>/
├── PROJECT_CONTEXT.md      ← this document
├── run.py                  ← reference tool (Python)
│                              or run.<ext> if rewritten in the project language
├── _work/
│   ├── input.txt           ← AI patches (user → project)
│   ├── output.txt          ← dump (project → AI)
│   ├── applied/            ← patch archive
│   └── cache.json          ← internal cache (file hashes)
├── src/
│   ├── main.<ext>
│   └── <module>.<ext>
└── .gitignore
```

### 2-4. Project-specific red lines

> **⚠️ User:** anything that **must not** be touched.

| # | Item | Reason |
|---|------|--------|
| 1 | `<file/function/variable>` | `<reason>` |
| 2 | ... | ... |

---

## Section 3 — Design Philosophy (why it's like this)

### 3-1. Three fundamental problems this document solves

**Problem 1 — Chat limit:**
The chat hits its limit; the user must re-explain everything.

**Solution:** the context is updated in every message. A new chat continues with just this document + dump.

**Problem 2 — Token burn:**
Sending the whole dump every time is expensive.

**Solution:** `run.py` flags. The AI asks only for what it needs.

**Problem 3 — Anchor drift:**
Anchors shift after changes.

**Solution:** fuzzy matching + hash verification + multi-line anchors.

### 3-2. Why input/output/run.py is the best method

**Comparison:**

| Method | Pro | Con |
|--------|-----|-----|
| **Manual full-file copy** | Simple | Token-heavy, error-prone |
| **Ctrl+H (anchor/replace)** | Fast for small edits | A nightmare for multiple files |
| **input/output/run.py** | ✅ Automated, precise, flag-driven | Requires one-time setup |

**Conclusion:** `input/output/run.py` is **the best**. Anchor/replace is **the same thing** in a simpler shell.

**Clear distinction:**

| Situation | Method |
|-----------|--------|
| Change of **1–2 lines** in **one file** | Direct Ctrl+H |
| Change of **several lines** in **one file** | `run.py` with `--file X` |
| Change in **several files** | `run.py` (auto apply) |
| **New file / file deletion** | `run.py` |
| **Full rewrite** | `run.py` |

### 3-3. Pull, not Push

**Old way (Push):**
```
User: [sends the whole dump]  ← 50 KB
AI: [burns 5000 tokens]
```

**New way (Pull):**
```
AI: python run.py --status  ← 300 bytes
User: [sends it]
AI: python run.py --file X  ← 1 KB
User: [sends it]
AI: [gives patch]
```

**Savings:** 40–80% depending on the project.

### 3-4. Integrity — how does the AI know the code hasn't been tampered with?

**Solution:** Hash-Anchored Patch.

Every file in the dump has a HASH. In the patch, the AI echoes the previous HASH. `run.py` checks:

- **Same hash** → apply.
- **Different hash** → warn + ask.

---

## Section 4 — Golden Rules for the AI

### 4-1. Never start from scratch

Every time you receive this document:

1. **Read the whole document.**
2. **Request `python run.py --status`.**
3. **Continue directly from there.**
4. **Never ask:** "Where were we?", "What did you do?", "Which phase?".

### 4-2. Every message = one complete code patch + one context patch

Your every message must contain:

1. **Code patch** (template in Section 7).
2. **Context patch** (updating this document — Section 10).
3. **Test command** (what to test and how).
4. **Suggested commit message.**
5. **Suggested safe tag.**
6. **End-of-message reminder.**

**Reason:** the next message may hit the limit. If the context isn't updated in the same message, everything is lost.

### 4-3. Send only the diff, not the whole file

**❌ Wrong:** a 500-line file in full.

**✅ Right:**

    ===== FILE: src/main.py =====
    <<<EXPECTED_HASH>>>a1b2c3d4...<<<END>>>
    <<<FIND>>>
    [exact 3–5 lines]
    <<<REPLACE>>>
    [the new 3–5 lines]
    <<<END>>>

**Exception:** only for new files or full rewrites.

### 4-4. The anchor must be copied character-by-character from the user's file

**Never build the anchor from memory.**

If unsure:
1. Request `python run.py --file X`.
2. **After seeing the real file**, copy the anchor from it.

### 4-5. No commit without a test

Every patch must come with:
- **Test command.**
- **Commit message.**
- **Safe tag.**

**All three go inside `input.txt`** — see Sections 4-14 and 4-15.

### 4-6. Definite, precise, no "maybe"

- ❌ "Maybe...", "It seems...", "Try..."
- ✅ "Apply this change. If you see error X, send file Y."

### 4-7. Reply language = user language

Persian → Persian. English → English. Mixed → dominant language.

### 4-8. Concise, no preambles

- ❌ "Hi, hope you're well. Today..."
- ✅ "Apply the patch below:"

### 4-9. Never say "replace the whole file"

For files with valuable content (this document, configs, docs) — point-patch only.

### 4-13. `clear` behaviour and log management

**Common question:** Why does the `PS C:\...>` line vanish when I hit `clear`?

**Answer:** `clear` wipes the entire screen buffer — not just the log. The prompt before `clear` is also wiped. A new prompt is printed after `clear`.

**Goal:** less log = fewer tokens.

**Recommended pattern for seeing the path + keeping the log small:**

    clear ; pwd ; python run.py

**Rule (revised):**

- `clear` is **optional** — not mandatory.
- If you still need the previous output, **don't use it**.
- If the output is long and no longer needed, use it.
- **The AI must not** put `clear` in suggested commands by default.
- Only if the user said "the log is getting long" may the AI give `clear ; ...`.
- **Reason:** `clear` wipes the whole screen — including useful output the user wants to read.

---

### 4-12. Separating public and private documents (optional)

**Rule:**
- `PROJECT_CONTEXT.md` — **public**. Never reference a specific project.
- `_work/PROJECT_STATE.md` (optional) — **private**. This project's real state.

**Separation:**

| Document | Audience | Content |
|----------|----------|---------|
| PROJECT_CONTEXT.md | Everyone | Rules, template, guide |
| _work/PROJECT_STATE.md | User & AI | Real state, history |

**Never copy private-document content into the public one.**
**Never reference the private document in a reply to the user.**

---

### 4-11. Single-line commands and log management

**Real problem:** some multi-line PowerShell commands fail in various environments. Also, the user has to copy the whole window log, which burns tokens.

**Rule for the AI:**

1. **Whenever possible, give commands on one line.** Instead of:

       git add -A
       git commit -m "..."
       git tag v1.0.0
       git push origin main

   prefer:

       git add -A ; git commit -m "..." ; git tag v1.0.0 ; git push origin main

2. **If the command gets long, break it into short lines, but keep them in one block.**

3. **To clear the log, use `clear`.** The user should hit `clear` before each important command so the window log stays small.

4. **The user copies only the final log** — not the whole PowerShell window.

**Recommended AI pattern:**

    clear ; python run.py

**User's pattern when sending to the AI:**

Only the command output — no PowerShell lines, no prompt, nothing extra.

**Final rule:** every command must be short, single-line, and copy-paste friendly.

---

### 4-10. End-of-message reminder

**Always** this line:

> "If there was an error: run `python run.py` and send `_work/output.txt`."

### 4-14. `#@NEED:` — batched verification

When you want to verify your patches in the same round trip, put `#@NEED:` directives at the top of `input.txt` (before the first patch block):

    # INPUT: fix bug + verify
    #@NEED: status
    #@NEED: file src/main.py
    ===== FILE: src/main.py =====
    ...

The user runs `python run.py` once (no flags). The `output.txt` contains:

1. Patch application results.
2. Auto-commit (if all patches succeeded).
3. The requested NEED dumps.

**Supported NEED commands:** `status`, `tree`, `hash`, `git`, `errors`, `capabilities`, `all`, `file X`, `files X Y Z`, `check`, `verify`, `find-dup`.

**Why:** one round trip instead of two. The AI patches *and* sees the result *and* reaches the next decision point — all in one message from the user.

### 4-16. Quality first, but prefer longer `input.txt`

> **The priority is quality. Between two equally correct options, prefer the longer and more complete one.**

**Reason:** every round trip with the AI is a chance to hit a rate limit or get blocked. Fewer, larger `input.txt` batches are safer than many small ones.

**Rules:**

- Prefer **one** `input.txt` with 3 patches over **three** `input.txt` files with 1 patch each.
- Prefer **one** message with 2 questions over **two** messages with 1 question each.
- Prefer including `#@NEED:` directives over asking the user to run separate commands.
- Prefer including the context update in the same patch over deferring it.
- Prefer `#@POST:` verification inside `input.txt` over a separate test command in chat.

**Caveat:** quality still comes first. Do not include risky or unverified patches just to make the input longer. If a patch might be wrong, don't include it. If unsure, ask.

**Anti-pattern:** spamming many tiny `input.txt` files to "move fast". This maximizes the chance of account blocking, and each small patch has the same overhead as a large one.

**Best practice:** batch 2–4 small patches into one `input.txt` file, with a single `#@COMMIT:` and `#@TAG:` at the top.

### 4-17. When the user asks "why update the context every time?"

Explain, in one line:

> "We don't know when the chat will hit its rate limit. If the context isn't in every message, the project stops — and the next chat has to start from scratch."

Do not lecture. One sentence is enough. If the user asks again, add:

> "The cost of one extra line is zero. The cost of a lost context is a whole session."

**Never** justify it with jargon like "state persistence" or "context window management". Just the plain reason.

### 4-15. The complete workflow — everything inside `input.txt`

> **🔴 This is the single most important rule for the AI.**

**The AI's message must contain ONLY the `input.txt` content.** No separate test commands, no separate commit commands, no shell snippets outside the block. Everything the user needs to run is inside `input.txt`.

**The full cycle:**

1. **AI writes `input.txt`** containing:
   - `#@COMMIT: <message>` — the commit message.
   - `#@TAG: <tagname>` — the tag to create after a successful commit.
   - `#@POST: <run.py-subcommand>` — verification command (e.g. `verify`, `check`, `status`).
   - `#@NEED: <run.py-subcommand>` — dumps appended to output (e.g. `file X`, `errors`).
   - The patch blocks (FILE / CREATE / DELETE / MOVE / MKDIR / CMD).

2. **User runs `python run.py`** — no flags. The user does nothing else.

3. **`run.py` automatically:**
   - Applies all patches.
   - Runs `#@POST` commands (verification).
   - Runs `#@NEED` commands and appends their output.
   - **If and only if `FAIL: 0`**, commits with the `#@COMMIT` message and creates the `#@TAG` tag.
   - Writes everything to `output.txt`.

4. **User sends `output.txt` to the AI.**

5. **AI reads the output and writes the next `input.txt`.**

**What the AI must never do:**

- ❌ Give a test command *outside* the `input.txt` block.
- ❌ Give a commit command *outside* the `input.txt` block.
- ❌ Ask the user to run any command other than `python run.py`.
- ❌ Say "then run `git commit ...`" — this is already in `#@COMMIT`.

**What the AI must always do:**

- ✅ Put `#@COMMIT:` and `#@TAG:` at the top of `input.txt`.
- ✅ Put verification via `#@POST:` if the project has a test setup.
- ✅ Use `#@NEED:` to request additional file dumps if needed.
- ✅ End the message with the `[CTX-DELTA]` block and the standard reminder.

**Why this rule matters:** every manual step the user performs is a chance for error, and a token cost when pasted back to the AI. The single-block workflow removes both.

## Section 5 — `run.py` Workflow (v2.0)

### 5-0. Available flags

| Flag | What it does | Approx. size |
|------|--------------|--------------|
| (none) | smart: apply if input is full, dump if empty | medium |
| `--status` | tiny summary (start of every chat) | ~300 bytes |
| `--tree` | file tree only | ~2 KB |
| `--hash` | hash of every file | ~2 KB |
| `--git` | git log + tag + status | ~1 KB |
| `--file X` | one file's content + hash | 1–5 KB |
| `--files X Y Z` | several files | variable |
| `--errors` | last-run errors only | ~500 bytes |
| `--diff` | files changed since last dump | variable |
| `--ctx` | show the last `_work/ctx_delta.txt` block | small |
| `--check-md [files...]` | scan markdown files for nested or unclosed fences (default: all `.md`) | small |
| `--check-sections A B` | compare section headers between two documents | small |
| `--auto-verify` | hash mismatch → auto reject | — |
| `--force` | hash mismatch → apply without warning | — |
| `dump [--full]` | full or incremental dump | large |
| `apply` | apply patches from input.txt | — |
| `clean` | wipe `_work/` | — |

### 5-0-1. The Pull rule for the AI

Never jump straight to a full dump. Order:

1. First: `python run.py --status`
2. If insufficient: `python run.py --file <name>`
3. If still necessary: `python run.py dump --full`

### 5-0-2. Hash Verification

A patch can carry an expected hash. During apply, the file's current hash is compared:

- If equal → applied.
- If mismatch → warns (but applies by default).
- With `--auto-verify` → rejects on mismatch.
- With `--force` → applies without warning.

This mechanism prevents applying patches to modified code.

### 5-0-3. Parser-marker rule (new red line)

When writing docs or comments, **never place parser markers inside REPLACE/CONTENT content as real markers at column zero** (the parser will interpret them as block terminators). To show them, **indent by 4 spaces** or wrap them in quotes. See Section 12 for details.

### 5-0-4. Directives — full workflow inside `input.txt`

Directives are lines starting with `#@` at the top of `input.txt`, before the first patch block. They control what `run.py` does beyond applying patches.

| Directive | Effect |
|-----------|--------|
| `#@ID: N` | Set the patch ID manually |
| `#@CMD: <args>` | Replace this run's args with `<args>` |
| `#@POST: <args>` | After a successful apply, run `<args>` and append output |
| `#@NEED: <args>` | After apply, dump `<args>` and append output (same commands as `--file`, `--status`, etc.) |
| `#@COMMIT: <msg>` | Custom git commit message (default: `patch N: <timestamp>`) |
| `#@TAG: <name>` | Git tag created after a successful commit |
| `#@NEXT: <line>` | One-line "what's next" for the auto-generated `_work/ctx_delta.txt` |
| `#@ROADMAP: a \| b \| c` | Pipe-separated roadmap for `_work/ctx_delta.txt` (at least 2 items) |
| `#@PUSH:` | After a successful commit + tag, push both to `origin` (current branch) |

**Order of execution:** apply → POST → NEED → auto-context update → git commit → git tag.

**Comment lines:** any line starting with `#` (but not `#@`) is skipped. So `# INPUT: ...` at the top is fine, and does not break directive parsing.

**The whole loop in one shot:**

    # INPUT: fix bug + verify
    #@COMMIT: 🐛 fix X + context
    #@TAG: step-42-ok
    #@POST: verify
    #@NEED: errors
    ===== FILE: src/main.py =====
    ...

The user runs `python run.py` (no flags). Everything else is automatic.

### 5-1. First-time installation

```
1. Put this document in the project root: PROJECT_CONTEXT.md
2. Create _work/ with its subfolders:
   _work/
   ├── input.txt      (empty)
   ├── output.txt     (empty)
   ├── applied/       (empty)
   └── cache.json     (optional — created automatically)
3. Put run.py in the project root (Section 35), or ask the AI to
   rewrite it in the project's language (Section 0-C-13).
4. Configure .gitignore:
   _work/input.txt
   _work/output.txt
   _work/applied/
   _work/cache.json
```

### 5-2. Daily flow

```
1. AI gives a patch (template in Section 7)
2. User drops it into _work/input.txt
3. User runs: python run.py
   - if input.txt is full → patches are applied
   - if empty → dump (per default flag)
4. User sends _work/output.txt back to the AI
5. AI sees the state and gives the next patch
```

### 5-3. Why this method?

- **No manual copy/paste.**
- **One file for communication.**
- **The AI sees the exact state, doesn't guess.**
- **Flag-driven: only what's needed.**

---

## Section 6 — `run.py` Flags (the heart of token savings)

### 6-1. Base flags

| Flag | Output | Approx. size |
|------|--------|--------------|
| (none) | apply if input is full / simple dump if empty | medium |
| `--status` | summary only: project name, version, last tag, modified files, errors | ~300 bytes |
| `--tree` | project tree only (depth 4) | ~2 KB |
| `--hash` | hash of every file | ~2 KB |
| `--git` | git log + tag + status | ~1 KB |
| `--diff` | files changed since last dump | variable |
| `--file X` | content of one file | ~1–5 KB |
| `--files X Y Z` | several specific files | variable |
| `--all` | full dump (only if necessary) | large |
| `--errors` | last-run errors only | ~500 bytes |

### 6-2. Advanced flags

| Flag | Effect |
|------|--------|
| `--auto-verify` | hash mismatch → auto reject (no prompt) |
| `--force` | hash mismatch → apply without prompt |
| `--dry-run` | preview only, no changes |
| `--fuzzy` | if the exact anchor fails, use the nearest |
| `--no-fuzzy` | exact match only |
| `--backup` | take a backup before applying |

### 6-3. Pull rule for the AI

**The AI must follow this order:**

```
Step 1: python run.py --status
        ↓ (if insufficient)
Step 2: python run.py --file <relevant file>
        ↓ (if still needed)
Step 3: python run.py --all
```

**Never jump from step 1 straight to step 3 unless the user asked for it.**

### 6-4. `--status` output template

```
PROJECT: MyApp v1.2.3
LAST TAG: step-42-ok
MODIFIED FILES: src/main.py, src/utils.py
LAST ERROR: None
UNCOMMITTED: 3 files
```

~300 bytes.

### 6-5. `--file X` output template

```
FILE: src/main.py
HASH: a1b2c3d4e5f6...
SIZE: 1234 bytes
MODIFIED: 2026-10-07 14:30
---CONTENT---
[full file content]
```

### 6-6. `--all` output template

```
PROJECT: MyApp v1.2.3
LAST TAG: step-42-ok
GIT LOG: <last 10 commits>
GIT TAG: <last 10 tags>
GIT STATUS: <summary>

---TREE---
[project tree]

---FILES---
FILE: src/main.py
HASH: ...
---CONTENT---
...

FILE: src/utils.py
HASH: ...
---CONTENT---
...
```

---

## Section 6-B — Exact `run.py` parser spec

### 6-B-1. Recognized markers

The parser recognizes only these markers:

**Block headers (at column zero):**
- 3+ equals signs + type (FILE/CREATE/DELETE/MOVE/MKDIR/CMD/DUMP) + colon + path + 3+ equals signs.

**Inner markers (at column zero):**
- FIND — start of the old-text block.
- REPLACE — start of the new-text block.
- CONTENT — start of the new file's content.
- RUN — start of a CMD script.
- END — end of each block.
- EXPECTED_HASH — optional hash (same line as END).

### 6-B-2. Critical rules

1. **All markers must be at column zero** (no leading space).
2. **If a marker appears inside REPLACE/CONTENT content as a real marker, the parser closes the block early → the file is corrupted.**
3. **To show a marker in docs, indent it by 4 spaces** or wrap it in quotes.
4. **Block order matters** — they run in the order they appear.

### 6-B-3. Error behaviour

| Error | Behaviour |
|-------|-----------|
| Incomplete block (no END) | Parser ignores it |
| Target file not found | FAIL file not found |
| Anchor mismatch | fuzzy → suggest → FAIL |
| Hash mismatch | warning → apply (unless auto-verify) |
| File has invalid chars | write with utf-8 — no error |

### 6-B-4. Execution order

- CREATE, FILE, DELETE, MKDIR, CMD run in the order they appear.
- If MKDIR precedes CREATE, the folder is created first.
- If CMD precedes FILE, the command runs first — keep that in mind.

### 6-B-5. If the parser fails

1. Look at `_work/output.txt`.
2. The FAIL line says exactly where and which block.
3. SUGGEST shows the nearest text (percent similarity + line number).
4. If it's a parser error (not an anchor error), check `_work/input.txt` by hand — probably a marker at column zero inside content.

### 6-B-6. Why this section matters

Because the most common mistakes come from here:

- Putting a real END inside REPLACE (without indent).
- Putting a FILE header inside docs content.
- Using tab instead of space for a marker.

**Golden rule:** if unsure, indent the marker by 4 spaces. Always safe.

---

### 6-B-7. The input.txt golden rule

**Never fill `input.txt` with `output.txt` content.** That causes wrong patches to be applied.

**Rules:**

1. `input.txt` should always be **empty** — except during apply.
2. If `input.txt` is non-empty and you're not running, a patch is unfinished.
3. To check: `python run.py` (if input is full, it applies).
4. To empty manually: in VS Code, select all and delete.
5. **Never** copy `output.txt` output into `input.txt`.

**Danger sign:** if you see several `===== FILE =====` blocks tangled together in `run.py` output, `input.txt` was polluted. Empty `input.txt` and start over.

**Consequence of pollution:** wrong blocks get applied, unwanted commits appear, and you'll need to `git reset`.

---

## Section 7 — Standard Patch Template

### 7-1. Base template (with hash)

    ===== FILE: <relative path> =====
    <<<EXPECTED_HASH>>>a1b2c3d4...<<<END>>>
    <<<FIND>>>
    [exact text — character by character from the user's file]
    <<<REPLACE>>>
    [new text]
    <<<END>>>

### 7-2. Template without hash (if the user has no hash)

    ===== FILE: <relative path> =====
    <<<FIND>>>
    [exact text]
    <<<REPLACE>>>
    [new text]
    <<<END>>>

### 7-3. New-file template

    ===== CREATE: <relative path> =====
    <<<CONTENT>>>
    [full new-file content]
    <<<END>>>

### 7-4-A. File-move template (MOVE)

    ===== MOVE: <source path> -> <dest path> =====

**Rules:**
- If source doesn't exist → FAIL.
- If dest exists → FAIL (no overwrite).
- The dest folder is created automatically.

**Example:**

    ===== MOVE: src/old.py -> src/new/old.py =====

### 7-4. File-delete template

    ===== DELETE: <relative path> =====

### 7-5. Shell-command template

    ===== CMD: <short description> =====
    RUN
    <PowerShell/Bash script>
    END

### 7-6. Make-folder template

    ===== MKDIR: <relative path> =====

### 7-7. Important template notes

1. **Markers at column zero only** (no leading space).
2. **If a marker appears inside a patch's content, the parser misinterprets it.** Safe options:
   - Wrap in quotes: "the END marker"
   - Internal space: `< END >`
   - Indent to the right (4 spaces is the recommended amount).
3. **Patch order matters.** They run in the order they appear.

## Section 8 — Hash verification (tamper detection)

### 8-1. Why?

- **Prevent applying patches to already-modified code.**
- **Let the AI confirm its anchor is still valid.**
- **If the hash changed, the AI knows the user edited something — and can ask "what did you change?".**

### 8-2. Pattern

Every file in the dump:

    FILE: src/main.py
    HASH: a1b2c3d4e5f6...

The AI in the patch:

    ===== FILE: src/main.py =====
    <<<EXPECTED_HASH>>>a1b2c3d4e5f6...<<<END>>>
    <<<FIND>>>
    ...
    <<<REPLACE>>>
    ...
    <<<END>>>

### 8-3. `run.py` behaviour

1. Compute the file's current hash.
2. Compare with `EXPECTED_HASH`.
3. **Equal:** apply the patch.
4. **Not equal:**

    [WARN] Hash mismatch on src/main.py
    Expected: a1b2c3d4e5f6...
    Actual:   f9e8d7c6b5a4...
    Apply anyway? (y/N):

### 8-4. Related flags

    --auto-verify    # auto-reject on mismatch
    --force          # apply without prompt

### 8-5. Hash computation

    SHA256(file content + last-modified timestamp)

**Not just content** — because if someone swaps the content back and forth, the hash would stay the same. Adding the timestamp closes that hole.

---

## Section 8-B — Anti-block (MSG-SEED)

### 8-B-1. The real problem

DeepSeek and some other services are sensitive not just to too many messages, but to **similar** messages. If a user sends 10 messages like:

    [APPLY] PATCH_ID: 2
    [P2] [EDIT] FILE
      [OK] applied

the account is likely to get blocked.

**Critical rule:** every message must look unique.

### 8-B-2. Primary solution: MSG-SEED

`run.py` (v1.0+) writes a line at the top of every output:

    # MSG-SEED: <random hex>

**Send-to-AI pattern:**

    # MSG-SEED: a1b2c3d4
    [APPLY]
    PATCH_ID: 2
    ...

**Rules:**

- The first line of the message is the MSG-SEED.
- It changes every run.
- That line alone is enough for the AI to see the message as unique.

### 8-B-3. Complementary solution: batching

If you have 3 small patches, send them together, not one by one.

- Bad: message 1 patch A, message 2 patch B, message 3 patch C.
- Good: message 1 = patch A + B + C.

Benefit: message count drops by 3×.

### 8-B-4. Complementary solution: time spacing

Between two back-to-back messages, wait at least 30 seconds.

### 8-B-5. Complementary solution: structural variety

Vary the message shape occasionally:

- Sometimes start with MSG-SEED.
- Sometimes start with a different sentence.
- Sometimes send status, sometimes a file.

### 8-B-6. Final safe-message pattern

    # MSG-SEED: a1b2c3d4e5f6
    <short status: e.g. "previous patch succeeded">
    <output.txt content>

### 8-B-7. If you still get blocked

- **Account Warning:** usually temporary (30 min to 24 h).
- **Permanent ban:** rare.
- **Fix:** in a new account, follow this protocol from the start.

### 8-B-8. If the user wants to move very fast

**Recommendation:** instead of sending every tiny change, bundle:

- 5 patches → one message
- Each message carries a clear CTX-DELTA
- After every 3 messages, run a status

This is both faster and safer.

---

## Section 9 — Fuzzy matching (drift tolerance)

### 9-1. The problem

Anchors shift after changes.

### 9-2. Solution: three-level matching

    Level 1: exact match
    Level 2: rstrip (drop trailing whitespace)
    Level 3: strip (drop leading + trailing whitespace)
    Level 4: nearest block with similarity > 85%

### 9-3. Multi-line anchors

The anchor should not be **one line only** — include 2–3 lines above + 2–3 lines below:

    <<<FIND>>>
    def process_data(items):
        if not items:
            return []
        result = [transform(i) for i in items]
    <<<REPLACE>>>
    def process_data(items):
        if not items:
            return []
        result = [transform(i) for i in items if i is not None]

**Benefit:** even if lines above/below shift, these 5 lines stay glued together.

### 9-4. If fuzzy fails too

    [FAIL] Anchor not found in src/main.py
    Closest match at line 45 (85% similarity):
    <nearest text>

The AI can read this message and understand what happened.

---

## Section 10 — Context Update (mandatory)

> **🔴 This section is the project's heart against chat limits.**

### 10-1. Why?

- The user doesn't know whether the next message will hit the limit.
- If the context isn't updated, a new chat won't know where we were.

### 10-2. What to update in every message?

Every message with a real change:

1. **Code patch** (Section 7).
2. **Section 13 (Session Tracker)** — always.
3. **Section 15 (Red Lines)** — if a new red line was added.
4. **Section 16 (Git tag)** — if a new tag was added.
5. **Any other section** that changed.

### 10-3. Update pattern


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

## Section 13 - Session Tracker

> **Note:** This section is for your real project. **Send the document as a template, this section is filled in** with the project's real state.
> If using the document as a template (new project), **clear this section** and fill it in again.

### 13-1. Session Tracker

| Field | Value |
|-------|-------|
| **Last safe tag** | `v1.0.7` |
| **Last commit** | fix CI workflow (24 files) + issue templates |
| **Last work** | v1.0.7: CI checks all 24 READMEs + required files + language bars; issue templates added |
| **Next step** | Share on communities (Reddit, HN, awesome-lists); create GitHub Release v1.0.7 |
| **Current phase** | v1.0.7 — released |
| **Completion** | 100% EN (single self-contained rule doc) |
| **Last error** | none |
| **Open issues** | Distribution: share on communities; first real test-project |

### 13-2. Update

**This section must be updated in every AI message.**

### 13-3. Tag palette

| Color | Tag name | Meaning | When |
|-------|----------|---------|------|
| 🟠 | `safe-before-XX` | Rollback point | Before big changes |
| 🟢 | `step-XX-ok` | Verified by tests | After a passing test |
| 🟡 | `step-XX-wip` | Work in progress | Mid-work |
| 🔴 | `broken-XX` | Broken (do not return here) | For documentation |

### 13-4. Project tag table

| Tag | Description | Date |
|-----|-------------|------|
| `<tag-1>` | `<description>` | `<YYYY-MM-DD>` |
| `<tag-2>` | `<description>` | `<YYYY-MM-DD>` |

---

## Section 11 - The Big-Context Problem (solution)

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

## Section 12 - Special Characters & Escape

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

**Note:** `_archive/` is skipped by default — it is deliberately unmaintained (see Section 33-5). Pass explicit paths to scan it.

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

## Section 13-B — Inline CHANGELOG and ADR (optional)

If the document is short (under 2000 lines), keep history and decisions here. If it grows, move them to `CHANGELOG.md` and `ADR.md`.

### Inline CHANGELOG

| Tag | Description |
|-----|-------------|
| v1.0.0 | First release — base template |

### Inline ADR

**ADR-1: Using `run.py` to coordinate with the AI**

- **Decision:** all AI communication goes through `input.txt` / `output.txt` + `run.py`.
- **Reason:** avoid token burn, improve precision, resist chat limits.
- **Alternatives:** manual copy/paste, manual Ctrl+H.

**ADR-2: MSG-SEED mechanism**

- **Decision:** every message begins with a unique seed (random hex).
- **Reason:** DeepSeek and others are sensitive to similar messages and block accounts.
- **Alternatives:** time spacing, batching, structural variety.

**ADR-3: `input.txt` output as a single code block**

- **Decision:** the AI always gives `input.txt` as one code block (preferably with 4 backticks).
- **Reason:** a 3-backtick fence clashes with content that contains triple backticks.
- **Alternatives:** 5-backtick fence (hard to type), manual escape.

**ADR-4: File structure based on "one document, one tool"**

- **Decision:** keep the number of project files minimal.
- **Reason:** file clutter conflicts with the "one document" principle.
- **Alternatives:** multiple files (separate CHANGELOG, separate ADR, etc.).

**ADR-5: Directives `#@COMMIT:` and `#@TAG:` inside `input.txt`**

- **Decision:** commit message and tag are specified as directives inside `input.txt`, not as separate shell commands.
- **Reason:** fewer manual steps for the user, fewer tokens for the AI, and per the "everything in one block" rule (Section 4-15).
- **Alternatives:** separate `git` commands in chat (rejected — 3 extra messages, 2 extra chances for user error).

**ADR-6: `#@NEED:` for batched verification**

- **Decision:** the AI can request additional file dumps via `#@NEED: file X` inside `input.txt`.
- **Reason:** removes one full round trip per verification step.
- **Alternatives:** user manually runs `python run.py --file X` after applying (rejected — extra step).

**ADR-7: Auto-generated CTX-DELTA from `#@COMMIT:` / `#@TAG:` / `#@NEXT:`**

- **Decision:** after every successful apply, `run.py` writes `_work/ctx_delta.txt` from the directives, so the next chat can bootstrap without the AI having to retype it.
- **Reason:** the AI sometimes forgets the CTX-DELTA block (Section 10-6). Making `run.py` generate it removes the failure mode.
- **Alternatives:** AI must remember to write CTX-DELTA manually (rejected — that's the current failure); user must copy-paste (rejected — extra step).

**ADR-8: `--diff`, `--dry-run`, `--backup`, `--fuzzy`, `--no-fuzzy`**

- **Decision:** implement the flags that the doc already advertises, so doc and tool stay in sync.
- **Reason:** a documented-but-missing flag is worse than no documentation at all — the user loses trust.
- **Alternatives:** remove them from the doc (rejected — they're useful).

**ADR-9: Absolute I/O discipline as red line #0 (Section 0-C-10)**

- **Decision:** make "never leave the `input.txt` protocol" the biggest red line, above all others.
- **Reason:** every step outside the protocol is a chance for user error, a token cost, and — most importantly — a gap in the context. The project must survive chat limits, and the AI must not poke holes in the protocol.
- **Alternatives:** allow occasional out-of-band commands (rejected — the discipline must be absolute to be trustworthy).

**ADR-10: Mandatory ROADMAP in CTX-DELTA (Section 10-6)**

- **Decision:** every `[CTX-DELTA]` block must have NEXT **and** a 2+ item ROADMAP.
- **Reason:** a single NEXT field only survives one message. A ROADMAP survives three or more, letting consecutive chats bootstrap without ever asking the user "where were we?".
- **Alternatives:** NEXT-only (rejected — the failure mode is exactly what happened in this project); a long-form history log (rejected — token-heavy).

**ADR-11: `#@PUSH:` directive instead of manual `git push`**

- **Decision:** pushing to `origin` is a directive inside `input.txt` — not a manual shell command.
- **Reason:** Section 0-C-10 forbids the AI from giving commands outside `input.txt`. Pushing is a normal step; it belongs in the protocol.
- **Alternatives:** manual `git push` in chat (rejected — violates the discipline); auto-push on every commit (rejected — pushes should be opt-in).

**ADR-12: `--check-md` for nested fences (Section 12-8)**

- **Decision:** a local linting command scans every `.md` file for nested or unclosed fences.
- **Reason:** this bug silently corrupts documents and cost this project several patches. Detection must be one command, not a manual read.
- **Alternatives:** rely on review (rejected — the bug is invisible until the file is sent); use a third-party linter (rejected — adds a dependency).

**ADR-13: The user has exactly three actions (Section 0-C-10-A)**

- **Decision:** the user only (1) pastes into `input.txt`, (2) runs `python run.py`, (3) sends `output.txt`. No other step is allowed.
- **Reason:** every extra step is a chance for error, a token cost, and a break in the protocol. Verification, commits, pushes, and context updates belong inside `input.txt` as directives.
- **Alternatives:** allow the AI to add per-message checklists (rejected - that is exactly the pattern that was silently pushing work back onto the user).

**ADR-14: Verification runs inside `input.txt` via `#@POST:` - language-agnostic (Section 4-19)**

- **Decision:** the language-specific build/test commands live in `_work/config.json`, triggered by `#@POST: check` / `#@POST: verify` inside the patch. The user still runs only `python run.py`.
- **Reason:** this makes the same protocol work for Rust, Python, Node, Go, and any other language without ever leaving `input.txt`.
- **Alternatives:** a different workflow per language (rejected - the protocol must be universal); asking the user to run the language's native command (rejected - violates Section 0-C-10-A).

**ADR-15: Single-document policy - no translated rule documents (Section 33)**

- **Decision:** `PROJECT_CONTEXT.en.md` is the only rule document. Translated rule documents (e.g. `PROJECT_CONTEXT.fa.md`) are **not maintained**. Only READMEs may be translated.
- **Reason:** a translated rule document drifts out of sync within two patches; the reply-language is already handled by Section 0-C-9. Maintaining two rule documents duplicates effort for no benefit.
- **Alternatives:** maintain a Persian rule document in parallel (rejected - proven drift in this project); auto-generate translations on every patch (rejected - token-heavy, fragile).

**ADR-16: The tool is a reference, not a requirement (Section 0-C-13)**

- **Decision:** `run.py` (Python) is the **reference implementation** of the tool. The protocol it implements is language-neutral. The AI may rewrite the tool in the user's project language (Rust, Go, Node, C#, etc.) provided it behaves identically (same flags, same directives, same patch syntax, same output sections).
- **Reason:** the protocol is about discipline (files, patches, directives, MSG-SEED, auto-commit), not about Python. Forcing Python on a Rust project's user is a needless barrier. Documenting the rewrite contract keeps the protocol universal.
- **Alternatives:** mandate Python everywhere (rejected — excludes projects without a Python runtime); ship separate tools per language (rejected — maintenance burden, N× drift risk).

## Section 14 — Starting a New Chat

### 14-1. What to send

**Minimum:**
1. This document.
2. `python run.py --status` output.

**Ideal:**
1. This document.
2. `CHANGELOG.md` (last 100 lines).
3. `python run.py --status`.
4. If needed: `python run.py --all`.

### 14-2. Message pattern

```
Continuing the project. Here is the document and current state:

[paste document]

[paste --status output]

Goal of this chat: <one line>
```

### 14-3. What the AI should do

1. **Confirm it read the document** (one line).
2. **Understand where we are from the Session Tracker.**
3. **Without extra questions, give the next patch.**

### 14-4. What the AI should NOT ask

- ❌ "What did you do before?"
- ❌ "Which phase should I continue?"
- ❌ "Explain the project."
- ✅ "I read the document. Ready. What's the last error?"

---

## Section 15 — Red Lines

### 15-1. General red lines

**0. 🔴 The biggest red line — never leave the `input.txt` protocol.**
   No shell command outside `input.txt`. No manual edits. No alternate workflow.
   The AI's message contains only: one-line summary + one `input.txt` block + `[CTX-DELTA]` + reminder.
   See Section 0-C-10.

1. **Never change things on your own.**
2. **Never delete a file without user approval.**
3. **Never make a big change without a commit.**
4. **Never break the project-specific red lines (Section 2-4).**
5. **Never guess a library API.**
6. **Never touch a sacred function or module.**
7. **Never change the software version on your own.**
8. **Never modify a critical environment variable or config.**
9. **Never skip `[CTX-DELTA]`** — including NEXT and ROADMAP (Section 10-6).
10. **Never send a message without an `input.txt` block** unless the user asked a question, asked for context, or asked for an explanation (Section 0-C-7-3).

### 15-2. This document's red lines

1. **Never rewrite this entire document** — only the changed parts.
2. **Never place parser markers inside a patch body as real markers.**
3. **Never skip the context update in a message.**

### 15-3. If a red line is broken?

1. **Inform the user immediately.**
2. **Suggest a rollback:** `git reset --hard <tag-safe>`.
3. **Explain the reason** — one line.
4. **After rollback, retry.**

---

## Section 16 — Git Workflow

### 16-1. Standard flow

```bash
# Step 1 — before changes (orange)
git add -A
git commit -m "🟠 SAFE before step-XX: <description>"
git tag safe-before-XX

# Step 2 — code + context changes
# (code and PROJECT_CONTEXT.md together)

# Step 3 — after a passing test (green)
git add -A
git commit -m "🎉 step-XX: <description> + context updated"
git tag step-XX-ok
git push origin main
git push origin step-XX-ok

# Step 4 — on failure
git reset --hard safe-before-XX
```

### 16-2. Commit message pattern

```
🎉 step-XX: <short description> + context updated
🐛 step-XX: fix <bug name> + context updated
✨ step-XX: add <feature name> + context updated
🧹 step-XX: cleanup <name> + context updated
```

### 16-3. Important tags list

```
<recent tag>     ← description
```

### 16-4. Broken commits

```
<warning>  ← description of the breakage
```

---

## Section 17 — Testing

### 17-1. Types of tests

1. **Compile/run** — no errors.
2. **Unit** — a single function.
3. **Integration** — several modules.
4. **Usage** — a real scenario.
5. **Regression** — previous tests still pass.

### 17-2. Pattern

```
📌 Test:
1. <step one>
2. <step two>
3. <expected: what should happen>
4. <on error: what to send>
```

### 17-3. If a test fails

Answer these 5 questions:

1. **What exactly failed?** (error message)
2. **Where did it fail?** (file and line)
3. **When did it fail?** (after which change)
4. **What was expected?**
5. **What actually happened?**

---

## Section 18 — Bug Fixing

### 18-1. Steps

1. **Reproduce:** see the bug again.
2. **Isolate:** smallest code that shows it.
3. **Root-cause:** why?
4. **Fix:** minimal change.
5. **Test:** fix + no regression.
6. **Commit.**

### 18-2. Pattern

```
## 🐛 Fix — <bug name>

**Cause:** <one line>

🔍 Anchor (Ctrl+F):
[exact text]

✂️ Replacement:
[new text]

📌 Test: <how to test>

💾 Commit:
git add -A
git commit -m "🐛 step-XX: fix <name> + context updated"
git tag step-XX-ok
```

### 18-3. If it's unclear

Ask the user for:
1. **Reproduction steps.**
2. **Full log.**
3. **Environment.**

**Without these, don't touch the code.**

---

## Section 19 — Adding a Feature

### 19-1. Steps

1. **Design** and user approval.
2. **Split** into small steps.
3. **Implement each step** with a test.
4. **Document.**
5. **Final test.**

### 19-2. Design pattern

```
## 🎯 New feature: <name>

**Goal:** <one line>

**Steps:**
1. <step one>
2. <step two>

**Affected files:** <list>

**Red lines:** <list>

**Shall we start?**
```

## Section 20 — DeepSeek and the Others

### 20-1. Why DeepSeek?

DeepSeek performs best at executing the "copy and replace" method exactly, without touching code.

### 20-2. For DeepSeek

1. **Copy the anchor character-by-character** — don't build it from memory.
2. **If unsure, ask.** With the right flag.
3. **Keep replies concise.**
4. **Every message = one complete patch + context.**
5. **Don't put parser markers in the body.**
6. **Test reminder at the end.**

### 20-3. For others (Claude/GPT/Gemini)

Mandatory instructions:

1. **Don't touch the user's code except in FIND/REPLACE.**
2. **Copy the anchor character-by-character from the file.**
3. **Follow the reply structure exactly.**
4. **Don't send any extra code.**

### 20-4. If the AI fails

- Send a message reminding "only FIND/REPLACE".
- If it still fails, switch to DeepSeek.

---

## Section 21 — Code Quality Principles

### 21-1. Base principles

- **SOLID**
- **DRY** — each piece of logic once.
- **KISS** — the simplest solution.
- **YAGNI** — nothing you don't need yet.

### 21-2. Error handling

```python
try:
    risky_operation()
except SpecificException as e:
    logger.error(f"Error: {e}")
    handle_error(e)
except Exception as e:
    logger.exception("Unexpected error")
    raise
```

**Never leave a bare `except`.**

### 21-3. Naming

- Variables: `snake_case` / `camelCase`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### 21-4. Size

- Function: max 50 lines.
- File: max 1000 lines.
- Nesting: max 3 levels.

### 21-5. Comments

- **Why**, not **what**.
- `# TODO: <description>`
- `# FIXME: <description>`
- `# HACK: <description>`

---

## Section 22 — Logging & Error Handling

### 22-1. Log levels

- **DEBUG** — debugging.
- **INFO** — general.
- **WARNING** — warning.
- **ERROR** — error.
- **CRITICAL** — fatal.

### 22-2. Pattern

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
logger.info("Application started")
```

### 22-3. Crash logger

```python
import sys
import traceback

def install_crash_logger():
    def handler(exc_type, exc_value, exc_traceback):
        with open("crash_log.txt", "a", encoding="utf-8") as f:
            f.write("=" * 60 + "\n")
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=f)
    sys.excepthook = handler
```

### 22-4. What not to log

- Passwords.
- Tokens.
- Sensitive user data.

---

## Section 23 — Decision Tree

| User says | Step 1 | Step 2 | Step 3 |
|-----------|--------|--------|--------|
| "It doesn't work" | log | `--status` | `--file X` |
| "It errored" | full error text | traceback | `--file X` |
| "It got slow" | profile | resource usage | algorithm |
| "It crashed" | crash log | `--diff` | isolated test |
| "It was great" | confirm tag | ask next step | — |
| "I hit the limit" | document | `--status` | git status |
| "Go to X" | wait for file | exact anchor | code |
| "I sent the file" | read | anchor from it | code |
| "Not sure" | ask more precisely | offer options | wait |
| "Several tasks" | prioritize | one at a time | separate commits |

---

## Section 24 — Operational Checklists

### 24-1. Before any change

- [ ] I read the document.
- [ ] I saw `--status`.
- [ ] I know the red lines.
- [ ] I have the exact anchor.
- [ ] The replacement is clear.
- [ ] The test is defined.
- [ ] The commit is ready.

### 24-2. After each change

- [ ] Patch applied.
- [ ] Test done.
- [ ] Committed.
- [ ] Tagged.
- [ ] Context updated.

### 24-3. Before a new chat

- [ ] Document sent.
- [ ] `--status` sent.
- [ ] Chat goal clear.

### 24-4. Before release

- [ ] Tests pass.
- [ ] Version updated.
- [ ] Changelog written.
- [ ] Docs complete.

---

## Section 25 — Ready-Made Response Patterns

### 25-1. Adding a function

```
## 🔧 Add function `<name>`

🔍 Anchor (Ctrl+F):
<exact text>

✂️ Replacement:
<new text>

📌 Test: <how to test>

💾 Commit:
git add -A
git commit -m "✨ step-XX: add <name> + context updated"
git tag step-XX-ok
```

**Note:** since run.py v1.0+, the test/commit/tag go **inside** `input.txt` via `#@COMMIT:` and `#@TAG:` (Section 4-15). The above chat-style pattern is only for AI that don't support directives.

### 25-2. Removing code

```
## 🗑 Remove `<name>`

🔍 Anchor (Ctrl+F):
<whole block>

✂️ Replacement:
<without that block>
```

### 25-3. Full rewrite

    ## 📄 Full rewrite of `<filename>`

    **Reason:** <one line>

    ===== CREATE: <path> =====
    <<<CONTENT>>>
    <full new content>
    <<<END>>>

### 25-4. Fixing an error

    ## 🐛 Fix — <error name>

    **Cause:** <one line>

    🔍 Anchor (Ctrl+F):
    <text>

    ✂️ Replacement:
    <new text>

### 25-5. DeepSeek special pattern

    📌 Summary: <one line>

    🔍 Anchor (Ctrl+F):
    <text>

    ✂️ Replacement:
    <new text>

    📌 Test: <how to test>

    💾 Commit: <command>

    ---
    If there was an error: run `python run.py` and send `_work/output.txt`.

### 25-6. The standard AI message (with directives)

Since run.py v1.0+ (Sections 4-15 and 5-0-4), the canonical AI message contains **only**:

1. **📌 One-line summary.**
2. **A single code block with the whole `input.txt`** — starting with `#@COMMIT:` and `#@TAG:`, then the patch blocks.
3. **`[CTX-DELTA]` block.**
4. **The end-of-message reminder.**

Nothing else. No separate test command, no separate commit command. All of it lives inside `input.txt`.

### 25-7. AUTODUMP control (`#@NODUMP:` and `#@DUMP:`)

When a patch fails, `run.py` appends an AUTODUMP block with the failed file's content — to help the AI re-anchor. For large files this can be very long.

- `#@NODUMP:` — suppress AUTODUMP entirely for this run.
- `#@DUMP: compact` — show first 25 + last 25 lines of each failed file (default).
- `#@DUMP: full` — show the whole file (like the old behaviour).
- `#@DUMP: off` — same as `#@NODUMP:`.

**Rule of thumb:** for small projects (<500 lines per file), `compact` is fine. For big files, add `#@NODUMP:` and re-anchor manually with `python run.py --file X`.

## Section 26 — Appendix: Full Examples

### 26-1. `run.py` reference

> **Note:** `run.py` is the **Python reference implementation**. The protocol it implements is language-neutral — the AI may rewrite the tool in the user's project language (Section 0-C-13).

The full reference implementation of `run.py` lives in this project's root as `run.py`. It supports:

- All flags in Section 6.
- All patch types in Section 7.
- All directives in Section 5-0-4 (`#@ID`, `#@CMD`, `#@POST`, `#@NEED`, `#@COMMIT`, `#@TAG`, `#@NODUMP`, `#@DUMP`).
- MSG-SEED on every output.
- Rate warnings between fast runs.
- Compact autodump of failed files (first 25 + last 25 lines).
- Auto-commit + auto-tag on `FAIL: 0`.

If you're starting from scratch, copy the minimal version from Section 35 and let the AI upgrade it step by step.

### 26-2. A complete patch example

    ===== FILE: src/main.py =====
    <<<EXPECTED_HASH>>>a1b2c3d4e5f6<<<END>>>
    <<<FIND>>>
    def validate_phone(phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone) is not None
    <<<REPLACE>>>
    def validate_phone(phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone) is not None


    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    <<<END>>>

### 26-3. A new-chat message

    Continuing the project. Here is the document and current state:

    [paste document]

    [paste python run.py --status output]

    Goal of this chat: continue adding tests.

### 26-4. A complete AI message with directives

See Section 5-0-4 for the directive list and Section 25-6 for the message shape.

A minimal real example (indent = 4 spaces, no nested fences):

    # INPUT: add validate_email
    #@COMMIT: ✨ step-15: add validate_email
    #@TAG: step-15-ok
    #@POST: verify
    #@NEED: file src/utils.py

    ===== FILE: src/main.py =====
    <<<FIND>>>
    def validate_phone(phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone) is not None
    <<<REPLACE>>>
    def validate_phone(phone):
        pattern = r'^\+?[0-9]{10,15}$'
        return re.match(pattern, phone) is not None


    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    <<<END>>>

    [CTX-DELTA]
    TAG: step-15-ok
    WORK: add validate_email
    NEXT: add validate_url
    FILES: src/main.py
    [/CTX-DELTA]

    ---
    If there was an error: run `python run.py` and send `_work/output.txt`.

---

## Section 28 — Anti-Patterns

### 28-1. Anti-patterns for the AI

| Anti-pattern | Why bad | Alternative |
|--------------|---------|-------------|
| Rewriting the whole file | Loses the user's code | FIND/REPLACE only |
| Anchor from memory | Mismatch errors | Anchor from the real file |
| Adding an unapproved feature | Out of scope | Ask, then patch |
| Long explanation | Token waste | One line is enough |
| Parser marker in content | File corruption | 4-space indent |
| Unsolicited suggestions | Annoyance | Only when asked |
| "Maybe" and "it seems" | Uncertainty | Definite and precise |
| Guessing a library API | Runtime error | Ask for docs |
| Forgetting the context | Hit the limit | CTX-DELTA in every message |
| Forgetting the commit | Lost changes | `#@COMMIT:` in every patch |
| Many tiny `input.txt` files | Account-block risk | Batch 2–4 patches per file |
| Test/commit in chat | Extra manual step | Use `#@COMMIT:` / `#@TAG:` |
| Full autodump of huge files | Token waste on errors | `#@NODUMP:` or compact mode |
| Nested markdown fences in docs | Renders as garbage | 4-space indent only |

### 28-2. Anti-patterns for the user

| Anti-pattern | Why bad | Alternative |
|--------------|---------|-------------|
| Applying code without understanding | Future bugs | Ask the AI to explain |
| Applying code without testing | Breaks the healthy version | Always test |
| Applying code without committing | Hard to roll back | tag + commit |
| Sending similar messages | Account blocking | MSG-SEED + batching |
| Ignoring dump errors | Problem persists | Look with `--errors` |
| Running unknown commands | Security risk | Ask for explanation first |
| Ignoring red lines | Project damage | Read Section 15 |
| Forgetting backups | Data loss | tag + cp -r |

### 28-3. Anti-patterns for the project

| Anti-pattern | Why bad | Alternative |
|--------------|---------|-------------|
| Duplicate code | Tech debt | Shared function |
| Hard-coded paths | Portability | pathlib |
| Hard-coded language | No i18n | Translation file |
| No try/except | Crashes | Error handling |
| No logging | Hard to debug | logger |
| No tests | Regressions | Unit tests |
| 5000-line file | Hard to read | Modular |
| 200-line function | Hard to test | Split into smaller |
| No docs | The next dev is lost | docstring |

---

## Section 29 — Definition of Done

### 29-1. When is a task done?

A task is considered done only when:

1. Code is written.
2. Compiles/runs without errors.
3. Test performed.
4. Exact anchor saved (in `applied/`).
5. Context updated (CTX-DELTA + sections).
6. Committed with a proper message.
7. Tagged (`step-XX-ok`).
8. User confirmed — not just the AI.
9. In-code docs updated (docstring, comments).
10. Registered in CHANGELOG (if the project is large).

### 29-2. When is a phase done?

1. All tasks pass Definition of Done.
2. Regression tests run — nothing broke.
3. User confirmed.
4. Phase tag created (`phase-N-done`).
5. Phase context recorded.

### 29-3. When is a version ready?

1. All phases done.
2. Full tests done.
3. Docs complete.
4. CHANGELOG up to date.
5. README up to date.
6. No open errors.
7. No unmotivated TODOs.
8. No dead code.
9. Rollback-able (`git tag vX.Y.Z`).
10. User final approval.

### 29-4. What violates Definition of Done?

- "I'll comment later."
- "Test later."
- "I'll leave this file temporarily."
- "Commit later."
- "Context later."
- "Docs later."

**Rule:** every "later" is tech debt. If a task is done, all the "later"s must be done too.

### 29-5. Exception tasks

Some tasks have a simpler Definition of Done:

- Research task: just a short report + findings.
- Documentation task: just the updated file + confirmation.
- Design task: just an ADR or document.

**Rule:** even exception tasks must be committed.

---

## Section 30 — Troubleshooting

### 30-1. Common `run.py` errors

| Error | Cause | Fix |
|-------|-------|-----|
| `anchor not found` | FIND text doesn't match file | Run `python run.py --file X` and copy the anchor from reality |
| `hash mismatch` | File changed after the patch | `--force` or `--auto-verify` |
| `file not found` | Wrong path | Check the path in the header |
| `SyntaxError` in output | Parser misinterpreted | Check markers aren't at column zero |
| `empty anchor` | Empty FIND | Copy FIND from the real file |
| `already applied` | Patch is being reapplied | Fine — it's skipped |
| `timeout 900s` | CMD ran too long | Shorten the CMD or run manually |
| `NameError` in run.py | Module not imported | Check imports |
| `PermissionError` | File locked | Close the program holding it |
| `UnicodeDecodeError` | Wrong encoding | Save the file as UTF-8 |
| `output.txt` too long | Autodump dumped a huge file | Use `#@NODUMP:` or `#@DUMP: compact` |

### 30-2. Step-by-step debugging

If `python run.py` errored:

1. `python run.py --file _work/output.txt` → see the full error.
2. `python run.py --file <failing file>` → see the real anchor.
3. If needed: `python run.py --status` → overview.
4. If all else fails: `git log --oneline -5` → last healthy commit.

### 30-3. Emergency recovery

If the project crashes or files are corrupted:

1. `git status` → see what changed.
2. `git log --oneline -10` → last healthy commits.
3. `git reset --hard <last-safe-tag>` → full rollback.
4. If uncommitted files mattered: `git stash` first, then reset, then `git stash pop`.

### 30-4. If the AI broke once

1. **Don't wait.** Roll back immediately.
2. **Ask why.** Why was the anchor wrong?
3. **Retry.** This time with the correct anchor.

**Golden rule:** every failure is a lesson. Don't make the same mistake twice.

---

## Section 31 — Setup & Project Management

### 31-1. Small/Medium/Large modes

**If your project is small (< 500 lines):**
- Read only these sections: 0, 1, 2, 4, 5, 7, 10, 13, 14, 15, 16, 23, 24
- Ignore: hash, fuzzy, CTX-DELTA, CHANGELOG, ADR
- Enough: simple `run.py` + anchor/replace

**If medium (500–5000 lines):**
- All sections except CHANGELOG/ADR
- Use flags
- Take MSG-SEED seriously

**If large (> 5000 lines):**
- All sections
- Hash verification
- CTX-DELTA in every message
- Pull, not Push, always

### 31-2. First-time setup

**Fast method (recommended):**

If you have `run.py` in the root:

    python run.py --init

This creates:
- `_work/` and `_work/applied/`
- `.gitignore` (if missing)
- Empty `input.txt` and `output.txt`

**AI-mediated method (for newcomers):**

The user gives only `PROJECT_CONTEXT.md` to the AI. The AI guides step by step:

1. AI asks: "What files do you have?"
2. If `run.py` missing: copy from Section 35.
3. If Python missing: install-Python guide.
4. `python run.py --init`.
5. Fill Sections 2 and 13.

**Rule:** the user never runs a command manually — unless the AI said so.

**Manual method (if all else fails):**

**Step 1:** Put this document in the project root: `PROJECT_CONTEXT.md`.

**Step 2:** Create `_work/`:

    _work/
    ├── input.txt      (empty)
    ├── output.txt     (empty)
    ├── applied/       (empty)
    └── cache.json     (optional)

**Step 3:** Take `run.py` from Section 35 and put it in the root.

**Step 4:** Create `.gitignore`:

    _work/input.txt
    _work/output.txt
    _work/applied/
    _work/cache.json

**Step 5:** Fill Section 2 (Identity) of this document.

**Step 6:** Fill Section 2-4 (project-specific red lines).

**Step 7:** Fill Section 13 (Session Tracker).

**Step 8:** Create `CHANGELOG.md` and `ADR.md` (if the project is large).

**Step 9:** git init + first commit + first tag:

    git init
    git add -A
    git commit -m "initial commit"
    git tag v0.1.0

**Step 10:** Ready. Take your first patch from the AI.

### 31-3. Backup protocol

Before any big change:

    git tag safe-before-XX
    cp -r <important folder> <important folder>-backup-XX

If the project is large, use `git stash`:

    git stash push -m "before big change"

After success: `git stash drop`. After failure: `git stash pop`.

**Rule:** before a big change, always have a rollback point. A `git tag` is enough for code, but if non-code files change too, `cp -r` is needed.

### 31-4. Doc integrity — how to tell the document hasn't broken

`PROJECT_CONTEXT.md` has two kinds of sections:

**Stable sections (must not change without approval):**
- Section 3 (philosophy)
- Section 4 (golden rules)
- Section 5 (workflow)
- Section 6 (flags)
- Section 6-B (parser)
- Section 7 (patch template)
- Section 8 (hash)
- Section 9 (matching)
- Section 10 (context)
- Section 12 (escape)
- Section 15 (red lines)
- Section 23 (decision tree)
- Section 24 (checklist)
- Section 25 (patterns)

**Variable sections (may change):**
- Section 2 (Identity)
- Section 13 (Session Tracker)
- Section 16 (Git)
- `CHANGELOG.md`
- `ADR.md`

**Rule:** changes are only allowed in variable sections. If the AI wants to change a stable section, user approval is required.

### 31-5. Common document bugs and fixes

| Bug | Cause | Fix |
|-----|-------|-----|
| ToC out of order | markdown escape | Manual check |
| Duplicate section | Patch reapplied | `git diff` |
| Parser marker inside content | The AI erred | `git reset --hard safe-before-XX` |
| Anchor not found | File text changed | `python run.py --file PROJECT_CONTEXT.md` |
| Document grew huge | History accumulated | Move to `CHANGELOG.md` |
| Content eaten by markdown | Nested fences | Use 4-space indent only |

### 31-6. When to rewrite the document?

**Rule of 3 patches:** if more than 3 patches have been applied to a section, that section should be **rewritten from scratch**.
**Reason:** accumulated patches create contradictions.

**Never on your own.** Only if:

1. Document > 5000 lines.
2. Main structure broke.
3. Library or language changed.
4. User explicitly asked.

**Before rewriting:**
- `git tag safe-before-rewrite-context`
- Print the current document.
- Gradual rewrite.
- User approval at each step.

## Section 32 — Quick Start Walkthrough (zero to first patch)

### 32-1. Prerequisites

- An empty folder (new project) or an existing project
- An AI (DeepSeek is recommended — it executes anchor/replace most precisely)
- A runner for the tool:
  - **Python 3.8 or newer** (default — the reference tool is `run.py`), **or**
  - **The project's own language toolchain** (Rust, Node, Go, etc.) — if the AI rewrites the tool (Section 0-C-13)

### 32-2. Steps

**Step 1 — Create the base structure**

In the project root:

    python run.py --init

That creates `_work/`, `_work/applied/`, an empty `.gitignore`, and empty `input.txt` / `output.txt`.

**Step 2 — Place this document**

`PROJECT_CONTEXT.md` (this file) goes in the project root.

**Step 3 — Ensure `run.py` exists**

The full `run.py` source is embedded in Section 35 of this document. If you don't have `run.py` yet, ask the AI: "Bootstrap `run.py` from Section 35." The AI emits it as a CREATE patch. Save it as `run.py` in the project root.

**Step 4 — Smoke test**

    python run.py --version
    python run.py --status

If both run without errors, you're ready.

**Step 5 — First chat with the AI**

Paste this document into the chat and send:

    New project. This document is the rulebook.
    run.py is installed.
    Goal: <one-line description>
    First feature: <one-line description>

**Step 6 — Receive a patch**

The AI returns a block starting with `#@COMMIT:` and `#@TAG:`. Drop the whole block into `_work/input.txt`.

**Step 7 — Apply**

    python run.py

On success, the run commits and tags automatically.

**Step 8 — Send status back to the AI**

    python run.py --status

Paste the output into the chat.

**Step 9 — Repeat**

Back to Step 6. Every AI message = one patch. Every patch = one commit + tag.

### 32-3. Success indicators

- Every patch applies without FAIL.
- `output.txt` starts with `# MSG-SEED:`.
- The AI's reply ends with `[CTX-DELTA]`.
- git tags accumulate in order.

### 32-4. Quick debugging

| Problem | Fix |
|---------|-----|
| `python` not recognized | Is Python installed? Is it on PATH? |
| `anchor not found` | Run `python run.py --file X` and copy the anchor from the real file |
| `input.txt` not applied | Save the file as UTF-8 |
| AI doesn't give a patch | Did you paste this document? |
| Chat hit the limit | Open a new chat, send document + `--status` |
| `_work` not found | Run `python run.py --init` |

### 32-5. Golden rule

> **No test, no commit. No commit, no next patch.**

---

## Section 33 — Localization Policy (single document, multi-language replies)

> **🔴 There is only ONE rule document: `PROJECT_CONTEXT.en.md` (English).**
> **Do NOT maintain translated versions of the rule document.**

### 33-1. The single-document rule

The rule document lives in **English only** — so that:

1. Any AI (DeepSeek, Claude, GPT, Gemini) parses it identically.
2. Parser markers, file names, tags, and commands stay byte-identical across all users.
3. There is exactly one source of truth to update — no drift between languages.

**No `PROJECT_CONTEXT.fa.md`, no `.ar.md`, no `.zh.md`, no other rule-document translations.** Only the English one.

### 33-2. How multi-language still works

The document is English — but the **conversation** is in the user's language.

- The AI detects the user's language from their first message (Section 0-C-1).
- The AI replies in that language.
- The AI asks once if the language is ambiguous.
- The AI never translates the `input.txt` / `output.txt` blocks — those stay in the language-neutral protocol (English keys, English tags, English file names).

This is the whole point of Section 0-C-9 and Section 0-C-12. The document's language ≠ the reply's language.

### 33-3. What CAN be translated

Only **discovery documents** — never the rule document:

| File | Translate? | Note |
|------|------------|------|
| README.md | ✅ Recommended | GitHub landing page — one file per language |
| LICENSE | ❌ No | Legal text stays English |
| run.py | ❌ No | Code — its docstring is enough |
| PROJECT_CONTEXT.en.md | ❌ No | The single source of truth — English only |

**Naming pattern for READMEs:**

    README.md        ← primary (English)
    README.fa.md     ← Persian
    README.ar.md     ← Arabic
    README.zh.md     ← Chinese

### 33-4. Translating a README — practical pattern

**Step 1:** Keep `README.md` as the primary.

**Step 2:** At the top of each README, link the languages:

    <p align="center">
      <b>English</b> ·
      <a href="README.fa.md">فارسی</a> ·
      <a href="README.ar.md">العربية</a>
    </p>

**Step 3:** Create the new file (`README.fa.md`, etc.).

**Step 4:** Translate freely, but leave unchanged:
- File names: `run.py`, `PROJECT_CONTEXT.en.md`.
- Commands: `git clone ...`, `python run.py --status`.
- Tag names: `v1.1.0`.

### 33-5. If a rule-document translation already exists

If someone already created `PROJECT_CONTEXT.<lang>.md` or a translated `PROJECT_CONTEXT.md`:

- Move it to `_archive/` (e.g. `_archive/PROJECT_CONTEXT.fa.md`).
- Do not link to it from the main README.
- Do not maintain it.
- The archive is only for reference and for the git history.

**Reason:** a translated rule document drifts out of sync within two patches. The cost of maintenance is not worth the benefit — the reply language is already handled by Section 0-C-9.

### 33-6. Contributing a translation

**Translations of the rule document are not accepted.** PRs adding `PROJECT_CONTEXT.<lang>.md` will be closed with a pointer to this section.

**Translations of the README are welcome.** Follow Section 33-4.

---

## Section 34 — First-Time User Checklist

### 34-1. If you're new

Before doing anything, walk through this checklist:

- [ ] I opened `PROJECT_CONTEXT.md` and read Section 1.
- [ ] I placed `run.py` in the root.
- [ ] I ran `python run.py --init`.
- [ ] `.gitignore` exists (or I used the template).
- [ ] I ran `git init` and made the first commit.
- [ ] `python run.py --version` works.
- [ ] `python run.py --status` works.
- [ ] I filled Section 2 (Identity).
- [ ] I filled Section 2-4 (red lines).
- [ ] I filled Section 13 (Session Tracker).
- [ ] I opened the first chat with the AI and sent document + goal.

### 34-2. Success indicators

When everything is right:

- Every AI patch applies without FAIL.
- `output.txt` starts with `# MSG-SEED`.
- Every AI reply ends with `[CTX-DELTA]`.
- Every change gets an automatic commit.
- git tags accumulate in order.

### 34-3. If something doesn't work

In order:

1. `python run.py --errors` — see which patch failed.
2. `python run.py --file <failing file>` — see the real anchor.
3. `git log --oneline -10` — find the last healthy commit.
4. `git reset --hard <last-safe-tag>` — roll back.

**If none of these work:** open a new chat, send document + `--status` + the error text.

### 34-4. Golden tips

1. **Always pull, not push.** `--status` first, `--file X` second, `dump --full` last.
2. **Every AI message must have `[CTX-DELTA]`.** If not, remind it.
3. **Keep the MSG-SEED.** It's your anti-block shield.
4. **Space out messages.** At least 30 seconds between sends.
5. **No commit without a test.**
6. **No next patch without a commit.**

### 34-5. Wrap-up

If all checklists pass, **your project is ready.**

Follow the rules in this document, and the AI always knows where it is, what it needs, and how to help.

**Good luck.**

---

## Section 35 - Full `run.py` source (Python reference)

> **One-file distribution.** This section contains the entire `run.py`. A newcomer who only has this document can be bootstrapped by an AI that emits the block below as a CREATE patch inside `input.txt`.

> **Never hand-copy this block.** Always let the AI emit it as a CREATE patch, so the protocol (Section 0-C-10) is respected.

> **Mature projects:** Section 35 is only needed once. If the document feels too large for your chat, trim this section from your local copy after `run.py` exists. The rest of the document is unaffected.

`````python
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

VERSION = "1.2.0"

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
`````

### 35-1. Bootstrap procedure (what the AI does)

1. Read the code block above.
2. Emit it as a CREATE patch inside `input.txt`.
3. Add `#@COMMIT: bootstrap run.py` and `#@TAG: bootstrap-runpy-ok` at the top.
4. The user saves the block as `run.py` and runs `python run.py --init`.

### 35-2. Bootstrap procedure (what the user does)

1. Save the AI block into a file called `run.py` in the project folder. This is the only manual save in the entire protocol, it happens once, before `input.txt` exists.
2. Run `python run.py --init`.
3. Done. From here on, follow Section 0-C-10-A: paste, run, send.

---

## Section 36 — Rate-Limit Mitigation

> **🔴 How to work fast without getting blocked by the chat provider.**

### 36-1. The problem

DeepSeek, Claude, OpenAI, and others throttle messages that arrive too fast, or that look too similar to each other. Local tools (`run.py`) don't have any such limit — only the **chat service** does.

Symptoms:

- `Messages too frequent. Try again later.`
- `Rate limit exceeded.`
- `Account warning` (temporary).

### 36-2. Six mitigations (ranked by impact)

1. **Batch.** One big `input.txt` with 2–4 patches beats 4 small ones. Same for questions: one message with 2 questions beats 2 messages with 1. See Section 4-16.

2. **MSG-SEED.** `run.py` writes a fresh `# MSG-SEED:` line at the top of every output. Paste the output including that line — each message looks unique.

3. **Time spacing.** Wait at least 30 seconds between sends. `run.py` prints a `RATE WARN:` line if you ran it under 25 seconds ago — respect it.

4. **Structural variety.** Don't send the exact same shape every time. Sometimes start with `--status`, sometimes with `--file X`, sometimes with a one-line prose summary before the block.

5. **Batch questions.** If you have 3 things to ask, put them in one message. The chat provider counts *messages*, not *tokens*.

6. **Switch models occasionally.** If you hit a hard limit on one provider, switch to another for an hour. The limit is per-account.

### 36-3. What does NOT help

- Sending the same message again immediately — makes it worse.
- Removing the MSG-SEED — makes the messages look identical.
- Splitting a patch into more, smaller messages — multiplies the rate.
- Using `clear` to hide the log — no effect on the chat provider.

### 36-4. Emergency plan

If you get `Messages too frequent`:

1. **Stop sending.** Don't retry.
2. **Wait 5–15 minutes.** The local run already worked — you have the `output.txt` ready.
3. **Come back with one batched message.** The MSG-SEED alone makes it unique.
4. **If the block persists:** wait 30 minutes, then try a different model in the same provider, or a different provider.

### 36-5. Long-term pattern

For a project that will run for days:

- Batch aggressively — one message every 5–10 minutes, not every 30 seconds.
- Keep a local note of what each patch did — the `output.txt` archive in `_work/applied/` is already that.
- After every 3–4 messages, take a break of a few minutes.

**Rule of thumb:** treat every chat message as expensive. Make it count.

---

## Section 37 — Uploading to GitHub

> **A short guide to pushing the project to GitHub for the first time and keeping it in sync.**

### 37-1. First-time upload

If the project is not yet on GitHub:

    git init
    git add -A
    git commit -m "initial commit"
    git branch -M main
    git remote add origin https://github.com/<user>/<repo>.git
    git push -u origin main

### 37-2. Everyday push

After every batch of local commits:

    git push origin main
    git push origin --tags

`--tags` pushes local tags so the remote keeps the same safe-point history.

### 37-3. Everyday pull

Before starting a session on a machine that might be behind:

    git pull --rebase

If there are unstaged changes:

    git stash
    git pull --rebase
    git stash pop

### 37-4. What should NOT be pushed

`.gitignore` should already exclude:

- `_work/input.txt`, `_work/output.txt`
- `_work/applied/`
- `_work/cache.json`, `_work/.patch_id`, `_work/.last_run`
- `__pycache__/`, `*.pyc`
- `.venv/`, `venv/`
- build artefacts

**If any of them got committed before `.gitignore` was set up:** untrack them without deleting locally:

    git rm -r --cached _work
    git commit -m "chore: untrack _work runtime files"

### 37-5. Recovery if a bad commit was pushed

If the bad commit is the latest and no one has pulled it:

    git reset --hard HEAD~1
    git push --force-with-lease origin main

**Never** force-push to a shared branch without `--force-with-lease`.

### 37-6. Keeping remote and local in sync

Check the state:

    git status
    git log --oneline -5
    git remote -v
    git branch -vv

The `branch -vv` line shows whether local `main` is ahead or behind `origin/main`.

---

*End of PROJECT_CONTEXT.en.md — 2026 edition.*