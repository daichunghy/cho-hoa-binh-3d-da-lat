# -*- coding: utf-8 -*-
# render_xh3r.py — Nghiệm thu XH-3R (TỈ LỆ HỒ, trọng tâm CHIỀU CAO):
# camera TẦM MẮT NGƯỜI trên đường dạo bờ bắc (số XH-3R: lát 12u z 24..36, kè flush 5.50,
# hàng thông tán ô scale ~1.7 cao ~11.7u, cầu đảo deck 3.2) + 2 nhân vật character.glb
# làm THƯỚC SỐNG (1,82u). Môi trường dựng đúng số index.html XH-3R; model từ lake.glb
# bản quantized sẽ ship. Cycles CPU threads 2, OIDN, ACES (research/26).
# Dùng: blender5/blender -b --python render_xh3r.py
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

def mat(name, rgb, rough=0.9):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bs = m.node_tree.nodes["Principled BSDF"]
    bs.inputs["Base Color"].default_value = (*rgb, 1.0)
    bs.inputs["Roughness"].default_value = rough
    return m

def box(name, size, tloc, m):
    bpy.ops.mesh.primitive_cube_add(location=T2B(*tloc))
    o = bpy.context.object; o.name = name; o.dimensions = (size[0], size[2], size[1])
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if m: o.data.materials.append(m)
    return o

def cylT(name, r, h, tloc, m, verts=40):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=h, location=T2B(*tloc))
    o = bpy.context.object; o.name = name
    if m: o.data.materials.append(m)
    return o

# ---------- texture hoa văn thuyền như web ----------
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

# ---------- người (character.glb phẳng) — thước sống 1,82u ----------
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

def person(tx, ty, tz, rotY, shirt, pants):
    c, s = math.cos(rotY), math.sin(rotY)
    for nm, (loc, src) in CHAR_BASE.items():
        o = src.copy(); SC.collection.objects.link(o)
        lx, ly, lz = loc
        o.rotation_euler = (0, 0, rotY)
        rx = lx * c - ly * s; ry = lx * s + ly * c
        o.location = (tx + rx, -tz + ry, ty + lz)
        o.hide_render = nm in ("HatNonLa", "HatCap")
        if nm in ("Torso", "ArmL", "ArmR", "tmpCollar"): tint(o, shirt)
        if nm in ("LegL", "LegR"): tint(o, pants)

for nm, (loc, src) in CHAR_BASE.items():
    src.hide_render = True

# ---------- môi trường đúng số XH-3R ----------
waterM = mat("Water", (0.020, 0.148, 0.255), 0.15)
grassM = mat("Grass", (0.115, 0.235, 0.065), 0.98)
paveM = mat("Pave", (0.72, 0.77, 0.77), 0.9)
kerbM = mat("Kerb", (0.20, 0.185, 0.165), 0.95)
curbM = mat("Curb", (0.78, 0.75, 0.66), 0.9)
washM = mat("Wash", (0.88, 0.85, 0.78), 0.9)

box("WaterPlane", (336, 0.1, 160), (-392, 4.85, 116), waterM)
box("Plateau", (144, 0.12, 61), (-288, 5.42, 5.5), grassM)                    # thềm cỏ, đỉnh 5.48
box("Promenade", (144, 0.12, 12), (-288, 5.43, 30), paveM)                    # XH-3R: lát z 24..36, đỉnh 5.49
box("KeN1", (100.4, 1.14, 0.7), (-301.8, 4.93, 36), kerbM)                    # XH-3R: đỉnh kè 5.50 flush
box("KeN2", (24.4, 1.14, 0.7), (-236.2, 4.93, 36), kerbM)
box("Curb1", (100.4, 0.09, 0.9), (-301.8, 5.6, 36), curbM)
box("Curb2", (24.4, 0.09, 0.9), (-236.2, 5.6, 36), curbM)
box("BridgePad", (3.8, 0.08, 7), (-250, 5.30, 39.5), paveM)                   # XH-3R: nền cầu rộng 3.8
cylT("IslandGrass", 15, 0.12, (-250, 5.42, 58), grassM)
cylT("IslandRim", 16.1, 1.2, (-250, 4.84, 58), kerbM)
cylT("IslandRing", 14.3, 0.05, (-250, 5.485, 58), paveM)                      # XH-3R: vòng 9.8..14.3
cylT("IslandLawn", 9.8, 0.06, (-250, 5.49, 58), grassM)
box("FarShore", (336, 0.1, 34), (-392, 8.9, 213), grassM)                     # thềm nam xa (silhouette)

