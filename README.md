# 🔨 context-forge

> **Universal PROJECT_CONTEXT template + `run.py` for AI-assisted coding.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

<p align="center">
  <b>English</b> ·
  <a href="README.fa.md">فارسی</a> ·
  <a href="README.ar.md">العربية</a>
</p>

---

## 🎯 مشکل

اگر با AI کد می‌زنی، این دردها را دیده‌ای:

- ❌ چت به لیمیت می‌خورد → از صفر توضیح بده.
- ❌ توکن‌سوزی → هر بار کل پروژه را بفرست.
- ❌ AI لنگر را اشتباه می‌زند → کد خراب می‌شود.
- ❌ اکانت مسدود می‌شود → پیام‌های تکراری.
- ❌ AI یادش می‌رود کانتکست بدهد → چت جدید گم می‌شود.

## 💡 راه‌حل

**context-forge** یک سند واحد + یک ابزار است:

- ✅ **PROJECT_CONTEXT.md** — قانون اساسی (۳۷+ بخش، همه‌چیز این‌جاست).
- ✅ **run.py** — ابزار فلگ‌محور با ۱۵+ فلگ.
- ✅ **Pull نه Push** — AI فقط چیزی را می‌خواهد که لازم دارد.
- ✅ **MSG-SEED** — ضد مسدود شدن اکانت.
- ✅ **CTX-DELTA** — ضد فراموشی کانتکست.

## 🚀 شروع سریع

    git clone https://github.com/ama1372/context-forge.git my-project
    cd my-project
    mkdir _work
    python run.py --version
    python run.py --status

## 📂 ساختار (حداقلی)

    my-project/
    ├── PROJECT_CONTEXT.md   ← همه‌چیز این‌جاست
    ├── run.py               ← ابزار
    ├── README.md            ← همین فایل
    ├── LICENSE              ← MIT
    ├── .gitignore
    └── _work/               ← ارتباط با AI

## 🔄 گردش کار روزمره

    1. AI یک پچ می‌دهد.
    2. آن را در _work/input.txt می‌ریزی.
    3. python run.py
    4. _work/output.txt را به AI می‌دهی.
    5. AI وضعیت را می‌بیند و پچ بعدی را می‌دهد.

## 📚 مستندات کامل

همه‌چیز در **[PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)**:

- قوانین طلایی AI و قالب پاسخ اجباری
- گردش کار `run.py`، فلگ‌ها، مشخصات پارسر
- Hash verification و fuzzy matching
- MSG-SEED (ضد مسدود شدن اکانت)
- CTX-DELTA (ضد فراموشی کانتکست)
- خط قرمزها، git workflow، تست، رفع باگ، افزودن قابلیت
- Anti-patterns و Definition of Done
- Troubleshooting و نمونه‌های کامل

## 🎁 چرا متفاوت است؟

- **عمومی** — بدون محتوای اختصاصی.
- **بی‌هویت** — بدون اشاره به نویسنده یا پروژه‌ی مبدأ.
- **یک سند، یک ابزار** — بدون شلوغی فایل‌ها.
- **چندزبانه (در آینده)** — فارسی، انگلیسی، عربی.

## 📜 لایسنس

MIT — استفاده‌ی آزاد برای همه.

## 🤝 مشارکت

اول [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) را بخوان.

---

⭐ اگر این پروژه کمکت کرد، یک ستاره بده.