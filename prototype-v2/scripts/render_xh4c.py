# -*- coding: utf-8 -*-
# render_xh4c.py — Nghiệm thu XH-4C (PHỐI MÀU LẠI + TIẾT DIỆN theo research/28):
# nước xám bạc ngày / chàm tối + emissive #4a5a86, lát #a9aba8, cỏ olive, đường nhựa + vạch,
# dải tactile, kè bắc 3 đoạn -> CỎ DỐC (đoạn đông giữ kè đá + bó vỉa #b9bcba), cây lá rộng
# NGHIÊNG ra hồ + vôi xám, hoa giấy tím, thông tint xám xanh, đêm Thủy Tạ MAGENTA + vệt phản chiếu.
# Màu harness = giá trị TUYẾN TÍNH của mã hex đích (game: canvas sRGB -> linear khi render).
# Nhân vật character.glb (1,82u) làm thước sống. Cycles CPU threads 2, OIDN, ACES.
# Dùng: blender -b --python render_xh4c.py   (XH4C_ONLY=13 chỉ render shot 1+3)
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

def tube(name, a3, b3, r, m):
    # ống giữa 2 điểm tọa độ THREE (như xh4cTube trong game)
    a = Vector(T2B(*a3)); b = Vector(T2B(*b3))
    d = b - a; ln = d.length
    bpy.ops.mesh.primitive_cylinder_add(vertices=8, radius=r, depth=ln, location=(a + b) / 2)
    o = bpy.context.object; o.name = name
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(d.normalized())
    o.rotation_mode = 'XYZ'
    if m: o.data.materials.append(m)
    return o

