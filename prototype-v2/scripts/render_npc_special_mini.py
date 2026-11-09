# -*- coding: utf-8 -*-
"""NPC-SPECIAL-1 mini-scene: kiểm chứng CẬN CẢNH 3 nhân vật đặc biệt (Chú Ba coi bói /
ca sĩ góc hát / cô lao công) theo ĐÚNG số đo + màu trong code game (index.html NPC-SPECIAL-1).
Nhập character.glb thật, sơn lại material theo tên như web recolor(), giấu mũ như makePerson,
dựng đạo cụ bằng hình học nguyên thủy tại đúng tọa độ three của code.
Quy ước: three (x, y-up, z) -> Blender (x, -z, y). Chạy:
blender -b --factory-startup -noaudio --threads 2 --python scripts/render_npc_special_mini.py
Ra: renders/sp1-chuba.png / sp1-singer.png / sp1-sweeper.png (640x480, Cycles 32).
"""
import bpy, math, os
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
OUT = os.path.join(HERE, "..", "renders")
os.makedirs(OUT, exist_ok=True)
GLB = os.path.join(ASSETS, "character.glb")

def C(p):  # three pos (rel người) -> blender loc
    return (p[0], -p[2], p[1])

def mat(hexv, rough=0.9):
    m = bpy.data.materials.new("m%06x" % hexv); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (((hexv >> 16 & 255) / 255), ((hexv >> 8 & 255) / 255), ((hexv & 255) / 255), 1)
    b.inputs["Roughness"].default_value = rough
    return m

def setup():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.engine = 'CYCLES'
    sc.cycles.samples = 32; sc.cycles.use_denoising = True
    try: sc.render.threads = 2; sc.render.threads_mode = 'FIXED'
    except Exception: pass
    sc.render.resolution_x = 640; sc.render.resolution_y = 480
    sc.view_settings.view_transform = 'Filmic'
    w = bpy.data.worlds.new("W"); sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes["Background"]
    bg.inputs[0].default_value = (0.16, 0.13, 0.10, 1)  # nền ấm mờ kiểu chợ đêm
    bg.inputs[1].default_value = 0.85
    d = bpy.data.lights.new("Sun", 'SUN'); d.energy = 2.6; d.color = (1.0, 0.9, 0.78)
    o = bpy.data.objects.new("Sun", d); bpy.context.collection.objects.link(o)
    o.rotation_euler = (math.radians(48), 0, math.radians(28))
    pt = bpy.data.objects.new("Pt", bpy.data.lights.new("Pt", 'POINT'))
    bpy.context.collection.objects.link(pt)
    pt.location = (0.8, -1.6, 2.2); pt.data.energy = 260; pt.data.color = (1.0, 0.78, 0.5)
    # sàn
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, -0.05))
    g = bpy.context.object; g.scale = (9, 9, 0.1); bpy.ops.object.transform_apply(scale=True)
    g.data.materials.append(mat(0x5a4f42))
    return sc

def find(objs, base):
    for o in objs:
        if o.name.split('.')[0] == base:
            return o
    return None

def load_person():
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=GLB)
    return [o for o in bpy.data.objects if o not in before]

def recolor(objs, matname, hexv):
    m = mat(hexv)
    for o in objs:
        if o.type == 'MESH' and o.data and o.data.materials:
            for i, ms in enumerate(o.data.materials):
                if ms and ms.name.split('.')[0] == matname:
                    o.data.materials[i] = m

def paint_node(objs, nodename, hexv):
    root = find(objs, nodename)
    if not root: return
    m = mat(hexv)
    for o in [root] + list(root.children_recursive):
        if o.type == 'MESH' and o.data and o.data.materials:
            for i in range(len(o.data.materials)):
                o.data.materials[i] = m

def hats(objs, show):
    for hn in ('HatNonLa', 'HatBeanie', 'HatCap'):
        h = find(objs, hn)
        if h: h.hide_render = (hn != show)

def tbox(size3, pos3, hexv, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(location=C(pos3))
    o = bpy.context.object
    o.dimensions = (size3[0], size3[2], size3[1])
    o.rotation_euler = rot
    o.data.materials.append(mat(hexv))
    return o

def tsphere(r, pos3, hexv, scale3=(1, 1, 1), seg=16, ring=12):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, segments=seg, ring_count=ring, location=C(pos3))
    o = bpy.context.object
    o.scale = (scale3[0], scale3[2], scale3[1])
    o.data.materials.append(mat(hexv))
    return o

