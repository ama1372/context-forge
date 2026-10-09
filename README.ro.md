# 🚀 context-forge

**Tu împotriva chat-ului AI care uită totul.**

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
  <a href="README.sv.md">Svenska</a> ·
  <b>Română</b>
</p>

---

## Sună familiar?

- 😤 **Codezi cu AI de 3 ore. Chat-ul atinge limita. Totul se pierde.**
- 🤯 **AI-ul uită ce ai decis acum două mesaje.**
- 💸 **Fiecare mesaj nou lipești întregul proiect — arzând tokenuri, pierzând timp.**
- 🤖 **AI-ul editează codul manual, strică lucruri, și nu știi de ce.**
- 😴 **Petreci mai mult timp explicând decât construind.**
- 🚫 **Primești mereu "prea multe mesaje, încearcă mai târziu".**

**Da?** Atunci asta e pentru tine.

---

## Ce este?

Un **singur document** (`PROJECT_CONTEXT.md`) pe care îl lipești în orice chat AI — DeepSeek, Claude, ChatGPT, Gemini. Transformă un AI vorbăreț într-un **partener disciplinat de proiect** care:

- ✅ **Nu pierde niciodată contextul** — fiecare răspuns duce starea proiectului mai departe.
- ✅ **Nu editează niciodată codul manual** — trimite un patch, tu lipești, o comandă aplică.
- ✅ **Nu arde niciodată tokenuri** — cere doar fișierul de care are nevoie, nu întregul proiect.
- ✅ **Nu blochează niciodată contul tău** — protocol anti-limită integrat.
- ✅ **Nu cere niciodată 10 comenzi** — lipești, rulezi una, gata.
- ✅ **Nu uită niciodată unde erați** — următorul chat continuă exact de unde ai rămas.

**Un document. Un instrument. O comandă. Atât.**

---

## Cum funcționează (3 pași)

### 1. Obține documentul
Descarcă [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) din acest repo.

### 2. Lipește-l în chat-ul tău AI
Deschide un chat nou cu DeepSeek (sau Claude, ChatGPT, Gemini). Lipește întregul document ca **prim mesaj**. Scrie o linie despre ce vrei să construiești.

### 3. Urmărește AI-ul
AI-ul îți dă `run.py` (un mic instrument Python). Salvează-l. De atunci înainte:

> **Lipești → rulezi `python run.py` → trimiți rezultatul înapoi.**

Acesta este întregul flux de lucru. Pentru totdeauna.

---

## Ce primești

| Înainte | După |
|---------|------|
| Chat-ul pierde contextul | Contextul supraviețuiește fiecărui mesaj |
| 5000 tokenuri per răspuns | ~300 tokenuri per răspuns |
| AI-ul ghicește | AI-ul știe |
| 10 comenzi per schimbare | 1 comandă per schimbare |
| Cont blocat | Cont sigur |
| "Unde eram?" | "Iată următorul patch." |

**40–80% mai puține tokenuri. Zero pierdere de context. Zero editări manuale.**

---

## Funcționează cu orice limbă

Rust, Python, Node, Go, C++, orice. Îi spui `run.py` o dată cum să construiască și să testeze proiectul tău — protocolul este același pentru fiecare limbă.

---

## Limba documentului

Documentul de reguli este **doar în engleză** — astfel încât fiecare AI să îl parseze identic și să fie o singură sursă de adevăr.

**Dar conversația cu AI-ul tău este în limba ta.** Scrie primul mesaj în română, persană, arabă, chineză — AI-ul răspunde în aceeași limbă. Documentul este universal.

---

## Traduceri README disponibile

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Ελληνικά](README.el.md) · [Svenska](README.sv.md) · [Română](README.ro.md)

---

## Fișierele pe care le primești

- `PROJECT_CONTEXT.en.md` — documentul de reguli (lipește-l în AI)
- `run.py` — instrumentul (AI-ul îl dă la prima utilizare)
- `README.md` + traduceri — această pagină, 24 limbi
- `LICENSE` — MIT, fă ce vrei

---

## Întrebări frecvente

**Trebuie să știu să programez?**
Nu mult. Dacă poți lipi un mesaj și rula o comandă, poți folosi asta.

**Care AI este cel mai bun?**
DeepSeek — urmează protocolul cel mai precis. Claude, ChatGPT, Gemini funcționează și ele.

**Este gratuit?**
Documentul și instrumentul sunt MIT. API-ul AI conform furnizorului tău.

**Și dacă ceva se strică?**
Totul este versionat cu git. Revino cu o comandă. Documentul explică cum.

---

## Gata?

1. **[Descarcă `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Lipește-l în chat-ul tău AI
3. Spune: *"Vreau să construiesc X. Începe."*

**Atât. Nu te mai lupta cu AI-ul tău. Începe să construiești.**

---

*Construit pentru oameni care vor să livreze, nu să îngrijească o fereastră de chat.*