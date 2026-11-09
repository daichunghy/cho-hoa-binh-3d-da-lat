# -*- coding: utf-8 -*-
"""Render v4-05 khách sạn sau đồi — vòng 4: gom group bằng empty cha chắc chắn
+ EEVEE (chỉ kiểm chứng bố cục phông nền, cho nhanh) + log vị trí để debug.
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 16
sc.cycles.use_denoising = True
sc.render.resolution_x = 640
sc.render.resolution_y = 480
sc.view_settings.view_transform = 'Filmic'

w = bpy.data.worlds.new("W"); sc.world = w; w.use_nodes = True
bg = w.node_tree.nodes["Background"]
bg.inputs[0].default_value = (0.55, 0.68, 0.85, 1.0); bg.inputs[1].default_value = 0.9

d = bpy.data.lights.new("Sun", 'SUN'); d.energy = 3.0
so = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(so)
so.rotation_euler = (math.radians(50), 0, math.radians(35))

def import_glb(name):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name))
    return [o for o in bpy.data.objects if o not in before]

def group_at(objs, loc, tag):
    """Gom mọi root object vào 1 empty rồi đặt empty tại loc (giữ nguyên bố cục nội bộ)."""
    e = bpy.data.objects.new(tag, None)
    bpy.context.collection.objects.link(e)
    roots = [o for o in objs if o.parent is None]
    for o in roots:
        o.parent = e
    e.location = loc
    print(tag, "roots:", len(roots), "-> loc", loc)
    return e

def box(name, size, loc, rgb):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object; o.name = name; o.scale = size
    bpy.ops.object.transform_apply(scale=True)
    m = bpy.data.materials.new(name + "M"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (*rgb, 1)
    o.data.materials.append(m)
    return o

# market tại three (0,0,20) → blender (0,-20,0)
group_at(import_glb("market.glb"), (0, -20, 0), "MarketG")
# cầu thang: gốc GLB đã ở đúng dải y -13..14 quanh three z -32..-2 → blender y +2..+32:
# dịch +32 theo Y như bố cục web (chân thang y≈2+... lấy theo vòng trước +32 cho khớp đồi)
group_at(import_glb("stairs.glb"), (0, 32, 0), "StairsG")
ht = import_glb("hotels.glb")
def find(base):
    for o in ht:
        if o.name.split('.')[0] == base: return o
    return None
for nm, bx in (("HotelA", -38), ("HotelC", 0), ("HotelB", 38)):
    g = find(nm)
    if g: g.location = (bx, 77, 17); print(nm, "->", g.location)
gd = find("HotelD")
if gd:
    for ch in list(gd.children_recursive): bpy.data.objects.remove(ch, do_unlink=True)
    bpy.data.objects.remove(gd, do_unlink=True)

box("Hill", (150, 52, 17), (0, 56, 8.5), (0.42, 0.55, 0.36))
box("Valley", (170, 60, 0.2), (0, -25, -0.12), (0.45, 0.46, 0.48))

cd = bpy.data.cameras.new("Cam"); cd.lens = 35
co = bpy.data.objects.new("Cam", cd); bpy.context.collection.objects.link(co)
co.location = (58, -82, 20)
co.rotation_euler = (Vector((-2, 26, 10)) - Vector((58, -82, 20))).to_track_quat('-Z', 'Y').to_euler()
sc.camera = co
sc.render.filepath = os.path.join(OUT, "v4-05-khach-san.png")
bpy.ops.render.render(write_still=True)
print("RENDERED v4-05-khach-san")
