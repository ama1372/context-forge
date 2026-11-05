# 🚀 context-forge

**Bạn vs. trò chuyện AI quên mọi thứ.**

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
  <b>Tiếng Việt</b> ·
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

## Nghe quen không?

- 😤 **Bạn đã code với AI 3 tiếng. Chat đạt giới hạn. Mọi thứ mất hết.**
- 🤯 **AI quên điều bạn quyết định hai tin nhắn trước.**
- 💸 **Mỗi tin nhắn mới bạn dán toàn bộ dự án — đốt token, lãng phí thời gian.**
- 🤖 **AI sửa code bằng tay, phá vỡ mọi thứ, và bạn không biết tại sao.**
- 😴 **Bạn tốn thời gian giải thích nhiều hơn là xây dựng.**
- 🚫 **Bạn liên tục nhận "quá nhiều tin nhắn, thử lại sau".**

**Đúng không?** Vậy đây là dành cho bạn.

---

## Đây là gì?

Một **tài liệu duy nhất** (`PROJECT_CONTEXT.en.md`) bạn dán vào bất kỳ chat AI nào — DeepSeek, Claude, ChatGPT, Gemini. Nó biến một AI nói nhiều thành **đối tác dự án có kỷ luật** mà:

- ✅ **Không bao giờ mất ngữ cảnh** — mỗi phản hồi mang trạng thái dự án tiến lên.
- ✅ **Không bao giờ sửa code của bạn bằng tay** — gửi một patch, bạn dán, một lệnh áp dụng.
- ✅ **Tiết kiệm token** — chỉ yêu cầu tệp nó cần (`--status`, `--file`), không phải cả dự án.
- ✅ **Giúp bạn tránh giới hạn tin nhắn** — `run.py` cảnh báo khi bạn gửi quá nhanh, và công việc được gom vào ít tin nhắn hơn.
- ✅ **Không bao giờ yêu cầu 10 lệnh** — bạn dán, chạy một, xong.
- ✅ **Không bao giờ quên bạn đang ở đâu** — chat tiếp theo tiếp tục đúng nơi bạn dừng.
- ✅ **Cho nhiều AI cùng làm việc một lúc** — Claude, ChatGPT và DeepSeek trên cùng một dự án mà không ghi đè công việc của nhau (Chế độ Nhóm).

**Một tài liệu. Một công cụ. Một lệnh. Chỉ vậy thôi.**

---

## Bắt đầu nhanh — 6 bước

1. **Lưu `PROJECT_CONTEXT.en.md` vào thư mục gốc dự án.**
2. **(Khuyến nghị)** Lưu `run.py` cùng thư mục. Chưa có? Nói với AI: *"Tạo run.py từ Mục 35."*
3. **Cấu hình một lần:** `python run.py --init`
4. **Mở một cuộc trò chuyện DeepSeek** (hoặc Claude / ChatGPT / Gemini). Gửi **toàn bộ tài liệu** làm tin nhắn đầu tiên (đính kèm dạng tệp nếu chat cho phép). Nói: *"Dự án mới. Mục tiêu của tôi: <một dòng>."* Tài liệu khá lớn (~530 KB, khoảng 150 nghìn token); nếu chat từ chối, hãy gửi bản nhẹ hơn tạo bằng `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` (~360 KB), hoặc thêm `--profile moderate` (~260 KB).
5. **Vòng lặp:** AI gửi một khối → sao chép vào `_work/input.txt` → chạy `python run.py` → gửi `_work/output.txt` trả lại. Lặp lại.
6. **Giữ vòng lặp cho đến khi dự án xong.** Đừng để AI kéo bạn ra — không lệnh shell trong chat, không script nhanh. Câu trả lời luôn là: *"Đặt vào input.txt."*

> **Mẹo:** nếu AI đi chệch - gợi ý lệnh shell trong chat, bỏ qua ngữ cảnh - hãy nói: **"Ngữ cảnh dự án, làm ơn."**

---


## Hướng dẫn đầy đủ cho người mới (tóm tắt)

1. Cài **Python 3.10+** từ python.org (Windows: chọn "Add to PATH").
2. (Tùy chọn) Cài **VS Code**.
3. Tải `PROJECT_CONTEXT.en.md` và `run.py`, đặt vào một thư mục, mở trong VS Code.
4. Terminal: `python run.py` → thư mục `_work/` được tạo.
5. Trong DeepSeek, gửi `PROJECT_CONTEXT.en.md` làm tin nhắn đầu tiên (hoặc đính kèm tệp) và nêu mục tiêu. Quá dài với chat của bạn? Xem bước 4 phần bắt đầu nhanh (`--slim-context`).
6. **Vòng lặp:** AI gửi khối → sao chép vào `_work/input.txt` → chạy `python run.py` → gửi `_work/output.txt` trở lại.
7. Mỗi 10–20 tin nhắn, nhắc AI về dự án.
8. Nếu AI lệch, nói: **"Ngữ cảnh dự án, làm ơn."**

Phiên bản đầy đủ (tiếng Anh): xem `README.md`.

## Những gì bạn nhận được

| Trước | Sau |
|-------|-----|
| Chat mất ngữ cảnh | Ngữ cảnh sống sót mỗi tin nhắn |
| Dán cả dự án vào mỗi tin nhắn | AI chỉ yêu cầu những tệp cần thiết |
| AI đoán | AI biết |
| 10 lệnh mỗi thay đổi | 1 lệnh mỗi thay đổi |
| Bị chặn vì "quá nhiều tin nhắn" | Cảnh báo tốc độ và ít tin nhắn hơn, đầy đủ hơn |
| "Chúng ta đang ở đâu?" | "Đây là patch tiếp theo." |

