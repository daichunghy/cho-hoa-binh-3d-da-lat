# -*- coding: utf-8 -*-
"""SWEEP-1 mini-scene: kiểm chứng CẬN CẢNH đài phun nước + khu quần áo theo ĐÚNG số đo
code game (index.html khối V5.5), không dùng cảnh gương toàn map (vật che lệch).
Quy ước: three (x, y-up, z) -> Blender (x, -z, y). three rotY theta -> Blender rotZ theta.
Chạy: blender -b --factory-startup -noaudio --python scripts/render_sweep1_mini.py
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 32; sc.cycles.use_denoising = False
try: sc.render.threads = 2; sc.render.threads_mode = 'FIXED'
except Exception: pass
sc.render.resolution_x = 640; sc.render.resolution_y = 480
sc.render.resolution_percentage = 100
w = bpy.data.worlds.new("W"); sc.world = w
w.use_nodes = True
bg = w.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.05, 0.08, 0.16, 1)  # đêm xanh sâu kiểu game
bg.inputs[1].default_value = 1.1

def C(p):  # three pos -> blender loc
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

def tbox(size, pos, hexv, rotY=0.0, emis=None, estr=0.0):
    # size/pos theo three; blender size = (sx, sz, sy)
    bpy.ops.mesh.primitive_cube_add(location=C(pos))
    o = bpy.context.object
    o.dimensions = (size[0], size[2], size[1])
    o.rotation_euler = (0, 0, rotY)
    o.data.materials.append(mat(hexv, emis=emis, estr=estr))
    return o

def tcyl(rt, rb, h, pos, hexv, seg=18, emis=None, estr=0.0):
    bpy.ops.mesh.primitive_cone_add(vertices=seg, radius1=rb, radius2=rt, depth=h, location=C(pos))
    o = bpy.context.object
    o.data.materials.append(mat(hexv, emis=emis, estr=estr))
    return o

def jet(a):
    # tia nước game: cyl r0.03 h1.15 tâm (cos a*0.42, 2.2, sin a*0.42) tai dai phun (24.5, 5.2),
    # nghiêng rotation.z = cos(a)*0.6, rotation.x = -sin(a)*0.6 (Euler XYZ three)
    import mathutils
    e = mathutils.Euler((math.sin(a) * 0.6, 0, -math.cos(a) * 0.6), 'XYZ')
    d = e.to_matrix() @ Vector((0, 1, 0))  # hướng trục tia trong three
    c3 = Vector((24.5 + math.cos(a) * 0.42, 2.2, 5.2 + math.sin(a) * 0.42))
    p1 = c3 - d * 0.575; p2 = c3 + d * 0.575
    b1 = Vector(C((p1.x, p1.y, p1.z))); b2 = Vector(C((p2.x, p2.y, p2.z)))
    mid = (b1 + b2) / 2; direction = b2 - b1
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.03, radius2=0.03, depth=direction.length, location=mid)
    o = bpy.context.object
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(direction.normalized())
    o.data.materials.append(mat(0xcfe8f4, rough=0.3))
    return o

# ---------- mặt đất + tấm sân ----------
tbox((90, 0.1, 60), (22, -0.06, 8), 0x453f3a)                       # nhựa đường
tbox((24, 0.08, 13), (24, 0.01, 3), 0x978a78)                       # tấm sân đài phun (game)
tbox((10, 0.08, 13.5), (40.5, 0.01, 20.75), 0x978a78)               # tấm sân quần áo (game)

# ---------- ĐÀI PHUN (24.5, 5.2) — chép số đo khối V5.5 ----------
FX, FZ = 24.5, 5.2
tcyl(2.7, 2.9, 0.55, (FX, 0.28, FZ), 0x8a8074)                       # bồn
tcyl(2.45, 2.45, 0.04, (FX, 0.5, FZ), 0x7fb2c9)                     # mặt nước
tcyl(0.28, 0.42, 1.5, (FX, 1.05, FZ), 0x8a8074)                     # cột giữa
tcyl(0.85, 0.5, 0.25, (FX, 1.85, FZ), 0x8a8074)                     # bát trên
for i in range(6):
    jet(i / 6 * math.pi * 2)
for (ux, uz) in [(22.6, 3.3), (26.4, 3.3), (22.6, 7.1), (26.4, 7.1)]:
    tbox((0.22, 0.18, 0.22), (ux, 0.09, uz), 0x3a3f45, emis=0xffc98a, estr=2.8)  # uplight đêm

# ---------- KHU QUẦN ÁO: 2 sạp stall.glb + 3 giá treo (chép clothesRack) ----------
def stall(x, z):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, "stall.glb"))
    new = [o for o in bpy.data.objects if o not in before]
    root = bpy.data.objects.new("StallRoot", None)
    bpy.context.collection.objects.link(root)
    root.location = C((x, 0, z)); root.rotation_euler = (0, 0, -math.pi / 2)
    for o in new:
        if o.parent is None:
            o.parent = root
    return root
stall(40, 17.5); stall(40, 22.5)

RACK_COLS = [0xb03a30, 0x35507a, 0xe8c832, 0x68804f, 0xe8e0cc, 0x8668c4, 0xd97c2e, 0x7a4a2e]
def rack(gx, gz):
    th = -math.pi / 2  # rotY game
    def W(lx, lz):     # local -> world three
        return (gx + lx * math.cos(th) + lz * math.sin(th), gz - lx * math.sin(th) + lz * math.cos(th))
    for px in (-1.05, 1.05):
        wx, wz = W(px, 0); tbox((0.07, 1.55, 0.07), (wx, 0.78, wz), 0x6a5136, rotY=th)
    wx, wz = W(0, 0); tbox((2.3, 0.06, 0.06), (wx, 1.55, wz), 0x8a8074, rotY=th)
    for i in range(8):
        wx, wz = W(-0.95 + i * 0.27, 0); tbox((0.17, 0.78, 0.34), (wx, 1.12, wz), RACK_COLS[i], rotY=th)
    wx, wz = W(0, 0); tbox((2.3, 0.05, 0.5), (wx, 0.35, wz), 0x74522f, rotY=th)
    for i in range(4):
        wx, wz = W(-0.8 + i * 0.53, 0); tbox((0.42, 0.16, 0.4), (wx, 0.46, wz), RACK_COLS[(i + 3) % 8], rotY=th)
rack(36.9, 14.9); rack(36.9, 25.1); rack(40, 26.3)

# ---------- đèn + camera ----------
sun = bpy.data.objects.new("Sun", bpy.data.lights.new("Sun", 'SUN'))
bpy.context.collection.objects.link(sun)
sun.data.energy = 1.6; sun.data.color = (0.9, 0.95, 1.0)
sun.rotation_euler = (math.radians(65), 0, math.radians(30))
pt = bpy.data.objects.new("Pt", bpy.data.lights.new("Pt", 'POINT'))
bpy.context.collection.objects.link(pt)
pt.location = C((30, 6, 12)); pt.data.energy = 3000; pt.data.color = (1.0, 0.85, 0.6)

def camera(loc3, tgt3, lens=30):
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = C(loc3)
    dvec = Vector(C(tgt3)) - o.location
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = dvec.to_track_quat('-Z', 'Y')
    sc.camera = o

SHOTS = [
    ("M1-fountain", (16, 3.0, -6), (24.5, 1.2, 5.2)),
    ("M2-fountain-high", (17, 7.5, -4), (24.5, 0.4, 5.2)),
    ("M3-clothing", (31, 2.6, 13), (41, 1.2, 20.5)),
    ("M4-clothing-row", (35.5, 2.2, 27.5), (41.5, 1.2, 18)),
]
for nm, cl, ct in SHOTS:
    camera(cl, ct)
    sc.render.filepath = os.path.join(OUT, "sw1-%s-draft.png" % nm)
    bpy.ops.render.render(write_still=True)
    print("RENDERED", nm, flush=True)
print("MINI DONE", flush=True)
