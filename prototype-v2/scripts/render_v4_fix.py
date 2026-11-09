# -*- coding: utf-8 -*-
"""Render lại 5 góc V4 sau soi ảnh vòng 1 (camera/góc chưa đúng):
01 mặt tiền (+Y) · 01b mặt đồi (-Y) · 02 bùng binh rộng (thấy ô tô) ·
03 bậc thang (camera trong trục thang) · 05 khách sạn (bỏ HotelD thừa ở gốc).
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")

def clear():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def setup(samples=32):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = samples
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 720
    sc.render.resolution_y = 540
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

# 01 MẶT TIỀN (phía +Y blender)
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
import_glb("market.glb")
box("Ground", (100, 80, 0.2), (0, 22, -0.12), (0.42, 0.44, 0.46))
camera((27, 41, 15), (0, 2, 9))
render("v4-01-mat-tien")

# 01b MẶT ĐỒI / MẶT SAU (phía -Y blender)
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun(euler=(math.radians(55), 0, math.radians(-120)))
import_glb("market.glb")
box("Ground", (100, 80, 0.2), (0, -22, -0.12), (0.42, 0.44, 0.46))
camera((-27, -41, 15), (0, -2, 9))
render("v4-01b-mat-sau")

# 02 BÙNG BINH — góc cao rộng, thấy cả ô tô ở r=11.9
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
import_glb("roundabout.glb")
box("Road", (52, 52, 0.15), (0, 0, -0.09), (0.16, 0.16, 0.18))
veh = import_glb("vehicle.glb")
moto_tpl = find(veh, "Moto"); car_tpl = find(veh, "Car")
def dup_ring(tpl, n, r, phase=0.0):
    for i in range(n):
        a = phase + i / max(n, 1) * math.pi * 2
        bpy.ops.object.select_all(action='DESELECT')
        tpl.select_set(True)
        for ch in tpl.children_recursive: ch.select_set(True)
        bpy.context.view_layer.objects.active = tpl
        bpy.ops.object.duplicate()
        g = bpy.context.object
        g.location = (math.cos(a) * r, math.sin(a) * r, 0)
        g.rotation_euler = (0, 0, -a)
dup_ring(moto_tpl, 5, 10.6, 0.4)
dup_ring(car_tpl, 1, 11.9, 2.9)
for i, a in enumerate([0.3, 1.5, 2.9, 4.4, 5.6]):
    objs = import_glb("character.glb")
    wrap_person(objs, (math.cos(a) * 9.5, math.sin(a) * 9.5, 0), rotz=-a + math.pi)
camera((21, -28, 20), (0, 0, 2), lens=36)
render("v4-02-bung-binh-xe")

# 03 BẬC THANG — camera trong trục thang nhìn lên
clear(); setup(); world_bg((0.45, 0.55, 0.75), 0.8); sun(euler=(math.radians(60), 0, math.radians(-30)), energy=2.4)
import_glb("stairs.glb")
sitters = [(3, 4.2), (6, -4.4), (10, 4.5), (14, -4.2), (19, 4.4), (24, -4.5)]
for i, x in sitters:
    y = 2 + (i + 0.5) * 1.0667; z = (i + 1) * 0.6296
    box("Stool", (0.34, 0.34, 0.3), (x, y, z + 0.15), (0.15, 0.33, 0.65))
    objs = import_glb("character.glb")
    wrap_person(objs, (x, y, z + 0.30), rotz=math.pi, sit=True)
standers = [(4, -2.2), (12, 2.4), (21, -2.6)]
for i, x in standers:
    y = 2 + (i + 0.5) * 1.0667; z = (i + 1) * 0.6296
    objs = import_glb("character.glb")
    wrap_person(objs, (x, y, z), rotz=math.pi)
camera((3.0, -13, 2.2), (-0.5, 17, 9.5), lens=40)
render("v4-03-bac-thang-dong")

# 05 KHÁCH SẠN SAU ĐỒI — bỏ HotelD thừa, bố trí như web
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

print("ALL FIX RENDERS DONE")