**Ít token hơn. Ngữ cảnh vẫn còn khi mở chat mới. Không sửa tay.**

---

## 🤝 Nhiều AI cùng lúc — Chế độ Nhóm (mới trong v2.1)

Cho Claude, ChatGPT, DeepSeek và các agent lập trình **làm việc trên cùng một dự án cùng một lúc**. Mỗi AI trả lời bạn trong cuộc trò chuyện riêng — và không AI nào có thể ghi đè công việc của AI khác.

- **Một bảng dùng chung** nằm trong `.git/` — không bao giờ bị push, AI nào cũng thấy.
- **Giữ chỗ tệp** — mỗi AI giữ chỗ chính xác những tệp nó sẽ sửa; nếu hai AI cùng muốn một tệp, chỉ một AI nhận được.
- **Bắt buộc, không chỉ là lời khuyên** — `run.py` từ chối mọi bản vá chạm vào tệp chưa được giữ chỗ.
- **Một điều phối viên, nhiều người làm** — một AI xem xét và hợp nhất, không bao giờ tự duyệt công việc của mình; quyết định quan trọng là của bạn.
- **Công việc tiếp tục khi bạn nghỉ** — duyệt danh sách việc, chạy `team away on`, và các agent đã cài sẽ tiếp tục nhận việc trống tiếp theo; `run.py` từ chối mọi lệnh push cho đến khi bạn quay lại, và `team pause` dừng tất cả.
- **Chat hay agent đã cài** — AI chat làm mọi thứ qua `input.txt` (`#@CLAIM:`); agent tự chạy lệnh.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Quy tắc đầy đủ: mục 0-C-47 và 0-C-48 trong `PROJECT_CONTEXT.en.md`.

---

## Hoạt động với mọi ngôn ngữ

Rust, Python, Node, Go, C++, bất cứ thứ gì. Bạn nói với `run.py` một lần cách build và test dự án của bạn — giao thức giống nhau cho mọi ngôn ngữ.

---

## Ngôn ngữ của tài liệu

Tài liệu quy tắc **chỉ tiếng Anh** — để mọi AI phân tích giống nhau, và có một nguồn sự thật.

**Nhưng cuộc trò chuyện với AI của bạn bằng ngôn ngữ của bạn.** Chỉ cần viết tin nhắn đầu tiên bằng tiếng Việt, Ba Tư, Ả Rập, Trung — AI trả lời cùng ngôn ngữ. Tài liệu là phổ quát.

---

## Bản dịch README có sẵn

- [English](README.md) · [فارسی](README.fa.md) · [中文](README.zh.md) · [Español](README.es.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Português](README.pt.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Türkçe](README.tr.md) · [Italiano](README.it.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [עברית](README.he.md) · [Українська](README.uk.md)

---

## Tập tin bạn nhận được

- `PROJECT_CONTEXT.en.md` — tài liệu quy tắc (dán vào AI của bạn)
- `run.py` — công cụ (tải từ kho này, hoặc AI dựng lại từ Mục 35)
- `README.md` + bản dịch — trang này, 24 ngôn ngữ
- `LICENSE` — MIT, làm gì cũng được

---

## FAQ

**Tôi có cần biết code không?**
Không nhiều. Nếu bạn biết dán một tin nhắn và chạy một lệnh, bạn dùng được.

**AI nào tốt nhất?**
Bất kỳ mô hình chat mạnh nào: DeepSeek, Claude, ChatGPT, Gemini. Mọi mô hình đều lạc hướng trong chat dài — khi đó hãy nói "Ngữ cảnh dự án, làm ơn." Để dùng nhiều AI cùng lúc, hoặc làm việc khi bạn vắng mặt, hãy dùng agent đã cài (Claude Code, Codex, Cursor…).

**Miễn phí không?**
Tài liệu và công cụ là MIT. API AI theo giá nhà cung cấp.

**Nếu có gì hỏng?**
Nếu thư mục dùng git (khuyến nghị), `run.py` commit mỗi bản vá đã áp dụng, và `python run.py revert P<id>` quay về trạng thái trước bản vá đó (các bản vá sau cũng bị hoàn tác).

---

## Sẵn sàng?

1. **[Tải `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Dán vào chat AI của bạn
3. Nói: *"Tôi muốn xây X. Bắt đầu."*

**Vậy thôi. Ngừng đấu với AI của bạn. Bắt đầu xây dựng.**

---

*Được làm cho người muốn giao hàng, không phải trông cửa sổ chat.*

---

## 🌐 Một tài liệu cho AI chat và agent đã cài

Giao thức này hoạt động như nhau dù bạn dùng:

1. **Chat trên web** (ChatGPT, Claude, DeepSeek, Gemini) qua vòng lặp `input.txt` / `output.txt`.
2. **Agent lập trình đã cài** (Claude Code, Codex, Cursor và các công cụ khác) tự đọc kho mã và chạy lệnh.

- **Không mất ngữ cảnh** — trạng thái dự án luôn nằm trong tài liệu.
- **Mở chat mới bất cứ lúc nào** — tiếp tục mà không cần giải thích lại.
- **Ít token hơn** — AI chỉ yêu cầu những tệp cần thiết (`--status`, `--file`).
- **Nhiều AI cùng lúc** — Chế độ Nhóm ngăn chúng xung đột (xem ở trên).
