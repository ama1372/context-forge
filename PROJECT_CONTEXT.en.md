# 📘 PROJECT_CONTEXT.md — Final Edition

<!-- AUTO:START -->
## Last patch (auto - do not edit)

| Field | Value |
|-------|-------|
| Last patch | P112 |
| Last commit | `3d2b008` |
| Time | 2026-10-09 14:29 |
| MSG-SEED | `de96a8d6` |
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
- **Section 33** — Localization Guide
- **Section 34** — First-Time User Checklist
- **Section 35** — Minimal `run.py`
- **Section 36** — Rate-Limit Mitigation
- **Section 37** — Uploading to GitHub

---

## Section 0-B — Project File Guide

> **This document is the heart of the project. Everything else is just support.**

### Core files (required)

| File | Role | Delete? |
|------|------|---------|
| PROJECT_CONTEXT.md | The constitution — everything is here | ❌ |
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
> "First install Python: python.org/downloads — then we continue."

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
| **Programming language** | `<e.g. Python 3.11>` |
| **Framework / main libraries** | `<e.g. PyQt5, requests>` |
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
├── run.py                  ← dump/apply tool
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
3. Build run.py from the template in Section 35
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

The new AI doesn't know where we are → the user must re-explain from scratch → wasted time.

### 10-5. Golden rule

> **Every AI message = one code patch + one context patch.**
> If the context patch is missing, the message is incomplete.

### 10-6. CTX-DELTA — the anti-amnesia mechanism

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
- **Always include NEXT** — never leave it blank.
- **Always include ROADMAP** — at least 2 future steps. Even if the project is ending, write `ROADMAP: (none — release complete)`.
- Always list FILES — even if empty, write `FILES: (none)`.
- Big change → also update the context paragraphs.
- Small change → CTX-DELTA alone is enough.

**Why ROADMAP is mandatory:** the next chat may open with only this block. If it contains only `NEXT`, the AI after the next message loses the trail again. With a 3-step ROADMAP, three consecutive chats can bootstrap cleanly without ever asking the user "where were we?". This is the whole point of the anti-amnesia design — it must survive more than one message.

**What the AI must never do:**

- ❌ Write `NEXT: (unspecified)` — if you don't know, guess a plausible next step and mark it with `?`.
- ❌ Skip ROADMAP because "it's just a small patch".
- ❌ Put the ROADMAP in prose instead of the block — `run.py` reads the block, not your prose.

**Benefits:**

- If the AI forgets the main context, this block is a lifesaver.
- The user sees at a glance whether the AI is working properly.
- In a new chat, CTX-DELTA alone can bootstrap continuation.
- `run.py` saves this block automatically to `_work/ctx_delta.txt` after every successful apply — so the user can retrieve it with `python run.py --ctx` at any time.

### 10-7. Complete AI message pattern

Every AI message must have this structure:

1. **📌 Summary** — one line.
2. **Code patch** — template in Section 7.
3. **📌 Test** — what to test and how.
4. **💾 Commit** — ready-made command.
5. **Context** — if the change is big, a PROJECT_CONTEXT.md patch.
6. **[CTX-DELTA]** — always.
7. **End-of-message reminder** — "If there was an error: ...".

**Note:** Since run.py v1.0+ supports `#@COMMIT:` and `#@TAG:` directives, steps 3–4 are folded **inside** `input.txt`. See Section 4-15. The AI writes only `input.txt` + the CTX-DELTA block + the reminder.

---

## Section 11 — The Big-Context Problem (solution)

### 11-1. The problem

If this document reaches 5000 lines, sending it every time itself burns tokens.

### 11-2. Solution: three layers

**Layer 1 — main document (this file):**
- This document is **complete** and **stable**.
- Only Sections 2, 13, 15, 16 change.
- Sending it once is enough.

**Layer 2 — separate CHANGELOG.md:**
- Full history of changes.
- The AI reads it only when needed.
- Included in `_work/output.txt`.

**Layer 3 — ADR.md (Architecture Decision Records):**
- Past architectural decisions.
- Only for a new AI that wants to understand the "whys".

### 11-3. Practical pattern

**Every new chat:**

    1. This document (PROJECT_CONTEXT.md)
    2. CHANGELOG.md (last 100 lines)
    3. python run.py --status
    4. If needed: python run.py --all

