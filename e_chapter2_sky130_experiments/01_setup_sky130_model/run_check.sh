#!/bin/bash

# run_check.sh - Sky130 SPICE 初期動作確認スクリプト
# 教材用：ngspice による nfet/pfet の Vg–Id 特性確認

# 出力ディレクトリ準備
mkdir -p output

echo "=== ngspice 実行: nfet_vgid.spice ==="
ngspice -b -o output/nfet_vgid.log nfet_vgid.spice

echo "=== ngspice 実行: pfet_vgid.spice ==="
ngspice -b -o output/pfet_vgid.log pfet_vgid.spice

echo "=== 実行完了 ==="
echo "ログ出力: output/nfet_vgid.log, output/pfet_vgid.log"