def headprop(size3, hpos, hexv, sph=None):
    # hpos/size theo three Head-local: person (hx, 1.35+hy, hz)
    p3 = (hpos[0], 1.35 + hpos[1], hpos[2])
    if sph:
        return tsphere(sph[0], p3, hexv, scale3=sph[1])
    return tbox(size3, p3, hexv)

def glasses():
    headprop((0.17, 0.12, 0.03), (-0.16, 0.045, 0.435), 0x23272e)
    headprop((0.17, 0.12, 0.03), (0.16, 0.045, 0.435), 0x23272e)
    headprop((0.15, 0.025, 0.025), (0, 0.07, 0.435), 0x23272e)
    headprop((0.02, 0.02, 0.38), (-0.29, 0.06, 0.25), 0x23272e)
    headprop((0.02, 0.02, 0.38), (0.29, 0.06, 0.25), 0x23272e)

def camera(loc, tgt, lens=42):
    d = bpy.data.cameras.new("Cam"); d.lens = lens
    o = bpy.data.objects.new("Cam", d); bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_mode = 'QUATERNION'
    o.rotation_quaternion = (Vector(tgt) - Vector(loc)).to_track_quat('-Z', 'Y')
    bpy.context.scene.camera = o

def render(name):
    bpy.context.scene.render.filepath = os.path.join(OUT, name)
    bpy.ops.render.render(write_still=True)
    print("RENDERED", name, flush=True)

# ================= CHÚ BA COI BÓI (ngồi ghế, áo dài + râu bạc + kính + khăn xếp, bàn + thẻ) =================
setup()
objs = load_person()
recolor(objs, 'Shirt', 0x37455e); recolor(objs, 'Pants', 0xe8e2d4); recolor(objs, 'Skin', 0xc68a5e)
hats(objs, None)
scf = find(objs, 'Scarf');  scf and setattr(scf, 'hide_render', True)
# nâng người lên mặt ghế (+0.30 như game: origin tại mặt ghế)
for o in objs:
    if o.parent is None: o.location.z += 0.30
for nm, rx in (('LegL', -1.45), ('LegR', -1.45), ('ArmL', -0.7), ('ArmR', -0.9)):
    o = find(objs, nm)
    if o: o.rotation_euler.x = rx
# tà áo dài + ve áo (npcPart 'R' trong game)
tbox((0.69, 0.35, 0.45), (0, 0.36 + 0.30, 0), 0x37455e)
tbox((0.13, 0.30, 0.03), (-0.10, 0.80 + 0.30, 0.235), 0x37455e, rot=(0, 0, 0.18))
tbox((0.13, 0.30, 0.03), (0.10, 0.80 + 0.30, 0.235), 0x37455e, rot=(0, 0, -0.18))
# mặt: râu + ria + kính + khăn xếp (Head-local + dịch +0.30 vì người nâng lên ghế -> cộng vào y three = z blender)
def headprop_up(size3, hpos, hexv, sph=None):
    p3 = (hpos[0], 1.35 + hpos[1] + 0.30, hpos[2])
    if sph: return tsphere(sph[0], p3, hexv, scale3=sph[1])
    return tbox(size3, p3, hexv)
headprop_up(None, (0, -0.27, 0.29), 0xb8b0a2, sph=(0.17, (1.05, 0.72, 0.62)))
headprop_up((0.16, 0.03, 0.03), (0, -0.06, 0.415), 0xb8b0a2)
for s_, p_ in (((0.17, 0.12, 0.03), (-0.16, 0.045, 0.435)), ((0.17, 0.12, 0.03), (0.16, 0.045, 0.435)),
               ((0.15, 0.025, 0.025), (0, 0.07, 0.435)), ((0.02, 0.02, 0.38), (-0.29, 0.06, 0.25)),
               ((0.02, 0.02, 0.38), (0.29, 0.06, 0.25))):
    headprop_up(s_, p_, 0x23272e)
# khăn xếp: torus (blender mặc định đã nằm ngang) + đỉnh cầu dẹt
bpy.ops.mesh.primitive_torus_add(major_radius=0.40, minor_radius=0.085, major_segments=18, minor_segments=8,
                                 location=(0, -0.01, 1.35 + 0.30 + 0.30))
