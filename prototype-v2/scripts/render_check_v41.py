# -*- coding: utf-8 -*-
"""Render kiểm chứng V4.1 — TOÀN CẢNH như web (2 cao độ, nhà lồng, thang + cầu,
bùng binh + tượng + xe chạy + bãi xe đậu, dãy sạp, khách sạn, quán) VÀ đám đông
theo đúng phân bố web (ngồi ăn + xếp hàng + đứng trên bậc thang / đường chợ đêm).
2 ảnh nghiệm thu: v41-01-toan-canh-ngay (ngày) + v41-02-cho-dem (đêm, đèn sạp).
Chạy: blender -b --factory-startup -noaudio --python scripts/render_check_v41.py [-- draft]
Quy ước khung render = three (x, -z, y) như render_check.py bản v2.
Tối ưu tốc độ: model lặp (người/sạp/quán/đèn/thông) chỉ import 1 lần rồi
duplicate; màu áo từng người qua material slot link='OBJECT'.
"""
import bpy, math, os, random, sys
from mathutils import Vector

random.seed(42)
DRAFT = 'draft' in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
print("V41 MODE:", "draft" if DRAFT else "full", flush=True)
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

# ---------------- hàm chiều cao mặt đất (port từ index.html) ----------------
def stairH(z):
    if z >= -2: return 0.0
    if z <= -30: return 17.0
    if z > -9:
        t = (-9 - z) / 7.0
        s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
        return 5.67 * (1 - min(1.0, s))
    if z > -11.5: return 5.67
    if z > -19.5:
        t = (-19.5 - z) / 8.0
        s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
        return 11.33 - 5.66 * min(1.0, s)
    if z > -22: return 11.33
    t = (-30 - z) / 8.0
    s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
    return 17 - 5.67 * min(1.0, s)

def groundH(x, z):
    if 14.5 <= x <= 20.5 and -30 <= z <= 9: return 17 - 4.4 * ((z + 30) / 39.0)
    if 14 <= x <= 21 and 7 <= z <= 12: return 12.6
    if -34 <= x <= 34 and 12 <= z <= 28: return 0.5
    if z <= -30: return 17.0
    if z >= -2: return 0.0
    if -5.5 <= x <= 5.5: return stairH(z)
    return 17 * ((-2 - z) / 28.0)

def srgb(hx):
    out = []
    for i in (0, 2, 4):
        c = int(hx[i:i + 2], 16) / 255.0
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return tuple(out)

# ---------------- khung cảnh ----------------
bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 4 if DRAFT else 20
sc.cycles.use_denoising = True
sc.cycles.use_adaptive_sampling = True
sc.cycles.adaptive_threshold = 0.03
sc.render.resolution_x = 480 if DRAFT else 896
sc.render.resolution_y = 360 if DRAFT else 672

def world_bg(rgb, strength):
    w = bpy.data.worlds.new("W"); sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (*rgb, 1.0)
    bg.inputs[1].default_value = strength
    return bg

SUN = None
def make_sun(euler=(math.radians(50), 0, math.radians(35)), energy=3.0):
    global SUN
    d = bpy.data.lights.new("Sun", 'SUN'); d.energy = energy
    o = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(o)
    o.rotation_euler = euler
    SUN = o
    return o

def point(loc, color=(1.0, 0.78, 0.5), energy=0.0, dist=12.0):
    d = bpy.data.lights.new("Pt", 'POINT'); d.color = color; d.energy = energy
    d.shadow_soft_size = 0.3
    o = bpy.data.objects.new("Pt", d); bpy.context.collection.objects.link(o)
    o.location = loc
    return o

def camera(loc, target, lens=42):
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA': bpy.data.objects.remove(o, do_unlink=True)
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    sc.camera = o
    return o

def mat_plain(name, rgb):
    m = bpy.data.materials.new(name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1)
    return m

def box(name, size, loc, rgb, rot=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    # QUAN TRỌNG: location=False — nếu không Blender 5.0 nướng cả location vào mesh,
    # object về (0,0,0) khiến logic xoá Slope theo location.x ở dưới chết lặng lẽ.
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rot: o.rotation_euler = rot
    o.data.materials.append(mat_plain(name + "M", rgb))
    return o

def import_glb(name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name))
    return [o for o in bpy.data.objects if o not in before]

