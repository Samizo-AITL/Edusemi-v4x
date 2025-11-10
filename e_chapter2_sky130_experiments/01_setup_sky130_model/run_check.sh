#!/usr/bin/env bash
set -e

# 必要: ngspice / PDK_ROOT / PDK（volareスキーマ）
# 例:
#   export PDK_ROOT=/mnt/c/openlane/pdks
#   export PDK=sky130A

# 出力フォルダ作成
mkdir -p output

echo "[1/2] Running NFET..."
ngspice -b nfet_vgid.spice -o output/nfet_vgid.log
mv nfet_vgid.csv output/ 2>/dev/null || true
echo "  → output/nfet_vgid.csv"
echo "  → output/nfet_vgid.log"

echo "[2/2] Running PFET..."
ngspice -b pfet_vgid.spice -o output/pfet_vgid.log
mv pfet_vgid.csv output/ 2>/dev/null || true
echo "  → output/pfet_vgid.csv"
echo "  → output/pfet_vgid.log"

echo ""
echo "DONE. CSV + LOG は output/ に出力されています。"
