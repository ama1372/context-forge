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

Sebuah **dokumen tunggal** (`PROJECT_CONTEXT.en.md`) yang kamu tempel ke chat AI apa pun — DeepSeek, Claude, ChatGPT, Gemini. Ini mengubah AI yang banyak bicara menjadi **mitra proyek yang disiplin** yang:

- ✅ **Tidak pernah kehilangan konteks** — setiap balasan membawa status proyek maju.
- ✅ **Tidak pernah mengedit kodemu dengan tangan** — mengirim patch, kamu tempel, satu perintah menerapkan.
- ✅ **Menghemat token** — hanya meminta file yang dibutuhkan (`--status`, `--file`), bukan seluruh proyek.
- ✅ **Membantu menghindari batas pesan** — `run.py` memperingatkan saat kamu mengirim terlalu cepat, dan pekerjaan digabung ke lebih sedikit pesan.
- ✅ **Tidak pernah meminta 10 perintah** — tempel, jalankan satu, selesai.
- ✅ **Tidak pernah lupa di mana kamu berada** — chat berikutnya melanjutkan tepat dari tempatmu berhenti.
- ✅ **Membuat beberapa AI bekerja bersamaan** — Claude, ChatGPT, dan DeepSeek di satu proyek tanpa saling menimpa pekerjaan (Mode Tim).

**Satu dokumen. Satu alat. Satu perintah. Itu saja.**

---

## Mulai cepat — 6 langkah

1. **Simpan `PROJECT_CONTEXT.en.md` di akar proyek.**
2. **(Disarankan)** Simpan `run.py` di folder yang sama. Tidak ada? Katakan ke AI: *"Buat run.py dari Bagian 35."*
3. **Setup sekali:** `python run.py --init`
4. **Buka chat DeepSeek** (atau Claude / ChatGPT / Gemini). Kirim **seluruh dokumen** sebagai pesan pertama (lampirkan sebagai file jika chat mengizinkan). Katakan: *"Proyek baru. Tujuanku: <satu baris>."* Dokumennya besar (~530 KB, sekitar 150 ribu token); jika chat menolaknya, kirim salinan yang lebih ringan buatan `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~360 KB), atau tambahkan `--profile moderate` (~260 KB).
5. **Loop:** AI mengirim blok → salin ke `_work/input.txt` → jalankan `python run.py` → kirim `_work/output.txt` kembali. Ulangi.
6. **Pertahankan loop sampai proyek selesai.** Jangan biarkan AI menarikmu keluar — tidak ada perintah shell di chat, tidak ada skrip cepat. Jawabannya selalu: *"Taruh di input.txt."*

> **Tips:** jika AI menyimpang - menyarankan perintah shell di chat, melewati konteks - katakan: **"Konteks proyek, tolong."**

---


## Panduan lengkap pemula (ringkas)

1. Instal **Python 3.10+** dari python.org (di Windows, centang "Add to PATH").
2. (Opsional) Instal **VS Code**.
3. Unduh `PROJECT_CONTEXT.en.md` dan `run.py`, taruh di satu folder, buka di VS Code.
4. Terminal: `python run.py` → folder `_work/` dibuat.
5. Di DeepSeek, kirim `PROJECT_CONTEXT.en.md` sebagai pesan pertama (atau lampirkan sebagai file) dan sebutkan tujuanmu. Terlalu panjang untuk chat-mu? Lihat langkah 4 mulai cepat (`--slim-context`).
6. **Loop:** AI mengirim blok → salin ke `_work/input.txt` → jalankan `python run.py` → kirim `_work/output.txt` kembali.
7. Setiap 10–20 pesan, ingatkan AI tentang proyekmu.
8. Jika AI menyimpang, katakan: **"Konteks proyek, tolong."**

Versi lengkap (Inggris): lihat `README.md`.

## Apa yang kamu dapatkan

| Sebelum | Sesudah |
|---------|---------|
| Chat kehilangan konteks | Konteks bertahan di setiap pesan |
| Menempel seluruh proyek di setiap pesan | AI hanya meminta file yang dibutuhkan |
| AI menebak | AI tahu |
| 10 perintah per perubahan | 1 perintah per perubahan |
| Diblokir karena "terlalu banyak pesan" | Peringatan kecepatan dan pesan lebih sedikit, lebih lengkap |
| "Di mana kita tadi?" | "Ini patch berikutnya." |

**Lebih sedikit token. Konteks yang bertahan di chat baru. Tanpa edit manual.**

---

## 🤝 Beberapa AI sekaligus — Mode Tim (baru di v2.1)

Jalankan Claude, ChatGPT, DeepSeek, dan agen coding **di proyek yang sama pada saat yang sama**. Masing-masing menjawab di chat-nya sendiri — dan tidak ada yang bisa menimpa pekerjaan yang lain.

- **Satu papan bersama** di dalam `.git/` — tidak pernah di-push dan terlihat oleh semua AI.
- **Klaim file** — setiap AI mengklaim tepat file yang akan diubahnya; jika dua AI menginginkan file yang sama, hanya satu yang mendapatkannya.
- **Dipaksakan, bukan sekadar saran** — `run.py` menolak setiap patch yang menyentuh file yang belum diklaim.
- **Satu koordinator, banyak pekerja** — satu AI meninjau dan menggabungkan, dan tidak pernah menyetujui pekerjaannya sendiri; keputusan penting tetap milikmu.
- **Pekerjaan berlanjut saat kamu istirahat** — setujui daftar tugas, jalankan `team away on`, dan agen terpasang terus mengambil tugas kosong berikutnya; `run.py` menolak setiap push sampai kamu kembali, dan `team pause` menghentikan semuanya.
- **Chat atau agen terpasang** — AI chat melakukan semuanya lewat `input.txt` (`#@CLAIM:`); agen menjalankan perintah sendiri.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Aturan lengkap: bagian 0-C-47 dan 0-C-48 di `PROJECT_CONTEXT.en.md`.

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
- `run.py` — alatnya (unduh dari repositori ini, atau AI membangunnya ulang dari Bagian 35)
- `README.md` + terjemahan — halaman ini, 24 bahasa
- `LICENSE` — MIT, lakukan sesukamu

