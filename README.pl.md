# 🚀 context-forge

**Ty kontra czat AI, który zapomina wszystko.**

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
  <b>Polski</b> ·
  <a href="README.nl.md">Nederlands</a> ·
  <a href="README.el.md">Ελληνικά</a> ·
  <a href="README.sv.md">Svenska</a> ·
  <a href="README.ro.md">Română</a>
</p>

---

## Brzmi znajomo?

- 😤 **Kodujesz z AI od 3 godzin. Czat osiąga limit. Wszystko przepada.**
- 🤯 **AI zapomina, co ustaliłeś dwie wiadomości temu.**
- 💸 **Każda nowa wiadomość — wklejasz cały projekt, paląc tokeny i tracąc czas.**
- 🤖 **AI edytuje kod ręcznie, psuje rzeczy, a ty nie wiesz dlaczego.**
- 😴 **Spędzasz więcej czasu na tłumaczeniu niż na budowaniu.**
- 🚫 **Ciągle dostajesz "za dużo wiadomości, spróbuj później".**

**Tak?** To jest dla ciebie.

---

## Co to jest?

**Jeden dokument** (`PROJECT_CONTEXT.en.md`), który wklejasz do dowolnego czatu AI — DeepSeek, Claude, ChatGPT, Gemini. Zamienia gadatliwe AI w **zdyscyplinowanego partnera projektowego**, który:

- ✅ **Nigdy nie traci kontekstu** — każda odpowiedź niesie stan projektu dalej.
- ✅ **Nigdy nie edytuje twojego kodu ręcznie** — wysyła patch, ty wklejasz, jedna komenda stosuje.
- ✅ **Nigdy nie pali tokenów** — prosi tylko o plik, którego potrzebuje, nie cały projekt.
- ✅ **Nigdy nie blokuje twojego konta** — wbudowany protokół anty-limitowy.
- ✅ **Nigdy nie prosi o 10 komend** — wklejasz, uruchamiasz jedną, gotowe.
- ✅ **Nigdy nie zapomina, gdzie byliście** — następny czat kontynuuje dokładnie tam, gdzie skończyłeś.
- ✅ **Pozwala kilku AI pracować jednocześnie** — Claude, ChatGPT i DeepSeek nad jednym projektem, bez nadpisywania sobie pracy (tryb zespołowy).

**Jeden dokument. Jedno narzędzie. Jedna komenda. To wszystko.**

---

## Szybki start — 6 kroków

1. **Umieść `PROJECT_CONTEXT.en.md` w katalogu głównym projektu.**
2. **(Zalecane)** Umieść `run.py` w tym samym folderze. Nie masz? Powiedz AI: *"Wygeneruj run.py z Sekcji 35."*
3. **Skonfiguruj raz:** `python run.py --init`
4. **Otwórz czat DeepSeek** (lub Claude / ChatGPT / Gemini). Wklej **cały dokument** jako pierwszą wiadomość. Powiedz: *"Nowy projekt. Mój cel: <jedna linia>."*
5. **Pętla:** AI wysyła blok → skopiuj do `_work/input.txt` → uruchom `python run.py` → odeślij `_work/output.txt`. Powtarzaj.
6. **Trzymaj pętlę aż projekt będzie gotowy.** Nie pozwól AI wyciągnąć się z niej — żadnych poleceń shell w czacie, żadnych szybkich skryptów. Odpowiedź zawsze brzmi: *"Włóż do input.txt."*

> **Wskazówka:** jeśli AI zbacza - sugeruje polecenia shell w czacie, pomija kontekst - powiedz: **"Kontekst projektu, proszę."**

---


## Kompletny przewodnik dla początkujących (skrót)

1. Zainstaluj **Python 3.10+** z python.org (Windows: zaznacz "Add to PATH").
2. (Opcjonalnie) Zainstaluj **VS Code**.
3. Pobierz `PROJECT_CONTEXT.en.md` i `run.py`, umieść w jednym folderze, otwórz w VS Code.
4. Terminal: `python run.py` → tworzy się folder `_work/`.
5. W DeepSeek wklej `PROJECT_CONTEXT.en.md` jako pierwszą wiadomość, podaj cel.
6. **Pętla:** AI wysyła blok → skopiuj do `_work/input.txt` → uruchom `python run.py` → odeślij `_work/output.txt`.
7. Co 10–20 wiadomości przypominaj AI o projekcie.
8. Jeśli AI zbacza, powiedz: **"Kontekst projektu, proszę."**

Pełna wersja (angielski): zobacz `README.md`.

## Co dostajesz

