# -*- coding: utf-8 -*-
"""HB-SQUARE-1 — RENDER NGHIỆM THU (harness MÔ PHỎNG theo thông số code
index.html SAU vòng HB-SQUARE-1; KHÔNG phải screenshot game).

Dựng bằng GLB THẬT (roundabout.glb tại (-30,0,-6), market.glb tại (0,0,20)
— đúng vị trí code) + áp thay đổi của vòng:
- roundabout traverse HB-SQUARE-1: LeafGreen #3c5131 / PineMid #455833 /
  Flower0+Flower2 #d02e2d (PIL ảnh 44); các material còn lại giữ GLB.
- Sân quảng trường: lát đá canvas pzC của code (grout #716a60 + ô #8c8374
  jitter, PIL tái tạo tại /tmp/hbsq1_paving.png) thay hộp phẳng 0xa79a84;
  hình học giữ nguyên (64x14.2 tâm (14,4.8) mặt trên y 0.05).
- Đài phun code-built đúng thông số V5.5/WATER-1: bồn đá 0x8a8074, nước
  teal 0x276a8a (idiom riêng đài phun), vành/ghế 0xd8d2c2, tia trắng.
- Góc Hát (31,17,-52): sân khấu + loa kéo MỚI (26.7,-50.1) + bảng bài hát
  MỚI (35.7,-49.1, vẽ phẳng không chữ — game là canvas có chữ) + 2 ghế
  nhựa MỚI (xanh 0x2456a6 tại (27.4,-47.8), đỏ 0xc22e22 tại (34.2,-48.2)).
Nhân vật character.glb làm thước (đứng, không pose ngồi).

3 shot (Cycles 48 mẫu, threads 2, OIDN, AgX; chạng vạng ấm ~19:00):
 A hbsquare-plaza.png    — từ trước chợ (2,3.2,22) nhìn ra sân -> đài phun:
    lát đá mới + đài phun + đảo phía xa trái.
 B hbsquare-fountain.png — cận đài phun (21.5,1.7,11.5) -> (27,1.8,5.2).
 C hbsquare-stage.png    — Góc Hát (28.5,18.6,-43.5) -> (31.5,18.2,-51.5).
Chạy: ~/workspace/vinh-trang-3d/tools/blender5/blender --background \
      --threads 2 --python /tmp/render_hbsquare1.py
"""
import bpy, math, os
from mathutils import Vector

import os.path as _osp
ROOT = _osp.abspath(_osp.join(_osp.dirname(_osp.abspath(__file__)), '..'))
ASSETS = os.path.join(ROOT, 'assets')
OUT = os.path.join(ROOT, 'renders')
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

def T2B(p):
    return Vector((p[0], -p[2], p[1]))

def import_asset(name, three_pos):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name + '.glb'))
    new = [o for o in bpy.data.objects if o not in before]
    roots = [o for o in new if o.parent is None or o.parent in before]
    off = T2B(three_pos)
    for o in roots:
        o.location = o.location + off
    print(f"[hbsq1] {name}: {len(new)} objects @ three={three_pos}")
    return new

