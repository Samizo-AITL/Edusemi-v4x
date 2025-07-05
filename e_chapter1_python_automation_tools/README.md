# 🛠 第1章：Pythonによる自動化ツール群

本章では、半導体設計実務や教育演習において有効な **Pythonによる自動化スクリプト群**を紹介します。  
SPICEシミュレーション制御、特性データの可視化、OpenLaneによる論理合成結果の解析など、再利用性の高いツールとして整理します。

---

## 🎯 章の目的

- SPICE実験の自動化と可視化
- OpenLaneの設計結果の定量的評価
- 劣化モデルや寿命予測の数値解析
- MarkdownやZenn向けの図表出力支援

---

## 📁 フォルダ構成一覧（第1章：Pythonによる自動化ツール群）

| フォルダ名 | 内容 |
|-----------|------|
| [`01_spice_runner/`](01_spice_runner/) | `ngspice` を `Python` から自動実行し、パラメータスイープ・`Vth` 変化などを制御 |
| [`02_plot_vgid/`](02_plot_vgid/) | `Vg–Id` 特性など `SPICE` 出力ログの読み取りと可視化（`matplotlib`） |
| [`03_degradation_model/`](03_degradation_model/) | `BTI`・`TDDB` など信頼性モデルの数式計算とグラフ化 |
| [`04_openlane_log_parser/`](04_openlane_log_parser/) | `OpenLane` フローの結果（遅延・面積・電力）を抽出し `CSV` 化・可視化 |
| [`05_report_template/`](05_report_template/) | 自動レポート出力用テンプレート（`Jupyter` / `Markdown` 対応） |

---

## 🐍 使用技術

- Python 3.x
- numpy / pandas / matplotlib
- subprocess / pathlib / glob
- ngspice / OpenLane（外部ツールと連携）

---

## 💡 活用例

- Sky130ベースのMOS特性の比較プロット
- Ring Oscillatorの周波数変化の自動解析
- OpenLaneで設計した複数モジュールの性能一覧作成
- 教育演習結果の自動レポート生成（Zenn向け）

---

## 📘 対応章との連携

本章で開発したPythonツールは、以下の章と連携して使用されます：

- [02_plot_vgid/](02_plot_vgid/README.md)：`Vg–Id` 特性の可視化（`matplotlib`）
- [03_degradation_model/](03_degradation_model/README.md)：BTI・TDDBなどの信頼性劣化モデル評価
- [応用編 第6章：PDKとEDA環境構築](../d_chapter6_pdk_and_eda_environment/)

---

## 📬 連絡先

技術監修・執筆：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
お問い合わせは Issue または Discussions にて  
Email: shin3t72@gmail.com

---