**Savings:** ~30% tokens compared to sending everything.

### 11-4. How big should the document be?

- **Minimum:** 500 lines (start).
- **Ideal:** 2000–3000 lines.
- **Maximum:** 5000 lines (beyond this, it burns tokens).

**If it grows past that:**
- Historical sections → CHANGELOG.md
- ADRs → ADR.md
- Only active rules stay in the main document.

---

## Section 12 — Special Characters & Escape

### 12-1. The problem

Triple backticks (` ``` `), asterisks (`*`), and other markdown characters cause rendering issues.

### 12-2. Solution: the markers rule

**1. Parser markers (FILE, FIND, REPLACE, END, CONTENT, RUN) must never appear in a patch body as real markers.**

**2. If you must show a marker:**

- ✅ Wrap in quotes: "the END marker"
- ✅ Internal space: `< END >`
- ✅ Indent by 4 spaces: `    ===== FILE =====` (parser only sees column zero)

**3. If the file content contains triple backticks:**

Use `<<<FIND>>>` / `<<<REPLACE>>>` — no outer markdown.

    ===== FILE: src/README.md =====
    <<<FIND>>>
    This is a code block:
    ```
    print("hello")
    ```
    <<<REPLACE>>>
    This is an updated code block:
    ```
    print("hello world")
    ```
    <<<END>>>

### 12-3. Safe markdown template

If the patch contains markdown, **always** use the `===== FILE =====` shell — not triple backticks.

### 12-4. Pre-send test

Before sending a message, check:

- [ ] No unmatched ` ``` ` in the text.
- [ ] No `===== ` inside a patch body.
- [ ] No `<<<` without a matching `>>>`.

### 12-5. If `run.py` reports a parser error

    [FAIL] Parser error: unterminated block
    Line 45: <<<FIND>>>
    Reason: next ===== FILE ===== found before <<<END>>>

**Cause:** a marker likely appeared in the body. The user must check by hand.

---

### 12-7. Never nest fences in the English document

> **New red line for `PROJECT_CONTEXT.en.md` itself.**

**Forbidden:** any triple-backtick or multi-backtick fence nested inside another fence in this document.

**Reason:** markdown collapses nested fences — the outer fence closes at the first inner fence whose length is ≥ the outer length. The remaining content is then parsed as normal markdown, and backslashes, `$`, and asterisks get eaten.

**Rule:** every embedded example inside this document uses **4-space indentation only** — never a fence inside a fence.

**Safe:**

    ===== FILE: src/main.py =====
    <<<FIND>>>
    def f():
        pass
    <<<REPLACE>>>
    def f():
        return 1
    <<<END>>>

**Unsafe (do NOT do this in the document):** wrapping the above example in ` ``` ` inside another ` ``` `.

**If you must show a markdown fence as content:** show it as a line of backticks with 4-space indent — not as a real fence.

### 12-6. Golden rule for the AI: `input.txt` output format

**Every time the AI wants to give a patch, it must give the entire `input.txt` in a single code block** — not piecemeal, not with prose in between.

**Hard rules:**

1. **One single block from `===== FILE` to the last `<<<END>>>`.**
2. **If the content contains triple backticks, use four backticks for the outer fence.** Example: ` ```` ` instead of ` ``` `.
3. **No prose between blocks.** If an explanation is needed, before or after the block — not inside.
4. **If the anchor or CONTENT is very large, split into two separate blocks** — but each block must be complete and self-contained.
5. **No parser markers (`===== FILE`, `<<<FIND>>>`, `<<<END>>>`, etc.) should appear in prose outside a block.**

---

## Section 13 — Session Tracker

> **Note:** This section is for your real project. **Send the document as a template, this section is filled in** with the project's real state.
> If using the document as a template (new project), **clear this section** and fill it in again.

### 13-1. Session Tracker

| Field | Value |
|-------|-------|
| **Last safe tag** | `v1.1.1-en` |
| **Last commit** | after v1.1.1 patch |
| **Last work** | v1.1.1: absolute I/O discipline (0-C-10) + newcomer onboarding (0-C-11) + language policy (0-C-12) + CTX-DELTA ROADMAP (10-6) |
| **Next step** | Sync `PROJECT_CONTEXT.fa.md` with all v1.1 / v1.1.1 additions |
| **Current phase** | v1.1.1 — I/O discipline locked down |
| **Completion** | 100% EN, 100% FA (Persian needs v1.1+ sync) |
| **Last error** | none |
| **Open issues** | Persian v1.1 sync; bootstrap helper for newcomers; `--check-md` (nested fence detector) |

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

- Python 3.8 or newer
- An empty folder (new project) or an existing project
- An AI (DeepSeek is recommended — it executes anchor/replace most precisely)

### 32-2. Steps

**Step 1 — Create the base structure**

In the project root:

    python run.py --init

That creates `_work/`, `_work/applied/`, an empty `.gitignore`, and empty `input.txt` / `output.txt`.

**Step 2 — Place this document**

`PROJECT_CONTEXT.md` (this file) goes in the project root.

**Step 3 — Ensure `run.py` exists**

The full `run.py` reference is in the project root. If you don't have it yet, copy it from the project you obtained this document from — or ask the AI to help you bootstrap it from Section 35.

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

## Section 33 — Localization Guide (how to translate)

### 33-1. Why localize

`PROJECT_CONTEXT.md` is a global document. Translating it opens it to more users.

### 33-2. Which files to translate

| File | Translate? | Note |
|------|------------|------|
| README.md | ✅ Recommended | For the GitHub landing page |
| PROJECT_CONTEXT.md | ⚠️ Optional | Only for major languages |
| run.py | ❌ No | Code — its docstring is enough |
| LICENSE | ❌ No | Legal text must be English |

### 33-3. Naming pattern

    README.md              ← primary language (English)
    README.fa.md           ← Persian
    README.ar.md           ← Arabic
    README.zh.md           ← Chinese

    PROJECT_CONTEXT.md     ← English
    PROJECT_CONTEXT.fa.md  ← Persian

### 33-4. Translating README — practical pattern

**Step 1:** Keep the primary language.

**Step 2:** At the top of the README, list the languages:

    <p align="center">
      <b>English</b> ·
      <a href="README.fa.md">فارسی</a> ·
      <a href="README.ar.md">العربية</a>
    </p>

**Step 3:** Create the new file: `README.fa.md`.

**Step 4:** Translate the English content, but:
- Leave file names unchanged (`run.py`, `PROJECT_CONTEXT.md`).
- Leave commands unchanged (`git clone ...`, `python run.py --status`).
- Leave tag names unchanged (`v1.1.0`).

### 33-5. Translating PROJECT_CONTEXT.md

**Important:** this document contains parser markers:

- `===== FILE =====`
- `<<<FIND>>>`, `<<<REPLACE>>>`, `<<<END>>>`
- `# MSG-SEED`

**Never translate these.** Only translate the surrounding prose.

### 33-6. Translation notes

1. **Technical terms:** use the standard equivalent if one exists. Otherwise keep the English original.
2. **Section numbers:** do not renumber. `Section 5` stays `Section 5` in every language.
3. **Internal links:** if an anchor exists (`#section-5`), translate it or keep it — depending on GitHub support.
4. **RTL/LTR:** in right-to-left text, wrap code and commands in `LTR` or `bdi`.

### 33-7. Code pattern in translation

In the Persian document:

    To install:
    git clone https://github.com/...

Keep commands in their own code blocks.

### 33-8. If the translation is incomplete

That's fine. A half-translated file still has value. Add at the top:

    > ⚠️ This translation is incomplete. Contributions welcome.

### 33-9. Contributing a translation

- Create a new file.
- Link it from the main README.
- Send a PR.

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

## Section 35 — Minimal `run.py`

The full reference `run.py` ships in the project root and supports every flag in Section 6, every patch type in Section 7, and every directive in Section 5-0-4.

**Do not copy-paste `run.py` from this document.** Copy the file directly from the project root — that avoids fence-nesting problems entirely (Section 12-7) and keeps the version consistent.

If you don't have `run.py` yet, the fastest path is:

1. Ask the AI: "Bootstrap a minimal run.py for this project. It should support `--init`, `--status`, `--file X`, and the `FILE` / `CREATE` / `DELETE` patch types."
2. Drop the AI's patch into `_work/input.txt` and run `python run.py`.
3. Then ask the AI to upgrade it step by step toward the full reference.

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