# ---------- đặt model lake.glb theo index XH-2/XH-3R ----------
place("ThuyTa", -262, 5.47, 58, -math.pi / 2)
place("IslandBridge", -250, 5.38, 39.5, 0)
pine_src = SC.objects.get("PineUmbrella")
place("PineUmbrella", -244.5, 5.47, 62.5, 0.7)                                # cây đảo scale 1.0 (khớp ảnh 37)
wl0 = place("Willow", -262.5, 5.47, 50.5, 50.5)
dup_root(wl0, -262.5, 5.47, 65.5, 65.5)
hide("CherryTree")

# hàng thông tán ô bờ bắc — ĐÚNG tọa độ/scale index XH-3R (z 25.2, y = groundH-0.05 = 5.45)
for (px, ps) in [(-344, 1.74), (-330, 1.66), (-316, 1.78), (-302, 1.70), (-288, 1.76),
                 (-274, 1.64), (-260, 1.79), (-246, 1.68), (-220, 1.72)]:
    dup_root(pine_src, px, 5.45, 25.2, (px * 7 + 25.2 * 13) % 3.14, ps)
    cylT("Wash", 0.22 * ps, 0.8, (px, 5.9, 25.2), washM, 10)                   # gốc quét vôi trắng 0.8u
# silhouette bờ nam xa
for (px, pz, py, ps) in [(-512, 206, 6.9, 1.85), (-450, 207, 7.0, 1.68), (-388, 209, 7.1, 1.70),
                         (-326, 206, 6.9, 1.79), (-280, 215, 7.9, 1.83), (-470, 227, 9.0, 1.75), (-300, 227, 9.0, 1.70)]:
    dup_root(pine_src, px, py, pz, (px * 7 + pz * 13) % 3.14, ps)

boat_src = {nm: SC.objects.get(nm) for nm in ("SwanBoat", "SwanBoatPattern")}
def place_boat(pattern, x, z, rotY):
    src = boat_src["SwanBoatPattern" if pattern else "SwanBoat"]
    dup_root(src, x, 4.9, z, rotY)
place_boat(True, -272, 39.5, math.pi - 0.05)
place_boat(False, -241, 39.5, math.pi + 0.04)
place_boat(False, -259, 39.3, math.pi)
for (phi, pat, r) in [(-44, 1, 18.7), (0, 0, 18.6), (44, 1, 18.8)]:
    a = math.radians(phi); dx, dz = math.sin(a), math.cos(a)
    place_boat(pat == 1, -250 + dx * r, 58 + dz * r, math.atan2(-dx, -dz))

# người làm thước: A giữa đường dạo, B sát mép kè nhìn ra hồ
person(-256, 5.49, 30.5, -0.6, (0.75, 0.25, 0.15), (0.15, 0.18, 0.35))
person(-266, 5.49, 34.4, math.pi + 0.4, (0.15, 0.35, 0.65), (0.25, 0.22, 0.2))

# ---------- ánh sáng / camera ----------
def setup(sun_energy, sun_rot, sun_color, bg, bg_strength, exposure):
    for o in list(SC.objects):
        if o.type == 'LIGHT':
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

def shot(out, camT, tgtT, res=(1152, 768)):
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

# 1) tầm mắt NGÀY — đứng trên đường dạo nhìn dọc bờ về cầu/đảo
setup(3.4, (math.radians(52), 0, math.radians(30)), (1.0, 0.97, 0.92), (0.55, 0.68, 0.82), 0.9, -0.18)
shot("xh3r-eye-day.png", (-238, 7.15, 33.0), (-272, 6.0, 28.0))
# 2) tầm mắt CHẠNG VẠNG — cùng vị trí
setup(2.0, (math.radians(78), 0, math.radians(-115)), (1.0, 0.62, 0.34), (0.10, 0.15, 0.24), 0.55, -0.18)
shot("xh3r-eye-dusk.png", (-238, 7.15, 33.0), (-272, 6.0, 28.0))
# 3) khung ghép so ảnh thật 03 — từ tây nhìn đông-dông nam: lát + thông trái, nước + đảo phải
setup(3.4, (math.radians(52), 0, math.radians(30)), (1.0, 0.97, 0.92), (0.55, 0.68, 0.82), 0.9, -0.18)
shot("xh3r-cmp-src.png", (-326, 7.4, 29.0), (-256, 5.6, 41.0))
print("XH3R RENDERS DONE")
