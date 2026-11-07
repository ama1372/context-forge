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
- ✅ **Oszczędza tokeny** — prosi tylko o potrzebny plik (`--status`, `--file`), a nie o cały projekt.
- ✅ **Pomaga unikać limitów wiadomości** — `run.py` ostrzega, gdy wysyłasz za szybko, a praca jest łączona w mniej wiadomości.
- ✅ **Nigdy nie prosi o 10 komend** — wklejasz, uruchamiasz jedną, gotowe.
- ✅ **Nigdy nie zapomina, gdzie byliście** — następny czat kontynuuje dokładnie tam, gdzie skończyłeś.
- ✅ **Pozwala kilku AI pracować jednocześnie** — Claude, ChatGPT i DeepSeek nad jednym projektem, bez nadpisywania sobie pracy (tryb zespołowy).

**Jeden dokument. Jedno narzędzie. Jedna komenda. To wszystko.**

---

## Szybki start — 6 kroków

1. **Umieść `PROJECT_CONTEXT.en.md` w katalogu głównym projektu.**
2. **(Zalecane)** Umieść `run.py` w tym samym folderze. Nie masz? Powiedz AI: *"Wygeneruj run.py z Sekcji 35."*
3. **Skonfiguruj raz:** `python run.py --init`
4. **Otwórz czat DeepSeek** (lub Claude / ChatGPT / Gemini). Wyślij **cały dokument** jako pierwszą wiadomość (dołącz jako plik, jeśli czat na to pozwala). Powiedz: *"Nowy projekt. Mój cel: <jedna linia>."* Dokument jest duży (~610 KB, około 160 tys. tokenów); jeśli czat go odrzuci, wyślij lżejszą kopię utworzoną przez `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~380 KB) albo dodaj `--profile moderate` (~275 KB).
5. **Pętla:** AI wysyła blok → skopiuj do `_work/input.txt` → uruchom `python run.py` → odeślij `_work/output.txt`. Powtarzaj.
6. **Trzymaj pętlę aż projekt będzie gotowy.** Nie pozwól AI wyciągnąć się z niej — żadnych poleceń shell w czacie, żadnych szybkich skryptów. Odpowiedź zawsze brzmi: *"Włóż do input.txt."*

> **Wskazówka:** jeśli AI zbacza - sugeruje polecenia shell w czacie, pomija kontekst - powiedz: **"Kontekst projektu, proszę."**

---


## Kompletny przewodnik dla początkujących (skrót)

1. Zainstaluj **Python 3.10+** z python.org (Windows: zaznacz "Add to PATH").
2. (Opcjonalnie) Zainstaluj **VS Code**.
3. Pobierz `PROJECT_CONTEXT.en.md` i `run.py`, umieść w jednym folderze, otwórz w VS Code.
4. Terminal: `python run.py` → tworzy się folder `_work/`.
5. W DeepSeek wyślij `PROJECT_CONTEXT.en.md` jako pierwszą wiadomość (lub dołącz jako plik) i podaj cel. Za długi dla twojego czatu? Zobacz krok 4 szybkiego startu (`--slim-context`).
6. **Pętla:** AI wysyła blok → skopiuj do `_work/input.txt` → uruchom `python run.py` → odeślij `_work/output.txt`.
7. Co 10–20 wiadomości przypominaj AI o projekcie.
8. Jeśli AI zbacza, powiedz: **"Kontekst projektu, proszę."**

Pełna wersja (angielski): zobacz `README.md`.

## Co dostajesz

| Przed | Po |
|-------|-----|
| Czat traci kontekst | Kontekst przetrwa każdą wiadomość |
| Wklejasz cały projekt w każdej wiadomości | AI prosi tylko o potrzebne pliki |
| AI zgaduje | AI wie |
| 10 komend na zmianę | 1 komenda na zmianę |
| Blokady „za dużo wiadomości” | Ostrzeżenia o tempie i mniej, pełniejszych wiadomości |
| "Gdzie byliśmy?" | "Oto następny patch." |

**Mniej tokenów. Kontekst, który przetrwa nowy czat. Bez ręcznych zmian.**

---

## 🤝 Kilka AI naraz — tryb zespołowy (nowość w v2.1)

Uruchom Claude, ChatGPT, DeepSeek i agentów programistycznych **nad tym samym projektem w tym samym czasie**. Każdy odpowiada ci we własnym czacie — i żaden nie może nadpisać pracy innego.

- **Jedna wspólna tablica** wewnątrz `.git/` — nigdy nie jest wypychana, widzi ją każde AI.
- **Rezerwacja plików** — każde AI rezerwuje dokładnie te pliki, które będzie edytować; jeśli dwa chcą tego samego pliku, dostaje go tylko jedno.
- **Wymuszane, nie tylko zalecane** — `run.py` odrzuca każdą łatkę, która dotyka niezarezerwowanego pliku.
- **Jeden koordynator, wielu wykonawców** — jedno AI przegląda i scala, i nigdy nie zatwierdza własnej pracy; ważne decyzje należą do ciebie.
- **Praca trwa, gdy odpoczywasz** — zatwierdź listę zadań, uruchom `team away on`, a zainstalowani agenci biorą kolejne wolne zadanie; do twojego powrotu `run.py` odrzuca każdy push, a `team pause` zatrzymuje wszystkich.
- **Czat albo zainstalowany agent** — AI w czacie robi wszystko przez `input.txt` (`#@CLAIM:`); agenci sami uruchamiają polecenia.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Pełne zasady: sekcje 0-C-47 i 0-C-48 w `PROJECT_CONTEXT.en.md`.

