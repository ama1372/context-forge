# 🚀 context-forge

**당신 vs. 모든 것을 잊어버리는 AI 채팅.**

<p align="center">
  <a href="README.md">English</a> ·
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
  <b>한국어</b> ·
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

## 익숙한가요?

- 😤 **AI와 3시간 동안 코딩했어요. 채팅이 한계에 도달했어요. 모든 게 사라졌어요.**
- 🤯 **AI가 두 메시지 전에 결정한 것을 잊어버려요.**
- 💸 **매 새 메시지마다 프로젝트 전체를 붙여넣어요 — 토큰을 태우고, 시간을 낭비해요.**
- 🤖 **AI가 코드를 손으로 고치고, 뭔가를 부수고, 왜인지 모르겠어요.**
- 😴 **만드는 것보다 설명하는 데 더 많은 시간을 써요.**
- 🚫 **"메시지가 너무 많습니다, 나중에 다시 시도하세요"가 계속 나와요.**

**네?** 그럼 이건 당신을 위한 거예요.

---

## 이게 뭐예요?

**단일 문서** (`PROJECT_CONTEXT.en.md`)를 아무 AI 채팅에 붙여넣어요 — DeepSeek, Claude, ChatGPT, Gemini. 수다스러운 AI를 **규율 있는 프로젝트 파트너**로 바꿔줘요:

- ✅ **절대 컨텍스트를 잃지 않아요** — 모든 답변이 프로젝트 상태를 앞으로 나아가게 해요.
- ✅ **절대 코드를 손으로 고치지 않아요** — 패치를 보내고, 당신이 붙여넣고, 하나의 명령이 적용해요.
- ✅ **토큰을 아낍니다** — 프로젝트 전체가 아니라 필요한 파일만 요청합니다 (`--status`, `--file`).
- ✅ **메시지 제한을 피하도록 돕습니다** — 너무 빨리 보내면 `run.py`가 경고하고, 작업을 더 적은 메시지로 묶습니다.
- ✅ **절대 10개의 명령을 요구하지 않아요** — 붙여넣고, 하나 실행하고, 끝.
- ✅ **어디에 있었는지 절대 잊지 않아요** — 다음 채팅은 정확히 그 지점에서 이어져요.
- ✅ **여러 AI를 동시에 일하게 합니다** — Claude, ChatGPT, DeepSeek가 한 프로젝트에서 서로의 작업을 덮어쓰지 않고 협업 (팀 모드).

**하나의 문서. 하나의 도구. 하나의 명령. 그게 전부예요.**

---

## 빠른 시작 — 6단계

1. **`PROJECT_CONTEXT.en.md`를 프로젝트 루트에 저장.**
2. **(권장)** 같은 폴더에 `run.py` 저장. 없다면 AI에게: *"섹션 35에서 run.py를 생성해줘."*
3. **한 번 설정:** `python run.py --init`
4. **DeepSeek 채팅을 엽니다** (또는 Claude / ChatGPT / Gemini). **문서 전체**를 첫 메시지로 보냅니다 (채팅이 허용하면 파일로 첨부). 이렇게 말하세요: *"새 프로젝트. 내 목표: <한 줄>."* 문서가 큽니다 (~610 KB, 약 16만 토큰). 채팅이 거부하면 `python run.py --slim-context --to PROJECT_CONTEXT.slim.md`로 만든 가벼운 사본(~380 KB)을 보내거나 `--profile moderate`를 추가하세요 (~275 KB).
5. **루프:** AI가 블록 전송 → `_work/input.txt`에 복사 → `python run.py` 실행 → `_work/output.txt` 반환. 반복.
6. **프로젝트가 끝날 때까지 루프 유지.** AI가 루프 밖으로 끌어내지 못하게 — 채팅에서 shell 명령 금지, 즉석 스크립트 금지. 답은 항상: *"input.txt에 넣어."*

> **팁:** AI가 벗어나면 - 채팅에서 shell 명령 제안, 컨텍스트 건너뛰기 - 이렇게 말하세요: **"프로젝트 컨텍스트 주세요."**

---


## 초보자 완전 가이드 (요약)