def find(objs, base):
    for o in objs:
        if o.name.split('.')[0] == base:
            return o
    return None

def wrap(objs, name):
    e = bpy.data.objects.new(name, None)
    bpy.context.collection.objects.link(e)
    for o in objs:
        if o.parent is None: o.parent = e
    return e

def imp(name, loc=(0, 0, 0), rotz=0.0, scale=(1, 1, 1), rotx=0.0):
    objs = import_glb(name)
    e = wrap(objs, "wrap_" + name)
    e.location = loc; e.rotation_euler = (rotx, 0, rotz); e.scale = scale
    return e, objs

def make_template(name, wrap_name):
    """Import 1 lần, gom vào empty, ẩn toàn bộ — làm khuôn để duplicate."""
    objs = import_glb(name)
    e = wrap(objs, wrap_name)
    for o in [e] + objs:
        o.hide_render = True
    return e

def dup_tree(tpl):
    """Duplicate cả cây từ tpl (tpl là empty gốc). Trả về root mới, đã hiện lại."""
    bpy.ops.object.select_all(action='DESELECT')
    tpl.select_set(True)
    for ch in tpl.children_recursive: ch.select_set(True)
    bpy.context.view_layer.objects.active = tpl
    bpy.ops.object.duplicate()
    root = bpy.context.object
    for o in [root] + list(root.children_recursive):
        o.hide_render = False
    return root

def tree(root):
    return [root] + list(root.children_recursive)

def own_mat(root, base, rgb):
    """Gán màu riêng cho các slot material tên `base` trong cây (link OBJECT)."""
    for o in tree(root):
        if o.type != 'MESH': continue
        for slot in o.material_slots:
            m = slot.material
            if m and m.name.split('.')[0] == base:
                slot.link = 'OBJECT'
                nm = m.copy()
                nm.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*rgb, 1)
                slot.material = nm

def set_mat(objs, base, rgb=None, emission_strength=None):
    for o in objs:
        if o.type != 'MESH': continue
        for m in o.data.materials:
            if m and m.name.split('.')[0] == base and m.use_nodes:
                bsdf = m.node_tree.nodes["Principled BSDF"]
                if rgb is not None:
                    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
                if emission_strength is not None:
                    bsdf.inputs["Emission Strength"].default_value = emission_strength

# ---------------- mặt đất / đồi / đường ----------------
box("Plaza", (170, 130, 0.2), (0, -18, -0.1), (0.52, 0.50, 0.46))
box("Road", (170, 11, 0.22), (0, -2, 0.0), (0.26, 0.26, 0.27))
box("Hill", (150, 52, 17), (0, 56, 8.5), (0.42, 0.38, 0.34))
box("Hilltop", (150, 52, 0.2), (0, 56, 17.05), (0.55, 0.52, 0.46))
box("Grass", (150, 10, 0.22), (0, 76, 17.06), (0.34, 0.42, 0.29))
for (x0, x1) in ((-70, -5.5), (5.5, 14.5), (20.5, 70)):
    w = x1 - x0
    box("Slope", (w, 34.5, 0.3), ((x0 + x1) / 2, 16, 8.4), (0.40, 0.46, 0.35),
        rot=(math.atan2(17, 28), 0, 0))
# sườn tây rút về phía bắc (render y 14..33) để không chôn đảo bùng binh
# (đảo nằm trên plaza phẳng như bản web; box Slope tạo bởi script này chỉ là mô phỏng địa hình)
for o in list(bpy.data.objects):
    if o.name.startswith("Slope") and o.location.x < -30:
        bpy.data.objects.remove(o, do_unlink=True)
box("SlopeW", (64.5, 20.5, 0.3), (-37.75, 23.5, 11.4), (0.40, 0.46, 0.35),
    rot=(math.atan2(17, 28), 0, 0))

