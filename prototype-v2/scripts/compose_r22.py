# -*- coding: utf-8 -*-
"""Ghép đối chiếu r22 (đợt kiểm chứng V5.1+V5.2):
TƯ LIỆU ĐÊM (research/18) | TRƯỚC v5.0 | SAU v5.1+v5.2 (+ khối quét chi tiết), cùng góc A đêm."""
import os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REAL = os.path.join(ROOT, "..", "theme", "real-market")
REN = os.path.join(ROOT, "renders")
PW, PH = 1280, 720
def panel(path, label, sub):
    im = Image.open(path).convert("RGB")
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
canvas = Image.new("RGB", (PW * 3, PH))
canvas.paste(panel(os.path.join(REAL, "28-bung-binh-dem-mat-dat-xe-nguoi.jpg"), "TƯ LIỆU ĐÊM — research/18", "bùng binh về đêm, xe + người kín vành"), (0, 0))
canvas.paste(panel(os.path.join(REN, "v52-A-bung-binh-dem.png"), "ĐẦU ĐỢT — v5.0", "góc A đêm: trong đảo -> mặt tiền, 24mm"), (PW, 0))
canvas.paste(panel(os.path.join(REN, "v53-C-crowd-dem.png"), "SAU QUÉT — cận đám đông", "giỏ dâu/chậu chân sạp + trang phục 4 phom"), (PW * 2, 0))
out = os.path.join(REN, "r22-doi-chieu-sau-quet.png")
canvas.save(out, quality=92)
print("WROTE", out, canvas.size)
