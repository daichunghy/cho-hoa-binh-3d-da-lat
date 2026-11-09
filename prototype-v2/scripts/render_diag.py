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
    return min(5.5, (-52 - x) * 0.07) if x < -52 else 0.0  # V5.5: nap 5.5

def groundH(x, z):
    if 14.5 <= x <= 20.5 and -30 <= z <= 9: return 17.14 - (z + 30) * 0.11282
    if 29 <= x <= 33 and 12 <= z <= 26.8: return innerStairH(z)
    if 14 <= x <= 21 and 7 <= z <= 12: return 12.6
    if 21 <= x <= 33 and 7 <= z <= 12.2: return 12.6
    if -34 <= x <= 34 and 12 <= z <= 28: return 0.5
    if -58 <= x <= -35 and -16.5 <= z <= -2: return (entryRampY(x) + 0.11) if x < -52 else 0.0  # V5.5: THEM BAC
    if -131 <= x <= -59 and -13.9 <= z <= -11.1: return entryRampY(x) + 0.11  # V5.5: via he bac
    if -82.5 <= x <= -51.5 and 10.5 <= z <= 13.9: return entryRampY(x) + 0.11  # via he nam
    if -133 <= x < -58 and -17.5 <= z <= 24:
        r = entryRampY(x)
        return r + 0.11 if (z < -14.5 or (13.5 < z <= 20.2)) else r  # V5.5: hanh lang keo dai
    if -133 <= x < -52 and z > 24: return entryRampY(x)  # V5.5: nen nha nam keo dai
    if -84 <= x <= -34 and 13.5 < z <= 24: return entryRampY(x) + 0.05  # V5.5: them sap nam
    if x < -52 and -17.5 <= z <= 24: return entryRampY(x)  # V5.5
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
sc.cycles.samples = 4 if DRAFT else 16
sc.cycles.use_denoising = True
sc.cycles.use_adaptive_sampling = True
sc.render.threads_mode = 'FIXED'
sc.render.threads = 2  # V5.3: RAM chat
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
box("Plaza", (170, 130, 0.2), (0, -18, -0.1), (0.59, 0.54, 0.47))  # V5.5: san sang hon (khop web 0x978a78)
box("Road", (170, 30, 0.22), (0, -5, 0.0), (0.27, 0.24, 0.21))  # V5.5: rong 30 (three z -10..20)
box("RoadW", (52, 30, 0.22), (-109, -5, 3.99), (0.27, 0.24, 0.21), rot=(0, 0.0699, 0))  # V5.5: doan doc keo dai x -135..-83 (bam entryRampY)
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
shophouse(-60.5, -26.5, (0.62, 0.52, 0.40), (0.65, 0.20, 0.14), 15.85)  # V5.5: day nam z 26.5
shophouse(-53.0, -26.5, (0.55, 0.46, 0.38), (0.16, 0.36, 0.55), 12.8)
shophouse(-38.5, -26.5, (0.66, 0.55, 0.42), (0.20, 0.45, 0.30), 15.85)
shophouse(-62.0, 24, (0.58, 0.48, 0.40), (0.55, 0.35, 0.16), 12.8, z0=13.4)  # V5.5: day bac z -24
shophouse(-52.0, 24.5, (0.52, 0.44, 0.36), (0.65, 0.20, 0.14), 15.85, z0=13.7)
shophouse(-42.0, 23, (0.60, 0.50, 0.40), (0.16, 0.36, 0.55), 12.8, z0=12.8)
shophouse(-80, -26.5, (0.55, 0.46, 0.38), (0.65, 0.20, 0.14), 12.8, z0=1.9)  # V5.5: nha keo dai nam (bam doc)
shophouse(-95, -26.5, (0.62, 0.52, 0.40), (0.20, 0.45, 0.30), 15.85, z0=3.0)
shophouse(-110, -26.5, (0.66, 0.55, 0.42), (0.16, 0.36, 0.55), 12.8, z0=4.05)
shophouse(-124, -27.5, (0.58, 0.48, 0.40), (0.55, 0.35, 0.16), 15.85, z0=5.0)
shophouse(-80, 24, (0.52, 0.44, 0.36), (0.65, 0.20, 0.14), 12.8, z0=13.4)  # V5.5: nha keo dai bac (tren suon)
shophouse(-96, 24.5, (0.55, 0.46, 0.38), (0.65, 0.20, 0.14), 15.85, z0=13.7)
shophouse(-112, 25, (0.62, 0.52, 0.40), (0.55, 0.20, 0.14), 12.8, z0=14.0)
shophouse(-126, 25, (0.66, 0.55, 0.42), (0.20, 0.45, 0.30), 12.8, z0=14.0)
# cổng chào tại spawn
for py in (-17.5, 13.5):
    ebox("GatePost", (0.55, 0.55, 5.2), (-131, py, 8.2), mat_plain("GateP", (0.35, 0.22, 0.12)))