# ---------------- công trình ----------------
imp("market.glb", (0, -20, 0))
imp("theater.glb", (-19, 56, 17))
imp("cafe.glb", (13, 60, 17))
imp("stairs.glb", (0, 16, 0))
imp("roundabout.glb", (-24, 6, 0))
imp("bridge.glb", (17.5, 10.5, 14.65), rotx=math.atan2(4.4, 39))
imp("pier.glb", (17.5, 2, 0), scale=(1, 1, 13.4))
imp("pier.glb", (17.5, 16, 0), scale=(1, 1, 15.0))
print("SECTION buildings done", flush=True)

# khách sạn: nhân bản từng group HotelA/B/C/D theo vị trí web
ht_objs = import_glb("hotels.glb")
ht_roots = {}
for nm in ("HotelA", "HotelB", "HotelC", "HotelD"):
    r = find(ht_objs, nm)
    if r: ht_roots[nm] = r
for r in ht_roots.values():
    p = r.parent
    if p is None:
        e = bpy.data.objects.new("wrap_" + r.name, None)
        bpy.context.collection.objects.link(e)
        r.parent = e
        ht_roots[r.name.split('.')[0]] = e
HOTEL_SPOTS = [
    ("HotelA", (-38, 77, 17), 0), ("HotelC", (0, 77.5, 17), 0), ("HotelB", (38, 77, 17), 0),
    ("HotelD", (-66, -4, 0), math.pi / 2), ("HotelB", (66, -8, 0), -math.pi / 2),
    ("HotelA", (-28, -52, 0), math.pi), ("HotelD", (30, -54, 0), math.pi),
]
for nm, loc, rz in HOTEL_SPOTS:
    src = ht_roots.get(nm)
    if not src: continue
    # khuôn: nếu group chưa có wrapper riêng thì dùng chính group làm khuôn
    tpl = src
    bpy.ops.object.select_all(action='DESELECT')
    tpl.select_set(True)
    for ch in tpl.children_recursive: ch.select_set(True)
    bpy.context.view_layer.objects.active = tpl
    bpy.ops.object.duplicate()
    dup = bpy.context.object
    dup.location = loc; dup.rotation_euler = (0, 0, rz)
for r in list(ht_roots.values()):
    for o in tree(r): o.hide_render = True

# quán vỉa hè x3 (template)
shop_tpl = make_template("shop.glb", "ShopTpl")
for loc, rz in (((-44, -12, 0), 0.6), ((12, -8.5, 0), -0.35), ((46, -12.5, 0), -0.55)):
    g = dup_tree(shop_tpl)
    g.location = loc; g.rotation_euler = (0, 0, rz)
print("SECTION hotels+shops done", flush=True)

# ---------------- dãy sạp (template) ----------------
stall_tpl = make_template("stall.glb", "StallTpl")
STALLS = [  # (x three, z three, rotY three, baseY, tag)
    (-36, 8.4, math.pi, 0, 'grill'), (-31, 8.4, math.pi, 0, ''), (-26, 8.4, math.pi, 0, ''),
    (-21, 8.4, math.pi, 0, ''), (22, 8.4, math.pi, 0, ''), (27, 8.4, math.pi, 0, 'phin'),
    (32, 8.4, math.pi, 0, ''), (37.5, 8.4, math.pi, 0, ''),
    (-24, 15, 0, 0.5, ''), (16, 15, 0, 0.5, ''), (-16, 23.5, math.pi, 0.5, ''), (24, 23.5, math.pi, 0.5, ''),
    (2, -46, 0, 17, ''), (9.5, -46, 0, 17, ''), (-6, -47, 0, 17, ''), (-31, -47, 0, 17, ''),
    (-12, 3, 0, 0, ''), (6, 3, 0, 0, ''), (30, 3, 0, 0, ''), (-38, 3, 0, 0, ''),
]
stall_lights = []
for (sx, sz, ry, by, tag) in STALLS:
    g = dup_tree(stall_tpl)
    g.location = (sx, -sz, by); g.rotation_euler = (0, 0, ry)
    for o in tree(g):
        nm = o.name.split('.')[0]
        if nm.startswith('Grill'): o.hide_render = (tag != 'grill')
        elif nm.startswith('Phin'): o.hide_render = (tag != 'phin')
    lx, lz = 0.0, 1.02
    wx = sx + lx * math.cos(ry) + lz * math.sin(ry)
    wz = sz - lx * math.sin(ry) + lz * math.cos(ry)
    stall_lights.append((wx, -wz, by + 2.42))

