---
layout: default
title: 基礎編 第2章：デジタル論理と論理回路設計
---

---

# 📘 基礎編 第2章：デジタル論理と論理回路設計  
**Fundamentals-Chapter 2: Digital Logic and Logic Circuit Design**

---

## 🎯 本章の目的｜Objectives

| 🇯🇵 日本語                                                                                           | 🇺🇸 English                                                                                       |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| - AND, OR, NOT, NAND, XORなどの**基本論理ゲート**の構成と特性を理解する                              | - Understand the structure and characteristics of **basic logic gates** such as AND, OR, NOT.   |
| - 真理値表・論理式・回路図の**相互変換**ができるようになる                                           | - Be able to **convert** between truth tables, logic expressions, and circuit diagrams.         |
| - MUXや加算器などの**応用的な組み合わせ回路の設計**を学ぶ                                           | - Learn how to design **combinational logic** such as MUXes and adders.                         |
| - FSM（有限状態機械）の構造と概念を理解し、**順序回路設計への橋渡し**を行う                          | - Understand FSMs and connect them to **sequential logic design**.                              |

---

## 🗂️ 章構成｜Chapter Structure (`chapter2_comb_logic/`)

| 節番号 | 日本語タイトル | 英語タイトル | ファイル名 |
|--------|----------------|---------------|------------|
| 2.1 | 基本ゲート構成 | Basic Gate Design | [`2.1_logic_gates.md`](./2.1_logic_gates.md) |
| 2.2 | 複合ゲート論理 | Compound Gate Logic | [`2.2_nand_nor_xor.md`](./2.2_nand_nor_xor.md) |
| 2.3 | 動作検証法 | Verification Methods | [`2.3_truth_table_waveform.md`](./2.3_truth_table_waveform.md) |
| 2.4 | 選択回路設計 | Multiplexer and Selector Design | [`2.4_mux_and_selector.md`](./2.4_mux_and_selector.md) |
| 2.5 | 加算器構成 | Adder Structures | [`2.5_half_full_adder.md`](./2.5_half_full_adder.md) |
| 2.6 | FSM導入 | Introduction to FSM | [`2.6_fsm_intro.md`](./2.6_fsm_intro.md) |
| 2.7 | 全体構成の俯瞰 | Overview of Logical Components | [`2.7_component_relationships.md`](./2.7_component_relationships.md) |

---

## 🧠 学習のポイント｜Key Takeaways

- **論理式 ↔ 回路図 ↔ 真理値表 ↔ 波形** の相互変換力を養成  
  > Foster the ability to **translate between logic expressions, schematics, truth tables, and waveforms**.  
- CMOS構成における**論理機能と物理実装の対応関係**を理解  
  > Understand the **mapping between logic and CMOS physical implementation**.  
- MUX・加算器・FSMなど**応用構成要素の設計手法**を体得  
  > Learn design techniques for **applied building blocks** like MUX, adders, FSM.  
- FSMによって、**時間的に変化する動作の記述法**が導入される  
  > FSMs introduce design methods for **time-varying behaviors**.  
- 最終節では**制御・選択・演算**の3分類で全体設計視野を整理  
  > Final section classifies components into **control, selection, arithmetic** for system-level overview.  

---

## 📂 ディレクトリ構成｜Directory Structure

```
Edusemi-v4x/
└── chapter2_comb_logic/
    ├── README.md
    ├── 2.1_logic_gates.md
    ├── 2.2_nand_nor_xor.md
    ├── 2.3_truth_table_waveform.md
    ├── 2.4_mux_and_selector.md
    ├── 2.5_half_full_adder.md
    ├── 2.6_fsm_intro.md
    └── 2.7_component_relationships.md
```

---

## 🖼️ 図版・補足予定｜Illustrations

- ゲート回路記号、CMOS構成図、真理値表テンプレート  
- タイミング波形、MUX構成、加算器構成、FSM状態遷移図  
- All illustrations stored under `/images/` with `chapter2_` prefix

---

## 🔄 前章との接続｜Connection to Previous Chapter

| 🇯🇵 日本語 | 🇺🇸 English |
|-----------|------------|
| 第1章では、**MOS構造とスイッチ動作の物理基盤**を解説しました。 | Chapter 1 covered **MOS structure and switching behavior fundamentals**. |
| 本章では、その動作原理をもとに**論理回路の構成法を体系的に学習**します。 | This chapter systematically explores **logic circuit design** based on those principles. |

📎 [← 第1章へ戻る](../chapter1_materials/README.md)

---

## 🔜 次章への接続｜Lead-in to Next Chapter

| 🇯🇵 日本語 | 🇺🇸 English |
|-----------|------------|
| 第3章では、論理回路の背景にある**CMOS構造・プロセス技術・設計限界**を扱います。 | Chapter 3 deals with **CMOS structure, process evolution, and design limits** behind logic circuits. |
| FSMで触れた「状態・順序性」は、**設計とプロセスの接続点**として扱われます。 | The concepts of **state and sequencing** introduced via FSM will link to process-aware design. |

📎 [→ 第3章へ進む](../chapter3_process_evolution/README.md)

---

## 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

## 🔙 戻る｜Back to Top
**🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)**
