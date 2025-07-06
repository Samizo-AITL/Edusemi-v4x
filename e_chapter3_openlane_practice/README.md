# 🏗️ 第3章：OpenLaneによるデジタル設計実習

本章では、オープンソースEDAフロー「OpenLane」を用いて、RTL記述（Verilog）からGDS生成までの一連のデジタルLSI設計プロセスを体験します。

Sky130 PDKとの接続、実行フローの理解、制約設定、最適化パラメータの調整までを含みます。

---

## 🎯 学習目標

- Verilog RTLからGDSまでのフロー全体を理解する
- 各ステップ（合成・配置・配線・DRC等）の役割とツールを知る
- 面積・タイミング・消費電力といった設計結果を評価・解析できる
- 制約ファイル（`sdc`, `floorplan`）の基本操作を理解する

---

## 📚 フォルダ構成

| フォルダ名 | 内容 |
|-----------|------|
| [`01_intro_openlane/`](01_intro_openlane/README.md) | OpenLaneの概要、必要ツール、Sky130との関係 |
| [`02_rtl_to_gds_flow/`](02_rtl_to_gds_flow/README.md) | Verilog RTLからGDSまでの設計フロー実習 |
| [`03_power_timing_report/`](03_power_timing_report/README.md) | 面積・タイミング・電力のレポート抽出と分析 |
| [`04_custom_constraint/`](04_custom_constraint/README.md) | 制約ファイル（floorplan, clock等）のカスタマイズ |

---

## 🛠️ 使用ツール

- OpenLane 2.x 以降（推奨）
- Sky130 PDK（`sky130A`）
- Docker（またはローカルビルド環境）
- Python 3.x（補助スクリプト用）

---

## 🔗 関連章へのリンク

- [第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)
- [第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)

---

## 📦 事前準備

```bash
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
make pull-openlane
make pull-sky130-pdk
```

•	詳細は 01_intro_openlane/ を参照

---

## 📝 備考
	•	教材上は Sky130 PDK を用いた最小例で構成
	•	SoC/マクロ設計向けに拡張することも可能

---

