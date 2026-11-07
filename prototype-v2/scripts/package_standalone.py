# -*- coding: utf-8 -*-
"""Đóng gói index-standalone.html: nhúng toàn bộ GLB dạng base64 vào index.html.
Chạy: python3 scripts/package_standalone.py
- Đọc danh sách asset từ chính index.html (const names = [...]).
- Thay đoạn tải 'assets/'+n+'.glb' bằng tra cứu GLB_DATA[n].
"""
import base64, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

m = re.search(r"const names = \[([^\]]+)\];", html)
assert m, "không tìm thấy const names"
names = re.findall(r"'([^']+)'", m.group(1))
print("assets:", names)

blobs = []
total_raw = 0
for n in names:
    p = os.path.join(ROOT, "assets", n + ".glb")
    data = open(p, "rb").read()
    assert data[:4] == b"glTF", f"{p} không phải GLB"
    total_raw += len(data)
    b64 = base64.b64encode(data).decode()
    blobs.append(f'  {n}: "data:model/gltf-binary;base64,{b64}"')
glb_data = "const GLB_DATA = {\n" + ",\n".join(blobs) + "\n};\n"

old_expr = "'assets/' + n + '.glb'"
assert html.count(old_expr) == 1, "không khớp biểu thức tải asset"
out = html.replace(old_expr, "GLB_DATA[n]")
anchor = "const ASSETS = {};"
assert out.count(anchor) == 1
out = out.replace(anchor, glb_data + anchor)

outpath = os.path.join(ROOT, "index-standalone.html")
open(outpath, "w", encoding="utf-8").write(out)
size = os.path.getsize(outpath)
print(f"GLB raw total: {total_raw:,} bytes")
print(f"STANDALONE: {outpath} = {size:,} bytes ({size/1048576:.2f} MB)")
print("VUOT 10MB!" if size > 10 * 1048576 else "duoi nguong 10MB OK")
