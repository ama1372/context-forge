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

**Jeden dokument** (`PROJECT_CONTEXT.md`), który wklejasz do dowolnego czatu AI — DeepSeek, Claude, ChatGPT, Gemini. Zamienia gadatliwe AI w **zdyscyplinowanego partnera projektowego**, który:

- ✅ **Nigdy nie traci kontekstu** — każda odpowiedź niesie stan projektu dalej.
- ✅ **Nigdy nie edytuje twojego kodu ręcznie** — wysyła patch, ty wklejasz, jedna komenda stosuje.
- ✅ **Nigdy nie pali tokenów** — prosi tylko o plik, którego potrzebuje, nie cały projekt.
- ✅ **Nigdy nie blokuje twojego konta** — wbudowany protokół anty-limitowy.
- ✅ **Nigdy nie prosi o 10 komend** — wklejasz, uruchamiasz jedną, gotowe.
- ✅ **Nigdy nie zapomina, gdzie byliście** — następny czat kontynuuje dokładnie tam, gdzie skończyłeś.

**Jeden dokument. Jedno narzędzie. Jedna komenda. To wszystko.**

---

## Jak to działa (3 kroki)

### 1. Pobierz dokument
Pobierz [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) z tego repozytorium.

### 2. Wklej do czatu AI
Otwórz nowy czat z DeepSeek (lub Claude, ChatGPT, Gemini). Wklej cały dokument jako **pierwszą wiadomość**. Napisz jedną linię, co chcesz zbudować.

### 3. Podążaj za AI
AI daje ci `run.py` (małe narzędzie Pythona). Zapisz je. Od tego momentu:

> **Wklejasz → uruchamiasz `python run.py` → wysyłasz wynik z powrotem.**

To cały workflow. Na zawsze.

---

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