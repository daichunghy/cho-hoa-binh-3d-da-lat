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
import bpy, bmesh, math, mathutils, os, random, sys
from mathutils import Vector

random.seed(42)
DRAFT = 'draft' in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
print("V45 MODE:", "draft" if DRAFT else "full", flush=True)
HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

# ---------------- hàm chiều cao mặt đất (port từ index.html) ----------------
def stairH(z):
    # V4.5: chiếu nghỉ sâu 4 + SỬA LỖI DẤU t (khớp index.html — u đo từ đỉnh chuyến)
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
        t = (z - 12) / 6.4
        s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
        return 12.6 - 6.05 * min(1.0, s)
    if z <= 20.4: return 6.55
    t = (z - 20.4) / 6.4
    s = min(1.0, math.floor(t * 10) / 10.0 + (0.1 if t >= 0.999 else 0.0))
    return 6.55 - 6.05 * min(1.0, s)

def entryRampY(x):
    return min(2.0, (-52 - x) * 0.07) if x < -52 else 0.0

def groundH(x, z):
    if 14.5 <= x <= 20.5 and -30 <= z <= 9: return 17.14 - (z + 30) * 0.11282
    if 29 <= x <= 33 and 12 <= z <= 26.8: return innerStairH(z)
    if 14 <= x <= 21 and 7 <= z <= 12: return 12.6
    if 21 <= x <= 33 and 7 <= z <= 12.2: return 12.6
    if -34 <= x <= 34 and 12 <= z <= 28: return 0.5
    if x < -52 and -9 <= z <= 13.5: return entryRampY(x)  # V4.7
    if z <= -30: return 17.0
    if z >= -2: return 0.0
    if -11 <= x <= 11: return stairH(z)
    if (-19 <= x < -11) or (11 < x < 14.5):
        if z > -8.25: return 2.8
        if z > -18.75: return 8.5
        return 14.2
    if -45 <= x < -19 and -30 < z < -2:  # V4.8: them phang quanh dao (khop web)
        if z >= -16: return 0.0
        return 17 * ((-16 - z) / 14.0)
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
box("Road", (170, 18, 0.22), (0, -1.5, 0.0), (0.26, 0.26, 0.27))  # V4.7: rong 18
box("Hill", (150, 52, 17), (0, 56, 8.5), (0.42, 0.38, 0.34))
box("Hilltop", (150, 52, 0.2), (0, 56, 17.05), (0.55, 0.52, 0.46))
box("Grass", (150, 10, 0.22), (0, 76, 17.06), (0.34, 0.42, 0.29))
for (x0, x1) in ((-70, -19), (20.5, 70)):
    w = x1 - x0
    box("Slope", (w, 34.5, 0.3), ((x0 + x1) / 2, 16, 8.4), (0.40, 0.46, 0.35),
        rot=(math.atan2(17, 28), 0, 0))
# sườn tây rút về phía bắc (render y 14..33) để không chôn đảo bùng binh
# (đảo nằm trên plaza phẳng như bản web; box Slope tạo bởi script này chỉ là mô phỏng địa hình)
for o in list(bpy.data.objects):
    if o.name.startswith("Slope") and o.location.x < -30:
        bpy.data.objects.remove(o, do_unlink=True)
# V4.8: suon tay 2 doan - (a) x -70..-45 doc goc; (b) x -45..-19 THOAI ve bac
# (chi con render y 16..30, doc hon) khop them phang quanh dao cua web
box("SlopeW1", (25, 34.5, 0.3), (-57.5, 16, 8.4), (0.40, 0.46, 0.35),
    rot=(math.atan2(17, 28), 0, 0))
box("SlopeW2", (26, 22.02, 0.3), (-32, 23, 8.5), (0.40, 0.46, 0.35),
    rot=(math.atan2(17, 14), 0, 0))
# V4.5: thềm bậc thang 2 bên sườn (hộp đặc + tấm lát) — khớp groundH web
for (bx0, bx1) in ((-19, -11), (11, 14.5)):
    bw = bx1 - bx0; bcx = (bx0 + bx1) / 2
    for (top, zc, dd) in ((14.2, -24.375, 11.25), (8.5, -13.5, 10.5), (2.8, -5.125, 6.25)):
        box("Terr", (bw, dd, top + 1), (bcx, -zc, (top - 1) / 2), (0.40, 0.46, 0.35))
        box("TerrTop", (bw - 0.15, dd - 0.15, 0.05), (bcx, -zc, top + 0.02), (0.54, 0.50, 0.45))
# V4.5: thang phụ cầu vồng sườn đông
RB45 = [(0.76, 0.23, 0.18), (0.88, 0.48, 0.16), (0.91, 0.78, 0.20), (0.29, 0.60, 0.29),
        (0.18, 0.48, 0.72), (0.35, 0.29, 0.60), (0.60, 0.29, 0.48), (0.76, 0.23, 0.18)]
for i in range(8):
    zz = -5 - i * 2.9; yy = 17 * ((-2 - zz) / 28) + 0.10
    box("Rainbow", (3.4, 1.6, 0.18), (22.4, -zz, yy), RB45[i], rot=(math.atan2(17, 28), 0, 0))

# ---------------- công trình ----------------
imp("market.glb", (0, -20, 0))
imp("theater.glb", (-19, 56, 17))
imp("cafe.glb", (13, 60, 17))
imp("stairs.glb", (0, 16, 0))
imp("roundabout.glb", (-24, 6, 0))
# V4.8: vanh duong nhua quanh dao (guong web)
bpy.ops.mesh.primitive_cylinder_add(radius=16, depth=0.05, location=(-24, 6, 0.135), vertices=40)
_rd = bpy.context.object; _rd.name = "RingRoad"; _rd.data.materials.append(mat_plain("RingRoadM", (0.26, 0.24, 0.22)))
imp("bridge.glb", (17.5, 10.5, 14.65), rotx=math.atan2(4.4, 39))
imp("pier.glb", (17.5, 2, 0), scale=(0.78, 0.78, 13.4))
imp("pier.glb", (17.5, 16, 0), scale=(0.78, 0.78, 15.0))
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
ebox("EntryRoad", (31, 18, 0.22), (-67.5, -1.5, 1.0), mat_plain("AsphaltW", (0.16, 0.14, 0.12)), rot=(0, TILT, 0))  # V4.7
for sy in (-9.7, 4.7):
    ebox("Sidewalk", (31, 1.7, 0.3), (-67.5, sy, 1.06), mat_plain("WalkM", (0.42, 0.38, 0.33)), rot=(0, TILT, 0))
for dx in (-74, -64, -55):
    ebox("Dash", (2.2, 0.18, 0.03), (dx, -2.5, entryRampY(dx) + 0.14), mat_plain("DashM", (0.75, 0.72, 0.62)), rot=(0, TILT, 0))
def shophouse(x, ry, body_c, sign_c, h=6.0, z0=0):
    ebox("ShopBody", (7.6, 5.2, h), (x, ry, z0 + h / 2), mat_plain("ShopB", body_c))
    ebox("ShopRoof", (8.2, 5.9, 0.35), (x, ry, z0 + h + 0.18), mat_plain("ShopR", (0.30, 0.16, 0.10)))
    sgn = 1 if ry < 0 else -1
    ebox("ShopSign", (5.6, 0.16, 0.95), (x, ry + sgn * 2.68, z0 + h - 0.9), SignGlowM)
    for i, wx in enumerate((-2.4, 0, 2.4)):
        for wz in (1.6, 4.65, 7.7, 10.75):
            if wz > h - 1.8: continue
            ebox("ShopWin", (1.15, 0.1, 1.25), (x + wx, ry + sgn * 2.63, z0 + wz + 0.7), WinGlowM)
    ebox("ShopAwning", (7.0, 1.6, 0.1), (x, ry + sgn * 3.3, z0 + 2.6), mat_plain("AwnM", sign_c), rot=(sgn * 0.35, 0, 0))
shophouse(-60.5, -16.5, (0.62, 0.52, 0.40), (0.65, 0.20, 0.14), 15.85)
shophouse(-53.0, -16.5, (0.55, 0.46, 0.38), (0.16, 0.36, 0.55), 12.8)
shophouse(-38.5, -16.5, (0.66, 0.55, 0.42), (0.20, 0.45, 0.30), 15.85)
shophouse(-62.0, 15.2, (0.58, 0.48, 0.40), (0.55, 0.35, 0.16), 12.8, z0=8.0)
shophouse(-52.0, 16.0, (0.52, 0.44, 0.36), (0.65, 0.20, 0.14), 15.85, z0=8.5)
shophouse(-42.0, 15.2, (0.60, 0.50, 0.40), (0.16, 0.36, 0.55), 12.8, z0=0)
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
for (hx, hy, hz) in [(-72, -13.6, 1.9), (-64, -13.6, 1.4), (-56, -13.6, 0.95), (-47, -13.6, 0.55),
                     (-70, 10.4, 1.75), (-61, 10.4, 1.25), (-52, 10.4, 0.8),
                     (-32, -3.4, 0), (-16, -3.6, 0), (-30, 14.5, 0), (-18, 14.2, 0),
                     (-8, 33, 17), (12, 33, 17), (24, 40, 17), (-20, 44, 17)]:
    hydra(hx, hy, hz)
