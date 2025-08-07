---
layout: default
title: 04_bti_tddb_estimation - 劣化モデルと数式可視化
---

# 🧪 04_bti_tddb_estimation - 劣化モデルと数式可視化  
**BTI & TDDB Degradation Modeling and Visualization**

---

## 📄 概要｜Overview

本章では、MOSトランジスタの信頼性課題である **BTI（Bias Temperature Instability）** および  
**TDDB（Time-Dependent Dielectric Breakdown）** に関する基本モデルを Python により数式・グラフで可視化します。

This chapter visualizes key models of MOSFET reliability degradation—**BTI** and **TDDB**—using Python.  
The goal is to intuitively understand their mathematical behavior through plots and formulae.

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

### 🔸 BTI劣化モデルの実行

```bash
python3 plot_bti_model.py
```

- ΔVth（しきい値シフト）の **時間・温度依存性** を log-log プロット  
- 結果：`output/bti_degradation.png`

### 🔸 TDDBモデルの実行

```bash
python3 plot_tddb_model.py
```

- 電界強度と寿命（MTTF）の関係を2モデルで比較  
- 結果：`output/tddb_models.png`

---

## 🔢 モデル式｜Model Equations

### ⚡ BTIモデル式｜BTI Model Equation

MOSFETのBTI劣化（しきい値電圧シフト）は、以下の時間・温度依存モデルで表されます：

<div align="center">
<span>$$
\Delta V_{th}(t) = A \cdot t^n \cdot \exp\left(-\frac{E_a}{kT}\right)
$$</span>
</div>

| 項目｜Parameter | 内容｜Description |
|----------------|------------------------|
| <span>$begin:math:text$ A $end:math:text$</span> | スケーリング定数 |
| <span>$begin:math:text$ n $end:math:text$</span> | 時間依存係数（0.1〜0.3） |
| <span>$begin:math:text$ E_{\\mathrm{a}} $end:math:text$</span> | 活性化エネルギー [eV] |
| <span>$begin:math:text$ k $end:math:text$</span> | ボルツマン定数（<span>$begin:math:text$8.617 \\times 10^{-5}$end:math:text$</span> eV/K） |
| <span>$begin:math:text$ T $end:math:text$</span> | 絶対温度 [K] |

---

### ⚡ TDDBモデル式｜TDDB Model Equations

TDDB（酸化膜破壊寿命）は、次の2種類のモデルで近似されます：

#### 📈 指数モデル（Eモデル）｜Exponential (E) Model

<div align="center">
<span>$$
\mathrm{MTTF} \propto \exp(\gamma \cdot E)
$$</span>
</div>

#### 📉 パワーモデル（フィールド指数モデル）｜Field Power Model

<div align="center">
<span>$$
\mathrm{MTTF} \propto \frac{1}{E^n}
$$</span>
</div>

| 項目｜Parameter | 内容｜Description |
|----------------|----------------------------|
| <span>$begin:math:text$ E $end:math:text$</span> | 酸化膜電界（V/nm または MV/cm） |
| <span>$begin:math:text$ \\gamma $end:math:text$</span> | 電界加速係数（材料・膜厚依存） |
| <span>$begin:math:text$ n $end:math:text$</span> | パワーモデル指数（2〜4） |

---

## 💡 教育的意義｜Educational Value

- 数式・グラフ・設計インパクトを同時に理解  
- 時間・温度・電界における **信頼性設計マージンの考察**  
- 実測との整合性やパラメータ調整の教育的体験

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
