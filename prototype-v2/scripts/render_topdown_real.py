# -*- coding: utf-8 -*-
"""LAYOUT-FIX-1 — RENDER TOP-DOWN BẰNG GLB THẬT (bằng chứng bố cục trước/sau).

Dựng lại bố cục nhìn từ trên cao bằng CHÍNH CÁC GLB THẬT trong assets/:
market (0,0,20), roundabout (-30,0,-6), stairs (SX,0,-16) — SX lấy từ tham số
dòng lệnh để render bản TRƯỚC (SX=0) và SAU (SX=-56) bằng cùng một script.
Thêm vành đường vòng đảo R11.8 (code: CircleGeometry tại (-30,0.045,-6)) vẽ
bằng đĩa phẳng để thấy rõ quan hệ thang <-> vòng xe quanh đảo.

Camera: ORTHO thẳng từ trên cao, bắc (đồi, -z three) lên trên khung —
khớp hướng minimap trong game. Quy ước three (x,y-up,z) -> Blender (x,-z,y).

Chạy: blender --background --threads 2 --python scripts/render_topdown_real.py \
        -- --stairs-x 0 --out layout-before
"""
import bpy, math, os, sys
from mathutils import Vector, Matrix

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
args = dict(zip(argv[::2], argv[1::2]))
STAIRS_X = float(args.get('--stairs-x', '0'))
OUTNAME = args.get('--out', 'layout-topdown')

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

def three_to_blender(p):
    return Vector((p[0], -p[2], p[1]))

def import_asset(name, three_pos, scale=1.0, rot_y=0.0):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name + ".glb"))
    new = [o for o in bpy.data.objects if o not in before]
    roots = [o for o in new if o.parent is None or o.parent in before]
    off = three_to_blender(three_pos)
    for o in roots:
        if abs(rot_y) > 1e-9:
            m = (Matrix.Translation(off)
                 @ Matrix.Rotation(rot_y, 4, 'Z')
                 @ Matrix.Translation(-off)
                 @ o.matrix_world)
            o.matrix_world = m
        o.location = o.location + off
        if scale != 1.0:
            o.scale = o.scale * scale
    print(f"[td] {name}: dat tai three={three_pos}")
    return new

market_objs = import_asset('market', (0, 0, 20))
import_asset('roundabout', (-30, 0, -6))
import_asset('stairs', (STAIRS_X, 0, -16))

# 2 chỉnh màu mặt tiền theo code web (như render_facade_real)
def set_base_color(mat, hexcol):
    r = int(hexcol[1:3], 16) / 255.0
    g = int(hexcol[3:5], 16) / 255.0
    b = int(hexcol[5:7], 16) / 255.0
    for node in mat.node_tree.nodes:
        if node.type == 'BSDF_PRINCIPLED':
            node.inputs['Base Color'].default_value = (r, g, b, 1.0)
    mat.diffuse_color = (r, g, b, 1.0)

seen_mats = set()
for o in market_objs:
    if o.type != 'MESH':
        continue
    for slot in o.material_slots:
        m = slot.material
        if not m or m.name in seen_mats:
            continue
        seen_mats.add(m.name)
        base = m.name.split('.')[0]
        if base == 'SignLetters':
            set_base_color(m, '#c8372d')
        elif base in ('WallCream', 'ColumnCream'):
            set_base_color(m, '#e3d7bd')

# nền trung tính + vành đường vòng đảo R11.8 + đĩa đường trục z=1.5 (tham chiếu)
bpy.ops.mesh.primitive_plane_add(size=600, location=(0, 0, 0))
ground = bpy.context.active_object
ground.name = 'NeutralGround'
gm = bpy.data.materials.new('NeutralAsphalt')
gm.use_nodes = True
gm.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (0.23, 0.23, 0.24, 1.0)
gm.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 1.0
ground.data.materials.append(gm)

def flat_disc(three_pos, radius, color, name):
    bpy.ops.mesh.primitive_circle_add(radius=radius, fill_type='NGON', vertices=48,
                                      location=three_to_blender(three_pos))
    o = bpy.context.active_object
    o.name = name
    m = bpy.data.materials.new(name + 'Mat')
    m.use_nodes = True
    m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*color, 1.0)
    m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 1.0
    o.data.materials.append(m)
    return o

flat_disc((-30, 0.06, -6), 11.8, (0.10, 0.10, 0.11), 'RingRoadR11.8')   # vành xe quanh đảo
flat_disc((0, 0.04, -2), 1.6, (0.85, 0.25, 0.2), 'OldStairFootMark')    # mốc chân thang CŨ (0,-2) — chỉ để đối chiếu

# ánh sáng
world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes['Background']
bg.inputs[0].default_value = (0.55, 0.70, 0.95, 1.0)
bg.inputs[1].default_value = 0.85

sun_data = bpy.data.lights.new('Sun', 'SUN')
sun_data.energy = 3.0
sun_data.angle = math.radians(2.0)
sun = bpy.data.objects.new('Sun', sun_data)
bpy.context.scene.collection.objects.link(sun)
sun.location = (-40, 30, 90)
d = (Vector((0, 0, 0)) - sun.location).normalized()
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

# camera ORTHO từ trên cao: tâm three (-28, -14), khung ngang 156u
cam_data = bpy.data.cameras.new('CamTop')
cam_data.type = 'ORTHO'
cam_data.ortho_scale = 156.0
cam_data.clip_start = 0.1
cam_data.clip_end = 400
cam = bpy.data.objects.new('CamTop', cam_data)
bpy.context.scene.collection.objects.link(cam)
cam.location = three_to_blender((-28, 120, -14))
cam.rotation_euler = (0.0, 0.0, 0.0)  # nhìn thẳng xuống -Z Blender; +Y Blender (= -z three, phía đồi) lên trên khung
bpy.context.scene.camera = cam
print(f"[td] camera ortho tai Blender={tuple(round(v,1) for v in cam.location)} scale={cam_data.ortho_scale}")

scene = bpy.context.scene
scene.render.engine = 'CYCLES'
scene.cycles.samples = 16
scene.cycles.use_denoising = False
scene.render.resolution_x = 1200
scene.render.resolution_y = 900
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = os.path.join(OUT, OUTNAME + '.png')
bpy.ops.render.render(write_still=True)
print("[td] DA RENDER XONG ->", scene.render.filepath, "| stairs_x =", STAIRS_X)