bpy.context.object.data.materials.append(mat(0x27324e))
headprop_up(None, (0, 0.36, 0.01), 0x27324e, sph=(0.30, (1, 0.45, 1)))
# ghế + bàn + thẻ (three rel GỐC NGƯỜI Ở MẶT ĐẤT +0.30 do người ngồi trên ghế: y three = rel + 0.30)
tbox((0.34, 0.05, 0.34), (0, 0.30, 0), 0x7a1f1a)
tbox((0.26, 0.28, 0.26), (0, 0.14, 0), 0x7a1f1a)
tbox((0.85, 0.48, 0.55), (0, 0.24, 0.68), 0x6b4a2f)
tbox((0.92, 0.04, 0.62), (0, 0.50, 0.68), 0x7a1f1a)
for ci in range(3):
    tbox((0.15, 0.012, 0.21), (-0.18 + ci * 0.18, 0.525, 0.68), 0xf0ead8, rot=(0, 0, (ci - 1) * 0.35))
camera((2.0, -2.7, 1.6), (0, 0, 1.05))
render("sp1-chuba.png")

# ================= CA SĨ (đứng, denim + mũ đỏ rượu + kính mát + khăn + guitar) =================
setup()
objs = load_person()
recolor(objs, 'Shirt', 0x2f4d6e); recolor(objs, 'Pants', 0x2e2a26); recolor(objs, 'Skin', 0xc68a5e)
recolor(objs, 'Scarf', 0x8c2f39)
hats(objs, 'HatCap')
paint_node(objs, 'HatCap', 0x8c2f39)
scf = find(objs, 'Scarf');  scf and setattr(scf, 'hide_render', False)
for nm, rx in (('ArmL', -0.75), ('ArmR', -0.95)):
    o = find(objs, nm)
    if o: o.rotation_euler.x = rx
glasses()
# guitar: thân đĩa + cổ (số đo khối sân khấu trong game)
bpy.ops.mesh.primitive_cone_add(vertices=20, radius1=0.26, radius2=0.26, depth=0.09, location=C((0.16, 0.92, 0.30)))
go = bpy.context.object; go.rotation_euler = (math.pi / 2 - 0.35, 0, 0.15); go.data.materials.append(mat(0x9c3a24))
# cổ đàn: trong game nằm trong group guitar xoay (0.15,0,-0.35) + tự xoay z -0.5 -> hướng three ~(0.66,0.72,0.10);
# bản mini: đặt hộp cổ tại tâm đã cộng group (0.45, 1.07, 0.33) three và chĩa trục +Y theo hướng đó (quaternion).
bpy.ops.mesh.primitive_cube_add(location=C((0.45, 1.07, 0.33)))
no = bpy.context.object; no.dimensions = (0.05, 0.045, 0.52)
no.rotation_mode = 'QUATERNION'
no.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(Vector((0.66, -0.10, 0.72)).normalized())
no.data.materials.append(mat(0x4c3428))
camera((1.5, -2.3, 1.3), (0, 0, 1.0))
render("sp1-singer.png")

# ================= CÔ LAO CÔNG (đứng, bảo hộ xanh + mũ cam + sọc phản quang + chổi) =================
setup()
objs = load_person()
recolor(objs, 'Shirt', 0x1f6f8b); recolor(objs, 'Pants', 0x2e4a54); recolor(objs, 'Skin', 0xa96f42)
hats(objs, 'HatCap')
paint_node(objs, 'HatCap', 0xe8862e)
scf = find(objs, 'Scarf');  scf and setattr(scf, 'hide_render', True)
for nm, rx in (('ArmL', -0.68), ('ArmR', -0.85)):
    o = find(objs, nm)
    if o: o.rotation_euler.x = rx
tbox((0.54, 0.05, 0.02), (0, 0.70, 0.245), 0xd8dde2)  # sọc phản quang
# chổi: pivot (0.30, 0.95, 0.22); cán + đầu + nan theo số đo code
bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=0.018, radius2=0.018, depth=1.05, location=C((0.30, 0.57, 0.29)))
ho = bpy.context.object; ho.rotation_euler = (0.38, 0, 0); ho.data.materials.append(mat(0xb08954))
tbox((0.36, 0.07, 0.05), (0.30, 0.15, 0.46), 0x8a6a34)
for fi in range(-2, 3):
    tbox((0.055, 0.16, 0.02), (0.30 + fi * 0.07, 0.07, 0.48), 0xc9a44e, rot=(0.25, 0, fi * 0.16))
camera((1.5, -2.1, 1.05), (0, 0, 0.8))
render("sp1-sweeper.png")
print("NPC SPECIAL MINI DONE", flush=True)
