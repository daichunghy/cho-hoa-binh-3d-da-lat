# -*- coding: utf-8 -*-
"""Render so sánh mặt character cũ/mới (HEAD-OPT-1) — cận mặt 3 góc, cùng đèn, cùng mũ.
Mô phỏng web makePerson: chỉ beanie bật, khăn ẩn, 2 mũ còn lại ẩn.
Chạy: blender -b --factory-startup -noaudio --threads 2 --python scripts/render_headopt_compare.py -- <glb_path> <tag>
Ra: renders/ho1-<tag>-face-front.png / -face-34.png / -face-side.png (512x512, Cycles 24).
"""
import bpy, math, os, sys
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "renders")
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
GLB = argv[0]
TAG = argv[1] if len(argv) > 1 else "x"

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

def shot(cam_loc, cam_tgt, suffix, lens=50):
    clear(); setup()
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=GLB)
    objs = [o for o in bpy.data.objects if o not in before]
    for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
        h = find(objs, hn)
        if h: h.hide_render = (hn != 'HatBeanie')
    sc = find(objs, 'Scarf')
    if sc: sc.hide_render = True
    camera(cam_loc, cam_tgt, lens)
    bpy.context.scene.render.filepath = os.path.join(OUT, "ho1-%s-%s.png" % (TAG, suffix))
    bpy.ops.render.render(write_still=True)
    print("RENDERED", TAG, suffix)

# cận mặt chính diện (beanie — mũ phổ biến nhất trong đám đông)
shot((0, -1.3, 1.38), (0, 0, 1.35), "face-front")
# cận mặt 3/4 — soi mắt/má/miệng/tóc
shot((0.6, -1.0, 1.52), (0, 0, 1.32), "face-34", lens=55)
# cận mặt nghiêng — soi silhouette đầu/tóc/mũi
shot((1.25, -0.2, 1.35), (0, 0, 1.33), "face-side")
print("HEADOPT COMPARE DONE", TAG)
