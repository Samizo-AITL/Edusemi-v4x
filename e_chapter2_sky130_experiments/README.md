---
layout: default
title: 実践編 第2章　Sky130実験とSPICE特性評価
---

# ⚗️ 実践編 第2章：Sky130実験とSPICE特性評価  
**Practical Chapter 2: Sky130 Experiments and SPICE-Based Characterization**

---

## 📘 概要｜Overview

本章では、SkyWaterのSky130 PDKを用いて、MOSトランジスタの基本特性（Vg–Idカーブ、Vth）や劣化予測（BTI・TDDB）まで含む  
**SPICEベースの設計評価実験**を構成します。  

This chapter uses the **Sky130 PDK** to evaluate MOSFET characteristics such as **Vg–Id curves**, **threshold voltage (Vth)**,  
and **reliability predictions** using BTI and TDDB models through **SPICE simulations**.

---

## 🎯 学習目的｜Learning Objectives

- ✅ Sky130 MOS モデルによる SPICE 実験  
 SPICE simulation using Sky130 device models  
- ✅ Python による自動化・可視化・寿命推定  
 Automation, visualization, and lifetime estimation via Python  
- ✅ `.meas` による定量抽出とスクリプト連携  
 Measurement extraction using `.meas` and scripting integration  

---

## 📁 章内構成｜Chapter Contents

| フォルダ名｜Folder | 内容｜Description |
|--------------------|---------------------------------------------|
| [`01_setup_sky130_model/`](01_setup_sky130_model/) | Sky130と`ngspice`のセットアップ｜Set up ngspice and Sky130 |
| [`02_idvg_experiment/`](02_idvg_experiment/) | Vg–Id特性シミュレーションとパラメトリックSweep｜Vg–Id sweeping |
| [`03_vth_extraction/`](03_vth_extraction/) | `.meas` を使った Vth 抽出｜Extracting Vth using `.meas` |
| [`04_bti_tddb_estimation/`](04_bti_tddb_estimation/) | 劣化（BTI・TDDB）による寿命予測｜Lifetime prediction using BTI/TDDB |
| [`05_data_summary/`](05_data_summary/) | 実験結果のまとめとレポート出力｜Result summary and reporting |

---

## 🔧 実行環境｜Required Environment

- ✅ Sky130 PDK（e.g., `sky130_fd_pr__nfet_01v8`）  
- ✅ `ngspice` version 35+  
- ✅ Python 3.9+  
- ✅ 必要パッケージ｜Packages: `matplotlib`, `pandas`, `numpy`, など  

---

## 🔁 実験の流れ｜Experiment Flow

1. `.spice` テンプレートと Sweep により特性取得  
2. Python でログ解析とプロット  
3. `.meas` による Vth 自動抽出  
4. 劣化モデルを組み合わせて寿命予測  

---

## 📘 関連リンク｜Related Chapters

- [実践編 第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)  
- [実践編 第3章：OpenLaneによるデジタル設計実習](../e_chapter3_openlane_practice/README.md)  

---

## 📌 教材の意義｜Educational Significance

- 📈 **特性＝現象** の実感をSPICEで得る
- 🧪 `.meas` やスクリプトによる構造化評価
- 🔄 信頼性評価・設計マージン設計との接続を体感

---

## 🧭 次に進むべき章｜Next Chapters

- ✅ **第3章：OpenLaneでの物理設計と評価**
- ✅ **応用編：高耐圧やESD設計との組合せ**

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
