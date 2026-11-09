# -*- coding: utf-8 -*-
"""Render kiểm chứng V4.2 — HÀNH TRÌNH ĐI VÀO, toàn bộ chụp ĐÊM ẤM. — TOÀN CẢNH như web (2 cao độ, nhà lồng, thang + cầu,
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

def entryRampY(x):
    return min(2.0, (-52 - x) * 0.07) if x < -52 else 0.0

def groundH(x, z):
    if x < -52 and -5.5 <= z <= 10.5: return entryRampY(x)
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

# ================= V4.2: TRỤC ĐƯỜNG VÀO + PHÔNG ĐÀ LẠT =================
def emat(name, rgb, e_rgb, e_str, rough=0.6):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*rgb, 1)
    b.inputs["Emission Color"].default_value = (*e_rgb, 1)
    b.inputs["Emission Strength"].default_value = e_str
    b.inputs["Roughness"].default_value = rough
    return m
def ebox(name, size, loc, mat, rot=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rot: o.rotation_euler = rot
    o.data.materials.append(mat)
    return o
WinGlowM = emat("WinGlow", (0.45, 0.30, 0.12), (1.0, 0.70, 0.32), 2.0)
SignGlowM = emat("SignGlow", (0.55, 0.33, 0.10), (1.0, 0.60, 0.22), 2.6)
LantGlowM = emat("LantGlow", (0.98, 0.62, 0.16), (1.0, 0.58, 0.18), 3.2, rough=0.9)
WoodDarkM = mat_plain("WoodDark", (0.23, 0.15, 0.09))
TILT = math.atan2(2.0, 31.0)
# nền hậu cảnh lớn (không thấy mép thế giới)
box("BackGround", (480, 480, 0.2), (0, 0, -0.32), (0.13, 0.12, 0.10))
# mặt đường dốc + vỉa hè + vạch
ebox("EntryRoad", (31, 11, 0.22), (-67.5, -2.5, 1.0), mat_plain("AsphaltW", (0.16, 0.14, 0.12)), rot=(0, TILT, 0))
for sy in (-9.7, 4.7):
    ebox("Sidewalk", (31, 1.7, 0.3), (-67.5, sy, 1.06), mat_plain("WalkM", (0.42, 0.38, 0.33)), rot=(0, TILT, 0))
for dx in (-74, -64, -55):
    ebox("Dash", (2.2, 0.18, 0.03), (dx, -2.5, entryRampY(dx) + 0.14), mat_plain("DashM", (0.75, 0.72, 0.62)), rot=(0, TILT, 0))
def shophouse(x, ry, body_c, sign_c, h=6.0):
    ebox("ShopBody", (7.6, 5.2, h), (x, ry, h / 2), mat_plain("ShopB", body_c))
    ebox("ShopRoof", (8.2, 5.9, 0.35), (x, ry, h + 0.18), mat_plain("ShopR", (0.30, 0.16, 0.10)))
    sgn = 1 if ry < 0 else -1
    ebox("ShopSign", (5.6, 0.16, 0.95), (x, ry + sgn * 2.68, h - 0.9), SignGlowM)
    for i, wx in enumerate((-2.4, 0, 2.4)):
        for wz in (1.6, 3.6):
            ebox("ShopWin", (1.15, 0.1, 1.25), (x + wx, ry + sgn * 2.63, wz + 0.7), WinGlowM)
    ebox("ShopAwning", (7.0, 1.6, 0.1), (x, ry + sgn * 3.3, 2.6), mat_plain("AwnM", sign_c), rot=(sgn * 0.35, 0, 0))
shophouse(-60.5, -12.4, (0.62, 0.52, 0.40), (0.65, 0.20, 0.14), 6.4)
shophouse(-53.0, -12.4, (0.55, 0.46, 0.38), (0.16, 0.36, 0.55), 5.6)
shophouse(-38.5, -12.4, (0.66, 0.55, 0.42), (0.20, 0.45, 0.30), 6.0)
shophouse(-62.0, 13.7, (0.58, 0.48, 0.40), (0.55, 0.35, 0.16), 6.2)
shophouse(-52.0, 14.7, (0.52, 0.44, 0.36), (0.65, 0.20, 0.14), 5.8)
shophouse(-42.0, 13.7, (0.60, 0.50, 0.40), (0.16, 0.36, 0.55), 6.6)
# cổng chào tại spawn
for py in (-7.6, 2.6):
    ebox("GatePost", (0.55, 0.55, 5.2), (-81, py, 2.6), mat_plain("GateP", (0.35, 0.22, 0.12)))
ebox("GateBeam", (0.5, 10.8, 0.55), (-81, -2.5, 5.1), mat_plain("GateBm", (0.30, 0.19, 0.10)))
ebox("GateSign", (0.34, 8.2, 1.05), (-81, -2.5, 4.35), SignGlowM)
# phông đồi thông lớp lớp + tháp chuông hậu cảnh
def cone(x, y, r, h, c):
    bpy.ops.mesh.primitive_cone_add(radius1=r, radius2=0, depth=h, location=(x, y, h / 2 - 0.3), vertices=24)
    o = bpy.context.object; o.data.materials.append(mat_plain("RidgeM", c)); return o
for (cx, cy, cr, ch, cc) in [(-120, 150, 42, 30, (0.07, 0.10, 0.08)), (-70, 168, 48, 34, (0.06, 0.09, 0.07)),
                             (-20, 150, 40, 27, (0.07, 0.10, 0.08)), (30, 168, 46, 32, (0.06, 0.09, 0.07)),
                             (80, 150, 42, 29, (0.07, 0.10, 0.08)), (130, 162, 44, 30, (0.06, 0.09, 0.07)),
                             (-155, 55, 40, 26, (0.07, 0.10, 0.08)), (155, 45, 42, 28, (0.07, 0.10, 0.08)),
                             (60, -135, 46, 28, (0.07, 0.10, 0.08)), (-50, -140, 48, 30, (0.06, 0.09, 0.07)),
                             (-90, 106, 30, 21, (0.10, 0.14, 0.10)), (-14, 118, 34, 24, (0.09, 0.13, 0.09)),
                             (40, 106, 30, 20, (0.10, 0.14, 0.10)), (95, 112, 32, 22, (0.09, 0.13, 0.09))]:
    cone(cx, cy, cr, ch, cc)
# tháp chuông nhà thờ stylized tại render (-58, 118)
ebox("Tower", (4.6, 4.6, 19), (-66, 92, 9.5), mat_plain("TowerM", (0.16, 0.15, 0.17)))
bpy.ops.mesh.primitive_cone_add(radius1=3.6, radius2=0, depth=7.5, location=(-66, 92, 22.7), vertices=4)
bpy.context.object.data.materials.append(mat_plain("SpireM", (0.08, 0.08, 0.10)))
ebox("CrossV", (0.16, 0.16, 1.7), (-66, 92, 27.4), mat_plain("CrossM", (0.08, 0.08, 0.10)))
ebox("CrossH", (0.9, 0.16, 0.16), (-66, 92, 27.7), mat_plain("CrossM2", (0.08, 0.08, 0.10)))
for wz in (11.5, 14.5):
    ebox("TowerWin", (0.85, 0.12, 1.7), (-66, 89.6, wz), WinGlowM)
# cẩm tú cầu: cụm cầu hoa trên thảm lá
HydraCols = [(0.45, 0.52, 0.85), (0.62, 0.50, 0.85), (0.88, 0.62, 0.70), (0.55, 0.65, 0.95)]
def hydra(x, y, z):
    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.30, location=(x, y, z + 0.16), subdivisions=1)
    bpy.context.object.data.materials.append(mat_plain("HydLeaf", (0.13, 0.26, 0.12)))
    for i in range(3):
        bpy.ops.mesh.primitive_ico_sphere_add(radius=0.15 + 0.04 * (i % 2), location=(x + (i - 1) * 0.17, y + (0.1 if i == 1 else -0.05), z + 0.34), subdivisions=1)
        bpy.context.object.data.materials.append(mat_plain("HydF", HydraCols[(int(x) + i) % 4]))
for (hx, hy, hz) in [(-72, -9.0, 1.9), (-64, -9.0, 1.4), (-56, -9.0, 0.95), (-47, -9.0, 0.55),
                     (-70, 4.0, 1.75), (-61, 4.0, 1.25), (-52, 4.0, 0.8),
                     (-32, -3.4, 0), (-16, -3.6, 0), (-30, 14.5, 0), (-18, 14.2, 0),
                     (-8, 33, 17), (12, 33, 17), (24, 40, 17), (-20, 44, 17)]:
    hydra(hx, hy, hz)
ENTRY_LAMPS = [(-72, -8.8), (-60, -8.8), (-48, -8.8), (-72, 3.8), (-58, 3.8), (-44, 3.8)]
# sương: vật liệu trong suốt pha
def fogmat():
    m = bpy.data.materials.new("FogM"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    mix = nt.nodes.new("ShaderNodeMixShader"); mix.inputs[0].default_value = 0.86
    tr = nt.nodes.new("ShaderNodeBsdfTransparent")
    pr = nt.nodes.new("ShaderNodeBsdfPrincipled")
    pr.inputs["Base Color"].default_value = (0.85, 0.78, 0.68, 1)
    pr.inputs["Roughness"].default_value = 1.0
    nt.links.new(tr.outputs[0], mix.inputs[1]); nt.links.new(pr.outputs[0], mix.inputs[2])
    nt.links.new(mix.outputs[0], out.inputs[0])
    return m
FogM = fogmat()
def fogplane(x, y, z, w, d, vert=False):
    bpy.ops.mesh.primitive_plane_add(size=1, location=(x, y, z))
    o = bpy.context.object; o.scale = (w, d, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if vert: o.rotation_euler = (math.pi / 2, 0, 0)
    o.data.materials.append(FogM); return o
fogplane(-58, -2, 0.75, 32, 15); fogplane(-24, 0, 0.5, 27, 27)
fogplane(24, -6, 0.6, 21, 13); fogplane(0, 50, 18.35, 38, 20)
print("SECTION entry+backdrop done", flush=True)

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
    ("HotelD", (-70, -15.5, 0), math.pi), ("HotelB", (66, -8, 0), -math.pi / 2),
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
    (-56, 8.4, math.pi, 0.28, ''), (-49.5, 8.4, math.pi, 0, ''),   # V4.2: 2 sạp đường vào
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
for (lx, ly) in ENTRY_LAMPS:
    g = dup_tree(lamp_tpl); g.location = (lx, ly, entryRampY(lx))
# thông lớn trên sườn đồi sau quảng trường (lớp gần của phông)
pine_tpl = make_template("pine.glb", "PineTpl")
for (px, py, ps) in [(-52, 96, 2.8), (-20, 100, 3.2), (8, 97, 2.6), (-78, 99, 3.0), (30, 102, 2.9), (58, 98, 2.7)]:
    g = dup_tree(pine_tpl); g.location = (px, py, 9.5); g.scale = (ps, ps, ps)
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
for (vx, vy, rz) in ((-62, -0.6, math.pi / 2), (-44, -3.9, -math.pi / 2)):  # xe chạy trên dốc đường vào
    g = dup_sub(moto_tpl)
    g.location = (vx, vy, entryRampY(vx)); g.rotation_euler = (0, 0, rz)
    paint_vehicle(g)
for vx in (-70, -57, -45):  # xe đậu dọc lề nam đường vào
    g = dup_sub(moto_tpl)
    g.location = (vx, -7.7, entryRampY(vx)); g.rotation_euler = (0, 0, 0.12)
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
# --- V4.2: đám đông DÀY NHẤT dọc trục hành trình ---
for (wx, wz, rz) in [(-72, 2, -math.pi / 2), (-68, 4.6, math.pi / 2), (-63, 0.2, -math.pi / 2), (-59, 3.4, math.pi / 2),
                     (-54, 6.2, -math.pi / 2), (-47, 0.8, math.pi / 2), (-43, 5.2, -math.pi / 2), (-38, 2.2, math.pi / 2),
                     (-35, -1, 0), (-30, 3.6, math.pi)]:
    person(wx, wz, rotz=rz)
for qx in (-56, -49.5):  # hàng chờ 2 sạp mới đường vào
    for i in range(2):
        person(qx + (random.random() - 0.5) * 0.3, 5.85 - i * 0.48, rotz=math.pi + (random.random() - 0.5) * 0.2)
for (sx2, sz2) in ((-60.5, 9.9), (-52.5, 9.9), (-64, 9.7)):  # khách ngồi trước nhà phố + hàng rong ngồi
    stool(sx2, sz2, groundH(sx2, sz2), (0.10, 0.28, 0.60))
    person(sx2, sz2, rotz=math.pi, sit=True)
for i in range(3):  # nhóm chat vỉa hè
    a = i / 3 * math.pi * 2 + 0.5
    person(-66 + math.cos(a) * 0.55, 5.6 + math.sin(a) * 0.55, rotz=-a)
for a in (0.9, 2.2, 3.6, 5.1):  # thêm người quanh bùng binh
    person(-24 + math.cos(a) * 9.5, -6 + math.sin(a) * 9.5, rotz=-a, y3=0)
person(24.5, 5.9, rotz=math.pi)  # người chơi đứng trước sạp sữa (cho ảnh cận sạp)
print("PEOPLE TOTAL:", people_count[0], flush=True)

# ================= V4.2: GRADE ĐÊM ẤM + 5 ẢNH HÀNH TRÌNH =================
# (bản tối ưu: dựng prop đêm bằng data API + mesh dùng chung — tránh bpy.ops hàng loạt
#  vì mỗi ops kích hoạt depsgraph eval trên cảnh ~6.000 object, rất chậm)
make_sun(euler=(math.radians(65), 0, math.radians(30)), energy=0.22)
SUN.data.color = (1.0, 0.72, 0.45)
BG = world_bg((0.032, 0.020, 0.009), 0.5)
sc.view_settings.exposure = 0.30
bulb_mat = bpy.data.materials.new("BulbNight"); bulb_mat.use_nodes = True
_bb = bulb_mat.node_tree.nodes["Principled BSDF"]
_bb.inputs["Emission Color"].default_value = (1, 0.88, 0.62, 1)
_bb.inputs["Emission Strength"].default_value = 8.0
def _octa(name, mat):
    v = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    f = [(4,0,2),(4,2,1),(4,1,3),(4,3,0),(5,2,0),(5,1,2),(5,3,1),(5,0,3)]
    m = bpy.data.meshes.new(name); m.from_pydata(v, [], f); m.update()
    if mat: m.materials.append(mat)
    return m
def _cube(name, mat):
    v = [(-.5,-.5,-.5),(.5,-.5,-.5),(.5,.5,-.5),(-.5,.5,-.5),(-.5,-.5,.5),(.5,-.5,.5),(.5,.5,.5),(-.5,.5,.5)]
    f = [(0,1,2,3),(4,0,3,7),(1,5,6,2),(5,4,7,6),(3,2,6,7),(4,5,1,0)]
    m = bpy.data.meshes.new(name); m.from_pydata(v, [], f); m.update()
    if mat: m.materials.append(mat)
    return m
OCTA_BULB = _octa("OctaBulb", bulb_mat)
OCTA_LANT = _octa("OctaLant", LantGlowM)
OCTA_FOG = _octa("OctaFog", FogM)
CUBE_WOOD = _cube("CubeWood", WoodDarkM)
CUBE_SIGN = _cube("CubeSign", SignGlowM)
CUBE_TASS = _cube("CubeTass", mat_plain("TassM2", (0.62, 0.10, 0.08)))
def put(mesh, loc, scale=(1, 1, 1)):
    o = bpy.data.objects.new("P", mesh)
    bpy.context.collection.objects.link(o)
    o.location = loc; o.scale = scale
    return o
for i, (lx, ly, lz) in enumerate(stall_lights):
    put(OCTA_BULB, (lx, ly, lz), (0.075, 0.075, 0.075))
    if i % 2 == 0:
        point((lx, ly - 0.8, lz + 0.2), (1.0, 0.72, 0.38), energy=80, dist=12)
for (lx, ly) in ENTRY_LAMPS:
    lz = entryRampY(lx)
    put(OCTA_BULB, (lx, ly, lz + 3.35), (0.10, 0.10, 0.10))
    point((lx, ly, lz + 3.3), (1.0, 0.70, 0.36), energy=65, dist=14)
_EM = {'SignLetters': 2.4, 'MarketWin': 0.8, 'HotelWinA': 1.6, 'HotelWinB': 0.6, 'HeadLamp': 1.6}
for m in bpy.data.materials:
    base = m.name.split('.')[0]
    if base in _EM and m.use_nodes:
        m.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = _EM[base]
print("TAIL lights done", flush=True)
# mô phỏng lớp web BÁM ẢNH CHỐT: biển lớn phát sáng + lồng đèn giấy lớn + tua đỏ trên dãy sạp mặt đường
for (sx, sz, ry, by, tag) in STALLS:
    if sz != 8.4: continue
    fy = -sz - 1.05
    put(CUBE_WOOD, (sx, fy + 0.30, by + 2.52), (4.2, 0.14, 0.98))
    put(CUBE_SIGN, (sx, fy + 0.20, by + 2.52), (3.9, 0.05, 0.70))
    for (dx, hh) in ((-1.3, 3.05), (0.0, 3.44), (1.3, 3.02)):
        put(OCTA_LANT, (sx + dx, fy - 0.15, by + hh), (0.21, 0.21, 0.27))
        put(CUBE_TASS, (sx + dx, fy - 0.15, by + hh - 0.36), (0.035, 0.035, 0.24))
for (r, hz) in ((0.34, 1.7), (0.5, 2.35), (0.68, 3.05)):  # cột hơi trên sạp sữa (22)
    put(OCTA_FOG, (22.4, -7.3, hz), (r, r, r * 0.8))
print("TAIL facade props done", flush=True)
for (px, py, pz, pe) in ((0, 10, 7.5, 70), (0, 20, 13.5, 70), (0, 30, 18.5, 60), (31, 50, 20.5, 95)):
    point((px, py, pz), (1.0, 0.72, 0.38), energy=pe, dist=17)
SHOTS = [
    ("a-duong-vao", (-79.5, -2.2, 3.8), (-4, -10, 1.0), 44),
    ("b-vong-xoay", (-36, 12, 5.5), (16, -16, 2.2), 44),
    ("c-bac-thang", (24, -20, 17), (-2, 26, 11), 50),
    ("d-doi-thong", (30, -30, 26), (-40, 120, 14), 40),
    ("e-can-sap", (18.5, -1.8, 2.6), (30, -9.5, 1.2), 42),
]
_only = [x for a in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []) if a.startswith('only=') for x in a.split('=')[1].split(',')]
for (nm, cl, ct, ln) in SHOTS:
    if _only and nm.split('-')[0] not in _only: continue
    camera(cl, ct, lens=ln)
    sc.render.filepath = os.path.join(OUT, ("v42-%s-dem.png" % nm) if not DRAFT else ("v42-%s-draft.png" % nm))
    bpy.ops.render.render(write_still=True)
    print("RENDERED v42", nm, flush=True)
print("ALL V42 SHOTS DONE", flush=True)
