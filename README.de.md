# 🚀 context-forge

**Du vs. der KI-Chat, der alles vergisst.**

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
  <b>Deutsch</b> ·
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

## Kommt dir das bekannt vor?

- 😤 **Du programmierst 3 Stunden mit der KI. Der Chat erreicht sein Limit. Alles ist verloren.**
- 🤯 **Die KI vergisst, was du vor zwei Nachrichten entschieden hast.**
- 💸 **Jede neue Nachricht fügst du das ganze Projekt ein — verbrennst Tokens, verlierst Zeit.**
- 🤖 **Die KI ändert den Code per Hand, macht Sachen kaputt, und du weißt nicht warum.**
- 😴 **Du verbringst mehr Zeit mit Erklären als mit Bauen.**
- 🚫 **Du bekommst ständig "zu viele Nachrichten, versuche es später".**

**Ja?** Dann ist das für dich.

---

## Was ist das?

Ein **einzelnes Dokument** (`PROJECT_CONTEXT.md`), das du in jeden KI-Chat einfügst — DeepSeek, Claude, ChatGPT, Gemini. Es verwandelt eine geschwätzige KI in einen **disziplinierten Projektpartner**, der:

- ✅ **Niemals den Kontext verliert** — jede Antwort trägt den Projektstatus weiter.
- ✅ **Niemals deinen Code per Hand ändert** — sendet einen Patch, du fügst ein, ein Befehl wendet an.
- ✅ **Niemals Tokens verbrennt** — fragt nur nach der Datei, die er braucht, nicht nach dem ganzen Projekt.
- ✅ **Niemals dein Konto sperrt** — eingebautes Anti-Limit-Protokoll.
- ✅ **Niemals 10 Befehle verlangt** — einfügen, einen Befehl ausführen, fertig.
- ✅ **Niemals vergisst, wo ihr wart** — der nächste Chat macht genau da weiter.

**Ein Dokument. Ein Werkzeug. Ein Befehl. Das war's.**

---

## So funktioniert es (3 Schritte)

### 1. Hol dir das Dokument
Lade [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) aus diesem Repo herunter.

### 2. Füge es in deinen KI-Chat ein
Öffne einen neuen Chat mit DeepSeek (oder Claude, ChatGPT, Gemini). Füge das ganze Dokument als **erste Nachricht** ein. Schreibe eine Zeile, was du bauen willst.

### 3. Folge der KI
Die KI gibt dir `run.py` (ein kleines Python-Werkzeug). Speichere es. Von da an:

> **Du fügst ein → führst `python run.py` aus → sendest die Ausgabe zurück.**

Das ist der ganze Workflow. Für immer.

---

## Was du bekommst

| Vorher | Nachher |
|--------|---------|
| Chat verliert Kontext | Kontext überlebt jede Nachricht |
| 5000 Tokens pro Antwort | ~300 Tokens pro Antwort |
| KI rät | KI weiß |
| 10 Befehle pro Änderung | 1 Befehl pro Änderung |
| Konto gesperrt | Konto sicher |
| "Wo waren wir?" | "Hier ist der nächste Patch." |

**40–80% weniger Tokens. Null Kontextverlust. Null manuelle Bearbeitung.**

---

## Funktioniert mit jeder Sprache

Rust, Python, Node, Go, C++, was auch immer. Du sagst `run.py` einmal, wie man dein Projekt baut und testet — das Protokoll ist für alle Sprachen gleich.

---

## Sprache des Dokuments

Das Regel-Dokument ist **nur auf Englisch** — damit jede KI es identisch analysiert und es eine einzige Wahrheitsquelle gibt.

**Aber das Gespräch mit deiner KI ist in deiner Sprache.** Schreibe einfach deine erste Nachricht auf Deutsch, Persisch, Arabisch, Chinesisch — die KI antwortet in derselben Sprache. Das Dokument ist universell.

---

## Dateien, die du bekommst

- `PROJECT_CONTEXT.en.md` — das Regel-Dokument (füge es in deine KI ein)
- `run.py` — das Werkzeug (die KI gibt es dir bei der ersten Nutzung)
- `README.md` + Übersetzungen — diese Seite, mehrsprachig
- `LICENSE` — MIT, mach was du willst

---

## FAQ

**Muss ich programmieren können?**
Nicht viel. Wenn du eine Nachricht einfügen und einen Befehl ausführen kannst, reicht es.

**Welche KI ist am besten?**
DeepSeek — folgt dem Protokoll am präzisesten. Claude, ChatGPT, Gemini funktionieren auch.

**Ist es kostenlos?**
Dokument und Werkzeug sind MIT. Die KI-API kostet, was dein Anbieter verlangt.

**Und wenn etwas kaputtgeht?**
Alles ist mit git versioniert. Ein Befehl macht rückgängig. Das Dokument erklärt wie.

---

## Bereit?

1. **[Lade `PROJECT_CONTEXT.en.md` herunter](PROJECT_CONTEXT.en.md)**
2. Füge es in deinen KI-Chat ein
3. Sag: *"Ich will X bauen. Fang an."*

**Das war's. Hör auf, mit deiner KI zu kämpfen. Fang an zu bauen.**

---

*Gemacht für Leute, die ausliefern wollen, nicht ein Chat-Fenster hüten.*