# -*- coding: utf-8 -*-
"""Render cận mặt nhân vật (trước/sau sửa) — mô phỏng ĐÚNG web makePerson:
chỉ 1 mũ được bật, khăn ẩn. Thêm 1 kiểu 'allhats' tái hiện lỗi render v4
(bật cả 3 mũ chồng nhau).
Chạy: blender -b --factory-startup -noaudio --python scripts/render_face.py -- before|after
"""
import bpy, math, os, sys
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else ["x"]
TAG = argv[0] if argv else "x"

def clear():
    bpy.ops.wm.read_factory_settings(use_empty=True)

def setup():
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = 24
    sc.cycles.use_denoising = True
    sc.render.resolution_x = 512
    sc.render.resolution_y = 512
    sc.view_settings.view_transform = 'Filmic'
    w = bpy.data.worlds.new("W"); sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.55, 0.68, 0.85, 1.0)
    bg.inputs[1].default_value = 0.9
    d = bpy.data.lights.new("Sun", 'SUN'); d.energy = 3.0
    o = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(o)
    o.rotation_euler = (math.radians(50), 0, math.radians(35))
    # mặt đất xám để có bóng
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.06))
    g = bpy.context.object; g.scale = (8, 8, 0.1)
    bpy.ops.object.transform_apply(scale=True)
    m = bpy.data.materials.new("GM"); m.use_nodes = True
    m.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.45, 0.45, 0.47, 1)
    g.data.materials.append(m)
    return sc

def camera(loc, target, lens=50):
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    bpy.context.scene.camera = o

def find(objs, base):
    for o in objs:
        if o.name.split('.')[0] == base:
            return o
    return None

def shot(hatmode, cam_loc, cam_tgt, suffix):
    clear(); setup()
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, "character.glb"))
    objs = [o for o in bpy.data.objects if o not in before]
    keep = {'nonla': 'HatNonLa', 'beanie': 'HatBeanie', 'cap': 'HatCap'}.get(hatmode)
    for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
        h = find(objs, hn)
        if h: h.hide_render = (hatmode != 'allhats' and hn != keep)
    sc = find(objs, 'Scarf')
    if sc: sc.hide_render = True
    camera(cam_loc, cam_tgt)
    bpy.context.scene.render.filepath = os.path.join(OUT, "v41-face-%s-%s.png" % (TAG, suffix))
    bpy.ops.render.render(write_still=True)
    print("RENDERED", suffix)

# beanie (mũ phổ biến nhất trong đám đông) — nhìn thẳng mặt
shot('beanie', (0, -3.0, 1.55), (0, 0, 1.42), "beanie-front")
# nón lá — nhìn từ trên-trước như render v4-03
shot('nonla', (1.7, -2.5, 2.8), (0, 0, 1.30), "nonla-above")
# cả 3 mũ chồng nhau — tái hiện điều kiện render v4 (chỉ có ở bản before)
if TAG == 'before':
    shot('allhats', (1.7, -2.5, 2.8), (0, 0, 1.30), "allhats-above")
print("FACE RENDERS DONE", TAG)
