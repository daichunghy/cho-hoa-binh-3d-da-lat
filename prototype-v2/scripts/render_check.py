# -*- coding: utf-8 -*-
"""Render kiểm chứng model v2 — lắp các GLB theo đúng bố cục thế giới thật.
Blender coords = three (x, -z, y)."""
import bpy, math, os
from mathutils import Vector

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
A = os.path.join(BASE, "assets")
R = os.path.join(BASE, "renders")
os.makedirs(R, exist_ok=True)

bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)

def mat(name, color, rough=0.95):
    m = bpy.data.materials.new(name); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (*color, 1)
    m.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = rough
    return m

def imp(name, loc=(0,0,0), rot=(0,0,0), scale=(1,1,1)):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(A, name + ".glb"))
    new = [o for o in bpy.data.objects if o not in before]
    root = bpy.data.objects.new("root_" + name, None)
    bpy.context.collection.objects.link(root)
    root.location = loc; root.rotation_euler = rot; root.scale = scale
    for o in new:
        if o.parent is None: o.parent = root
    return root

def box(dims, loc, m):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o = bpy.context.object; o.dimensions = dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    o.data.materials.append(m); return o

# nền: thung lũng + khối đồi + sườn
box((170, 130, 0.2), (0, -18, -0.1), mat("plaza", (0.52, 0.50, 0.46)))
box((170, 11, 0.22), (0, -2, 0.0), mat("road", (0.26, 0.26, 0.27)))
box((150, 52, 17), (0, 56, 8.5), mat("hill", (0.42, 0.38, 0.34)))
box((150, 52, 0.2), (0, 56, 17.05), mat("hilltop", (0.55, 0.52, 0.46)))
box((150, 10, 0.22), (0, 76, 17.06), mat("grass", (0.34, 0.42, 0.29)))

# công trình chính
imp("market", (0, -20, 0))
imp("theater", (-19, 56, 17))
imp("cafe", (13, 60, 17))
imp("stairs", (0, 16, 0))
imp("bridge", (17.5, 10.5, 14.65), rot=(math.atan2(4.4, 39), 0, 0))
imp("pier", (17.5, 2, 0), scale=(1, 1, 13.4))
imp("pier", (17.5, 16, 0), scale=(1, 1, 15.0))
imp("roundabout", (-24, 6, 0))
# gian hàng: dãy trước chợ (xoay 180°) + 1 gian trên đồi + 1 gian trong chợ
for x in (-36, -31, -26):
    imp("stall", (x, -8.4, 0), rot=(0, 0, math.pi))
imp("stall", (2, 46, 17))
imp("stall", (-24, -15, 0))
# nhân vật: tiểu thương trong gian + khách trước gian + người trên thang
# (ẩn 2 mũ không dùng như web makePerson, chỉ giữ 1 mũ/người)
def hide_hats(root, keep):
    for o in root.children_recursive:
        for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
            if o.name.startswith(hn) and hn != keep:
                o.hide_render = True
hide_hats(imp("character", (-31, -9.6, 0)), 'HatNonLa')
hide_hats(imp("character", (-31, -5.6, 0)), 'HatBeanie')
hide_hats(imp("character", (0, 16, 8.6)), 'HatCap')
hide_hats(imp("character", (5, -2, 0)), 'HatBeanie')
hide_hats(imp("character", (6.4, -2.8, 0)), 'HatNonLa')
# thông + đèn
for (x, y, z, s) in [(-52, 38, 17, 1.2), (52, 40, 17, 1.1), (-60, 62, 17, 1.3), (58, 66, 17, 1.2),
                     (-64, 14, 0, 0.9), (64, 12, 0, 0.95), (40, 48, 17, 1.0)]:
    imp("pine", (x, y, z), scale=(s, s, s))
for x in (-40, -20, 0, 20, 40):
    imp("lamp", (x, 3.2, 0))

# ánh sáng + world
world = bpy.data.worlds['World']; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.75, 0.82, 0.86, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.9
bpy.ops.object.light_add(type='SUN', location=(-45, -30, 70))
sun = bpy.context.object; sun.data.energy = 3.2; sun.rotation_euler = (0.7, 0.2, -0.6)
bpy.ops.object.light_add(type='AREA', location=(30, -40, 40))
ar = bpy.context.object; ar.data.energy = 600; ar.data.shape = 'DISK'; ar.data.size = 30
ar.rotation_euler = (0.9, 0, 0.4)

scene = bpy.context.scene
# VM không có GPU/libEGL (Eevee báo "Couldn't open libEGL.so.1") -> dùng Cycles CPU
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 12
scene.cycles.use_denoising = False
scene.render.resolution_x = 880; scene.render.resolution_y = 495
scene.render.image_settings.file_format = 'PNG'

def shot(name, loc, target):
    bpy.ops.object.camera_add(location=loc)
    cam = bpy.context.object
    d = Vector(target) - Vector(loc)
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.data.lens = 42
    scene.camera = cam
    scene.render.filepath = os.path.join(R, name + ".png")
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam, do_unlink=True)
    print("RENDERED", name)

shot("01-overview", (38, 40, 46), (-4, 4, 2))
shot("02-stall", (-31, 3.5, 3.2), (-31, -8.4, 1.2))
shot("03-character", (5.6, -6.4, 2.4), (5.6, -2.2, 0.95))
print("RENDERS DONE")