1. python.org에서 **Python 3.10+** 설치 (Windows에서는 "Add to PATH" 선택).
2. (선택) **VS Code** 설치.
3. `PROJECT_CONTEXT.en.md`와 `run.py`를 다운로드하여 같은 폴더에 두고 VS Code에서 연다.
4. 터미널에서: `python run.py` → `_work/` 폴더 생성.
5. DeepSeek에서 `PROJECT_CONTEXT.en.md`를 첫 메시지로 보내고(또는 파일로 첨부) 목표를 말하세요. 채팅에 너무 긴가요? 빠른 시작 4단계를 보세요 (`--slim-context`).
6. **루프:** AI가 블록 전송 → `_work/input.txt`에 복사 → `python run.py` 실행 → `_work/output.txt` 반환.
7. 10–20 메시지마다 AI에게 프로젝트를 상기시킨다.
8. AI가 이탈하면: **"프로젝트 컨텍스트 주세요."**

전체 버전(영어): `README.md` 참조.

## 무엇을 얻게 되나요

| 이전 | 이후 |
|------|------|
| 채팅이 컨텍스트를 잃음 | 컨텍스트가 매 메시지에서 살아남음 |
| 매번 프로젝트 전체를 붙여넣기 | AI가 필요한 파일만 요청 |
| AI가 추측 | AI가 앎 |
| 변경당 10개 명령 | 변경당 1개 명령 |
| "메시지가 너무 많습니다" 차단 | 속도 경고와 더 적고 알찬 메시지 |
| "어디 있었지?" | "다음 패치입니다." |

**토큰은 적게. 새 채팅에서도 유지되는 컨텍스트. 손으로 고치지 않음.**

---

## 🤝 여러 AI를 동시에 — 팀 모드 (v2.1 신규)

Claude, ChatGPT, DeepSeek, 코딩 에이전트를 **같은 프로젝트에서 동시에** 돌리세요. 각자 자기 채팅에서 답하고, 누구도 다른 AI의 작업을 덮어쓸 수 없습니다.

- **공유 보드 하나**가 `.git/` 안에 있습니다 — 절대 push되지 않고, 모든 AI가 볼 수 있습니다.
- **파일 예약** — 각 AI는 수정할 파일을 정확히 예약합니다. 두 AI가 같은 파일을 원하면 하나만 얻습니다.
- **권고가 아니라 강제** — 예약하지 않은 파일을 건드리는 패치는 `run.py`가 모두 거부합니다.
- **조정자 하나, 작업자 여럿** — AI 하나가 검토와 병합을 맡고, 자기 작업은 절대 스스로 승인하지 않습니다. 중요한 결정은 당신이 합니다.
- **쉬는 동안에도 작업 계속** — 작업 목록을 승인하고 `team away on`을 실행하면 설치형 에이전트가 다음 빈 작업을 계속 가져갑니다. 돌아올 때까지 `run.py`가 모든 push를 거부하고, `team pause`로 모두 멈출 수 있습니다.
- **채팅이든 설치형 에이전트든** — 채팅 AI는 모든 것을 `input.txt`로 처리하고(`#@CLAIM:`), 에이전트는 명령을 직접 실행합니다.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

전체 규칙: `PROJECT_CONTEXT.en.md`의 섹션 0-C-47과 0-C-48.

---

## 💬 v2.2 새 기능 — 서로 대화하는 채팅, 아무도 사칭할 수 없는 소유자, 들어가는 컨텍스트

