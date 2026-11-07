# QA tủ đồ v4.4: render cận TỪNG MÓN trên character.glb theo đúng spec WARDROBE_DEFS trong index.html
# three(x,y,z) -> blender(x,-z,y); xoay euler xấp xỉ (rx, -rz, ry); pattern canvas chỉ kiểm chứng ở web (ghi chú trong báo cáo)
import bpy, json, re, math, sys
from mathutils import Vector, Euler

WD = "/home/hatch/workspace/cho-hoa-binh-3d/prototype-v2"
def hex2lin(hx):
    hx = hx.lstrip('#')
    out = []
    for k in (0, 2, 4):
        c = int(hx[k:k + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return tuple(out)

src = open(WD + "/index.html", encoding="utf-8").read()
i = src.index("const WARDROBE_DEFS = ")
start = src.index("[", i)
depth, j = 0, start
for j in range(start, len(src)):
    if src[j] == "[": depth += 1
    elif src[j] == "]":
        depth -= 1
        if not depth: break
DEFS = json.loads(src[start:j + 1])
BYID = {d["id"]: d for d in DEFS}
print("DEFS", len(DEFS))

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=WD + "/assets/character.glb")
CHAR = [o for o in bpy.data.objects]
def by_mat(name):
    out = []
    for o in CHAR:
        if o.type == 'MESH' and any(m and m.name == name for m in o.data.materials): out.append(o)
    return out
def by_name(n):
    for o in CHAR:
        if o.name == n: return o
    return None
def paint(matname, hexcol):
    rgb = hex2lin(hexcol)
    for o in by_mat(matname):
        for m in o.data.materials:
            if m and m.name == matname:
                m.diffuse_color = (*rgb, 1)
                nt = m.node_tree
                if nt:
                    bsdf = nt.nodes.get("Principled BSDF")
                    if bsdf: bsdf.inputs["Base Color"].default_value = (*rgb, 1)
NODES = {n: by_name(n) for n in ('HatBeanie', 'HatCap', 'HatNonLa', 'Scarf')}
def set_nodes(hat_node=None, scarf_on=False):
    for n, o in NODES.items():
        if o: o.hide_render = not ((n == hat_node) or (n == 'Scarf' and scarf_on))

# sân khấu nhỏ
bpy.ops.mesh.primitive_circle_add(radius=2.6, location=(0, 0, 0.0))
disc = bpy.context.active_object; disc.name = "QA_disc"
dm = bpy.data.materials.new("QADisc"); dm.diffuse_color = (0.16, 0.11, 0.07, 1); disc.data.materials.append(dm)
def light(name, loc, energy, color, size=2.0):
    ld = bpy.data.lights.new(name, 'AREA'); ld.energy = energy; ld.color = color; ld.shape = 'DISK'; ld.size = size
    lo = bpy.data.objects.new(name, ld); lo.location = loc; bpy.context.collection.objects.link(lo)
    lo.rotation_euler = Euler((math.radians(50), 0, math.radians(-30)), 'XYZ')
    return lo
light("key", (1.6, -2.2, 2.6), 420, (1.0, 0.78, 0.52))
light("fill", (-2.0, -1.4, 1.4), 150, (0.75, 0.82, 1.0))
light("rim", (0.5, 2.2, 2.2), 240, (1.0, 0.62, 0.35))
w = bpy.data.worlds.get('World') or bpy.data.worlds.new('World'); bpy.context.scene.world = w; w.use_nodes = True
w.node_tree.nodes['Background'].inputs[0].default_value = (0.035, 0.045, 0.09, 1)
w.node_tree.nodes['Background'].inputs[1].default_value = 1.0
cam_data = bpy.data.cameras.new("cam"); cam_data.lens = 52
cam = bpy.data.objects.new("cam", cam_data); bpy.context.collection.objects.link(cam)
bpy.context.scene.camera = cam
def look(cam_obj, target):
    d = Vector(target) - cam_obj.location
    cam_obj.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
sc = bpy.context.scene
sc.render.engine = 'CYCLES'; sc.cycles.samples = 6; sc.cycles.use_denoising = False
sc.cycles.device = 'CPU'
sc.render.resolution_x = 400; sc.render.resolution_y = 400
sc.view_settings.view_transform = 'Filmic'; sc.view_settings.exposure = 0.05

PIV = { 'R': (0, 0, 0), 'AR': (0.40, 0, 0.88), 'AL': (-0.40, 0, 0.88), 'LL': (-0.12, 0, 0.40), 'LR': (0.12, 0, 0.40) }  # pivot dung theo dump GLB ĐỢT MODEL 07/11: hip 0.40, vai (±0.40, 0.88)
def t2b(p): return (p[0], -p[2], p[1])
def part_loc(anchor, p):
    pv = PIV[anchor]; q = t2b(p)
    return (pv[0] + q[0], pv[1] + q[1], pv[2] + q[2])
_mats = {}
def pmat(p):
    key = p['c'] + str(p.get('e', ''))
    if key in _mats: return _mats[key]
    m = bpy.data.materials.new("WDM")
    rgb = hex2lin(p['c'])
    m.diffuse_color = (*rgb, 1)
    m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]; b.inputs["Base Color"].default_value = (*rgb, 1); b.inputs["Roughness"].default_value = 0.92
    if p.get('e'):
        b.inputs["Emission Color"].default_value = (*rgb, 1); b.inputs["Emission Strength"].default_value = p['e']
    _mats[key] = m; return m
