# -*- coding: utf-8 -*-
# render_xh3s.py — Nghiệm thu XH-3S (TRANG TRÍ BỜ + SINH HOẠT + SƯƠNG LẠNH):
# 3 shot TẦM MẮT theo ĐÚNG thông số index.html XH-3S: đèn bướm cao ~5,9u (bảng XH-3R),
# ghế 2,1/0,5/1,0 trên dải cỏ 5,53, kè 4 đoạn (khe bến §7 + 2 khe cầu Y), cầu bến 2 ngón +
# slip, cầu Y -282, ki-ốt + biển giá + biển nhiệt độ 17°C (tempNow 19h), sương 5 lớp.
# Nhân vật character.glb (1,82u) làm thước sống. Cycles CPU threads 2, OIDN, ACES.
# Dùng: blender5/blender -b --python render_xh3s.py
import bpy, math, os, random
from mathutils import Vector

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "renders")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=os.path.join(ROOT, "assets", "lake.glb"))
bpy.ops.import_scene.gltf(filepath=os.path.join(ROOT, "assets", "character.glb"))
SC = bpy.context.scene

def T2B(x, y, z):
    return (x, -z, y)

def hide(name):
    o = SC.objects.get(name)
    if o: o.location = T2B(0, -80, 0)

def place(name, tx, ty, tz, rotY=0.0, s=1.0):
    o = SC.objects.get(name)
    o.location = T2B(tx, ty, tz)
    o.rotation_euler = (0, 0, rotY)
    o.scale = (s, s, s)
    return o

def dup_root(src, tx, ty, tz, rotY, s=1.0):
    g = src.copy(); SC.collection.objects.link(g)
    for ch in list(src.children):
        c = ch.copy(); c.parent = g; SC.collection.objects.link(c)
    g.location = T2B(tx, ty, tz); g.rotation_euler = (0, 0, rotY); g.scale = (s, s, s)
    return g

def mat(name, rgb, rough=0.9, emis=None, estr=0.0):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bs = m.node_tree.nodes["Principled BSDF"]
    bs.inputs["Base Color"].default_value = (*rgb, 1.0)
    bs.inputs["Roughness"].default_value = rough
    if emis:
        bs.inputs["Emission Color"].default_value = (*emis, 1.0)
        bs.inputs["Emission Strength"].default_value = estr
    return m

def tex_mat(name, path):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bs = m.node_tree.nodes["Principled BSDF"]
    tex = m.node_tree.nodes.new("ShaderNodeTexImage")
    tex.image = bpy.data.images.load(path)
    m.node_tree.links.new(tex.outputs["Color"], bs.inputs["Base Color"])
    bs.inputs["Roughness"].default_value = 0.6
    return m

def box(name, size, tloc, m, rotY=0.0):
    bpy.ops.mesh.primitive_cube_add(location=T2B(*tloc))
    o = bpy.context.object; o.name = name; o.dimensions = (size[0], size[2], size[1])
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if rotY: o.rotation_euler = (0, 0, rotY)
    if m: o.data.materials.append(m)
    return o

def cylT(name, r, h, tloc, m, verts=20):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=T2B(*tloc))
    o = bpy.context.object; o.name = name
    if m: o.data.materials.append(m)
    return o

def sph(name, r, tloc, scale, m, rotZ=0.0):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=T2B(*tloc))
    o = bpy.context.object; o.name = name; o.scale = scale
    if rotZ: o.rotation_euler = (0, 0, rotZ)
    if m: o.data.materials.append(m)
    return o

