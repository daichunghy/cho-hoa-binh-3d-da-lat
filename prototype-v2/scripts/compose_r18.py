# -*- coding: utf-8 -*-
"""Ghép file đối chiếu r18: 3 panel 1280x720 (THẬT | TRƯỚC v4.7 | SAU v4.8)
cùng định dạng panel của r17 (ảnh thật cạnh render cùng góc).
Chạy: python3 scripts/compose_r18.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REAL = os.path.join(ROOT, "..", "theme", "real-market")
REN = os.path.join(ROOT, "renders")
PW, PH = 1280, 720

def panel(path, label, sub):
    im = Image.open(path).convert("RGB")
    # center-crop về 16:9 rồi resize 1280x720
    w, h = im.size
    t = 16 / 9
    if w / h > t:
        nw = int(h * t); x0 = (w - nw) // 2; im = im.crop((x0, 0, x0 + nw, h))
    else:
        nh = int(w / t); y0 = (h - nh) // 2; im = im.crop((0, y0, w, y0 + nh))
    im = im.resize((PW, PH), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, PW, 46], fill=(20, 12, 6))
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except Exception:
        f = ImageFont.load_default()
    d.text((16, 9), label, font=f, fill=(255, 220, 150))
    d.text((PW - 16 - d.textlength(sub, font=f), 9), sub, font=f, fill=(230, 220, 200))
    return im

def compose(real, before, after, out, la, lb):
    canvas = Image.new("RGB", (PW * 3, PH))
    canvas.paste(panel(real, "ẢNH THẬT", la), (0, 0))
    canvas.paste(panel(before, "TRƯỚC — v4.7", lb), (PW, 0))
    canvas.paste(panel(after, "SAU — v4.8", lb), (PW * 2, 0))
    canvas.save(out, quality=92)
    print("WROTE", out, canvas.size)

compose(os.path.join(REAL, "01-mat-tien-cho-ngay.jpg"),
        os.path.join(REN, "before-A-bung-binh-dem.png"),
        os.path.join(REN, "v48-A-bung-binh-dem.png"),
        os.path.join(REN, "r18-doi-chieu-bung-binh-mat-tien.png"),
        "chợ Đà Lạt, từ bùng binh", "góc A: trong đảo -> mặt tiền, 24mm")
compose(os.path.join(REAL, "27-bung-binh-dem-tu-dinh-thang.jpg"),
        os.path.join(REN, "before-B-dinh-thang-dem.png"),
        os.path.join(REN, "v48-B-dinh-thang-dem.png"),
        os.path.join(REN, "r18-doi-chieu-dem-dinh-thang.png"),
        "bùng binh về đêm, từ đỉnh thang", "góc B: đỉnh thang -> đảo, 24mm")
