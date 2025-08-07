# 📊 04_openlane_log_parser：OpenLaneログの自動解析と可視化

本フォルダでは、OpenLane フローから生成されるレポートファイル（delay、面積、消費電力など）を対象に、**Pythonで自動的に情報を抽出・CSV化・グラフ化するツール群**を提供します。

OpenLane による SoC 設計演習と連携し、設計品質の可視化・比較を効率化します。

---

## 📄 内容と目的

| 項目 | 内容 |
|------|------|
| 対象ツール | OpenLane（Yosys + OpenROAD ベース） |
| 入力形式 | `openlane/<design>/reports/` 以下の `.rpt`, `.log`, `.txt` |
| 出力形式 | CSVファイル（delay/power/area）、折れ線グラフ（複数Run比較） |
| 活用例 | コンストレイント別の遅延変化、クロック別の電力比較、最小面積設計の傾向把握など |

---

## 🧰 使用スクリプト例（予定）

```bash
python3 parse_delay_report.py    # 最終遅延 (setup/slack) の抽出
python3 parse_power_report.py    # dynamic/leakage power の集計
python3 plot_area_vs_run.py      # 面積 vs 実行バージョンのグラフ化
```

🔧 依存パッケージ
```
Python 3.9+
pandas
matplotlib
```

インストール：
```
pip install pandas matplotlib
```
📁 出力フォーマット（例）
```
results_delay.csv
```
```
┌────────┬────────┬────────┐
│ Run ID │ Delay  │ Slack  │
├────────┼────────┼────────┤
│ run1   │ 1.23ns │ 0.10ns │
│ run2   │ 1.05ns │ 0.20ns │
└────────┴────────┴────────┘
```

## 📌 教育的意義
	•	設計制約（clock period等）と物理成果物（delay, area）の関係を可視化
	•	複数Runの結果を比較し、EDAフローの感度を把握
	•	自動レポート化による設計実験の省力化

---

## 🔗 関連リンク
	•	../03_degradation_model/：信頼性モデルとの併用による製品寿命評価
	•	../../e_chapter3_openlane_practice/：OpenLaneによる物理設計実習教材

---

[🐍 実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
