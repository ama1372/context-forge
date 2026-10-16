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

Un **documento unico** (`PROJECT_CONTEXT.md`) che incolli in qualsiasi chat IA — DeepSeek, Claude, ChatGPT, Gemini. Trasforma un'IA chiacchierona in un **partner di progetto disciplinato** che:

- ✅ **Non perde mai il contesto** — ogni risposta porta avanti lo stato del progetto.
- ✅ **Non modifica mai il tuo codice a mano** — invia una patch, tu incolli, un comando applica.
- ✅ **Non brucia mai token** — chiede solo il file di cui ha bisogno, non tutto il progetto.
- ✅ **Non blocca mai il tuo account** — protocollo anti-limite integrato.
- ✅ **Non chiede mai 10 comandi** — incolli, ne esegui uno, fatto.
- ✅ **Non dimentica mai dov'eri** — la prossima chat riprende esattamente da dove hai lasciato.

**Un documento. Uno strumento. Un comando. Tutto qui.**

---

## Avvio rapido — 6 passi

1. **Salva `PROJECT_CONTEXT.en.md` nella radice del progetto.**
2. **(Consigliato)** Salva `run.py` nella stessa cartella. Non ce l'hai? Di' all'IA: *"Genera run.py dalla Sezione 35."*
3. **Configura una volta:** `python run.py --init`
4. **Apri una chat con DeepSeek** (o Claude / ChatGPT / Gemini). Incolla l'**intero documento** come primo messaggio. Di': *"Nuovo progetto. Il mio obiettivo: <una riga>."*
5. **Loop:** l'IA invia un blocco → copia in `_work/input.txt` → esegui `python run.py` → rimanda `_work/output.txt`. Ripeti.
6. **Mantieni il loop finché il progetto non è finito.** Non lasciare che l'IA ti tiri fuori — niente comandi shell in chat, niente script rapidi. La risposta è sempre: *"Mettilo in input.txt."*

> **Consiglio:** se l'IA devia - suggerisce comandi shell in chat, salta il contesto - di': **"Contesto del progetto, per favore."**

---


## Guida completa per principianti (riassunto)

1. Installa **Python 3.10+** da python.org (su Windows, spunta "Add to PATH").
2. (Opzionale) Installa **VS Code**.
3. Scarica `PROJECT_CONTEXT.en.md` e `run.py`, mettili in una cartella, aprila in VS Code.
4. Terminale: `python run.py` → viene creata la cartella `_work/`.
5. In DeepSeek, incolla `PROJECT_CONTEXT.en.md` come primo messaggio, di' il tuo obiettivo.
6. **Loop:** l'IA invia un blocco → copia in `_work/input.txt` → esegui `python run.py` → rimanda `_work/output.txt`.
7. Ogni 10–20 messaggi ricorda all'IA il tuo progetto.
8. Se l'IA devia, di': **"Contesto del progetto, per favore."**

Versione completa (inglese): vedi `README.md`.

## Cosa ottieni

| Prima | Dopo |
|-------|------|
| La chat perde il contesto | Il contesto sopravvive a ogni messaggio |
| 5000 token per risposta | ~300 token per risposta |
| L'IA indovina | L'IA sa |
| 10 comandi per modifica | 1 comando per modifica |
| Account bloccato | Account sicuro |
| "Dov'eravamo?" | "Ecco la prossima patch." |

**40–80% meno token. Zero perdita di contesto. Zero modifiche manuali.**

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
- `run.py` — lo strumento (l'IA te lo dà al primo utilizzo)
- `README.md` + traduzioni — questa pagina, multilingue
- `LICENSE` — MIT, fai quello che vuoi

---

## FAQ

**Devo saper programmare?**
Non molto. Se sai incollare un messaggio ed eseguire un comando, puoi usarlo.

**Quale IA funziona meglio?**
DeepSeek — segue il protocollo con più precisione. Funzionano anche Claude, ChatGPT e Gemini.

**È gratis?**
Documento e strumento sono MIT. L'API IA è quello che ti addebita il tuo provider.

**E se qualcosa si rompe?**
Tutto è versionato con git. Torna indietro con un comando. Il documento spiega come.

---

## Pronto?

1. **[Scarica `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Incollalo nella tua chat IA
3. Di': *"Voglio costruire X. Inizia."*

**Tutto qui. Smetti di combattere con la tua IA. Inizia a costruire.**

---

*Fatto per chi vuole spedire, non badare a una finestra di chat.*