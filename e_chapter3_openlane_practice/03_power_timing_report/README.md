---
layout: default
title: 設計レポート解析：面積・タイミング・電力の可視化 
---

---

# 📊 設計レポート解析：面積・タイミング・電力の可視化  
**Analysis of Area, Timing, and Power Reports in OpenLane Flow**

---

## 📘 概要｜Overview

この章では、OpenLaneフローで生成された各種レポートを **Pythonで自動解析・CSV化・グラフ表示** する方法を紹介します。  
**面積・セル数・遅延・電力** などの設計指標を読み解き、設計改善や比較検証に役立てます。

This section demonstrates how to parse OpenLane reports using Python  
to extract key metrics like **area, timing slack, and power consumption** and visualize them.

---

## 🎯 学習目的｜Objectives

- ✅ **OpenLaneが出力するレポートログを構造的に解析できる**  
  *You can structurally analyze report logs output by OpenLane.*

- ✅ **面積・消費電力・タイミング情報をCSV化・視覚化できる**  
  *You can convert and visualize area, power, and timing information as CSV.*

- ✅ **複数Runの結果を比較・分析する基盤を習得できる**  
  *You can learn how to compare and analyze results across multiple runs.*

---

## 📁 対象レポート例｜Target Directories (Example: `run1`)

```text
designs/inverter/runs/run1/reports/
├── synthesis/
│   └── synthesis.log
├── placement/
│   └── placement.log
├── routing/
│   └── routing.log
├── power/
│   └── power_report.log
└── timing/
    └── final_summary.csv
```

---

## 🧰 Pythonスクリプト構成｜Scripts for Parsing & Visualization

| ファイル名 | 説明（Description） |
|------------|----------------------|
| [`parse_synthesis_log.py`](./parse_synthesis_log.py) | 面積・セル数などの論理合成ログを抽出 |
| [`parse_power_report.py`](./parse_power_report.py) | 電力内訳を解析（静的 / 動的 / 総電力） |
| [`parse_timing_summary.py`](./parse_timing_summary.py) | タイミングSlack情報を抽出・ヒストグラム化 |
| [`plot_metric_trend.py`](./plot_metric_trend.py) | 複数Run間の比較可視化（横棒・折れ線など） |

---

## 🚀 実行例｜Usage Example

```bash
python3 parse_power_report.py \
  --input ./designs/inverter/runs/run1/reports/power/power_report.log \
  --output ./output/power_metrics.csv
```

```bash
python3 plot_metric_trend.py \
  --input-dir ./designs/inverter/runs/
```

---

## 📈 可視化例（想定）｜Expected Graphs

- ✅ 面積 vs Run 名（横棒グラフ）
- ✅ 消費電力の内訳（Pie Chart）
- ✅ タイミングSlackの分布（ヒストグラム）
- ✅ 複数Run間での面積・遅延・電力の傾向分析

---

## 🔗 関連リンク｜Related Links

- [🧩 OpenLane Report Format Spec (公式)](https://openlane.readthedocs.io/en/latest/)
- [📘 第2節：RTLからGDSへのフロー](../02_rtl_to_gds_flow/README.md)
- [🏠 第3章トップへ戻る](../README.md)

---

## 🧠 教育的意義｜Educational Significance

| 観点 | 内容 |
|------|------|
| 📊 データ解析力 | 数値だけでなく傾向・相関として理解できる力を育む |
| 🔁 改善サイクル | 改善 → 評価 → 検証の反復で設計品質向上を体験 |
| 🐍 実務対応 | Pythonによるログ解析・データ整形を実践できる |

---

## 📦 必要パッケージ｜Required Python Packages

```bash
pip install pandas matplotlib seaborn
```

---

## 📝 備考｜Notes

- OpenLaneのバージョンによりログ構造が一部異なる可能性があります。
- スクリプトは `output/` フォルダにCSVやグラフファイルを出力します。
- スクリプトは順次 [`GitHub - Samizo-AITL`](https://github.com/Samizo-AITL) にて公開予定です。

---
