---
layout: default
title: 04_bti_tddb_estimation - 劣化モデルの数式可視化
---

# 🧪 04_bti_tddb_estimation  
**BTI・TDDB 劣化モデルの数式可視化**  
*BTI / TDDB Degradation Models with Equation Visualization*

---

## 🎯 概要｜Overview

MOSトランジスタの信頼性課題である **BTI（Bias Temperature Instability）** と  
**TDDB（Time-Dependent Dielectric Breakdown）** に関する数学モデルを Python により可視化します。

This chapter provides model-based visualization of transistor degradation mechanisms,  
such as BTI and TDDB, using Python plots.

---

## 📁 スクリプト構成｜Script Structure

| ファイル名 | 説明｜Description |
|------------|------------------|
| [`plot_bti_model.py`](./plot_bti_model.py) | BTIモデルの ΔVth vs 時間・温度グラフ |
| [`plot_tddb_model.py`](./plot_tddb_model.py) | TDDB寿命モデル（指数/パワー）グラフ |
| [`model_constants.py`](./model_constants.py) | モデル定数定義（Ea, k, 温度 など） |
| [`output/`](./output/) | 出力グラフ（PNG）保存先 |

---

## ⚡ BTIモデル式｜BTI Model Equation

BTI（しきい値電圧シフト）は、以下の時間・温度依存モデルで表されます：

$$
\Delta V_{th}(t) = A \cdot t^n \cdot \exp\left( -\frac{E_a}{kT} \right)
$$

### 🔹 パラメータ定義｜Parameter Definitions

| Symbol | 日本語名称 | English Name | 単位 |
|--------|------------|---------------|------|
| A      | スケーリング定数 | Scaling Constant | - |
| n      | 時間依存係数 | Time Exponent | - |
| E_a    | 活性化エネルギー | Activation Energy | eV |
| k      | ボルツマン定数 | Boltzmann Constant | eV/K |
| T      | 絶対温度 | Absolute Temperature | K |

---

## ⚡ TDDBモデル式｜TDDB Model Equations

TDDB（酸化膜破壊寿命）は、次の2種類のモデルで近似されます：

### 📈 指数モデル｜Exponential (E) Model

$$
\mathrm{MTTF} \propto \exp(\gamma \cdot E)
$$

### 📉 パワーモデル｜Field Power Model

$$
\mathrm{MTTF} \propto \frac{1}{E^n}
$$

### 🔹 パラメータ定義｜Parameter Definitions

| Symbol | 日本語名称 | English Name | 単位 |
|--------|------------|---------------|------|
| E      | 酸化膜電界 | Electric Field | V/nm または MV/cm |
| γ      | 電界加速係数 | Acceleration Coefficient | - |
| n      | パワーモデル指数 | Power Model Exponent | - |

---

## 📈 出力グラフ例｜Example Plots

### BTI劣化（ΔVth vs 時間）

```bash
python3 plot_bti_model.py
```

出力例：
- ΔVthの時間依存（log-logプロット）
- 複数温度（T）で系列表示

---

### TDDBモデル（MTTF vs 電界強度）

```bash
python3 plot_tddb_model.py
```

出力例：
- MTTFの電界依存性（logスケール）
- 指数モデル vs パワーモデルの比較

---

## 💡 教育的意義｜Educational Value

- **数式・グラフ・設計インパクト** を同時に体験できる
- **時間・温度・電界**による寿命設計の視覚的理解
- モデル定数の感度分析や信頼性マージン設計への応用

---

## 🔗 関連リンク｜Related Links

| 内容 | リンク |
|------|--------|
| 第2章トップに戻る | [../README.md](../README.md) |
| 02：Vg–Id特性抽出 | [../02_idvg_experiment/](../02_idvg_experiment/) |
| 03：Vth抽出（.meas自動化） | [../03_vth_extraction/](../03_vth_extraction/) |
| 📘 Sky130 GitHub | [https://github.com/google/skywater-pdk](https://github.com/google/skywater-pdk) |

---
