---
layout: default
title: 使用方法：03_degradation_model 
---

# 📉 使用方法：03_degradation_model  
**How to Use: 03_degradation_model – Reliability Modeling of BTI / TDDB**

本フォルダでは、`MOSトランジスタ` の信頼性劣化（`BTI` / `TDDB`）に関するモデルを `Python` で数式化・可視化します。  
電圧・温度・動作時間などを変数とした簡易的な寿命予測モデルの構築に利用できます。  
This folder provides Python-based visualization of transistor reliability models, including BTI (Bias Temperature Instability) and TDDB (Time-Dependent Dielectric Breakdown), using voltage, temperature, and time as key variables.

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨設定 / Recommended |
|-------------|------------------------|
| Python バージョン | 3.9+ |
| 使用ライブラリ | `numpy`, `matplotlib` |

🔽 インストール例 / Installation:

```bash
pip install numpy matplotlib
```

---

## 📁 構成ファイル一覧 / File Structure

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`bti_model.py`](bti_model.py) | `NBTI`（負バイアス温度不安定性）モデルの定式化とグラフ描画<br>BTI model for ΔVth shift vs time |
| [`tddb_model.py`](tddb_model.py) | `TDDB`（絶縁破壊）寿命推定モデルの描画スクリプト<br>TDDB lifetime prediction script |
| [`common_plot.py`](common_plot.py) | 軸設定・スタイルなど共通関数<br>Common plotting utilities |
| [`figures/`](figures/) | 出力グラフ保存先（自動生成）<br>Auto-generated output directory for plots |

---

## 🚀 実行方法 / How to Run

### 1️⃣ BTI モデルの実行 / Run BTI Model

```bash
python3 bti_model.py
```

- 温度、電圧、動作時間を変数に、しきい値電圧変化 `ΔVth(t)` を可視化  
- 結果は [`figures/bti_vth_shift.png`](figures/bti_vth_shift.png) に出力

---

### 2️⃣ TDDB モデルの実行 / Run TDDB Model

```bash
python3 tddb_model.py
```

- 酸化膜厚や印加電界に基づき、寿命予測カーブを描画  
- 結果は [`figures/tddb_lifetime_plot.png`](figures/tddb_lifetime_plot.png) に保存

---

## 📈 出力例 / Output Examples

```text
figures/
├── bti_vth_shift.png
├── tddb_lifetime_plot.png
```

🖼️ 画像形式は `matplotlib.pyplot.savefig()` により PNG / PDF などで保存可能です。  
Plots can be saved in PNG/PDF formats using `savefig()`.

---

## 🔗 関連ツール / Related Tools

| フォルダ / Folder | 機能 / Description |
|------------------|---------------------|
| [`../02_plot_vgid/`](../02_plot_vgid/) | 初期特性（Vthなど）との比較可視化<br>Compare degraded Vth with initial Vg–Id curves |
| [`../05_report_template/`](../05_report_template/) | グラフのレポート自動挿入に対応<br>Auto-insertion of plots into reports |

---

## 📝 備考 / Notes

- 本モデルは教育用の簡易式（例：ΔVth ∝ tⁿ）に基づいています  
  These models are simplified (e.g., ΔVth ∝ tⁿ) for educational use  
- 実際の信頼性評価では JEITA / JEDEC など標準に基づいた試験・データ解析が必要です  
  Real evaluations require compliance with JEITA/JEDEC standards and measured data  
- 出力形式・軸設定・スタイルはスクリプト内で変更可能です  
  Output formats and plot styles can be customized in the scripts

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
