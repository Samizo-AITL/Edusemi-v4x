---
layout: default
title: 実践編 第5章 設計結果の評価とレポート
---

---

# 🧪 実践編 第5章：設計結果の評価とレポート  
**Practical Chapter 5: Evaluation and Reporting of Design Results**

---

この章では、実際に設計・実装されたPoCブロック（FSM, MUX, Adder）に対して、  
**シミュレーション結果・面積・タイミング・DRC/LVS** などの評価指標を用いて解析を行います。

設計行為は、実行して終わりではありません。  
**結果の確認 → 改善提案 → 再設計** というフィードバックサイクルを回すことで、真の設計力が養われます。

---

## 📚 章構成｜Section Overview

| 節番号 | 📘 日本語タイトル | 📙 English Title | 🔗 ファイル名 |
|--------|------------------|------------------|-----------------------------|
| **5.1** | [シミュレーション結果と波形評価](5.1_simulation_result_check.md) | Waveform Evaluation | `5.1_simulation_result_check.md` |
| **5.2** | [面積・タイミングとレポート解釈](5.2_area_and_timing_report.md) | Area & Timing Report | `5.2_area_and_timing_report.md` |
| **5.3** | [DRC・LVSチェックとエラー解析](5.3_drc_and_lvs_check.md) | DRC/LVS & Error Analysis | `5.3_drc_and_lvs_check.md` |
| **5.4** | [ブロック間比較と特性考察](5.4_comparison_summary.md) | Block Comparison | `5.4_comparison_summary.md` |
| **5.5** | [改善提案と設計フィードバック](5.5_improvement_feedback.md) | Feedback and Redesign | `5.5_improvement_feedback.md` |

---

## 🎯 対象ブロック｜Target PoC Blocks

- ✅ **FSM**（有限状態機械 / Finite State Machine）  
- ✅ **MUX**（2:1セレクタ / 2:1 Multiplexer）  
- ✅ **Adder**（4ビット加算器 / 4-bit Adder）  

---

## 📘 学習のポイント｜Learning Objectives

- 📈 **波形とレポートから「設計が正しいか」を読み取る**  
- 🧠 **数値（Slack、面積、DRC件数）に基づく評価と比較**  
- 🔧 **改善点を構造的に分析し、設計改善案として表現する**

---

## 🔗 次章への接続｜Next Step

評価結果をもとに、**より高度な設計・実装（応用編）** へのステップアップが可能です。

- 高耐圧設計（HV）
- AMS混載設計
- DFM/PDK適応設計
- SRAM/非揮発性メモリ統合設計 などへ展開可能です。

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
