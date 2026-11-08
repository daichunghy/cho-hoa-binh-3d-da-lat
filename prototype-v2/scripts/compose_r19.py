# -*- coding: utf-8 -*-
"""Ghép đối chiếu r19 (bản cuối đợt v4.8 + mục 7):
- r19 khung chuẩn: THẬT | TRƯỚC v4.7 | SAU v4.9 (v50: v4.8 + mục 7 + lớp GPT đã lọc)
- r19 GPT: ẢNH GỢI Ý ChatGPT | SAU v4.9 cùng góc
Chạy sau khi render_v50 xong: python3 scripts/compose_r19.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
REAL = os.path.join(ROOT, "..", "theme", "real-market")
GPT = os.path.join(ROOT, "..", "theme", "chatgpt-suggest")
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

def compose3(real, before, after, out, la, lb):
    canvas = Image.new("RGB", (PW * 3, PH))
    canvas.paste(panel(real, "ẢNH THẬT", la), (0, 0))
    canvas.paste(panel(before, "TRƯỚC — v4.7", lb), (PW, 0))
    canvas.paste(panel(after, "SAU — v4.9 (mục 7 + GPT lọc)", lb), (PW * 2, 0))
    canvas.save(out, quality=92)
    print("WROTE", out, canvas.size)

def compose2(gpt, after, out, sub):
    canvas = Image.new("RGB", (PW * 2, PH))
    canvas.paste(panel(gpt, "GỢI Ý — ChatGPT", sub), (0, 0))
    canvas.paste(panel(after, "SAU — v4.9 trong game", sub), (PW, 0))
    canvas.save(out, quality=92)
    print("WROTE", out, canvas.size)

compose3(os.path.join(REAL, "01-mat-tien-cho-ngay.jpg"),
         os.path.join(REN, "before-A-bung-binh-dem.png"),
         os.path.join(REN, "v51-A-bung-binh-dem.png"),
         os.path.join(REN, "r19-doi-chieu-bung-binh-mat-tien.png"),
         "chợ Đà Lạt, từ bùng binh", "góc A: trong đảo -> mặt tiền, 24mm")
compose3(os.path.join(REAL, "27-bung-binh-dem-tu-dinh-thang.jpg"),
         os.path.join(REN, "before-B-dinh-thang-dem.png"),
         os.path.join(REN, "v50-B-dinh-thang-dem.png"),
         os.path.join(REN, "r19-doi-chieu-dem-dinh-thang.png"),
         "bùng binh về đêm, từ đỉnh thang", "góc B: đỉnh thang -> đảo, 24mm")
compose2(os.path.join(GPT, "gpt-bung-binh.png"),
         os.path.join(REN, "v51-A-bung-binh-dem.png"),
         os.path.join(REN, "r19-doi-chieu-gpt-bung-binh.png"),
         "góc A: bùng binh -> mặt tiền")
compose2(os.path.join(GPT, "gpt-duong-vao.png"),
         os.path.join(REN, "v50-a-duong-vao-dem.png"),
         os.path.join(REN, "r19-doi-chieu-gpt-duong-vao.png"),
         "góc đường vào -> bùng binh + mặt tiền")