created = []
def add_part(p, anchor):
    loc = part_loc(anchor, p['p'])
    g = p['g']
    if g == 'flower':
        sc_ = p['s'][0]
        cols = [p['c'], p.get('c2', '#7a4a2e')]
        objs = []
        cen = bpy.ops.mesh.primitive_uv_sphere_add(radius=0.035 * sc_, location=loc)
        co = bpy.context.active_object; co.name = "WDP_"; co.data.materials.append(pmat({'c': cols[1]})); objs.append(co)
        flat = bool(p.get('r'))
        for k in range(6):
            a = k / 6 * math.pi * 2
            off3 = (math.cos(a) * 0.058 * sc_, math.sin(a) * 0.058 * sc_, -0.005)
            off = (loc[0] + off3[0], loc[1] + (0.005 if not flat else off3[1]), loc[2] + (off3[1] if not flat else 0.005))
            if flat: off = (loc[0] + off3[0], loc[1] + off3[1], loc[2] + 0.01)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045 * sc_, location=off)
            po = bpy.context.active_object; po.name = "WDP_"; po.scale = (1.5, 0.45, 0.7) if not flat else (1.5, 0.7, 0.45)
            po.data.materials.append(pmat({'c': cols[0]})); objs.append(po)
        created.extend(objs); return
    if g == 'box': bpy.ops.mesh.primitive_cube_add(location=loc); o = bpy.context.active_object; o.scale = (p['s'][0] / 2, p['s'][2] / 2, p['s'][1] / 2)  # three [x,y,z] -> blender (x, z, y)
    elif g == 'sph': bpy.ops.mesh.primitive_uv_sphere_add(radius=p['s'][0], location=loc); o = bpy.context.active_object
    elif g in ('cyl', 'cone'):
        if g == 'cyl' and p['s'][0] == p['s'][1]: bpy.ops.mesh.primitive_cylinder_add(radius=p['s'][0], depth=p['s'][2], location=loc)
        else: bpy.ops.mesh.primitive_cone_add(radius1=p['s'][1] if g == 'cyl' else p['s'][0], radius2=p['s'][0] if g == 'cyl' else 0.0, depth=p['s'][2] if g == 'cyl' else p['s'][1], location=loc)
        o = bpy.context.active_object
    elif g == 'tor': bpy.ops.mesh.primitive_torus_add(major_radius=p['s'][0], minor_radius=p['s'][1], location=loc); o = bpy.context.active_object
    else: return
    o.name = "WDP_"
    if p.get('r'):
        r3 = p['r']
        base_x = math.pi / 2 if g == 'tor' else 0.0  # torus three (vòng coronal) -> blender cộng Rx 90°
        o.rotation_euler = Euler((base_x + r3[0], -r3[2], r3[1]), 'XYZ')
    elif g == 'tor':
        o.rotation_euler = Euler((math.pi / 2, 0, 0), 'XYZ')
    if p.get('sc'): o.scale = (o.scale[0] * p['sc'][0], o.scale[1] * p['sc'][2], o.scale[2] * p['sc'][1])
    o.data.materials.append(pmat(p))
    created.append(o)
def clear_parts():
    global created
    for o in created:
        if o and o.name in bpy.data.objects: bpy.data.objects.remove(o, do_unlink=True)
    created = []
def apply_item(d, base=True):
    clear_parts()
    paint('Shirt', '#a62b25'); paint('Beanie', '#a62b25'); paint('Scarf', '#d9a62e')
    set_nodes('HatBeanie' if base else None, False)
    if base: paint('Beanie', '#a62b25')
    # lớp nền theo ô: mũ đơn độc; khăn/áo thêm M1; tay/phụ kiện/giày thêm M1+K1+A1(màu)
    slot = d['slot']
    if slot in ('hand', 'extra', 'shoes') and base:
        set_nodes('HatBeanie', True); paint('Scarf', '#2e6b46')
    if slot == 'hat':
        node = {'beanie': 'HatBeanie', 'nonla': 'HatNonLa'}.get(d.get('node'))
        set_nodes(node, False)
        if d.get('mat') == 'Beanie': paint('Beanie', d['color'])
    elif slot == 'scarf':
        set_nodes('HatBeanie', d.get('node') == 'scarf')
        if d.get('node') == 'scarf': paint('Scarf', d['color'])
    elif slot == 'coat':
        set_nodes('HatBeanie', False)
        if d.get('mat') == 'Shirt': paint('Shirt', d['color'])
    for p in d.get('parts', []):
        anchors = {'LEGS': ('LL', 'LR'), 'ARMS': ('AL', 'AR')}.get(p['a'], (p['a'],))
        if d.get('sway') and p['a'] == 'R':
            pp = dict(p); pp['p'] = [p['p'][0] + d['sway'][0], p['p'][1] + d['sway'][2], p['p'][2] + d['sway'][1]]
            # sway parts: p đã tương đối pivot (three) -> cộng pivot three (x, z, y) rồi t2b xử lý ở part_loc với anchor R cần p three đầy đủ:
            pp['p'] = [d['sway'][0] + p['p'][0], d['sway'][1] + p['p'][1], d['sway'][2] + p['p'][2]]
            add_part(pp, 'R'); continue
        for a in anchors: add_part(p, a)

