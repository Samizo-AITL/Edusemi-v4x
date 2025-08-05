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
| 3.1    | [`3.1_node_scaling_history.md`](./3.1_node_scaling_history.md)       | ノード微細化の歴史と寸法ルールの進化<br>📏 *Scaling History and Design Rules*       |
| 3.2    | [`3.2_cmos_structure_shift.md`](./3.2_cmos_structure_shift.md)       | STI・LDDなど構造革新による寸法と特性の変化<br>🔬 *Structural Innovations in CMOS*    |
| 3.3    | [`3.3_interconnect_and_litho.md`](./3.3_interconnect_and_litho.md)   | 配線・CMP・RC遅延の技術進化と設計影響<br>🧵 *Interconnect and Delay Constraints*     |
| 3.4    | [`3.4_variation_and_reliability.md`](./3.4_variation_and_reliability.md) | DIBLやHCIなど信頼性とばらつきの物理限界<br>⚠️ *SCE and Reliability in Scaling*   |
| 3.5    | [`3.5_summary_and_scope.md`](./3.5_summary_and_scope.md)             | 教育ノードの選定と実践的意義の整理<br>🎓 *Choosing and Using Educational Nodes*     |

---

## 📎 付録：プロセス技術フローチャート（Appendix）  
### Appendix: Process Technology Flow Charts

| リファレンス | ファイル名 / Filename                                                                 | 内容概要 / Description |
|--------------|------------------------------------------------------------------------------------------|-------------------------|
| A-1          | [`0.18um_Logic_ProcessFlow.md`](./docs/0.18um_Logic_ProcessFlow.md)                           | 🧪 0.18µm CMOSプロセス（基本フロー） |
| A-1b         | [`0.18um_1.8V_3.3V_5V.md`](./docs/0.18um_1.8V_3.3V_5V.md)                                         | ⚡ 1.8V〜5V対応多電圧プロセス |
| A-1c         | [`0.18um_etests_summary_unified.md`](./docs/0.18um_etests_summary_unified.md)                 | 📐 E-Test特性まとめ（電圧・構造別） |
| A-2          | [`0.18um_Logic_ProcessFlow_en.md`](./docs/0.18um_Logic_ProcessFlow_en.md)                     | 🧪 0.18µm CMOS Process Flow (EN) |
| A-3          | [`0.13um_Logic_ProcessFlow.md`](./docs/0.13um_Logic_ProcessFlow.md)                           | 🧪 0.13µmプロセス（Cu配線・Low-k対応） |
| A-4          | [`0.09um_Logic_ProcessFlow.md`](./docs/0.09um_Logic_ProcessFlow.md)                           | 🧪 90nm CMOS（NiSi, strained-Si等） |
| A-5          | [`process_node_comparison.md`](./docs/process_node_comparison.md)                             | 📊 ノード比較：寸法・材料・構造 |
| A-6          | [`equipment_list_by_node.md`](./docs/equipment_list_by_node.md)                               | 🛠️ ノード別装置一覧（製造工程ごと） |

---

## 🔄 次章への接続｜Transition to Chapter 4

| 🇯🇵 日本語 | 🇺🇸 English |
|----------|-----------|
| 第4章では、ここで扱ったCMOSノード（sky130 / 0.18µm）を基盤として、**PDK・MOS特性・設計ルールの理解**へと進みます。 | In Chapter 4, we build on these CMOS nodes (sky130 / 0.18µm) to explore **PDKs, MOS characteristics, and design rules**. |

➡️ [**第4章：MOSトランジスタ特性と設計基盤**](../chapter4_mos_characteristics/README.md)

---

## 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)
