---
layout: default
title: 使用方法：03_degradation_model
---

---

# 📉 使用方法：03_degradation_model  
**How to Use: 03_degradation_model – Reliability Modeling Tools**

---

このフォルダでは、MOSトランジスタにおける代表的な信頼性劣化現象である  
**BTI（Bias Temperature Instability）** や **TDDB（Time Dependent Dielectric Breakdown）** の理論モデルに基づき、  
**しきい値電圧（Vth）やリーク電流の劣化挙動を Python で計算・可視化**するツールを提供します。  
This folder provides tools to simulate and visualize reliability degradation in MOSFETs—such as Vth drift (BTI) and oxide breakdown lifetime (TDDB)—based on physics-inspired models using Python.

---

## 📄 内容と目的 / Models and Objectives

| モデル / Model | 対象現象 / Phenomenon | 特徴・数式 / Description |
|----------------|------------------------|----------------------------|
| **BTIモデル** | Vth ドリフト / Vth drift | ΔVth ∝ (t)^n × exp(-Ea/kT) |
| **TDDBモデル** | 酸化膜破壊 / Oxide Breakdown | Weibull分布・Eモデルなどによる寿命予測 / Lifetime estimation using Weibull or E-model |

---

## 🧪 使用例 / Example Usage

```bash
python3 plot_bti_model.py     # ΔVth vs 時間のプロット / Plot ΔVth over time
python3 plot_tddb_model.py    # 寿命 vs 電界強度のプロット / Plot lifetime vs electric field
```

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨バージョン / Recommended |
|-------------|-------------------------------|
| Python | 3.8+ |
| 使用ライブラリ | `numpy`, `matplotlib` |

🔽 インストール方法 / Installation:

```bash
pip install numpy matplotlib
```

---

## 📁 構成ファイル一覧 / File Structure

| スクリプト / Script | 概要 / Description |
|----------------------|---------------------|
| [`bti_model.py`](bti_model.py) | BTI（しきい値電圧の時間変化）モデルのプロット<br>Plot ΔVth over time (BTI model) |
| [`tddb_model.py`](tddb_model.py) | TDDB（絶縁破壊寿命）の分布と電界依存性を可視化<br>Visualize TDDB lifetime distribution vs field |
| [`common_plot.py`](common_plot.py) | 軸設定・描画スタイルなどの共通関数群<br>Common plotting utility functions |

---

## 🔗 関連ツール / Related Tools

| フォルダ / Folder | 機能 / Description |
|------------------|---------------------|
| [`../01_spice_runner/`](../01_spice_runner/) | 初期特性（Vthなど）の取得<br>Initial SPICE-based simulation of Vth |
| [`../02_plot_vgid/`](../02_plot_vgid/) | SPICEログからのVg–Idプロット<br>Visualization of SPICE logs |
| [`../../e_chapter2_sky130_experiments/`](../../e_chapter2_sky130_experiments/) | Sky130実験と劣化評価の応用教材<br>Sky130-based reliability experiments |

---

## 🎯 教育的意義 / Educational Purpose

- 信頼性設計の基礎モデルを **定量的に体験**  
  Quantitative exploration of core reliability models
- **Vthの劣化挙動** や **寿命分布の傾向** を視覚的に把握  
  Visual understanding of degradation and lifetime trends
- 温度 T、時間 t、電界 E などのパラメータ感度を体感  
  Sensitivity analysis with respect to key parameters
- 信頼性設計・寿命評価の導入教材として活用可能  
  Useful for training in lifetime prediction and margin design

---

## 📌 備考 / Notes

- 本スクリプト群は **教育目的の疑似モデル** に基づいています  
  These scripts are simplified models intended for educational use  
- 実製品の評価には、物理モデル・試験・実測データが必要です  
  Real product evaluation requires physical testing and advanced modeling  
- 各モデルの理論背景は、別教材にて詳述予定です  
  Theoretical details will be provided in future teaching materials

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
