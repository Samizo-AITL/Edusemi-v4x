# 📊 設計レポート解析：面積・タイミング・電力の可視化

この章では、OpenLaneによって生成された各種レポートをPythonで読み取り、**CSV化・グラフ化**して設計結果を解析する方法を紹介します。

---

## 🎯 目的

- OpenLaneの各ステージ出力（レポート）を構造的に読み取る
- 面積・セル数・遅延・電力などの設計指標を取得・可視化
- フロー改善やパラメータ比較の基盤となる分析力を養う

---

## 📁 対象ディレクトリ（例）

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

## 🧰 Pythonスクリプト構成（予定）

| ファイル名 | 説明 |
|------------|------|
| `parse_synthesis_log.py` | 論理合成のレポート（セル数・面積）を抽出 |
| `parse_power_report.py` | 消費電力（総電力・静的/動的）をCSV化 |
| `parse_timing_summary.py` | セットアップ・ホールドタイミングのSlack解析 |
| `plot_metric_trend.py` | 複数Run間での面積・電力・遅延推移をグラフ化 |

---

## 🧪 実行例

```bash
python3 parse_power_report.py \
  --input ./designs/inverter/runs/run1/reports/power/power_report.log \
  --output power_metrics.csv
```

```bash
python3 plot_metric_trend.py --input-dir ./designs/inverter/runs/
```

---

## 📈 可視化の例（想定）

- 面積 vs. Run（横棒グラフ）
- 消費電力内訳（Pieチャート）
- タイミングSlack分布（ヒストグラム）

---

## 🔗 参考リンク

- [OpenLane 公式レポート仕様](https://openlane.readthedocs.io/en/latest/)
- [第2章：RTLからGDSまで](../02_rtl_to_gds_flow/README.md)

---

## 🧠 教育的意義

- 数値だけでなく「設計の傾向」を視覚的に捉える力を育む
- 改善サイクル（改善→検証→比較）を実践形式で学習
- Pythonによるツール連携・ログ解析の実務的経験

---

## 📦 必要パッケージ

```bash
pip install pandas matplotlib seaborn
```

---

## 📌 備考

- ログ形式はOpenLaneのバージョンで若干異なる場合あり
- スクリプトは後続で公開・GitHubと連携予定
