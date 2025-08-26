---
layout: default
title: 実践編 第4章　PoC仕様書と設計展開
---

---

# 🧩 実践編 第4章：PoC仕様書と設計展開  
**Practical Chapter 4: PoC Specifications and Design Implementation**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter4_poc_spec_and_design/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter4_poc_spec_and_design) |

---

## 📘 概要｜Overview

本章では、SkyWaterの Sky130 PDK を用いた最小限のPoC（Proof of Concept）回路を題材に、  
**論理仕様書の作成からRTL設計・物理実装までの一連の設計プロセス**を体験します。

扱う回路は **FSM / MUX / Adder** の3種類で、いずれも**教育的に有用かつ再利用性の高い設計ブロック**です。  
This chapter walks through the end-to-end design process for FSM, MUX, and Adder blocks,  
providing hands-on experience with reusable PoC designs using the Sky130 PDK.

---

## 🎯 学習目標｜Learning Objectives

- ✅ 仕様書に基づいた設計要件の整理  
  Understand and organize design requirements based on PoC specifications  
- ✅ Sky130固有の制約項目を把握し、設計に反映  
  Learn Sky130-specific design constraints and apply them  
- ✅ 論理合成から物理設計までの流れを実践  
  Practice the full flow from logic synthesis to layout  
- ✅ Verilog・Makefile・スクリプト連携の実装力向上  
  Gain practical skills in integrating HDL, Makefile, and scripts  

---

## 🛠️ 対象PDKとツール｜Target PDK & Tools

| 項目｜Item | 内容｜Details |
|------|-----------------------------|
| **PDK** | SkyWater Sky130 |
| **EDA環境** | OpenLane v2.x, Magic, KLayout |
| **記述言語** | Verilog 2005 準拠 |
| **補助ツール** | Python3, Makefile scripts など |

---

## 🗂️ 章内構成｜Section List

| 節番号 | ファイル名 | 内容 |
|--------|------------|------|
| 4.1 | [`4.1_poc_spec_overview.md`](4.1_poc_spec_overview.md) | **PoC仕様の概要と設計方針**  
| 4.2 | [`4.2_poc_block_definition.md`](4.2_poc_block_definition.md) | **FSM・MUX・Adderの機能仕様**  
| 4.3 | [`4.3_sky130_design_constraints.md`](4.3_sky130_design_constraints.md) | **Sky130設計制約の理解**  
| 4.4 | [`4.4_verilog_and_testbench.md`](4.4_verilog_and_testbench.md) | **Verilog RTLとTestbench構成**  
| 4.5 | [`4.5_physical_design_flow.md`](4.5_physical_design_flow.md) | **OpenLaneによる物理設計実施**  
| 4.6 | [`4.6_layout_result_and_discussion.md`](4.6_layout_result_and_discussion.md) | **結果の検証と考察**  

---

## 🧱 PoC対象ブロック例｜PoC Block Examples

### ✅ FSM（Finite State Machine）

- 状態数：4（IDLE, LOAD, EXEC, DONE）  
- I/O：clk, rst, ctrl, flag  
- 主目的：**状態制御の学習、時系列遷移の理解**

---

### ✅ MUX（2:1 Multiplexer）

- 入力：A, B, SEL  
- 出力：Y = SEL ? B : A  
- 主目的：**シンプルな論理構造とレイアウト確認**

---

### ✅ Adder（4-bit Ripple Carry）

- 入力：A[3:0], B[3:0]  
- 出力：SUM[3:0], COUT  
- 主目的：**ルーティング・遅延特性の観察**

---

## 📏 Sky130制約の代表例｜Typical Sky130 Constraints

| 区分 | 制約項目 | 内容 |
|------|----------|------|
| 回路規模 | ～1,000ゲート | OpenLaneで処理可能な範囲 |
| クロック周波数 | ～25 MHz | Setup / Hold 余裕あり |
| 電源 | 1.8 V | Sky130の標準条件に準拠 |
| IO配置 | ピン配置制限あり | レイアウトでの考慮必要 |
| DRC / LVS | Magic / Netgen 通過要件 | 物理検証に必須 |
| 命名規則 | snake_case 推奨 | OpenLane互換を保つため |
| バス表記 | `[3:0]`形式で統一 | 明示的ビット指定を徹底 |
| 面積 | ～100 µm × 100 µm | 小スケールに適した構成 |

---

## 📁 ソースディレクトリ構成｜Source Directory

| ディレクトリ | 内容 |
|-------------|------|
| [`src_rtl/`](src_rtl/) | Verilog RTL 記述（FSM, MUX, Adder） |
| [`src_tb/`](src_tb/) | テストベンチ（fsm_tb.v など） |

---

## 🛠 Makefileによる自動化｜Automation with Makefile

- [`Makefile`](Makefile)：以下を一括実行可能  
  - `make sim` → テストベンチによる機能確認  
  - `make synth` → 論理合成ステップ  
  - `make flow` → OpenLane物理設計全体の実行  
  - `make report` → レポート生成

---

## 💡 Tips（補足）

- FSMの状態遷移図を [Mermaid.js](https://mermaid.js.org/) で描画可能  
- 各ブロックは [実践編 第3章](../e_chapter3_openlane_practice/README.md) と連携可能  
- `.cfg`・`.tcl`制約ファイルの微調整で設計改善が可能  

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
