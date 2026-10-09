# 🚀 context-forge

**You vs. the AI chat that forgets everything.**

<p align="center">
  <b>English</b> ·
  <a href="README.fa.md">فارسی</a> ·
  <a href="README.zh.md">中文</a> ·
  <a href="README.es.md">Español</a> ·
  <a href="README.ar.md">العربية</a> ·
  <a href="README.hi.md">हिन्दी</a> ·
  <a href="README.fr.md">Français</a> ·
  <a href="README.ru.md">Русский</a> ·
  <a href="README.pt.md">Português</a> ·
  <a href="README.de.md">Deutsch</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="README.ko.md">한국어</a> ·
  <a href="README.tr.md">Türkçe</a> ·
  <a href="README.it.md">Italiano</a>
</p>

---

## Does this sound familiar?

- 😤 **You've been coding with an AI for 3 hours. The chat hits its limit. Everything is lost.**
- 🤯 **The AI forgets what you decided two messages ago.**
- 💸 **Every new message you paste the whole project — burning tokens, wasting time.**
- 🤖 **The AI edits code by hand, breaks things, and you don't know why.**
- 😴 **You spend more time explaining what you want than building it.**
- 🚫 **You keep hitting "message too frequent, try again later".**

**Yes?** Then this is for you.

---

## What is it?

A **single document** (`PROJECT_CONTEXT.en.md`) you paste into any AI chat — DeepSeek, Claude, ChatGPT, Gemini. It turns a chatty AI into a **disciplined project partner** that:

- ✅ **Never loses context** — every reply carries the project's state forward.
- ✅ **Never edits your code by hand** — it sends a patch, you paste, one command applies it.
- ✅ **Never burns tokens** — it asks only for the file it needs, not the whole project.
- ✅ **Never blocks your account** — built-in anti-rate-limit protocol.
- ✅ **Never asks you to run 10 commands** — you paste, run one command, done.
- ✅ **Never forgets where you were** — next chat picks up from exactly where you left.

**One document. One tool. One command. That's it.**

---

## How it works (3 steps)

### 1. Get the document
Download [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) from this repo.

### 2. Paste it into your AI chat
Open a new chat with DeepSeek (or Claude, ChatGPT, Gemini). Paste the whole document as your **first message**. Write one line about what you want to build.

### 3. Follow the AI
The AI gives you `run.py` (a small Python tool). Save it. From then on:

> **You paste → run `python run.py` → send the output back.**

That's the entire workflow. Forever.

---

## What you get

| Before | After |
|--------|-------|
| Chat loses context | Context survives every message |
| 5000 tokens per reply | ~300 tokens per reply |
| AI guesses | AI knows |
| 10 commands per change | 1 command per change |
| Account blocked | Account safe |
| "Where were we?" | "Here's the next patch." |

**40–80% less tokens. Zero context loss. Zero manual edits.**

---

## Works with any language

Rust, Python, Node, Go, C++, anything. You tell `run.py` once how to build and test your project — the protocol stays the same for every language.

---

## Languages of the document

The rule document is **English only** — so every AI parses it identically, and there's one source of truth.

**But the conversation with your AI is in your language.** Just write your first message in Persian, Arabic, Chinese, Spanish — the AI replies in the same language. The document is universal.

---

## Available README translations

- [English](README.md)
- [فارسی (Persian)](README.fa.md)
- [中文 (Chinese)](README.zh.md)
- [Español (Spanish)](README.es.md)
- [العربية (Arabic)](README.ar.md)
- [हिन्दी (Hindi)](README.hi.md)
- [Français (French)](README.fr.md)
- [Русский (Russian)](README.ru.md)
- [Português (Portuguese)](README.pt.md)
- [Deutsch (German)](README.de.md)
- [日本語 (Japanese)](README.ja.md)
- [한국어 (Korean)](README.ko.md)
- [Türkçe (Turkish)](README.tr.md)
- [Italiano (Italian)](README.it.md)

---

## Files you get

- `PROJECT_CONTEXT.en.md` — the rule document (paste this into your AI)
- `run.py` — the tool (given to you by the AI on first use)
- `README.md` + translations — this page, 14 languages
- `LICENSE` — MIT, do whatever you want

---

## FAQ

**Do I need to know how to code?**
Not much. If you can paste a message and run one command, you can use this.

**Which AI works best?**
DeepSeek — it follows the protocol most precisely. Claude, ChatGPT, Gemini also work.

**Is it free?**
The document and tool are MIT. The AI's API is whatever your provider charges.

**What if something breaks?**
Everything is versioned with git. Roll back with one command. The document explains how.

---

## Ready?

1. **[Download `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Paste into your AI chat
3. Say: *"I want to build X. Start."*

**That's it. Stop fighting your AI. Start building.**

---

*Built for people who want to ship, not babysit a chat window.*