# 🚀 context-forge

**Du mot AI-chatten som glömmer allt.**

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
  <b>Svenska</b> ·
  <a href="README.ro.md">Română</a>
</p>

---

## Låter detta bekant?

- 😤 **Du har kodat med AI i 3 timmar. Chatten når sin gräns. Allt är förlorat.**
- 🤯 **AI:n glömmer vad du bestämde två meddelanden sedan.**
- 💸 **Varje nytt meddelande klistrar du in hela projektet — bränner tokens, slösar tid.**
- 🤖 **AI:n redigerar kod för hand, förstör saker, och du vet inte varför.**
- 😴 **Du lägger mer tid på att förklara än på att bygga.**
- 🚫 **Du får ständigt "för många meddelanden, försök senare".**

**Ja?** Då är detta för dig.

---

## Vad är det?

Ett **enda dokument** (`PROJECT_CONTEXT.md`) som du klistrar in i vilken AI-chatt som helst — DeepSeek, Claude, ChatGPT, Gemini. Det förvandlar en pratsam AI till en **disciplinerad projektpartner** som:

- ✅ **Aldrig tappar kontexten** — varje svar bär projektets tillstånd framåt.
- ✅ **Aldrig redigerar din kod för hand** — skickar en patch, du klistrar in, ett kommando tillämpar.
- ✅ **Aldrig bränner tokens** — ber bara om filen den behöver, inte hela projektet.
- ✅ **Aldrig blockerar ditt konto** — inbyggt anti-gränsprotokoll.
- ✅ **Aldrig ber dig köra 10 kommandon** — klistra in, kör ett, klart.
- ✅ **Aldrig glömmer var ni var** — nästa chatt fortsätter precis där du slutade.

**Ett dokument. Ett verktyg. Ett kommando. Det är allt.**

---

## Hur det fungerar (3 steg)

### 1. Skaffa dokumentet
Ladda ner [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) från detta repo.

### 2. Klistra in i din AI-chatt
Öppna en ny chatt med DeepSeek (eller Claude, ChatGPT, Gemini). Klistra in hela dokumentet som **första meddelande**. Skriv en rad om vad du vill bygga.

### 3. Följ AI:n
AI:n ger dig `run.py` (ett litet Python-verktyg). Spara det. Från och med då:

> **Du klistrar in → kör `python run.py` → skickar tillbaka utdata.**

Det är hela arbetsflödet. För alltid.

---

## Vad du får

| Före | Efter |
|------|-------|
| Chatten tappar kontext | Kontexten överlever varje meddelande |
| 5000 tokens per svar | ~300 tokens per svar |
| AI:n gissar | AI:n vet |
| 10 kommandon per ändring | 1 kommando per ändring |
| Konto blockerat | Konto säkert |
| "Var var vi?" | "Här är nästa patch." |

**40–80% färre tokens. Noll kontextförlust. Noll manuella redigeringar.**

---

## Fungerar med alla språk

Rust, Python, Node, Go, C++, vad som helst. Du berättar för `run.py` en gång hur man bygger och testar ditt projekt — protokollet är detsamma för alla språk.

---

## Dokumentets språk

Regeldokumentet är **endast på engelska** — så att varje AI tolkar det identiskt och det finns en enda sanningskälla.

**Men konversationen med din AI är på ditt språk.** Skriv bara ditt första meddelande på svenska, persiska, arabiska, kinesiska — AI:n svarar på samma språk. Dokumentet är universellt.

---

## Tillgängliga README-översättningar

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Ελληνικά](README.el.md) · [Svenska](README.sv.md) · [Română](README.ro.md)

---

## Filer du får

- `PROJECT_CONTEXT.en.md` — regeldokumentet (klistra in i din AI)
- `run.py` — verktyget (AI:n ger vid första användning)
- `README.md` + översättningar — denna sida, 24 språk
- `LICENSE` — MIT, gör vad du vill

---

## FAQ

**Behöver jag kunna koda?**
Inte mycket. Om du kan klistra in ett meddelande och köra ett kommando kan du använda detta.

**Vilken AI är bäst?**
DeepSeek — följer protokollet mest exakt. Claude, ChatGPT, Gemini fungerar också.

**Är det gratis?**
Dokumentet och verktyget är MIT. AI-API:t enligt din leverantör.

**Vad händer om något går sönder?**
Allt är versionshanterat med git. Rulla tillbaka med ett kommando. Dokumentet förklarar hur.

---

## Redo?

1. **[Ladda ner `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Klistra in i din AI-chatt
3. Säg: *"Jag vill bygga X. Börja."*

**Det är allt. Sluta slåss med din AI. Börja bygga.**

---

*Byggt för människor som vill leverera, inte passa ett chattfönster.*