ENTRY_LAMPS = [(-72, -11.9), (-60, -11.9), (-48, -11.9), (-72, 8.6), (-58, 8.6), (-44, 8.6)]  # V4.7
# sương: vật liệu trong suốt pha
def fogmat():
    m = bpy.data.materials.new("FogM"); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    mix = nt.nodes.new("ShaderNodeMixShader"); mix.inputs[0].default_value = 0.80
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
fogplane(0, -10.5, 1.1, 42, 11); fogplane(-24, 6, 0.85, 30, 30)
fogplane(24, -6, 0.6, 21, 13); fogplane(0, 50, 18.35, 38, 20)
fogplane(-56, -2, 1.0, 44, 16); fogplane(0, -2, 0.8, 34, 12)  # V4.7: sương ngang đường vào + chân thang
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
    (-36, 10.15, math.pi, 0, 'grill'), (-31, 10.15, math.pi, 0, ''), (-26, 10.15, math.pi, 0, ''),
    (-21, 10.15, math.pi, 0, ''), (22, 10.15, math.pi, 0, ''), (27, 10.15, math.pi, 0, 'phin'),
    (32, 10.15, math.pi, 0, ''), (37.5, 10.15, math.pi, 0, ''),
    (-24, 15, 0, 0.5, ''), (16, 15, 0, 0.5, ''), (-16, 23.5, math.pi, 0.5, ''), (24, 23.5, math.pi, 0.5, ''),
    (-20, 20, math.pi, 0.5, ''), (20, 20, 0, 0.5, ''),   # V4.5: đặc sản + trà dời vào nhà lồng
    (6.2, -21.6, math.pi / 2, 11.33, ''), (6.2, -10.4, math.pi / 2, 5.67, ''),  # V4.5: 2 sạp chiếu nghỉ
    (-6, -47, 0, 17, ''), (-31, -47, 0, 17, ''),
    (-12, 3, 0, 0, ''), (6, 3, 0, 0, ''), (30, 3, 0, 0, ''), (-38, 3, 0, 0, ''),
    (-56, 10.15, math.pi, 0.28, ''), (-49.5, 10.15, math.pi, 0, ''),   # V4.2: 2 sạp đường vào
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
# V4.8 POLISH (gương web): thông + đèn trên sườn tây — phá mảng tường phẳng ở góc A
for (px, py, pz, ps) in [(-40, 26, 12.14, 1.05), (-33, 20, 4.86, 0.9), (-27, 27, 13.36, 1.1), (-22, 21, 6.07, 0.85)]:
    g = dup_tree(pine_tpl); g.location = (px, py, pz); g.scale = (ps, ps, ps)
for (lx, ly, lz) in [(-36, 17, 1.21), (-24, 17, 1.21)]:
    g = dup_tree(lamp_tpl); g.location = (lx, ly, lz)
print("SECTION stalls done", flush=True)

# sân khấu đồi
box("Stage", (8, 5, 0.5), (31, 52, 17.25), (0.45, 0.33, 0.22))
box("StageBack", (8, 0.3, 3.2), (31, 54.6, 18.6), (0.30, 0.22, 0.16))

# ================= V4.5: GƯƠNG HÌNH HỌC (nhà lồng / thang trong nhà / vành đồi) =================
# (data-API thuần, KHÔNG bpy.ops — cảnh đã ~5.000 object, mỗi ops rất chậm)
_CV = [(-.5,-.5,-.5),(.5,-.5,-.5),(.5,.5,-.5),(-.5,.5,-.5),(-.5,-.5,.5),(.5,-.5,.5),(.5,.5,.5),(-.5,.5,.5)]
_CF = [(0,1,2,3),(4,0,3,7),(1,5,6,2),(5,4,7,6),(3,2,6,7),(4,5,1,0)]
_cmesh_cache = {}
def cbox(size, loc, rgb=None, mat=None, rot=None):
    key = mat.name if mat is not None else rgb
    m = _cmesh_cache.get(key)
    if m is None:
        m = bpy.data.meshes.new("CB45")
        m.from_pydata(_CV, [], _CF); m.update()
        m.materials.append(mat if mat is not None else mat_plain("CB45M", rgb))
        _cmesh_cache[key] = m
    o = bpy.data.objects.new("CB45", m)
    bpy.context.collection.objects.link(o)
    o.location = loc; o.scale = size
    if rot: o.rotation_euler = rot
    return o
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
    cbox((3.6, 0.05, 0.95), (rx + fx * 0.62, -(rz + fz * 0.62), 3.05), (0.80, 0.72, 0.55))  # biển kem chữ đỏ (web: canvas, KHÔNG phát sáng)
    cbox((4.4, 1.55, 0.08), (rx + fx * 0.25, -(rz + fz * 0.25), 2.35), AWN45[qn % 6])
print("V45 counters:", qn, flush=True)
cbox((56, 0.95, 0.3), (0, -26.95, 3.55), (0.43, 0.40, 0.35))
cbox((56, 0.08, 1.1), (0, -26.55, 4.35), (0.56, 0.71, 0.79))
cbox((56, 0.09, 0.09), (0, -26.55, 4.95), (0.42, 0.29, 0.19))
cbox((12, 5.2, 0.35), (27, -9.6, 12.42), (0.54, 0.50, 0.45))
cbox((0.35, 15.2, 13.2), (28.82, -19.4, 6.85), (0.43, 0.40, 0.35))
for i in range(10):
    cbox((4, 0.72, 0.28), (31, -(12 + 0.64 * i + 0.32), (12.6 - 6.05 * i / 10) - 0.14), (0.54, 0.50, 0.45))
    cbox((4, 0.72, 0.28), (31, -(20.4 + 0.64 * i + 0.32), (6.55 - 6.05 * i / 10) - 0.14), (0.54, 0.50, 0.45))
cbox((4, 2.0, 0.3), (31, -19.4, 6.4), (0.54, 0.50, 0.45))
cbox((1.7, 2.2, 0.1), (32.1, -19.4, 7.0), (0.48, 0.29, 0.18))
for i, cc in enumerate([(0.76, 0.23, 0.18), (0.91, 0.78, 0.20), (0.18, 0.48, 0.72), (0.88, 0.48, 0.16), (0.60, 0.29, 0.48), (0.29, 0.60, 0.29)]):
    cbox((0.3, 0.1, 0.62), (31.35, -(18.65 + i * 0.31), 7.28), cc)
cbox((0.05, 1.5, 0.5), (32.1, -19.4, 8.25), (0.80, 0.72, 0.55))
def rim_cafe(cx, cz, awn):
    cbox((5.4, 3.8, 0.18), (cx, -cz, 17.09), (0.54, 0.35, 0.22))
    cbox((5.4, 0.18, 2.2), (cx, -(cz - 1.8), 18.1), (0.30, 0.20, 0.16))
    cbox((5.6, 4.0, 0.14), (cx, -cz, 19.35), awn)
    cbox((4.2, 0.7, 0.85), (cx, -(cz - 1.15), 17.55), (0.42, 0.29, 0.19))
    for tx in (-1.5, 1.3):
        cbox((0.84, 0.84, 0.06), (cx + tx, -(cz + 0.35), 17.85), (0.94, 0.92, 0.85))
rim_cafe(-17, -32.5, (0.48, 0.29, 0.18))
rim_cafe(17.5, -32.5, (0.35, 0.42, 0.27))
for (kx, kz, kc) in ((-12.8, -35.5, (0.78, 0.22, 0.18)), (12, -35, (0.18, 0.43, 0.64)), (-24, -37, (0.91, 0.53, 0.18))):
    cbox((2.6, 2.2, 2.0), (kx, -kz, 18.0), (0.46, 0.32, 0.18))
    cbox((2.9, 2.5, 0.12), (kx, -kz, 19.1), kc)
for rcx in (-15.25, 15.25):
    cbox((7.5, 0.1, 0.1), (rcx, 30.4, 18.05), (0.42, 0.29, 0.19))
for (sx, sz, sc45) in ((-8.6, -15.2, (0.76, 0.23, 0.18)), (8.6, -5.6, (0.85, 0.49, 0.18))):
    yy = stairH(sz)
    cbox((1.5, 0.8, 0.75), (sx, -sz, yy + 0.45), (0.54, 0.37, 0.23))
    cbox((1.7, 1.0, 0.08), (sx, -sz, yy + 1.62), sc45)
for (vx, vz) in ((-15.5, -27.5), (-13.2, -20.5), (-16.5, -15.5), (-13.8, -11), (-15.2, -6.5), (-16.8, -3.8), (12.7, -27), (12.9, -15), (12.6, -6)):
    vy = groundH(vx, vz)
    cbox((2.0, 1.5, 0.04), (vx, -vz, vy + 0.04), (0.48, 0.55, 0.35))
    cbox((0.6, 0.5, 0.3), (vx - 0.3, -vz, vy + 0.16), (0.88, 0.48, 0.16))
    cbox((0.5, 0.45, 0.26), (vx + 0.4, -(vz + 0.2), vy + 0.14), (0.42, 0.60, 0.29))
print("V45 geometry mirrors done", flush=True)

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

# V4.8: vanh XE DAU quanh dao R10.5 (guong web - bo xe chay vong dao)
for deg in (20, 45, 70, 95, 120, 150, 180, 205, 225):
    a = math.radians(deg)
    g = dup_sub(moto_tpl)
    g.location = (-24 + math.cos(a) * 12.6, 6 - math.sin(a) * 12.6, 0)  # render y = -three z
    g.rotation_euler = (0, 0, -a)
    hide_rider(g); paint_vehicle(g)
for (px, pz) in ((-40.2, -8), (-40.8, -3), (-40.2, 2.5)):  # 3 o to dau phia tay dao (three)
    g = dup_sub(car_tpl)
    g.location = (px, -pz, 0)
    g.rotation_euler = (0, 0, 0)
    paint_vehicle(g)
for (vx, vy, rz) in ((-50, 1.5, math.pi / 2), (5, 1.5, math.pi / 2), (-15, -4.5, -math.pi / 2), (45, -4.5, -math.pi / 2)):  # V4.7
    g = dup_sub(moto_tpl)
    g.location = (vx, vy, 0); g.rotation_euler = (0, 0, rz)
    paint_vehicle(g)
