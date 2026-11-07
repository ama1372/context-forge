# 🚀 context-forge

**Tu vs. la chat IA che dimentica tutto.**

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
  <b>Italiano</b> ·
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

## Ti suona familiare?

- 😤 **Stai programmando con l'IA da 3 ore. La chat raggiunge il limite. Tutto è perduto.**
- 🤯 **L'IA dimentica cosa hai deciso due messaggi fa.**
- 💸 **Ogni nuovo messaggio incolli l'intero progetto — bruci token, perdi tempo.**
- 🤖 **L'IA modifica il codice a mano, rompe cose, e non sai perché.**
- 😴 **Passi più tempo a spiegare che a costruire.**
- 🚫 **Ricevi sempre "troppi messaggi, riprova più tardi".**

**Sì?** Allora è per te.

---

## Cos'è?

Un **documento unico** (`PROJECT_CONTEXT.en.md`) che incolli in qualsiasi chat IA — DeepSeek, Claude, ChatGPT, Gemini. Trasforma un'IA chiacchierona in un **partner di progetto disciplinato** che:

- ✅ **Non perde mai il contesto** — ogni risposta porta avanti lo stato del progetto.
- ✅ **Non modifica mai il tuo codice a mano** — invia una patch, tu incolli, un comando applica.
- ✅ **Risparmia token** — chiede solo il file che gli serve (`--status`, `--file`), non l'intero progetto.
- ✅ **Ti aiuta a evitare i limiti di messaggi** — `run.py` avvisa quando invii troppo in fretta, e il lavoro viene raggruppato in meno messaggi.
- ✅ **Non chiede mai 10 comandi** — incolli, ne esegui uno, fatto.
- ✅ **Non dimentica mai dov'eri** — la prossima chat riprende esattamente da dove hai lasciato.
- ✅ **Fa lavorare più IA contemporaneamente** — Claude, ChatGPT e DeepSeek sullo stesso progetto senza sovrascriversi il lavoro (modalità Team).

**Un documento. Uno strumento. Un comando. Tutto qui.**

---

## Avvio rapido — 6 passi

1. **Salva `PROJECT_CONTEXT.en.md` nella radice del progetto.**
2. **(Consigliato)** Salva `run.py` nella stessa cartella. Non ce l'hai? Di' all'IA: *"Genera run.py dalla Sezione 35."*
3. **Configura una volta:** `python run.py --init`
4. **Apri una chat DeepSeek** (o Claude / ChatGPT / Gemini). Invia l'**intero documento** come primo messaggio (allegalo come file se la chat lo consente). Di': *"Nuovo progetto. Il mio obiettivo: <una riga>."* Il documento è grande (~610 KB, circa 160k token); se la chat lo rifiuta, invia una copia più leggera creata con `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~380 KB), oppure aggiungi `--profile moderate` (~275 KB).
5. **Loop:** l'IA invia un blocco → copia in `_work/input.txt` → esegui `python run.py` → rimanda `_work/output.txt`. Ripeti.
6. **Mantieni il loop finché il progetto non è finito.** Non lasciare che l'IA ti tiri fuori — niente comandi shell in chat, niente script rapidi. La risposta è sempre: *"Mettilo in input.txt."*

> **Consiglio:** se l'IA devia - suggerisce comandi shell in chat, salta il contesto - di': **"Contesto del progetto, per favore."**

---


## Guida completa per principianti (riassunto)

1. Installa **Python 3.10+** da python.org (su Windows, spunta "Add to PATH").
2. (Opzionale) Installa **VS Code**.
3. Scarica `PROJECT_CONTEXT.en.md` e `run.py`, mettili in una cartella, aprila in VS Code.
4. Terminale: `python run.py` → viene creata la cartella `_work/`.
5. In DeepSeek, invia `PROJECT_CONTEXT.en.md` come primo messaggio (o allegalo come file) e indica il tuo obiettivo. Troppo lungo per la tua chat? Vedi il passo 4 dell'avvio rapido (`--slim-context`).
6. **Loop:** l'IA invia un blocco → copia in `_work/input.txt` → esegui `python run.py` → rimanda `_work/output.txt`.
7. Ogni 10–20 messaggi ricorda all'IA il tuo progetto.
8. Se l'IA devia, di': **"Contesto del progetto, per favore."**

Versione completa (inglese): vedi `README.md`.

## Cosa ottieni

| Prima | Dopo |
|-------|------|
| La chat perde il contesto | Il contesto sopravvive a ogni messaggio |
| Incolli tutto il progetto a ogni messaggio | L'IA chiede solo i file necessari |
| L'IA indovina | L'IA sa |
| 10 comandi per modifica | 1 comando per modifica |
| Blocchi per "troppi messaggi" | Avvisi di velocità e messaggi meno numerosi, più completi |
| "Dov'eravamo?" | "Ecco la prossima patch." |

**Meno token. Un contesto che sopravvive a una nuova chat. Nessuna modifica a mano.**

---

## 🤝 Più IA contemporaneamente — modalità Team (novità della v2.1)

Fai lavorare Claude, ChatGPT, DeepSeek e agenti di programmazione **sullo stesso progetto nello stesso momento**. Ognuno ti risponde nella propria chat — e nessuno può sovrascrivere il lavoro di un altro.

- **Una bacheca condivisa** dentro `.git/` — non viene mai inviata al remoto ed è visibile a tutte le IA.
- **Prenotazione dei file** — ogni IA prenota esattamente i file che modificherà; se due vogliono lo stesso file, solo una lo ottiene.
- **Imposto, non solo consigliato** — `run.py` rifiuta qualsiasi patch che tocchi un file non prenotato.
- **Un coordinatore, molti esecutori** — una IA rivede e unisce, e non approva mai il proprio lavoro; le decisioni importanti restano tue.
- **Il lavoro continua mentre riposi** — approva un elenco di attività, esegui `team away on` e gli agenti installati prendono la successiva attività libera; `run.py` rifiuta ogni push finché non torni, e `team pause` ferma tutti.
- **Chat o agente installato** — le IA in chat fanno tutto tramite `input.txt` (`#@CLAIM:`); gli agenti eseguono i comandi da soli.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Regole complete: sezioni 0-C-47 e 0-C-48 di `PROJECT_CONTEXT.en.md`.

