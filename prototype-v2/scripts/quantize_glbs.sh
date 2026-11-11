#!/usr/bin/env bash
# =====================================================================
# quantize_glbs.sh — Lượng tử hoá KHR_mesh_quantization cho TOÀN BỘ GLB
# trong assets/ (GLB-QUANTIZE-1, 11/11/2026 — quy trình đo ở research/26).
#
# LUẬT PIPELINE (bắt buộc từ 11/11/2026):
#   MỖI lần build lại GLB từ Blender (build_models.py / build_one_glb.py)
#   phải chạy script này TRƯỚC khi đóng gói standalone / ship.
#   GLB gốc từ Blender là nguồn sự thật; file quantized chỉ là sản phẩm
#   đóng gói. Rollback = chép <ten>.glb.bak-quantize-<ngày> đè lại.
#
# CẤM (đã đo/chốt ở research/26):
#   - KHÔNG strip TEXCOORD_0: web gắn map canvas (TEX_GRIME...) lúc chạy,
#     xoá UV = vỡ texture. Quantize giữ UV ở 12-bit.
#   - KHÔNG meshopt/Draco: tránh thêm decoder; three r160 đọc
#     KHR_mesh_quantization NATIVE, 0 dòng code.
#   - KHÔNG weld/simplify: weld vô ích trên file của dự án (đã đo),
#     simplify không cần (số tam giác đã thấp).
#
# Cách dùng:
#   bash scripts/quantize_glbs.sh            # quantize + thay assets (có backup)
#   DRY_RUN=1 bash scripts/quantize_glbs.sh  # chỉ in bảng trước/sau, không thay
#   ASSETS_DIR=<thư mục> bash scripts/quantize_glbs.sh
# Yêu cầu: gltf-transform CLI 4.x. Mặc định tìm ở /tmp/diag/node_modules/.bin;
#   thiếu thì cài:  (cd /tmp/diag && npm i @gltf-transform/cli)
#   hoặc trỏ GT=/đường/dẫn/gltf-transform.
# An toàn từng file: quantize ra file tạm -> `validate` đạt -> MỚI thay
#   (kèm backup .bak-quantize-<YYYYMMDD>). File nào lỗi thì GIỮ bản gốc.
# =====================================================================
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
ASSETS_DIR="${ASSETS_DIR:-$HERE/../assets}"
GT="${GT:-/tmp/diag/node_modules/.bin/gltf-transform}"
DRY_RUN="${DRY_RUN:-0}"
STAMP="$(date +%Y%m%d)"

if [ ! -x "$GT" ]; then
  echo "THIẾU gltf-transform CLI tại: $GT"
  echo "Cài: (cd /tmp/diag && npm i @gltf-transform/cli)  hoặc đặt biến GT=<path>"
  exit 1
fi

total_before=0; total_after=0; ok=0; fail=0
printf '%-18s %10s %10s %8s  %s\n' "file" "truoc" "sau" "delta%" "trang thai"
for f in "$ASSETS_DIR"/*.glb; do
  case "$f" in *.bak-*) continue;; esac
  name="$(basename "$f")"
  before=$(stat -c%s "$f")
  tmp="$f.qtmp.glb"
  if ! "$GT" quantize "$f" "$tmp" >/dev/null 2>&1; then
    echo "$name: QUANTIZE LOI — giu ban goc"; fail=$((fail+1)); rm -f "$tmp"; continue
  fi
  if ! "$GT" validate "$tmp" >/dev/null 2>&1; then
    echo "$name: VALIDATE LOI — giu ban goc"; fail=$((fail+1)); rm -f "$tmp"; continue
  fi
  after=$(stat -c%s "$tmp")
  pct=$(awk -v a="$after" -v b="$before" 'BEGIN{printf "%.1f", 100*(a-b)/b}')
  if [ "$DRY_RUN" = "1" ]; then
    printf '%-18s %10d %10d %7s%%  %s\n' "$name" "$before" "$after" "$pct" "DRY-RUN"
    rm -f "$tmp"
  else
    cp "$f" "$f.bak-quantize-$STAMP"
    mv "$tmp" "$f"
    printf '%-18s %10d %10d %7s%%  %s\n' "$name" "$before" "$after" "$pct" "DA THAY (+backup)"
  fi
  total_before=$((total_before+before)); total_after=$((total_after+after)); ok=$((ok+1))
done
tpct=$(awk -v a="$total_after" -v b="$total_before" 'BEGIN{if(b>0) printf "%.1f", 100*(a-b)/b; else printf "0"}')
printf '%-18s %10d %10d %7s%%  ok=%d fail=%d\n' "TONG" "$total_before" "$total_after" "$tpct" "$ok" "$fail"
echo "Xong. Nho: dong goi lai standalone (python3 scripts/package_standalone.py) va chay du 8 cong truoc khi ship."
