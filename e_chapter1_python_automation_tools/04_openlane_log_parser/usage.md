---
layout: default
title: 使用方法：04_openlane_log_parser
---

# 📊 使用方法：04_openlane_log_parser  
**How to Use: 04_openlane_log_parser – Automated Extraction of OpenLane Reports**

本フォルダでは、`OpenLane` 実行後に出力される複数の `レポートファイル` を自動で読み取り、  
設計の **面積・遅延・電力** などを抽出・CSV化・グラフ化します。  
This folder provides a Python tool to automatically parse OpenLane-generated report files, extract key metrics (delay, area, power), and export them to CSV and plot formats.

複数バージョンや異なる合成条件の比較にも活用できます。  
Useful for comparing multiple synthesis runs or OpenLane versions.

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨環境 / Recommended |
|-------------|------------------------|
| Python | 3.9+ |
| 使用ライブラリ / Required Libraries | `pandas`, `matplotlib` |

🔽 インストール例 / Installation:

```bash
pip install pandas matplotlib
```

---

## 📁 構成ファイル一覧 / File Structure

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`parse_openlane_log.py`](parse_openlane_log.py) | OpenLaneログを読み取り、CSV＋グラフを生成<br>Main script to parse logs and generate CSV/plots |
| [`example_config.json`](example_config.json) | 対象パスやバージョン名を指定する設定ファイル<br>Config file to define paths and versions |
| `logs/` | OpenLane実行時に出力されたレポート群を格納<br>Directory for OpenLane output reports |
| `results/` | 整理されたCSVやグラフ（PNG形式）の保存先<br>Output directory for results (auto-generated) |

---

## 🚀 実行方法 / How to Run

### 1️⃣ ログフォルダの準備 / Prepare Logs

以下のような構成で `logs/` ディレクトリに OpenLane の出力ファイルを配置します：

```text
logs/
├── metrics.csv
├── reports/
│   ├── final_summary_report.rpt
│   ├── power.rpt
│   └── area.rpt
```

---

### 2️⃣ スクリプト実行 / Run Script

以下のコマンドを実行します：

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

| フォルダ / Folder | 説明 / Description |
|------------------|---------------------|
| [`../03_degradation_model/`](../03_degradation_model/) | 信頼性劣化との相関分析に応用可能<br>Useful for reliability–area trade-off analysis |
| [`../05_report_template/`](../05_report_template/) | 結果グラフのレポート自動挿入に対応<br>Supports auto-inserting graphs into reports |

---

## 📝 備考 / Notes

- OpenLaneのバージョンやPDKにより `metrics.csv` の構成が変わる場合があります。  
  The format of `metrics.csv` may differ depending on OpenLane version or PDK.

- 事前に `flow.tcl` によるOpenLane実行が完了している必要があります。  
  Please run the OpenLane flow beforehand.

- 複数Runの比較を行う場合、`example_config.json` やスクリプト内の `run_labels` を編集してください。  
  For multiple run comparisons, modify `example_config.json` accordingly.

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
