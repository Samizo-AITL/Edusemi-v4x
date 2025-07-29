# 🏗️ 第3章：OpenLaneによるデジタル設計実習  
**Practical Chapter 3: Digital Design Practice Using OpenLane**

---

## 📘 概要｜Overview

本章では、オープンソースEDAフロー「**OpenLane**」を用いて、RTL記述（Verilog）からGDS生成までの  
一連のデジタルLSI設計プロセスを体験します。  

This chapter provides hands-on practice of a **digital design flow** from Verilog RTL to GDS layout  
using the open-source EDA framework **OpenLane**.

Sky130 PDKとの接続、各工程の役割理解、制約設定、最適化なども含みます。  
Topics include integration with **Sky130 PDK**, constraint customization, optimization, and analysis.

---

## 🎯 学習目標｜Learning Objectives

- ✅ RTL記述からGDS出力までの設計ステップを体験  
 Understand the complete flow from RTL to GDS  
- ✅ 合成、配置、配線、DRC等の役割とツールを理解  
 Recognize each tool’s role in the digital backend process  
- ✅ 面積・タイミング・電力などの設計指標を分析  
 Analyze area, timing, and power metrics  
- ✅ `SDC`, `floorplan`などの制約記述に習熟  
 Learn how to configure basic design constraints

---

## 📚 フォルダ構成｜Folder Structure

| フォルダ名｜Folder | 内容｜Description |
|---------------------|-----------------------------------------------|
| [`01_intro_openlane/`](01_intro_openlane/README.md) | OpenLaneとSky130の概要｜Introduction to OpenLane & Sky130 |
| [`02_rtl_to_gds_flow/`](02_rtl_to_gds_flow/README.md) | VerilogからGDSまでの設計フロー｜RTL-to-GDS implementation |
| [`03_power_timing_report/`](03_power_timing_report/README.md) | レポート解析｜Power, timing, area analysis |
| [`04_custom_constraint/`](04_custom_constraint/README.md) | 制約ファイルのカスタマイズ｜Constraint customization |

---

## 🛠️ 使用ツール｜Required Tools

- 🧩 OpenLane v2.x+（推奨）  
- 🧩 Sky130 PDK (`sky130A`)  
- 🐳 Docker またはローカル開発環境  
- 🐍 Python 3.x（補助スクリプト用）

---

## 🔗 関連章｜Related Chapters

- [第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)  
- [第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)

---

## 📦 OpenLane / Sky130 の準備手順｜Setup

```bash
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
make pull-openlane
make pull-sky130-pdk
```

🔎 詳細は [`01_intro_openlane/`](01_intro_openlane/README.md) を参照。

---

## 📝 備考｜Notes

- ✅ 教材内では Sky130 PDK を使った最小構成例を採用  
- 🔁 実務応用では SoC や IP マクロ設計への拡張が可能  

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)

---