---

## 💬 Nowość w v2.2 — czaty, które rozmawiają, właściciel, którego nie da się podrobić, kontekst, który się mieści

- **Czaty piszą do siebie** — kilka czatów w jednym folderze wysyła krótkie wiadomości przez wspólną tablicę (`team send`, `team inbox`; czatowe AI piszą `#@MSG:` w `input.txt`). Koniec z kopiowaniem między czatami.
- **Nikt nie mówi w twoim imieniu** — AI słucha tylko tego, co sam napiszesz w jego czacie. „Właściciel mówi…” od innego AI, z notatki lub pliku jest ignorowane i oznaczane. Wznowienie, tryb nieobecności i delegowanie wymagają ciebie przy terminalu z jednorazowym kodem.
- **Tymczasowy kierownik tylko na twoje słowo** — napisz sam w każdym czacie „X jest twoim kierownikiem do 8:00”; wpis na tablicy (`team delegate`) wygasa sam.
- **Duży kontekst, małe wklejenie** — `ctx split` zamienia dokument w folder małych, połączonych plików z mapą; AI czyta mapę i bieżący stan (~11 tys. tokenów zamiast ~97 tys.). Do darmowego czatu `ctx pack <temat>` tworzy jedno wklejenie ok. 40 KB.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Pełne zasady: sekcje 0-C-49, 0-C-50 i 0-C-51 w `PROJECT_CONTEXT.en.md`.

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
- `run.py` — narzędzie (pobierz z tego repozytorium albo AI odtworzy je z sekcji 35)
- `README.md` + tłumaczenia — ta strona, 24 języki
- `LICENSE` — MIT, rób co chcesz

---

## FAQ

**Czy muszę umieć programować?**
Nie bardzo. Jeśli umiesz wkleić wiadomość i uruchomić jedną komendę, dasz radę.

**Które AI jest najlepsze?**
Dowolny mocny model czatu: DeepSeek, Claude, ChatGPT, Gemini. Każdy model zbacza w długich czatach — wtedy powiedz „Kontekst projektu, proszę.” Do kilku AI naraz lub pracy pod twoją nieobecność użyj zainstalowanego agenta (Claude Code, Codex, Cursor…).

**Czy to darmowe?**
Dokument i narzędzie są na MIT. API AI zgodnie z cennikiem twojego dostawcy.

**A jeśli coś się zepsuje?**
Jeśli folder używa git (zalecane), `run.py` commituje każdą zastosowaną łatkę, a `python run.py revert P<id>` wraca do stanu sprzed tej łatki (późniejsze łatki też są cofane).

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
- **Mniej tokenów** — AI prosi tylko o potrzebne pliki (`--status`, `--file`).
- **Kilka AI naraz** — tryb zespołowy zapobiega kolizjom (patrz wyżej).
