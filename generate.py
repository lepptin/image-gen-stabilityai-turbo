import argparse
import os
import torch
from diffusers import DiffusionPipeline

# ---------------------------------------------------------
# VARSAYILAN MODEL AYARLARI
# ---------------------------------------------------------
MODEL_CONFIGS = {
    "lcm": {
        "id": "SimianLuo/LCM_Dreamshaper_v7",
        "steps": 6,
        "guidance_scale": 1.5,
        "desc": "Hızlı ve stabil (LCM)"
    },
    "turbo": {
        "id": "stabilityai/sdxl-turbo",
        "steps": 2,
        "guidance_scale": 1.0, 
        "desc": "Ultra hızlı / Keskin Portreler (SDXL Turbo)"
    },
    "pixart": {
        "id": "PixArt-alpha/PixArt-XL-2-512x512",
        "steps": 20,
        "guidance_scale": 4.5,
        "desc": "Sanatsal ve Detaylı (PixArt)"
    }
}

def generate_image(model_key, prompt, output_path, height, width, steps, cfg, seed=None):
    if model_key not in MODEL_CONFIGS:
        raise ValueError(f"❌ Desteklenmeyen model: '{model_key}'")
    
    config = MODEL_CONFIGS[model_key]
    model_id = config["id"]
    
    # Parametre hiyerarşisi: Manuel Giriş > Model Varsayılanı
    final_steps = steps if steps is not None else config["steps"]
    final_cfg = cfg if cfg is not None else config["guidance_scale"]
    
    print(f"🔄 Model: {model_id}")
    print(f"📊 Ayarlar: {width}x{height} | {final_steps} adım | CFG: {final_cfg}")
    
    try:
        pipe = DiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32, 
            use_safetensors=True
        )
        pipe.to("cpu")
        pipe.enable_attention_slicing()

        generator = torch.Generator("cpu").manual_seed(seed) if seed is not None else None

        # Güçlendirilmiş Negatif Prompt
        negative_prompt = (
            "bad anatomy, deformed, extra fingers, blurry, low quality, watermark, "
            "deformed iris, asymmetrical eyes, mutated hands, melted face, "
            "gross proportions, malformed limbs, misshapen body, out of frame"
        )
        
        image = pipe(
            prompt=prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=final_steps,
            guidance_scale=final_cfg,
            height=height,
            width=width,
            generator=generator
        ).images[0]

        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
        image.save(output_path)
        print(f"✅ Görsel kaydedildi: {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"❌ Hata: {e}")

def main():
    parser = argparse.ArgumentParser(description="Dinamik Parametreli Görsel Üretici")
    parser.add_argument("--model", type=str, required=True, choices=list(MODEL_CONFIGS.keys()))
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--output", type=str, default="output.png")
    parser.add_argument("--seed", type=int, default=None)
    
    # Dinamik Parametreler (Varsayılan None bırakıldı ki sözlükten çekebilelim)
    parser.add_argument("--height", type=int, default=512)
    parser.add_argument("--width", type=int, default=512)
    parser.add_argument("--steps", type=int, default=None, help="Modelin varsayılan adım sayısını ezer")
    parser.add_argument("--cfg", type=float, default=None, help="Modelin varsayılan CFG değerini ezer")

    args = parser.parse_args()

    generate_image(
        model_key=args.model,
        prompt=args.prompt,
        output_path=args.output,
        height=args.height,
        width=args.width,
        steps=args.steps,
        cfg=args.cfg,
        seed=args.seed
    )

if __name__ == "__main__":
    main()
