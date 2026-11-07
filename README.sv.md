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

Ett **enda dokument** (`PROJECT_CONTEXT.en.md`) som du klistrar in i vilken AI-chatt som helst — DeepSeek, Claude, ChatGPT, Gemini. Det förvandlar en pratsam AI till en **disciplinerad projektpartner** som:

- ✅ **Aldrig tappar kontexten** — varje svar bär projektets tillstånd framåt.
- ✅ **Aldrig redigerar din kod för hand** — skickar en patch, du klistrar in, ett kommando tillämpar.
- ✅ **Sparar tokens** — ber bara om filen den behöver (`--status`, `--file`), inte hela projektet.
- ✅ **Hjälper dig undvika meddelandegränser** — `run.py` varnar när du skickar för snabbt, och arbetet samlas i färre meddelanden.
- ✅ **Aldrig ber dig köra 10 kommandon** — klistra in, kör ett, klart.
- ✅ **Aldrig glömmer var ni var** — nästa chatt fortsätter precis där du slutade.
- ✅ **Låter flera AI arbeta samtidigt** — Claude, ChatGPT och DeepSeek i samma projekt utan att skriva över varandras arbete (Teamläge).

**Ett dokument. Ett verktyg. Ett kommando. Det är allt.**

---

## Snabbstart — 6 steg

1. **Lägg `PROJECT_CONTEXT.en.md` i projektets rot.**
2. **(Rekommenderas)** Lägg `run.py` i samma mapp. Har du inte? Säg till AI:n: *"Generera run.py från Sektion 35."*
3. **Ställ in en gång:** `python run.py --init`
4. **Öppna en DeepSeek-chatt** (eller Claude / ChatGPT / Gemini). Skicka **hela dokumentet** som första meddelande (bifoga som fil om chatten tillåter det). Säg: *"Nytt projekt. Mitt mål: <en rad>."* Dokumentet är stort (~610 KB, ungefär 160k tokens); om chatten vägrar, skicka en lättare kopia skapad med `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~380 KB), eller lägg till `--profile moderate` (~275 KB).
5. **Slinga:** AI:n skickar ett block → kopiera till `_work/input.txt` → kör `python run.py` → skicka `_work/output.txt` tillbaka. Upprepa.
6. **Håll slingan tills projektet är klart.** Låt inte AI:n dra ut dig — inga shell-kommandon i chatten, inga snabba skript. Svaret är alltid: *"Lägg det i input.txt."*

> **Tips:** om AI:n driver iväg - föreslår shell-kommandon i chatten, hoppar över kontext - säg: **"Projektkontext, tack."**

---


## Fullständig nybörjarguide (sammanfattning)

1. Installera **Python 3.10+** från python.org (Windows: markera "Add to PATH").
2. (Valfritt) Installera **VS Code**.
3. Ladda ner `PROJECT_CONTEXT.en.md` och `run.py`, lägg i samma mapp, öppna i VS Code.
4. Terminal: `python run.py` → mappen `_work/` skapas.
5. I DeepSeek, skicka `PROJECT_CONTEXT.en.md` som första meddelande (eller bifoga som fil) och ange ditt mål. För långt för din chatt? Se steg 4 i snabbstarten (`--slim-context`).
6. **Slinga:** AI skickar ett block → kopiera till `_work/input.txt` → kör `python run.py` → skicka `_work/output.txt` tillbaka.
7. Var 10–20 meddelande, påminn AI:n om ditt projekt.
8. Om AI:n driver iväg, säg: **"Projektkontext, tack."**

Full version (engelska): se `README.md`.

## Vad du får

| Före | Efter |
|------|-------|
| Chatten tappar kontext | Kontexten överlever varje meddelande |
| Du klistrar in hela projektet i varje meddelande | AI:n ber bara om de filer som behövs |
| AI:n gissar | AI:n vet |
| 10 kommandon per ändring | 1 kommando per ändring |
| Spärrar för "för många meddelanden" | Tempovarningar och färre, fylligare meddelanden |
| "Var var vi?" | "Här är nästa patch." |

**Färre tokens. Kontext som klarar en ny chatt. Inga handredigeringar.**

---

## 🤝 Flera AI samtidigt — Teamläge (nytt i v2.1)

Låt Claude, ChatGPT, DeepSeek och kodagenter arbeta **i samma projekt samtidigt**. Var och en svarar dig i sin egen chatt — och ingen kan skriva över en annans arbete.

- **En gemensam tavla** inuti `.git/` — pushas aldrig och syns för alla AI.
- **Filreservation** — varje AI reserverar exakt de filer den ska redigera; om två vill ha samma fil får bara en den.
- **Tvingande, inte bara råd** — `run.py` vägrar varje patch som rör en fil som inte är reserverad.
- **En samordnare, många arbetare** — en AI granskar och slår ihop och godkänner aldrig sitt eget arbete; viktiga beslut fattar du.
- **Arbetet fortsätter medan du vilar** — godkänn en uppgiftslista, kör `team away on`, så tar installerade agenter nästa lediga uppgift; tills du är tillbaka vägrar `run.py` varje push, och `team pause` stoppar alla.
- **Chatt eller installerad agent** — chatt-AI gör allt via `input.txt` (`#@CLAIM:`); agenter kör kommandona själva.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Alla regler: avsnitt 0-C-47 och 0-C-48 i `PROJECT_CONTEXT.en.md`.