# đèn đường + thông (template)
lamp_tpl = make_template("lamp.glb", "LampTpl")
for x in (-40, -20, 0, 20, 40):
    g = dup_tree(lamp_tpl); g.location = (x, 3.2, 0)
pine_tpl = make_template("pine.glb", "PineTpl")
for (px, py, pz, ps) in [(-52, 38, 17, 1.2), (52, 40, 17, 1.1), (-60, 62, 17, 1.3),
                          (58, 66, 17, 1.2), (-64, 14, 0, 0.9), (64, 12, 0, 0.95),
                          (40, 48, 17, 1.0), (-16.6, 13.8, 0, 1.15)]:
    g = dup_tree(pine_tpl); g.location = (px, py, pz); g.scale = (ps, ps, ps)
print("SECTION stalls done", flush=True)

# sân khấu đồi
box("Stage", (8, 5, 0.5), (31, 52, 17.25), (0.45, 0.33, 0.22))
box("StageBack", (8, 0.3, 3.2), (31, 54.6, 18.6), (0.30, 0.22, 0.16))

# ---------------- xe cộ ----------------
veh_objs = import_glb("vehicle.glb")
veh_wrap = wrap(veh_objs, "VehTpl")
moto_tpl = find(veh_objs, "Moto")
car_tpl = find(veh_objs, "Car")
for o in tree(veh_wrap): o.hide_render = True

def dup_sub(tpl):
    bpy.ops.object.select_all(action='DESELECT')
    tpl.select_set(True)
    for ch in tpl.children_recursive: ch.select_set(True)
    bpy.context.view_layer.objects.active = tpl
    bpy.ops.object.duplicate()
    root = bpy.context.object
    for o in tree(root): o.hide_render = False
    return root

BIKE_COLS = ['b03a30', '30303a', 'f0ead8', '2e6da4', '8c8c92', '7a2e35', '2f5d5a']
def paint_vehicle(g):
    own_mat(g, 'BikeBody', srgb(random.choice(BIKE_COLS)))

def hide_rider(g):
    for ch in tree(g):
        if ch.name.split('.')[0] in ('Rider', 'Helmet'):
            ch.hide_render = True

for i in range(5):  # xe chạy vòng bùng binh (tâm render (-24, 6))
    a = 0.4 + i / 5 * math.pi * 2
    g = dup_sub(moto_tpl)
    g.location = (-24 + math.cos(a) * 10.6, 6 + math.sin(a) * 10.6, 0)
    g.rotation_euler = (0, 0, -a)
    paint_vehicle(g)
g = dup_sub(car_tpl)
g.location = (-24 + math.cos(2.2) * 11.9, 6 + math.sin(2.2) * 11.9, 0)
g.rotation_euler = (0, 0, -2.2)
for (vx, vy, rz) in ((-50, -0.2, math.pi / 2), (5, -0.2, math.pi / 2), (-15, -3.6, -math.pi / 2), (45, -3.6, -math.pi / 2)):
    g = dup_sub(moto_tpl)
    g.location = (vx, vy, 0); g.rotation_euler = (0, 0, rz)
    paint_vehicle(g)
g = dup_sub(car_tpl)
g.location = (30, -3.6, 0); g.rotation_euler = (0, 0, -math.pi / 2)
for gx in range(-46, 47):  # bãi xe đậu trước chợ (three z=11.25 -> render y=-11.25)
    x = gx * 1.0
    if -5.5 < x < 5.5 or x < -40 or x > 41: continue
    if random.random() < 0.18: continue
    g = dup_sub(moto_tpl)
    g.location = (x + (random.random() - 0.5) * 0.15, -11.25 + (random.random() - 0.5) * 0.12, 0)
    g.rotation_euler = (0, 0, (random.random() - 0.5) * 0.12)
    hide_rider(g); paint_vehicle(g)
