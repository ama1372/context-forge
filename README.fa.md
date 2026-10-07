# 🔨 context-forge

> **قالب جهانی PROJECT_CONTEXT + `run.py` برای کدنویسی با هوش مصنوعی.**
> پایان لیمیت چت، هدررفت توکن، و گم‌شدن کانتکست.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

<p align="center">
  <a href="README.md">English</a> ·
  <b>فارسی</b> ·
  <a href="README.ar.md">العربية</a>
</p>

---

## 🎯 مشکل

اگر با هوش مصنوعی کد می‌زنی، این دردها را حتماً دیده‌ای:

- ❌ **چت به لیمیت می‌خورد** → مجبوری چت جدید باز کنی و همه‌چیز را از صفر توضیح بدهی.
- ❌ **هدررفت توکن** → هر بار کل پروژه را می‌فرستی.
- ❌ **هوش مصنوعی لنگر را اشتباه می‌زند** → کد خراب می‌شود.
- ❌ **اکانتت مسدود می‌شود** → چون پیام‌های تکراری می‌فرستی.
- ❌ **هوش مصنوعی یادش می‌رود کانتکست بدهد** → چت جدید گم می‌شود.

## 💡 راه‌حل

**context-forge** یک سند واحد + یک ابزار است:

- ✅ **PROJECT_CONTEXT.md** — قانون اساسی پروژه (۳۵+ بخش).
- ✅ **run.py** — ابزار فلگ‌محور با ۱۵+ فلگ.
- ✅ **Pull نه Push** — هوش مصنوعی فقط چیزی را می‌خواهد که لازم دارد.
- ✅ **MSG-SEED** — ضد مسدود شدن اکانت.
- ✅ **CTX-DELTA** — ضد فراموشی کانتکست.

## 🚀 شروع سریع

نصب به‌عنوان قالب:

    git clone https://github.com/ama1372/context-forge.git my-project
    cd my-project
    mkdir _work
    python run.py --version
    python run.py --status

## 📂 ساختار

    my-project/
    ├── PROJECT_CONTEXT.md   ← قانون اساسی (۳۵+ بخش)
    ├── run.py               ← ابزار یکپارچه
    ├── README.md            ← انگلیسی
    ├── README.fa.md         ← همین فایل
    ├── LICENSE              ← MIT
    ├── .gitignore
    └── _work/               ← ارتباط با AI
        ├── input.txt        ← پچ‌های AI
        ├── output.txt       ← dump پروژه
        ├── applied/         ← بایگانی
        └── CONTEXT_DEV.md   ← سند مخفی توسعه

## 🛠 فلگ‌های `run.py`

| فلگ | کار |
|-----|-----|
| (بدون) | smart: input empty → dump، input full → apply |
| `--version` | نمایش نسخه |
| `--status` | خلاصه‌ی خیلی کوچک (~۳۰۰ بایت) |
| `--tree` | فقط درخت فایل‌ها |
| `--hash` | hash همه‌ی فایل‌ها |
| `--git` | git log + tag + status |
| `--file X` | محتوای یک فایل + hash |
| `--files X Y Z` | چند فایل مشخص |
| `--errors` | فقط خطاهای آخرین اجرا |
| `--auto-verify` | hash mismatch → رد |
| `--force` | hash mismatch → اعمال بی‌صدا |
| `dump [--full]` | dump کامل یا incremental |
| `apply` | اعمال پچ‌های input.txt |
| `clean` | پاک‌کردن `_work/` |

## 🔄 گردش کار روزمره

    ۱. AI یک پچ می‌دهد.
    ۲. آن را در _work/input.txt می‌ریزی.
    ۳. python run.py
    ۴. _work/output.txt را به AI می‌دهی.
    ۵. AI وضعیت را می‌بیند و پچ بعدی را می‌دهد.

## 📚 مستندات کامل

همه‌چیز در **[PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)** — شامل:

- قوانین طلایی AI و قالب پاسخ اجباری
- گردش کار `run.py`، فلگ‌ها، مشخصات پارسر
- Hash verification و fuzzy matching
- `MSG-SEED` (ضد مسدود شدن اکانت)
- `CTX-DELTA` (ضد فراموشی کانتکست)
- خط قرمزها، git workflow، تست، رفع باگ، افزودن قابلیت
- Anti-patterns و Definition of Done
- Troubleshooting، راهنمای ترجمه، و چک‌لیست کاربر تازه

## 🎁 چرا متفاوت است؟

- **عمومی** — بدون محتوای اختصاصی. قابل استفاده برای هر پروژه.
- **بی‌هویت** — بدون اشاره به نویسنده یا پروژه‌ی مبدأ.
- **یک سند، یک ابزار** — بدون شلوغی فایل‌ها.
- **چندزبانه** — فارسی، انگلیسی، عربی.

## 📜 لایسنس

MIT — استفاده‌ی آزاد برای همه.

## 🙏 تقدیر

این پروژه از تجربه‌ی واقعی کار با AI در پروژه‌های متعدد شکل گرفته.
هدف: کمک به همه‌ی کسانی که می‌خواهند با AI کد بزنند — بدون دردسر.

---

⭐ اگر این پروژه کمکت کرد، یک ستاره بده.