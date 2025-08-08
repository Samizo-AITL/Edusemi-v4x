---
layout: default
title: 05_data_summary - 実験データの要約と可視化
---

# 📊 05_data_summary - 実験データの要約と可視化  
**Summarizing and Visualizing Sky130 Experiment Data**

---

## 📄 概要｜Overview

本フォルダでは、第2章までの Sky130 実験（Vg–Id, Vth, 劣化モデル等）で得られた  
ログデータ・測定結果を **集計・グラフ化・設計観点で可視化** します。  
Pythonを用いてCSV集計や自動グラフ化を行い、設計上のばらつき傾向や制約を把握する教材です。

This folder summarizes and visualizes the Sky130 experimental results  
including Vg–Id, Vth, and reliability modeling. Python scripts are used  
to automate data aggregation and plotting for design-oriented analysis.

---

## 📁 フォルダ構成｜Folder Structure

| ファイル名 / Folder | 内容｜Description |
|---------------------|---------------------------------------------|
| [`summary_vth.py`](./summary_vth.py) | 抽出VthデータをW/Lごとに集計・プロット |
| [`summary_bti_tddb.py`](./summary_bti_tddb.py) | 劣化モデル出力（ΔVth, MTTF）を並列可視化 |
| [`output/`](./output/) | 集計結果のCSVやプロット画像を保存 |

---

## 🔧 実行環境｜Requirements

| 項目｜Item | 内容｜Details |
|------------|------------------------|
| 🐍 **Pythonバージョン**<br>Python Version | Python 3.x |
| 📦 **必要ライブラリ**<br>Required Libraries | `matplotlib`, `pandas`, `numpy` |

**インストール例｜Example Installation:**

```bash
pip install matplotlib pandas numpy
```

---

## 🚀 実行方法｜How to Run

### ✅ Vth 結果の集計（summary_vth.py）

```bash
python3 summary_vth.py
```

- 入力：`../03_vth_extraction/output/*.dat`
- 出力：Vth–W/Lプロット（PNG）、CSV

---

### ✅ 劣化モデルの集計（summary_bti_tddb.py）

```bash
python3 summary_bti_tddb.py
```

- 入力：`../04_bti_tddb_estimation/output/*.csv`
- 出力：ΔVth vs 時間、MTTF vs 電界などの比較図

---

## 📈 出力例｜Example Outputs

- Vth vs W/L 比のプロット
- ΔVth の温度依存比較（BTI）
- MTTF の電界強度依存比較（TDDB）

---

## 🧠 教育的意義｜Educational Value

- 各特性が **構造パラメータ・時間・温度・電界**によりどう変化するかを視覚的に理解
- 実験結果とモデルの整合性を確認することで **設計マージンやプロセス最適化**の考察が可能
- データ集計と可視化を通じて、**設計指標としての意味づけ**を学習

---

## 🔗 関連リンク｜Related Links

| 項目｜Item | リンク｜Link |
|--------|-------------------------|
| 📘 Vth抽出 | [../03_vth_extraction/README.md](../03_vth_extraction/README.md) |
| 📘 劣化モデル評価 | [../04_bti_tddb_estimation/README.md](../04_bti_tddb_estimation/README.md) |
| 🗂️ 第2章全体構成 | [../README.md](../README.md) |

---

## 🔍 視覚構成（Mermaid図）

```
graph TD
  A[Vth抽出結果<br>03_vth_extraction] --> B[📊 データ集計<br>summary_vth.py]
  C[BTI/TDDBモデル<br>04_bti_tddb_estimation] --> D[📉 劣化可視化<br>summary_bti_tddb.py]
  B --> E[設計指標グラフ]
  D --> E
  style B fill:#e1f5fe,stroke:#0288d1
  style D fill:#fce4ec,stroke:#c2185b
  style E fill:#ede7f6,stroke:#4527a0,stroke-width:2px
```

---

## 🔙 戻る｜Back to Chapter Top

[🏠 実践編 第2章 トップへ戻る](../README.md)
