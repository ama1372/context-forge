# 🚀 context-forge

**Kamu vs. chat AI yang melupakan segalanya.**

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
  <b>Bahasa Indonesia</b> ·
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

## Terdengar familier?

- 😤 **Kamu coding dengan AI selama 3 jam. Chat mencapai limitnya. Semuanya hilang.**
- 🤯 **AI lupa apa yang kamu putuskan dua pesan lalu.**
- 💸 **Setiap pesan baru kamu tempel seluruh proyek — membakar token, membuang waktu.**
- 🤖 **AI mengedit kode dengan tangan, merusak sesuatu, dan kamu tidak tahu kenapa.**
- 😴 **Kamu lebih banyak menghabiskan waktu menjelaskan daripada membangun.**
- 🚫 **Kamu terus mendapat "terlalu banyak pesan, coba lagi nanti".**

**Ya?** Maka ini untukmu.

---

## Apa ini?

Sebuah **dokumen tunggal** (`PROJECT_CONTEXT.md`) yang kamu tempel ke chat AI apa pun — DeepSeek, Claude, ChatGPT, Gemini. Ini mengubah AI yang banyak bicara menjadi **mitra proyek yang disiplin** yang:

- ✅ **Tidak pernah kehilangan konteks** — setiap balasan membawa status proyek maju.
- ✅ **Tidak pernah mengedit kodemu dengan tangan** — mengirim patch, kamu tempel, satu perintah menerapkan.
- ✅ **Tidak pernah membakar token** — hanya meminta file yang dibutuhkan, bukan seluruh proyek.
- ✅ **Tidak pernah memblokir akunmu** — protokol anti-limit bawaan.
- ✅ **Tidak pernah meminta 10 perintah** — tempel, jalankan satu, selesai.
- ✅ **Tidak pernah lupa di mana kamu berada** — chat berikutnya melanjutkan tepat dari tempatmu berhenti.

**Satu dokumen. Satu alat. Satu perintah. Itu saja.**

---

## Cara kerjanya (3 langkah)

### 1. Dapatkan dokumen
Unduh [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) dari repo ini.

### 2. Tempel ke chat AI-mu
Buka chat baru dengan DeepSeek (atau Claude, ChatGPT, Gemini). Tempel seluruh dokumen sebagai **pesan pertama**. Tulis satu baris tentang apa yang ingin kamu bangun.

### 3. Ikuti AI
AI memberimu `run.py` (alat Python kecil). Simpan. Sejak saat itu:

> **Kamu tempel → jalankan `python run.py` → kirim outputnya kembali.**

Itu seluruh alur kerjanya. Selamanya.

---

## Apa yang kamu dapatkan

| Sebelum | Sesudah |
|---------|---------|
| Chat kehilangan konteks | Konteks bertahan di setiap pesan |
| 5000 token per balasan | ~300 token per balasan |
| AI menebak | AI tahu |
| 10 perintah per perubahan | 1 perintah per perubahan |
| Akun diblokir | Akun aman |
| "Di mana kita tadi?" | "Ini patch berikutnya." |

**40–80% lebih sedikit token. Nol kehilangan konteks. Nol edit manual.**

---

## Bekerja dengan bahasa apa pun

Rust, Python, Node, Go, C++, apa saja. Kamu beri tahu `run.py` sekali cara membangun dan menguji proyekmu — protokolnya sama untuk setiap bahasa.

---

## Bahasa dokumen

Dokumen aturan **hanya bahasa Inggris** — agar setiap AI memparsenya identik, dan ada satu sumber kebenaran.

**Tapi percakapan dengan AI-mu dalam bahasamu.** Cukup tulis pesan pertama dalam Bahasa Indonesia, Persia, Arab, Cina — AI membalas dalam bahasa yang sama. Dokumennya universal.

---

## Terjemahan README yang tersedia

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md)

---

## File yang kamu dapatkan

- `PROJECT_CONTEXT.en.md` — dokumen aturan (tempel ke AI-mu)
- `run.py` — alat (diberikan AI saat pertama kali digunakan)
- `README.md` + terjemahan — halaman ini, 19 bahasa
- `LICENSE` — MIT, lakukan sesukamu

---

## FAQ

**Apakah saya perlu tahu coding?**
Tidak banyak. Jika kamu bisa menempel pesan dan menjalankan satu perintah, kamu bisa pakai ini.

**AI mana yang terbaik?**
DeepSeek — paling tepat mengikuti protokol. Claude, ChatGPT, Gemini juga bekerja.

**Apakah gratis?**
Dokumen dan alatnya MIT. API AI sesuai tarif penyediamu.

**Bagaimana jika ada yang rusak?**
Semuanya diberi versi dengan git. Kembali dengan satu perintah. Dokumen menjelaskan caranya.

---

## Siap?

1. **[Unduh `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Tempel ke chat AI-mu
3. Katakan: *"Saya ingin membangun X. Mulai."*

**Itu saja. Berhenti bertarung dengan AI-mu. Mulai membangun.**

---

*Dibuat untuk orang yang ingin mengirim, bukan mengasuh jendela chat.*