def _s2l(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def set_base_color(mat, hexcol):
    r, g, b = (int(hexcol[i:i + 2], 16) / 255.0 for i in (1, 3, 5))
    r, g, b = _s2l(r), _s2l(g), _s2l(b)
    for node in mat.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            node.inputs['Base Color'].default_value = (r, g, b, 1.0)
    mat.diffuse_color = (r, g, b, 1.0)

def apply_table(objs, table):
    seen = set()
    for o in objs:
        if o.type != 'MESH':
            continue
        for slot in o.material_slots:
            m = slot.material
            if not m or m.name in seen:
                continue
            seen.add(m.name)
            base = m.name.split('.')[0]
            if base in table:
                set_base_color(m, table[base])

# ---------- GLB that ----------
rb_objs = import_asset('roundabout', (-30, 0, -6))
apply_table(rb_objs, {  # HB-SQUARE-1 traverse (PIL anh 44)
    'LeafGreen': '#3c5131', 'PineMid': '#455833',
    'Flower0': '#d02e2d', 'Flower2': '#d02e2d',
})
market_objs = import_asset('market', (0, 0, 20))
apply_table(market_objs, {  # bang EFF_MARKET (render_stair1)
    'AdGreen': '#95cb95', 'AdLED': '#c88181', 'AdWhite': '#f6f3ec',
    'AdYellow': '#e3d5a9', 'ColumnCream': '#eae3d5', 'Concrete': '#d1cbbd',
    'ConcreteDk': '#b8aea0', 'ElevGlass': '#a0ceb3', 'Glass': '#bcd3d7',
    'GlassDark': '#647073', 'GoodsA': '#ddb68f', 'GoodsB': '#ce8f85',
    'GoodsC': '#e6d8b4', 'LouverWhite': '#e8eae9', 'MarketWin': '#3a4c5e',
    'MetalDark': '#877e75', 'Peach': '#ecbfa7', 'PeachDk': '#d8b198',
    'PineDark': '#2a3520', 'SignLetters': '#bf3b47', 'StatueWhite': '#f7f6f1',
    'Stone': '#c8beaf', 'StripeA': '#83afcb', 'StripeB': '#fafaf8',
    'TerraceMat': '#e2dacb', 'TrimBrown': '#d3a78b', 'Trunk': '#99866f',
    'WallCream': '#eae3d5', 'WhiteConc': '#f3f2ed', 'Wood': '#c4a681',
    'WoodDark': '#a68b6f', 'ZigBack': '#b3b9bf', 'ZigWhite': '#faf8f2',
})

# ---------- khoi code-built mo phong ----------
_MATS = {}
def M(hexcol, rough=0.9, emis=None, estr=0.0):
    key = (hexcol, emis, estr)
    if key in _MATS:
        return _MATS[key]
    m = bpy.data.materials.new('CB' + str(hexcol))
    m.use_nodes = True
    bs = m.node_tree.nodes['Principled BSDF']
    r, g, b = (int(hexcol[i:i + 2], 16) / 255.0 for i in (1, 3, 5))
    bs.inputs['Base Color'].default_value = (_s2l(r), _s2l(g), _s2l(b), 1.0)
    bs.inputs['Roughness'].default_value = rough
    if emis:
        er, eg, eb = (int(emis[i:i + 2], 16) / 255.0 for i in (1, 3, 5))
        bs.inputs['Emission Color'].default_value = (_s2l(er), _s2l(eg), _s2l(eb), 1.0)
        bs.inputs['Emission Strength'].default_value = estr
    _MATS[key] = m
    return m

def box3(cx, cy, cz, sx, sy, sz, mat):
    bpy.ops.mesh.primitive_cube_add(location=T2B((cx, cy, cz)))
    o = bpy.context.active_object
    o.dimensions = (sx, sz, sy)
    bpy.ops.object.transform_apply(scale=True)
    if mat:
        o.data.materials.append(mat)
    return o

def cyl3(cx, cy, cz, r_bottom, r_top, h, mat, seg=20):
    # cac loi goi truyen (day, dinh) theo three cyl(rt= dinh, rb= day); blender cone radius1=day, radius2=dinh
    bpy.ops.mesh.primitive_cone_add(radius1=r_bottom, radius2=r_top, depth=h,
                                    vertices=seg, location=T2B((cx, cy, cz)))
    o = bpy.context.active_object
    if mat:
        o.data.materials.append(mat)
    return o

def ball3(cx, cy, cz, r, mat):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=T2B((cx, cy, cz)))
    o = bpy.context.active_object
    if mat:
        o.data.materials.append(mat)
    return o

def tex_mat(repX, repY):
    m = bpy.data.materials.new('Paving')
    m.use_nodes = True
    nt = m.node_tree
    bs = nt.nodes['Principled BSDF']
    bs.inputs['Roughness'].default_value = 0.95
    tex = nt.nodes.new('ShaderNodeTexImage')
    tex.image = bpy.data.images.load('/tmp/hbsq1_paving.png')
    tex.extension = 'REPEAT'
    mp = nt.nodes.new('ShaderNodeMapping')
    mp.inputs['Scale'].default_value = (repX, repY, 1.0)
    tc = nt.nodes.new('ShaderNodeTexCoord')
    nt.links.new(tc.outputs['UV'], mp.inputs['Vector'])
    nt.links.new(mp.outputs['Vector'], tex.inputs['Vector'])
    nt.links.new(tex.outputs['Color'], bs.inputs['Base Color'])
    return m

# san quang truong lat da MOI (hinh hoc giu nguyen hop cu)
slab = box3(14, 0.01, 4.8, 64, 0.08, 14.2, None)
slab.data.materials.append(tex_mat(10, 2.2))
box3(-18.0, 0.02, 4.8, 0.7, 0.1, 14.2, M('#6e6257'))          # dai vien tay cu
box3(40.5, 0.01, 20.75, 10, 0.08, 13.5, None).data.materials.append(tex_mat(1.6, 2.1))

