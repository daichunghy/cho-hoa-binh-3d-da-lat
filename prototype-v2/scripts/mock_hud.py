# -*- coding: utf-8 -*-
"""Ghép MÔ PHỎNG lớp UI game (HUD nhiệm vụ / thẻ khu vực / minimap / popup +Xu /
cột sáng dẫn đường) lên ảnh render hành trình (a) — chỉ để hình dung, UI thật
chạy bằng DOM/canvas trong index.html.
Chạy: python3 scripts/mock_hud.py [input.png] [output.png]
"""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = sys.argv[1] if len(sys.argv) > 1 else 'renders/v42-a-duong-vao-dem.png'
DST = sys.argv[2] if len(sys.argv) > 2 else 'renders/v42-f-ui-mock.png'
img = Image.open(SRC).convert('RGB')
W, H = img.size
S = W / 896.0  # hệ số theo bản full 896x672

def font(sz, bold=True):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    return ImageFont.truetype(p, int(sz * S))

ov = Image.new('RGBA', (W, H), (0, 0, 0, 0))
d = ImageDraw.Draw(ov)
BROWN = (43, 29, 18, 225); BRASS = (216, 164, 65, 255); CREAM = (255, 233, 176, 255); GOLD = (255, 201, 60, 255)

def panel(x, y, w, h, r=14):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r * S, fill=BROWN, outline=BRASS, width=max(1, int(2 * S)))

# --- cột sáng dẫn đường tại vòng xoay (vị trí ước lượng trong khung a) ---
bx = W * 0.66
beam = Image.new('RGBA', (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(beam)
for i in range(60):
    a = int(70 * (1 - i / 60))
    bd.rectangle([bx - 7 * S + i * 0, H * 0.30 + i * (H * 0.34) / 60, bx + 7 * S, H * 0.30 + (i + 1) * (H * 0.34) / 60 + 1], fill=(255, 190, 60, a))
beam = beam.filter(ImageFilter.GaussianBlur(3 * S))
ov = Image.alpha_composite(ov, beam)
d = ImageDraw.Draw(ov)
d.polygon([(bx, H * 0.235), (bx - 11 * S, H * 0.285), (bx + 11 * S, H * 0.285)], fill=GOLD)

# --- HUD trái trên: Xu + hộ chiếu ---
panel(10 * S, 10 * S, 252 * S, 40 * S)
d.text((22 * S, 20 * S), 'Xu 250  ·  Dấu hộ chiếu 3/9', font=font(15), fill=CREAM)

# --- Panel nhiệm vụ phải trên ---
panel(W - 344 * S, 10 * S, 334 * S, 74 * S)
d.text((W - 330 * S, 18 * S), 'HÀNH TRÌNH ĐI CHỢ — Chặng 1/5', font=font(14), fill=GOLD)
d.text((W - 330 * S, 40 * S), 'Đi dọc đường vào tới vòng xoay', font=font(12.5, bold=False), fill=CREAM)
d.rounded_rectangle([W - 330 * S, 62 * S, W - 24 * S, 70 * S], radius=4 * S, outline=BRASS, width=1)
d.rounded_rectangle([W - 330 * S, 62 * S, W - 330 * S + 306 * S * 0.35, 70 * S], radius=4 * S, fill=GOLD)

# --- Thẻ khu vực giữa khung ---
t = 'ĐƯỜNG VÀO CHỢ'
f = font(44)
tw = d.textlength(t, font=f)
d.text(((W - tw) / 2 + 2, H * 0.16 + 2), t, font=f, fill=(0, 0, 0, 160))
d.text(((W - tw) / 2, H * 0.16), t, font=f, fill=(255, 240, 200, 235))

# --- Popup +Xu bay ---
d.text((W * 0.60, H * 0.52), '+30 Xu', font=font(22), fill=GOLD)

# --- Minimap phải dưới ---
mx, my, ms = W - 166 * S, H - 176 * S, 156 * S
panel(mx, my, ms, ms, r=12)
cx, cy = mx + ms / 2, my + ms / 2
d.rectangle([mx + 12 * S, cy - 4 * S, mx + 62 * S, cy + 4 * S], fill=(120, 100, 80, 255))        # đường vào
d.ellipse([mx + 58 * S, cy - 15 * S, mx + 84 * S, cy + 11 * S], outline=BRASS, width=max(1, int(2 * S)))  # vòng xoay
d.rectangle([mx + 88 * S, cy - 20 * S, mx + 142 * S, cy + 16 * S], fill=(112, 82, 52, 255))          # nhà lồng
d.rectangle([mx + 88 * S, cy - 58 * S, mx + 142 * S, cy - 28 * S], fill=(88, 106, 72, 255))          # đồi
d.ellipse([mx + 66 * S, cy - 10 * S, mx + 76 * S, cy], fill=GOLD)                                   # mục tiêu
d.ellipse([mx + 16 * S, cy - 5 * S, mx + 26 * S, cy + 5 * S], fill=(255, 255, 255, 255))            # người chơi

img = Image.alpha_composite(img.convert('RGBA'), ov)
d = ImageDraw.Draw(img)
d.rectangle([0, H - 22 * S, W, H], fill=(20, 12, 6, 235))
d.text((10 * S, H - 19 * S), 'MÔ PHỎNG UI trên render — UI thật chạy trong index.html (DOM/canvas)', font=font(12, bold=False), fill=CREAM)
img.convert('RGB').save(DST)
print('saved', DST, img.size)
