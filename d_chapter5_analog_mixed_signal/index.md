---
layout: default
title: 応用編 第5章　アナログ／ミックスドシグナル
---

---

# 🎛️ 応用編 第5章　: アナログ／ミックスドシグナル  
**Applied Chapter 5. Analog / Mixed-Signal Design**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) |

---

## 📘 概要｜Overview

**アナログ／ミックスドシグナル（AMS）設計**は、デジタルとアナログが混在するSoCやセンサ応用において不可欠な技術領域です。  
本章では、**オペアンプやコンパレータなどの基本回路**から、**レイアウト設計、ノイズ対策、ADC/DACの混載課題**に至るまで、AMS設計の全体像を構造的に学びます。

**Analog / Mixed-Signal (AMS) design** is an essential domain in SoCs and sensor applications where digital and analog circuits coexist.  
This chapter provides a structured understanding of AMS design, from **basic circuits such as op-amps and comparators** to **layout design, noise countermeasures**, and **integration challenges with ADC/DAC**.

---

## 📂 セクション構成｜Section Structure

| 📄 **ファイル名｜Filename** | 📚 **内容｜Description** |
|----------------------------|--------------------------|
| [`ams_overview.md`](./ams_overview.md) | AMS設計の概要と設計課題全体像<br>Overview of AMS design and key design challenges |
| [`basic_blocks.md`](./basic_blocks.md) | オペアンプ、バッファ、コンパレータなどの基本構成と動作<br>Basic building blocks like op-amps, buffers, comparators |
| [`layout_considerations.md`](./layout_considerations.md) | AMS回路における対称性・マッチング・ウェル配置の注意点<br>Layout considerations: symmetry, matching, well placement |
| [`noise_and_psrr.md`](./noise_and_psrr.md) | ノイズ源の分類とPSRRによる電源変動耐性評価<br>Noise sources classification and PSRR-based noise tolerance |
| [`mixed_signal_interface.md`](./mixed_signal_interface.md) | ADC/DACの構成と混載インタフェース設計課題<br>ADC/DAC architecture and mixed-signal interface design issues |
| [`ams_node_selection.md`](./ams_node_selection.md) | AMS設計におけるノード選定とプロセス技術の特徴<br>Node selection strategies and process characteristics for AMS |

---

## 🎯 対象読者｜Target Audience

- アナログ回路の基本構成に慣れてきた初学者  
  *Beginners familiar with basic analog circuits*
- SoCにおける混載設計を体系的に理解したい設計者  
  *Engineers aiming to understand mixed-signal SoC design*
- ノイズやレイアウトといった非理想要因への対策に興味のある方  
  *Learners interested in countermeasures for noise and layout imperfections*

---

## 🔗 関連章｜Related Chapters

| 章｜Chapter | 内容｜Details |
|-------------|----------------|
| [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/) | MOSトランジスタの物性とマッチング視点<br>MOS characteristics and matching considerations |
| [`d_chapter6_pdk_and_eda_environment/`](../d_chapter6_pdk_and_eda_environment/) | PDKを活用したアナログ設計環境<br>Analog design environments using PDKs |

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
