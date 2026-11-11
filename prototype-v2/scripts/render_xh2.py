# -*- coding: utf-8 -*-
# render_xh2.py — Nghiệm thu XH-2: nạp lake.glb THẬT (bản quantized sẽ ship) +
# môi trường hồ tối thiểu (nước teal WATER-1, đĩa đảo + vòng lát XH-1, đường dạo).
# Ảnh: cận thuyền hoa văn / đảo ngày / đảo chạng vạng 19h / đảo từ tây-nam (cung thuyền).
# Harness gắn texture hoa văn cho vật liệu SwanPattern Y NHƯ web làm lúc chạy
# (canvas runtime trong index.html) để render cho ra đúng hình người chơi thấy.
# Cycles CPU, threads 2, OIDN denoise, ACES 1.3, exposure -0.18 (research/26).
# Dùng: blender5/blender -b --python render_xh2.py
import bpy, math, os, random
from mathutils import Vector

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "renders")

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=os.path.join(ROOT, "assets", "lake.glb"))
SC = bpy.context.scene

def T2B(x, y, z):  # three (x, y-up, z) -> blender (x, -z, y)
    return (x, -z, y)

def hide(name):
    o = SC.objects.get(name)
    if o: o.location = T2B(0, -80, 0)

def place(name, tx, ty, tz, rotY=0.0):
    o = SC.objects.get(name)
    o.location = T2B(tx, ty, tz)
    o.rotation_euler = (0, 0, rotY)
    return o

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

# ---------- texture hoa văn như web (chấm + hoa 5 cánh trên nền trắng) ----------
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

# ---------- môi trường ----------
waterM = mat("Water", (0.020, 0.148, 0.255), 0.15)      # #276a8a sRGB -> linear
grassM = mat("Grass", (0.115, 0.235, 0.065), 0.98)       # ~0x5f8547
paveM = mat("Pave", (0.72, 0.77, 0.77), 0.9)             # #dde2e2
kerbM = mat("Kerb", (0.20, 0.185, 0.165), 0.95)
box("WaterPlane", (336, 0.1, 160), (-392, 4.85, 116), waterM)
cylT("BoatPad", 7, 0.1, (0, -0.05, 0), waterM)  # đĩa nước dưới thuyền cho shot cận (ngoài khung đảo)
box("ShoreGrass", (420, 0.1, 90), (-300, 5.42, -8), grassM)
box("Promenade", (144, 0.12, 8), (-288, 5.46, 32), paveM)
cylT("IslandGrass", 15, 0.12, (-250, 5.42, 58), grassM)
cylT("IslandRing", 13.8, 0.05, (-250, 5.485, 58), paveM)
cylT("IslandLawn", 9, 0.06, (-250, 5.49, 58), grassM)
cylT("IslandKerb", 16.1, 1.1, (-250, 4.95, 58), kerbM)

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
SC.collection.objects.link(cam); SC.camera = cam

def shot(out, camT, tgtT, res=(960, 720)):
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

# 1) cận thuyền hoa văn — giấu mọi root khác (từng bị CherryTree đè ở lượt 1)
for nm in ("SwanBoat", "ThuyTa", "IslandBridge", "CherryTree", "PineUmbrella", "Willow"):
    hide(nm)
bp = SC.objects.get("SwanBoatPattern")
bp.location = T2B(0, 0, 0); bp.rotation_euler = (0, 0, 0.5)
setup(3.2, (math.radians(48), 0, math.radians(35)), (1.0, 0.95, 0.88), (0.55, 0.68, 0.82), 0.85, -0.18)
shot("xh2-boat.png", (3.1, 1.7, -3.4), (0, 0.75, 0.3), (880, 660))
hide("SwanBoatPattern")

# ---------- đặt model đúng số index.html XH-2 ----------
place("ThuyTa", -262, 5.47, 58, -math.pi / 2)
place("IslandBridge", -250, 5.38, 39.5, 0)
place("PineUmbrella", -244.5, 5.47, 62.5, 0.7)
wl0 = place("Willow", -262.5, 5.47, 50.5, 50.5)
wl2 = wl0.copy(); SC.collection.objects.link(wl2)
for ch in list(wl0.children):
    c2 = ch.copy(); c2.parent = wl2; SC.collection.objects.link(c2)
wl2.location = T2B(-262.5, 5.47, 65.5); wl2.rotation_euler = (0, 0, 65.5)

boat_src = {nm: SC.objects.get(nm) for nm in ("SwanBoat", "SwanBoatPattern")}
def place_boat(pattern, x, z, rotY):
    src = boat_src["SwanBoatPattern" if pattern else "SwanBoat"]
    g = src.copy(); SC.collection.objects.link(g)
    for ch in list(src.children):
        c = ch.copy(); c.parent = g; SC.collection.objects.link(c)
    g.location = T2B(x, 4.9, z); g.rotation_euler = (0, 0, rotY)
    return g

for (phi, pat, r, jr) in [(-66, 0, 19.2, 0.05), (-44, 1, 18.7, -0.04), (-22, 0, 19.0, 0.03),
                          (0, 1, 18.6, -0.05), (22, 0, 19.1, 0.04), (44, 1, 18.8, -0.03), (66, 0, 19.3, 0.05)]:
    a = math.radians(phi); dx, dz = math.sin(a), math.cos(a)
    place_boat(pat == 1, -250 + dx * r, 58 + dz * r, math.atan2(-dx, -dz) + jr)
place_boat(True, -272, 39.5, math.pi - 0.05)
place_boat(False, -241, 39.5, math.pi + 0.04)
place_boat(False, -259, 39.3, math.pi)

# 2) đảo ngày — từ bờ bắc
setup(3.4, (math.radians(52), 0, math.radians(30)), (1.0, 0.97, 0.92), (0.55, 0.68, 0.82), 0.9, -0.18)
shot("xh2-island-day.png", (-231, 11.5, 14), (-256, 6.0, 60))
# 3) đảo chạng vạng 19h
setup(2.0, (math.radians(78), 0, math.radians(-115)), (1.0, 0.62, 0.34), (0.10, 0.15, 0.24), 0.55, -0.18)
shot("xh2-island-dusk.png", (-231, 11.5, 14), (-256, 6.0, 60))
# 4) đảo từ tây-nam trên cao — cung thuyền nam + mặt hồ của nhà
setup(3.4, (math.radians(52), 0, math.radians(30)), (1.0, 0.97, 0.92), (0.55, 0.68, 0.82), 0.9, -0.18)
shot("xh2-island-sw.png", (-296, 30, 128), (-250, 5.0, 58))
print("XH2 RENDERS DONE")
