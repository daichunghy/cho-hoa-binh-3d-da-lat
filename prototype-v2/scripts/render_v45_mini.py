# -*- coding: utf-8 -*-
"""Render mini V4.5 — kiểm chứng HÌNH HỌC nhanh (thang mới + nhà lồng + thang trong nhà).
Chỉ import model liên quan, ~40 người. Quy ước: render = three (x, -z, y)."""
import bpy, math, os, random, sys
from mathutils import Vector

random.seed(7)
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

def stairH(z):
    if z >= -2: return 0.0
    if z <= -30: return 17.0
    if z > -8.25:
        s = min(1.0, math.floor((z + 8.25) / 6.25 * 10) / 10.0)
        return 5.67 * (1 - s)
    if z > -12.25: return 5.67
    if z > -18.75:
        s = min(1.0, math.floor((z + 18.75) / 6.5 * 10) / 10.0)
        return 11.33 - 5.66 * s
    if z > -22.75: return 11.33
    s = min(1.0, math.floor((z + 30) / 7.25 * 10) / 10.0)
    return 17 - 5.67 * s

def innerStairH(z):
    if z <= 18.4:
        s = min(1.0, math.floor((z - 12) / 6.4 * 10) / 10.0)
        return 12.6 - 6.05 * s
    if z <= 20.4: return 6.55
    s = min(1.0, math.floor((z - 20.4) / 6.4 * 10) / 10.0)
    return 6.55 - 6.05 * s

def groundH(x, z):
    if 14.5 <= x <= 20.5 and -30 <= z <= 9: return 17.14 - (z + 30) * 0.11282
    if 29 <= x <= 33 and 12 <= z <= 26.8: return innerStairH(z)
    if 14 <= x <= 21 and 7 <= z <= 12: return 12.6
    if 21 <= x <= 33 and 7 <= z <= 12.2: return 12.6
    if -34 <= x <= 34 and 12 <= z <= 28: return 0.5
    if z <= -30: return 17.0
    if z >= -2: return 0.0
    if -11 <= x <= 11: return stairH(z)
    if (-19 <= x < -11) or (11 < x < 14.5):
        if z > -8.25: return 2.8
        if z > -18.75: return 8.5
        return 14.2
    return 17 * ((-2 - z) / 28.0)

def srgb(hx):
    out = []
    for i in (0, 2, 4):
        c = int(hx[i:i + 2], 16) / 255.0
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return tuple(out)

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 10
sc.cycles.use_denoising = True
sc.render.resolution_x = 720
sc.render.resolution_y = 540

w = bpy.data.worlds.new("W"); sc.world = w
w.use_nodes = True
bg = w.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.088, 0.060, 0.033, 1.0)
bg.inputs[1].default_value = 1.6
d = bpy.data.lights.new("Sun", 'SUN'); d.energy = 0.65; d.color = (1.0, 0.72, 0.45)
o = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(o)
o.rotation_euler = (math.radians(65), 0, math.radians(30))
sc.view_settings.exposure = 1.08

def point(loc, energy=150, dist=15):
    dd = bpy.data.lights.new("Pt", 'POINT'); dd.color = (1.0, 0.72, 0.38); dd.energy = energy
    dd.shadow_soft_size = 0.3
    oo = bpy.data.objects.new("Pt", dd); bpy.context.collection.objects.link(oo)
    oo.location = loc

def camera(loc, target, lens=44):
    for oo in list(bpy.data.objects):
        if oo.type == 'CAMERA': bpy.data.objects.remove(oo, do_unlink=True)
    dd = bpy.data.cameras.new("Cam"); dd.lens = lens
    oo = bpy.data.objects.new("Cam", dd); bpy.context.collection.objects.link(oo)
    oo.location = loc
    oo.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    sc.camera = oo

def mat_plain(name, rgb):
    m = bpy.data.materials.new(name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1)
    return m

_CV = [(-.5,-.5,-.5),(.5,-.5,-.5),(.5,.5,-.5),(-.5,.5,-.5),(-.5,-.5,.5),(.5,-.5,.5),(.5,.5,.5),(-.5,.5,.5)]
_CF = [(0,1,2,3),(4,0,3,7),(1,5,6,2),(5,4,7,6),(3,2,6,7),(4,5,1,0)]
_cmesh_cache = {}
def cbox(size, loc, rgb, rot=None):
    m = _cmesh_cache.get(rgb)
    if m is None:
        m = bpy.data.meshes.new("CB")
        m.from_pydata(_CV, [], _CF); m.update()
        m.materials.append(mat_plain("CBM", rgb))
        _cmesh_cache[rgb] = m
    oo = bpy.data.objects.new("CB", m)
    bpy.context.collection.objects.link(oo)
    oo.location = loc; oo.scale = size
    if rot: oo.rotation_euler = rot
    return oo

