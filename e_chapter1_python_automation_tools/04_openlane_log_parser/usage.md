# 使用方法：04_openlane_log_parser

本フォルダでは、`OpenLane` 実行後に出力される複数の `レポートファイル` を自動で読み取り、  
設計の面積・遅延・電力などを抽出・CSV化・グラフ化します。  
複数バージョンや異なる合成条件の比較にも活用できます。

---

## 🔧 前提環境

- `Python 3.9+`
- `pandas`
- `matplotlib`

インストール例：

`pip install pandas matplotlib`

---

## 📁 構成ファイル一覧

| ファイル名 | 説明 |
|------------|------|
| `parse_openlane_log.py` | OpenLane出力ログを読み取り、CSVとグラフに出力 |
| `example_config.json` | 対象パスや条件設定を記述するJSONファイル |
| `logs/` | OpenLane実行時に出力された `metrics.csv` やレポート群 |
| `results/` | 整理された `CSV` と `PNG` グラフが保存されるフォルダ（自動生成） |

---

## 🚀 実行方法

### 1. ログフォルダの準備

`logs/` フォルダに以下のようなファイルが含まれていることを確認：

```text
logs/
├── metrics.csv
├── reports/
│   ├── final_summary_report.rpt
│   ├── power.rpt
│   └── area.rpt
```

## 2. スクリプトの実行

python3 parse_openlane_log.py
	•	必要に応じて example_config.json を修正し、対象のバージョン名やパスを設定します。
	•	抽出された情報は results/ 以下に自動出力されます。

## 📈 出力例
```
results/
├── summary_table.csv
├── delay_comparison.png
├── area_comparison.png
└── power_comparison.png
```

## 🔗 関連ツール
	•	03_degradation_model/：信頼性・面積の関係分析に活用可能
	•	05_report_template/：結果グラフのレポート自動挿入に対応

---

## 📝 備考
	•	OpenLaneのバージョンやPDKにより metrics.csv の形式が変わる場合があります。
	•	事前に openlane/flow.tcl によるフローが完了している必要があります。
	•	複数回の比較には、スクリプト冒頭の run_labels を変更してください。

---