ebox("GateBeam", (0.5, 31.5, 0.55), (-131, -2, 11.0), mat_plain("GateBm", (0.30, 0.19, 0.10)))
ebox("GateSign", (0.34, 8.2, 1.05), (-131, -2, 10.3), SignGlowM)  # V5.5: cong tai x -131, nen doc 5.53
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
for (hx, hy, hz) in [(-72, -24.2, 1.4), (-64, -24.2, 0.85), (-56, -24.2, 0.3), (-47, -24.2, 0.05),
                     (-88, -24.2, 2.5), (-104, -24.2, 3.6), (-120, -24.2, 4.75),
                     (-53.5, 16.2, 0.2), (-48.5, 16.2, 0.11), (-43.5, 16.2, 0.11),
                     (-88, 17.2, 2.6), (-104, 17.2, 3.75), (-120, 17.2, 4.9),
                     (-32, -3.4, 0), (-16, -3.6, 0), (-30, 14.5, 0), (-18, 14.2, 0),
                     (-8, 33, 17), (12, 33, 17), (24, 40, 17), (-20, 44, 17)]:
    hydra(hx, hy, hz)
ENTRY_LAMPS = [(-74, 12.5), (-58, 12.5), (-43, 12.5), (-66, -18.6), (-50, -18.6), (-100, 12.5), (-100, -18.6), (-126, 12.5)]  # V5.5: den theo le mo rong + doan keo dai (blender y = -three z)
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
# --- PROBE: liet ke object giao vung x -165..-120, y -30..20, z 8..18 ---
import mathutils
for o in bpy.data.objects:
    if o.type != 'MESH': continue
    try:
        bb = [o.matrix_world @ mathutils.Vector(c) for c in o.bound_box]
    except Exception:
        continue
    xs = [v.x for v in bb]; ys = [v.y for v in bb]; zs = [v.z for v in bb]
    if min(xs) < -100 and max(xs) > -165 and min(ys) < 20 and max(ys) > -30 and min(zs) < 20 and max(zs) > 5:
        print("PROBE-HIT", o.name, "x[%.1f..%.1f] y[%.1f..%.1f] z[%.1f..%.1f]" % (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)), flush=True)
print("PROBE DONE", flush=True)
# --- RAYCAST tu camera K: trung tam + 4 goc phan tu khung ---
bpy.context.view_layer.update()
_dg = bpy.context.evaluated_depsgraph_get()
_o = mathutils.Vector((-136.2, -5.6, 13.5))
_t = mathutils.Vector((-126, -5.6, 7.28))
_fwd = (_t - _o).normalized()
_right = _fwd.cross(mathutils.Vector((0, 0, 1))).normalized()
_up = _right.cross(_fwd).normalized()
for (fx, fy) in [(0, 0), (-0.3, 0.1), (0.3, 0.1), (-0.3, -0.25), (0.3, -0.25), (0, -0.4), (0, 0.35)]:
    _d = (_fwd + _right * fx * 1.4 + _up * fy * 1.05).normalized()
    _hit, _loc, _n, _idx, _obj, _m = bpy.context.scene.ray_cast(_dg, _o, _d, distance=400)
    print("RAY", fx, fy, "->", (_obj.name if _hit else "SKY"), ("dist %.1f" % ((_loc - _o).length)) if _hit else "", flush=True)
print("RAYCAST DONE", flush=True)
# --- DIAG: lighting toi gian + 3 shot truy vat che o cong ---
world_bg((0.020, 0.034, 0.068), 1.2)
make_sun(euler=(math.radians(65), 0, math.radians(30)), energy=0.5)
sc.view_settings.exposure = 1.12
DSHOTS = [
    ("D1-goc-K-goc", (-136.2, -5.6, 13.5), (-126, -5.6, 7.28), 25),
    ("D2-tay-tren-cao", (-152, -5.6, 26), (-120, -5.6, 5), 30),
    ("D3-trong-cong", (-116, -5.6, 11), (-70, -4, 2), 30),
]
for (nm, cl, ct, ln) in DSHOTS:
    camera(cl, ct, lens=ln)
    sc.render.filepath = os.path.join(OUT, "diag55-%s-draft.png" % nm)
    bpy.ops.render.render(write_still=True)
    print("RENDERED diag", nm, flush=True)
print("DIAG DONE", flush=True)
