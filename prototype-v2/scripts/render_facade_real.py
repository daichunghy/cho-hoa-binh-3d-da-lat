# -*- coding: utf-8 -*-
"""V8 — RENDER NGHIỆM THU MẶT TIỀN BẰNG MODEL THẬT (sửa sai nghiệm thu V7-2).

LÝ DO: ảnh ghép renders/v7-2-cmp-r1.png của V7-IMPROVE-2 dùng harness mini
(render_real1.py) — nhà lồng là KHỐI HỘP TRƠN, tượng là TRỤ + QUẢ CẦU, không
texture/chữ — Chung Hy chấm 01:27 10/11: "nhìn không ra luôn, có giống đâu".
Verdict "r1 đạt khung" bị rút lại. Script này dựng lại góc mặt tiền bằng
CHÍNH CÁC GLB THẬT trong assets/, đặt đúng tọa độ/quay/scale mà index.html
dùng khi nạp, để đối chiếu với ảnh thật theme/real-market/01-mat-tien-cho-ngay.jpg.

VỊ TRÍ LẤY TỪ index.html (đọc trực tiếp, không đoán):
- market.glb:     mk.position.set(0, 0, 20), không quay, scale 1
  (mặt tiền GLB ở local z=-8: SignLetters y 14.2..16.2, LouverWhite, ZigWhite;
  -> mặt tiền thế giới z = 20-8 = 12, khớp marketFrontZ = 12 trong code).
- roundabout.glb: rb.position.set(-30, 0, -6), không quay, scale 1
  (tượng trong GLB: StatueBase tâm local (-4.2, +3.2), Statue cao tới y 9.6
  -> tượng thế giới (-34.2, -2.8), khớp điểm ngắm spotlight trong code).
- stairs.glb:     st.position.set(-56, 0, -16), không quay, scale 1. (LAYOUT-FIX-1: truoc 10/11 dat (0,0,-16) o tam)
- pine.glb:       pine(-22.5, -16.8, 1.15) cạnh bùng binh (y = groundH ~ 0);
  rotY theo công thức code (x*7+z*13) % 3.14 (JS remainder) = -2.24 rad.
KHÔNG nạp: lamp/bridge/hotels/shop (ngoài khung hình mặt tiền này), nhân vật,
sạp, và toàn bộ chi tiết dựng bằng code (biển, đài phun, hàng rào...) — render
này chỉ chấm MODEL + BỐ CỤC KHỐI THẬT. Mặt đất là 1 plane xám trung tính làm
nền ngữ cảnh, KHÔNG phải hình học game.

ÁNH SÁNG/PHỐI MÀU THEO WEB (chỉ 2 chỉnh có ghi trong code):
- Vật liệu SignLetters của market: code ép màu 0xc8372d (clampSat) -> áp.
- WallCream/ColumnCream của market: code ghi đè 0xe3d7bd (mặt tiền ngà kem,
  ghi chú V5.5 tránh cháy trắng) -> áp.
Chưa tái tạo: clamp bão hòa toàn cục của web, texture bẩn facade (canvas
TEX_GRIME), sương/khói — ghi nhận là khác biệt còn lại khi chấm.

CAMERA (quy ước trục three (x, y-up, z) -> Blender (x, -z, y);
game rotY -> Blender rotation_z = +rotY):
- Đứng phía tây-nam đảo trên mặt đường: three (-62, 4.5, -20),
  ngắm tâm mặt tiền three (4, 8, 12) — tương ứng hướng chụp của ảnh 01
  (từ bùng binh nhìn thẳng mặt tiền, tượng tiền cảnh, đảo dưới chân).
  (Lượt đầu đặt (-54, 3, -13) -> (2, 8, 12): mặt tiền bị cắt góc trên-phải,
  tượng choán giữa khung — đã lùi camera + nâng nhẹ cho trọn khối nhà.)
- Lens 32mm, khung 900x600 (khớp tỉ lệ 3:2 của ảnh thật 1400x933).
GHI CHÚ BỐ CỤC (đo bằng hình học trước khi render): tượng nằm ở góc tây,
sát phía chợ của đảo; từ mọi điểm đứng phía nam/tây-nam nhìn về mặt tiền,
tượng rơi GIỮA tới PHẢI khung — không tái tạo được "tượng tiền cảnh trái"
như ảnh thật nếu không dời tượng (vị trí tượng đã khóa từ GEOMETRY-2).
Đây là lệch vị trí thật của game, ghi vào verdict chứ không né.

Chạy: ~/workspace/vinh-trang-3d/tools/blender5/blender --background \
        --threads 2 --python scripts/render_facade_real.py
Cycles 32 mẫu, 900x600, threads 2 (RAM máy chật — không bật denoise).
Xuất: renders/v8-facade-real.png
"""
import bpy, math, os
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)