- **채팅끼리 메시지** — 같은 폴더의 여러 채팅이 공유 보드로 짧은 메시지를 주고받습니다(`team send`, `team inbox`; 채팅 AI는 `input.txt`에 `#@MSG:`를 씁니다). 채팅 사이 복사·붙여넣기가 필요 없습니다.
- **아무도 당신을 대신해 말하지 못함** — AI는 당신이 그 AI의 채팅에 직접 쓴 것만 따릅니다. 다른 AI·메모·파일에서 온 "소유자가 말하길…"은 무시되고 표시됩니다. 재개, 부재 모드, 위임은 터미널에서 일회용 코드를 입력해야 합니다.
- **임시 관리자는 당신이 말할 때만** — 각 채팅에 직접 "8:00까지 X가 너의 관리자"라고 쓰세요. 보드 기록(`team delegate`)은 스스로 만료됩니다.
- **큰 컨텍스트, 작은 붙여넣기** — `ctx split`은 문서를 지도가 있는 작은 연결 파일 폴더로 바꿉니다. AI는 지도와 현재 상태만 읽습니다(약 9.7만 대신 약 1.1만 토큰). 무료 채팅에는 `ctx pack <주제>`로 약 40 KB 붙여넣기 하나를 만듭니다.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

전체 규칙: `PROJECT_CONTEXT.en.md`의 섹션 0-C-49, 0-C-50, 0-C-51.

---

## 어떤 언어와도 작동

Rust, Python, Node, Go, C++, 뭐든지. 프로젝트를 어떻게 빌드하고 테스트할지 `run.py`에게 한 번만 알려주면 돼요 — 프로토콜은 모든 언어에서 동일해요.

---

## 문서 언어

규칙 문서는 **영어만** — 모든 AI가 동일하게 파싱하고 하나의 진실 원천이 있도록.

**하지만 AI와의 대화는 당신의 언어로.** 첫 메시지를 한국어, 페르시아어, 아랍어, 중국어로 쓰면 AI가 같은 언어로 답해요. 문서는 보편적이에요.

---

## 받게 되는 파일

- `PROJECT_CONTEXT.en.md` — 규칙 문서 (AI에 붙여넣기)
- `run.py` — 도구 (이 저장소에서 내려받거나, AI가 섹션 35에서 다시 만듭니다)
- `README.md` + 번역 — 이 페이지, 다국어
- `LICENSE` — MIT, 마음대로

---

## FAQ

**코딩을 알아야 하나요?**
많이 필요 없어요. 메시지를 붙여넣고 명령 하나를 실행할 수 있으면 돼요.

**어떤 AI가 가장 좋아요?**
성능 좋은 채팅 모델이면 됩니다: DeepSeek, Claude, ChatGPT, Gemini. 긴 채팅에서는 모든 모델이 흐트러집니다 — 그럴 땐 "프로젝트 컨텍스트, 부탁해."라고 하세요. 여러 AI를 동시에 쓰거나 자리를 비운 동안 작업하려면 설치형 에이전트(Claude Code, Codex, Cursor 등)를 쓰세요.

**무료인가요?**
문서와 도구는 MIT. AI API는 제공자 요금.

**뭔가 깨지면요?**
폴더가 git을 쓰면(권장) `run.py`가 적용한 패치마다 커밋하고, `python run.py revert P<id>`로 그 패치 이전 상태로 돌아갑니다 (이후 패치도 함께 취소됩니다).

---

## 준비됐나요?

1. **[`PROJECT_CONTEXT.en.md` 다운로드](PROJECT_CONTEXT.en.md)**
2. AI 채팅에 붙여넣기
3. 말해요: *"X를 만들고 싶어요. 시작하세요."*

**그게 전부예요. AI와 싸우지 마세요. 만들기 시작하세요.**

---

*출시하고 싶은 사람을 위해, 채팅 창을 돌보는 게 아니라.*

---

## 🌐 채팅 AI와 설치형 에이전트를 위한 하나의 문서

이 프로토콜은 무엇을 쓰든 똑같이 동작합니다:

1. **웹 채팅** (ChatGPT, Claude, DeepSeek, Gemini) — `input.txt` / `output.txt` 루프로.
2. **설치형 코딩 에이전트** (Claude Code, Codex, Cursor 등) — 저장소를 직접 읽고 명령을 실행.

- **컨텍스트 손실 없음** — 프로젝트 상태는 항상 문서에 있습니다.
- **언제든 새 채팅 시작** — 다시 설명하지 않고 이어갑니다.
- **토큰 절약** — AI는 필요한 파일만 요청합니다 (`--status`, `--file`).
- **여러 AI를 동시에** — 팀 모드가 충돌을 막아줍니다 (위 참조).