print("SECTION vehicles done", flush=True)

# ---------------- đám đông (template character) ----------------
char_tpl = make_template("character.glb", "CharTpl")
SHIRTS = ['9c4034', '7a2e35', '5c4633', '2e4a6b', '51624a', '74566b', '8c6a3a',
          '3f4854', 'a8573c', '6b4a7a', '2f5d5a', 'b08a5a', '845460', '44586b']
PANTS = ['4a4640', '3a3f4a', '5c4633', '2e2a26']
SCARVES = ['c9a227', 'b03a30', '2e6da4', '74566b', 'e07b2a']
HATS = ['beanie', 'cap', 'nonla', 'beanie', 'nonla', 'cap', 'beanie']
people_count = [0]

def person(x3, z3, rotz=0.0, sit=False, y3=None, hat=None):
    g = dup_tree(char_tpl)
    objs = tree(g)
    y = groundH(x3, z3) if y3 is None else y3
    if sit: y += 0.30
    g.location = (x3, -z3, y)
    g.rotation_euler = (0, 0, rotz)
    hat = hat or HATS[people_count[0] % len(HATS)]
    keep = {'nonla': 'HatNonLa', 'beanie': 'HatBeanie', 'cap': 'HatCap'}.get(hat)
    for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
        h = find(objs, hn)
        if h: h.hide_render = (hn != keep)
    scarf = find(objs, 'Scarf')
    show_scarf = random.random() < 0.35
    if scarf: scarf.hide_render = not show_scarf
    shirt = srgb(random.choice(SHIRTS))
    own_mat(g, 'Shirt', shirt)
    own_mat(g, 'Beanie', shirt)
    own_mat(g, 'Pants', srgb(random.choice(PANTS)))
    if show_scarf: own_mat(g, 'Scarf', srgb(random.choice(SCARVES)))
    if sit:
        for nm in ('LegL', 'LegR'):
            leg = find(objs, nm)
            if leg: leg.rotation_euler.x = -1.45
        arm = find(objs, 'ArmR')
        if arm: arm.rotation_euler.x = -1.0
    people_count[0] += 1
    return g

def stool(x3, z3, y3, color):
    box("Stool", (0.34, 0.34, 0.30), (x3, -z3, y3 + 0.15), color)

STAIR_SITTERS = [(4.3, -5.5), (-4.4, -7.5), (4.5, -13), (-4.3, -16.5), (3.9, -20.6),
                 (-4.5, -20.9), (4.4, -25.5), (-4.2, -27.5), (-3.8, -4.5), (3.6, -10.5),
                 (-4.6, -24), (4.6, -18.3)]
for (sx, sz) in STAIR_SITTERS:
    stool(sx, sz, groundH(sx, sz), (0.10, 0.28, 0.60) if random.random() < 0.7 else (0.65, 0.15, 0.12))
    person(sx, sz, rotz=(random.random() - 0.5) * 0.5, sit=True)
for (sx, sz, rz) in [(-1.5, -6, math.pi), (2, -10, 0), (-2, -14, math.pi), (1.5, -18, 0),
                     (-1, -23, math.pi), (2.5, -26, 0), (-2.5, -29, math.pi), (0.5, -8, 0)]:
    person(sx, sz, rotz=rz)
for qx in (-36, -31, 22, 27):  # xếp hàng trước 4 sạp ăn mặt tiền
    for i in range(3):
        person(qx + (random.random() - 0.5) * 0.2, 5.85 - i * 0.48, rotz=(random.random() - 0.5) * 0.24)
for (wx, wz, rz) in [(-40, 1.5, 0), (-28, 2.5, math.pi), (-16, 1, 0), (-6, 2.8, math.pi),
                     (4, 1.2, 0), (14, 2.6, math.pi), (24, 1, 0), (34, 2.4, math.pi),
                     (44, 1.5, 0), (-48, 2, math.pi)]:
    person(wx, wz, rotz=rz)
