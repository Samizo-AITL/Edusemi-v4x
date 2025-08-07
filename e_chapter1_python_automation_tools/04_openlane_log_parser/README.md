---
layout: default
title: 使用方法：04_openlane_log_parser
---

# 📊 使用方法：04_openlane_log_parser  
**How to Use: 04_openlane_log_parser – Auto-Parsing & Visualization of OpenLane Logs**

本フォルダでは、OpenLane フローから生成されるレポートファイル（delay、面積、消費電力など）を対象に、  
**Pythonで自動的に情報を抽出・CSV化・グラフ化するツール群**を提供します。  
This folder provides Python tools for automatically extracting, converting, and visualizing OpenLane reports such as delay, area, and power into CSVs and plots.

OpenLane による SoC 設計演習と連携し、設計品質の可視化・比較を効率化します。  
These tools support SoC design labs using OpenLane by enabling efficient quality comparison between runs.

---

## 📄 内容と目的 / Overview & Purpose

| 項目 / Item | 内容 / Description |
|-------------|---------------------|
| 対象ツール / Target | OpenLane（Yosys + OpenROAD） |
| 入力形式 / Input | `openlane/<design>/reports/` 以下の `.rpt`, `.log`, `.txt` |
| 出力形式 / Output | CSVファイル（delay/power/area）、折れ線グラフ（複数Run比較） |
| 活用例 / Use Cases | クロック別遅延変化、電力比較、最小面積Runの抽出など |

---

## 🧰 使用スクリプト例 / Example Scripts (Planned)

```bash
python3 parse_delay_report.py     # 最終遅延 (setup/slack) の抽出
python3 parse_power_report.py     # dynamic/leakage power の集計
python3 plot_area_vs_run.py       # 面積 vs Run ID の比較グラフ
```

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨設定 / Recommended |
|-------------|------------------------|
| Python | 3.9+ |
| 使用ライブラリ | `pandas`, `matplotlib` |

🔽 インストール例 / Installation:

```bash
pip install pandas matplotlib
```

---

## 📁 構成ファイル一覧 / File Structure

| スクリプト / Script | 説明 / Description |
|----------------------|---------------------|
| [`parse_delay_report.py`](parse_delay_report.py) | Slack / Delay 情報をログから抽出し CSV 出力<br>Extract setup timing from reports |
| [`parse_power_report.py`](parse_power_report.py) | 消費電力情報（動的 / リーク）を収集し CSV 出力<br>Summarize dynamic & leakage power |
| [`plot_area_vs_run.py`](plot_area_vs_run.py) | 各 Run の面積を比較しグラフ化<br>Visualize area across multiple runs |
| [`figures/`](figures/) | 出力画像保存先（自動生成）<br>Output directory for generated figures |

---

## 📂 出力CSVフォーマット例 / Output CSV Example

```text
results_delay.csv
```

```text
┌────────┬────────┬────────┐
│ Run ID │ Delay  │ Slack  │
├────────┼────────┼────────┤
│ run1   │ 1.23ns │ 0.10ns │
│ run2   │ 1.05ns │ 0.20ns │
└────────┴────────┴────────┘
```

🗂️ 他にも `results_power.csv`, `results_area.csv` などが生成されます。

---

## 🎯 教育的意義 / Educational Value

- 設計制約（例：clock period）と物理成果（delay, area, power）との相関を理解  
- 複数Run結果を視覚的に比較することでEDA感度を体感  
- 自動CSV・グラフ出力により設計実験を効率化

---

## 🔗 関連ツール / Related Tools

| フォルダ / Folder | 機能 / Description |
|------------------|---------------------|
| [`../03_degradation_model/`](../03_degradation_model/) | 劣化モデルとの連携分析<br>Combine with degradation models for lifetime estimation |
| [`../../e_chapter3_openlane_practice/`](../../e_chapter3_openlane_practice/) | OpenLaneによる物理設計実習教材<br>Hands-on layout design with OpenLane |

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
