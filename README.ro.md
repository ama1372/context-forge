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

Un **singur document** (`PROJECT_CONTEXT.en.md`) pe care îl lipești în orice chat AI — DeepSeek, Claude, ChatGPT, Gemini. Transformă un AI vorbăreț într-un **partener disciplinat de proiect** care:

- ✅ **Nu pierde niciodată contextul** — fiecare răspuns duce starea proiectului mai departe.
- ✅ **Nu editează niciodată codul manual** — trimite un patch, tu lipești, o comandă aplică.
- ✅ **Nu arde niciodată tokenuri** — cere doar fișierul de care are nevoie, nu întregul proiect.
- ✅ **Nu blochează niciodată contul tău** — protocol anti-limită integrat.
- ✅ **Nu cere niciodată 10 comenzi** — lipești, rulezi una, gata.
- ✅ **Nu uită niciodată unde erați** — următorul chat continuă exact de unde ai rămas.
- ✅ **Lasă mai multe AI să lucreze simultan** — Claude, ChatGPT și DeepSeek pe același proiect, fără să-și suprascrie munca (modul Echipă).

**Un document. Un instrument. O comandă. Atât.**

---

## Pornire rapidă — 6 pași

1. **Pune `PROJECT_CONTEXT.en.md` în rădăcina proiectului.**
2. **(Recomandat)** Pune `run.py` în același folder. Nu ai? Spune-i AI-ului: *"Generează run.py din Secțiunea 35."*
3. **Configurează o dată:** `python run.py --init`
4. **Deschide un chat DeepSeek** (sau Claude / ChatGPT / Gemini). Lipește **întregul document** ca prim mesaj. Spune: *"Proiect nou. Scopul meu: <o linie>."*
5. **Buclă:** AI-ul trimite un bloc → copiază în `_work/input.txt` → rulează `python run.py` → trimite `_work/output.txt` înapoi. Repetă.
6. **Ține bucla până termini proiectul.** Nu lăsa AI-ul să te scoată — fără comenzi shell în chat, fără scripturi rapide. Răspunsul e mereu: *"Pune-l în input.txt."*

> **Sfat:** dacă AI-ul deviază - sugerează comenzi shell în chat, sare peste context - spune: **"Contextul proiectului, te rog."**

---


## Ghid complet pentru începători (rezumat)

1. Instalează **Python 3.10+** de pe python.org (Windows: bifează "Add to PATH").
2. (Opțional) Instalează **VS Code**.
3. Descarcă `PROJECT_CONTEXT.en.md` și `run.py`, pune-le într-un folder, deschide-l în VS Code.
4. Terminal: `python run.py` → se creează folderul `_work/`.
5. În DeepSeek, lipește `PROJECT_CONTEXT.en.md` ca prim mesaj, spune-ți obiectivul.
6. **Buclă:** AI trimite un bloc → copiază în `_work/input.txt` → rulează `python run.py` → trimite `_work/output.txt` înapoi.
7. La fiecare 10–20 mesaje, reamintește AI-ului proiectul tău.
8. Dacă AI-ul deviază, spune: **"Contextul proiectului, te rog."**

Versiune completă (engleză): vezi `README.md`.

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

## 🤝 Mai multe AI simultan — modul Echipă (nou în v2.1)

Pune Claude, ChatGPT, DeepSeek și agenți de programare **pe același proiect în același timp**. Fiecare îți răspunde în propriul chat — și niciunul nu poate suprascrie munca altuia.

- **Un panou comun** în `.git/` — nu este trimis niciodată pe remote și îl văd toate AI-urile.
- **Rezervarea fișierelor** — fiecare AI rezervă exact fișierele pe care le va edita; dacă două vor același fișier, doar unul îl primește.
- **Impus, nu doar recomandat** — `run.py` respinge orice patch care atinge un fișier nerezervat.
- **Un coordonator, mulți executanți** — un AI revizuiește și integrează și nu își aprobă niciodată propria muncă; deciziile importante sunt ale tale.
- **Munca continuă cât te odihnești** — aprobă o listă de sarcini, rulează `team away on`, iar agenții instalați preiau următoarea sarcină liberă; nimic nu e trimis până nu revii, iar `team pause` îi oprește pe toți.
- **Chat sau agent instalat** — AI-urile din chat fac totul prin `input.txt` (`#@CLAIM:`); agenții rulează singuri comenzile.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Regulile complete: secțiunile 0-C-47 și 0-C-48 din `PROJECT_CONTEXT.en.md`.

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

---

## 🌐 Un singur document pentru AI-uri de chat și agenți instalați

Acest protocol funcționează la fel, indiferent dacă folosești:

1. **Chaturi web** (ChatGPT, Claude, DeepSeek, Gemini) prin bucla `input.txt` / `output.txt`.
2. **Agenți de programare instalați** (Claude Code, Codex, Cursor și alții) care citesc singuri depozitul și rulează comenzi.

- **Fără pierderea contextului** — starea proiectului stă mereu în document.
- **Pornești un chat nou oricând** — continui fără să explici din nou.
- **Până la 80% mai puțini tokeni** — AI-ul cere doar fișierele de care are nevoie (`--status`, `--file`).
- **Mai multe AI simultan** — modul Echipă le împiedică să se ciocnească (vezi mai sus).
