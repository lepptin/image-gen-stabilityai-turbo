```markdown
# CPU-Based Local Image Generator / CPU Tabanlı Yerel Görsel Üretici

Welcome to this lightweight, CPU-optimized image generation repository. This project is designed for AI enthusiasts who want to experiment with text-to-image diffusion models locally on standard consumer hardware without requiring a high-end dedicated GPU.

Bu depo, yüksek performanslı bir harici GPU'ya ihtiyaç duymadan, standart tüketici donanımlarında yerel olarak yapay zeka tabanlı görsel üretmek isteyenler için tasarlanmış CPU optimizasyonlu hafif bir araçtır.

---

## 🌍 Language / Dil Seçimi
* [Türkçe Açıklama (#türkçe)]
* [English Description (#english)]

---

## Türkçe

### 📌 Proje Hakkında
Amatör olarak yerel (local) ortamımda yapay zeka ve görsel oluşturma modelleri üzerine araştırmalar yapıyorum. Tamamen CPU tabanlı çalışan bu basit Python scriptini, benim gibi kısıtlı donanımlarla yerel ortamda yapay zeka deneyimini yaşamak isteyen herkes için hazırladım. 

Süreç boyunca 3 farklı popüler modeli test ettim:
1. **SimianLuo/LCM_Dreamshaper_v7** (Hızlı ve kararlı)
2. **stabilityai/sdxl-turbo** (Ultra hızlı ve keskin portreler)
3. **PixArt-alpha/PixArt-XL-2-512x512** (Sanatsal ve detaylı)

**Kişisel Deneyim Notu:** Aşağıda detaylarını paylaştığım bilgisayar konfigürasyonuma göre, insan portresi oluşturmada en iyi gerçekçiliği ve netliği **stabilityai/sdxl-turbo** modeli ile elde ettim. Siz de kendi donanımınızla farklı denemeler yapabilir, aldığınız sonuçları ve görüşlerinizi benimle paylaşabilirsiniz!

### 💻 Test Edilen Sistem Konfigürasyonu
* **Model:** Dell Vostro 5471
* **İşlemci (CPU):** Intel® Core™ i7-8550U × 8
* **Dahili Grafik:** Intel® UHD Graphics 620 (KBL GT2)
* **Harici Grafik:** AMD Radeon™ R5 M465 Series
* **Bellek (RAM):** 24 GB
* **Depolama:** 376,1 GB Disk
* **İşletim Sistemi:** Ubuntu

---

### ⚙️ Kurulum ve Hazırlık

Scriptin çalışabilmesi için sisteminizde Python 3 ve gerekli kütüphanelerin yüklü olması gerekir. CPU üzerinde optimize çalışabilmesi adına `diffusers` ve `torch` kütüphanelerini yüklemek için terminalinizde şu komutu çalıştırın:

```bash
pip install torch diffusers transformers accelerate safetensors

```

---

### 🚀 Kullanım Rehberi (CLI Yardım İçeriği)

`generate.py` scripti terminal üzerinden dinamik parametreler alarak çalışır. Kullanabileceğiniz tüm argümanlar ve açıklamaları şunlardır:

| Argüman | Türü | Zorunlu mu? | Varsayılan | Açıklama |
| --- | --- | --- | --- | --- |
| `--model` | `str` | **Evet** | - | Kullanılacak model anahtarı: `lcm`, `turbo` veya `pixart`. |
| `--prompt` | `str` | **Evet** | - | Üretilmek istenen görselin İngilizce metin tarifi. |
| `--output` | `str` | Hayır | `output.png` | Üretilen görselin kaydedileceği dosya adı ve yolu. |
| `--width` | `int` | Hayır | `512` | Görselin piksel genişliği. |
| `--height` | `int` | Hayır | `512` | Görselin piksel yüksekliği. |
| `--steps` | `int` | Hayır | *Modele Bağlı* | Modelin varsayılan adım (inference steps) sayısını ezer. |
| `--cfg` | `float` | Hayır | *Modele Bağlı* | Modelin varsayılan CFG (Guidance Scale) değerini ezer. |
| `--seed` | `int` | Hayır | `None` | Aynı görseli tekrar üretebilmek için sabit rastgelelik değeri. |

#### 📝 Örnek Kullanım Komutu:

Aşağıdaki komut, parkta kitap okuyan bir adamın gerçekçi bir fotoğrafını üretir:

```bash
python generate.py --model turbo --prompt "candid photograph of a 22-year-old man sitting on a park bench reading a book, legs crossed, wearing beige trench coat and scarf, relaxed posture, soft afternoon light, natural facial expression, realistic clothing folds and skin details, photorealistic lifestyle photo" --width 640 --height 512 --steps 4 --cfg 1.1 --output reading_man.png

