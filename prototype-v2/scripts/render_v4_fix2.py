# -*- coding: utf-8 -*-
"""Render vòng 3: 01 mặt tiền (sau sửa chữ) · 03 bậc thang (người đặt theo
bbox bậc trích trực tiếp từ GLB) · 05 khách sạn sau đồi.
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")

def clear():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def setup(samples=24):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = samples
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 640
    sc.render.resolution_y = 480
    sc.view_settings.view_transform = 'Filmic'
    return sc

def world_bg(rgb, strength=1.0):
    w = bpy.data.worlds.new("W"); bpy.context.scene.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (*rgb, 1.0)
    bg.inputs[1].default_value = strength

def sun(euler=(math.radians(50), 0, math.radians(35)), energy=3.0):
    d = bpy.data.lights.new("Sun", 'SUN'); d.energy = energy
    o = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(o)
    o.rotation_euler = euler

def camera(loc, target, lens=42):
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.camera = o

def import_glb(name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name))
    return [o for o in bpy.data.objects if o not in before]

def find(objs, base):
    for o in objs:
        if o.name.split('.')[0] == base:
            return o
    return None

def box(name, size, loc, rgb):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    m = bpy.data.materials.new(name + "M"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (*rgb, 1)
    o.data.materials.append(m)
    return o

def wrap_person(objs, loc, rotz=0.0, sit=False):
    e = bpy.data.objects.new("Person", None)
    bpy.context.collection.objects.link(e)
    e.location = loc; e.rotation_euler = (0, 0, rotz)
    for o in objs:
        if o.type in ('MESH', 'EMPTY') and o.parent is None:
            o.parent = e
    if sit:
        for nm in ('LegL', 'LegR'):
            leg = find(objs, nm)
            if leg: leg.rotation_euler.x = -1.45
        arm = find(objs, 'ArmR')
        if arm: arm.rotation_euler.x = -1.0
    return e

def render(name):
    bpy.context.scene.render.filepath = os.path.join(OUT, name + ".png")
    bpy.ops.render.render(write_still=True)
    print("RENDERED", name)

# 01 MẶT TIỀN — xác nhận chữ đọc đúng sau sửa rotation
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
import_glb("market.glb")
box("Ground", (100, 80, 0.2), (0, 22, -0.12), (0.42, 0.44, 0.46))
camera((27, 41, 15), (0, 2, 9))
render("v4-01-mat-tien")

# 03 BẬC THANG — vị trí người trích từ bbox thật của từng khối Step
clear(); setup(); world_bg((0.45, 0.55, 0.75), 0.8); sun(euler=(math.radians(60), 0, math.radians(-30)), energy=2.4)
sobjs = import_glb("stairs.glb")
steps = []
for o in sobjs:
    if o.type == 'MESH' and o.name.split('.')[0] in ('Step', 'Landing1', 'Landing2'):
        corners = [o.matrix_world @ Vector(c) for c in o.bound_box]
        ys = [c.y for c in corners]; zs = [c.z for c in corners]
        steps.append((max(ys), max(zs), (min(ys) + max(ys)) / 2))
steps.sort()  # theo mép trước (y lớn dần = lên cao dần theo +Y)
print("STEP TOPS:", [(round(y, 1), round(z, 1)) for y, z, _ in steps])
picks = [steps[i] for i in (1, 4, 7, 10, 13, 16) if i < len(steps)]
for k, (yfront, ztop, ymid) in enumerate(picks):
    x = 4.2 if k % 2 == 0 else -4.3
    ysit = yfront - 0.45
    box("Stool", (0.34, 0.34, 0.3), (x, ysit, ztop + 0.15), (0.15, 0.33, 0.65))
    objs = import_glb("character.glb")
    wrap_person(objs, (x, ysit, ztop + 0.30), rotz=math.pi, sit=True)
for k, (yfront, ztop, ymid) in enumerate(picks[::2]):
    objs = import_glb("character.glb")
    wrap_person(objs, (-2.2 if k % 2 == 0 else 2.4, yfront - 0.5, ztop), rotz=math.pi)
camera((11, -27, 5.5), (0, 4, 8.5), lens=40)
render("v4-03-bac-thang-dong")

# 05 KHÁCH SẠN SAU ĐỒI
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
mk = import_glb("market.glb")
for o in mk:
    if o.parent is None: o.location = (o.location.x, o.location.y - 20, o.location.z)
ht = import_glb("hotels.glb")
for nm, bx in (("HotelA", -38), ("HotelC", 0), ("HotelB", 38)):
    g = find(ht, nm)
    if g: g.location = (bx, 77, 17)
gd = find(ht, "HotelD")
if gd:
    for ch in list(gd.children_recursive): bpy.data.objects.remove(ch, do_unlink=True)
    bpy.data.objects.remove(gd, do_unlink=True)
st = import_glb("stairs.glb")
for o in st:
    if o.parent is None: o.location = (o.location.x, o.location.y + 32, o.location.z)
box("Hill", (150, 52, 17), (0, 56, 8.5), (0.42, 0.55, 0.36))
box("Valley", (170, 60, 0.2), (0, -25, -0.12), (0.45, 0.46, 0.48))
camera((34, -38, 9), (-4, 52, 12), lens=40)
render("v4-05-khach-san")

print("ALL FIX2 DONE")