def import_glb(name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name))
    return [oo for oo in bpy.data.objects if oo not in before]

def wrap(objs, name):
    e = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(e)
    for oo in objs:
        if oo.parent is None: oo.parent = e
    return e

def imp(name, loc=(0, 0, 0)):
    objs = import_glb(name)
    e = wrap(objs, "wrap_" + name)
    e.location = loc
    return e

imp("stairs.glb", (0, 16, 0))
imp("market.glb", (0, -20, 0))
# sàn đất đơn giản quanh thang
cbox((150, 40, 0.2), (0, 22, -0.1), (0.52, 0.50, 0.46))
cbox((150, 56, 17), (0, 58, 8.5), (0.42, 0.38, 0.34))
for (bx0, bx1) in ((-19, -11), (11, 14.5)):
    bw = bx1 - bx0; bcx = (bx0 + bx1) / 2
    for (top, zc, dd2) in ((14.2, -24.375, 11.25), (8.5, -13.5, 10.5), (2.8, -5.125, 6.25)):
        cbox((bw, dd2, top + 1), (bcx, -zc, (top - 1) / 2), (0.40, 0.46, 0.35))
        cbox((bw - 0.15, dd2 - 0.15, 0.05), (bcx, -zc, top + 0.02), (0.54, 0.50, 0.45))
print("MINI ground done", flush=True)

# sạp template
stall_objs = import_glb("stall.glb")
stall_tpl = wrap(stall_objs, "StallTpl")
for oo in [stall_tpl] + stall_objs: oo.hide_render = True
def dup_tree(tpl):
    bpy.ops.object.select_all(action='DESELECT')
    tpl.select_set(True)
    for ch in tpl.children_recursive: ch.select_set(True)
    bpy.context.view_layer.objects.active = tpl
    bpy.ops.object.duplicate()
    root = bpy.context.object
    for oo in [root] + list(root.children_recursive): oo.hide_render = False
    return root
def tree(root): return [root] + list(root.children_recursive)
def find(objs, base):
    for oo in objs:
        if oo.name.split('.')[0] == base: return oo
    return None
def own_mat(root, base, rgb):
    for oo in tree(root):
        if oo.type != 'MESH': continue
        for slot in oo.material_slots:
            m = slot.material
            if m and m.name.split('.')[0] == base:
                slot.link = 'OBJECT'
                nm = m.copy()
                nm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1)
                slot.material = nm
AWNC = [(0.85, 0.35, 0.16), (0.16, 0.42, 0.62), (0.25, 0.55, 0.30), (0.78, 0.30, 0.45)]
STALLS = [(6.2, -21.6, math.pi / 2, 11.33), (6.2, -10.4, math.pi / 2, 5.67),
          (-20, 20, math.pi, 0.5), (20, 20, 0, 0.5), (-24, 15, 0, 0.5), (16, 15, 0, 0.5)]
for i, (sx, sz, ry, by) in enumerate(STALLS):
    g = dup_tree(stall_tpl)
    g.location = (sx, -sz, by); g.rotation_euler = (0, 0, ry)
    own_mat(g, 'Awning', AWNC[i % 4])
    lx, lz = 0.0, 1.02
    wx = sx + lx * math.cos(ry) + lz * math.sin(ry)
    wz = sz - lx * math.sin(ry) + lz * math.cos(ry)
    point((wx, -wz, by + 2.3), 160, 14)
print("MINI stalls done", flush=True)

# lưới quầy + lửng + thang trong nhà (gương cbox như bản full)
INNER45 = [(-24, 15), (16, 15), (-16, 23.5), (24, 23.5), (-20, 20), (20, 20)]
AWN45 = [(0.78, 0.22, 0.18), (0.18, 0.43, 0.64), (0.91, 0.53, 0.18), (0.25, 0.62, 0.30), (0.53, 0.41, 0.77), (0.85, 0.49, 0.18)]
qn = 0
rows45 = []
for i in range(12):
    cx = -28.6 + i * 5.2
    rows45 += [(cx, 13.3, 0), (cx, 26.7, math.pi)]
for i in range(12):
    cx = -28.6 + i * 5.2
    rows45 += [(cx, 19.35, math.pi), (cx, 20.65, 0)]
