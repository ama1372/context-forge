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

Một **tài liệu duy nhất** (`PROJECT_CONTEXT.md`) bạn dán vào bất kỳ chat AI nào — DeepSeek, Claude, ChatGPT, Gemini. Nó biến một AI nói nhiều thành **đối tác dự án có kỷ luật** mà:

- ✅ **Không bao giờ mất ngữ cảnh** — mỗi phản hồi mang trạng thái dự án tiến lên.
- ✅ **Không bao giờ sửa code của bạn bằng tay** — gửi một patch, bạn dán, một lệnh áp dụng.
- ✅ **Không bao giờ đốt token** — chỉ yêu cầu tập tin nó cần, không phải toàn bộ dự án.
- ✅ **Không bao giờ khóa tài khoản của bạn** — giao thức chống giới hạn tích hợp.
- ✅ **Không bao giờ yêu cầu 10 lệnh** — bạn dán, chạy một, xong.
- ✅ **Không bao giờ quên bạn đang ở đâu** — chat tiếp theo tiếp tục đúng nơi bạn dừng.

**Một tài liệu. Một công cụ. Một lệnh. Chỉ vậy thôi.**

---

## Cách hoạt động (3 bước)

### 1. Lấy tài liệu
Tải [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) từ repo này.

### 2. Dán vào chat AI của bạn
Mở chat mới với DeepSeek (hoặc Claude, ChatGPT, Gemini). Dán toàn bộ tài liệu làm **tin nhắn đầu tiên**. Viết một dòng về điều bạn muốn xây dựng.

### 3. Làm theo AI
AI đưa bạn `run.py` (một công cụ Python nhỏ). Lưu lại. Từ đó trở đi:

> **Bạn dán → chạy `python run.py` → gửi đầu ra trở lại.**

Đó là toàn bộ quy trình làm việc. Mãi mãi.

---

## Những gì bạn nhận được

| Trước | Sau |
|-------|-----|
| Chat mất ngữ cảnh | Ngữ cảnh sống sót mỗi tin nhắn |
| 5000 token mỗi phản hồi | ~300 token mỗi phản hồi |
| AI đoán | AI biết |
| 10 lệnh mỗi thay đổi | 1 lệnh mỗi thay đổi |
| Tài khoản bị khóa | Tài khoản an toàn |
| "Chúng ta đang ở đâu?" | "Đây là patch tiếp theo." |

**Giảm 40–80% token. Không mất ngữ cảnh. Không sửa tay.**

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
- `run.py` — công cụ (AI đưa khi dùng lần đầu)
- `README.md` + bản dịch — trang này, 19 ngôn ngữ
- `LICENSE` — MIT, làm gì cũng được

---

## FAQ

**Tôi có cần biết code không?**
Không nhiều. Nếu bạn biết dán một tin nhắn và chạy một lệnh, bạn dùng được.

**AI nào tốt nhất?**
DeepSeek — tuân thủ giao thức chính xác nhất. Claude, ChatGPT, Gemini cũng hoạt động.

**Miễn phí không?**
Tài liệu và công cụ là MIT. API AI theo giá nhà cung cấp.

**Nếu có gì hỏng?**
Mọi thứ được đánh phiên bản với git. Quay lại bằng một lệnh. Tài liệu giải thích cách.

---

## Sẵn sàng?

1. **[Tải `PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md)**
2. Dán vào chat AI của bạn
3. Nói: *"Tôi muốn xây X. Bắt đầu."*

**Vậy thôi. Ngừng đấu với AI của bạn. Bắt đầu xây dựng.**

---

*Được làm cho người muốn giao hàng, không phải trông cửa sổ chat.*