---
layout: default
title: 実践編 第4章　PoC仕様書と設計展開
---

---

# 🧩 実践編 第4章：PoC仕様書と設計展開  
**Practical Chapter 4: PoC Specifications and Design Implementation**

---

## 📘 概要｜Overview

本章では、Sky130 PDKを用いた最小限の半導体設計PoC（Proof of Concept）を通じて、  
**論理回路の仕様書作成から物理設計に至るプロセス**を体験します。

対象はFSM、MUX、Adderなど、教育的価値と再利用性の高いブロックです。  
This chapter guides learners through the **entire design process**, from specification to layout,  
using reusable educational blocks like FSM, MUX, and Adder on the Sky130 PDK.

---

## 🎯 本章の目的｜Objectives

- ✅ 仕様書をもとにした設計要求の整理  
 Clarify design intent through PoC-based specifications  
- ✅ Sky130制約項目の実務理解  
 Understand Sky130-specific design constraints  
- ✅ 論理合成～物理設計までの設計フロー習得  
 Master synthesis to physical design flow  
- ✅ Verilog, Makefile, 自動化スクリプトの統合体験  
 Integrate HDL, Makefile, and automation scripts

---

## 🏗️ 使用PDKとツール｜Target PDK & Tools

| 項目｜Item | 内容｜Details |
|---------|------------------------------|
| **PDK** | SkyWater Sky130 |
| **EDA環境** | OpenLane v2, Magic, KLayout |
| **言語** | Verilog 2005 準拠 |
| **補助ツール** | Python3, Makefile scripts |

---

## 📚 章構成｜Section List

| **節番号<br>Section** | **ファイル名<br>Filename** | **内容<br>Content** |
|-----------------------|-----------------------------|----------------------|
| 4.1 | [`4.1_poc_spec_overview.md`](4.1_poc_spec_overview.md) | **PoC仕様概要と設計目的**<br>Overview of PoC Spec and Design Goals |
| 4.2 | [`4.2_poc_block_definition.md`](4.2_poc_block_definition.md) | **FSM, MUX, Adderの機能仕様**<br>Functional Spec of FSM, MUX, Adder |
| 4.3 | [`4.3_sky130_design_constraints.md`](4.3_sky130_design_constraints.md) | **Sky130設計制約とPDK依存項目**<br>Design Constraints and PDK Dependencies |
| 4.4 | [`4.4_verilog_and_testbench.md`](4.4_verilog_and_testbench.md) | **VerilogとTestbench構成**<br>Verilog and Testbench Setup |
| 4.5 | [`4.5_physical_design_flow.md`](4.5_physical_design_flow.md) | **OpenLaneを用いた物理設計フロー**<br>Physical Design Flow with OpenLane |
| 4.6 | [`4.6_layout_result_and_discussion.md`](4.6_layout_result_and_discussion.md) | **結果検証とまとめ**<br>Result Evaluation and Summary |

---

## 🧱 最小PoCブロック例｜PoC Block Examples

### 1. FSM（Finite State Machine）

- 状態数：4（IDLE, LOAD, EXEC, DONE）  
- I/O：clk, rst, ctrl, flag  
- 目的：状態制御と制御信号生成の学習

### 2. MUX（2:1 Multiplexer）

- 入力：A, B, SEL  
- 出力：Y = SEL ? B : A  
- 目的：シンプルな組合せ論理とレイアウト評価

### 3. Adder（4-bit Ripple Carry）

- 入力：A[3:0], B[3:0]  
- 出力：SUM[3:0], COUT  
- 目的：ルーティング・タイミング評価

---

## 📏 Sky130制約項目例｜Sky130 Constraint Checklist

| **区分｜Type**            | **制約項目｜Constraint** | **内容｜Details**                          |
|---------------------------|---------------------------|-------------------------------------------|
| 回路規模<br>Gate Count     | ～1,000 gates              | OpenLaneで無理なく通過可能                  |
| 周波数<br>Clock Freq.     | ～25 MHz                  | Setup / Hold 余裕を確保                    |
| 電源<br>Supply            | VDD = 1.8 V               | Sky130 規格に準拠                          |
| IO制約<br>IO Pad          | サイズ・配置制限あり          | マクロ内レイアウトに配慮                    |
| レイアウト<br>DRC / LVS   | Magic / Netgen 通過         | 検証ツール基準を満たす必要がある             |
| ネーミング<br>Signal Name | snake_case 命名             | OpenLane互換性のあるスタイル推奨             |
| バス構文<br>Bus Notation  | `[3:0]` 表記で統一            | 明示的なビット範囲指定を行う                 |
| 面積<br>Die Area          | ～100 µm × 100 µm         | FSM・MUXに最適な小スケール構成              |

---

## 🗂 ソース構成｜Source Directory

| ディレクトリ｜Dir | 内容｜Description |
|-------------------|-----------------------------|
| [`src_rtl/`](src_rtl/) | RTL記述（FSM, MUX, Adder） |
| [`src_tb/`](src_tb/) | テストベンチ（fsm_tb.vなど） |

---

## 🛠 Makefile

- [`Makefile`](Makefile)：シミュレーション、OpenLane実行など自動化コマンドを含む

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
