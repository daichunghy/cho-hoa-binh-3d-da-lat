#!/usr/bin/env python3
"""Sample real colors from theme/real-market photos for research/22 (SOUND-COLOR-1).
Per photo: overall 4 dominant colors (simple k-means on downscaled pixels),
plus mean color of top third (sky/lights) and bottom third (ground/asphalt).
Output: hex codes ready for the palette table."""
import os, sys
import numpy as np
from PIL import Image

BASE = os.path.expanduser('~/workspace/cho-hoa-binh-3d/theme/real-market')
PHOTOS = sys.argv[1:] or [
    '40-duong-ntmk-dem-sap-hai-ben.jpg',
    '30-dam-dong-dem-ao-phao.jpg',
    '04-bung-binh-dem-tren-cao.jpg',
    '14-banh-trang-nuong-can-canh.jpg',
    '31-sap-xien-nuong-can-canh.jpg',
    '08-bac-thang-dem-ngoi-an.jpg',
    '43-cho-dem-quan-ao.jpg',
    '41-sua-dau-nanh-hoa-sua.jpg',
    '28-bung-binh-dem-mat-dat-xe-nguoi.jpg',
    '07-duong-cho-ngay-tren-cao.jpg',
    '06-duong-cho-dem-tren-cao.jpg',
    '32-tuong-dai-roi-sang-dem-nguoi-cam-ly.jpg',
]

def hx(rgb):
    return '#%02x%02x%02x' % tuple(int(round(c)) for c in rgb)

def kmeans(px, k=4, iters=12, seed=7):
    rng = np.random.default_rng(seed)
    idx = rng.choice(len(px), k, replace=False)
    c = px[idx].astype(np.float64)
    for _ in range(iters):
        d = ((px[:, None, :] - c[None, :, :]) ** 2).sum(axis=2)
        lab = d.argmin(axis=1)
        for j in range(k):
            if (lab == j).any():
                c[j] = px[lab == j].mean(axis=0)
    counts = np.bincount(lab, minlength=k)
    order = np.argsort(-counts)
    return [(c[j], counts[j] / len(px)) for j in order]

for name in PHOTOS:
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        print(f'{name}: KHONG CO FILE'); continue
    im = Image.open(p).convert('RGB')
    w, h = im.size
    small = im.resize((120, int(120 * h / w)))
    px = np.asarray(small, dtype=np.float64).reshape(-1, 3)
    dom = kmeans(px, 4)
    top = np.asarray(im.crop((0, 0, w, h // 3)).resize((60, 20)), dtype=np.float64).reshape(-1, 3).mean(axis=0)
    bot = np.asarray(im.crop((0, 2 * h // 3, w, h)).resize((60, 20)), dtype=np.float64).reshape(-1, 3).mean(axis=0)
    mid = np.asarray(im.crop((0, h // 3, w, 2 * h // 3)).resize((60, 20)), dtype=np.float64).reshape(-1, 3).mean(axis=0)
    print(f'\n{name} ({w}x{h})')
    print('  dominant:', ', '.join(f'{hx(c)} {s*100:.0f}%' for c, s in dom))
    print(f'  top(1/3)={hx(top)}  mid={hx(mid)}  bottom(1/3)={hx(bot)}')