```

> 💡 **İpucu:** Farklı yaş, cinsiyet, dış mekan ve kompozisyon senaryolarını içeren diğer hazır komut örneklerine deponun içerisindeki `prompts.md` dosyasından ulaşabilirsiniz.

---

## English

### 📌 About the Project

I am an amateur AI researcher exploring image generation models in a local environment. I created this simple Python script, which runs entirely on the CPU, for anyone who wants to experience local AI generation using standard or limited hardware.

During my testing phase, I experimented with 3 different popular models:

1. **SimianLuo/LCM_Dreamshaper_v7** (Fast and stable)
2. **stabilityai/sdxl-turbo** (Ultra-fast and sharp portraits)
3. **PixArt-alpha/PixArt-XL-2-512x512** (Artistic and detailed)

**Personal Finding:** Based on my hardware configuration detailed below, I achieved the best photorealism and crispness for human portraits using **stabilityai/sdxl-turbo**. Feel free to run your own benchmarks on your hardware and share your thoughts!

### 💻 Tested Hardware Configuration

* **Model:** Dell Vostro 5471
* **Processor (CPU):** Intel® Core™ i7-8550U × 8
* **Integrated GPU:** Intel® UHD Graphics 620 (KBL GT2)
* **Dedicated GPU:** AMD Radeon™ R5 M465 Series
* **Memory (RAM):** 24 GB
* **Storage:** 376.1 GB Disk
* **OS:** Ubuntu

---

### ⚙️ Installation & Prerequisites

To run the script, you must have Python 3 and the required deep learning packages installed. Run the following command to install the required libraries optimized for CPU execution:

```bash
pip install torch diffusers transformers accelerate safetensors

```

---

### 🚀 Usage Guide (CLI Help Content)

The `generate.py` script accepts dynamic arguments directly from your terminal. Here is the complete list of available parameters:

| Argument | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `--model` | `str` | **Yes** | - | Model key to use: `lcm`, `turbo`, or `pixart`. |
| `--prompt` | `str` | **Yes** | - | Text description of the image to be generated. |
| `--output` | `str` | No | `output.png` | Filename/path where the output image will be saved. |
| `--width` | `int` | No | `512` | Width of the generated image in pixels. |
| `--height` | `int` | No | `512` | Height of the generated image in pixels. |
| `--steps` | `int` | No | *Model Default* | Overrides the model's default inference step count. |
| `--cfg` | `float` | No | *Model Default* | Overrides the model's default CFG (Guidance Scale). |
| `--seed` | `int` | No | `None` | Set a specific seed integer for reproducible outputs. |

#### 📝 Example Command:

The following command generates a photorealistic image of a man reading a book on a bench:

```bash
python generate.py --model turbo --prompt "candid photograph of a 22-year-old man sitting on a park bench reading a book, legs crossed, wearing beige trench coat and scarf, relaxed posture, soft afternoon light, natural facial expression, realistic clothing folds and skin details, photorealistic lifestyle photo" --width 640 --height 512 --steps 4 --cfg 1.1 --output reading_man.png

```

> 💡 **Tip:** For more structured prompt blueprints spanning multiple categories (close-up portraits, full-body outdoor shots, professional headshots), check out the provided `prompts.md` file.

```

```