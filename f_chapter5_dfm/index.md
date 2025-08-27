---
layout: default
title: 特別編 第5章　PDKとレイアウト検証による物理整合とDFM設計指針 
---

---

# 🧬 特別編 第5章：PDKとレイアウト検証による物理整合とDFM設計指針  
**Special Chapter 5: Physical Verification and DFM Design Guidelines with PDK**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) |

---

本章では、Sky130 PDKを用いたレイアウト検証と、  
GDSレベルでの物理整合・製造配慮（DFM）に関する設計指針を学びます。  
This chapter explores physical verification using the Sky130 PDK and outlines layout design guidelines for manufacturability (DFM) at the GDS level.

---

## 🎯 本章の目的｜Chapter Objectives

| 🎯 **目的｜Objective** | 📘 **内容｜Description** |
|------------------------|--------------------------|
| **PDK構造の理解**<br>Understanding PDK Structure | Sky130におけるレイヤー構成やマスク命名の把握<br>Grasping layer stacks and mask naming in Sky130 |
| **GDS可視化と階層解析**<br>GDS Visualization and Hierarchy Analysis | Magic/KLayoutを用いた階層構造の確認<br>Visual inspection using Magic/KLayout |
| **レイアウト検証の基礎**<br>Basics of Layout Verification | DRC / LVS / ERC の仕組みと活用方法の理解<br>Understanding and using DRC, LVS, ERC |
| **DFM設計指針の習得**<br>Learning DFM Design Principles | 量産対応設計、寄生・ストレス回避設計を実践<br>Guidelines for parasitics, stress, and mass production readiness |

---

## 📖 節構成｜Section Overview

| 🔢 **節番号**<br>**Section** | 📖 **タイトル（日本語）**<br>**Title (JP)** | 📘 **Title (EN)** | 📝 **概要｜Summary** |
|--------------------------|---------------------------------------------|--------------------|-------------------------|
| **5.1** | [PDK構造の理解とSky130レイヤー体系](5_1_pdk_layer.md) | Understanding PDK and Sky130 Layer System | レイヤー命名・マスク体系を解説<br>Layer naming and mask structure |
| **5.2** | [MagicによるGDS階層と層構成の可視化](5_2_magic_gds.md) | Visualizing GDS Hierarchy with Magic | セル構造・金属層構成の可視化<br>Viewing hierarchy and metal layers |
| **5.3** | [DRCルールとその根拠（例：metal spacing）](5_3_drc_check.md) | DRC Rules and Their Basis (e.g., Metal Spacing) | MagicでのDRCチェック実施と背景の理解<br>Checking rules and understanding their reasoning |
| **5.4** | [LVSの仕組みと等価性判定の論理](5_4_lvs_check.md) | LVS Concepts and Equivalence Checking | ネットリストとGDSの比較手法を解説<br>Comparing netlists with layouts |
| **5.5** | [DFM設計：量産対応のためのレイアウト指針](5_5_dfm_guideline.md) | DFM Design Guidelines for Manufacturability | 寄生防止・ストレス緩和など実用的指針<br>Practical rules for parasitics and stress |
| **5.6** | [チップ完成に向けた最終検証ステップ](5_6_final_check.md) | Final Verification Toward Tapeout | ERC, テープアウト準備、プロービング対応<br>ERC and final checks for tapeout |

---

## 🛠️ 使用ツール・PDK｜Tools and PDK

| 🔧 **ツール｜Tool** | 📝 **説明｜Description** |
|-------------------|--------------------------|
| **Sky130A PDK** | Google/SkyWater提供のオープンPDK |
| **Magic** | DRC/LVS支援付きのレイアウトツール（PDK標準） |
| **KLayout** | 高機能GDSビューア・編集ツール |
| **Netgen** | LVS検証ツール（Magic連携） |

---

## 🔗 関連教材｜Related Materials

- 🔄 [特別編 第4章：OpenLane配置配線とGDS生成](../f_chapter4_openlane/README.md)  
  *Appendix Chapter 4: OpenLane P&R and GDS Generation*
- 🧪 [実践編：Sky130自動化・DFM評価（予定）](../p_chapter6_practice/README.md)  
  *Practice Chapter: Automation & DFM Checks with Sky130 (Upcoming)*

---

## ✅ 備考｜Notes

- 本章はSky130ベースの**レイアウト検証・PDK構造理解**に焦点を当てています。  
  This chapter focuses on **layout verification and PDK structure using Sky130**.
- **物理設計の終盤フェーズ**として、量産・テープアウトに繋がる設計知識を習得します。  
  Learn final design practices for manufacturability and tapeout readiness.

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [X / Twitter](https://x.com/shin3t72)<br>💻 [Samizo-AITL Portal](https://samizo-aitl.github.io/) |
| **ライセンス / License** | **Hybrid License**<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top
**🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)**

