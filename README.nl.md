# 🚀 context-forge

**Jij versus de AI-chat die alles vergeet.**

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
  <b>Nederlands</b> ·
  <a href="README.el.md">Ελληνικά</a> ·
  <a href="README.sv.md">Svenska</a> ·
  <a href="README.ro.md">Română</a>
</p>

---

## Komt dit bekend voor?

- 😤 **Je programmeert al 3 uur met AI. De chat raakt zijn limiet. Alles kwijt.**
- 🤯 **De AI vergeet wat je twee berichten geleden besloot.**
- 💸 **Elk nieuw bericht plak je het hele project — tokens verbranden, tijd verspillen.**
- 🤖 **De AI past code met de hand aan, breekt dingen, en je weet niet waarom.**
- 😴 **Je besteedt meer tijd aan uitleggen dan aan bouwen.**
- 🚫 **Je krijgt steeds "te veel berichten, probeer later".**

**Ja?** Dan is dit voor jou.

---

## Wat is het?

Een **enkel document** (`PROJECT_CONTEXT.md`) dat je in elke AI-chat plakt — DeepSeek, Claude, ChatGPT, Gemini. Het verandert een praatgrage AI in een **gedisciplineerde projectpartner** die:

- ✅ **Nooit de context verliest** — elk antwoord draagt de projectstatus verder.
- ✅ **Nooit je code met de hand aanpast** — stuurt een patch, jij plakt, één commando past toe.
- ✅ **Nooit tokens verbrandt** — vraagt alleen het bestand dat het nodig heeft, niet het hele project.
- ✅ **Nooit je account blokkeert** — ingebouwd anti-limietprotocol.
- ✅ **Nooit 10 commando's vraagt** — plakken, één uitvoeren, klaar.
- ✅ **Nooit vergeet waar jullie waren** — de volgende chat gaat verder waar je stopte.

**Één document. Één tool. Één commando. Dat is alles.**

---

## Hoe het werkt (3 stappen)

### 1. Pak het document
Download [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) uit deze repo.

### 2. Plak in je AI-chat
Open een nieuwe chat met DeepSeek (of Claude, ChatGPT, Gemini). Plak het hele document als **eerste bericht**. Schrijf één regel over wat je wilt bouwen.

### 3. Volg de AI
De AI geeft je `run.py` (een kleine Python-tool). Sla het op. Vanaf dan:

> **Je plakt → voert `python run.py` uit → stuurt de uitvoer terug.**

Dat is de hele workflow. Voor altijd.

---

## Wat je krijgt

| Voor | Na |
|------|-----|
| Chat verliest context | Context overleeft elk bericht |
| 5000 tokens per antwoord | ~300 tokens per antwoord |
| AI gokt | AI weet |
| 10 commando's per wijziging | 1 commando per wijziging |
| Account geblokkeerd | Account veilig |
| "Waar waren we?" | "Hier is de volgende patch." |

**40–80% minder tokens. Nul contextverlies. Nul handmatige aanpassingen.**

---

## Werkt met elke taal

Rust, Python, Node, Go, C++, wat dan ook. Je vertelt `run.py` één keer hoe je project te bouwen en testen — het protocol is hetzelfde voor elke taal.

---

## Taal van het document

Het regel-document is **alleen Engels** — zodat elke AI het identiek parseert en er één bron van waarheid is.

**Maar het gesprek met je AI is in jouw taal.** Schrijf gewoon je eerste bericht in het Nederlands, Perzisch, Arabisch, Chinees — de AI antwoordt in dezelfde taal. Het document is universeel.

---

## Beschikbare README-vertalingen

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Ελληνικά](README.el.md) · [Svenska](README.sv.md) · [Română](README.ro.md)

---

## Bestanden die je krijgt

- `PROJECT_CONTEXT.en.md` — het regel-document (plak in je AI)
- `run.py` — de tool (AI geeft bij eerste gebruik)
- `README.md` + vertalingen — deze pagina, 24 talen
- `LICENSE` — MIT, doe wat je wilt

---

## FAQ

**Moet ik kunnen programmeren?**
Niet veel. Als je een bericht kunt plakken en één commando kunt uitvoeren, kun je dit gebruiken.

**Welke AI is het beste?**
DeepSeek — volgt het protocol het nauwkeurigst. Claude, ChatGPT, Gemini werken ook.

**Is het gratis?**
Het document en de tool zijn MIT. De AI-API volgens je provider.

**En als er iets breekt?**
Alles is geversioneerd met git. Draai terug met één commando. Het document legt uit hoe.

---

## Klaar?

1. **[Download `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Plak in je AI-chat
3. Zeg: *"Ik wil X bouwen. Begin."*

**Dat is alles. Stop met vechten tegen je AI. Begin te bouwen.**

---

*Gemaakt voor mensen die willen verzenden, niet een chatvenster willen babysitten.*