---
layout: default
title: 実践編 第1章 Pythonによる自動化ツール群 
---

---

# 🛠️ 実践編 第1章：Pythonによる自動化ツール群  
**Practical Chapter 1: Python-Based Automation Tools for Semiconductor Design**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) |

---

## 📘 概要｜Overview

本章では、Sky130 PDK や OpenLane フローと連携しながら、  
**半導体設計・評価を Python で自動化する実践スクリプト群**を提供します。  

This chapter provides a suite of **Python automation scripts**  
for semiconductor design and evaluation, integrated with **Sky130 PDK** and **OpenLane**.

---

## 🎯 目的｜Objectives

- ✅ SPICEシミュレーションの自動実行と可視化  
 Automated SPICE execution and result visualization  
- ✅ 信頼性モデル（BTI・TDDB）の数値評価とグラフ化  
 BTI/TDDB reliability modeling and plotting  
- ✅ OpenLaneレポートの解析・CSV出力  
 OpenLane report parsing and CSV generation  
- ✅ Pythonによる設計実験の一貫体験  
 Fully automated design experiments via Python  

---

## 📂 フォルダ構成一覧｜Folder Structure

| フォルダ名｜Folder | 内容｜Description |
|--------------------|------------------------------|
| [`01_spice_runner/`](01_spice_runner/README.md) | `ngspice` を `Python` から制御し、パラメータスイープや `Vth` 変化を評価<br>Run `ngspice` from Python and sweep device parameters |
| [`02_plot_vgid/`](02_plot_vgid/README.md) | SPICE出力ログの読み取りと `Vg–Id` 可視化（`matplotlib`）<br>Parse simulation logs and plot transistor curves |
| [`03_degradation_model/`](03_degradation_model/README.md) | `BTI`・`TDDB` モデルをPythonで数式化しグラフ化<br>Numerical modeling and visualization of degradation |
| [`04_openlane_log_parser/`](04_openlane_log_parser/README.md) | `OpenLane` のログを解析し、遅延・電力・面積を抽出<br>Extract key metrics from OpenLane log files |
| [`05_report_template/`](05_report_template/README.md) | 自動レポート出力のテンプレート（Notebook/Markdown）<br>Template for automated design reporting |

---

## 🧰 利用技術と前提環境｜Tools and Requirements

- **Python** 3.8 or later
- 必須ライブラリ｜Required libraries:
  - `matplotlib`, `pandas`, `numpy`, `jupyter`
- 実行環境｜Runtime tools:
  - `ngspice`, `Sky130 PDK`, `OpenLane`（セットアップ済）


---

## 🗺️ 自動化ツール群の構成図（Mermaidフローチャート＋色分け＋GitHubリンク）
 
[📎 GitHubでMermaidフローチャートを見る](https://github.com/Samizo-AITL/Edusemi-v4x/blob/main/e_chapter1_python_automation_tools/README.md)

```mermaid
graph TD
    A01[📘 01_spice_runner<br>SPICE自動実行]
    A02[📊 02_plot_vgid<br>Vg-Id特性の可視化]
    A03[📉 03_degradation_model<br>信頼性モデル（BTI / TDDB）]
    A04[📈 04_openlane_log_parser<br>OpenLaneログ解析]
    A05[📝 05_report_template<br>自動レポート生成]

    A01 --> A02
    A02 --> A05
    A03 --> A05
    A04 --> A05

    style A01 fill:#e0f7fa,stroke:#00796b,stroke-width:2px
    style A02 fill:#f1f8e9,stroke:#33691e,stroke-width:2px
    style A03 fill:#fff8e1,stroke:#f57f17,stroke-width:2px
    style A04 fill:#fce4ec,stroke:#c2185b,stroke-width:2px
    style A05 fill:#ede7f6,stroke:#4527a0,stroke-width:2px
```

---

## 📘 関連章リンク｜Related Chapters

- [実践編 第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)  
 → Sky130デバイスを対象としたSPICEシミュレーション実習  
- [実践編 第3章：OpenLaneによるデジタル設計実習](../e_chapter3_openlane_practice/README.md)  
 → OpenLaneでのP&R・STA結果の評価と接続  

---

## 📌 教材の意義｜Educational Significance

- 🎓 GUIに頼らず **構造的な実験と設計評価** を実践できる  
- 💡 **スクリプト技術 × 設計解析** の実務スキル育成  
- 📈 教育現場でも **再現性の高い自動化環境** を提供可能  

---

## 📦 今後の拡張｜Future Extensions

- `.meas` を使った Vth 自動抽出と劣化モデル接続  
- OpenLane で得たセル特性と信頼性シミュレーションの統合  
- GitHub Actions や CI/CD との連携による自動化パイプライン化  

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)