for (rx, rz, ry) in rows45:
    if rx > 25 and rz > 14: continue
    if any(abs(rx - sx) < 4.6 and abs(rz - sz) < 2.7 for (sx, sz) in INNER45): continue
    qn += 1
    cbox((4.3, 1.4, 0.95), (rx, -rz, 0.98), (0.54, 0.42, 0.26) if qn % 2 else (0.46, 0.32, 0.18))
    fx = math.sin(ry); fz = math.cos(ry)
    cbox((3.6, 0.05, 0.95), (rx + fx * 0.62, -(rz + fz * 0.62), 3.05), (0.80, 0.72, 0.55))
    cbox((4.4, 1.55, 0.08), (rx + fx * 0.25, -(rz + fz * 0.25), 2.35), AWN45[qn % 6])
cbox((56, 0.95, 0.3), (0, -26.95, 3.55), (0.43, 0.40, 0.35))
cbox((56, 0.08, 1.1), (0, -26.55, 4.35), (0.56, 0.71, 0.79))
cbox((12, 5.2, 0.35), (27, -9.6, 12.42), (0.54, 0.50, 0.45))
cbox((0.35, 15.2, 13.2), (28.82, -19.4, 6.85), (0.43, 0.40, 0.35))
for i in range(10):
    cbox((4, 0.72, 0.28), (31, -(12 + 0.64 * i + 0.32), (12.6 - 6.05 * i / 10) - 0.14), (0.54, 0.50, 0.45))
    cbox((4, 0.72, 0.28), (31, -(20.4 + 0.64 * i + 0.32), (6.55 - 6.05 * i / 10) - 0.14), (0.54, 0.50, 0.45))
cbox((4, 2.0, 0.3), (31, -19.4, 6.4), (0.54, 0.50, 0.45))
cbox((1.7, 2.2, 0.1), (32.1, -19.4, 7.0), (0.48, 0.29, 0.18))
for i, cc in enumerate([(0.76, 0.23, 0.18), (0.91, 0.78, 0.20), (0.18, 0.48, 0.72), (0.88, 0.48, 0.16), (0.60, 0.29, 0.48), (0.29, 0.60, 0.29)]):
    cbox((0.3, 0.1, 0.62), (31.35, -(18.65 + i * 0.31), 7.28), cc)
point((0, -20, 4.5), 220, 20); point((-16, -16, 3.5), 120, 12); point((31, -19.4, 9.5), 90, 9)
# V4.5 polish: 4 sạp chân thang (gương web)
for (fx2, fz2, fc) in ((-17.6, 1.6, (0.78, 0.22, 0.18)), (-13.0, 2.0, (0.18, 0.43, 0.64)), (13.0, 2.0, (0.91, 0.53, 0.18)), (17.6, 1.6, (0.25, 0.62, 0.30))):
    cbox((1.1, 2.2, 0.85), (fx2, -fz2, 0.48), (0.54, 0.37, 0.23))
    cbox((1.5, 2.5, 0.08), (fx2, -fz2, 1.95), fc)
print("MINI counters:", qn, flush=True)

# người
char_objs = import_glb("character.glb")
char_tpl = wrap(char_objs, "CharTpl")
for oo in [char_tpl] + char_objs: oo.hide_render = True
SHIRTS = ['a62b25', 'd97a30', 'd9a62e', 'e8c87e', '6b8f3e', '2e6b46', '2f8f83',
          '3a6bc2', '8668c4', 'e58e6b', 'c95d7e', '7a4a2e', '96683f', '35507a']
PANTS = ['4a4640', '3a3f4a', '5c4633', '2e2a26']
cnt = [0]
def person(x3, z3, rotz=0.0, sit=False, y3=None):
    g = dup_tree(char_tpl)
    objs = tree(g)
    y = groundH(x3, z3) if y3 is None else y3
    if sit: y += 0.30
    g.location = (x3, -z3, y)
    g.rotation_euler = (0, 0, rotz)
    keep = ['HatNonLa', 'HatBeanie', 'HatCap'][cnt[0] % 3]
    for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
        hh = find(objs, hn)
        if hh: hh.hide_render = (hn != keep)
    scarf = find(objs, 'Scarf')
    if scarf: scarf.hide_render = random.random() < 0.65
    own_mat(g, 'Shirt', srgb(random.choice(SHIRTS)))
    own_mat(g, 'Pants', srgb(random.choice(PANTS)))
    if sit:
        for nm in ('LegL', 'LegR'):
            leg = find(objs, nm)
            if leg: leg.rotation_euler.x = -1.45
        arm = find(objs, 'ArmR')
        if arm: arm.rotation_euler.x = -1.0
    cnt[0] += 1
    return g