# ---------- don sach scene ----------
bpy.ops.wm.read_factory_settings(use_empty=True)

def three_to_blender(p):
    return Vector((p[0], -p[2], p[1]))

def import_asset(name, three_pos, scale=1.0, rot_y=0.0):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name + ".glb"))
    new = [o for o in bpy.data.objects if o not in before]
    roots = [o for o in new if o.parent is None or o.parent in before]
    off = three_to_blender(three_pos)
    for o in roots:
        if abs(rot_y) > 1e-9:
            # quay quanh truc dung tai diem dat asset: T(off) * Rz(rotY) * T(-off) * M
            m = (Matrix.Translation(off)
                 @ Matrix.Rotation(rot_y, 4, 'Z')
                 @ Matrix.Translation(-off)
                 @ o.matrix_world)
            o.matrix_world = m
        o.location = o.location + off
        if scale != 1.0:
            o.scale = o.scale * scale
    print(f"[v8] {name}: {len(new)} objects, dat tai three={three_pos} scale={scale} rotY={rot_y}")
    return new

# ---------- tai model that theo dung vi tri index.html ----------
market_objs = import_asset('market', (0, 0, 20))
import_asset('roundabout', (-30, 0, -6))
import_asset('stairs', (-56, 0, -16))  # LAYOUT-FIX-1: thang doi ve hong tay (index.html: st.position.set(-56, 0, -16))
import_asset('pine', (-22.5, 0, -16.8), scale=1.15, rot_y=math.fmod(-22.5 * 7 + -16.8 * 13, 3.14))

# ---------- mau hieu dung theo code web (chi tren market) ----------
# FACADE-COLOR-1 (11/11): ap BANG MAU HIEU DUNG DAY DU cua web cho market —
# clampSat(0.15, 0.45, warmGray) + ghi de WallCream/ColumnCream 0xeae3d5,
# MarketWin 0x3a4c5e, bang FACADE_HEX (Peach/PeachDk/LouverWhite/ZigBack/
# TrimBrown) + SignLetters ep 0xbf3b47. Bang duoi tai tao bang three r160
# chay dung pipeline index.html (scripts/_fc1_tmp.mjs luc do, da xoa).
# set_base_color PHAI chuyen sRGB -> linear (three.js ColorManagement lam
# tuong tu) — ban V8 cu dat thang so sRGB vao o linear nen render rua sang.
EFF_MARKET = {
    'AdGreen': '#95cb95', 'AdLED': '#c88181', 'AdWhite': '#f6f3ec',
    'AdYellow': '#e3d5a9', 'ColumnCream': '#eae3d5', 'Concrete': '#d1cbbd',
    'ConcreteDk': '#b8aea0', 'ElevGlass': '#a0ceb3', 'Glass': '#bcd3d7',
    'GlassDark': '#647073', 'GoodsA': '#ddb68f', 'GoodsB': '#ce8f85',
    'GoodsC': '#e6d8b4', 'LouverWhite': '#e8eae9', 'MarketWin': '#3a4c5e',
    'MetalDark': '#877e75', 'Peach': '#ecbfa7', 'PeachDk': '#d8b198',
    'PineDark': '#81aa81', 'SignLetters': '#bf3b47', 'StatueWhite': '#f7f6f1',
    'Stone': '#c8beaf', 'StripeA': '#83afcb', 'StripeB': '#fafaf8',
    'TerraceMat': '#e2dacb', 'TrimBrown': '#d3a78b', 'Trunk': '#99866f',
    'WallCream': '#eae3d5', 'WhiteConc': '#f3f2ed', 'Wood': '#c4a681',
    'WoodDark': '#a68b6f', 'ZigBack': '#b3b9bf', 'ZigWhite': '#faf8f2',
}

