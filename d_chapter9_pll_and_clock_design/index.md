---
layout: default
title: 応用編 第9章　PLLとクロック設計 
---

---

# ⏰ 応用編 第9章：PLLとクロック設計　
**Applied Chapter 9: PLL and Clock Design**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) |

---

## 📘 概要｜Overview

クロックはすべての同期動作の基準であり、LSI設計において最も重要な信号のひとつです。  
Clock is the foundation of all synchronous operations and one of the most critical signals in LSI design.

その中でも、**PLL（Phase-Locked Loop）** は高精度なクロックを生成・整形する中心的な構成要素です。  
Among them, **PLL (Phase-Locked Loop)** plays a central role in generating and refining high-precision clocks.

本章では、PLLの動作原理からスキュー・ジッタ対策、クロックツリー設計までを網羅します。  
This chapter covers everything from the basic principles of PLLs to skew/jitter handling and clock tree design.

---

## 📂 セクション構成｜Section Structure

| ファイル名｜File | 内容｜Description |
|------------------|--------------------------|
| [`pll_basics.md`](pll_basics.md) | **PLLの基本構造と動作原理**<br>Structure and operation of PLL, including VCO, PFD, loop filter |
| [`clock_tree_design.md`](clock_tree_design.md) | **クロックツリー設計と遅延最小化**<br>CTS techniques to minimize skew and delay |
| [`jitter_and_skew.md`](jitter_and_skew.md) | **ジッタとスキューの理解と対策**<br>Definition, causes, and mitigation of jitter and skew |

---

## 🎯 対象読者｜Target Audience

- 初めてクロック設計やタイミング設計を学ぶ学生・若手技術者  
  Students and junior engineers new to clock/timing design  
- PLLやCTSの基礎知識を整理したい設計者  
  Designers looking to review PLL and CTS basics  
- ジッタ・スキューの物理的意味を学びたい教育者  
  Educators exploring physical implications of jitter and skew  

---

## 🔗 関連章｜Related Chapters

- [基礎編 第5章 SoC設計フローとEDA](../chapter5_soc_design_flow/README.md)  
  ↳ クロックツリー構築とSTAとの接続  
  ↳ Clock tree construction and STA integration  
- [基礎編 第6章 テストとパッケージ](../chapter6_test_and_package/README.md)  
  ↳ 波形品質、タイミング検証との関連  
  ↳ Signal integrity and timing test connections  

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
