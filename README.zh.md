# 🚀 context-forge

**你 vs. 一个会遗忘一切的 AI 聊天。**

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README.fa.md">فارسی</a> ·
  <b>中文</b> ·
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
  <a href="README.it.md">Italiano</a> ·
  <a href="README.id.md">Bahasa Indonesia</a> ·
  <a href="README.vi.md">Tiếng Việt</a> ·
  <a href="README.th.md">ไทย</a> ·
  <a href="README.he.md">עברית</a> ·
  <a href="README.uk.md">Українська</a> ·
  <a href="README.pl.md">Polski</a> ·
  <a href="README.nl.md">Nederlands</a> ·
  <a href="README.el.md">Ελληνικά</a> ·
  <a href="README.sv.md">Svenska</a> ·
  <a href="README.ro.md">Română</a>
</p>

---

## 这些听起来熟悉吗？

- 😤 **你和 AI 一起写了 3 小时代码。聊天达到上限。一切都没了。**
- 🤯 **AI 忘记了你两条消息前的决定。**
- 💸 **每条新消息你都粘贴整个项目 —— 浪费 token,浪费时间。**
- 🤖 **AI 手动改代码,搞坏了,你还不知道为什么。**
- 😴 **你花在解释上的时间比构建的还多。**
- 🚫 **你老是收到 "消息太频繁,请稍后再试"。**

**是吗?** 那这正是给你的。

---

## 这是什么?

一份**单一文档** (`PROJECT_CONTEXT.en.md`),你把它粘贴到任何 AI 聊天中 —— DeepSeek、Claude、ChatGPT、Gemini。它把闲聊型 AI 变成一个**有纪律的项目伙伴**,它:

- ✅ **永不丢失上下文** —— 每次回复都把项目状态向前推进。
- ✅ **从不手动改你的代码** —— 发一个补丁,你粘贴,一条命令应用。
- ✅ **节省 token** — 只请求它需要的文件（`--status`、`--file`），而不是整个项目。
- ✅ **帮你避开频率限制** — 你发送太快时 `run.py` 会提醒，工作也会合并成更少的消息。
- ✅ **不让你跑 10 条命令** —— 粘贴,一条命令,搞定。
- ✅ **永不忘记你们在哪** —— 新聊天从离开处继续。
- ✅ **让多个 AI 同时工作** — Claude、ChatGPT 和 DeepSeek 在同一个项目上协作，互不覆盖（团队模式）。

**一份文档。一个工具。一条命令。就这样。**

---

## 快速开始 — 6 步

1. **将 `PROJECT_CONTEXT.en.md` 放入项目根目录。**
2. **（推荐）** 将 `run.py` 放在同一文件夹。没有？告诉 AI：*"从第 35 节引导 run.py。"*
3. **初始化一次：** `python run.py --init`
4. **打开 DeepSeek 聊天**（或 Claude / ChatGPT / Gemini）。把**整份文档**作为第一条消息发送（如果聊天支持，也可以作为文件上传）。说：*"新项目。我的目标：<一句话>。"* 文档较大（约 610 KB，大约 16 万 token）；如果聊天拒收，请发送用 `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` 生成的精简版（约 380 KB），或加上 `--profile moderate`（约 275 KB）。
5. **循环：** AI 发送一个块 → 复制到 `_work/input.txt` → 运行 `python run.py` → 将 `_work/output.txt` 发回。重复。
6. **一直循环到项目完成。** 不要让 AI 把你拉出循环 —— 不在聊天中运行 shell 命令,不用快速脚本。答案始终是:*"放进 input.txt。"*

> **提示：** 如果 AI 偏离 - 在聊天中建议 shell 命令、跳过上下文 - 只需说：**"项目上下文。"**

---


## 初学者完整指南（简版）

1. 从 python.org 安装 **Python 3.10+**（Windows 上勾选 "Add to PATH"）。
2. （可选）安装 **VS Code**。
3. 下载 `PROJECT_CONTEXT.en.md` 和 `run.py`，放进同一个文件夹，在 VS Code 中打开。
4. 在终端运行：`python run.py` → 会创建 `_work/` 文件夹。
5. 在 DeepSeek 中把 `PROJECT_CONTEXT.en.md` 作为第一条消息发送（或作为文件上传），并说明目标。对你的聊天来说太长？见快速开始第 4 步（`--slim-context`）。
6. **循环：** AI 发一个代码块 → 复制到 `_work/input.txt` → 运行 `python run.py` → 把 `_work/output.txt` 发回给 AI。
7. 每隔 10–20 条消息提醒 AI 你的项目内容。
8. 若 AI 偏离，说：**"项目上下文。"**

完整版（英文）：见 `README.md`。

## 你会得到什么

| 之前 | 之后 |
|------|------|
| 聊天丢失上下文 | 上下文在每条消息中存活 |
| 每条消息都粘贴整个项目 | AI 只请求需要的文件 |
| AI 猜测 | AI 知道 |
| 每次修改 10 条命令 | 每次修改 1 条命令 |
| "消息过于频繁"被限制 | 速度提醒，消息更少、内容更完整 |
| "我们在哪?" | "这是下一个补丁。" |

