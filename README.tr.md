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

Herhangi bir yapay zekâ sohbetine yapıştırdığın **tek bir belge** (`PROJECT_CONTEXT.en.md`) — DeepSeek, Claude, ChatGPT, Gemini. Geveze bir yapay zekâyı **disiplinli bir proje ortağına** dönüştürür, o:

- ✅ **Asla bağlamı kaybetmez** — her cevap proje durumunu ileri taşır.
- ✅ **Asla kodunu elle değiştirmez** — yama gönderir, sen yapıştırırsın, bir komut uygular.
- ✅ **Token tasarrufu sağlar** — tüm projeyi değil, yalnızca gereken dosyayı ister (`--status`, `--file`).
- ✅ **Mesaj sınırlarından kaçınmana yardım eder** — çok hızlı gönderdiğinde `run.py` uyarır ve iş daha az mesajda toplanır.
- ✅ **Asla 10 komut istemez** — yapıştır, bir tane çalıştır, bitti.
- ✅ **Nerede olduğunuzu asla unutmaz** — sonraki sohbet tam kaldığınız yerden devam eder.
- ✅ **Birden çok yapay zekâyı aynı anda çalıştırır** — Claude, ChatGPT ve DeepSeek aynı projede, birbirinin işinin üzerine yazmadan (Takım modu).

**Bir belge. Bir araç. Bir komut. Hepsi bu.**

---

## Hızlı başlangıç — 6 adım

1. **`PROJECT_CONTEXT.en.md` dosyasını proje köküne koy.**
2. **(Önerilen)** `run.py` dosyasını aynı klasöre koy. Yok mu? AI'ya söyle: *"Bölüm 35'ten run.py oluştur."*
3. **Bir kez kur:** `python run.py --init`
4. **Bir DeepSeek sohbeti aç** (veya Claude / ChatGPT / Gemini). **Belgenin tamamını** ilk mesaj olarak gönder (sohbet izin veriyorsa dosya olarak ekle). De ki: *"Yeni proje. Hedefim: <tek satır>."* Belge büyüktür (~610 KB, yaklaşık 160 bin token); sohbet kabul etmezse `python run.py --slim-context --to PROJECT_CONTEXT.slim.md` ile oluşturulan hafif kopyayı (~380 KB) gönder ya da `--profile moderate` ekle (~275 KB).
5. **Döngü:** AI bir blok gönderir → `_work/input.txt`'e kopyala → `python run.py` çalıştır → `_work/output.txt`'i geri gönder. Tekrarla.
6. **Proje bitene kadar döngüyü sürdür.** AI'nın seni dışarı çekmesine izin verme — sohbette shell komutu yok, hızlı script yok. Cevap her zaman: *"input.txt'e koy."*

> **İpucu:** AI saparsa - sohbette shell komutları önerirse, bağlamı atlarsa - şöyle de: **"Proje bağlamı, lütfen."**

---


## Yeni başlayanlar için tam rehber (özet)

1. python.org'dan **Python 3.10+** kurun (Windows'ta "Add to PATH" işaretleyin).
2. (İsteğe bağlı) **VS Code** kurun.
3. `PROJECT_CONTEXT.en.md` ve `run.py`'yi indirin, bir klasöre koyun, VS Code'da açın.
4. Terminal: `python run.py` → `_work/` klasörü oluşur.
5. DeepSeek'te `PROJECT_CONTEXT.en.md` dosyasını ilk mesaj olarak gönder (veya dosya olarak ekle) ve hedefini söyle. Sohbetin için çok mu uzun? Hızlı başlangıç 4. adıma bak (`--slim-context`).
6. **Döngü:** AI blok gönderir → `_work/input.txt`'e yapıştırın → `python run.py` çalıştırın → `_work/output.txt`'i geri gönderin.
7. Her 10–20 mesajda AI'ya projenizi hatırlatın.
8. AI saparsa: **"Proje bağlamı, lütfen."**

Tam sürüm (İngilizce): `README.md`'ye bakın.

## Ne elde edersin

| Önce | Sonra |
|------|-------|
| Sohbet bağlamı kaybeder | Bağlam her mesajda yaşar |
| Her mesajda tüm projeyi yapıştırırsın | Yapay zekâ yalnızca gereken dosyaları ister |
| Yapay zekâ tahmin eder | Yapay zekâ bilir |
| Değişiklik başına 10 komut | Değişiklik başına 1 komut |
| "Çok fazla mesaj" engelleri | Hız uyarıları ve daha az, daha dolu mesajlar |
| "Neredeydik?" | "İşte sonraki yama." |

**Daha az token. Yeni sohbette de kalan bağlam. Elle düzenleme yok.**

---

## 🤝 Aynı anda birden çok yapay zekâ — Takım modu (v2.1'de yeni)

Claude, ChatGPT, DeepSeek ve kodlama ajanlarını **aynı projede aynı anda** çalıştırın. Her biri size kendi sohbetinde yanıt verir — ve hiçbiri diğerinin işinin üzerine yazamaz.