---

## 💬 Novità della v2.2 — chat che si parlano, un proprietario che nessuno può impersonare, un contesto che ci sta

- **Le chat si scrivono** — più chat sulla stessa cartella si mandano brevi messaggi tramite la bacheca condivisa (`team send`, `team inbox`; le IA di chat scrivono `#@MSG:` in `input.txt`). Basta copia-incolla tra chat.
- **Nessuno parla al posto tuo** — un'IA obbedisce solo a ciò che scrivi nella sua chat. «Il proprietario dice…» da un'altra IA, da una nota o da un file viene ignorato e segnalato. Riprendere, la modalità assente e la delega richiedono te al terminale mentre digiti un codice monouso.
- **Un responsabile temporaneo solo se lo dici tu** — scrivi tu in ogni chat «X è il tuo responsabile fino alle 8:00»; la registrazione in bacheca (`team delegate`) scade da sola.
- **Contesto grande, incolla piccolo** — `ctx split` trasforma il documento in una cartella di piccoli file collegati con una mappa; l'IA legge la mappa e lo stato attuale (~11k token invece di ~97k). Per una chat gratuita, `ctx pack <argomento>` crea un unico incolla di circa 40 KB.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Regole complete: sezioni 0-C-49, 0-C-50 e 0-C-51 di `PROJECT_CONTEXT.en.md`.

---

## Funziona con qualsiasi linguaggio

Rust, Python, Node, Go, C++, qualunque cosa. Dici a `run.py` una volta come costruire e testare il tuo progetto — il protocollo è lo stesso per ogni linguaggio.

---

## Lingua del documento

Il documento delle regole è **solo in inglese** — così ogni IA lo analizza in modo identico e c'è un'unica fonte di verità.

**Ma la conversazione con la tua IA è nella tua lingua.** Scrivi semplicemente il tuo primo messaggio in italiano, persiano, arabo, cinese — l'IA risponde nella stessa lingua. Il documento è universale.

---

## File che ottieni

- `PROJECT_CONTEXT.en.md` — il documento delle regole (incollalo nella tua IA)
- `run.py` — lo strumento (scaricalo da questo repository, oppure l'IA lo ricostruisce dalla sezione 35)
- `README.md` + traduzioni — questa pagina, multilingue
- `LICENSE` — MIT, fai quello che vuoi

---

## FAQ

**Devo saper programmare?**
Non molto. Se sai incollare un messaggio ed eseguire un comando, puoi usarlo.

**Quale IA funziona meglio?**
Qualsiasi modello di chat valido: DeepSeek, Claude, ChatGPT, Gemini. Tutti i modelli deviano nelle chat lunghe — allora di' "Contesto del progetto, per favore." Per più IA contemporaneamente, o lavoro mentre sei via, usa un agente installato (Claude Code, Codex, Cursor…).

**È gratis?**
Documento e strumento sono MIT. L'API IA è quello che ti addebita il tuo provider.

**E se qualcosa si rompe?**
Se la cartella usa git (consigliato), `run.py` fa un commit per ogni patch applicata, e `python run.py revert P<id>` torna allo stato precedente a quella patch (anche le patch successive vengono annullate).

---

## Pronto?

1. **[Scarica `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Incollalo nella tua chat IA
3. Di': *"Voglio costruire X. Inizia."*

**Tutto qui. Smetti di combattere con la tua IA. Inizia a costruire.**

---

*Fatto per chi vuole spedire, non badare a una finestra di chat.*

---

## 🌐 Un unico documento per IA in chat e agenti installati

Questo protocollo funziona allo stesso modo sia che tu usi:

1. **Chat web** (ChatGPT, Claude, DeepSeek, Gemini) con il ciclo `input.txt` / `output.txt`.
2. **Agenti di programmazione installati** (Claude Code, Codex, Cursor e altri) che leggono il repository ed eseguono i comandi da soli.

- **Nessuna perdita di contesto** — lo stato del progetto vive sempre nel documento.
- **Apri una nuova chat quando vuoi** — continua senza rispiegare.
- **Meno token** — l'IA chiede solo i file che le servono (`--status`, `--file`).
- **Più IA contemporaneamente** — la modalità Team evita le collisioni (vedi sopra).