---

## FAQ

**Apakah saya perlu tahu coding?**
Tidak banyak. Jika kamu bisa menempel pesan dan menjalankan satu perintah, kamu bisa pakai ini.

**AI mana yang terbaik?**
Model chat kuat mana pun: DeepSeek, Claude, ChatGPT, Gemini. Semua model melenceng di chat panjang — saat itu katakan "Konteks proyek, tolong." Untuk beberapa AI sekaligus, atau kerja saat kamu pergi, pakai agen terpasang (Claude Code, Codex, Cursor…).

**Apakah gratis?**
Dokumen dan alatnya MIT. API AI sesuai tarif penyediamu.

**Bagaimana jika ada yang rusak?**
Jika folder memakai git (disarankan), `run.py` membuat commit untuk setiap patch yang diterapkan, dan `python run.py revert P<id>` kembali ke keadaan sebelum patch itu (patch sesudahnya juga dibatalkan).

---

## Siap?

1. **[Unduh `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Tempel ke chat AI-mu
3. Katakan: *"Saya ingin membangun X. Mulai."*

**Itu saja. Berhenti bertarung dengan AI-mu. Mulai membangun.**

---

*Dibuat untuk orang yang ingin mengirim, bukan mengasuh jendela chat.*

---

## 🌐 Satu dokumen untuk AI chat dan agen terpasang

Protokol ini bekerja sama baiknya, baik kamu memakai:

1. **Chat web** (ChatGPT, Claude, DeepSeek, Gemini) lewat siklus `input.txt` / `output.txt`.
2. **Agen coding terpasang** (Claude Code, Codex, Cursor, dan lainnya) yang membaca repositori dan menjalankan perintah sendiri.

- **Konteks tidak pernah hilang** — status proyek selalu ada di dokumen.
- **Mulai chat baru kapan saja** — lanjutkan tanpa menjelaskan ulang.
- **Lebih sedikit token** — AI hanya meminta file yang dibutuhkan (`--status`, `--file`).
- **Beberapa AI sekaligus** — Mode Tim mencegah bentrokan (lihat di atas).
