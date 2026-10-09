# 🚀 context-forge

**Sen vs. her şeyi unutan yapay zekâ sohbeti.**

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
  <b>Türkçe</b> ·
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
  <a href="README.ro.md">Română</a>
</p>

---

## Tanıdık geldi mi?

- 😤 **Yapay zekâyla 3 saat kod yazdın. Sohbet limitine ulaştı. Her şey gitti.**
- 🤯 **Yapay zekâ iki mesaj önce karar verdiğini unutuyor.**
- 💸 **Her yeni mesajda tüm projeyi yapıştırıyorsun — token yakıyor, zaman kaybediyorsun.**
- 🤖 **Yapay zekâ kodu elle değiştiriyor, bir şeyleri kırıyor, neden bilmiyorsun.**
- 😴 **İnşa etmekten çok açıklamaya zaman harcıyorsun.**
- 🚫 **Sürekli "çok fazla mesaj, sonra dene" alıyorsun.**

**Evet?** Öyleyse bu senin için.

---

## Bu nedir?

Herhangi bir yapay zekâ sohbetine yapıştırdığın **tek bir belge** (`PROJECT_CONTEXT.md`) — DeepSeek, Claude, ChatGPT, Gemini. Geveze bir yapay zekâyı **disiplinli bir proje ortağına** dönüştürür, o:

- ✅ **Asla bağlamı kaybetmez** — her cevap proje durumunu ileri taşır.
- ✅ **Asla kodunu elle değiştirmez** — yama gönderir, sen yapıştırırsın, bir komut uygular.
- ✅ **Asla token yakmaz** — sadece ihtiyaç duyduğu dosyayı ister, tüm projeyi değil.
- ✅ **Asla hesabını engellemez** — dahili anti-limit protokolü.
- ✅ **Asla 10 komut istemez** — yapıştır, bir tane çalıştır, bitti.
- ✅ **Nerede olduğunuzu asla unutmaz** — sonraki sohbet tam kaldığınız yerden devam eder.

**Bir belge. Bir araç. Bir komut. Hepsi bu.**

---

## Nasıl çalışır (3 adım)

### 1. Belgeyi al
Bu depodan [`PROJECT_CONTEXT.en.md`](PROJECT_CONTEXT.en.md) dosyasını indir.

### 2. Yapay zekâ sohbetine yapıştır
DeepSeek (veya Claude, ChatGPT, Gemini) ile yeni bir sohbet aç. Tüm belgeyi **ilk mesaj** olarak yapıştır. Ne inşa etmek istediğini bir satırda yaz.

### 3. Yapay zekâyı takip et
Yapay zekâ sana `run.py` (küçük bir Python aracı) verir. Kaydet. O andan itibaren:

> **Yapıştır → `python run.py` çalıştır → çıktıyı geri gönder.**

Tüm iş akışı bu. Sonsuza kadar.

---

## Ne elde edersin

| Önce | Sonra |
|------|-------|
| Sohbet bağlamı kaybeder | Bağlam her mesajda yaşar |
| Yanıt başına 5000 token | Yanıt başına ~300 token |
| Yapay zekâ tahmin eder | Yapay zekâ bilir |
| Değişiklik başına 10 komut | Değişiklik başına 1 komut |
| Hesap engellendi | Hesap güvende |
| "Neredeydik?" | "İşte sonraki yama." |

**%40–80 daha az token. Sıfır bağlam kaybı. Sıfır elle düzenleme.**

---

## Her dille çalışır

Rust, Python, Node, Go, C++, ne olursa. `run.py`'ye projeni nasıl derleyip test edeceğini bir kez söylersin — protokol tüm diller için aynıdır.

---

## Belgenin dili

Kural belgesi **yalnızca İngilizce** — böylece her yapay zekâ onu aynı şekilde ayrıştırır ve tek bir gerçek kaynağı olur.

**Ama yapay zekânla konuşma senin dilinde.** İlk mesajını Türkçe, Farsça, Arapça, Çince yaz — yapay zekâ aynı dilde yanıtlar. Belge evrenseldir.

---

## Elde ettiğin dosyalar

- `PROJECT_CONTEXT.en.md` — kural belgesi (bunu yapay zekâna yapıştır)
- `run.py` — araç (ilk kullanımda yapay zekâ verir)
- `README.md` + çeviriler — bu sayfa, çok dilli
- `LICENSE` — MIT, ne istersen yap

---

## SSS

**Kodlamayı bilmem gerekir mi?**
Pek değil. Bir mesaj yapıştırıp bir komut çalıştırabiliyorsan kullanabilirsin.

**Hangi yapay zekâ en iyi?**
DeepSeek — protokolü en hassas şekilde takip eder. Claude, ChatGPT, Gemini de çalışır.

**Ücretsiz mi?**
Belge ve araç MIT. Yapay zekâ API'si sağlayıcının ücreti.

**Bir şey bozulursa?**
Her şey git ile sürümlenmiştir. Bir komutla geri dön. Belge açıklar.

---

## Hazır mısın?

1. **[`PROJECT_CONTEXT.en.md`'yi indir](PROJECT_CONTEXT.en.md)**
2. Yapay zekâ sohbetine yapıştır
3. Söyle: *"X inşa etmek istiyorum. Başla."*

**Hepsi bu. Yapay zekânla savaşmayı bırak. İnşa etmeye başla.**

---

*Göndermek isteyenler için, sohbet penceresine bakmak değil.*