g = dup_sub(car_tpl)
g.location = (30, -4.5, 0); g.rotation_euler = (0, 0, -math.pi / 2)  # V4.7
for gx in range(-46, 47):  # bãi xe đậu trước chợ (three z=11.25 -> render y=-11.25)
    x = gx * 1.0
    if -5.5 < x < 5.5 or x < -40 or x > 41: continue
    if random.random() < 0.18: continue
    g = dup_sub(moto_tpl)
    g.location = (x + (random.random() - 0.5) * 0.15, -11.75 + (random.random() - 0.5) * 0.12, 0)  # V4.7
    g.rotation_euler = (0, 0, (random.random() - 0.5) * 0.12)
    hide_rider(g); paint_vehicle(g)
for (vx, vy, rz) in ((-62, -0.6, math.pi / 2), (-44, -3.9, -math.pi / 2)):  # xe chạy trên dốc đường vào
    g = dup_sub(moto_tpl)
    g.location = (vx, vy, entryRampY(vx)); g.rotation_euler = (0, 0, rz)
    paint_vehicle(g)
for vx in (-76, -72, -68, -64, -60, -56):  # V4.7: xe đậu vệ nam đường vào (web z=9.9)
    g = dup_sub(moto_tpl)
    g.location = (vx, -9.9, entryRampY(vx)); g.rotation_euler = (0, 0, 0.12)
    hide_rider(g); paint_vehicle(g)
for vx in (-74, -70, -66, -62, -58, -54):  # V4.7: xe đậu vệ bắc đường vào (web z=-7.2)
    g = dup_sub(moto_tpl)
    g.location = (vx, 7.2, entryRampY(vx)); g.rotation_euler = (0, 0, 0.12)
    hide_rider(g); paint_vehicle(g)
for vx in (42, 45.5, 49):  # V4.7: xe đậu phía đông trước chợ (web z=8.9)
    g = dup_sub(moto_tpl)
    g.location = (vx, -8.9, 0); g.rotation_euler = (0, 0, 0.1)
    hide_rider(g); paint_vehicle(g)
print("SECTION vehicles done", flush=True)

# ================= V4.9 MỤC 7: GƯƠNG CHI TIẾT + BỐ CỤC (biển/giá/bày hàng/dây đèn/kiến trúc) =================
M7D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "renders", "m7")
def tex_mat(name, path, emis=0.30, rep=(1, 1)):
    img = bpy.data.images.load(path)
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; bsdf = nt.nodes["Principled BSDF"]
    tex = nt.nodes.new("ShaderNodeTexImage"); tex.image = img
    mp = nt.nodes.new("ShaderNodeMapping"); mp.inputs["Scale"].default_value = (rep[0], rep[1], 1)
    tc = nt.nodes.new("ShaderNodeTexCoord")
    nt.links.new(tc.outputs["UV"], mp.inputs["Vector"])
    nt.links.new(mp.outputs["Vector"], tex.inputs["Vector"])
    nt.links.new(tex.outputs["Color"], bsdf.inputs["Base Color"])
    nt.links.new(tex.outputs["Color"], bsdf.inputs["Emission Color"])
    bsdf.inputs["Emission Strength"].default_value = emis
    bsdf.inputs["Roughness"].default_value = 0.9
    return m
def tplaneV(name, w, h, loc, mt, flip=False):
    verts = [(-w / 2, 0, -h / 2), (-w / 2, 0, h / 2), (w / 2, 0, h / 2), (w / 2, 0, -h / 2)]
    if flip:
        faces = [(0, 3, 2, 1)]; uvs = [(0, 0), (0, 1), (1, 1), (1, 0)]
    else:
        faces = [(0, 1, 2, 3)]; uvs = [(1, 0), (1, 1), (0, 1), (0, 0)]
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces); me.update()
    uv = me.uv_layers.new(name="UV")
    for li, loop in enumerate(me.loops):
        uv.data[li].uv = uvs[loop.vertex_index]
    me.materials.append(mt)
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    ob.location = loc
    return ob
_GRP = {}
def _grp(kind, rgb, emis):
    key = (kind, rgb, emis)
    if key not in _GRP: _GRP[key] = bmesh.new()
    return _GRP[key]
def sph(loc, r, rgb, sxyz=(1, 1, 1), emis=None):
    bm = _grp("s", rgb, emis)
    for v in bmesh.ops.create_icosphere(bm, subdivisions=1, radius=r)["verts"]:
        v.co.x = loc[0] + v.co.x * sxyz[0]; v.co.y = loc[1] + v.co.y * sxyz[1]; v.co.z = loc[2] + v.co.z * sxyz[2]
def cylM(loc, r, h, rgb, emis=None):
    bm = _grp("c", rgb, emis)
    for v in bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=r, radius2=r, depth=h)["verts"]:
        v.co.x += loc[0]; v.co.y += loc[1]; v.co.z += loc[2]
def flush_grp():
    for (kind, rgb, emis), bm in _GRP.items():
        me = bpy.data.meshes.new("M7G"); bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new("M7G", me); bpy.context.collection.objects.link(ob)
        if emis is None:
            me.materials.append(mat_plain("M7GM", rgb))
        else:
            me.materials.append(emat("M7GE", rgb, emis[0], emis[1]))
def L2W(sx, sz, ry, by, lx, ly, lz):
    wx = sx + lx * math.cos(ry) + lz * math.sin(ry)
    wz = sz - lx * math.sin(ry) + lz * math.cos(ry)
    return (wx, -wz, by + ly)
STEEL = srgb("b9c0c4"); WOOD = srgb("8a6a42"); CLAYC = srgb("6a4630"); PAPER = srgb("ffc46b")
SPILL = {"food": ["d8542e", "e8c33c", "f0ead8"], "drink": ["f0ead8", "d8b13c", "e88ac0"],
         "produce": ["d63c2a", "4a7a3a", "e07b2a"], "wool": ["b03a30", "e8c33c", "2e6da4"],
         "specialty": ["c9a227", "b03a30", "d88f2e"]}
DIST7 = {"banhtrang": "food", "khoai": "food", "banhcan": "food", "supcua": "food", "sua": "drink",
         "caphe": "drink", "yaourt": "drink", "hoa": "produce", "banhuot": "food", "suatuoi": "drink",
         "dau": "produce", "len1": "wool", "rau": "produce", "dacsan": "specialty"}
def stall_deco_mirror(sx, sz, ry, by, sid):
    cbox((4.34, 0.07, 1.08), L2W(sx, sz, ry, by, 0, 2.5, 0.98), srgb("4c3423"))
    tplaneV("Sign_" + sid, 4.2, 0.95, L2W(sx, sz, ry, by, 0, 2.5, 1.05),
            tex_mat("SignM_" + sid, os.path.join(M7D, "sign-%s.png" % sid)), flip=(ry == 0))
    tplaneV("Card_" + sid, 0.62, 0.39, L2W(sx, sz, ry, by, 1.42, 1.34, 1.06),
            tex_mat("CardM_" + sid, os.path.join(M7D, "card-%s.png" % sid), 0.15), flip=(ry == 0))
    for (lx, ly) in [(-1.55, 3.02), (0, 3.4), (1.55, 2.98)]:
        sph(L2W(sx, sz, ry, by, lx, ly, 1.42), 0.21, PAPER, (1, 1, 1.25), emis=(srgb("ffa63d"), 1.6))
        cbox((0.05, 0.05, 0.16), L2W(sx, sz, ry, by, lx, ly - 0.33, 1.42), srgb("c22e22"))
    for i in range(6):
        sph(L2W(sx, sz, ry, by, -1.7 + i * 0.68, 3.32, 0.72), 0.28, srgb("4d7340") if i % 2 else srgb("3d6034"), (1, 1, 0.55))
    sp = SPILL[DIST7[sid]]
    for i in range(5):
        cylM(L2W(sx, sz, ry, by, -0.84 + i * 0.42, 1.16, 0.88), 0.052, 0.1, srgb(sp[i % 3]))
    for gx in (-1.95, 1.95):
        cylM(L2W(sx, sz, ry, by, gx, 0.15, 2.28), 0.3, 0.3, srgb("9a6a42"))
        for i in range(5):
            a = i * 1.26
            sph(L2W(sx, sz, ry, by, gx + math.cos(a) * 0.14, 0.34, 2.28 + math.sin(a) * 0.14), 0.06, srgb("d8342a"), (1, 1, 0.95))
    side = -2.35 if len(sid) % 2 == 0 else 2.35
    cbox((0.55, 0.45, 0.34), L2W(sx, sz, ry, by, side, 0.17, 0.9), WOOD)
    cbox((0.5, 0.4, 0.3), L2W(sx, sz, ry, by, side, 0.49, 0.9), srgb("74522f"))
