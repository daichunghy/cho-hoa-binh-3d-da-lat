# -*- coding: utf-8 -*-
# Ghép r25-doi-chieu-v55.png: ảnh thật | khung chơi V5.4 (image-59) | render V5.5 khung mở đầu ngày.
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.join(os.path.dirname(__file__), '..')
REAL = os.path.normpath(os.path.join(BASE, '..', 'theme', 'real-market', '40-duong-ntmk-dem-sap-hai-ben.jpg'))
OLD = os.path.expanduser('~/workspace/user/media_library/image/image-59.png')
NEW = os.path.join(BASE, 'renders', 'v55-K-mo-dau-ngay-draft.png')
OUT = os.path.join(BASE, 'renders', 'r25-doi-chieu-v55.png')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

PW, PH = 620, 465          # kích thước mỗi panel
BAR = 44                    # thanh nhãn trên mỗi panel
GAP = 10
BG = (24, 18, 9)

def cover(img, w, h):
    """resize + crop giữa cho vừa khung w×h (giữ tỉ lệ)."""
    iw, ih = img.size
    sc = max(w / iw, h / ih)
    img = img.resize((round(iw * sc), round(ih * sc)), Image.LANCZOS)
    x = (img.size[0] - w) // 2; y = (img.size[1] - h) // 2
    return img.crop((x, y, x + w, y + h))

old = Image.open(OLD).convert('RGB')
ow, oh = old.size
old = old.crop((int(ow * 0.06), int(oh * 0.235), int(ow * 0.96), int(oh * 0.965)))  # bỏ phần lớn UI, giữ khung 3D

panels = [
    ('1 · ẢNH THẬT: đường vào chợ đêm Đà Lạt', cover(Image.open(REAL).convert('RGB'), PW, PH)),
    ('2 · V5.4: ảnh chơi thật ban ngày (cháy trắng)', cover(old, PW, PH)),
    ('3 · V5.5: khung mở đầu mới — render đối chiếu', cover(Image.open(NEW).convert('RGB'), PW, PH)),
]
W = PW * 3 + GAP * 4
H = PH + BAR + GAP * 2
canvas = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(canvas)
f = ImageFont.truetype(FONT, 19)
for i, (label, im) in enumerate(panels):
    x = GAP + i * (PW + GAP)
    canvas.paste(im, (x, GAP + BAR))
    tw = d.textlength(label, font=f)
    d.text((x + (PW - tw) / 2, GAP + 10), label, font=f, fill=(255, 196, 107))
canvas.save(OUT)
print('saved', OUT, canvas.size)
