---
layout: default
title: 04_bti_tddb_estimation - 劣化モデルの可視化
---

# 🧪 04_bti_tddb_estimation：BTI・TDDB 劣化モデルの可視化  
**Degradation Model Visualization for BTI and TDDB**

---

## 📄 概要｜Overview

本ディレクトリでは、MOSトランジスタの代表的な信頼性課題である  
**BTI（Bias Temperature Instability）** および **TDDB（Time-Dependent Dielectric Breakdown）** に対する  
**寿命モデルの数式とグラフをPythonで可視化**します。

This directory visualizes **mathematical degradation models** for MOSFET reliability issues,  
specifically **BTI** and **TDDB**, using Python plotting tools.

---

## 🎯 学習目的｜Learning Objectives

| 目的｜Goals |
|-----------|
| 📉 劣化現象の数式化による理解  
| 🔥 時間・温度・電界と寿命の関係を定量化  
| 🔍 SPICEでは扱いにくい**時間軸の劣化挙動**の可視化  

---

## 🧾 スクリプト構成｜Script Structure

| ファイル名｜File | 内容｜Description |
|------------------|-------------------------------------------|
| `plot_bti_model.py` | ΔVthの時間変化と温度依存をプロット |
| `plot_tddb_model.py` | MTTFと電界強度の関係を可視化 |
| `model_constants.py` | 各モデルで用いる定数群（Ea, γ, n など）を一元管理 |
| `output/` | グラフ画像（`.png`）の保存フォルダ |

---

## 📈 出力例｜Example Outputs

### 🔹 BTI劣化モデル（ΔVth vs 時間）

```bash
python3 plot_bti_model.py
```

- 時間（log軸）とΔVthの関係を温度別にプロット  
- 出力画像：`output/bti_degradation.png`

---

### 🔹 TDDBモデル（MTTF vs 電界）

```bash
python3 plot_tddb_model.py
```

- 酸化膜電界 E による寿命変化をモデル比較  
- 出力画像：`output/tddb_models.png`

---

## 📚 理論式と物理モデル｜Model Equations

### ⚡ BTIモデル式｜BTI Model Equation

```text
ΔVth(t) = A × tⁿ × exp(-Ea / kT)
```

| 項目｜Parameter | 内容｜Description |
|-------|--------------------------|
| A     | スケーリング定数 | Scaling factor |
| n     | 時間依存係数（0.1〜0.3）| Time exponent |
| Ea    | 活性化エネルギー [eV] | Activation energy |
| k     | ボルツマン定数（8.617e-5 eV/K）| Boltzmann constant |
| T     | 絶対温度 [K] | Absolute temperature |

---

### ⚡ TDDBモデル式｜TDDB Model Equations

```text
MTTF ∝ exp(γ × E)        # 指数モデル（Eモデル）  
MTTF ∝ 1 / Eⁿ             # パワーモデル
```

| 項目｜Parameter | 内容｜Description |
|-------|------------------------------|
| E     | 酸化膜電界（V/nm or MV/cm） | Electric field across oxide |
| γ     | 感度係数（材料依存） | Field acceleration factor |
| n     | パワーモデル指数（2〜4） | Power model exponent |

---

## 💡 教育的意義｜Educational Value

- 📊 **数式・グラフ・設計インパクト** を同時に理解  
- 🔄 **時間・温度・電界における信頼性設計マージン**の考察  
- ⚙️ 実デバイス設計での **寿命予測と評価指標化** の基盤形成  

---

## 🔧 実行環境｜Requirements

| 項目｜Item | 内容｜Details |
|--------|---------------------|
| 🐍 Python | Version 3.x 推奨 |
| 📦 必須パッケージ | `numpy`, `matplotlib` |

### 📦 インストールコマンド｜Install Command

```bash
pip install numpy matplotlib
```

---

## 🔗 関連リンク｜Related Chapters

| 項目｜Item | リンク｜Link |
|--------|-----------------------------------------------|
| ⚗️ 実践編 第2章｜Sky130実験とSPICE特性評価 | [../README.md](../README.md) |
| 🧰 実践編 第1章｜Python自動化ツール群 | [../../e_chapter1_python_automation_tools/README.md](../../e_chapter1_python_automation_tools/README.md) |
| 🏗️ 実践編 第3章｜OpenLaneによるデジタル設計 | [../../e_chapter3_openlane_practice/README.md](../../e_chapter3_openlane_practice/README.md) |

---

## 🔙 戻る｜Back to Chapter Top

[🏠 実践編 第2章 トップへ戻る｜Back to `e_chapter2_sky130_experiments`](../README.md)