---

## 💬 Nytt i v2.2 — chattar som pratar med varandra, en ägare som ingen kan härma, en kontext som får plats

- **Chattar skickar meddelanden till varandra** — flera chattar i samma mapp skickar korta meddelanden via den delade tavlan (`team send`, `team inbox`; chatt-AI:er skriver `#@MSG:` i `input.txt`). Slut på kopiera-klistra mellan chattar.
- **Ingen talar för dig** — en AI lyder bara det du skriver i dess egen chatt. "Ägaren säger…" från en annan AI, en anteckning eller en fil ignoreras och flaggas. Återuppta, frånvaroläge och delegering kräver att du sitter vid terminalen och skriver en engångskod.
- **En tillfällig chef bara om du säger det** — skriv själv i varje chatt "X är din chef till 8:00"; posten på tavlan (`team delegate`) går ut av sig själv.
- **Stor kontext, liten inklistring** — `ctx split` gör dokumentet till en mapp med små länkade filer och en karta; AI:n läser kartan och nuläget (~11k tokens i stället för ~97k). För en gratis chatt gör `ctx pack <ämne>` en enda inklistring på cirka 40 KB.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Alla regler: avsnitt 0-C-49, 0-C-50 och 0-C-51 i `PROJECT_CONTEXT.en.md`.

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
- `run.py` — verktyget (ladda ner det från detta kodförråd, eller låt AI:n bygga om det från avsnitt 35)
- `README.md` + översättningar — denna sida, 24 språk
- `LICENSE` — MIT, gör vad du vill

---

## FAQ

**Behöver jag kunna koda?**
Inte mycket. Om du kan klistra in ett meddelande och köra ett kommando kan du använda detta.

**Vilken AI är bäst?**
Vilken stark chattmodell som helst: DeepSeek, Claude, ChatGPT, Gemini. Alla modeller driver iväg i långa chattar — säg då "Projektkontext, tack." För flera AI samtidigt, eller arbete medan du är borta, använd en installerad agent (Claude Code, Codex, Cursor…).

**Är det gratis?**
Dokumentet och verktyget är MIT. AI-API:t enligt din leverantör.

**Vad händer om något går sönder?**
Om mappen använder git (rekommenderas) committar `run.py` varje tillämpad patch, och `python run.py revert P<id>` går tillbaka till läget före den patchen (senare patchar ångras också).

---

## Redo?

1. **[Ladda ner `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Klistra in i din AI-chatt
3. Säg: *"Jag vill bygga X. Börja."*

**Det är allt. Sluta slåss med din AI. Börja bygga.**

---

*Byggt för människor som vill leverera, inte passa ett chattfönster.*

---

## 🌐 Ett dokument för chatt-AI och installerade agenter

Protokollet fungerar likadant oavsett om du använder:

1. **Webbchattar** (ChatGPT, Claude, DeepSeek, Gemini) via slingan `input.txt` / `output.txt`.
2. **Installerade kodagenter** (Claude Code, Codex, Cursor med flera) som själva läser kodförrådet och kör kommandon.

- **Ingen kontextförlust** — projektets läge finns alltid i dokumentet.
- **Starta en ny chatt när som helst** — fortsätt utan att förklara igen.
- **Färre tokens** — AI:n ber bara om de filer den behöver (`--status`, `--file`).
- **Flera AI samtidigt** — Teamläget hindrar krockar (se ovan).
