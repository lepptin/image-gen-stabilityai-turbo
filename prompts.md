```markdown
# 📋 Example Prompts / Örnek Promptlar

This file contains structured example prompts and terminal commands categorized by shot types to test your local image generator.
Bu dosya, yerel görsel üreticinizi test etmeniz için çekim türlerine göre kategorize edilmiş örnek promptları ve terminal komutlarını içerir.

---

## 🔍 Close-Up Portraits / Yakın Çekim Portreler

### 1. PROFESYONEL KADIN / PROFESSIONAL WOMAN
```bash
python generate.py --model turbo --prompt "corporate headshot of a professional woman in her late twenties, curly auburn hair, natural freckles, soft window light, business portrait, shot on 85mm f/1.8, photorealistic, clean background, highly detailed skin pores" --width 512 --height 512 --steps 2 --cfg 1.0 --output headshot_woman.png

```

### 2. YAŞLI ZANAATKAR / ELDERLY ARTISAN

```bash
python generate.py --model turbo --prompt "Ultra-realistic portrait of an elderly artisan in a dusty workshop, deep wrinkles, kind eyes, soft natural light through a window, 8k resolution, cinematic lighting, masterpiece, highly detailed skin texture" --width 512 --height 512 --steps 3 --cfg 1.1 --output artisan.png

```

### 3. ASYALI ERKEK / ASIAN MAN

```bash
python generate.py --model turbo --prompt "professional headshot of a 40-year-old Asian man, short black hair, clean shaven, wearing crisp white shirt, neutral studio background, soft diffused lighting, realistic facial features, natural skin tone, photorealistic portrait, 8k resolution" --width 512 --height 512 --steps 2 --cfg 1.0 --output headshot_man.png

```

---

## 📐 Medium and Three-Quarter Shots / Orta ve Üç Çeyrek Çekimler

### 4. ORMANDAKİ GENÇ KADIN / YOUNG WOMAN IN THE FOREST

```bash
python generate.py --model turbo --prompt "Close-up photorealistic portrait of a young woman with freckles, wearing a green linen scarf, outdoors in a forest, soft bokeh background, morning sunlight, shot on 85mm lens, f/1.8, extremely detailed eyes and eyelashes" --width 512 --height 640 --steps 3 --cfg 1.1 --output forest_woman.png

```

### 5. AKDENİZLİ KADIN / MEDITERRANEAN WOMAN

```bash
python generate.py --model turbo --prompt "cinematic portrait of a 60-year-old Mediterranean woman, silver wavy hair, warm brown eyes, gentle smile, wearing knitted cardigan, window light illuminating face from left, shot on Sony A7R IV 50mm f/1.8, ultra-detailed skin wrinkles and texture, lifelike, no digital smoothing, photorealistic" --width 512 --height 640 --steps 4 --cfg 1.1 --output mediterranean_woman.png

```

### 6. KOT CEKETLİ LATİN ERKEK / LATINO MAN IN A DENIM JACKET

```bash
python generate.py --model turbo --prompt "medium shot of a 25-year-old Latino man with tan skin, short faded haircut, wearing vintage denim jacket over plain white t-shirt, casual stance, outdoor golden hour lighting, realistic fabric details and skin pores, photorealistic, 4k quality" --width 512 --height 640 --steps 4 --cfg 1.2 --output latino_man.png

```

### 7. İSKANDİNAV ERKEK / SCANDINAVIAN MAN

```bash
python generate.py --model turbo --prompt "three-quarter portrait of a 45-year-old Scandinavian man, light blue eyes, short blond hair, light stubble, wearing olive green wool coat and turtleneck sweater, overcast natural light, highly detailed facial structure and clothing texture, unretouched photorealistic style" --width 512 --height 640 --steps 4 --cfg 1.1 --output scandi_man.png

```

---

## 🌲 Full-Body and Outdoor / Tam Boy ve Dış Mekan

### 8. MODERN GÖKDELEN ÖNÜNDE MİMAR / ARCHITECT IN FRONT OF A MODERN SKYSCRAPER

```bash
python generate.py --model turbo --prompt "A professional architect standing in front of a modern glass skyscraper during golden hour, reflecting city lights, sharp suit, holding blueprints, architectural photography, hyper-realistic, volumetric lighting, wide angle shot, clear facial features" --width 768 --height 512 --steps 4 --cfg 1.2 --output architect.png

