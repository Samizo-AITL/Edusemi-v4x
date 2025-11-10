---
layout: default
title: 設計レポート解析：面積・タイミング・電力の可視化（OpenLane v2 完全版）
---

---

# 📊 設計レポート解析：面積・タイミング・電力の可視化（OpenLane v2 完全版）  
**Analysis of Area, Timing, and Power Reports in OpenLane v2 Flow**

---

## 📘 概要｜Overview

この章では **OpenLane v2** が生成するレポート群を  
**Python により解析・CSV化・可視化**する方法を解説します。

扱う指標は：

- ✅ **面積（Area）**
- ✅ **タイミング（WNS/TNS/遅延）**
- ✅ **電力（Power）**
- ✅ **配置・配線のQoR**

OpenLane v2 の出力構造に完全準拠した **最新版教材** です。

---

## 🎯 学習目的｜Objectives

- ✅ OpenLane v2 のレポート形式を理解する  
- ✅ Python による数値抽出 → CSV → グラフ化の流れを身に付ける  
- ✅ 複数の Run を比較・検証する仕組みを構築する  

---

# 🗂️ レポートディレクトリ構成（OpenLane v2 正式構造）

以下は **designs/inverter/runs/run1/** の出力例：

```
runs/run1/
├── logs/                   
├── reports/               
│   ├── synthesis/          ← yosys 合成ログ
│   ├── floorplan/
│   ├── placement/
│   ├── cts/
│   ├── routing/
│   ├── parasitics/         ← SPEF, R/C 抽出
│   ├── timing/             ← metrics.csv / slack rpt
│   ├── power/              ← total_power.rpt
│   └── signoff/            ← drc / lvs
└── results/
    └── final/
        └── gds/inverter.gds
```

✅ **v2 では timing, power, parasitics, signoff が独立ディレクトリに整理される。**  
✅ **“log” ではなく “rpt (report)” 形式が多い点が v1 と異なる。**

---

# 🧰 Python 解析スクリプト構成（最新版）

以下は v2 レポートを正しく解析するための公式対応ファイル例：

| スクリプト名 | 解析対象 |
|--------------|----------|
| `parse_synthesis_log.py` | `reports/synthesis/1-yosys.log` |
| `parse_power_report.py` | `reports/power/total_power.rpt` |
| `parse_timing_summary.py` | `reports/timing/metrics.csv` |
| `plot_metric_trend.py` | `runs/*/reports/` を横断解析 |

---

# ✅ 解析対象ファイル一覧（OpenLane v2）

| 項目 | ファイル例 | 内容 |
|------|------------|------|
| 合成 | `1-yosys.log` | セル数・ゲート数・面積 |
| タイミング | `metrics.csv` | WNS/TNS/遅延/ルート特性 |
| 電力 | `total_power.rpt` | static / dynamic / internal / switching |
| 配線 | `route.rpt` | ワイヤ長・ビア数 |
| 抽出 | `parasitics/*.spef` | RC情報（STAに利用） |
| サインオフ | `drc.rpt`, `lvs.rpt` | DRC/LVS結果 |

---

# 🚀 Python 解析例｜Usage Example

## ✅ 電力レポート → CSV

```bash
python3 parse_power_report.py \
  --input ./designs/inverter/runs/run1/reports/power/total_power.rpt \
  --output ./output/power_metrics.csv
```

## ✅ 複数Run比較

```bash
python3 plot_metric_trend.py \
  --input-dir ./designs/inverter/runs/
```

---

# 📈 可視化例（想定）

- ✅ Run毎の面積比較（Bar Chart）
- ✅ WNS/TNS の Slack 分布（Histogram）
- ✅ 総電力の推移（Line Chart）
- ✅ ルーティングQoR（ワイヤ長・ビア数）の比較グラフ

---

# 🧠 教育的意義｜Educational Significance

| 観点 | 内容 |
|------|------|
| 📊 データ解析 | 数値変化を俯瞰し、設計品質の変化を理解 |
| 🔁 改善サイクル | design → run → analyze → optimize の流れを体験 |
| 🐍 実務力 | Python によるレポート処理は企業でも必須スキル |

---

# 📦 必要パッケージ（軽量構成）｜Required Python Packages

```bash
pip install pandas matplotlib
```

✅ seaborn は **必須ではない**（教育・再現性の観点で非推奨）。  
必要なら optional として追加してもよい。

---

# 📝 Notes（補足）

- OpenLane のバージョンごとにレポート構造が微細に変わることがあります。  
- power/ 以下は `total_power.rpt` や `power.rpt` など名称が異なる場合があります。  
- 出力先として `output/` フォルダを作成して CSV や PNG を保存する想定です。  
- 解析スクリプトは順次 GitHub に公開予定です。

---

# 🔗 関連リンク

- [OpenLane Documentation](https://openlane.readthedocs.io/en/latest/)
- [第2節：RTL→GDSフロー](../02_rtl_to_gds_flow/README.md)
- [第3章トップ](../README.md)
