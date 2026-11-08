# -*- coding: utf-8 -*-
"""V4.9 MỤC 7: sinh texture PNG cho harness cận cảnh (gương layout biển web):
biển sạp (gỗ + tên + giá + icon theo sạp), thẻ giá, banner rạp, nền lát đá, sàn kim cương, biển quầy.
Chạy: python3 scripts/gen_m7_assets.py  -> renders/m7/*.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "renders", "m7")
os.makedirs(OUT, exist_ok=True)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(px):
    return ImageFont.truetype(FONT, px)

CREAM = (240, 234, 216)
GOLD = (216, 177, 60)
RED = (216, 74, 53)
GREEN = (127, 174, 90)

def icon(d, kind, cx, cy):
    """Icon đơn giản theo họ sạp, vẽ quanh (cx, cy), cỡ ~90px — bám lựa chọn icon của web."""
    if kind == "phin":
        d.rectangle([cx - 26, cy - 40, cx + 26, cy - 30], fill=CREAM)
        d.polygon([(cx - 22, cy - 30), (cx + 22, cy - 30), (cx + 14, cy), (cx - 14, cy)], fill=CREAM)
        d.ellipse([cx - 5, cy + 9, cx + 5, cy + 19], fill=GOLD)
        d.line([(cx - 19, cy + 32), (cx + 19, cy + 32), (cx + 14, cy + 50), (cx - 14, cy + 50), (cx - 19, cy + 32)], fill=CREAM, width=6)
    elif kind == "cake":
        d.ellipse([cx - 33, cy - 33, cx + 33, cy + 33], fill=(232, 200, 138))
        for i in range(5):
            x = cx - 15 + (i % 3) * 15; y = cy - 8 + (i // 3) * 19
            d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED)
        d.line([(cx - 40, cy + 42), (cx + 40, cy + 42)], fill=CREAM, width=6)
    elif kind == "mold":
        for i in range(3):
            x = cx - 26 + i * 26
            d.ellipse([x - 12, cy, x + 12, cy + 24], fill=(138, 90, 58))
            d.ellipse([x - 7, cy + 3, x + 7, cy + 17], fill=(240, 208, 144))
        d.rectangle([cx - 42, cy + 30, cx + 42, cy + 38], fill=CREAM)
    elif kind == "berry":
        d.polygon([(cx, cy + 48), (cx - 30, cy + 8), (cx - 22, cy - 20), (cx, cy - 20), (cx + 22, cy - 20), (cx + 30, cy + 8)], fill=RED)
        d.rectangle([cx - 17, cy - 32, cx + 17, cy - 22], fill=GREEN)
        d.rectangle([cx - 4, cy - 41, cx + 4, cy - 30], fill=GREEN)
    elif kind == "flower":
        for (dx, dy) in [(-14, 4), (0, 0), (14, 4)]:
            d.line([(cx, cy + 50), (cx + dx, cy + 6)], fill=GREEN, width=6)
        for (dx, dy, c) in [(-16, -10, RED), (0, -20, (232, 138, 192)), (16, -10, GOLD)]:
            d.ellipse([cx + dx - 11, cy + dy - 11, cx + dx + 11, cy + dy + 11], fill=c)
    elif kind == "wool":
        d.ellipse([cx - 33, cy - 21, cx + 25, cy + 37], fill=(201, 93, 126))
        d.arc([cx - 24, cy - 12, cx + 16, cy + 28], 20, 160, fill=(110, 35, 60), width=4)
        d.line([(cx + 8, cy - 34), (cx + 30, cy + 16)], fill=CREAM, width=5)
        d.line([(cx + 26, cy - 30), (cx + 16, cy + 20)], fill=CREAM, width=5)
    elif kind == "gift":
        d.rectangle([cx - 30, cy - 12, cx + 30, cy + 34], fill=GOLD)
        d.rectangle([cx - 34, cy - 22, cx + 34, cy - 9], fill=RED)
        d.rectangle([cx - 5, cy - 22, cx + 5, cy + 34], fill=RED)
    elif kind == "cup":
        d.rectangle([cx - 21, cy - 8, cx + 21, cy + 44], fill=CREAM)
        d.rectangle([cx - 21, cy - 8, cx + 21, cy + 3], fill=GOLD)
    elif kind == "bowl":
        d.pieslice([cx - 32, cy - 30, cx + 32, cy + 34], 15, 165, fill=CREAM)
        d.rectangle([cx - 36, cy - 4, cx + 36, cy + 3], fill=CREAM)
    elif kind == "carrot":
        d.polygon([(cx - 15, cy - 8), (cx + 15, cy - 8), (cx, cy + 46)], fill=(224, 123, 42))
        for dx in (-12, 0, 12):
            d.line([(cx, cy - 8), (cx + dx, cy - 32)], fill=GREEN, width=6)
    elif kind == "potato":
        d.ellipse([cx - 30, cy - 12, cx + 30, cy + 30], fill=(168, 100, 46))
        d.ellipse([cx - 15, cy - 4, cx + 19, cy + 16], fill=(232, 163, 76))
    else:  # leaf mặc định
        d.ellipse([cx - 26, cy - 22, cx + 26, cy + 10], fill=GREEN)
        d.ellipse([cx - 9, cy + 7, cx + 21, cy + 37], fill=RED)

SIGNS = [
    ("banhtrang", "BÁNH TRÁNG NƯỚNG", 20, "cake"),
    ("khoai", "KHOAI & BẮP NƯỚNG", 12, "potato"),
    ("banhcan", "BÁNH CĂN", 22, "mold"),
    ("supcua", "SÚP CUA & CHÈ NÓNG", 20, "bowl"),
    ("sua", "SỮA ĐẬU NÀNH", 15, "cup"),
    ("caphe", "CÀ PHÊ PHIN", 18, "phin"),
    ("yaourt", "YAOURT & SINH TỐ", 14, "cup"),
    ("hoa", "HOA TƯƠI ĐÀ LẠT", 40, "flower"),
    ("banhuot", "BÁNH ƯỚT LÒNG GÀ", 25, "bowl"),
    ("suatuoi", "SỮA TƯƠI & ĐẬU HŨ", 14, "cup"),
    ("dau", "DÂU TÂY & KEM BƠ", 22, "berry"),
    ("len1", "LEN BÀ BẢY", 60, "wool"),
    ("rau", "RAU CỦ ĐÀ LẠT", 45, "carrot"),
    ("dacsan", "ĐẶC SẢN MỨT & HỒNG", 45, "gift"),
]

def sign_png(sid, name, price, kind):
    im = Image.new("RGB", (1024, 256), (107, 68, 35))
    d = ImageDraw.Draw(im)
    planks = [(107, 68, 35), (117, 80, 44), (101, 66, 34), (112, 72, 40)]
    for i in range(4):
        d.rectangle([0, i * 64, 1024, i * 64 + 64], fill=planks[i])
        if i:
            d.rectangle([0, i * 64 - 2, 1024, i * 64 + 2], fill=(0, 0, 0))
    d.rectangle([12, 12, 1012, 244], outline=(201, 168, 106), width=6)
    size = 88
    while size > 30:
        f = font(size)
        if d.textlength(name, font=f) <= 700:
            break
        size -= 6
    d.text((512, 86), name, font=font(size), fill=(255, 233, 176), anchor="mm")
    d.text((512, 190), "— %dK —" % price, font=font(62), fill=(255, 217, 77), anchor="mm")
    icon(d, kind, 100, 158)
    icon(d, kind, 924, 158)
    im.save(os.path.join(OUT, "sign-%s.png" % sid))

def card_png(sid, price):
    im = Image.new("RGB", (256, 160), (243, 227, 194))
    d = ImageDraw.Draw(im)
    d.rectangle([8, 8, 248, 152], outline=(176, 32, 32), width=10)
    d.text((128, 84), "%dK" % price, font=font(84), fill=(176, 32, 32), anchor="mm")
    im.save(os.path.join(OUT, "card-%s.png" % sid))

def banner_png(fname, text, bg):
    im = Image.new("RGB", (192, 640), bg)
    d = ImageDraw.Draw(im)
    d.rectangle([10, 10, 182, 630], outline=(232, 200, 126), width=6)
    f = font(74)
    for i, ch in enumerate(text):
        d.text((96, 78 + i * 82), ch, font=f, fill=(255, 217, 138), anchor="mm")
    im.save(os.path.join(OUT, fname))

def stone_png():
    import random
    random.seed(7)
    im = Image.new("RGB", (512, 512), (87, 80, 74))
    d = ImageDraw.Draw(im)
    tints = [(141, 133, 123), (148, 139, 127), (133, 125, 114), (138, 129, 119)]
    for ty in range(2):
        for tx in range(2):
            d.rectangle([tx * 256 + 5, ty * 256 + 5, tx * 256 + 251, ty * 256 + 251], fill=tints[(tx + ty * 2) % 4])
            d.rectangle([tx * 256 + 5, ty * 256 + 5, tx * 256 + 251, ty * 256 + 35], fill=(255, 255, 255))
    ov = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    od.rectangle([5, 5, 251, 35], fill=(255, 255, 255, 13))
    od.rectangle([261, 5, 507, 35], fill=(255, 255, 255, 13))
    od.rectangle([5, 261, 251, 291], fill=(255, 255, 255, 13))
    od.rectangle([261, 261, 507, 291], fill=(255, 255, 255, 13))
    for _ in range(2600):
        c = (255, 250, 240, 18) if random.random() > 0.5 else (20, 16, 12, 18)
        x, y = random.random() * 512, random.random() * 512
        od.rectangle([x, y, x + 2.2, y + 2.2], fill=c)
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    im.save(os.path.join(OUT, "stone.png"))

def diamond_png():
    im = Image.new("RGB", (256, 256), (122, 114, 104))
    d = ImageDraw.Draw(im)
    for ry in range(4):
        for rx in range(4):
            cx, cy = rx * 64 + 32, ry * 64 + 32
            d.polygon([(cx, cy - 30), (cx + 30, cy), (cx, cy + 30), (cx - 30, cy)], fill=(141, 132, 120))
    im.save(os.path.join(OUT, "diamond.png"))

def quay_png(n, cat):
    im = Image.new("RGB", (512, 128), (243, 227, 194))
    d = ImageDraw.Draw(im)
    d.text((256, 44), "QUẦY SỐ %d" % n, font=font(52), fill=(176, 32, 32), anchor="mm")
    d.text((256, 98), cat, font=font(34), fill=(90, 60, 40), anchor="mm")
    im.save(os.path.join(OUT, "quay-%d.png" % n))

def board_png(fname, title, lines):
    im = Image.new("RGB", (256, 320), (46, 42, 38))
    d = ImageDraw.Draw(im)
    d.rectangle([6, 6, 250, 314], outline=(201, 168, 106), width=8)
    d.text((128, 58), title, font=font(40), fill=(255, 217, 77), anchor="mm")
    for i, ln in enumerate(lines):
        d.text((128, 118 + i * 44), ln, font=font(27), fill=(240, 234, 216), anchor="mm")
    im.save(os.path.join(OUT, fname))

def mural_png():
    im = Image.new("RGB", (512, 320), (232, 220, 192))
    d = ImageDraw.Draw(im)
    for i in range(4):
        d.ellipse([60 + i * 26, 166 - i * 8, 120 + i * 26, 254 - i * 8], fill=(127, 174, 90))
    for i in range(3):
        d.ellipse([77 + i * 30, 166 - i * 10, 115 + i * 30, 226 - i * 10], fill=(77, 115, 64))
    d.polygon([(400, 250), (436, 130), (472, 250)], fill=(51, 80, 46))
    d.text((300, 108), "ATISÔ", font=font(64), fill=(176, 58, 48), anchor="mm")
    d.text((300, 178), "ĐÀ LẠT", font=font(64), fill=(176, 58, 48), anchor="mm")
    d.text((256, 282), "ĐẶC SẢN CAO NGUYÊN", font=font(30), fill=(106, 81, 54), anchor="mm")
    im.save(os.path.join(OUT, "mural-atiso.png"))

for (sid, name, price, kind) in SIGNS:
    sign_png(sid, name, price, kind)
    card_png(sid, price)
board_png("board-hoa.png", "HOA ĐÀ LẠT", ["Cẩm tú cầu", "Hồng · Baby", "Lavender"])
board_png("board-nuong.png", "ĐỒ NƯỚNG", ["Bắp nướng", "Khoai lang", "Xiên que"])
mural_png()
banner_png("banner-rap.png", "RẠPHÒA", (122, 31, 26))
banner_png("banner-phim.png", "PHIMHAY", (39, 74, 99))
stone_png()
diamond_png()
for n, cat in [(3, "RAU CỦ"), (7, "TRÁI CÂY"), (11, "HOA TƯƠI"), (15, "ĐỒ KHÔ")]:
    quay_png(n, cat)
print("M7 ASSETS DONE ->", OUT)