```

### 9. İŞKADINI / BUSINESSWOMAN

```bash
python generate.py --model turbo --prompt "full body photograph of a 32-year-old Black woman, athletic build, wearing charcoal gray business suit and black leather shoes, standing confidently, natural daylight, urban sidewalk background, realistic skin texture, photorealistic, shot on Canon EOS R5 35mm f/1.4" --width 512 --height 768 --steps 5 --cfg 1.2 --output black_woman_full.png

```

### 10. SALVADOR SOKAKLARINDA BREZİLYALI KADIN / BRAZILIAN WOMAN ON THE STREETS OF SALVADOR

```bash
python generate.py --model turbo --prompt "Full-body photorealistic portrait of a 25-year-old Brazilian woman standing on a vibrant street in Salvador, wearing a colorful flowing summer dress with floral patterns, leather sandals, sunlight dappling through trees, 8k resolution, sharp focus, natural pose, detailed skin tones" --width 512 --height 768 --steps 5 --cfg 1.2 --output brazil_woman.png

```

### 11. KOŞAN KADIN / JOGGING WOMAN

```bash
python generate.py --model turbo --prompt "action shot of a 30-year-old woman jogging in a park, wearing black running leggings and sports top, hair tied in ponytail, mid-stride pose, morning sunlight filtering through trees, realistic motion blur on background, sharp focus on subject, photorealistic sports photography" --width 512 --height 768 --steps 5 --cfg 1.3 --output jogging.png

```

### 12. BANKTA KİTAP OKUYAN ADAM / MAN READING A BOOK ON A BENCH

```bash
python generate.py --model turbo --prompt "candid photograph of a 22-year-old man sitting on a park bench reading a book, legs crossed, wearing beige trench coat and scarf, relaxed posture, soft afternoon light, natural facial expression, realistic clothing folds and skin details, photorealistic lifestyle photo" --width 640 --height 512 --steps 4 --cfg 1.1 --output reading_man.png

```

### 13. TAKSİ ÇAĞIRAN KADIN / WOMAN HAILING A TAXI

```bash
python generate.py --model turbo --prompt "dynamic portrait of a 38-year-old woman raising her hand to hail a taxi, standing on city street, wearing red coat and black boots, urban background with blurred traffic, realistic wind-blown hair, natural lighting, shot on Leica M10 50mm f/1.4, highly detailed photorealistic image" --width 512 --height 768 --steps 5 --cfg 1.2 --output taxi_woman.png

```

### 14. İZLANDA'DA ETİYOPYALI DAĞCI / ETHIOPIAN HIKER IN ICELAND

```bash
python generate.py --model turbo --prompt "Full-body photorealistic shot of a 35-year-old Ethiopian male hiker standing on a snowy ridge in Iceland at night, wearing a high-tech bright orange puffer jacket and professional trekking trousers, vibrant Aurora Borealis in the background, headlamp glowing, 8k resolution, crisp details, hyper-realistic textures" --width 512 --height 768 --steps 5 --cfg 1.2 --output iceland_hiker.png

```

### 15. AMALFİ KIYISINDA İTALYAN KADIN / ITALIAN WOMAN ON THE AMALFI COAST

```bash
python generate.py --model turbo --prompt "A full-length portrait of a 50-year-old Italian woman walking on a rugged coastal path in Amalfi, wearing a white linen jumpsuit and wide-brimmed straw hat, carrying a leather backpack, turquoise sea and limestone cliffs in the background, bright noon sunlight, sharp focus on fabric and skin, professional travel photography" --width 512 --height 768 --steps 5 --cfg 1.2 --output amalfi_woman.png

```

### 16. TROPİKAL ORMANDA TAYLAND'LI BİYOLOG / THAI BIOLOGIST IN A TROPICAL RAINFOREST

```bash
python generate.py --model turbo --prompt "Full-body cinematic shot of a 28-year-old Thai biologist standing inside a dense tropical rainforest, wearing khaki tactical vest and cargo pants, holding a vintage camera, misty atmosphere with sunbeams filtering through giant palm leaves, extreme detail on foliage and equipment, realistic proportions, 85mm lens style" --width 512 --height 768 --steps 5 --cfg 1.2 --output biologist.png

```

```

```
