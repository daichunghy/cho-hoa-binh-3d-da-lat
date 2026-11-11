# -*- coding: utf-8 -*-
"""STAIR-TOP-PAIR-1 — RENDER TOP-DOWN VÙNG ĐỈNH THANG MỚI (kiểm chứng cặp nhà đỉnh thang).

GLB thật: stairs tại (-56,0,-16). Hai tòa La Tulipe / L'angfarm là CODE-BUILT (không có GLB)
nên vẽ bằng HỘP FOOTPRINT đúng kích thước code (thân 8.8 x 6.2, cao tương đối) tại vị trí MỚI,
kèm footprint hàng shophouse z=-28.5 (xám) + ki-ốt (-24,-37) để soi va chạm/khe hở,
điểm TOUR target (-56,-33) và đường thẳng tham chiếu tới check-in (-19,-48).

Chạy: blender --background --threads 2 --python scripts/render_topdown_stairtoppair.py
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ASSETS = os.path.join(ROOT, "assets")
OUT = os.path.join(ROOT, "renders")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)

def three_to_blender(p):
    return Vector((p[0], -p[2], p[1]))

def import_asset(name, three_pos):
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=os.path.join(ASSETS, name + ".glb"))
    new = [o for o in bpy.data.objects if o not in before]
    roots = [o for o in new if o.parent is None or o.parent in before]
    off = three_to_blender(three_pos)
    for o in roots:
        o.location = o.location + off
    print(f"[stp] {name}: dat tai three={three_pos}")
    return new

import_asset('stairs', (-56, 0, -16))

def mat_new(name, color):
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = (*color, 1.0)
    m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value = 1.0
    return m

def box_three(cx, cy, cz, sx, sy, sz, color, name):
    bpy.ops.mesh.primitive_cube_add(location=three_to_blender((cx, cy, cz)))
    o = bpy.context.active_object
    o.name = name
    o.scale = (sx / 2, sz / 2, sy / 2)  # Blender: x=three x, y=three -z(bo dau khi scale duong), z=three y
    bpy.ops.object.transform_apply(scale=True)
    o.data.materials.append(mat_new(name + 'Mat', color))
    return o

# nền trung tính + cao nguyên y17 (z<=-30)
bpy.ops.mesh.primitive_plane_add(size=600, location=(0, 0, 0))
g0 = bpy.context.active_object; g0.name = 'NeutralGround'
g0.data.materials.append(mat_new('NeutralMat', (0.23, 0.23, 0.24)))
bpy.ops.mesh.primitive_plane_add(size=2, location=three_to_blender((-50, 16.9, -45)))
gp = bpy.context.active_object; gp.name = 'PlateauY17'
gp.scale = (65, 15, 1); bpy.ops.object.transform_apply(scale=True)
gp.data.materials.append(mat_new('PlateauMat', (0.35, 0.33, 0.30)))

# cặp nhà MỚI (code-built -> hộp footprint): La Tulipe (-73.5,-33.5) cao ~11; L'angfarm (-38.5,-33.5) cao ~8.4
box_three(-73.5, 17 + 5.5, -36.4, 8.8, 11.0, 6.2, (0.35, 0.55, 0.85), 'LaTulipe_NEW')
box_three(-38.5, 17 + 4.2, -36.4, 8.8, 8.4, 6.2, (0.85, 0.55, 0.30), "Langfarm_NEW")
# hàng shophouse z=-28.5 (footprint thân 7x5.6, xám) — vật có sẵn gần nhất
for sx in (-80, -62, -52, -42):
    box_three(sx, 17 + 0.35, -28.5, 7, 0.7, 5.6, (0.45, 0.45, 0.45), f'ShopRow_{sx}')
# ki-ốt (-24,-37) footprint 2.6x2.2
box_three(-24, 17 + 0.35, -37, 2.6, 0.7, 2.2, (0.45, 0.45, 0.45), 'KioskDoChoi')
# mốc: TOUR target (-56,-33) đỏ + check-in (-19,-48) vàng + đoạn thẳng nối (chấm tham chiếu)
def disc_three(cx, cz, r, color, name, y=17.15):
    bpy.ops.mesh.primitive_circle_add(radius=r, fill_type='NGON', vertices=32,
                                      location=three_to_blender((cx, y, cz)))
    o = bpy.context.active_object; o.name = name
    o.data.materials.append(mat_new(name + 'Mat', color))
    return o
disc_three(-56, -33, 1.6, (0.9, 0.2, 0.15), 'TourTarget')
disc_three(-19, -48, 1.6, (0.95, 0.8, 0.2), 'Checkin')
for t in (0.25, 0.5, 0.75):
    disc_three(-56 + 37 * t, -33 - 15 * t, 0.55, (0.95, 0.9, 0.3), f'PathPt{t}', y=17.12)

# ánh sáng
world = bpy.data.worlds.get('World') or bpy.data.worlds.new('World')
bpy.context.scene.world = world
world.use_nodes = True
world.node_tree.nodes['Background'].inputs[0].default_value = (0.55, 0.70, 0.95, 1.0)
world.node_tree.nodes['Background'].inputs[1].default_value = 0.85
sun_data = bpy.data.lights.new('Sun', 'SUN'); sun_data.energy = 3.0; sun_data.angle = math.radians(2.0)
sun = bpy.data.objects.new('Sun', sun_data); bpy.context.scene.collection.objects.link(sun)
sun.location = (-40, 30, 90)
d = (Vector((0, 0, 0)) - sun.location).normalized()
sun.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()

cam_data = bpy.data.cameras.new('CamTop'); cam_data.type = 'ORTHO'; cam_data.ortho_scale = 100.0
cam_data.clip_start = 0.1; cam_data.clip_end = 400
cam = bpy.data.objects.new('CamTop', cam_data); bpy.context.scene.collection.objects.link(cam)
cam.location = three_to_blender((-52, 120, -31)); cam.rotation_euler = (0.0, 0.0, 0.0)
bpy.context.scene.camera = cam

scene = bpy.context.scene
scene.render.engine = 'CYCLES'; scene.cycles.samples = 16; scene.cycles.use_denoising = False
scene.render.resolution_x = 1300; scene.render.resolution_y = 900; scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = 'PNG'
scene.render.filepath = os.path.join(OUT, 'stairtoppair-topdown.png')
bpy.ops.render.render(write_still=True)
print("[stp] DA RENDER XONG ->", scene.render.filepath)
