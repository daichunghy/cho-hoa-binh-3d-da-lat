# render_glb_check.py — Render kiểm từng GLB riêng lẻ (BLENDER-DEEP-1).
# Dùng: blender5 -b --python render_glb_check.py -- <glb_path> <out_prefix> <view>
# view: "34" (3/4 từ mặt trước-phải-trên), "side" (ngang), "front" (chính diện),
#       "top" (từ trên xuống), "profile" (ngang sát, cho thang/cầu).
# Cycles CPU samples thấp, threads cố định 2 (máy RAM ít).
import bpy, sys, math, os
from mathutils import Vector

argv = sys.argv[sys.argv.index('--') + 1:]
glb_path, out_prefix, view = argv[0], argv[1], argv[2]
only = argv[3] if len(argv) > 3 else None

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=glb_path)
if only:
    keep = bpy.context.scene.objects.get(only)
    keep_names = set()
    if keep:
        keep_names.add(keep.name)
        for ch in keep.children_recursive: keep_names.add(ch.name)
    for o in list(bpy.context.scene.objects):
        if o.name not in keep_names and o.type in ('MESH', 'EMPTY'):
            bpy.data.objects.remove(o, do_unlink=True)

# bbox toàn cảnh
mins = Vector((1e9, 1e9, 1e9)); maxs = Vector((-1e9, -1e9, -1e9))
for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        for c in o.bound_box:
            w = o.matrix_world @ Vector(c)
            mins = Vector(map(min, mins, w)); maxs = Vector(map(max, maxs, w))
ctr = (mins + maxs) / 2; size = maxs - mins
R = max(size) * 0.5

sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.samples = 16
sc.cycles.use_denoising = False
sc.render.threads_mode = 'FIXED'; sc.render.threads = 2
sc.render.resolution_x = 640; sc.render.resolution_y = 480
sc.render.film_transparent = False
w = bpy.data.worlds.new('W'); sc.world = w
w.use_nodes = True
w.node_tree.nodes['Background'].inputs[0].default_value = (0.35, 0.38, 0.45, 1)
w.node_tree.nodes['Background'].inputs[1].default_value = 0.7

sun = bpy.data.objects.new('Sun', bpy.data.lights.new('Sun', 'SUN'))
sun.data.energy = 3.0; sun.rotation_euler = (math.radians(50), 0, math.radians(30))
sc.collection.objects.link(sun)
fill = bpy.data.objects.new('Fill', bpy.data.lights.new('Fill', 'SUN'))
fill.data.energy = 1.0; fill.rotation_euler = (math.radians(70), 0, math.radians(-120))
sc.collection.objects.link(fill)

cam = bpy.data.objects.new('Cam', bpy.data.cameras.new('Cam'))
sc.collection.objects.link(cam); sc.camera = cam
D = R * 2.6 + 2.0
if view == '34':    off = Vector((D * 0.75, -D * 0.75, D * 0.5))
elif view == 'side': off = Vector((D, 0, R * 0.25))
elif view == 'front': off = Vector((0, -D, R * 0.3))
elif view == 'top':  off = Vector((D * 0.25, -D * 0.35, D * 1.15))
elif view == 'profile': off = Vector((D * 1.05, -D * 0.25, R * 0.15))
else: off = Vector((D * 0.75, -D * 0.75, D * 0.5))
cam.location = ctr + off
cam.rotation_euler = (ctr - cam.location).to_track_quat('-Z', 'Y').to_euler()
cam.data.clip_end = D * 8
sc.render.filepath = out_prefix + '-' + view + '.png'
bpy.ops.render.render(write_still=True)
print('RENDERED', sc.render.filepath, 'bbox size', tuple(round(s, 2) for s in size))