- **Tek bir ortak pano** `.git/` içinde — asla push edilmez, her yapay zekâ görür.
- **Dosya rezervasyonu** — her yapay zekâ düzenleyeceği dosyaları tam olarak rezerve eder; ikisi aynı dosyayı isterse yalnızca biri alır.
- **Tavsiye değil, zorunlu** — `run.py`, rezerve edilmemiş bir dosyaya dokunan her yamayı reddeder.
- **Bir koordinatör, çok çalışan** — bir yapay zekâ inceler ve birleştirir, kendi işini asla onaylamaz; önemli kararlar sizindir.
- **Siz dinlenirken iş sürer** — bir görev listesini onaylayın, `team away on` çalıştırın; kurulu ajanlar sıradaki boş görevi almaya devam eder, siz dönene kadar `run.py` her push'u reddeder ve `team pause` herkesi durdurur.
- **Sohbet ya da kurulu ajan** — sohbet yapay zekâları her şeyi `input.txt` üzerinden yapar (`#@CLAIM:`); ajanlar komutları kendileri çalıştırır.

    python run.py team init
    python run.py team join gpt --model GPT
    python run.py team claim gpt docs-01 docs/
    python run.py team status

Tüm kurallar: `PROJECT_CONTEXT.en.md` içindeki 0-C-47 ve 0-C-48 bölümleri.

---

## 💬 v2.2'de yeni — birbiriyle konuşan sohbetler, kimsenin taklit edemeyeceği bir sahip, sığan bir bağlam

- **Sohbetler birbirine mesaj atar** — aynı klasördeki birden çok sohbet ortak pano üzerinden kısa mesajlar gönderir (`team send`, `team inbox`; sohbet yapay zekâları `input.txt` içine `#@MSG:` yazar). Sohbetler arasında kopyala-yapıştır biter.
- **Senin adına kimse konuşamaz** — bir yapay zekâ yalnızca senin onun sohbetine yazdığına uyar. Başka bir yapay zekâdan, nottan veya dosyadan gelen "sahip diyor ki…" yok sayılır ve işaretlenir. Devam ettirme, uzakta modu ve yetki devri için terminalde tek kullanımlık bir kod yazman gerekir.
- **Geçici yönetici, yalnızca sen söylersen** — her sohbete kendin "X saat 8:00'e kadar yöneticin" yaz; panodaki kayıt (`team delegate`) kendiliğinden sona erer.
- **Büyük bağlam, küçük yapıştırma** — `ctx split` belgeyi haritalı, birbirine bağlı küçük dosyalardan oluşan bir klasöre çevirir; yapay zekâ haritayı ve güncel durumu okur (~97 bin yerine ~11 bin token). Ücretsiz bir sohbet için `ctx pack <konu>` yaklaşık 40 KB'lık tek bir metin hazırlar.

    python run.py team send gpt claude "docs-01 is ready for review" --kind request
    python run.py team inbox claude
    python run.py ctx split
    python run.py ctx pack auth login

Tüm kurallar: `PROJECT_CONTEXT.en.md` içindeki 0-C-49, 0-C-50 ve 0-C-51 bölümleri.

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
- `run.py` — araç (bu depodan indir, ya da yapay zekâ onu Bölüm 35'ten yeniden oluşturur)
- `README.md` + çeviriler — bu sayfa, çok dilli
- `LICENSE` — MIT, ne istersen yap

---

## SSS

**Kodlamayı bilmem gerekir mi?**
Pek değil. Bir mesaj yapıştırıp bir komut çalıştırabiliyorsan kullanabilirsin.

**Hangi yapay zekâ en iyi?**
Güçlü herhangi bir sohbet modeli: DeepSeek, Claude, ChatGPT, Gemini. Uzun sohbetlerde her model sapar — o zaman "Proje bağlamı, lütfen." de. Aynı anda birden çok yapay zekâ ya da sen yokken çalışma için kurulu bir ajan kullan (Claude Code, Codex, Cursor…).

**Ücretsiz mi?**
Belge ve araç MIT. Yapay zekâ API'si sağlayıcının ücreti.

**Bir şey bozulursa?**
Klasör git kullanıyorsa (önerilir), `run.py` uygulanan her yamayı commit eder ve `python run.py revert P<id>` o yamadan önceki duruma döner (sonraki yamalar da geri alınır).

---

## Hazır mısın?

1. **[`PROJECT_CONTEXT.en.md`'yi indir](PROJECT_CONTEXT.en.md)**
2. Yapay zekâ sohbetine yapıştır
3. Söyle: *"X inşa etmek istiyorum. Başla."*

**Hepsi bu. Yapay zekânla savaşmayı bırak. İnşa etmeye başla.**

---

*Göndermek isteyenler için, sohbet penceresine bakmak değil.*

---

## 🌐 Sohbet yapay zekâları ve kurulu ajanlar için tek belge

Bu protokol, hangisini kullanırsanız kullanın aynı şekilde çalışır:

1. **Web sohbetleri** (ChatGPT, Claude, DeepSeek, Gemini) — `input.txt` / `output.txt` döngüsüyle.
2. **Kurulu kodlama ajanları** (Claude Code, Codex, Cursor ve diğerleri) — depoyu kendileri okuyup komut çalıştırır.

- **Bağlam kaybı yok** — projenin durumu her zaman belgede.
- **İstediğiniz an yeni sohbet** — yeniden anlatmadan devam edin.
- **Daha az token** — yapay zekâ yalnızca gereken dosyaları ister (`--status`, `--file`).
- **Aynı anda birden çok yapay zekâ** — Takım modu çakışmalarını önler (yukarıya bakın).