| Przed | Po |
|-------|-----|
| Czat traci kontekst | Kontekst przetrwa każdą wiadomość |
| 5000 tokenów na odpowiedź | ~300 tokenów na odpowiedź |
| AI zgaduje | AI wie |
| 10 komend na zmianę | 1 komenda na zmianę |
| Konto zablokowane | Konto bezpieczne |
| "Gdzie byliśmy?" | "Oto następny patch." |

**40–80% mniej tokenów. Zero utraty kontekstu. Zero ręcznych edycji.**

---

## 🤝 Kilka AI naraz — tryb zespołowy (nowość w v2.1)

Uruchom Claude, ChatGPT, DeepSeek i agentów programistycznych **nad tym samym projektem w tym samym czasie**. Każdy odpowiada ci we własnym czacie — i żaden nie może nadpisać pracy innego.

- **Jedna wspólna tablica** wewnątrz `.git/` — nigdy nie jest wypychana, widzi ją każde AI.
- **Rezerwacja plików** — każde AI rezerwuje dokładnie te pliki, które będzie edytować; jeśli dwa chcą tego samego pliku, dostaje go tylko jedno.
- **Wymuszane, nie tylko zalecane** — `run.py` odrzuca każdą łatkę, która dotyka niezarezerwowanego pliku.
- **Jeden koordynator, wielu wykonawców** — jedno AI przegląda i scala, i nigdy nie zatwierdza własnej pracy; ważne decyzje należą do ciebie.
- **Praca trwa, gdy odpoczywasz** — zatwierdź listę zadań, uruchom `team away on`, a zainstalowani agenci biorą kolejne wolne zadanie; nic nie zostanie wypchnięte przed twoim powrotem, a `team pause` zatrzymuje wszystkich.
- **Czat albo zainstalowany agent** — AI w czacie robi wszystko przez `input.txt` (`#@CLAIM:`); agenci sami uruchamiają polecenia.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Pełne zasady: sekcje 0-C-47 i 0-C-48 w `PROJECT_CONTEXT.en.md`.

---

## Działa z każdym językiem

Rust, Python, Node, Go, C++, cokolwiek. Mówisz `run.py` raz, jak budować i testować twój projekt — protokół jest taki sam dla każdego języka.

---

## Język dokumentu

Dokument zasad jest **tylko po angielsku** — żeby każde AI parsowało go identycznie i było jedno źródło prawdy.

**Ale rozmowa z twoim AI jest w twoim języku.** Po prostu napisz pierwszą wiadomość po polsku, persku, arabsku, chińsku — AI odpowie w tym samym języku. Dokument jest uniwersalny.

---

## Dostępne tłumaczenia README

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Nederlands](README.nl.md) · [Ελληνικά](README.el.md) · [Svenska](README.sv.md) · [Română](README.ro.md)

---

## Pliki, które dostajesz

- `PROJECT_CONTEXT.en.md` — dokument zasad (wklej do AI)
- `run.py` — narzędzie (AI daje przy pierwszym użyciu)
- `README.md` + tłumaczenia — ta strona, 24 języki
- `LICENSE` — MIT, rób co chcesz

---

## FAQ

**Czy muszę umieć programować?**
Nie bardzo. Jeśli umiesz wkleić wiadomość i uruchomić jedną komendę, dasz radę.

**Które AI jest najlepsze?**
DeepSeek — najdokładniej podąża za protokołem. Claude, ChatGPT, Gemini też działają.

**Czy to darmowe?**
Dokument i narzędzie są na MIT. API AI zgodnie z cennikiem twojego dostawcy.

**A jeśli coś się zepsuje?**
Wszystko jest wersjonowane przez git. Cofnij jedną komendą. Dokument wyjaśnia jak.

---

## Gotowy?

1. **[Pobierz `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Wklej do czatu AI
3. Powiedz: *"Chcę zbudować X. Zaczynaj."*

**To wszystko. Przestań walczyć z AI. Zacznij budować.**

---

*Zbudowane dla ludzi, którzy chcą wysyłać, a nie pilnować okna czatu.*

---

## 🌐 Jeden dokument dla AI w czacie i zainstalowanych agentów

Ten protokół działa tak samo, niezależnie od tego, czy używasz:

1. **Czatów w przeglądarce** (ChatGPT, Claude, DeepSeek, Gemini) z pętlą `input.txt` / `output.txt`.
2. **Zainstalowanych agentów programistycznych** (Claude Code, Codex, Cursor i inni), którzy sami czytają repozytorium i uruchamiają polecenia.

- **Bez utraty kontekstu** — stan projektu zawsze jest w dokumencie.
- **Nowy czat w dowolnej chwili** — kontynuuj bez ponownego tłumaczenia.
- **Do 80% mniej tokenów** — AI prosi tylko o potrzebne pliki (`--status`, `--file`).
- **Kilka AI naraz** — tryb zespołowy zapobiega kolizjom (patrz wyżej).
