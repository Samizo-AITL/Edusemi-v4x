# 04_openlane_log_parser：OpenLane設計結果の定量分析

このフォルダでは、OpenLaneフローから出力された各ステージのログ・JSONファイルを解析し、  
遅延・面積・電力などの情報を抽出して一覧化・可視化します。

## 📌 主な機能

- `results.json` や `reports/` 以下からの自動抽出
- 面積・タイミング・セル数・消費電力などの可視化
- モジュール間比較、コーナー別結果の集計

## 🐍 使用予定ライブラリ

- `json`, `os`, `glob`
- `pandas`, `matplotlib`
