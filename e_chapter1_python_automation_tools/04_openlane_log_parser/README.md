---
layout: default
title: 使用方法：04_openlane_log_parser
---

---

# 📊 04_openlane_log_parser：OpenLaneログの自動解析と可視化  
**Automated Parsing and Visualization of OpenLane Reports**

---

本フォルダでは、OpenLane 実行後に出力されるレポート群（`.rpt`, `.csv`, `.log`）を Python スクリプトで解析し、  
**設計の遅延・面積・電力などを自動抽出し、CSV化・グラフ化** するツールを提供します。

This tool automatically extracts key metrics from OpenLane reports, organizes them into CSV files, and visualizes trends using graphs.

---

## 🔧 必要環境 / Requirements

| 項目 / Item | 推奨バージョン / Version |
|-------------|---------------------------|
| Python | 3.9+ |
| ライブラリ | `pandas`, `matplotlib` |

🔽 インストールコマンド:

```bash
pip install pandas matplotlib
```

---

## 📁 ファイル構成 / File Structure

| ファイル名 | 説明 |
|------------|------|
| [`parse_openlane_log.py`](parse_openlane_log.py) | OpenLaneログを解析し、CSVとPNGグラフを生成するメインスクリプト |
| [`example_config.json`](example_config.json) | 実行条件（バージョン名、対象パスなど）を記述する設定ファイル |
| `logs/` | OpenLane実行結果のログ・レポートファイル群（例：`metrics.csv`, `power.rpt`） |
| `results/` | 自動生成される解析結果（CSV・グラフ）出力フォルダ |

---

## 🚀 実行方法 / How to Run

### 1️⃣ ログの準備

OpenLaneのレポート群を `logs/` 以下に格納してください。構成例：

```text
logs/
├── metrics.csv
└── reports/
    ├── final_summary_report.rpt
    ├── power.rpt
    └── area.rpt
```

> ※ `metrics.csv` は OpenLane 実行後に `reports/metrics.csv` として生成されます。

---

### 2️⃣ 設定ファイルの編集（必要に応じて）

`example_config.json` には、以下のような形式で対象パスやラベルを記述します：

```json
{
  "log_dir": "logs",
  "run_labels": ["run1", "run2"],
  "output_dir": "results"
}
```

---

### 3️⃣ スクリプトの実行

```bash
python3 parse_openlane_log.py
```

📌 実行時の処理内容：

- `example_config.json` に基づいて、対象のバージョン名やパスを設定  
- `metrics.csv` や `.rpt` ファイルを解析し、指定項目を抽出  
- 抽出情報を `results/` フォルダへ CSV・グラフ形式で保存

---

## 📈 出力例 / Output Example

```text
results/
├── summary_table.csv
├── delay_comparison.png
├── area_comparison.png
└── power_comparison.png
```

🗂️ `summary_table.csv` には Run IDごとの各種指標（Delay, Area, Power）が整列されます。  
📉 各 PNG は複数Runの比較グラフとして保存され、レポートにも使用可能です。

---

## 🔗 関連ツール / Related Tools

| フォルダ | 機能 |
|---------|------|
| [`../03_degradation_model/`](../03_degradation_model/) | 信頼性モデルとの連携で劣化 vs 面積・電力を評価 |
| [`../05_report_template/`](../05_report_template/) | レポート出力にグラフを自動組み込み可能 |

---

## 📝 備考 / Notes

- OpenLaneのバージョンやPDKにより `metrics.csv` のフォーマットが異なる可能性があります。  
- 複数回のRun比較には、`run_labels` に複数のバージョン名を指定してください。  
- 出力グラフはレポートやプレゼン資料にも活用できます。

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