def sign_plane(name, w, h, tloc, face_dir_blender, m):
    bpy.ops.mesh.primitive_plane_add(location=T2B(*tloc))
    o = bpy.context.object; o.name = name; o.dimensions = (w, h, 0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.rotation_euler = Vector(face_dir_blender).to_track_quat('Z', 'Y').to_euler()
    if m: o.data.materials.append(m)
    return o

# ---------- texture hoa văn thuyền như web (copy xh3r) ----------
def pattern_image():
    W, H = 512, 256
    img = bpy.data.images.new("HarnessPattern", W, H, alpha=False)
    img.colorspace_settings.name = 'sRGB'
    px = [1.0, 0.99, 0.97, 1.0] * (W * H)
    def stamp(cx, cy, r, col):
        for yy in range(max(0, cy - r), min(H, cy + r + 1)):
            for xx in range(max(0, cx - r), min(W, cx + r + 1)):
                if (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r:
                    i = (yy * W + xx) * 4
                    px[i] = col[0]; px[i + 1] = col[1]; px[i + 2] = col[2]; px[i + 3] = 1.0
    rnd = random.Random(11)
    for _ in range(110):
        stamp(rnd.randrange(W), rnd.randrange(H), rnd.choice([4, 5, 6]),
              rnd.choice([(0.35, 0.65, 0.95), (0.98, 0.45, 0.65), (0.25, 0.75, 0.70), (0.98, 0.75, 0.30)]))
    for _ in range(30):
        cx, cy = rnd.randrange(16, W - 16), rnd.randrange(16, H - 16)
        pc = rnd.choice([(0.30, 0.55, 0.95), (0.95, 0.40, 0.60)])
        for k in range(5):
            a = k * 2 * math.pi / 5.0
            stamp(cx + int(9 * math.cos(a)), cy + int(9 * math.sin(a)), 7, pc)
        stamp(cx, cy, 5, (0.98, 0.80, 0.25))
    img.pixels = px
    return img

pimg = pattern_image()
for m in bpy.data.materials:
    if m.name.startswith("SwanPattern"):
        m.use_nodes = True
        bs = m.node_tree.nodes["Principled BSDF"]
        tex = m.node_tree.nodes.new("ShaderNodeTexImage")
        tex.image = pimg
        m.node_tree.links.new(tex.outputs["Color"], bs.inputs["Base Color"])

# ---------- người (character.glb) — thước sống 1,82u; sit = pose ngồi ghế (xh3) ----------
CHAR_PARTS = [o for o in SC.objects if o.name in
              ("LegL", "LegR", "Torso", "tmpCollar", "ArmL", "ArmR", "Head", "HatNonLa", "HatBeanie", "HatCap", "Scarf")]
CHAR_BASE = {o.name: (tuple(o.location), o) for o in CHAR_PARTS}

def tint(o, rgb):
    if not o.data.materials: return
    m = o.data.materials[0].copy()
    m.use_nodes = True
    bs = m.node_tree.nodes.get("Principled BSDF")
    if bs: bs.inputs["Base Color"].default_value = (*rgb, 1.0)
    o.data = o.data.copy()
    o.data.materials[0] = m

def person(tx, ty, tz, rotY, shirt, pants, sit=False):
    c, s = math.cos(rotY), math.sin(rotY)
    for nm, (loc, src) in CHAR_BASE.items():
        o = src.copy(); SC.collection.objects.link(o)
        lx, ly, lz = loc
        o.rotation_euler = (0, 0, rotY)
        if sit and nm in ("LegL", "LegR"):
            o.rotation_euler.x = -1.15
            ly -= 0.16; lz -= 0.30
        elif sit:
            lz -= 0.34
        rx = lx * c - ly * s; ry = lx * s + ly * c
        o.location = (tx + rx, -tz + ry, ty + lz)
        o.hide_render = nm in ("HatNonLa", "HatCap")
        if nm in ("Torso", "ArmL", "ArmR", "tmpCollar"): tint(o, shirt)
        if nm in ("LegL", "LegR"): tint(o, pants)

for nm, (loc, src) in CHAR_BASE.items():
    src.hide_render = True

# ---------- môi trường đúng số XH-3R/XH-3S ----------
waterM = mat("Water", (0.020, 0.148, 0.255), 0.15, emis=(0.05, 0.18, 0.28), estr=0.0)   # đêm: phát sáng nhẹ như waterMats của game (set theo shot)
grassM = mat("Grass", (0.115, 0.235, 0.065), 0.98)
paveM = mat("Pave", (0.72, 0.77, 0.77), 0.9)
kerbM = mat("Kerb", (0.20, 0.185, 0.165), 0.95)
curbM = mat("Curb", (0.78, 0.75, 0.66), 0.9)
washM = mat("Wash", (0.88, 0.85, 0.78), 0.9)
vergeM = mat("Verge", (0.13, 0.27, 0.09), 0.98)

box("WaterPlane", (336, 0.1, 160), (-392, 4.85, 116), waterM)
box("Plateau", (144, 0.12, 61), (-288, 5.42, 5.5), grassM)
box("Promenade", (144, 0.12, 12), (-288, 5.43, 30), paveM)
# kè bắc 4 ĐOẠN XH-3S (khe cầu Y -318/-282, khe bến -266..-252, khe cầu đảo 3,2)
for (kw, kx) in [(32.8, -335.6), (33.6, -300.0), (14.8, -273.4), (24.4, -236.2)]:
    box("KeSeg", (kw, 1.14, 0.7), (kx, 4.93, 36), kerbM)
    box("CurbSeg", (kw, 0.09, 0.9), (kx, 5.6, 36), curbM)
box("VergeW", (86, 0.05, 1.3), (-309, 5.505, 35.35), vergeM)
box("VergeE", (24.4, 0.05, 1.3), (-236.2, 5.505, 35.35), vergeM)
box("BridgePad", (3.8, 0.08, 7), (-250, 5.30, 39.5), paveM)
cylT("IslandGrass", 15, 0.12, (-250, 5.42, 58), grassM)
cylT("IslandRim", 16.1, 1.2, (-250, 4.84, 58), kerbM)
cylT("IslandRing", 14.3, 0.05, (-250, 5.485, 58), paveM)
cylT("IslandLawn", 9.8, 0.06, (-250, 5.49, 58), grassM)
box("FarShore", (336, 0.1, 34), (-392, 8.9, 213), grassM)

place("ThuyTa", -262, 5.47, 58, -math.pi / 2)
place("IslandBridge", -250, 5.38, 39.5, 0)
pine_src = SC.objects.get("PineUmbrella")
place("PineUmbrella", -244.5, 5.47, 62.5, 0.7)
wl0 = place("Willow", -262.5, 5.47, 50.5, 50.5)
dup_root(wl0, -262.5, 5.47, 65.5, 65.5)
for (px, ps) in [(-344, 1.74), (-330, 1.66), (-316, 1.78), (-302, 1.70), (-288, 1.76),
                 (-274, 1.64), (-260, 1.79), (-246, 1.68), (-220, 1.72)]:
    dup_root(pine_src, px, 5.45, 25.2, (px * 7 + 25.2 * 13) % 3.14, ps)
    cylT("Wash", 0.22 * ps, 0.8, (px, 5.9, 25.2), washM, 10)
for (px, pz, py, ps) in [(-512, 206, 6.9, 1.85), (-450, 207, 7.0, 1.68), (-388, 209, 7.1, 1.70),
                         (-326, 206, 6.9, 1.79), (-280, 215, 7.9, 1.83), (-470, 227, 9.0, 1.75), (-300, 227, 9.0, 1.70)]:
    dup_root(pine_src, px, py, pz, (px * 7 + pz * 13) % 3.14, ps)
cherry_src = SC.objects.get("CherryTree")
dup_root(cherry_src, -253, 5.47, 25.2, 2.1, 1.5)   # phượng tím XH-3S scale 1,5
dup_root(cherry_src, -231, 5.47, 25.2, 0.6, 1.5)
hide("CherryTree")

boat_src = {nm: SC.objects.get(nm) for nm in ("SwanBoat", "SwanBoatPattern")}
def place_boat(pattern, x, z, rotY):
    dup_root(boat_src["SwanBoatPattern" if pattern else "SwanBoat"], x, 4.9, z, rotY)
place_boat(True, -272, 39.5, math.pi - 0.05)
place_boat(False, -241, 39.5, math.pi + 0.04)
place_boat(False, -259, 39.3, math.pi)
for (phi, pat, r) in [(-44, 1, 18.7), (0, 0, 18.6), (44, 1, 18.8)]:
    a = math.radians(phi); dx, dz = math.sin(a), math.cos(a)
    place_boat(pat == 1, -250 + dx * r, 58 + dz * r, math.atan2(-dx, -dz))
hide("SwanBoat"); hide("SwanBoatPattern")

# ---------- trang trí XH-3S đúng số code ----------
woodM = mat("DeckWood", (0.30, 0.18, 0.08), 0.9)
wood2M = mat("DeckWood2", (0.24, 0.14, 0.06), 0.9)
railM = mat("Rail", (0.90, 0.89, 0.86), 0.6)
creamM = mat("BenchCream", (0.80, 0.76, 0.68), 0.9)
legM = mat("BenchLeg", (0.10, 0.08, 0.065), 0.95)
# ghế bê tông: dài 2,1 · mặt ngồi đỉnh baseY+0,50 · tựa đỉnh ~baseY+1,0
def bench(x, z, baseY):
    box("BSeat", (2.1, 0.09, 0.55), (x, baseY + 0.455, z), creamM)
    bk = box("BBack", (2.1, 0.52, 0.08), (x, baseY + 0.76, z - 0.27), creamM); bk.rotation_euler.x = 0.0
    box("BLeg", (0.14, 0.41, 0.5), (x - 0.85, baseY + 0.205, z), legM)
    box("BLeg", (0.14, 0.41, 0.5), (x + 0.85, baseY + 0.205, z), legM)
for bx in (-346, -334, -322, -310, -298, -286, -274, -242, -230):
    bench(bx, 35.35, 5.53)
# đèn BƯỚM: cột 5,2 + cánh/panel ở +5,5..5,62 (tổng ~5,9u) + đĩa huy hiệu +4,05
postM = mat("LampPost", (0.008, 0.07, 0.03), 0.6)
panelM = mat("LampPanel", (0.95, 0.88, 0.72), 0.4, emis=(1.0, 0.72, 0.42), estr=0.0)
badgeM = mat("LampBadge", (0.92, 0.83, 0.62), 0.5, emis=(1.0, 0.66, 0.32), estr=0.0)
def butterfly(x, z):
    cylT("LPost", 0.08, 5.2, (x, 5.49 + 2.6, z), postM, 10)
    sph("LWing", 0.55, (x - 0.66, 5.49 + 5.62, z), (1.3, 0.52, 0.16), postM)
    sph("LWing", 0.55, (x + 0.66, 5.49 + 5.62, z), (1.3, 0.52, 0.16), postM)
    sph("LPanel", 0.5, (x, 5.49 + 5.5, z), (1.25, 0.5, 0.13), panelM)
    bd = cylT("LBadge", 0.27, 0.05, (x, 5.49 + 4.05, z), badgeM, 16)
    bd.rotation_euler = (math.pi / 2, 0, 0)
for lx in (-344, -326, -308, -290, -272, -254, -236):
    butterfly(lx, 27.5)
# bollard quanh đầu cầu đảo/bến
bolM = mat("Bollard", (0.07, 0.08, 0.07), 0.8)
bolTopM = mat("BolTop", (0.95, 0.92, 0.80), 0.5, emis=(1.0, 0.85, 0.55), estr=0.0)
for bx in (-268, -262, -256, -244, -238, -232):
    box("Bol", (0.14, 0.42, 0.14), (bx, 5.7, 34.55), bolM)
    box("BolTop", (0.15, 0.1, 0.15), (bx, 5.96, 34.55), bolTopM)
# cầu bến §7: 2 ngón + lối nối + lan can trên (2 thanh rút gọn thành mặt trên + trụ thưa)
box("PierW", (4, 0.18, 6.5), (-264, 5.41, 39.25), woodM)
box("PierE", (4, 0.18, 6.5), (-254, 5.41, 39.25), woodM)
box("PierLink", (14, 0.18, 1.2), (-259, 5.41, 36.6), woodM)
for sx in (-265.9, -252.1):
    box("PRail", (0.06, 0.06, 6.2), (sx, 6.35, 39.3), railM)
    box("PRail", (0.06, 0.06, 6.2), (sx, 6.0, 39.3), railM)
    for pz in (36.4, 38.5, 40.6, 42.3):
        box("PPost", (0.07, 0.85, 0.07), (sx, 5.92, pz), railM)
box("PRailF", (3.8, 0.06, 0.06), (-264, 6.35, 42.4), railM)
box("PRailF", (3.8, 0.06, 0.06), (-254, 6.35, 42.4), railM)
cylT("PierSignPost", 0.05, 2.2, (-267.6, 6.6, 34.6), postM, 8)
sign_plane("PierSign", 2.6, 0.65, (-267.6, 7.35, 34.6), (0, 1, 0), tex_mat("PierSignM", "/tmp/sign_pier.png"))
# cầu Y -282: thân + 2 cánh xoay ±0,62 + lan can thân
box("YStem", (1.8, 0.18, 5), (-282, 5.41, 38.5), woodM)
for sgn in (-1, 1):
    a = sgn * 0.62
    box("YArm", (1.4, 0.18, 2.6), (-282 + math.sin(a) * 1.3, 5.41, 41 + math.cos(a) * 1.3), woodM, a)
for sx in (-282.86, -281.14):
    box("YRail", (0.06, 0.06, 4.8), (sx, 6.35, 38.5), railM)
    box("YRail", (0.06, 0.06, 4.8), (sx, 6.0, 38.5), railM)
# ki-ốt đầu cầu đảo (world-coords, mặt quầy hướng +x như code rotY pi/2)
box("KFloor", (1.7, 0.06, 2.4), (-258.5, 5.52, 30.3), wood2M)
box("KCounter", (0.5, 1.05, 2.2), (-257.95, 6.04, 30.3), woodM)
box("KBack", (0.12, 2.3, 2.2), (-259.15, 6.64, 30.3), creamM)
box("KRoof", (1.9, 0.09, 2.7), (-258.45, 7.99, 30.3), mat("KRoofM", (0.42, 0.10, 0.07), 0.8))
for (px, pz) in [(-257.85, 29.25), (-257.85, 31.35), (-259.15, 29.25), (-259.15, 31.35)]:
    cylT("KPost", 0.045, 2.4, (px, 6.69, pz), wood2M, 8)
vestM = mat("Vest", (0.90, 0.48, 0.05), 0.8)
for vz in (29.7, 30.3, 30.9):
    box("KVest", (0.1, 0.44, 0.36), (-257.68, 7.08, vz), vestM)
sign_plane("KSign", 2.5, 0.55, (-257.78, 7.61, 30.3), (1, 0, 0), tex_mat("KSignM", "/tmp/sign_kiosk.png"))
sign_plane("KPrice", 1.5, 0.4, (-257.67, 6.65, 30.3), (1, 0, 0), tex_mat("KPriceM", "/tmp/sign_price.png"))
# biển nhiệt độ cạnh bến (mặt quay -z về đường dạo như code)
cylT("TPost", 0.045, 1.9, (-264.5, 6.45, 33.4), postM, 8)
sign_plane("TBoard", 1.5, 0.95, (-264.5, 7.05, 33.4), (0, 1, 0), tex_mat("TempM", "/tmp/sign_temp.png"))

# ---------- sương mặt hồ (texture alpha như xh3, 5 vị trí của code XH-3S) ----------
fog_img = bpy.data.images.new("FogTex", 256, 128, alpha=True)
fog_img.colorspace_settings.name = 'sRGB'
fpx = [0.0] * (256 * 128 * 4)
for yy in range(128):
    for xx in range(256):
        a = 0.0
        for (ex, ey, er) in ((128, 64, 92), (70, 60, 56), (186, 68, 62)):
            d = math.hypot(xx - ex, (yy - ey) * 2.0)
            a = max(a, max(0.0, 1.0 - d / er) * 0.55)
        i = (yy * 256 + xx) * 4
        fpx[i] = 0.90; fpx[i + 1] = 0.94; fpx[i + 2] = 0.97; fpx[i + 3] = a
fog_img.pixels = fpx
fogM = bpy.data.materials.new("LakeFog")
fogM.use_nodes = True
fbs = fogM.node_tree.nodes["Principled BSDF"]
fbs.inputs["Base Color"].default_value = (0.87, 0.91, 0.93, 1.0)
fbs.inputs["Roughness"].default_value = 1.0
ftex = fogM.node_tree.nodes.new("ShaderNodeTexImage"); ftex.image = fog_img
fmul = fogM.node_tree.nodes.new("ShaderNodeMath"); fmul.operation = 'MULTIPLY'
fogM.node_tree.links.new(ftex.outputs["Alpha"], fmul.inputs[0])
fogM.node_tree.links.new(fmul.outputs[0], fbs.inputs["Alpha"])
def fog_plane(fx, fy, fz, fw, fd):
    bpy.ops.mesh.primitive_plane_add(location=T2B(fx, fy, fz))
    o = bpy.context.object; o.dimensions = (fw, fd, 0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(fogM)
for (fx, fy, fz, fw, fd) in [(-285, 5.35, 52, 95, 26), (-335, 5.55, 68, 80, 30), (-252, 5.28, 88, 70, 24),
                             (-395, 5.6, 120, 120, 34), (-300, 5.45, 150, 90, 26)]:
    fog_plane(fx, fy, fz, fw, fd)

# ---------- xe đạp harness (đúng kích thước code: bánh r0,34, rider ngồi +0,52) ----------
def bike(tx, tz, rotY, col):
    g = bpy.data.objects.new("Bike", None)
    g.location = T2B(tx, 5.49, tz); g.rotation_euler = (0, 0, rotY)
    SC.collection.objects.link(g)
    tireM = mat("Tire", (0.05, 0.05, 0.06), 0.85)
    frM = mat("BikeFr", col, 0.5)
    for wz in (0.55, -0.55):
        bpy.ops.mesh.primitive_torus_add(major_radius=0.34, minor_radius=0.045)
        o = bpy.context.object; o.parent = g
        o.location = (0, -wz, 0.34); o.rotation_euler = (0, math.pi / 2, 0)
        o.data.materials.append(tireM)
    for (sz, sy, ez, ey) in [(-0.55, 0.34, -0.05, 0.62), (-0.05, 0.62, 0.55, 0.34), (-0.05, 0.62, 0.42, 0.88), (-0.55, 0.34, -0.38, 0.78)]:
        bpy.ops.mesh.primitive_cube_add(location=(0, -(sz + ez) / 2, (sy + ey) / 2))
        o = bpy.context.object; o.parent = g
        o.dimensions = (0.045, abs(ez - sz) + 0.05, abs(ey - sy) + 0.05)
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        o.rotation_euler = (math.atan2(ey - sy, ez - sz) * 0 + (0.62 if False else 0), 0, 0)
        o.data.materials.append(frM)
    return g

# ---------- ánh sáng / camera ----------
def setup(sun_energy, sun_rot, sun_color, bg, bg_strength, exposure):
    for o in list(SC.objects):
        if o.type == 'LIGHT' and not o.name.startswith('LampPt'):
            bpy.data.objects.remove(o, do_unlink=True)
    sun = bpy.data.objects.new("Sun", bpy.data.lights.new("Sun", 'SUN'))
    sun.data.energy = sun_energy; sun.data.color = sun_color
    sun.rotation_euler = sun_rot
    SC.collection.objects.link(sun)
    w = bpy.data.worlds.new("W"); SC.world = w; w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (*bg, 1.0)
    w.node_tree.nodes["Background"].inputs[1].default_value = bg_strength
    SC.view_settings.view_transform = 'ACES 1.3'
    SC.view_settings.exposure = exposure

cam = bpy.data.objects.new("Cam", bpy.data.cameras.new("Cam"))
cam.data.lens = 38
SC.collection.objects.link(cam); SC.camera = cam

XH3S_ONLY = os.environ.get('XH3S_ONLY', '')   # vd XH3S_ONLY=23: chỉ render shot 2+3 (scene vẫn dựng đủ)
def shot(out, camT, tgtT, res=(1152, 768)):
    _sn = '1' if 'prom' in out else ('2' if 'dawn' in out else '3')
    if XH3S_ONLY and _sn not in XH3S_ONLY:
        print("SKIP", out); return
    cam.location = T2B(*camT)
    tgt = Vector(T2B(*tgtT))
    cam.rotation_euler = (tgt - cam.location).to_track_quat('-Z', 'Y').to_euler()
    SC.render.resolution_x, SC.render.resolution_y = res
    SC.render.filepath = os.path.join(OUT, out)
    bpy.ops.render.render(write_still=True)
    print("RENDERED", out)

SC.render.engine = 'CYCLES'
SC.cycles.samples = 32
SC.cycles.use_denoising = True
SC.cycles.denoiser = 'OPENIMAGEDENOISE'
SC.render.threads_mode = 'FIXED'; SC.render.threads = 2

# ===== SHOT 1: đường dạo 19:00 — đèn bướm sáng, cặp ngồi ghế, tình nhân đi đôi, xe đạp, sương nhẹ =====
# LƯU Ý harness: person() bị GƯƠNG hướng so với game (T2B) — rotY truyền vào = -rotY game.
panelM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 4.0
badgeM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
bolTopM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
waterM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.5
fmul.inputs[1].default_value = 0.20 / 0.55
for lx in (-344, -326, -308, -290, -272, -254, -236):
    pt = bpy.data.objects.new("LampPt", bpy.data.lights.new("LampPt", 'POINT'))
    pt.data.energy = 40; pt.data.color = (1.0, 0.62, 0.25); pt.data.shadow_soft_size = 0.4
    pt.location = T2B(lx, 10.9, 27.5)
    SC.collection.objects.link(pt)
person(-310.5, 5.73, 35.3, 0.06, (0.72, 0.28, 0.32), (0.16, 0.15, 0.20), sit=True)   # cặp ngồi ghế -310
person(-309.5, 5.73, 35.3, -0.05, (0.18, 0.28, 0.45), (0.09, 0.09, 0.11), sit=True)
person(-300, 5.49, 31.7, math.pi / 2, (0.80, 0.33, 0.45), (0.12, 0.15, 0.26))         # tình nhân đi đôi hướng tây (lane 31,7 + B lệch -0,85)
person(-300, 5.49, 30.85, math.pi / 2, (0.12, 0.20, 0.38), (0.07, 0.08, 0.10))
person(-284, 5.49, 28.4, -math.pi / 2, (0.30, 0.42, 0.50), (0.20, 0.18, 0.15))        # người đi bộ hướng đông
bike(-292, 33.4, math.pi / 2, (0.62, 0.10, 0.07))                                     # xe đạp lane ngoài hướng đông
person(-292, 6.01, 33.4, -math.pi / 2, (0.30, 0.42, 0.55), (0.11, 0.11, 0.13), sit=True)
setup(1.1, (math.radians(80), 0, math.radians(-100)), (0.50, 0.62, 0.95), (0.045, 0.07, 0.13), 0.75, 0.15)
shot("xh3s-prom-night.png", (-272, 7.2, 33.8), (-316, 5.9, 34.6))

# ===== SHOT 2: sáng sớm — sương rõ + chạy bộ =====
panelM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.0
badgeM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.0
bolTopM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.0
fmul.inputs[1].default_value = 1.45
waterM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.0
for o in list(SC.objects):
    if o.name.startswith("LampPt"): o.hide_render = True
person(-272, 5.49, 32.6, -math.pi / 2, (0.82, 0.14, 0.10), (0.09, 0.09, 0.11))        # chạy bộ sáng sớm hướng đông
person(-298, 5.49, 30.8, math.pi / 2, (0.25, 0.35, 0.55), (0.15, 0.14, 0.12))         # đi bộ sớm hướng tây
setup(2.8, (math.radians(63), 0, math.radians(115)), (1.0, 0.80, 0.58), (0.45, 0.56, 0.68), 0.8, -0.1)
shot("xh3s-dawn.png", (-240, 8.2, 31), (-322, 5.4, 60))

# ===== SHOT 3: cận ki-ốt + biển nhiệt độ (19:00) =====
panelM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 4.0
badgeM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
bolTopM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 2.0
fmul.inputs[1].default_value = 0.20 / 0.55
waterM.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = 0.5
for o in list(SC.objects):
    if o.name.startswith("LampPt"): o.hide_render = False
person(-258.85, 5.49, 30.3, -math.pi / 2, (0.85, 0.55, 0.15), (0.22, 0.18, 0.14))      # người bán vé sau quầy (mặt +x về khách)
person(-256.6, 5.49, 30.9, math.pi / 2, (0.65, 0.25, 0.40), (0.13, 0.14, 0.22))        # khách đứng trước quầy (mặt -x về quầy)
person(-256.6, 5.49, 29.8, math.pi / 2, (0.15, 0.30, 0.50), (0.08, 0.08, 0.10))
setup(1.1, (math.radians(80), 0, math.radians(-100)), (0.50, 0.62, 0.95), (0.045, 0.07, 0.13), 0.75, 0.15)
shot("xh3s-kiosk.png", (-242, 7.2, 28.0), (-260.5, 6.5, 31.8), (1024, 768))   # từ đông-bắc: mặt quầy +x hướng camera, tia tới biển nhiệt độ (-264,5) lách phía nam ki-ốt (bản trước bị mái che)
print("XH3S RENDERS DONE")