def _srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def set_base_color(mat, hexcol):
    r, g, b = (int(hexcol[i:i + 2], 16) / 255.0 for i in (1, 3, 5))
    r, g, b = _srgb_to_linear(r), _srgb_to_linear(g), _srgb_to_linear(b)
    for node in mat.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            node.inputs['Base Color'].default_value = (r, g, b, 1.0)
    mat.diffuse_color = (r, g, b, 1.0)

seen_mats = set()
for o in market_objs:
    if o.type != 'MESH':
        continue
    for slot in o.material_slots:
        m = slot.material
        if not m or m.name in seen_mats:
            continue
        seen_mats.add(m.name)
        base = m.name.split('.')[0]
        if base in EFF_MARKET:
            set_base_color(m, EFF_MARKET[base])
            print(f"[fc1] mat {m.name} -> {EFF_MARKET[base]} (hieu dung web)")

# ---------- mat dat trung tinh (chi lam nen ngu canh) ----------
bpy.ops.mesh.primitive_plane_add(size=500, location=(0, 0, 0))
ground = bpy.context.active_object
ground.name = 'NeutralGround'
gm = bpy.data.materials.new('NeutralAsphalt')
gm.use_nodes = True
gm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.16, 0.16, 0.17, 1.0)
gm.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 1.0
ground.data.materials.append(gm)

# ---------- anh sang ngay: nang + bau troi ----------
world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes['Background']
bg.inputs[0].default_value = (0.55, 0.70, 0.95, 1.0)  # troi xanh nhat nhu anh that
bg.inputs[1].default_value = 0.85

sun_data = bpy.data.lights.new('Sun', 'SUN')
sun_data.energy = 3.2
sun_data.angle = math.radians(2.0)
sun = bpy.data.objects.new('Sun', sun_data)
bpy.context.scene.collection.objects.link(sun)
# nang tu phia tay-nam tren cao (bong do ve dong-nam nhu anh 01):
# huong chieu tu vi tri (-60, 55, 80) nhin ve goc toa do (Blender)
sun.location = (-60, 55, 80)
d = (Vector((0, 0, 0)) - sun.location).normalized()
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

# ---------- camera ----------
cam_data = bpy.data.cameras.new('Cam')
cam_data.lens = 32.0
cam_data.clip_start = 0.1
cam_data.clip_end = 600
cam = bpy.data.objects.new('Cam', cam_data)
bpy.context.scene.collection.objects.link(cam)
# FACADE-COLOR-1: camera V8 goc (-62, 4.5, -20) nay nam TRONG khoi thang moi
# (LAYOUT-FIX-1 doi thang ve (-56,0,-16): bbox x -67..-45, z -30..-2) -> render
# DEN HOAN TOAN. Lui ve phia tay-nam ngoai khoi thang: three (-41, 6.5, -48),
# ngam (5, 9, 12) — khoang cach mat tien ~75u nhu goc V8 cu, tuong vao khung.
cam.location = three_to_blender((-41, 6.5, -48))
target = three_to_blender((5, 9, 12))
d = (target - cam.location).normalized()
cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
bpy.context.scene.camera = cam
print(f"[v8] camera Blender loc={tuple(round(v,1) for v in cam.location)} -> target={tuple(round(v,1) for v in target)}")

# ---------- thong ke tuong de bao cao ----------
for o in bpy.data.objects:
    if o.name.startswith('Statue') and o.type == 'MESH':
        bb = [o.matrix_world @ Vector(c) for c in o.bound_box]
        xs = [v.x for v in bb]; ys = [v.y for v in bb]; zs = [v.z for v in bb]
        print(f"[v8] {o.name}: Blender bbox x[{min(xs):.1f},{max(xs):.1f}] y[{min(ys):.1f},{max(ys):.1f}] z[{min(zs):.1f},{max(zs):.1f}] verts={len(o.data.vertices)}")

# ---------- render ----------
scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 32
scene.cycles.use_denoising = False
# so thread do co CLI --threads 2 chi dinh (Blender 5.0 bo thuoc tinh thread rieng)
scene.render.resolution_x = 900
scene.render.resolution_y = 600
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = os.path.join(OUT, os.environ.get('FC_OUT', 'v8-facade-real.png'))
bpy.ops.render.render(write_still=True)
print("[v8] DA RENDER XONG ->", scene.render.filepath)
