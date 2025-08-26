---
layout: default
title: 特別編 第3章 FSM×PID×LLMによる統合制御システムのSoC実装手法
---

---

# 🧠 特別編 第3章  
## FSM×PID×LLMによる統合制御システムのSoC実装手法  
**Special Chapter 3: SoC Implementation of Integrated Control System with FSM × PID × LLM**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) |

---

本章では、**AITL-H構想**（FSM・PID・LLMによる三層制御）をベースとした  
**統合制御アーキテクチャのSoC実装手法**を学習します。  
*This chapter presents the method for implementing the AITL-H three-layer control architecture as a System-on-Chip (SoC).*

---

## 🎯 目的と構成 | Purpose & Overview

| 🧩 構成層｜Layer | 🔧 役割｜Function | 🛠️ 実装対象｜Target Implementation |
|------------------|----------------------|------------------------------|
| **FSM**          | 状態遷移による反応制御<br>Instinctive control via state transitions | Verilog RTL<br>`fsm_engine.v` |
| **PID**          | 安定化・物理量制御<br>Stabilization and control of physical parameters | VerilogまたはMixed-Signal<br>`pid_controller.v` |
| **LLM**          | 高度判断・外部応答制御<br>High-level decision & external interaction | RISC-V連携ソフト<br>`llm_interface.c` |

本章では、これら三層構造を**機能分離・階層連携・SoC内統合**する手法を習得します。  
*You will learn how to separate concerns, connect layers, and integrate the entire system into a unified SoC.*

---

## 📚 章構成 | Chapter Structure

| 🚩 節番号 | 📖 日本語タイトル | 📘 英語タイトル |
|-----------|------------------|------------------|
| 3.1 | [AITL-Hアーキテクチャと層分離設計](docs/3_1_aitl_architecture.md) | [AITL-H Architecture and Layered Design](docs/3_1_aitl_architecture.md) |
| 3.2 | [FSM設計とRTLモジュール構成](docs/3_2_fsm_design.md) | [FSM Design and RTL Module Structure](docs/3_2_fsm_design.md) |
| 3.3 | [PID制御のASIC実装（デジタル／アナログ）](docs/3_3_pid_design.md) | [PID Controller Implementation (Digital/Analog)](docs/3_3_pid_design.md) |
| 3.4 | [LLMとの接続設計（RISC-V・I/O連携）](docs/3_4_llm_interface.md) | [LLM Interface Design (RISC-V / I/O Integration)](docs/3_4_llm_interface.md) |
| 3.5 | [SoC統合とバス構造・通信設計](docs/3_5_soc_integration.md) | [SoC Integration and Communication Design](docs/3_5_soc_integration.md) |
| 3.6 | [ケーススタディ：三層制御によるPoC実装例](docs/3_6_case_study.md) | [Case Study: PoC with Three-Layer Control](docs/3_6_case_study.md) |

---

## 🗂️ ディレクトリ構成 | Directory Structure

```plaintext
f_chapter3_socsystem/
├── README.md                      ← 本ファイル / This file
├── toc.md                         ← 章内目次 / Table of Contents
├── docs/                          ← 各節ドキュメント / Chapter Sections
│   ├── 3_1_aitl_architecture.md
│   ├── 3_2_fsm_design.md
│   ├── 3_3_pid_design.md
│   ├── 3_4_llm_interface.md
│   ├── 3_5_soc_integration.md
│   └── 3_6_case_study.md
├── verilog/                       ← RTL設計ファイル / Verilog Modules
│   ├── fsm_engine.v
│   ├── pid_controller.v
│   └── soc_top.v
├── sw_riscv/                      ← LLM連携ソフト / RISC-V Software
│   └── llm_interface.c
├── testbench/                     ← テストベンチ / Simulation Testbenches
│   └── test_soc_top.v
└── images/                        ← 図・構成図 / Figures & Diagrams
    └── aitl_three_layer_architecture.png
```

---

## 🔗 参考リンク | Reference Links

| 🔍 項目 | 📎 リンク |
|--------|------------|
| **AITL-H理論**<br>AITL-H Theory | [theory/](https://github.com/Samizo-AITL/AITL-H/tree/main/theory) |
| **PoC設計マニュアル**<br>PoC Design Manual | [docs/](https://github.com/Samizo-AITL/AITL-H/tree/main/docs) |
| **FSM実装例（Python）** | [`fsm_engine.py`](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/fsm_engine/fsm_engine.py) |
| **LLM制御ソフト（Python）** | [`llm_interface.py`](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/llm_interface.py) |

> 💡 **注記 / Note**  
> 本章は **Edusemi特別編** の一部であり、**AITL-H実装の実験的PoC設計**に基づいています。  
> *This chapter is part of Edusemi's special edition, based on experimental PoC designs for AITL-H.*

---

## 🎓 学習目標 | Learning Objectives

| 🎯 項目 | 内容 |
|--------|------|
| **三層制御の責務分離と再利用設計**<br>Layered Responsibility & Reuse | 各層の独立性と再利用性を高める設計を学ぶ |
| **FSMのVerilog構造化**<br>FSM to Verilog Structuring | 状態遷移モデルからRTLモジュール化の流れを習得 |
| **PID制御器のSoC統合**<br>PID SoC Integration | アナログ/デジタルPIDの利点と統合方法を理解 |
| **LLM連携設計**<br>LLM Integration Design | RISC-VベースのI/O制御と知能判断接続設計を習得 |
| **統合設計テンプレートの理解**<br>SoC Pattern Mastery | 三層連携のSoC設計テンプレートを習得する |

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

🏠 [Edusemi-v4x トップへ戻る](../README.md)

