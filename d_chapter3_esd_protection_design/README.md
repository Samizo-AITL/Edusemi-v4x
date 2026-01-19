---
layout: default
title: 応用編 第3章　ESD設計
---

---

# ⚠️ 応用編 第3章 : ESD設計 
**Applied Chapter 3 : ESD Protection Design**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) |

---

## 📘 概要 / Overview

**ESD（Electrostatic Discharge：静電気放電）**は、**半導体ICに最も頻繁に影響を与える信頼性リスクの一つ**です。  
特にI/Oセルや電源ラインでは、外部からの高電圧スパイクによりデバイスが破壊される恐れがあります。

**ESD is one of the most frequent reliability risks in semiconductor ICs.**  
External high-voltage spikes at I/O or power lines can cause serious damage to internal circuits.

本章では、**ESD保護設計の基本原理から、素子構造・レイアウト設計・試験規格・破壊解析まで**、実務に基づいて体系的に解説します。

This chapter provides a comprehensive overview of **ESD protection**, covering fundamentals, device structures, layout strategies, qualification standards, and real-world failure cases.

---

## 🗂️ セクション構成 / Section Contents

| ファイル名 / File | 内容概要 / Description |
|------------------|-------------------------|
| [`esd_overview.md`](./esd_overview.md) | **ESDの基本現象と設計意義**（HBM, CDM, 対策方針）<br>Basic ESD phenomena and importance of protection design |
| [`esd_devices.md`](./esd_devices.md) | **保護素子の構造と動作**（GGNMOS, ダイオード, SCR）<br>Structures and operation of key protection devices |
| [`esd_layout.md`](./esd_layout.md) | **レイアウト上の工夫**（DPP距離、ガードリング）<br>Layout-level strategies such as DPP and guard rings |
| [`esd_spec.md`](./esd_spec.md) | **ESD試験モデルと評価規格**（HBM, MM, CDM）<br>Evaluation models and JEDEC/ESDA standards |
| [`esd_failure_case.md`](./esd_failure_case.md) | **破壊モードと物理解析**（OBIRCH, EMMI, FIB）<br>Failure modes and physical failure analysis techniques |

---

## 🎯 対象読者 / Intended Audience

- 🔧 ESD破壊やI/Oトラブルに直面したことのある**若手エンジニア**  
  Young engineers dealing with ESD-related failures

- 🧠 **回路設計者・レイアウト設計者**  
  Circuit and layout designers aiming to improve protection schemes

- 🔍 製品品質・信頼性試験・不良解析に関わる**品質技術者・FA担当者**  
  Quality and failure analysis engineers

---

## 🧩 本章の到達目標 / Learning Objectives

- ✅ **ESDの発生原理・破壊モード・保護回路の基本**を理解する  
  Understand the principles of ESD and protection strategies

- ✅ GGNMOSやダイオード等の**保護素子の構造と動作**を把握する  
  Learn how ESD protection devices function and trigger

- ✅ 配線・ガードリング・DPP距離など**レイアウトでの工夫**を実装できる  
  Apply layout-level optimizations for ESD resilience

- ✅ 破壊解析から設計改善への**実務的フィードバックループ**を理解する  
  Recognize how failure analysis informs better design

---

## 🔗 関連リンク・参照章 / Related Chapters

- 📘 [応用編 第2章 高耐圧デバイス](../d_chapter2_high_voltage_devices/README.md)  
  **dv/dt破壊・電界集中回避とESDとの連携**  
  High-voltage devices and coordination with ESD design

- 🧪 [基礎編 第6章 テストとパッケージ](../chapter6_test_and_package/README.md)  
  **信頼性試験・ESDスクリーニングとの接続**  
  Reliability testing and screening context for ESD

- 🔧 [応用編 第5章 アナログ／ミックスドシグナル](../d_chapter5_analog_mixed_signal/README.md)  
  **ESD感受性の高いアナログ端子の注意点**  
  ESD-prone analog interfaces and layout guidelines

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-black?logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** |[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)
