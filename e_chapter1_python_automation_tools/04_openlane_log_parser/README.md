---
layout: default
title: 使用方法：04_openlane_log_parser
---

# 📊 使用方法：04_openlane_log_parser  
**How to Use: 04_openlane_log_parser – OpenLane Log Auto Parser**

このフォルダでは、OpenLane 実行後に出力される各種レポートファイルを自動解析し、  
設計の **面積・遅延・電力などを CSV化・グラフ化** するツール群を提供します。  
複数の設計バージョンや合成条件を比較・可視化することで、設計最適化・EDA教育に活用できます。

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨バージョン / Version |
|-------------|---------------------------|
| Python | 3.9+ |
| 使用ライブラリ / Libraries | `pandas`, `matplotlib` |

🔽 インストール：

```bash
pip install pandas matplotlib
```

---

## 📁 構成ファイル一覧 / File Structure

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`parse_openlane_log.py`](parse_openlane_log.py) | メインスクリプト：OpenLaneログのCSV化＋グラフ出力 |
| [`example_config.json`](example_config.json) | 対象レポートのディレクトリや比較条件を記述する設定ファイル |
| [`logs/`](logs/) | OpenLane実行後の出力ログ（`metrics.csv`, `reports/*.rpt` などを格納） |
| [`results/`](results/) | 整理されたCSVデータや出力グラフ（自動生成されます） |

---

## 🚀 実行方法 / How to Run

### 1️⃣ ログフォルダの準備 / Prepare Log Files

以下のような構成で [`logs/`](logs/) フォルダにファイルを格納します：

```text
logs/
├── run1/
│   ├── metrics.csv
│   └── reports/
│       ├── final_summary_report.rpt
│       ├── power.rpt
│       └── area.rpt
├── run2/
│   ├── metrics.csv
│   └── reports/
│       └── ...
```

> 各 `runX/` は異なる OpenLane 実行ディレクトリを想定しています。

---

### 2️⃣ スクリプト実行 / Run Parser Script

以下のように実行します：

```bash
python3 parse_openlane_log.py
```

- [`example_config.json`](example_config.json) 内のパスとラベルを修正すれば、比較対象を自由に変更できます。
- 実行後、[`results/`](results/) フォルダに解析結果が生成されます。

---

## 📈 出力例 / Output Example

```text
results/
├── summary_table.csv
├── delay_comparison.png
├── area_comparison.png
└── power_comparison.png
```

- `summary_table.csv`：各Runの遅延・面積・電力の一覧表  
- `*_comparison.png`：各指標の比較グラフ（棒グラフまたは折れ線グラフ）

---

## 🔗 関連ツール / Related Tools

| フォルダ | 機能 |
|---------|------|
| [`../03_degradation_model/`](../03_degradation_model/) | 信頼性モデルとの併用による設計評価 |
| [`../../e_chapter3_openlane_practice/`](../../e_chapter3_openlane_practice/) | OpenLaneによる物理設計教材と連携 |

---

## 🎓 教育的意義 / Educational Purpose

- 合成制約と成果物（Delay, Area, Power）の関係を視覚的に理解  
- 複数Runの比較により EDA フローの感度分析を体験  
- 自動レポート出力により設計実験の効率を大幅に向上

---

## 📝 備考 / Notes

- OpenLane のバージョン・PDK により `metrics.csv` の構成が異なる可能性があります。  
- 必ず事前に `flow.tcl` による各Runの完了を確認してください。  
- Run名や比較軸のカスタマイズは、スクリプトまたは設定ファイルを直接編集してください。

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