**更少的 token。新聊天也不丢上下文。不手动改代码。**

---

## 🤝 多个 AI 同时工作 — 团队模式（v2.1 新增）

让 Claude、ChatGPT、DeepSeek 和编程代理**同时在同一个项目上工作**。每个 AI 都在自己的聊天里回复你 — 而且谁都无法覆盖别人的工作。

- **一个共享看板**，存放在 `.git/` 内 — 永远不会被推送，所有 AI 都能看到。
- **文件认领** — 每个 AI 精确认领它要编辑的文件；两个 AI 想要同一个文件时，只有一个能拿到。
- **强制执行，而不只是建议** — 任何触碰未认领文件的补丁都会被 `run.py` 拒绝。
- **一个协调者，多个执行者** — 一个 AI 负责审查和合并，从不批准自己的工作；重要决定由你做。
- **你休息时工作继续** — 批准待办清单，运行 `team away on`，已安装的代理会继续领取下一个空闲任务；你回来之前 `run.py` 会拒绝任何推送，`team pause` 可让所有人停下。
- **聊天或已安装的代理** — 聊天 AI 通过 `input.txt` 完成一切（`#@CLAIM:`）；代理自己运行命令。

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

完整规则：`PROJECT_CONTEXT.en.md` 的第 0-C-47 和 0-C-48 节。

---

## 💬 v2.2 新功能 —— 会互相沟通的聊天、无法冒充的主人、装得下的上下文

- **聊天之间互发消息** —— 同一文件夹上的多个聊天通过共享看板发送短消息（`team send`、`team inbox`；聊天 AI 在 `input.txt` 中写 `#@MSG:`）。不用再在聊天之间复制粘贴。
- **没人能代你发言** —— AI 只执行你在它自己聊天里写的内容。来自其他 AI、便签或文件的“主人说……”会被忽略并标记。恢复、离开模式和委托需要你在终端输入一次性验证码。
- **临时经理，只在你亲口说时有效** —— 你亲自在每个聊天里写“X 是你的经理，到 8:00 为止”；看板记录（`team delegate`）会自动过期。
- **上下文大，粘贴小** —— `ctx split` 把文档变成带地图的小文件夹，文件之间互相链接；AI 只读地图和当前状态（约 1.1 万 token，而不是约 9.7 万）。免费聊天可用 `ctx pack <主题>` 生成一份约 40 KB 的粘贴内容。

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

完整规则：`PROJECT_CONTEXT.en.md` 的第 0-C-49、0-C-50 和 0-C-51 节。

---

## 兼容任何语言

Rust、Python、Node、Go、C++、任何语言。你告诉 `run.py` 一次如何构建和测试 —— 协议对每种语言都一样。

---

## 文档语言

规则文档**只有英文** —— 这样每个 AI 都一致解析,只有一个真相来源。

**但你与 AI 的对话用你的语言。** 用中文、波斯语、阿拉伯语、西班牙语写第一条消息 —— AI 用同一种语言回复。文档是通用的。

---

## 文件清单

- `PROJECT_CONTEXT.en.md` —— 规则文档(粘贴进 AI)
- `run.py` — 工具（从本仓库下载，或让 AI 根据第 35 节重建）
- `README.md` + 翻译 —— 本页,多语言
- `LICENSE` —— MIT,随便用

---

## 常见问题

**我需要会编程吗?**
不太需要。如果你能粘贴消息并运行一条命令,就够了。

**哪个 AI 最好?**
任何强大的聊天模型都可以：DeepSeek、Claude、ChatGPT、Gemini。所有模型在长聊天中都会跑偏 — 这时说"项目上下文，谢谢。"需要多个 AI 同时工作或在你离开时继续工作，请使用已安装的代理（Claude Code、Codex、Cursor 等）。

**免费吗?**
文档和工具是 MIT。AI 的 API 费用由你的服务商收取。

**如果出错了?**
如果文件夹使用 git（推荐），`run.py` 会为每个已应用的补丁提交一次，`python run.py revert P<id>` 可回到该补丁之前的状态（之后的补丁也会被撤销）。

---

## 准备好了?

1. **[下载 `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. 粘贴到你的 AI 聊天
3. 说:*"我想构建 X。开始。"*

**就这样。别再和你的 AI 打架。开始构建。**

---

*为想发布东西的人打造,不是为伺候聊天窗口的人。*

---

## 🌐 一份文档，同时适用于聊天 AI 和已安装的代理

无论你使用哪种方式，这套协议都一样工作：

1. **网页聊天**（ChatGPT、Claude、DeepSeek、Gemini），通过 `input.txt` / `output.txt` 循环。
2. **已安装的编程代理**（Claude Code、Codex、Cursor 等），它们自己读取仓库并运行命令。

- **不丢失上下文** — 项目状态始终保存在文档中。
- **随时开启新聊天** — 无需重新解释即可继续。
- **更少的 token** — AI 只请求它需要的文件（`--status`、`--file`）。
- **多个 AI 同时工作** — 团队模式防止它们互相冲突（见上文）。