def sign_plane(name, w, h, tloc, face_dir_blender, m):
    bpy.ops.mesh.primitive_plane_add(location=T2B(*tloc))
    o = bpy.context.object; o.name = name; o.dimensions = (w, h, 0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.rotation_euler = Vector(face_dir_blender).to_track_quat('Z', 'Y').to_euler()
    if m: o.data.materials.append(m)
    return o

# ---------- texture hoa văn thuyền như web (copy xh3s) ----------
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

# ---------- XH-4C: tint material lake.glb như runtime game (Pine xám xanh, Trunk nâu xám, LeafGreen sẫm) ----------
XH4C_TINT = {"PineDark": (0.042, 0.079, 0.040), "PineMid": (0.062, 0.119, 0.073),
             "PineLight": (0.104, 0.168, 0.126), "Trunk": (0.163, 0.133, 0.108),
             "LeafGreen": (0.047, 0.086, 0.030)}
for m in bpy.data.materials:
    for k, v in XH4C_TINT.items():
        if m.name.startswith(k) and m.use_nodes:
            bs = m.node_tree.nodes.get("Principled BSDF")
            if bs: bs.inputs["Base Color"].default_value = (*v, 1.0)

# ---------- người (character.glb) — thước sống 1,82u ----------
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

# ---------- môi trường: số XH-4C (màu tuyến tính của hex đích) ----------
waterM = mat("Water", (0.262, 0.310, 0.335), 0.15, emis=(0.069, 0.104, 0.237), estr=0.0)  # ngày #8b979c; tối: tint chàm + emissive #4a5a86 (set theo shot)
grassM = mat("Grass", (0.132, 0.161, 0.027), 0.98)     # olive #66702f
paveM = mat("Pave", (0.402, 0.410, 0.396), 0.9)        # lát #a9aba8
kerbM = mat("Kerb", (0.20, 0.185, 0.165), 0.95)        # kè đá giữ #7e776c
curbM = mat("Curb", (0.484, 0.502, 0.490), 0.9)        # bó vỉa #b9bcba
washM = mat("Wash", (0.636, 0.636, 0.588), 0.9)        # vôi gốc #cfcfc8
vergeM = mat("Verge", (0.062, 0.083, 0.022), 0.98)     # cỏ vệt sẫm #46512a
asphaltM = mat("Asphalt", (0.088, 0.108, 0.126), 0.97) # nhựa #545c63
dashM = mat("Dash", (0.55, 0.54, 0.48), 0.9)
tactM = mat("Tactile", (0.278, 0.290, 0.305), 0.9)     # tactile #8f9296

box("WaterPlane", (336, 0.1, 160), (-392, 4.85, 116), waterM)
box("Plateau", (144, 0.12, 61), (-288, 5.42, 5.5), grassM)
box("Promenade", (144, 0.12, 12), (-288, 5.43, 30), paveM)
# XH-4C: đường nhựa (z 17,4..23,0) + vạch đứt giữa + dải tactile z 30,0
box("Road", (144, 0.05, 5.6), (-288, 5.475, 20.2), asphaltM)
for dx in range(-356, -220, 8):
    box("Dash", (1.6, 0.012, 0.18), (dx, 5.503, 20.2), dashM)
box("Tactile", (144, 0.012, 0.45), (-288, 5.5, 30.0), tactM)
# XH-4C: mép bắc — 3 đoạn CỎ DỐC thay kè (slope nghiêng, cạnh nam chạm nước), đoạn ĐÔNG giữ kè đá + bó vỉa
for (kw, kx) in [(32.8, -335.6), (33.6, -300.0), (14.8, -273.4)]:
    sl = box("Slope", (kw, 0.1, 3.0), (kx, 5.14, 37.2), grassM)
    sl.rotation_euler.x = 0.23
box("KeSegE", (24.4, 1.14, 0.7), (-236.2, 4.93, 36), kerbM)
box("CurbSegE", (24.4, 0.09, 0.9), (-236.2, 5.6, 36), curbM)
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
for (px, ps) in [(-344, 1.74), (-330, 1.66), (-302, 1.70),
                 (-274, 1.64), (-246, 1.68)]:   # XH-4C+: phá hàng đều — chỉ còn 5 thông (research/29)
    dup_root(pine_src, px, 5.45, 25.2, (px * 7 + 25.2 * 13) % 3.14, ps)
    cylT("Wash", 0.22 * ps, 0.8, (px, 5.9, 25.2), washM, 10)
# hàng hậu cảnh sau đường (z 14): 2 thông thẳng
for (px, ps) in [(-312, 1.70), (-228, 1.80)]:
    dup_root(pine_src, px, 5.42, 14, (px * 7 + 14 * 13) % 3.14, ps)
# đảo: thêm thông #2
dup_root(pine_src, -245, 5.44, 51, 1.1, 1.60)
for (px, pz, py, ps) in [(-512, 206, 6.9, 1.85), (-450, 207, 7.0, 1.68), (-388, 209, 7.1, 1.70),
                         (-326, 206, 6.9, 1.79), (-280, 215, 7.9, 1.83), (-470, 227, 9.0, 1.75), (-300, 227, 9.0, 1.70)]:
    dup_root(pine_src, px, py, pz, (px * 7 + pz * 13) % 3.14, ps)
cherry_src = SC.objects.get("CherryTree")
dup_root(cherry_src, -253, 5.47, 25.2, 2.1, 1.5)
dup_root(cherry_src, -231, 5.47, 25.2, 0.6, 1.5)
dup_root(cherry_src, -254, 5.47, 65, 1.3, 1.3)   # XH-4C+: phượng tím trên đảo (ảnh 36)
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

# ---------- trang trí XH-3S (giữ số) ----------
woodM = mat("DeckWood", (0.30, 0.18, 0.08), 0.9)
wood2M = mat("DeckWood2", (0.24, 0.14, 0.06), 0.9)
railM = mat("Rail", (0.90, 0.89, 0.86), 0.6)
creamM = mat("BenchCream", (0.80, 0.76, 0.68), 0.9)
legM = mat("BenchLeg", (0.10, 0.08, 0.065), 0.95)
def bench(x, z, baseY):
    box("BSeat", (2.1, 0.09, 0.55), (x, baseY + 0.455, z), creamM)
    box("BBack", (2.1, 0.52, 0.08), (x, baseY + 0.76, z - 0.27), creamM)
    box("BLeg", (0.14, 0.41, 0.5), (x - 0.85, baseY + 0.205, z), legM)
    box("BLeg", (0.14, 0.41, 0.5), (x + 0.85, baseY + 0.205, z), legM)
for bx in (-346, -334, -322, -310, -298, -286, -274, -242, -230):
    bench(bx, 35.35, 5.53)
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
bolM = mat("Bollard", (0.07, 0.08, 0.07), 0.8)
bolTopM = mat("BolTop", (0.95, 0.92, 0.80), 0.5, emis=(1.0, 0.85, 0.55), estr=0.0)
for bx in (-268, -262, -256, -244, -238, -232):
    box("Bol", (0.14, 0.42, 0.14), (bx, 5.7, 34.55), bolM)
    box("BolTop", (0.15, 0.1, 0.15), (bx, 5.96, 34.55), bolTopM)
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
sign_plane("PierSign", 2.6, 0.65, (-267.6, 7.35, 34.6), (0, 1, 0), mat("SignBlue", (0.10, 0.16, 0.30), 0.6))
box("YStem", (1.8, 0.18, 5), (-282, 5.41, 38.5), woodM)
for sgn in (-1, 1):
    a = sgn * 0.62
    box("YArm", (1.4, 0.18, 2.6), (-282 + math.sin(a) * 1.3, 5.41, 41 + math.cos(a) * 1.3), woodM, a)
for sx in (-282.86, -281.14):
    box("YRail", (0.06, 0.06, 4.8), (sx, 6.35, 38.5), railM)
    box("YRail", (0.06, 0.06, 4.8), (sx, 6.0, 38.5), railM)
box("KFloor", (1.7, 0.06, 2.4), (-258.5, 5.52, 30.3), wood2M)
box("KCounter", (0.5, 1.05, 2.2), (-257.95, 6.04, 30.3), woodM)
box("KBack", (0.12, 2.3, 2.2), (-259.15, 6.64, 30.3), creamM)
box("KRoof", (1.9, 0.09, 2.7), (-258.45, 7.99, 30.3), mat("KRoofM", (0.42, 0.10, 0.07), 0.8))
for (px, pz) in [(-257.85, 29.25), (-257.85, 31.35), (-259.15, 29.25), (-259.15, 31.35)]:
    cylT("KPost", 0.045, 2.4, (px, 6.69, pz), wood2M, 8)
vestM = mat("Vest", (0.90, 0.48, 0.05), 0.8)
for vz in (29.7, 30.3, 30.9):
    box("KVest", (0.1, 0.44, 0.36), (-257.68, 7.08, vz), vestM)
sign_plane("KSign", 2.5, 0.55, (-257.78, 7.61, 30.3), (1, 0, 0), mat("SignTeal", (0.05, 0.25, 0.30), 0.6))
cylT("TPost", 0.045, 1.9, (-264.5, 6.45, 33.4), postM, 8)
sign_plane("TBoard", 1.5, 0.95, (-264.5, 7.05, 33.4), (0, 1, 0), mat("TempBoard", (0.12, 0.13, 0.16), 0.6))

# ---------- XH-4C: cây lá rộng NGHIÊNG + hoa giấy (đúng helper game) ----------
trunkM4 = mat("Trunk4", (0.163, 0.133, 0.108), 0.95)
leafM4 = mat("Leaf4", (0.027, 0.046, 0.023), 1.0)
def lean_tree(x, z, baseY, dx, dz, ang, s):
    ux, uy, uz = dx * math.sin(ang), math.cos(ang), dz * math.sin(ang)
    p1 = (x + ux * 2.1 * s, baseY + uy * 2.1 * s, z + uz * 2.1 * s)
    a2 = ang * 0.78
    vx, vy, vz = dx * math.sin(a2), math.cos(a2), dz * math.sin(a2)
    p2 = (p1[0] + vx * 2.3 * s, p1[1] + vy * 2.3 * s, p1[2] + vz * 2.3 * s)
    tube("Trunk", (x, baseY - 0.2, z), p1, 0.17 * s, trunkM4)
    tube("WashT", (x, baseY - 0.2, z), (x + ux * 1.0 * s, baseY + uy * 1.0 * s, z + uz * 1.0 * s), 0.19 * s, washM)
    tube("Trunk2", p1, p2, 0.115 * s, trunkM4)
    for (ox, oy, oz, r) in [(0, 0.55, 0, 2.0), (-1.25, 0.1, -0.35, 1.5), (1.25, 0.15, 0.3, 1.55),
                            (-0.4, 0.25, 1.15, 1.4), (0.5, 0.3, 1.05, 1.45), (0.05, -0.3, 0.65, 1.25)]:
        sph("Canopy", r * s, (p2[0] + (ox + dx * 0.5) * s, p2[1] + oy * s, p2[2] + (oz + dz * 0.5) * s), (1, 1, 0.58), leafM4)
# XH-4C+ theo research/29: cụm cây mép nước (lá rộng nghiêng + THÔNG NGHIÊNG xen) + hàng trong/hậu cảnh
lean_tree(-349, 35.3, 5.42, 0, 1, 0.62, 1.05)
lean_tree(-343, 35.3, 5.42, 0, 1, 0.55, 0.95)
lean_tree(-324, 35.3, 5.42, 0, 1, 0.52, 1.10)
lean_tree(-298, 35.3, 5.42, 0, 1, 0.68, 0.98)
lean_tree(-291, 35.3, 5.42, 0, 1, 0.50, 1.08)
lean_tree(-240, 35.3, 5.42, 0, 1, 0.60, 1.00)
lean_tree(-226, 35.3, 5.42, 0, 1, 0.58, 0.96)
def lean_pine(x, z, s, tilt):
    g = dup_root(pine_src, x, 5.30, z, 0.0, s)
    g.rotation_euler = (tilt, 0, 0)   # blender +x rotation: đỉnh đổ về -y blender = +z three (ra hồ)
    tube("WashT", (x, 5.20, z), (x, 5.30 + 0.95 * math.cos(tilt), z + 0.95 * math.sin(tilt)), 0.20 * s, washM)
lean_pine(-335, 35.3, 1.55, 0.50)
lean_pine(-272, 35.3, 1.48, 0.55)
lean_pine(-233, 35.3, 1.42, 0.50)
lean_tree(-316, 25.2, 5.47, 0, 1, 0.14, 1.12)   # lá rộng THẲNG hàng trong
lean_tree(-260, 25.2, 5.47, 0, 1, 0.10, 1.05)
lean_tree(-335, 14, 5.44, 0, 1, 0.12, 1.15)     # hậu cảnh sau đường
lean_tree(-283, 14, 5.44, 0, 1, 0.16, 1.05)
lean_tree(-252, 14, 5.44, 0, 1, 0.10, 1.10)
lean_tree(-236, 58, 5.44, 1, 0, 0.50, 0.92)     # lá rộng nghiêng mép đông đảo
bougLeafM = mat("BougLeaf", (0.033, 0.081, 0.026), 1.0)
bougFlM = mat("BougFl", (0.335, 0.023, 0.262), 0.9)
def bougain(x, z):
    for (ox, oy, oz, r, fl) in [(0, 0.95, 0, 1.5, 0), (-1.15, 0.7, 0.25, 1.1, 0), (1.15, 0.75, -0.2, 1.15, 0),
                                (-0.6, 1.55, 0.35, 0.72, 1), (0.45, 1.7, -0.3, 0.78, 1), (1.35, 1.25, 0.3, 0.6, 1),
                                (-1.4, 1.15, -0.35, 0.62, 1), (0.05, 1.3, 0.75, 0.66, 1), (0.9, 0.95, 0.65, 0.55, 1)]:
        sph("Boug", r, (x + ox, 5.49 + oy, z + oz), (1, 1, 0.72), bougFlM if fl else bougLeafM)
bougain(-296, 24.7); bougain(-323, 24.8); bougain(-240, 24.9)

# ---------- sương mặt hồ (copy xh3s) ----------
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

# ---------- XH-4C: Thủy Tạ MAGENTA + vệt phản chiếu (chỉ hiện ở shot tối) ----------
magM = mat("TTMagenta", (0.08, 0.01, 0.07), 0.5, emis=(0.699, 0.079, 0.643), estr=0.0)
box("TTWin", (0.14, 1.15, 7.6), (-265.85, 7.55, 58), magM)
box("TTSign", (0.14, 0.5, 5.2), (-265.85, 9.75, 58), magM)
magPt = bpy.data.objects.new("MagPt", bpy.data.lights.new("MagPt", 'POINT'))
magPt.data.energy = 60; magPt.data.color = (1.0, 0.25, 0.95); magPt.data.shadow_soft_size = 0.5
magPt.location = T2B(-269.5, 8.6, 58)
SC.collection.objects.link(magPt)
magPt.hide_render = True
streakM = bpy.data.materials.new("Streak")
streakM.use_nodes = True
sbs = streakM.node_tree.nodes["Principled BSDF"]
sbs.inputs["Base Color"].default_value = (0.85, 0.20, 0.80, 1.0)
sbs.inputs["Emission Color"].default_value = (0.699, 0.079, 0.643, 1.0)
sbs.inputs["Emission Strength"].default_value = 0.35
sbs.inputs["Roughness"].default_value = 1.0
stex = streakM.node_tree.nodes.new("ShaderNodeTexImage"); stex.image = fog_img
smul = streakM.node_tree.nodes.new("ShaderNodeMath"); smul.operation = 'MULTIPLY'
smul.inputs[1].default_value = 0.8
streakM.node_tree.links.new(stex.outputs["Alpha"], smul.inputs[0])
streakM.node_tree.links.new(smul.outputs[0], sbs.inputs["Alpha"])
bpy.ops.mesh.primitive_plane_add(location=T2B(-260, 4.94, 31))
so = bpy.context.object; so.name = "StreakPlane"; so.dimensions = (7.5, 26, 0)
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
# LƯU Ý: plane Blender (XY) đã nằm NGANG trong không gian three (blender Y = three -Z) — không xoay thêm
so.data.materials.append(streakM)
so.hide_render = True
# XH-4C+: dải mép nước sẫm (wet edge) — vật liệu alpha blob như sương, tông sẫm
wetM = bpy.data.materials.new("WetEdge")
wetM.use_nodes = True
wbs2 = wetM.node_tree.nodes["Principled BSDF"]
wbs2.inputs["Base Color"].default_value = (0.045, 0.065, 0.07, 1.0)
wbs2.inputs["Roughness"].default_value = 1.0
wtex = wetM.node_tree.nodes.new("ShaderNodeTexImage"); wtex.image = fog_img
wmul = wetM.node_tree.nodes.new("ShaderNodeMath"); wmul.operation = 'MULTIPLY'
wmul.inputs[1].default_value = 1.15
wetM.node_tree.links.new(wtex.outputs["Alpha"], wmul.inputs[0])
wetM.node_tree.links.new(wmul.outputs[0], wbs2.inputs["Alpha"])
def wet_strip(cx, cz, w, d):
    bpy.ops.mesh.primitive_plane_add(location=T2B(cx, 4.935, cz))
    o = bpy.context.object; o.dimensions = (w, d, 0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(wetM)
wet_strip(-392, 37.9, 336, 3.6)
wet_strip(-392, 194.1, 336, 3.6)
cylT("WetRing", 18.0, 0.02, (-250, 4.93, 58), wetM)
# vệt phản chiếu đèn bướm (chỉ shot tối)
lampStreakM = bpy.data.materials.new("LampStreak")
lampStreakM.use_nodes = True
lbs = lampStreakM.node_tree.nodes["Principled BSDF"]
lbs.inputs["Base Color"].default_value = (0.95, 0.55, 0.20, 1.0)
lbs.inputs["Emission Color"].default_value = (1.0, 0.55, 0.20, 1.0)
lbs.inputs["Emission Strength"].default_value = 0.55
ltex = lampStreakM.node_tree.nodes.new("ShaderNodeTexImage"); ltex.image = fog_img
lmul = lampStreakM.node_tree.nodes.new("ShaderNodeMath"); lmul.operation = 'MULTIPLY'
lmul.inputs[1].default_value = 0.85
lampStreakM.node_tree.links.new(ltex.outputs["Alpha"], lmul.inputs[0])
lampStreakM.node_tree.links.new(lmul.outputs[0], lbs.inputs["Alpha"])
lamp_streaks = []
for lx in (-344, -326, -308, -290, -272, -254, -236):
    bpy.ops.mesh.primitive_plane_add(location=T2B(lx, 4.945, 40.5))
    o = bpy.context.object; o.dimensions = (1.4, 9, 0)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(lampStreakM)
    o.hide_render = True
    lamp_streaks.append(o)

# ---------- ánh sáng / camera ----------
def setup(sun_energy, sun_rot, sun_color, bg, bg_strength, exposure):
    for o in list(SC.objects):
        if o.type == 'LIGHT' and not o.name.startswith('LampPt') and not o.name.startswith('MagPt'):
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

XH4C_ONLY = os.environ.get('XH4C_ONLY', '')
def shot(out, camT, tgtT, res=(1152, 768)):
    _sn = '1' if 'day' in out else ('2' if 'eye' in out else '3')
    if XH4C_ONLY and _sn not in XH4C_ONLY:
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

def set_estr(m, v):
    m.node_tree.nodes["Principled BSDF"].inputs["Emission Strength"].default_value = v

# ===== SHOT 1: bờ bắc BUỔI SÁNG — dọc đường dạo hướng tây (nước xám bạc, lát xám, đường nhựa, cây nghiêng) =====
set_estr(panelM, 0.0); set_estr(badgeM, 0.0); set_estr(bolTopM, 0.0); set_estr(waterM, 0.0)
fmul.inputs[1].default_value = 0.55   # sương sáng nhẹ (opacity ~0,30 đỉnh)
person(-300, 5.49, 31.7, math.pi / 2, (0.80, 0.33, 0.45), (0.12, 0.15, 0.26))
person(-300, 5.49, 30.85, math.pi / 2, (0.12, 0.20, 0.38), (0.07, 0.08, 0.10))
person(-310.5, 5.73, 35.3, 0.06, (0.72, 0.28, 0.32), (0.16, 0.15, 0.20), sit=True)
person(-309.5, 5.73, 35.3, -0.05, (0.18, 0.28, 0.45), (0.09, 0.09, 0.11), sit=True)
person(-284, 5.49, 28.4, -math.pi / 2, (0.30, 0.42, 0.50), (0.20, 0.18, 0.15))
setup(2.8, (math.radians(63), 0, math.radians(115)), (1.0, 0.84, 0.64), (0.42, 0.53, 0.66), 0.8, -0.18)
shot("xh4c-day-raw.png", (-240, 7.15, 32.5), (-332, 5.6, 34.0))

# ===== SHOT 2: TẦM MẮT CẮT NGANG — từ mặt nước nhìn vào bờ: nước -> cỏ dốc -> lát+tactile -> nhựa -> thông/hoa giấy =====
shot("xh4c-eye.png", (-276, 6.9, 47), (-264, 6.0, 16))

# ===== SHOT 3: CHẠNG VẠNG/TỐI — đảo Thủy Tạ MAGENTA + nước chàm + vệt phản chiếu + đèn bướm =====
set_estr(panelM, 4.0); set_estr(badgeM, 2.0); set_estr(bolTopM, 2.0)
wbs = waterM.node_tree.nodes["Principled BSDF"]
wbs.inputs["Base Color"].default_value = (0.207, 0.263, 0.455, 1.0)   # tint chàm lên canvas ngày (như tick game 17:30-19:00)
set_estr(waterM, 0.55)
set_estr(magM, 2.2)
magPt.hide_render = False
so.hide_render = False
for o in lamp_streaks: o.hide_render = False
fmul.inputs[1].default_value = 0.24 / 0.55
for lx in (-344, -326, -308, -290, -272, -254, -236):
    pt = bpy.data.objects.new("LampPt", bpy.data.lights.new("LampPt", 'POINT'))
    pt.data.energy = 40; pt.data.color = (1.0, 0.62, 0.25); pt.data.shadow_soft_size = 0.4
    pt.location = T2B(lx, 10.9, 27.5)
    SC.collection.objects.link(pt)
setup(0.7, (math.radians(84), 0, math.radians(-95)), (0.55, 0.52, 0.78), (0.075, 0.10, 0.20), 0.65, 0.1)
shot("xh4c-dusk-raw.png", (-233, 7.6, 30), (-261, 7.0, 58))
print("XH4C RENDERS DONE")