def hero_mirror(sx, sz, ry, by, sid):
    def W(lx, ly, lz): return L2W(sx, sz, ry, by, lx, ly, lz)
    if sid == "sua":
        for sy in (1.44, 1.74): cbox((0.95, 0.3, 0.05), W(-1.08, sy, -0.3), WOOD)
        for i in range(3):
            cylM(W(-1.32 + i * 0.26, 1.55, -0.3), 0.07, 0.17, srgb("d8b13c"))
            cylM(W(-1.32 + i * 0.26, 1.85, -0.3), 0.07, 0.17, srgb("f0ead8"))
        cylM(W(-0.3, 1.3, 0.02), 0.33, 0.42, STEEL)
        cylM(W(-0.3, 1.54, 0.02), 0.32, 0.07, STEEL)
        for i in range(4): cylM(W(0.42, 1.20 + i * 0.055, 0.3), 0.05, 0.07, srgb("f0ead8"))
    elif sid == "banhtrang":
        for i in range(6): cylM(W(1.18, 1.13 + i * 0.022, 0.32), 0.17, 0.02, srgb("e8c88a"))
        cbox((0.95, 0.52, 0.04), W(0.05, 1.1, 0.78), WOOD)
        for i in range(3):
            cylM(W(-0.25 + i * 0.32, 1.14, 0.78), 0.15, 0.025, srgb("e8c88a"))
            sph(W(-0.25 + i * 0.32, 1.17, 0.78), 0.045, srgb("d8542e"), (1, 1, 0.6))
        cylM(W(-1.32, 1.2, 0.42), 0.06, 0.16, srgb("c22e22"))
        for i in range(2): sph(W(0.62 + i * 0.24, 1.14, 0.5), 0.09, srgb(["d8542e", "7fae5a"][i]), (1, 1, 0.45))
    elif sid == "banhcan":
        cbox((0.98, 0.52, 0.3), W(-0.72, 0.94, 0.12), CLAYC)
        for i in range(5):
            cylM(W(-1.08 + i * 0.19, 1.13, 0.12), 0.09, 0.075, CLAYC)
            cylM(W(-1.08 + i * 0.19, 1.17, 0.12), 0.07, 0.02, srgb("f0d090"))
        sph(W(0.28, 1.13, 0.3), 0.17, srgb("f0ead8"), (1, 1, 0.5))
        cbox((0.44, 0.32, 0.05), W(0.88, 1.1, 0.32), WOOD)
        for i in range(6): sph(W(0.74 + (i % 3) * 0.1, 1.15, 0.26 + (i // 3) * 0.1), 0.032, srgb("f5f2ea"), (1, 1, 0.9))
        cylM(W(0.15, 1.11, 0.8), 0.3, 0.02, srgb("4d7340"))
        for i in range(4): cylM(W(-0.02 + (i % 2) * 0.17, 1.14, 0.72 + (i // 2) * 0.17), 0.075, 0.02, srgb("f0d090"))
    elif sid == "caphe":
        cbox((0.88, 0.42, 0.04), W(-0.52, 1.11, 0.22), WOOD)
        for i in range(4):
            cylM(W(-0.82 + i * 0.21, 1.17, 0.22), 0.045, 0.1, srgb("f5f2ea"))
            cylM(W(-0.82 + i * 0.21, 1.28, 0.22), 0.058, 0.085, STEEL)
        sph(W(1.52, 0.32, 0.62), 0.3, srgb("9a7a4e"), (1, 1, 0.62))
        for i in range(3):
            cylM(W(0.68 + i * 0.15, 1.19, -0.12), 0.055, 0.11, srgb("f0ead8"))
            cylM(W(0.68 + i * 0.15, 1.22, -0.12), 0.056, 0.03, srgb("c22e22"))
    elif sid == "supcua":
        cylM(W(-0.52, 1.31, 0.02), 0.36, 0.44, STEEL)
        cylM(W(-0.38, 1.56, 0.02), 0.35, 0.07, STEEL)
        for sx2 in (0.5, 0.92):
            for i in range(4): cylM(W(sx2, 1.16 + i * 0.048, 0.32), 0.1, 0.05, srgb("f0ead8"))
        for i, tc in enumerate(["e8c33c", "f0ead8", "d8542e"]):
            cylM(W(-0.2 + i * 0.3, 1.15, 0.82), 0.09, 0.06, WOOD)
            sph(W(-0.2 + i * 0.3, 1.19, 0.82), 0.075, srgb(tc), (1, 1, 0.5))
    elif sid == "dau":
        for s in range(3): cbox((1.15 - s * 0.18, 0.34, 0.16), W(0.72, 1.16 + s * 0.17, -0.18 + s * 0.05), WOOD)
        for s in range(3):
            for i in range(4 - (1 if s == 2 else 0)):
                sph(W(0.32 + i * 0.26, 1.28 + s * 0.17, -0.13 + s * 0.05), 0.05, srgb("d8342a"), (1, 1, 0.95))
        cbox((0.56, 0.42, 0.3), W(-1.05, 1.05, 0.3), WOOD)
        for i in range(6): sph(W(-1.22 + (i % 3) * 0.18, 1.26, 0.22 + (i // 3) * 0.17), 0.105, srgb("51783c"), (1, 1, 0.85))
        for i, kc in enumerate(["f5e6b8", "e88ac0", "bfe3c0", "f5e6b8"]):
            cylM(W(-0.12 + i * 0.17, 1.19, 0.85), 0.05, 0.12, srgb(kc))
    if sid in ("sua", "supcua", "banhcan", "banhtrang"):
        for j, (py, pr) in enumerate([(1.95, 0.34), (2.55, 0.5), (3.15, 0.66)]):
            sph(W(-0.9, py, 0.15), pr, srgb("f7f2e6"), (1, 1, 0.8), emis=(srgb("f7f2e6"), 0.22))
for (sx, sz, ry, by, sid) in [
    (-36, 10.15, math.pi, 0, "banhtrang"), (-31, 10.15, math.pi, 0, "khoai"),
    (-26, 10.15, math.pi, 0, "banhcan"), (-21, 10.15, math.pi, 0, "supcua"),
    (22, 10.15, math.pi, 0, "sua"), (27, 10.15, math.pi, 0, "caphe"),
    (32, 10.15, math.pi, 0, "yaourt"), (37.5, 10.15, math.pi, 0, "hoa"),
    (-56, 10.15, math.pi, 0.28, "banhuot"), (-49.5, 10.15, math.pi, 0, "suatuoi"),
    (24, 23.5, math.pi, 0.5, "dau"), (-24, 15, 0, 0.5, "len1"),
    (16, 15, 0, 0.5, "rau"), (-20, 20, math.pi, 0.5, "dacsan"),
]:
    stall_deco_mirror(sx, sz, ry, by, sid)
    if sid in ("sua", "banhtrang", "banhcan", "caphe", "supcua", "dau"):
        hero_mirror(sx, sz, ry, by, sid)
# --- dây lồng đèn giăng ngang (gương web) ---
def lstring(p0, p1, n, r):
    (x0, y0, z0), (x1, y1, z1) = p0, p1
    def bez(t):
        cx, cy, cz = (x0 + x1) / 2, (y0 + y1) / 2, min(z0, z1) - 0.85
        return ((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1,
                (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1,
                (1 - t) ** 2 * z0 + 2 * (1 - t) * t * cz + t ** 2 * z1)
    for i in range(13):
        sph(bez(i / 12), 0.028, srgb("2e2a24"), (1, 1, 1))
    for i in range(1, n + 1):
        p = bez(i / (n + 1))
        sph((p[0], p[1], p[2] - 0.3 - r * 0.6), r, PAPER, (1, 1, 1.22), emis=(srgb("ffa63d"), 1.6))
        cbox((0.05, 0.05, 0.17), (p[0], p[1], p[2] - 0.3 - r * 1.9), srgb("c22e22"))
lstring((-62, 13, 9.2), (-62, -13, 9.2), 7, 0.30)
lstring((-48, 13, 8.6), (-48, -13, 8.6), 6, 0.26)
lstring((-20, -11.5, 8.4), (-20, 4, 8.4), 7, 0.30)
lstring((-11.5, 14, 11.6), (11.5, 14, 11.6), 7, 0.30)
# --- mặt tiền: đồng hồ + cờ tam giác + giỏ hoa (gương web) ---
sph((0, -11.5, 17.7), 1.58, srgb("8c2f26"), (1, 0.10, 1))
sph((0, -11.58, 17.7), 1.5, srgb("f0ead8"), (1, 0.10, 1))
for i in range(12):
    a = i / 12 * math.tau
    cbox((0.07, 0.03, 0.22), (math.sin(a) * 1.24, -11.68, 17.7 + math.cos(a) * 1.24), srgb("4a3423"))
cbox((0.11, 0.04, 0.78), (0.166, -11.68, 17.59), srgb("33241a"), rot=(0, 2.16, 0))
cbox((0.08, 0.04, 1.12), (-0.28, -11.7, 17.7), srgb("33241a"), rot=(0, -math.pi / 2, 0))
PENC = ["c8372d", "e8862e", "e8c832", "3f9e4d", "2e6da4", "8668c4"]
for i in range(22):
    px = -31 + (i + 0.5) * (62 / 22)
    pz = 7.9 - (1 - (px / 31) ** 2) * 0.7
    cbox((0.42, 0.03, 0.42), (px, -11.4, pz - 0.21), srgb(PENC[i % 6]))
for i, x in enumerate(range(-30, 31, 6)):
    cylM((x, -11.42, 7.28), 0.15, 0.2, srgb("a8542e"))
    sph((x, -11.42, 7.48), 0.17, srgb(["d66a8c", "e8c832", "c8372d"][i % 3]), (1, 1, 0.75))
# --- rạp: banner dọc + chậu đối xứng ---
tplaneV("BannerRap", 1.7, 5.4, (-27.6, 49.15, 20.6), tex_mat("BannerRapM", os.path.join(M7D, "banner-rap.png"), 0.2), flip=True)
tplaneV("BannerPhim", 1.7, 5.4, (-10.4, 49.15, 20.6), tex_mat("BannerPhimM", os.path.join(M7D, "banner-phim.png"), 0.2), flip=True)
for (px, py) in [(-29.2, 47.6), (-8.8, 47.6), (-9.8, 16), (9.8, 16)]:
    lz = groundH(px, py) if abs(py) < 30 else 17
    cylM((px, py, lz + 0.37), 0.46, 0.75, srgb("8a4a34"))
    sph((px, py, lz + 0.95), 0.55, srgb("4d7340"), (1, 1, 0.8))
    sph((px + 0.3, py, lz + 1.25), 0.2, srgb("d66a8c"), (1, 1, 0.8))
# --- thang: 3 cặp đèn trụ ---
for (lx, ly) in [(-10.6, 8), (10.6, 8), (-10.6, 16), (10.6, 16), (-10.6, 24), (10.6, 24)]:
    g = dup_tree(lamp_tpl); g.location = (lx, ly, groundH(lx, ly))
# --- trong nhà lồng: dải len + dây bóng + sàn kim cương + mặt biển chữ cho quầy sẵn có (rows45) ---
KNIT = ["b03a30", "e07b2a", "e8c33c", "3f7a44", "2e6da4", "74566b", "d66a8c", "8c6a3a"]
for kx in (-19.5, 0, 19.5):
    for i in range(8):
        cbox((0.36, 0.05, 0.78), (kx - 1.4 + i * 0.4, -26.42, 4.42), srgb(KNIT[i]))
for i in range(21):
    sph((-27 + i * 2.7, -26.4, 5.02), 0.05, srgb("ffc46b"), (1, 1, 1), emis=(srgb("ffc46b"), 2.0))
_fl = tplaneV("DiamondFloor", 58, 15.6, (0, -20.2, 0.54), tex_mat("DiamondM", os.path.join(M7D, "diamond.png"), 0.05, (11, 3)))
_fl.rotation_euler = (math.pi / 2, 0, 0)
QUAYS = [3, 7, 11, 15]
_qn2 = 0
_rows2 = []
for i in range(12):
    cx = -28.6 + i * 5.2
    _rows2 += [(cx, 13.3, 0), (cx, 26.7, math.pi)]
for i in range(12):
    cx = -28.6 + i * 5.2
    _rows2 += [(cx, 19.35, math.pi), (cx, 20.65, 0)]
for (rx, rz, ry) in _rows2:
    if rx > 25 and rz > 14: continue
    if any(abs(rx - sx) < 4.6 and abs(rz - sz) < 2.7 for (sx, sz) in INNER45): continue
    _qn2 += 1
    if abs(rx) > 21: continue
    fx = math.sin(ry); fz = math.cos(ry)
    tplaneV("Quay%d" % _qn2, 3.6, 0.95, (rx + fx * 0.68, -(rz + fz * 0.68), 3.05),
            tex_mat("QuayM%d" % _qn2, os.path.join(M7D, "quay-%d.png" % QUAYS[_qn2 % 4]), 0.2), flip=(ry == 0))
# --- nền lát đá phố trước chợ + đường vào ---
_pv1 = tplaneV("Pave1", 96, 15, (0, -5.2, 0.02), tex_mat("StoneM1", os.path.join(M7D, "stone.png"), 0.0, (13, 2)))
_pv1.rotation_euler = (math.pi / 2, 0, 0)
_pv2 = tplaneV("Pave2", 38, 17, (-60, -2, 0.02), tex_mat("StoneM2", os.path.join(M7D, "stone.png"), 0.0, (5, 2)))
_pv2.rotation_euler = (math.pi / 2, 0, 0)
flush_grp()
print("SECTION m7-detail done", flush=True)

# ================= V4.9 MỤC 7 — GƯƠNG LỚP GỢI Ý ChatGPT ĐÃ LỌC =================
_GRP2 = {}
def _grp2(kind, rgb, emis):
    key = (kind, rgb, emis)
    if key not in _GRP2: _GRP2[key] = bmesh.new()
    return _GRP2[key]
def sph2(loc, r, rgb, sxyz=(1, 1, 1), emis=None):
    bm = _grp2("s", rgb, emis)
    for v in bmesh.ops.create_icosphere(bm, subdivisions=1, radius=r)["verts"]:
        v.co.x = loc[0] + v.co.x * sxyz[0]; v.co.y = loc[1] + v.co.y * sxyz[1]; v.co.z = loc[2] + v.co.z * sxyz[2]
def cyl2(loc, r, h, rgb, emis=None):
    bm = _grp2("c", rgb, emis)
    for v in bmesh.ops.create_cone(bm, cap_ends=True, segments=12, radius1=r, radius2=r, depth=h)["verts"]:
        v.co.x += loc[0]; v.co.y += loc[1]; v.co.z += loc[2]
def flush2():
    for (kind, rgb, emis), bm in _GRP2.items():
        me = bpy.data.meshes.new("GPTG"); bm.to_mesh(me); bm.free()
        ob = bpy.data.objects.new("GPTG", me); bpy.context.collection.objects.link(ob)
        if emis is None:
            me.materials.append(mat_plain("GPTGM", rgb))
        else:
            me.materials.append(emat("GPTGE", rgb, emis[0], emis[1]))
BOUG = ["d63384", "e75480", "c22e6e", "e88ac0"]
def boug(bx, bz, s=1.0):  # toa do three -> render
    y = groundH(bx, -bz)
    sph2((bx, -bz, y + 0.25), 0.55 * s, srgb("3d6034"), (1, 1, 0.6))
    for i in range(6):
        a = i * 1.05 + bx
        sph2((bx + math.cos(a) * 0.42 * s, -bz + math.sin(a) * 0.42 * s, y + 0.42 + (i % 2) * 0.16),
             (0.15 + (i % 3) * 0.05) * s, srgb(BOUG[i % 4]), (1, 1, 0.9))
for bx in (-42, -36, -30, -24):
    for bz in (-19.5, -23, -26.5):
        boug(bx + (bz * 7 % 2), bz, 1 + ((bx + bz) % 3) * 0.12)
for bx in (-40, -33, -26): boug(bx, -28.8, 1.25)
for bx in (-44, -20): boug(bx, -17.2, 0.85)
HYDC = ["7f9fd4", "e88ac0", "f0ead8", "b39ddb", "5b84c4"]
def hyd(x, z):  # three -> render, chan y=0.35
    sph2((x, -z, 0.57), 0.5, srgb("40642f"), (1, 1, 0.65))
    for i in range(5):
        a = i * 1.26 + x * 2
        sph2((x + math.cos(a) * 0.3, -z + math.sin(a) * 0.3, 0.83), 0.17, srgb(HYDC[i % 5]), (1, 1, 0.95))
    sph2((x, -z, 0.93), 0.19, srgb(HYDC[abs(round(x * 10)) % 5]), (1, 1, 0.95))
for i in range(10):
    a = -0.5 + i * 0.42
    hyd(-28.2 + math.cos(a) * 3.9, -2.8 + math.sin(a) * 3.9)
hyd(-18.5, 1.8); hyd(-30.5, 3.6); hyd(-15.8, -9.5)
for i in range(12):
    a = i / 12 * math.tau + 0.3
    mx, mz = -24 + math.cos(a) * (5.6 + (i % 3) * 1.3), -6 + math.sin(a) * (5.6 + (i % 3) * 1.3)
    cyl2((mx, -mz, 0.47), 0.035, 0.24, srgb("6a6257"))
    sph2((mx, -mz, 0.63), 0.11, srgb("ffe2b0"), (1, 1, 1), emis=(srgb("ffb45e"), 1.8))
def stool(x3, z3, y3, color):
    box("Stool", (0.34, 0.34, 0.30), (x3, -z3, y3 + 0.15), color)

def eat_set(x, z):
    y = groundH(x, -z)
    cbox((0.58, 0.58, 0.05), (x, -z, y + 0.44), srgb("74522f"))
    cbox((0.08, 0.08, 0.42), (x, -z, y + 0.21), srgb("5a4632"))
    stool(x + 0.55, z + 0.15, y, (0.85, 0.15, 0.12)); stool(x - 0.5, z - 0.2, y, (0.85, 0.15, 0.12)); stool(x + 0.05, z + 0.58, y, (0.88, 0.25, 0.15))
eat_set(-6.8, -13.5); eat_set(6.8, -13.5); eat_set(-31, 4.5); eat_set(-17.5, 5.5); eat_set(-2, 8.4)
def bucket(x, z):
    y = groundH(x, -z)
    cyl2((x, -z, y + 0.25), 0.23, 0.5, srgb("9aa2a6"))
    for i in range(5):
        a = i * 1.26 + z
        sph2((x + math.cos(a) * 0.13, -z + math.sin(a) * 0.13, y + 0.58), 0.14, srgb(HYDC[i % 5]), (1, 1, 0.95))
    sph2((x, -z, y + 0.66), 0.15, srgb("f0ead8"), (1, 1, 0.95))
for fx in (-30, -18, 14, 26): bucket(fx, 11.35)
bucket(-52, 12.6); bucket(-38.5, -13.6)
def chalk(x, z, tex, flip):
    y = groundH(x, -z)
    tplaneV("Chalk", 0.95, 1.15, (x, -z, y + 0.62), tex_mat("ChalkM", os.path.join(M7D, tex), 0.15), flip=flip)
    cbox((0.06, 0.06, 0.5), (x - 0.35, -z, y + 0.25), srgb("5a4632"))
    cbox((0.06, 0.06, 0.5), (x + 0.35, -z, y + 0.25), srgb("5a4632"))
chalk(35.6, 7.4, "board-hoa.png", False)
chalk(-38.6, 7.6, "board-nuong.png", False)
for x in range(-30, 31, 4):  # den long do trong o lam tang 2 (buoc 3.75 web -> lam tron 4 cho harness)
    cyl2((x, -11.42, 10.85), 0.012, 0.5, srgb("2e2a24"))
    sph2((x, -11.42, 10.5), 0.155, srgb("d8342a"), (1, 1, 1.2), emis=(srgb("c22020"), 1.5))
_mu = tplaneV("MuralAtiso", 9.5, 5.9, (-34.3, -20, 9.9), tex_mat("MuralM", os.path.join(M7D, "mural-atiso.png"), 0.1, (-1, 1)))
_mu.rotation_euler = (0, 0, math.pi / 2)
for (mx, mz, rz) in [(-13.8, 8.6, -0.7), (-17.6, 9.8, -0.45)]:
    g = dup_sub(moto_tpl); g.location = (mx, -mz, 0); g.rotation_euler = (0, 0, rz)
    hide_rider(g); paint_vehicle(g)
for mn in ("StoneM1", "StoneM2"):
    if mn in bpy.data.materials:
        bpy.data.materials[mn].node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = 0.5
flush2()
print("SECTION gpt-layer done", flush=True)


# V4.4: đèn pha (trắng ấm) + đèn hậu (đỏ) dạng đèn điểm cho vài xe gần khung nghiệm thu
point((-49.2, -0.2, 0.95), (1.0, 0.92, 0.72), energy=26, dist=6)
point((-50.9, -0.2, 0.80), (1.0, 0.16, 0.10), energy=9, dist=3.5)
point((-15.9, -3.6, 0.95), (1.0, 0.92, 0.72), energy=26, dist=6)
point((-14.1, -3.6, 0.80), (1.0, 0.16, 0.10), energy=9, dist=3.5)
_a0 = 0.4
# V4.8: bo den pha xe vong dao (khong con xe chay vong)

# ---------------- đám đông (template character) ----------------
char_tpl = make_template("character.glb", "CharTpl")
SHIRTS = ['a62b25', 'd97a30', 'd9a62e', 'e8c87e', '6b8f3e', '2e6b46', '2f8f83',
          '3a6bc2', '8668c4', 'e58e6b', 'c95d7e', '7a4a2e', '96683f', '35507a']  # BANG 14 MAU research/13
PANTS = ['4a4640', '3a3f4a', '5c4633', '2e2a26']
SCARVES = ['d9a62e', 'a62b25', '3a6bc2', '8668c4', 'd97a30']
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

STAIR_SITTERS = [(-7.8, -21.5), (-8.6, -20.6), (7.6, -21.2), (8.4, -20.3), (-6.9, -19.3),
                 (-7.2, -17.6), (-8.1, -16.7), (-7.5, -15.8), (-6.8, -13.4),
                 (7.4, -17.2), (8.2, -16.3), (7.0, -14.2), (7.9, -13.5),
                 (-7.7, -11.3), (-8.5, -10.4), (7.5, -11.0), (8.3, -10.1), (6.7, -9.3),
                 (-7.3, -7.2), (-8.0, -6.4), (-6.9, -4.6),
                 (7.3, -6.8), (8.1, -5.9), (7.0, -4.9),
                 (-7.4, -28.6), (-8.2, -27.7), (7.5, -28.2), (8.3, -27.3),
                 (-7.6, -25.5), (-8.4, -24.6), (7.7, -25.8), (8.5, -24.9),
                 (-7.0, -18.9), (7.1, -19.2), (-6.9, -15.0), (7.2, -16.0),
                 (-8.2, -9.0), (8.0, -8.8), (-7.6, -3.4), (7.8, -3.6)]  # V4.7: +12
for (sx, sz) in STAIR_SITTERS:
    stool(sx, sz, groundH(sx, sz), (0.10, 0.28, 0.60) if random.random() < 0.75 else (0.65, 0.15, 0.12))
    person(sx, sz, rotz=(random.random() - 0.5) * 0.44, sit=True)
for (sx, sz, rz) in [(-1.5, -6, math.pi), (2, -10, 0), (-2, -14, math.pi), (1.5, -18, 0),
                     (-1, -23, math.pi), (2.5, -26, 0), (-2.5, -29, math.pi), (0.5, -8, 0)]:
    person(sx, sz, rotz=rz)
for qx in (-36, -31, 22, 27):  # xếp hàng trước 4 sạp ăn mặt tiền
    for i in range(3):
        person(qx + (random.random() - 0.5) * 0.2, 7.6 - i * 0.48, rotz=(random.random() - 0.5) * 0.24)  # V4.7
for (wx, wz, rz) in [(-40, 1.5, 0), (-28, 2.5, math.pi), (-16, 1, 0), (-6, 2.8, math.pi),
                     (4, 1.2, 0), (14, 2.6, math.pi), (24, 1, 0), (34, 2.4, math.pi),
                     (44, 1.5, 0), (-48, 2, math.pi)]:
    person(wx, wz, rotz=rz)
for (px, pz) in ((-12.9, -3.4), (-14.8, 1.6), (-19.5, 5.6), (-26, 6.2), (-31.5, 3.4), (-35.6, -2.2)):  # V4.8: quanh dao R10.5 (guong web)
    person(px, pz, rotz=math.atan2(-24 - px, -6 - pz), y3=0)
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
        person(qx + (random.random() - 0.5) * 0.3, 7.6 - i * 0.48, rotz=math.pi + (random.random() - 0.5) * 0.2)  # V4.7
for (sx2, sz2) in ((-60.5, 13.0), (-53, 13.0), (-38.5, 13.0), (-64, 13.2)):  # V4.7: trước mặt tiền nhà nam mới
    stool(sx2, sz2, groundH(sx2, sz2), (0.10, 0.28, 0.60))
    person(sx2, sz2, rotz=math.pi, sit=True)
for i in range(3):  # nhóm chat vỉa hè
    a = i / 3 * math.pi * 2 + 0.5
    person(-66 + math.cos(a) * 0.55, 5.6 + math.sin(a) * 0.55, rotz=-a)
for (px, pz) in ((-34.8, -9.4), (-32.2, -13.8)):  # V4.8: them nguoi cung bac dao (them phang)
    person(px, pz, rotz=math.atan2(-24 - px, -6 - pz), y3=0)
for bz in (-4, -12, -20, -26):
    person(17.5, bz, rotz=math.pi)   # V4.3: người đi trên MẶT CẦU NỔI (kiểm chứng hết lơ lửng)
person(17.5, 9.6, rotz=0)            # V4.3: người trên sân thượng tầng 2
person(22.5, 6.9, rotz=math.pi)  # V4.7: người chơi đứng trước sạp sữa (front mới 8.05)
# --- V4.4: hoạt động trong khung — khách trước quầy, ngồi ăn, nhóm chụp ảnh quanh tượng ---
for (qx, qz) in ((-36, 6.6), (-31, 6.6), (22, 6.6), (27, 6.6)):  # V4.7: trước front mới
    person(qx + 0.4, qz, rotz=math.pi)
for (ex, ez) in ((-56, 7.3), (-49.5, 7.3)):  # V4.7: ngồi ăn trước 2 sạp đường vào (front mới)
    stool(ex, ez, groundH(ex, ez), (0.10, 0.28, 0.60)); person(ex, ez, rotz=math.pi, sit=True)
person(-45, 3.5, rotz=-math.pi / 2); person(-44.2, 4.4, rotz=-math.pi / 2)
# V4.8: nhom chup anh o diem check-in tuong dai MOI (three (-13.2, 2.8)) + ngoi ghe da nam dao
for (px2, pz2, rz2) in ((-13.4, 2.6, 2.6), (-12.6, 1.4, 2.2), (-14.2, 1.2, 2.9)):
    person(px2, pz2, rotz=rz2, y3=0)
person(-12.4, 0.2, rotz=-2.2, y3=0)
for (bx2, bz2) in ((-15.6, 2.4), (-32.4, 2.4)):
    person(bx2, bz2, rotz=0, sit=True, y3=0.32)
person(21.3, 7.3, rotz=math.pi); person(23.8, 7.0, rotz=math.pi)  # V4.7
stool(20.4, 7.5, 0, (0.65, 0.15, 0.12)); person(20.4, 7.5, rotz=math.pi, sit=True)  # V4.7
# --- V4.5: người ở các hạng mục mới ---
for (lx, lz) in ((-8, 26.9), (3, 26.9), (13, 26.9)):   # khách lửng kính nhìn xuống khu rau
    person(lx, lz, rotz=math.pi, y3=3.7)
person(30.9, 19.4, rotz=math.pi / 2, y3=6.55)          # người bán quầy chợ la
person(30.3, 15, y3=innerStairH(15))                   # người đi thang trong nhà (chuyến 1)
person(30.3, 23, y3=innerStairH(23))                   # người đi thang trong nhà (chuyến 2)
person(25, 10.8, y3=12.6)                              # người đi hành lang nối
for (hx2, hz2, rz3) in ((-8, 17.5, math.pi / 2), (8, 22, -math.pi / 2), (-24, 21.5, 0), (14, 17.2, math.pi)):
    person(hx2, hz2, rotz=rz3)                         # khách đi lối trong nhà lồng
for (vx, vz) in ((-15.5, -27.5), (-13.2, -20.5), (-16.5, -15.5), (-13.8, -11), (-15.2, -6.5), (-16.8, -3.8), (12.7, -27), (12.9, -15), (12.6, -6)):
    person(vx + 0.15, vz - 0.8, rotz=0.4, sit=True)    # người bán hàng rong trên thềm
for (cx2, cz2, n2) in ((-15, -10.5, 3), (-15, -22.5, 2), (12.8, -21, 2), (12.8, -4.2, 2), (-13, 2, 3), (13, 2, 2)):
    for i in range(n2):
        a = i / n2 * math.pi * 2 + cx2 * 0.7
        person(cx2 + math.cos(a) * 0.55, cz2 + math.sin(a) * 0.55, rotz=-a)
for (ccx, ccz) in ((-17, -32.5), (17.5, -32.5)):       # khách ngồi cà phê hiên đồi
    for tx in (-1.5, 1.3):
        stool(ccx + tx, ccz - 0.35, 17.18, (0.10, 0.28, 0.60))
        person(ccx + tx, ccz - 0.35, rotz=(random.random() - 0.5) * 0.3, sit=True, y3=17.18)
for (vx2, vz2) in ((-14.5, -31.2), (15.8, -31.2), (-16.8, -31.4), (13.6, -31.5)):
    person(vx2, vz2, rotz=(random.random() - 0.5) * 0.4)   # người ngắm cảnh điểm nhìn xuống
person(-7.45, -14.9, rotz=-math.pi / 2)                # người bán sạp bậc bánh tráng
person(7.45, -5.3, rotz=math.pi / 2)                   # người bán sạp bậc trứng nướng
for (qx2, qz2) in ((8.6, -22.3), (8.6, -20.9), (8.6, -11.1), (8.6, -9.7)):
    person(qx2, qz2, rotz=-math.pi / 2)                # khách chờ ở 2 sạp chiếu nghỉ
# --- V4.7: người mua trước quầy trang trí trong nhà lồng (chạy lại đúng logic web) ---
_qn2 = [0]
for (rx, rz, ry) in rows45:
    if rx > 25 and rz > 14: continue
    if any(abs(rx - sx) < 4.6 and abs(rz - sz) < 2.7 for (sx, sz) in INNER45): continue
    _qn2[0] += 1
    if _qn2[0] % 10 >= 8: continue
    if ry == 0: person(rx + (_qn2[0] % 3 - 1) * 0.9, rz + 1.8, rotz=0, y3=0.5)
    else: person(rx + (_qn2[0] % 3 - 1) * 0.9, rz - 1.8, rotz=math.pi, y3=0.5)
# --- V4.7: ngắm sạp mặt tiền + cụm đường vào/đồi/phố đêm + ngồi trước nhà bắc + dạo quảng trường ---
for bx in (-33.5, -19, -8, 14, 25.5, 34.5, 36.2, 39.2):
    person(bx, 6.4, rotz=math.pi)
for (fx, fz) in ((-30, 7.6), (-18, 8.1), (-4, 7.6), (10, 8.1), (22, 7.6), (32, 8.1), (-19, 7.9), (-29, 7.9)):  # V4.8: hang truoc mat tien (guong web)
    person(fx, fz, rotz=0)
for (hx3, hz3, n3) in ((-70, 6.5, 3), (-63, -4, 2), (-56, 7.5, 2)):  # V4.8: cum dau duong vao (guong web)
    for i in range(n3):
        a = i / n3 * math.pi * 2 + hx3 * 0.7
        person(hx3 + math.cos(a) * 0.55, hz3 + math.sin(a) * 0.55, rotz=-a)
for (hx3, hz3, n3) in ((-58, 12.6, 3), (-47, -10.6, 2), (-30, -52, 3), (6, -44, 3), (36, -44, 2), (-38, -58, 2), (-20, 4.5, 3), (16, 5.5, 3)):
    for i in range(n3):
        a = i / n3 * math.pi * 2 + hx3 * 0.7
        person(hx3 + math.cos(a) * 0.55, hz3 + math.sin(a) * 0.55, rotz=-a)
for (sx3, sz3) in ((-62, -11.6), (-52, -12.4), (-42, -11.6)):  # V4.8: truoc day nha bac moi
    stool(sx3, sz3, groundH(sx3, sz3), (0.10, 0.28, 0.60))
    person(sx3, sz3, rotz=math.pi, sit=True)
for (wx3, wz3, rz4) in ((-66, 6.5, 0), (-52, 5.0, math.pi), (-44, 7.0, 0), (8, 6.5, math.pi), (20, 5.0, 0), (-70, -8.6, math.pi)):
    person(wx3, wz3, rotz=rz4)
print("PEOPLE TOTAL:", people_count[0], flush=True)

# ================= V4.8 MỤC 6: BẦU TRỜI — gương hệ trời của WEB (trước đây harness chỉ có world phẳng nâu chết) =================
# WEB: dome shader botC #a86834 (chân trời hổ phách) -> midC #3d2b52 (tím) -> topC #131c3a (xanh sâu);
# 420 sao r=300 nhấp nháy; trăng three(150,120,160) = render (150,-160,120) đĩa r13 + quầng; mây sprite y three 100..145 trôi.
def _sky_lerp(c1, c2, t):
    return tuple(c1[i] + (c2[i] - c1[i]) * t for i in range(3))
_SKY_BOT, _SKY_MID, _SKY_TOP = srgb("a86834"), srgb("3d2b52"), srgb("131c3a")
bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=24, radius=330, location=(0, 0, 0))
_dome = bpy.context.object; _dome.name = "SkyDome"
for _p in _dome.data.polygons:
    _p.flip()
_ca = _dome.data.color_attributes.new(name="Col", type="FLOAT_COLOR", domain="CORNER")
_vpos = [v.co.normalized() for v in _dome.data.vertices]
for _poly in _dome.data.polygons:
    for _li in _poly.loop_indices:
        _d = _vpos[_dome.data.loops[_li].vertex_index]
        _h = _d.z
        if _h > 0.12:
            _c = _sky_lerp(_SKY_MID, _SKY_TOP, min(1.0, max(0.0, (_h - 0.12) / 0.53)))
        else:
            _c = _sky_lerp(_SKY_BOT, _SKY_MID, min(1.0, max(0.0, (_h + 0.08) / 0.20)))
        _g = max(0.0, -_d.y) ** 3 * math.exp(-max(_h, 0.0) * 6.0) * 0.55  # quầng ấm chân trời phía chợ (render -Y)
        _ca.data[_li].color = (_c[0] + 1.0 * _g, _c[1] + 0.60 * _g, _c[2] + 0.24 * _g, 1.0)
_dm = bpy.data.materials.new("SkyDomeMat"); _dm.use_nodes = True
_db = _dm.node_tree.nodes["Principled BSDF"]
_vc = _dm.node_tree.nodes.new("ShaderNodeVertexColor"); _vc.layer_name = "Col"
_dm.node_tree.links.new(_vc.outputs["Color"], _db.inputs["Base Color"])
_dm.node_tree.links.new(_vc.outputs["Color"], _db.inputs["Emission Color"])
_db.inputs["Emission Strength"].default_value = 1.0
_dome.data.materials.append(_dm)
_rnd = random.Random(48)
_bm = bmesh.new()  # sao: 1 mesh từ 380 ico nhỏ (bán kính 315 như web r=300, cao độ xuống tới ~5° cho lọt đỉnh khung B)
for _i in range(380):
    _a = _rnd.uniform(0, math.tau); _e = _rnd.uniform(0.08, 1.42); _r = 315.0
    _cen = (_r * math.cos(_e) * math.cos(_a), _r * math.cos(_e) * math.sin(_a), _r * math.sin(_e))
    for _v in bmesh.ops.create_icosphere(_bm, subdivisions=0, radius=_rnd.uniform(0.8, 1.5))["verts"]:
        _v.co.x += _cen[0]; _v.co.y += _cen[1]; _v.co.z += _cen[2]
_sme = bpy.data.meshes.new("StarsMesh"); _bm.to_mesh(_sme); _bm.free()
_sob = bpy.data.objects.new("Stars", _sme); bpy.context.collection.objects.link(_sob)
_sm = bpy.data.materials.new("StarMat"); _sm.use_nodes = True
_sb = _sm.node_tree.nodes["Principled BSDF"]
_sb.inputs["Base Color"].default_value = (0.85, 0.9, 1.0, 1)
_sb.inputs["Emission Color"].default_value = (0.85, 0.9, 1.0, 1)
_sb.inputs["Emission Strength"].default_value = 2.4
_sme.materials.append(_sm)
def _moon_ball(rad, emis, strength, squash, name):  # trăng + quầng tại render (150,-160,120), dẹt theo hướng nhìn về gốc
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20, ring_count=12, radius=rad, location=(150, -160, 120))
    _o = bpy.context.object; _o.name = name
    _o.rotation_mode = "QUATERNION"
    _o.rotation_quaternion = mathutils.Vector((0, 0, 1)).rotation_difference(mathutils.Vector((-150, 160, -120)).normalized())
    _o.scale = (1, 1, squash)
    _mm = bpy.data.materials.new(name + "Mat"); _mm.use_nodes = True
    _mb = _mm.node_tree.nodes["Principled BSDF"]
    _mb.inputs["Base Color"].default_value = emis + (1,)
    _mb.inputs["Emission Color"].default_value = emis + (1,)
    _mb.inputs["Emission Strength"].default_value = strength
    _o.data.materials.append(_mm)
_moon_ball(26, (1.0, 0.90, 0.66), 0.30, 0.10, "MoonHalo")
_moon_ball(13, (1.0, 0.96, 0.84), 1.7, 0.15, "Moon")
_bm2 = bmesh.new()  # mây chibi: cụm cầu dẹt gộp 1 mesh, rải trời nam (phía chợ, lọt 2 khung chuẩn) + 2 cụm trời bắc
for (_cx, _cy, _cz) in [(80, -150, 88), (150, -70, 100), (-30, -170, 82), (-120, -120, 95), (40, -230, 105), (-170, -40, 78), (190, -190, 92), (-60, 150, 110), (120, 180, 98)]:
    for _k in range(5):
        _pr = _rnd.uniform(5.5, 10.5)
        _pc = (_cx + _rnd.uniform(-13, 13), _cy + _rnd.uniform(-7, 7), _cz + _rnd.uniform(-2.5, 2.5))
        for _v in bmesh.ops.create_icosphere(_bm2, subdivisions=1, radius=_pr)["verts"]:
            _v.co.x = _pc[0] + _v.co.x * 1.15; _v.co.y = _pc[1] + _v.co.y * 0.7; _v.co.z = _pc[2] + _v.co.z * 0.42
_cme = bpy.data.meshes.new("CloudsMesh"); _bm2.to_mesh(_cme); _bm2.free()
_cob = bpy.data.objects.new("Clouds", _cme); bpy.context.collection.objects.link(_cob)
_cm = bpy.data.materials.new("CloudMat"); _cm.use_nodes = True
_cb = _cm.node_tree.nodes["Principled BSDF"]
_cb.inputs["Base Color"].default_value = srgb("8ea2cc") + (1,)
_cb.inputs["Emission Color"].default_value = srgb("5d6f99") + (1,)
_cb.inputs["Emission Strength"].default_value = 0.5
_cb.inputs["Roughness"].default_value = 1.0
_cme.materials.append(_cm)

# ================= V4.2: GRADE ĐÊM ẤM + 5 ẢNH HÀNH TRÌNH =================
# (bản tối ưu: dựng prop đêm bằng data API + mesh dùng chung — tránh bpy.ops hàng loạt
#  vì mỗi ops kích hoạt depsgraph eval trên cảnh ~6.000 object, rất chậm)
make_sun(euler=(math.radians(65), 0, math.radians(30)), energy=0.65)
SUN.data.color = (1.0, 0.72, 0.45)
BG = world_bg((0.012, 0.016, 0.038), 1.2)  # V4.8 MỤC 6: nền dự phòng xanh đêm sâu (dome trời phủ kín khung; hết mảng nâu phẳng)
sc.view_settings.exposure = 1.08
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
    point((lx, ly - 0.8, lz + 0.2), (1.0, 0.72, 0.38), energy=200, dist=17)
for (lx, ly) in ENTRY_LAMPS:
    lz = entryRampY(lx)
    put(OCTA_BULB, (lx, ly, lz + 3.35), (0.10, 0.10, 0.10))
    point((lx, ly, lz + 3.3), (1.0, 0.70, 0.36), energy=120, dist=18)
_EM = {'SignLetters': 3.0, 'MarketWin': 0.8, 'HotelWinA': 2.0, 'HotelWinB': 0.6, 'HeadLamp': 3.2}
for m in bpy.data.materials:
    base = m.name.split('.')[0]
    if base in _EM and m.use_nodes:
        m.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = _EM[base]
print("TAIL lights done", flush=True)
# mô phỏng lớp web BÁM ẢNH CHỐT: biển lớn phát sáng + lồng đèn giấy lớn + tua đỏ trên dãy sạp mặt đường
for (sx, sz, ry, by, tag) in STALLS:
    if sz != 10.15: continue  # V4.7
    fy = -sz - 1.05
    put(CUBE_WOOD, (sx, fy + 0.30, by + 2.52), (4.2, 0.14, 0.98))
    put(CUBE_SIGN, (sx, fy + 0.20, by + 2.52), (3.9, 0.05, 0.70))
    for (dx, hh) in ((-1.3, 3.05), (0.0, 3.44), (1.3, 3.02)):
        put(OCTA_LANT, (sx + dx, fy - 0.15, by + hh), (0.21, 0.21, 0.27))
        put(CUBE_TASS, (sx + dx, fy - 0.15, by + hh - 0.36), (0.035, 0.035, 0.24))
for (r, hz) in ((0.34, 1.7), (0.5, 2.35), (0.68, 3.05)):  # cột hơi trên sạp sữa (22)
    put(OCTA_FOG, (22.4, -7.3, hz), (r, r, r * 0.8))
print("TAIL facade props done", flush=True)
# V4.4: dây bóng nhỏ quanh mép mái MỌI sạp + vũng sáng điểm trước quầy các dãy chính
for (sx, sz, ry, by, tag) in STALLS:
    fy = -sz - 1.38 * math.cos(ry)
    for dx in (-1.6, -0.8, 0.0, 0.8, 1.6):
        put(OCTA_BULB, (sx + dx, fy, by + 3.0), (0.05, 0.05, 0.05))
    if sz in (10.15, 3):  # V4.7
        point((sx, fy, by + 2.1), (1.0, 0.74, 0.40), energy=55, dist=9)
for (px, py, pz, pe) in ((0, 10, 7.5, 175), (0, 20, 13.5, 175), (0, 30, 18.5, 150), (31, 50, 20.5, 230)):
    point((px, py, pz), (1.0, 0.72, 0.38), energy=pe, dist=17)
# ---- V4.3: bão hòa màu GLB (gương boostSat web) ----
import colorsys as _cs
for _m in bpy.data.materials:
    if not _m.use_nodes: continue
    _b = next((n for n in _m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if not _b: continue
    _c = _b.inputs["Base Color"].default_value
    _h, _s, _v = _cs.rgb_to_hsv(_c[0], _c[1], _c[2])
    if _s <= 0.02:
        _r, _g2, _b2 = _cs.hsv_to_rgb(0.07, 0.15, _v)  # cam xam khong hue -> nga am (xap xi render)
        _b.inputs["Base Color"].default_value = (_r, _g2, _b2, _c[3])
    elif _s > 0.80 or (0.10 < _s < 0.45):
        _r, _g2, _b2 = _cs.hsv_to_rgb(_h, min(0.80, max(0.45, _s)), _v)
        _b.inputs["Base Color"].default_value = (_r, _g2, _b2, _c[3])
print("V43 saturation done", flush=True)
# V4.4: hoa thảm bùng binh rực riêng (gương rule Flower* trong web)
for _m in bpy.data.materials:
    if not _m.name.split('.')[0].startswith('Flower') or not _m.use_nodes: continue
    _b = next((n for n in _m.node_tree.nodes if n.type == 'BSDF_PRINCIPLED'), None)
    if not _b: continue
    _c = _b.inputs["Base Color"].default_value
    _h, _s, _v = _cs.rgb_to_hsv(_c[0], _c[1], _c[2])
    _r, _g2, _b2 = _cs.hsv_to_rgb(_h, min(0.88, max(0.62, _s)), max(_v, 0.55))
    _b.inputs["Base Color"].default_value = (_r, _g2, _b2, _c[3])
print("V44 flowers done", flush=True)
MOONM = emat("MoonM", (0.95, 0.92, 0.80), (1.0, 0.96, 0.84), 2.5)
put(_octa("OctaMoon", MOONM), (215, 195, 238), (13, 13, 13))
point((-24, 6, 3.0), (1.0, 0.70, 0.36), energy=240, dist=21)    # rọi tượng đài
point((-24, 6, 1.9), (1.0, 0.74, 0.42), energy=130, dist=13)    # V4.4: rửa sáng thảm hoa chân tượng
point((-24, -1.5, 2.6), (1.0, 0.72, 0.38), energy=150, dist=14)  # V4.4: rọi MẶT tượng phía chợ (góc người chơi nhìn)
point((-56, 0, 4.5), (1.0, 0.72, 0.38), energy=90, dist=18)      # V4.4: vũng sáng lớn đường vào (gương glowDisc web)
point((-24, -2, 5.0), (1.0, 0.72, 0.38), energy=100, dist=20)    # V4.4: vũng sáng quảng trường trước chợ
point((2, -6, 5.0), (1.0, 0.72, 0.38), energy=90, dist=18)
point((-10, -5, 5.5), (1.0, 0.72, 0.38), energy=250, dist=27)   # rọi mặt tiền
point((12, -5, 5.5), (1.0, 0.72, 0.38), energy=250, dist=27)
RINGM = emat("RingM", (0.9, 0.7, 0.2), (1.0, 0.8, 0.3), 1.6)
ebox("ChkDisc", (2.4, 2.4, 0.06), (-20.2, 1.6, 0.06), RINGM)    # vòng check-in tượng đài (mô phỏng)
STARM = emat("StarM", (1.0, 0.75, 0.2), (1.0, 0.6, 0.1), 2.2)
put(_octa("OctaStar", STARM), (-18, 11.5, 1.1), (0.34, 0.34, 0.5))  # đèn sao ẩn ở thảm hoa (mô phỏng)
put(_octa("OctaStar", STARM), (8, -10.6, 1.1), (0.34, 0.34, 0.5))   # đèn sao ẩn trước chợ (mô phỏng)
person(26.8, -49, rotz=0.6, y3=17)  # người chơi HÁT CÙNG trước góc hát (mô phỏng)
for i in range(3):
    put(OCTA_BULB, (26.8 + (i - 1) * 0.8, 49 - (i % 2) * 0.5, 19 + i * 0.5), (0.09, 0.09, 0.09))
# V4.9 MUC 7: tieu thuong sau quay mau (guong vi tri vendor web)
for (vx, vz, vy) in [(-36.4, 11.3, 0), (-31.4, 11.3, 0), (-26.4, 11.3, 0), (-21.4, 11.3, 0),
                     (21.6, 11.3, 0), (26.6, 11.3, 0), (31.6, 11.3, 0), (23.6, 24.65, 0.5)]:
    person(vx, vz, rotz=math.pi, y3=vy, hat="nonla")
print("V49 vendors done", flush=True)
print("V43 tail done", flush=True)
SHOTS = [
    ("A-bung-binh", (-38, 14, 2.0), (0, -12, 5), 24),
    ("B-dinh-thang", (2, 33, 20.5), (-24, 6, 1.5), 24),
    ("a-duong-vao", (-79.5, -2.2, 3.8), (-4, -10, 1.0), 44),
    ("C1-sua", (22, -2.5, 3.0), (22, -10.4, 1.3), 35),
    ("C2-nuong", (-33.5, -3.2, 3.1), (-29.5, -10.3, 1.1), 35),
    ("C4-dau", (24, -16.5, 2.8), (24.2, -23.3, 1.2), 35),
]
_only = [x for a in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []) if a.startswith('only=') for x in a.split('=')[1].split(',')]
for (nm, cl, ct, ln) in SHOTS:
    if _only and nm.split('-')[0] not in _only: continue
    camera(cl, ct, lens=ln)
    sc.render.filepath = os.path.join(OUT, ("v50-%s-dem.png" % nm) if not DRAFT else ("v50-%s-draft.png" % nm))
    bpy.ops.render.render(write_still=True)
    print("RENDERED v47", nm, flush=True)
print("ALL V50 SHOTS DONE", flush=True)
