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

Ein **einzelnes Dokument** (`PROJECT_CONTEXT.en.md`), das du in jeden KI-Chat einfügst — DeepSeek, Claude, ChatGPT, Gemini. Es verwandelt eine geschwätzige KI in einen **disziplinierten Projektpartner**, der:

- ✅ **Niemals den Kontext verliert** — jede Antwort trägt den Projektstatus weiter.
- ✅ **Niemals deinen Code per Hand ändert** — sendet einen Patch, du fügst ein, ein Befehl wendet an.
- ✅ **Spart Tokens** — fragt nur nach der Datei, die er braucht (`--status`, `--file`), nicht nach dem ganzen Projekt.
- ✅ **Hilft gegen Nachrichten-Limits** — `run.py` warnt, wenn du zu schnell sendest, und die Arbeit wird in weniger Nachrichten gebündelt.
- ✅ **Niemals 10 Befehle verlangt** — einfügen, einen Befehl ausführen, fertig.
- ✅ **Niemals vergisst, wo ihr wart** — der nächste Chat macht genau da weiter.
- ✅ **Lässt mehrere KIs gleichzeitig arbeiten** — Claude, ChatGPT und DeepSeek an einem Projekt, ohne sich gegenseitig zu überschreiben (Team-Modus).

**Ein Dokument. Ein Werkzeug. Ein Befehl. Das war's.**

---

## Schnellstart — 6 Schritte

1. **Speichere `PROJECT_CONTEXT.en.md` im Projektstammverzeichnis.**
2. **(Empfohlen)** Speichere `run.py` im selben Ordner. Kein `run.py`? Sag der KI: *"Erzeuge run.py aus Abschnitt 35."*
3. **Einmal einrichten:** `python run.py --init`
4. **Öffne einen DeepSeek-Chat** (oder Claude / ChatGPT / Gemini). Sende das **ganze Dokument** als erste Nachricht (als Datei anhängen, wenn der Chat das erlaubt). Sag: *"Neues Projekt. Mein Ziel: <eine Zeile>."* Das Dokument ist groß (~610 KB, rund 160k Tokens); lehnt dein Chat es ab, sende eine schlankere Kopie, erstellt mit `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~380 KB), oder ergänze `--profile moderate` (~275 KB).
5. **Schleife:** KI sendet einen Block → kopiere in `_work/input.txt` → führe `python run.py` aus → sende `_work/output.txt` zurück. Wiederhole.
6. **Halte die Schleife, bis dein Projekt fertig ist.** Lass die KI dich nicht rausziehen — keine Shell-Befehle im Chat, keine Schnellskripte. Die Antwort ist immer: *"Leg es in input.txt."*

> **Tipp:** Wenn die KI abdriftet - Shell-Befehle im Chat vorschlägt, den Kontext überspringt - sag: **"Projektkontext, bitte."**

---


## Komplette Anfänger-Anleitung (Kurzfassung)

1. **Python 3.10+** von python.org installieren (Windows: "Add to PATH" wählen).
2. (Optional) **VS Code** installieren.
3. `PROJECT_CONTEXT.en.md` und `run.py` herunterladen, in einen Ordner legen, in VS Code öffnen.
4. Terminal: `python run.py` → Ordner `_work/` wird erstellt.
5. In DeepSeek `PROJECT_CONTEXT.en.md` als erste Nachricht senden (oder als Datei anhängen) und das Ziel nennen. Zu lang für deinen Chat? Siehe Schnellstart Schritt 4 (`--slim-context`).
6. **Schleife:** KI sendet Block → in `_work/input.txt` einfügen → `python run.py` → `_work/output.txt` zurücksenden.
7. Alle 10–20 Nachrichten die KI an das Projekt erinnern.
8. Bei Drift: **"Projektkontext, bitte."**

Vollversion (Englisch): siehe `README.md`.

## Was du bekommst

| Vorher | Nachher |
|--------|---------|
| Chat verliert Kontext | Kontext überlebt jede Nachricht |
| Du fügst bei jeder Nachricht das ganze Projekt ein | Die KI fragt nur nach den nötigen Dateien |
| KI rät | KI weiß |
| 10 Befehle pro Änderung | 1 Befehl pro Änderung |
| Sperren wegen „zu vieler Nachrichten“ | Tempo-Warnungen und weniger, vollständigere Nachrichten |
| "Wo waren wir?" | "Hier ist der nächste Patch." |

**Weniger Tokens. Kontext, der einen neuen Chat übersteht. Keine Handarbeit am Code.**

---

## 🤝 Mehrere KIs gleichzeitig — Team-Modus (neu in v2.1)

Lass Claude, ChatGPT, DeepSeek und Coding-Agenten **gleichzeitig am selben Projekt** arbeiten. Jede antwortet dir in ihrem eigenen Chat — und keine kann die Arbeit einer anderen überschreiben.

- **Ein gemeinsames Board** in `.git/` — wird nie gepusht und ist für jede KI sichtbar.
- **Datei-Reservierung** — jede KI reserviert genau die Dateien, die sie bearbeitet; wollen zwei dieselbe Datei, bekommt sie nur eine.
- **Erzwungen, nicht nur empfohlen** — `run.py` lehnt jeden Patch ab, der eine nicht reservierte Datei berührt.
- **Ein Koordinator, viele Worker** — eine KI prüft und merged und genehmigt nie ihre eigene Arbeit; wichtige Entscheidungen triffst du.
- **Die Arbeit läuft weiter, während du pausierst** — genehmige eine Aufgabenliste, starte `team away on`, und installierte Agenten nehmen sich die nächste freie Aufgabe; bis zu deiner Rückkehr lehnt `run.py` jeden Push ab, und `team pause` stoppt alle.
- **Chat oder installierter Agent** — Chat-KIs erledigen alles über `input.txt` (`#@CLAIM:`); Agenten führen die Befehle selbst aus.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Alle Regeln: Abschnitte 0-C-47 und 0-C-48 in `PROJECT_CONTEXT.en.md`.

