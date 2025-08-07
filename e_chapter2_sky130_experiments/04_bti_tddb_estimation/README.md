---
layout: default
title: 04_bti_tddb_estimation - 劣化モデルと数式可視化
---

# 🧪 04_bti_tddb_estimation - 劣化モデルと数式可視化  
**BTI & TDDB Degradation Modeling and Visualization**

---

## 📄 概要｜Overview

MOSFETの信頼性課題である **BTI（Bias Temperature Instability）** および  
**TDDB（Time-Dependent Dielectric Breakdown）** に関する基本モデルを Python により可視化します。

This chapter visualizes the mathematical models of **BTI** and **TDDB**,  
making it easier to intuitively understand degradation trends using plots and formulae.

---

## 🔧 スクリプト構成｜Files

| ファイル名｜Filename | 内容｜Description |
|-----------------------|----------------------------|
| `plot_bti_model.py` | ΔVth vs 時間（BTI劣化）を描画 |
| `plot_tddb_model.py` | MTTF vs 電界（TDDB寿命）を描画 |
| `model_constants.py` | モデル定数の一元管理（Ea, n など） |
| `output/` | 出力図保存先（PNG形式） |

---

## 📈 実行と出力｜Run and Output

### 🔸 BTI劣化モデル

```bash
python3 plot_bti_model.py
```

出力：`output/bti_degradation.png`

- ΔVth（しきい値シフト）の **時間・温度依存性** を log-log プロット

---

### 🔸 TDDBモデル

```bash
python3 plot_tddb_model.py
```

出力：`output/tddb_models.png`

- 電界強度と寿命（MTTF）の関係を指数モデル・パワーモデルで比較

---

## 🔢 モデル式｜Model Equations

### ⚡ BTIモデル式｜BTI Model Equation

MOSFETのBTI劣化（しきい値電圧シフト）は、以下のモデルで表されます：

$$
\Delta V_{th}(t) = A \cdot t^n \cdot \exp\left( -\frac{E_a}{kT} \right)
$$

| 項目 | Parameter | 内容 |
|------|-----------|------|
| $begin:math:text$ A $end:math:text$ | Scaling constant | スケーリング定数 |
| $begin:math:text$ n $end:math:text$ | Time exponent | 時間依存係数（0.1〜0.3） |
| $begin:math:text$ E_a $end:math:text$ | Activation energy | 活性化エネルギー [eV] |
| $begin:math:text$ k $end:math:text$ | Boltzmann constant | $begin:math:text$8.617 \\times 10^{-5}$end:math:text$ eV/K |
| $begin:math:text$ T $end:math:text$ | Absolute temperature | 絶対温度 [K] |

---

### ⚡ TDDBモデル式｜TDDB Model Equations

TDDB（酸化膜破壊寿命）は、以下の2種類のモデルで近似されます：

#### 📈 指数モデル（Exponential E Model）

$$
\mathrm{MTTF} \propto \exp(\gamma \cdot E)
$$

#### 📉 パワーモデル（Field Power Model）

$$
\mathrm{MTTF} \propto \frac{1}{E^n}
$$

| 項目 | Parameter | 内容 |
|------|-----------|------|
| $begin:math:text$ E $end:math:text$ | Electric field | 酸化膜電界（V/nm または MV/cm） |
| $begin:math:text$ \\gamma $end:math:text$ | Acceleration factor | 電界加速係数（材料・膜厚依存） |
| $begin:math:text$ n $end:math:text$ | Power exponent | パワーモデル指数（2〜4） |

---

## 💡 教育的意義｜Educational Value

- 数式・グラフ・設計インパクトを同時に理解
- 時間・温度・電界の信頼性設計マージンを体感
- パラメータ調整と劣化評価の統合的理解を促進

---

## 🔗 関連リンク｜Related Links

| セクション | リンク |
|------------|--------|
| 📘 第2章トップ | [../README.md](../README.md) |
| 🧮 第1章：Python自動化 | [../../e_chapter1_python_automation_tools/README.md](../../e_chapter1_python_automation_tools/README.md) |
| 🧾 Sky130 PDK GitHub | [https://github.com/google/skywater-pdk](https://github.com/google/skywater-pdk) |

---

## 📦 必要なPythonパッケージ｜Requirements

```bash
pip install numpy matplotlib
```

---