FRAMES = {
  'hat':   ((0.85, -1.45, 1.68), (0, 0, 1.42)),
  'scarf': ((0.85, -1.55, 1.28), (0, 0, 0.90)),
  'coat':  ((1.05, -1.95, 1.02), (0, 0, 0.68)),
  'hand':  ((1.25, -1.25, 0.88), (0.38, -0.02, 0.44)),
  'extra': ((1.55, -2.55, 1.22), (0, 0, 0.80)),
  'shoes': ((0.85, -1.35, 0.50), (0, 0, 0.26)),
}
import os
os.makedirs(WD + "/renders", exist_ok=True)
order = ['hat', 'scarf', 'coat', 'hand', 'extra', 'shoes']
import os as _os
ONLY = _os.environ.get('WD_ONLY', '')
only_ids = set(ONLY.split(',')) if ONLY else None
for slot in order:
    camloc, tgt = FRAMES[slot]
    cam.location = camloc; look(cam, tgt)
    for d in [x for x in DEFS if x['slot'] == slot and (only_ids is None or x['id'] in only_ids)]:
        if d['id'] in ('T8', 'T9'):
            cam.location = (2.0, -3.3, 1.62); look(cam, (0.05, 0, 1.22))
        else:
            cam.location = camloc; look(cam, tgt)
        apply_item(d)
        suf = ""
        if _os.environ.get('WD_CAMBACK') and slot == 'extra':
            cam.location = (1.3, 2.7, 1.22); look(cam, (0, 0, 0.80)); suf = "-back"
        sc.render.filepath = WD + "/renders/wd-" + d['id'] + suf + ".png"
        bpy.ops.render.render(write_still=True)
        print("RENDERED", d['id'])
# 2 bộ đầy đủ đối chứng
def apply_outfit(ids):
    clear_parts()
    paint('Shirt', '#a62b25'); paint('Beanie', '#a62b25'); set_nodes(None, False)
    for id_ in ids:
        d = BYID[id_]
        if d['slot'] == 'hat':
            set_nodes({'beanie': 'HatBeanie', 'nonla': 'HatNonLa'}.get(d.get('node')), NODES['Scarf'].hide_render == False)
            if d.get('mat') == 'Beanie': paint('Beanie', d['color'])
        if d['slot'] == 'scarf':
            if d.get('node') == 'scarf': set_nodes('HatBeanie' if BYID['M1'] else None, True); paint('Scarf', d['color'])
        if d['slot'] == 'coat' and d.get('mat') == 'Shirt': paint('Shirt', d['color'])
        for p in d.get('parts', []):
            anchors = {'LEGS': ('LL', 'LR'), 'ARMS': ('AL', 'AR')}.get(p['a'], (p['a'],))
            if d.get('sway') and p['a'] == 'R':
                pp = dict(p); pp['p'] = [d['sway'][0] + p['p'][0], d['sway'][1] + p['p'][1], d['sway'][2] + p['p'][2]]
                add_part(pp, 'R'); continue
            for a in anchors: add_part(p, a)
if only_ids is not None:
    _out = _os.environ.get('WD_OUTFIT', '')
    if _out:
        cam.location = (1.7, -2.9, 1.42); look(cam, (0, 0, 0.86))
        apply_outfit(_out.split(','))
        sc.render.filepath = WD + "/renders/wd-outfit-" + _os.environ.get('WD_OUTNAME', 'set') + ".png"; bpy.ops.render.render(write_still=True)
    print("SUBSET DONE"); sys.exit(0)
cam.location = (1.7, -2.9, 1.42); look(cam, (0, 0, 0.86))
apply_outfit(['M1', 'K1', 'A1', 'T1', 'P1', 'G1'])
sc.render.filepath = WD + "/renders/wd-outfit-basic.png"; bpy.ops.render.render(write_still=True)
apply_outfit(['M2', 'K3', 'A2', 'T10', 'P2', 'P12', 'G4'])
sc.render.filepath = WD + "/renders/wd-outfit-night.png"; bpy.ops.render.render(write_still=True)
print("ALL DONE")
