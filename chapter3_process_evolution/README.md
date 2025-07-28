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

| リファレンス | ファイル名 / Filename                                               | 内容概要 / Description |
|--------------|----------------------------------------------------------------------|-------------------------|
| A-1          | [`0.18um_Logic_ProcessFlow.md`](./0.18um_Logic_ProcessFlow.md)       | 🧪 **0.18µm CMOSプロセスフロー（日本語）**<br>Full logic process flow in Japanese |
| A-2          | [`0.18um_Logic_ProcessFlow_en.md`](./0.18um_Logic_ProcessFlow_en.md) | 🧪 **0.18µm CMOS Process Flow（English）**<br>Full logic process flow in English  |

> 📌 **本章の理解を深める補足資料**として、0.18µmプロセスの工程を詳細に解説しています。

---

## 🔄 次章への接続｜Transition to Chapter 4

| 🇯🇵 日本語                                                                                             | 🇺🇸 English                                                                                          |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 第4章では、ここで扱ったCMOSノード（sky130 / 0.18µm）を基盤として、<br>**PDK・MOS特性・設計ルールの理解**へと進みます。 | In Chapter 4, we build on these CMOS nodes (sky130 / 0.18µm) to explore **PDKs, MOS characteristics, and design rules**. |

➡️ [**第4章：MOSトランジスタ特性と設計基盤**](../chapter4_mos_characteristics/README.md) に進む  
➡️ [**Chapter 4: MOS Characteristics and Design Fundamentals**](../chapter4_mos_characteristics/README.md) (EN)

---

## 📝 ライセンス｜License

この教材は [MIT License](../LICENSE) に基づき公開されています。  
> This content is released under the [MIT License](../LICENSE).

---