for a in (0.3, 1.5, 2.9, 4.4, 5.6):  # quanh bùng binh r9.5
    person(-24 + math.cos(a) * 9.5, -6 + math.sin(a) * 9.5, rotz=-a, y3=0)
for (cx, cz) in ((-44, 6), (18, 10.8)):  # nhóm nói chuyện
    for i in range(3):
        a = i / 3 * math.pi * 2 + cx * 0.7
        person(cx + math.cos(a) * 0.55, cz + math.sin(a) * 0.55, rotz=-a)
for (hx, hz) in ((6, -52), (12, -48), (-4, -50), (-14, -44), (20, -54), (-24, -58)):
    person(hx, hz, rotz=random.random() * 6.28)
box("FortuneMat", (1.6, 1.2, 0.08), (2.8, 20.8, 11.37), (0.55, 0.16, 0.14))
person(2.8, -20.8, rotz=0, sit=True, y3=11.33)   # chú coi bói
person(1.8, -19.8, rotz=math.pi, y3=11.33)       # khách coi bói
for (qx, qz) in ((-42.1, 14.76), (10.85, 11.65), (44.25, 15.36)):  # khách ngồi quán
    stool(qx, qz, 0, (0.10, 0.28, 0.60))
    person(qx, qz, sit=True, y3=0)
person(31, -51, rotz=0, y3=17.5)  # ca sĩ trên sân khấu
for (ax, az) in ((27.5, -48.5), (29, -47.8), (26, -47.6)):
    stool(ax, az, 17, (0.65, 0.15, 0.12))
    person(ax, az, rotz=math.pi, sit=True, y3=17)
print("PEOPLE TOTAL:", people_count[0], flush=True)

# ---------------- ẢNH 1: TOÀN CẢNH NGÀY ----------------
make_sun()
BG = world_bg((0.55, 0.68, 0.85), 0.9)
sc.view_settings.exposure = 0.0
ARGS = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
camera((-88, -52, 52), (-2, 2, 3), lens=38)
sc.render.filepath = os.path.join(OUT, "v41-01-toan-canh-ngay.png" if not DRAFT else "v41-01-draft.png")
if 'nightonly' not in ARGS:
    bpy.ops.render.render(write_still=True)
    print("RENDERED v41-01", flush=True)
if 'dayonly' in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []):
    print("DAY ONLY — skip night", flush=True)
    sys.exit(0)

# ---------------- ẢNH 2: CHỢ ĐÊM ----------------
BG.inputs[0].default_value = (0.012, 0.02, 0.045, 1.0)
BG.inputs[1].default_value = 0.5
SUN.data.energy = 0.25
SUN.data.color = (0.55, 0.65, 0.9)
sc.view_settings.exposure = 0.35
bulb_mat = bpy.data.materials.new("BulbNight"); bulb_mat.use_nodes = True
bsdf = bulb_mat.node_tree.nodes["Principled BSDF"]
bsdf.inputs["Emission Color"].default_value = (1, 0.9, 0.7, 1)
bsdf.inputs["Emission Strength"].default_value = 8.0
for i, (lx, ly, lz) in enumerate(stall_lights):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.075, location=(lx, ly, lz), segments=8, ring_count=6)
    b = bpy.context.object
    b.data.materials.append(bulb_mat)
    if i % 2 == 0:
        point((lx, ly - 0.8, lz + 0.2), energy=70, dist=11)
all_objs = list(bpy.data.objects)
set_mat(all_objs, 'SignLetters', emission_strength=2.2)
set_mat(all_objs, 'MarketWin', emission_strength=0.7)
set_mat(all_objs, 'HotelWinA', emission_strength=1.4)
set_mat(all_objs, 'HotelWinB', emission_strength=0.5)
set_mat(all_objs, 'HeadLamp', emission_strength=1.5)
camera((-24, -6.5, 2.8), (6, 12, 5.5), lens=44)
sc.render.filepath = os.path.join(OUT, "v41-02-cho-dem.png" if not DRAFT else "v41-02-draft.png")
bpy.ops.render.render(write_still=True)
print("RENDERED v41-02", flush=True)
print("ALL V41 RENDERS DONE", flush=True)
