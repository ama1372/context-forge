# 🔨 context-forge

> **Universal PROJECT_CONTEXT template + `run.py` for AI-assisted coding.**
> Kill chat limits, token waste, and lost context.

<p align="center">
  <img alt="status" src="https://img.shields.io/badge/status-active-success">
  <img alt="license" src="https://img.shields.io/badge/license-MIT-blue">
  <img alt="python" src="https://img.shields.io/badge/python-3.8%2B-blue">
  <img alt="ai" src="https://img.shields.io/badge/AI-agnostic-purple">
</p>

<p align="center">
  <b>English</b> · <a href="#-فارسی">فارسی</a>
</p>

---

## 🎯 The Problem

If you code with an AI, you've felt this pain:

- ❌ **Chat hits the limit** → open a new chat, re-explain everything from scratch.
- ❌ **Token waste** → you paste the entire project every time.
- ❌ **AI misses the anchor** → the code gets corrupted.
- ❌ **Account gets banned** → because you send repetitive messages.
- ❌ **AI forgets to update context** → the next chat is lost.

## 💡 The Solution

**context-forge** is a single document + a single tool that solves all of the above:

- ✅ **`PROJECT_CONTEXT.md`** — the project constitution, sent once per new chat.
- ✅ **`run.py`** — a flag-based tool with 15+ flags for minimal data transfer.
- ✅ **Pull, not push** — the AI asks only for what it needs.
- ✅ **`MSG-SEED`** — an anti-ban mechanism.
- ✅ **`CTX-DELTA`** — an anti-amnesia mechanism.
- ✅ **`CHANGELOG.md` + `ADR.md`** — for history and decisions.

## 🚀 Quick Start

Install as a template:

    git clone https://github.com/ama1372/context-forge.git my-project
    cd my-project
    mkdir _work
    python run.py --version
    python run.py --status

## 📂 Structure

    my-project/
    ├── PROJECT_CONTEXT.md   ← project constitution (31 sections)
    ├── CHANGELOG.md         ← tag history
    ├── ADR.md               ← architecture decisions
    ├── README.md            ← this file
    ├── LICENSE              ← MIT
    ├── .gitignore
    ├── run.py               ← the unified tool
    ├── _work/
    │   ├── input.txt        ← AI patches go here
    │   ├── output.txt       ← project dump
    │   ├── applied/         ← patch archive
    │   └── cache.json       ← hash cache
    └── (your code)

## 🛠 run.py Flags

| Flag | What it does |
|------|--------------|
| (none) | smart: input empty → dump, input full → apply |
| --version | show version |
| --status | tiny summary, ideal for chat start |
| --tree | file tree only |
| --hash | hash all files |
| --git | git log + tag + status |
| --file X | one file + hash |
| --files X Y Z | specific files |
| --errors | last run errors only |
| --auto-verify | hash mismatch → reject |
| --force | hash mismatch → apply silently |
| dump [--full] | full or incremental dump |
| apply | apply input.txt patches |
| clean | wipe _work/ |

## 🔄 Daily Workflow

    1. AI sends a patch (= = = FILE = = =)
    2. You paste it into _work/input.txt
    3. Run: python run.py
    4. Send _work/output.txt back to the AI
    5. AI sees the state and sends the next patch

## 📚 Docs

Everything lives in PROJECT_CONTEXT.md — **31 sections** covering quick start, golden rules, run.py workflow and flags, parser specification, hash verification, fuzzy matching, MSG-SEED anti-ban, CTX-DELTA anti-amnesia, escape rules, session tracker, red lines, git workflow, testing, bug-fix, feature-add, quality principles, logging, decision tree, checklists, anti-patterns, Definition of Done, troubleshooting, and full worked examples.

## 🎁 Why It's Different

- **Public domain** — no proprietary content.
- **Identity-neutral** — no reference to any author or origin project.
- **Multi-language (upcoming)** — Persian, English, Arabic.
- **Comprehensive** — 31 sections, 3000+ lines.
- **Practical** — every section ships with examples.

## 🤝 Contributing

Read PROJECT_CONTEXT.md first. Then open an issue or PR.

## 📜 License

MIT — free for everyone.

## 🙏 Credits

Born from real experience working with AIs across multiple projects.
The goal: help anyone who wants to code with an AI — without pain.

---

⭐ If this saved you time, drop a star.

---

## 📖 فارسی

> **قالب جهانی برای مدیریت پروژه‌های کد با هوش مصنوعی — بدون لیمیت، بدون تکرار، بدون فراموشی.**

### 🎯 مشکل

اگر با AI کد می‌زنی، این دردها رو حتماً دیدی:

- ❌ چت به لیمیت می‌خوره → مجبوری چت جدید باز کنی.
- ❌ توکن‌سوزی وحشتناک → هر بار کل کد رو می‌فرستی.
- ❌ AI لنگر رو اشتباه می‌زنه → کد خراب می‌شه.
- ❌ اکانتت مسدود می‌شه → چون پیام‌های تکراری می‌فرستی.
- ❌ AI یادش می‌ره کانتکست بده → چت جدید گم می‌شه.

### 💡 راه‌حل

**context-forge** یک **سند واحد** + **ابزار run.py** ارائه می‌ده:

- ✅ **PROJECT_CONTEXT.md** — قانون اساسی پروژه.
- ✅ **run.py** — ابزار فلگ‌محور.
- ✅ **Pull نه Push** — AI فقط چیزی رو می‌خواد که لازم داره.
- ✅ **MSG-SEED** — ضد مسدود شدن اکانت.
- ✅ **CTX-DELTA** — ضد فراموشی کانتکست.

### 🚀 شروع سریع

    git clone https://github.com/ama1372/context-forge.git my-project
    cd my-project
    mkdir _work
    python run.py --version

### 📜 لایسنس

MIT — استفاده‌ی آزاد برای همه.

---

**ساخته شده با ❤️ برای هر کسی که با AI کد می‌زند.**