# dai phun (27, 5.2) — thong so code V5.5/WATER-1
FNT = (27, 5.2)
cyl3(FNT[0], 0.28, FNT[1], 2.9, 2.7, 0.55, M('#8a8074'), 24)                 # bon (three rt=2.7 rb=2.9)
cyl3(FNT[0], 0.565, FNT[1], 2.72, 2.72, 0.02, M('#d8d2c2'), 28)              # vanh mieng
cyl3(FNT[0], 0.58, FNT[1], 2.45, 2.45, 0.015, M('#276a8a', rough=0.2), 24)   # mat nuoc teal
cyl3(FNT[0], 1.42, FNT[1], 0.44, 0.26, 2.3, M('#8a8074'), 12)                # cot giua
cyl3(FNT[0], 2.62, FNT[1], 0.52, 0.95, 0.25, M('#8a8074'), 14)               # bat chinh
cyl3(FNT[0], 3.12, FNT[1], 0.30, 0.50, 0.18, M('#8a8074'), 12)               # bat tang 2
ball3(FNT[0], 3.34, FNT[1], 0.16, M('#8a8074'))
jetM = M('#eaf6fc', rough=0.3, emis='#cfe8f5', estr=0.35)
for i in range(8):
    a = i / 8 * math.pi * 2
    jx, jz = FNT[0] + math.cos(a) * 0.52, FNT[1] + math.sin(a) * 0.52
    bpy.ops.mesh.primitive_cone_add(radius1=0.036, radius2=0.028, depth=1.55,
                                    vertices=6, location=T2B((jx, 2.95, jz)))
    jo = bpy.context.active_object
    jo.rotation_mode = 'AXIS_ANGLE'
    jo.rotation_axis_angle = (-0.62, math.sin(a), math.cos(a), 0.0)
    jo.data.materials.append(jetM)
cyl3(FNT[0], 3.92, FNT[1], 0.06, 0.04, 1.35, jetM, 8)                        # tia tam
for bx, bz in [(22.2, 5.2), (31.8, 5.2)]:                                    # ghe da canh dai phun
    box3(bx, 0.455, bz, 0.55, 0.09, 2.1, M('#d8d2c2'))
    box3(bx, 0.205, bz - 0.85, 0.5, 0.41, 0.16, M('#6e665a'))
    box3(bx, 0.205, bz + 0.85, 0.5, 0.41, 0.16, M('#6e665a'))
for fx, fz, fc in [(20.5, 9.8, '#c8372d'), (33.5, 9.8, '#d9a62e'), (20.5, 0.8, '#2e6da4'), (33.5, 0.8, '#c8372d')]:
    cyl3(fx, 2.8, fz, 0.06, 0.045, 5.6, M('#555049'), 8)
    box3(fx + 0.3, 4.65, fz, 0.55, 1.45, 0.04, M(fc))
    ball3(fx, 5.65, fz, 0.09, M('#ffd94d', emis='#ffd94d', estr=0.8))

# ---------- Goc Hat (31,17,-52) ----------
SX, SY, SZ = 31, 17, -52
box3(0, 17.02, -54, 120, 0.05, 44, None).data.materials.append(tex_mat(16, 6))  # sq2 lat da doi (ngu canh)
box3(SX, SY + 0.18, SZ, 7.5, 0.35, 4.6, M('#7a5a3a'))                        # san khau
box3(SX, SY + 0.8, SZ - 2.3, 7.5, 0.9, 0.25, M('#4c3428'))                   # phong sau
box3(SX, SY + 2.6, SZ - 2.16, 4.6, 0.8, 0.06, M('#4c3428'))                  # bien GOC HAT (phang, khong chu)
box3(SX - 3.1, SY + 0.78, SZ + 1.4, 0.55, 0.85, 0.45, M('#2c2c30'))          # loa trai
box3(SX + 3.1, SY + 0.78, SZ + 1.4, 0.55, 0.85, 0.45, M('#2c2c30'))          # loa phai
box3(SX, SY + 0.455, SZ + 4.8, 2.1, 0.09, 0.55, M('#d8d2c2'))                 # ghe da truoc san khau
box3(SX - 5.4, SY + 0.22, SZ, 0.45, 0.45, 3.6, M('#6a4a30'))                 # bang ghe go phia tay
box3(SX - 1.5, SY + 0.42, SZ + 1.85, 0.85, 0.14, 0.42, M('#3b2618'))         # hop dan tip
# LOA KEO moi (26.7, -50.1)
box3(SX - 4.3, SY + 0.48, SZ + 1.9, 0.52, 0.72, 0.42, M('#2c2c30'))
box3(SX - 4.3, SY + 0.88, SZ + 1.9, 0.40, 0.08, 0.30, M('#3a3a40'))
box3(SX - 4.52, SY + 0.09, SZ + 1.9, 0.06, 0.18, 0.18, M('#141416'))
box3(SX - 4.08, SY + 0.09, SZ + 1.9, 0.06, 0.18, 0.18, M('#141416'))
# BANG BAI HAT moi (35.7, -49.1) — phang khong chu nhu cac bien harness khac
box3(SX + 4.7, SY + 0.72, SZ + 2.9, 0.08, 1.45, 0.08, M('#4a3b2c'))
bb = box3(SX + 4.7, SY + 1.95, SZ + 2.9, 1.7, 1.0, 0.05, M('#4c3428'))
# LUU Y harness: khong xoay bb sau box3 — origin da bake vao vertices, gan rotation_euler
# se xoay quanh goc the gioi lam bang vang xa (da kiem chung). Game xoay 0.55 bang signMesh chuan.
# GHE NHUA moi + nguoi nghe (nhan vat thuoc dung canh ghe)
def stool(cx, cz, col):
    box3(cx, SY + 0.30, cz, 0.34, 0.05, 0.34, M(col))
    box3(cx, SY + 0.14, cz, 0.26, 0.28, 0.26, M(col))
