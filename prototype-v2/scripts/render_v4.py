# -*- coding: utf-8 -*-
"""Render kiểm chứng V4 (Cycles) — 5 góc:
01 mặt tiền chợ (ngày) · 01b mặt sau + tháp thang máy kính · 02 bùng binh + xe
03 bậc thang đông người · 04 dãy sạp đêm · 05 khách sạn sau đồi
Chạy: blender -b --factory-startup -noaudio --python scripts/render_v4.py
Quy ước: GLB import vào Blender giữ nguyên hướng gốc (mặt tiền -Y).
"""
import bpy, math, os, sys
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)

def clear():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def setup(samples=48, exposure=0.0):
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = samples
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 768
    sc.render.resolution_y = 576
    sc.view_settings.view_transform = 'Filmic'
    sc.view_settings.exposure = exposure
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
    return o

def point(loc, color=(1.0, 0.75, 0.45), energy=60.0, dist=14.0):
    d = bpy.data.lights.new("Pt", 'POINT'); d.color = color; d.energy = energy
    d.shadow_soft_size = 0.3
    o = bpy.data.objects.new("Pt", d); bpy.context.collection.objects.link(o)
    o.location = loc
    return o

def camera(loc, target, lens=42):
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = loc
    d_vec = Vector(target) - Vector(loc)
    o.rotation_euler = d_vec.to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.camera = o
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

def wrap_person(objs, loc, rotz=0.0, sit=False):
    """Gom các object của 1 character vào 1 empty để đặt/pose."""
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

def box(name, size, loc, rgb):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    m = bpy.data.materials.new(name + "M"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (*rgb, 1)
    o.data.materials.append(m)
    return o

def render(name):
    bpy.context.scene.render.filepath = os.path.join(OUT, name + ".png")
    bpy.ops.render.render(write_still=True)
    print("RENDERED", name)

# ============================================================ 01 mặt tiền
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
import_glb("market.glb")
box("Ground", (90, 70, 0.2), (0, -18, -0.12), (0.42, 0.44, 0.46))
camera((23, -37, 13.5), (0, 0, 8.5))
render("v4-01-mat-tien")

# ============================================================ 01b mặt sau
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun(euler=(math.radians(55), 0, math.radians(-120)))
import_glb("market.glb")
box("Ground", (90, 70, 0.2), (0, 16, -0.12), (0.42, 0.44, 0.46))
camera((-24, 33, 14), (0, 0, 9.5))
render("v4-01b-mat-sau")

# ============================================================ 02 bùng binh + xe
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
import_glb("roundabout.glb")
box("Road", (46, 46, 0.15), (0, 0, -0.09), (0.16, 0.16, 0.18))
veh = import_glb("vehicle.glb")
moto_tpl = find(veh, "Moto"); car_tpl = find(veh, "Car")
# nhân bản xe chạy vòng: moto r=10.6 (5 chiếc), ô tô r=11.9 (1 chiếc)
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
        g.rotation_euler = (0, 0, -a)  # hướng tiếp tuyến (soi ảnh sẽ chỉnh nếu ngược)
dup_ring(moto_tpl, 5, 10.6, 0.4)
dup_ring(car_tpl, 1, 11.9, 2.2)
# người đứng quanh vòng người r~9.5
for i, a in enumerate([0.3, 1.5, 2.9, 4.4, 5.6]):
    objs = import_glb("character.glb")
    wrap_person(objs, (math.cos(a) * 9.5, math.sin(a) * 9.5, 0), rotz=-a + math.pi)
camera((17, -24, 15), (0, 0, 2.5), lens=38)
render("v4-02-bung-binh-xe")

# ============================================================ 03 bậc thang đông
clear(); setup(); world_bg((0.45, 0.55, 0.75), 0.8); sun(euler=(math.radians(60), 0, math.radians(-30)), energy=2.4)
import_glb("stairs.glb")
# bậc i: mặt bậc tại y=2+(i+0.5)*1.0667, cao (i+1)*0.6296 — đặt người ngồi/đứng
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
camera((8.5, -7, 3.2), (0, 15, 8.5), lens=46)
render("v4-03-bac-thang-dong")

# ============================================================ 04 sạp đêm
clear(); setup(exposure=0.2); world_bg((0.012, 0.02, 0.045), 0.5)
for k, x in enumerate([-4.3, 0, 4.3]):
    objs = import_glb("stall.glb")
    for o in objs:
        if o.parent is None: o.location.x += x
    # bóng đèn mô phỏng web: cầu sáng + point light trước quầy
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.06, location=(x, -1.05, 2.42), segments=8, ring_count=6)
    bulb = bpy.context.object
    bm = bpy.data.materials.new("BulbM"); bm.use_nodes = True
    bsdf = bm.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Emission Color"].default_value = (1, 0.9, 0.7, 1)
    bsdf.inputs["Emission Strength"].default_value = 6.0
    bulb.data.materials.append(bm)
    point((x, -1.6, 2.6), energy=42, dist=11)
objs = import_glb("character.glb")
wrap_person(objs, (1.6, -3.4, 0), rotz=0.3)
objs = import_glb("character.glb")
wrap_person(objs, (-2.2, -3.1, 0), rotz=-0.2)
box("Ground", (30, 16, 0.2), (0, -2, -0.12), (0.10, 0.10, 0.12))
camera((5.2, -8.6, 2.7), (0, 0.4, 1.25), lens=44)
render("v4-04-sap-dem")

# ============================================================ 05 khách sạn sau đồi
clear(); setup(); world_bg((0.55, 0.68, 0.85), 0.9); sun()
mk = import_glb("market.glb")
for o in mk:
    if o.parent is None: o.location = (o.location.x, o.location.y - 20, o.location.z)  # three (0,0,20)
ht = import_glb("hotels.glb")
for nm, bx in (("HotelA", -38), ("HotelC", 0), ("HotelB", 38)):
    g = find(ht, nm)
    if g: g.location = (bx, 77, 17)  # three (x,17,-77) → blender (x, 77, 17)
st = import_glb("stairs.glb")
for o in st:
    if o.parent is None: o.location = (o.location.x, o.location.y + 32, o.location.z)
box("Hill", (150, 52, 17), (0, 56, 8.5), (0.42, 0.55, 0.36))
box("Valley", (170, 60, 0.2), (0, -25, -0.12), (0.45, 0.46, 0.48))
camera((30, -34, 7), (-4, 55, 13), lens=40)
render("v4-05-khach-san")

print("ALL RENDERS DONE")
