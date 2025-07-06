# 🛠️ 実践編 第1章：Pythonによる自動化ツール群

本章では、Sky130 PDK や OpenLane フローと連携しながら、**半導体設計・評価をPythonで自動化するための実践スクリプト群**を提供します。

---

## 🎯 目的

- SPICEシミュレーションの自動実行と可視化
- 信頼性モデル（BTI・TDDB）の数値評価とグラフ化
- OpenLaneレポートの解析・自動レポート出力
- Pythonによる設計実験・解析の一貫体験

---

## 📂 フォルダ構成一覧

| フォルダ名 | 内容 |
|-----------|------|
| [`01_spice_runner/`](01_spice_runner/README.md) | `ngspice` を `Python` から自動実行し、パラメータスイープ・`Vth` 変化などを制御 |
| [`02_plot_vgid/`](02_plot_vgid/README.md) | `Vg–Id` 特性など `SPICE` 出力ログの読み取りと可視化（`matplotlib`） |
| [`03_degradation_model/`](03_degradation_model/README.md) | `BTI`・`TDDB` など信頼性モデルの数式計算とグラフ化 |
| [`04_openlane_log_parser/`](04_openlane_log_parser/README.md) | `OpenLane` フローの結果（遅延・面積・電力）を抽出し `CSV` 化・可視化 |
| [`05_report_template/`](05_report_template/README.md) | 自動レポート出力用テンプレート（`Jupyter Notebook` / `Markdown`）

---

## 🧰 利用技術と前提環境

- Python 3.8 以上
- `matplotlib`, `pandas`, `numpy`, `jupyter` など
- `ngspice`, `Sky130 PDK`, `OpenLane`（各種セットアップ済みを想定）

---

## 📘 関連章リンク

- [実践編 第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)
- [実践編 第3章：OpenLaneによるデジタル設計実習](../e_chapter3_openlane_practice/README.md)

---

## 📌 教材の意義

- 教育現場でも再現可能な「自動化された実験環境」
- GUIに頼らず、**論理と構造で半導体設計を理解する訓練**
- 実務で使えるスクリプト技術 × 実験設計思考の融合

---

## 📦 今後の拡張

- `.meas` による自動Vth抽出 → 劣化予測との接続
- OpenLaneで得たセルデータを信頼性評価に連動
- GitHub ActionsやCI/CDとの自動連携