---

## 💬 Neu in v2.2 — Chats, die miteinander reden, ein Besitzer, den niemand fälschen kann, ein Kontext, der passt

- **Chats schreiben sich gegenseitig** — mehrere Chats im selben Ordner senden kurze Nachrichten über das gemeinsame Board (`team send`, `team inbox`; Chat-KIs schreiben `#@MSG:` in `input.txt`). Kein Kopieren mehr zwischen Chats.
- **Niemand spricht für dich** — eine KI befolgt nur, was du in ihrem eigenen Chat schreibst. „Der Besitzer sagt…“ von einer anderen KI, einer Notiz oder einer Datei wird ignoriert und markiert. Fortsetzen, Abwesenheitsmodus und Vertretung brauchen dich am Terminal mit einem Einmalcode.
- **Ein vorübergehender Leiter nur auf dein Wort** — schreib selbst in jeden Chat „X ist bis 8:00 dein Leiter“; der Board-Eintrag (`team delegate`) läuft von selbst ab.
- **Großer Kontext, kleiner Paste** — `ctx split` macht aus dem Dokument einen Ordner kleiner, verlinkter Dateien mit einer Karte; die KI liest Karte und aktuellen Stand (~11k statt ~97k Tokens). Für einen kostenlosen Chat erzeugt `ctx pack <Thema>` einen einzigen Paste von ~40 KB.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Alle Regeln: Abschnitte 0-C-49, 0-C-50 und 0-C-51 in `PROJECT_CONTEXT.en.md`.

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
- `run.py` — das Werkzeug (lade es aus diesem Repository, oder die KI baut es aus Abschnitt 35 neu)
- `README.md` + Übersetzungen — diese Seite, mehrsprachig
- `LICENSE` — MIT, mach was du willst

---

## FAQ

**Muss ich programmieren können?**
Nicht viel. Wenn du eine Nachricht einfügen und einen Befehl ausführen kannst, reicht es.

**Welche KI ist am besten?**
Jedes starke Chat-Modell: DeepSeek, Claude, ChatGPT, Gemini. Jedes Modell driftet in langen Chats ab — dann sag "Projektkontext, bitte." Für mehrere KIs gleichzeitig oder Arbeit in deiner Abwesenheit nutze einen installierten Agenten (Claude Code, Codex, Cursor…).

**Ist es kostenlos?**
Dokument und Werkzeug sind MIT. Die KI-API kostet, was dein Anbieter verlangt.

**Und wenn etwas kaputtgeht?**
Nutzt der Ordner git (empfohlen), committet `run.py` jeden angewendeten Patch, und `python run.py revert P<id>` kehrt zum Stand vor diesem Patch zurück (spätere Patches werden ebenfalls rückgängig gemacht).

---

## Bereit?

1. **[Lade `PROJECT_CONTEXT.en.md` herunter](PROJECT_CONTEXT.en.md)**
2. Füge es in deinen KI-Chat ein
3. Sag: *"Ich will X bauen. Fang an."*

**Das war's. Hör auf, mit deiner KI zu kämpfen. Fang an zu bauen.**

---

*Gemacht für Leute, die ausliefern wollen, nicht ein Chat-Fenster hüten.*

---

## 🌐 Ein Dokument für Chat-KIs und installierte Agenten

Dieses Protokoll funktioniert gleich, egal ob du nutzt:

1. **Web-Chats** (ChatGPT, Claude, DeepSeek, Gemini) über die Schleife `input.txt` / `output.txt`.
2. **Installierte Coding-Agenten** (Claude Code, Codex, Cursor und andere), die das Repository selbst lesen und Befehle ausführen.

- **Kein Kontextverlust** — der Projektstand steht immer im Dokument.
- **Jederzeit einen neuen Chat starten** — ohne alles neu zu erklären.
- **Weniger Tokens** — die KI fordert nur die nötigen Dateien an (`--status`, `--file`).
- **Mehrere KIs gleichzeitig** — der Team-Modus verhindert Kollisionen (siehe oben).