stool(SX - 3.6, -47.8, '#2456a6')
stool(SX + 3.2, -48.2, '#c22e22')

import_asset('character', (SX, SY + 0.35, SZ))          # ca si tren san khau
import_asset('character', (32.5, 0, 10.8))               # nguoi o san dai phun (me phai khung)
import_asset('character', (SX - 6.8, SY, -47.6))         # nguoi nghe goc hat

# ---------- nen + troi chang vang ----------
bpy.ops.mesh.primitive_plane_add(size=600, location=(0, 0, -1.5))
g0 = bpy.context.active_object
gm = bpy.data.materials.new('Ground'); gm.use_nodes = True
gm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.14, 0.13, 0.12, 1.0)
g0.data.materials.append(gm)
box3(-56, 16.9, -41, 90, 0.2, 26, M('#6e665a'))  # san dinh doi ngu canh (duoi sq2)

world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes['Background']
bg.inputs[0].default_value = (0.32, 0.40, 0.58, 1.0)
bg.inputs[1].default_value = 0.75

sun_data = bpy.data.lights.new('Sun', 'SUN')
sun_data.energy = 2.6
sun_data.color = (1.0, 0.78, 0.55)
sun_data.angle = math.radians(3.0)
sun = bpy.data.objects.new('Sun', sun_data)
bpy.context.scene.collection.objects.link(sun)
sun.location = (-80, -40, 45)
d = (Vector((0, 20, 0)) - sun.location).normalized()
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

# ---------- camera + render ----------
SC = bpy.context.scene
SC.render.engine = 'CYCLES'
SC.cycles.samples = 48
SC.cycles.device = 'CPU'
SC.cycles.use_denoising = True
SC.cycles.denoiser = 'OPENIMAGEDENOISE'
SC.view_settings.view_transform = 'AgX'
SC.view_settings.look = 'AgX - Medium High Contrast'
SC.render.resolution_x = 900
SC.render.resolution_y = 600
SC.render.image_settings.file_format = 'PNG'

cam_data = bpy.data.cameras.new('Cam')
cam_data.lens = 34.0
cam_data.clip_start = 0.1
cam_data.clip_end = 800
cam = bpy.data.objects.new('Cam', cam_data)
SC.collection.objects.link(cam)
SC.camera = cam

def shot(name, eye, target):
    cam.location = T2B(eye)
    d = (T2B(target) - cam.location).normalized()
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    SC.render.filepath = os.path.join(OUT, name)
    bpy.ops.render.render(write_still=True)
    print(f"[hbsq1] rendered {name}")

_only = os.environ.get('HBSQ_SHOTS')
_want = set(_only.split(',')) if _only else None
for _name, _eye, _tgt in [
    ('hbsquare-plaza.png', (-40, 6.0, 10), (27, 1.0, 5.0)),
    ('hbsquare-fountain.png', (20.5, 1.9, 12.8), (27.5, 2.0, 5.0)),
    ('hbsquare-stage.png', (24.8, 19.4, -41.5), (31.2, 17.8, -50.8)),
]:
    if _want is None or _name in _want:
        shot(_name, _eye, _tgt)
print("[hbsq1] DONE")
