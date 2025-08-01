# 📘 基礎編 第3章：プロセス技術と設計限界の理解  
# 📘 Chapter 3: Process Evolution and Design Limits in CMOS

---

## 🔁 前章との接続｜Connection to Previous Chapter

| 🇯🇵 日本語 | 🇺🇸 English |
|-----------|------------|
| 第2章では、**論理ゲート・組み合わせ回路・FSM**など、CMOS論理設計の基礎を学習しました。 | Chapter 2 covered **logic gates, combinational logic, and FSMs** as fundamentals of CMOS design. |
| 第3章では、それらの設計が実際に動作するための**物理的基盤（プロセス技術）**に踏み込みます。 | Chapter 3 now explores the **physical foundation (process technology)** that enables those designs. |

📎 [← 第2章：デジタル論理と論理回路設計](../chapter2_comb_logic/README.md)  
📎 [← Chapter 2: Digital Logic and Logic Circuit Design](../chapter2_comb_logic/README.md)

---

## 🧭 概要｜Overview

本章では、0.5µmから90nmノードに至るCMOS技術の変遷を通じて、  
**設計可能性を左右するプロセス技術の進化と物理限界**を体系的に学びます。

> This chapter explores the evolution of CMOS technologies from 0.5µm to 90nm,  
> focusing on how process advancements and limitations shape circuit design.

---

## ✨ 主なキーワード｜Key Concepts

```
STI, LDD, Salicide, Multi-Layer Interconnect, CMP, OPC, 
SCE, HCI, DIBL, Vth Variability, sky130, 0.18µm
```

---

## 🎯 学習のねらい｜Learning Objectives

| 🇯🇵 日本語                                                                                     | 🇺🇸 English                                                                                      |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| プロセス技術が**設計制約に与える影響**を理解する                                               | Understand how process technologies affect **design constraints**.                           |
| 微細化による**構造革新と信頼性課題**を体系的に整理する                                        | Learn about **structural evolution and reliability issues** caused by scaling.               |
| 教材として適したノード（sky130, 0.18µm）を選定できる                                          | Develop criteria to choose **educationally suitable process nodes** (e.g., sky130, 0.18µm). |

---

## 📚 章構成とリンク｜Chapter Contents and Links

| 節番号 | ファイル名 / Filename                                               | 内容概要 / Summary                                                                 |
|--------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 3.1    | [`3.1_node_scaling_history.md`](./3.1_node_scaling_history.md)       | ノード微細化の歴史<br>📏 *History of Node Scaling*                                 |
| 3.2    | [`3.2_cmos_structure_shift.md`](./3.2_cmos_structure_shift.md)       | トランジスタ構造の進化（STI, LDDなど）<br>🔬 *CMOS Structural Innovations*         |
| 3.3    | [`3.3_interconnect_and_litho.md`](./3.3_interconnect_and_litho.md)   | 多層配線・リソグラフィ技術<br>🧵 *Interconnect and Lithography Advancements*       |
| 3.4    | [`3.4_variation_and_reliability.md`](./3.4_variation_and_reliability.md) | SCE / DIBL / 信頼性限界<br>⚠️ *Variability & Reliability Issues*             |
| 3.5    | [`3.5_summary_and_scope.md`](./3.5_summary_and_scope.md)             | 教育用ノードの選定と適用範囲<br>🎓 *Selecting Nodes for Education*               |

---

## 📎 付録：プロセス技術フローチャート（Appendix）  
### Appendix: Process Technology Flow Charts

| リファレンス | ファイル名 / Filename                                                                 | 内容概要 / Description |
|--------------|------------------------------------------------------------------------------------------|-------------------------|
| A-1          | [`0.18um_Logic_ProcessFlow.md`](./docs/0.18um_Logic_ProcessFlow.md)                           | 🧪 **0.18µm CMOSプロセスフロー（日本語）**<br>Standard logic process flow in Japanese |
| A-1b         | [`0.18um_1.8_3.3_5V.md`](./docs/0.18um_1.8_3.3_5V.md)                                         | ⚡ **3電源対応プロセス（1.8V / 3.3V / 5V）**<br>Multi-V CMOS integration flow |
| A-1c         | [`0.18um_etests_summary_unified.md`](./docs/0.18um_etests_summary_unified.md)                 | 📐 **E-Test特性まとめ（電圧別・構造別）**<br>Unified E-test result overview |
| A-2          | [`0.18um_Logic_ProcessFlow_en.md`](./docs/0.18um_Logic_ProcessFlow_en.md)                     | 🧪 **0.18µm CMOS Process Flow（English）**<br>Standard logic process flow in English |
| A-3          | [`0.13um_Logic_ProcessFlow.md`](./docs/0.13um_Logic_ProcessFlow.md)                           | 🧪 **0.13µm CMOSプロセス（日本語）**<br>Includes Cu interconnect, Low-k dielectric |
| A-4          | [`0.09um_Logic_ProcessFlow.md`](./docs/0.09um_Logic_ProcessFlow.md)                           | 🧪 **90nm CMOSプロセス（日本語）**<br>NiSi salicide, strained-Si, ULK integration |
| A-5          | [`process_node_comparison.md`](./docs/process_node_comparison.md)                             | 📊 **180nm〜90nm ノード比較表（日本語）**<br>Comparison of oxide, interconnect, scaling trends 

> 📌 **本章の理解を補強する補足資料**です。プロセス技術の進化や、設計・製造・信頼性の観点から各世代の特徴を比較する教材として活用してください。  
> These reference files support your understanding of process evolution across technology nodes.

---

## 🔄 次章への接続｜Transition to Chapter 4

| 🇯🇵 日本語                                                                                             | 🇺🇸 English                                                                                          |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 第4章では、ここで扱ったCMOSノード（sky130 / 0.18µm）を基盤として、<br>**PDK・MOS特性・設計ルールの理解**へと進みます。 | In Chapter 4, we build on these CMOS nodes (sky130 / 0.18µm) to explore **PDKs, MOS characteristics, and design rules**. |

➡️ [**第4章：MOSトランジスタ特性と設計基盤**](../chapter4_mos_characteristics/README.md) に進む  
➡️ [**Chapter 4: MOS Characteristics and Design Fundamentals**](../chapter4_mos_characteristics/README.md) (EN)

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)

---