def stool(x3, z3, y3):
    cbox((0.34, 0.34, 0.30), (x3, -z3, y3 + 0.15), (0.10, 0.28, 0.60))
STAIR_SITTERS = [(-7.8, -21.5), (-8.6, -20.6), (7.6, -21.2), (8.4, -20.3), (-6.9, -19.3),
                 (-7.2, -17.6), (-8.1, -16.7), (-7.5, -15.8), (-6.8, -13.4),
                 (7.4, -17.2), (8.2, -16.3), (7.0, -14.2), (7.9, -13.5),
                 (-7.7, -11.3), (-8.5, -10.4), (7.5, -11.0), (8.3, -10.1), (6.7, -9.3),
                 (-7.3, -7.2), (-8.0, -6.4), (-6.9, -4.6),
                 (7.3, -6.8), (8.1, -5.9), (7.0, -4.9),
                 (-7.4, -28.6), (-8.2, -27.7), (7.5, -28.2), (8.3, -27.3)]
for (sx, sz) in STAIR_SITTERS:
    stool(sx, sz, groundH(sx, sz))
    person(sx, sz, rotz=(random.random() - 0.5) * 0.44, sit=True)
for (sx, sz, rz) in [(-2, -6, math.pi), (2.5, -12, 0), (-2.5, -17, math.pi), (3, -24, 0), (-3, -28, math.pi)]:
    person(sx, sz, rotz=rz)   # người đi trong làn giữa
person(2.8, -20.8, rotz=0, sit=True, y3=11.33)   # chú ba
person(1.8, -19.6, rotz=math.pi, y3=11.33)       # khách coi bói
for (qx, qz) in ((8.6, -22.3), (8.6, -20.9), (8.6, -11.1), (8.6, -9.7)):
    person(qx, qz, rotz=-math.pi / 2)            # khách chờ 2 sạp chiếu nghỉ
for (fx2, fz2, fl) in ((-17.6, 1.6, 1), (-13.0, 2.0, 1), (13.0, 2.0, -1), (17.6, 1.6, -1)):
    person(fx2 - 0.95 * fl, fz2, rotz=math.pi / 2 if fl > 0 else -math.pi / 2)  # người bán sạp chân thang (polish)
for (hx, hz, rz) in ((-8, 17.5, math.pi / 2), (8, 22, -math.pi / 2), (-24, 21.5, 0), (14, 17.2, math.pi), (0, 24, 0.5)):
    person(hx, hz, rotz=rz)                      # khách trong nhà lồng
for (lx, lz) in ((-8, 26.9), (3, 26.9), (13, 26.9)):
    person(lx, lz, rotz=math.pi, y3=3.7)         # khách lửng kính
person(30.9, 19.4, rotz=math.pi / 2, y3=6.55)    # người bán chợ la
person(30.3, 15, y3=innerStairH(15))             # người đi thang trong nhà
person(30.3, 23, y3=innerStairH(23))
person(25, 10.8, y3=12.6)                        # người trên hành lang nối
print("MINI people:", cnt[0], flush=True)

SHOTS = [
    ("m1-thang-can", (7.5, 13, 7.5), (-3, -6, 1), 44),
    ("m2-chan-thang", (0, -9, 2.4), (-1, 22, 9), 44),
    ("m3-trong-cho", (-19, -14.0, 2.6), (10, -21, 1.2), 44),
    ("m4-thang-trong-nha", (16, -6, 15.5), (31, -19, 6.5), 44),
    ("m5-trong-cho-rong", (-30, -13.5, 5.5), (15, -22, 0.8), 44),
    ("m6-thang-tu-sanh", (24, -22, 2.2), (31.5, -15, 9), 44),
    ("m7-trong-thang", (30.3, -16.5, 10.2), (30.8, -26.5, 0.8), 44),
]
_only = [x for a in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []) if a.startswith('only=') for x in a.split('=')[1].split(',')]
for (nm, cl, ct, ln) in SHOTS:
    if _only and nm.split('-')[0] not in _only: continue
    camera(cl, ct, lens=ln)
    sc.render.filepath = os.path.join(OUT, "v45-%s-mini.png" % nm)
    bpy.ops.render.render(write_still=True)
    print("RENDERED mini", nm, flush=True)
print("ALL MINI DONE", flush=True)
