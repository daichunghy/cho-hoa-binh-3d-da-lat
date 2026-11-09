# -*- coding: utf-8 -*-
"""PROPS-OPT-1 mini-scene: kiểm chứng CẬN CẢNH sạp hero 'dau' (dâu tây — dùng đúng
số đo code game + SỐ ĐOẠN MỚI sau giảm: cầu r<0.12 -> 8x6, r<0.45 -> 9x7) và
biển chỉ đường góc sân (24,10) 2 mặt chữ. Không dùng cảnh gương toàn map.
Quy ước: three (x, y-up, z) -> Blender (x, -z, y).
Chạy: blender -b --factory-startup -noaudio --python scripts/render_props_opt1_mini.py
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 32; sc.cycles.use_denoising = False
try: sc.render.threads = 2; sc.render.threads_mode = 'FIXED'
except Exception: pass
sc.render.resolution_x = 640; sc.render.resolution_y = 480
w = bpy.data.worlds.new("W"); sc.world = w
w.use_nodes = True
bg = w.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.05, 0.08, 0.16, 1)  # dem xanh sau kieu game
bg.inputs[1].default_value = 1.1

def C(p):
    return (p[0], -p[2], p[1])

def mat(hexv, rough=0.85, emis=None, estr=0.0):
    m = bpy.data.materials.new("m%06x" % hexv); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    r, g, bl = ((hexv >> 16 & 255) / 255, (hexv >> 8 & 255) / 255, (hexv & 255) / 255)
    b.inputs["Base Color"].default_value = (r, g, bl, 1)
    b.inputs["Roughness"].default_value = rough
    if emis is not None:
        er, eg, eb = ((emis >> 16 & 255) / 255, (emis >> 8 & 255) / 255, (emis & 255) / 255)
        b.inputs["Emission Color"].default_value = (er, eg, eb, 1)
        b.inputs["Emission Strength"].default_value = estr
    return m

def tbox(size, pos, hexv, rotY=0.0):
    bpy.ops.mesh.primitive_cube_add(location=C(pos))
    o = bpy.context.object
    o.dimensions = (size[0], size[2], size[1])
    o.rotation_euler = (0, 0, rotY)
    o.data.materials.append(mat(hexv))
    return o

def tcyl(rt, rb, h, pos, hexv, seg=10):
    bpy.ops.mesh.primitive_cone_add(vertices=seg, radius1=rb, radius2=rt, depth=h, location=C(pos))
    o = bpy.context.object
    o.data.materials.append(mat(hexv))
    return o

def tball(r, pos, hexv, sy=0.75):
    # dung dung so doan MOI cua game sau PROPS-OPT-1
    seg = 8 if r < 0.12 else 9 if r < 0.45 else 10
    ring = 6 if r < 0.12 else 7 if r < 0.45 else 8
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=C(pos), segments=seg, ring_count=ring)
    o = bpy.context.object
    o.scale = (1, 1, sy)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(mat(hexv))
    return o

def text3d(s, pos, size, rotY=0.0, color=0xffe9b0):
    bpy.ops.object.text_add(location=C(pos))
    o = bpy.context.object
    o.data.body = s
    o.data.size = size
    o.data.align_x = 'CENTER'; o.data.align_y = 'CENTER'
    o.rotation_euler = (math.pi / 2, 0, rotY)  # text Blender nam ngang -> dung len, xoay theo mat bien
    m = mat(color, rough=0.6); m.node_tree.nodes["Principled BSDF"].inputs["Emission Color"].default_value = ((color >> 16 & 255) / 255, (color >> 8 & 255) / 255, (color & 255) / 255, 1)
    m.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.9
    o.data.materials.append(m)
    return o

def camera(loc3, tgt3, lens=30):
    bpy.ops.object.camera_add(location=C(loc3))
    cam = bpy.context.object
    cam.data.lens = lens
    d = Vector(C(tgt3)) - Vector(C(loc3))
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    sc.camera = cam
    return cam

def lamp(loc3, energy=900):
    bpy.ops.object.light_add(type='POINT', location=C(loc3))
    l = bpy.context.object; l.data.energy = energy; l.data.color = (1.0, 0.72, 0.42)
    return l

# ---------- mat dat + tam san ----------
tbox((90, 0.1, 60), (22, -0.06, 8), 0x453f3a)
tbox((24, 0.08, 13), (24, 0.01, 3), 0x978a78)

# ---------- dai phun (don gian hoa theo so do game) ----------
tcyl(2.7, 2.9, 0.55, (24.5, 0.28, 5.2), 0x8a8074, seg=18)
bpy.ops.mesh.primitive_circle_add(radius=2.45, location=C((24.5, 0.5, 5.2)))
o = bpy.context.object; o.rotation_euler = (0, 0, 0); o.data.materials.append(mat(0xa8cfe0, rough=0.25))
tcyl(0.28, 0.42, 1.5, (24.5, 1.05, 5.2), 0x8a8074, seg=10)
tcyl(0.85, 0.5, 0.25, (24.5, 1.85, 5.2), 0x8a8074, seg=12)

# ---------- bien chi duong (24,10): cot + 2 mat ----------
tcyl(0.07, 0.09, 2.7, (24, 1.35, 10), 0x4a3b2c, seg=8)
tbox((0.06, 0.62, 2.4), (23.98, 2.85, 10), 0x7a1f1a)   # tam bien mat tay (nam doc theo z)
tbox((0.06, 0.62, 2.4), (24.02, 2.85, 10), 0x7a1f1a)   # tam bien mat dong
# chu: game ve tren canvas 1024x256, co chu chinh 84px -> cao ~0.20u; chu phu 44px -> ~0.10u
# (ban render truoc bi nguoc chu do xoay sai truc: mat tay dung -pi/2, mat dong dung +pi/2)
text3d('KHU QUAN AO', (23.93, 2.92, 10), 0.20, rotY=-math.pi / 2)
text3d('DAI PHUN NUOC', (23.93, 2.76, 10), 0.10, rotY=-math.pi / 2)
text3d('DAI PHUN NUOC', (24.07, 2.92, 10), 0.20, rotY=math.pi / 2)
text3d('BAC TAM CAP', (24.07, 2.76, 10), 0.10, rotY=math.pi / 2)

# ---------- sap 'dau' (dat o goc de chup can): quay mat +z ve camera ----------
# khung sap don gian: quay + ban + mai bat + 2 gio dau + bac 3 tang + thung bo + ly kem bo
SX, SZ = -2.0, -6.0  # tam sap trong mini-scene
def L(x, y, z):
    return (SX + x, y, SZ + z)
tbox((4.4, 1.05, 1.9), L(0, 0.55, 0), 0x6a5136)          # than quay
tbox((4.6, 0.08, 2.1), L(0, 1.12, 0), 0x8a6a42)          # mat quay
tbox((4.6, 0.06, 2.2), L(0, 2.6, 0), 0xc06c44)           # mai bat terracotta (SOUND-COLOR-1)
for lx in (-1.55, 0, 1.55):                                # 3 den long
    tball(0.21, L(lx, 3.0, 0.4), 0xffc46b, sy=1.25)
# 2 gio dau: moi gio 6 dau quanh + 1 tren + 1 la (so do strawberryBasket)
for bx, bz in ((-1.95, 2.25), (1.95, 2.3)):
    tcyl(0.34, 0.25, 0.3, L(bx, 0.15, bz), 0x9a6a42, seg=10)
    for i in range(6):
        a = i * 1.05
        tball(0.062, L(bx + math.cos(a) * 0.15, 0.33, bz + math.sin(a) * 0.15), 0xd8342a, sy=0.95)
    tball(0.07, L(bx, 0.37, bz), 0xd8342a, sy=0.95)
    tball(0.09, L(bx, 0.42, bz), 0x4d7340, sy=0.5)
# bac 3 tang dau (designHeroStall 'dau')
for s in range(3):
    tbox((1.15 - s * 0.18, 0.16, 0.34), L(0.72, 1.16 + s * 0.17, -0.18 + s * 0.05), 0x8a6a42)
    for i in range(4 - (1 if s == 2 else 0)):
        tball(0.05, L(0.32 + i * 0.26, 1.28 + s * 0.17, -0.13 + s * 0.05), 0xd8342a, sy=0.95)
# thung bo 034: 6 qua bo
tbox((0.56, 0.3, 0.42), L(-1.05, 1.05, 0.3), 0x8a6a42)
for i in range(6):
    tball(0.105, L(-1.22 + (i % 3) * 0.18, 1.26, 0.22 + (i // 3) * 0.17), 0x51783c, sy=0.85)
# 4 ly kem bo mep quay
for i, kc in enumerate([0xf5e6b8, 0xe88ac0, 0xbfe3c0, 0xf5e6b8]):
    tcyl(0.055, 0.042, 0.12, L(-0.12 + i * 0.17, 1.19, 0.85), kc, seg=8)
# day bong 6 bong tren mai
for i in range(6):
    tball(0.045, L(-1.85 + i * 0.74, 3.02 - abs(i - 2.5) * 0.05, 1.34), 0xb8b0a0, sy=1.0)

lamp((24, 4.5, 10), 700)
lamp((-2, 4.0, -2), 500)

# ---------- shot P1: can sap 'dau' tu phia truoc (tam mat nguoi choi) ----------
camera(L(0, 1.8, 6.8), L(0, 1.2, 0), lens=32)
sc.render.filepath = os.path.join(OUT, "po1-P1-stall-dau-draft.png")
bpy.ops.render.render(write_still=True)

# ---------- shot P2: bien chi duong nhin tu phia tay (huong di tu bac tam cap) ----------
camera((18.5, 1.8, 10), (24, 2.4, 10), lens=32)
sc.render.filepath = os.path.join(OUT, "po1-P2-sign-draft.png")
bpy.ops.render.render(write_still=True)
print("[props-opt] renders xong: po1-P1, po1-P2")
