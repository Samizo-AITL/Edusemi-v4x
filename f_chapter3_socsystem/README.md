---
layout: default
title: 特別編 第3章 FSM×PID×LLMによる統合制御システムのSoC実装手法
---

---

# 🧠　特別編 第3章　: FSM×PID×LLMによる統合制御システムのSoC実装手法  
**Special Chapter 3 : SoC Implementation of Integrated Control System with FSM×PID×LLM**

本章では、**AITL-H構想（FSM・PID・LLMによる三層制御）**をベースに、  
その統合制御システムを**SoCとして設計・実装**する手法を解説します。  
This chapter explains how to design and implement the **AITL-H three-layer control system (FSM, PID, LLM)** as a **System-on-Chip (SoC)**.

---

## 🎯 目的と概要｜Purpose and Overview

| 構成要素｜Layer | 機能｜Function | 実装対象｜Target Implementation |
|-------------|-------------------|------------------------------|
| **FSM**     | 状態遷移による本能的制御<br>Instinctive control via state transitions | Verilog RTL（`fsm_engine.v`） |
| **PID**     | 安定化・物理制御<br>Stabilization and physical control | VerilogまたはMixed-Signal（`pid_controller.v`） |
| **LLM**     | 知的判断・外部応答<br>Intelligent decision making and external interaction | RISC-Vソフト連携（`llm_interface.c`） |

三層構造をSoC上に実装し、**責務分離・接続戦略・ハイブリッド設計**を体系的に学びます。  
You will learn the **responsibility separation, connection strategy, and hybrid design** methodology for integrating this architecture into an SoC.

---

### 📚 章構成｜Chapter Structure

| 🚩 | 📖 日本語タイトル｜Japanese Title | 📘 英語タイトル｜English Title |
|----|-------------------------------|------------------------------|
| **3.1** | [AITL-Hアーキテクチャと層分離設計](docs/3_1_aitl_architecture.md) | [AITL-H Architecture and Layered Design](docs/3_1_aitl_architecture.md) |
| **3.2** | [FSM設計とRTLモジュール構成](docs/3_2_fsm_design.md) | [FSM Design and RTL Module Structure](docs/3_2_fsm_design.md) |
| **3.3** | [PID制御のASIC実装（デジタル／アナログ）](docs/3_3_pid_design.md) | [PID Controller Implementation (Digital/Analog)](docs/3_3_pid_design.md) |
| **3.4** | [LLMとの接続設計（RISC-V・I/O連携）](docs/3_4_llm_interface.md) | [LLM Interface Design (RISC-V / I/O Integration)](docs/3_4_llm_interface.md) |
| **3.5** | [SoC統合とバス構造・通信設計](docs/3_5_soc_integration.md) | [SoC Integration and Communication Design](docs/3_5_soc_integration.md) |
| **3.6** | [ケーススタディ：三層制御によるPoC実装例](docs/3_6_case_study.md) | [Case Study: PoC with Three-Layer Control](docs/3_6_case_study.md) |

---

## 🛠 実装ディレクトリ構成（例）｜Example Directory Structure

```plaintext
f_chapter3_socsystem/
├── README.md                      ← 章全体の概要 / Chapter Overview
├── toc.md                         ← 章内目次 / Table of Contents
├── docs/                          ← 各節の解説 / Section Documents
│   ├── 3_1_aitl_architecture.md
│   ├── 3_2_fsm_design.md
│   ├── 3_3_pid_design.md
│   ├── 3_4_llm_interface.md
│   ├── 3_5_soc_integration.md
│   └── 3_6_case_study.md
├── verilog/                       ← RTLコード / RTL Code
│   ├── fsm_engine.v
│   ├── pid_controller.v
│   └── soc_top.v
├── sw_riscv/                      ← LLM制御ソフト / LLM Software
│   └── llm_interface.c
├── testbench/                     ← テストベンチ / Testbench
│   └── test_soc_top.v
└── images/                        ← 構成図など / Diagrams
    └── aitl_three_layer_architecture.png
```

---

## 🔗 参照リンク｜Reference Links

| 項目｜Item | リンク｜Link |
|------|------|
| **AITL-H理論**<br>AITL-H Theory | [theory/](https://github.com/Samizo-AITL/AITL-H/tree/main/theory) |
| **PoC設計マニュアル**<br>PoC Design Guide | [docs/](https://github.com/Samizo-AITL/AITL-H/tree/main/docs) |
| **FSMエンジン実装例**<br>FSM Engine Example | [`fsm_engine.py`](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/fsm_engine/fsm_engine.py) |
| **LLM連携ソフト例**<br>LLM Interface Example | [`llm_interface.py`](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/llm_interface.py) |

> 💡 **注記｜Note**：本章は **Edusemi特別編** として、AITL-H実装との連携を前提としています。  
> This chapter is a **special edition** of Edusemi, assuming integration with the AITL-H implementation.

---

## 🎓 学習目標｜Learning Objectives

| 項目｜Item | 内容｜Details |
|------|------|
| **三層制御の責務分離と再利用設計**<br>Layered responsibility and reusable design | 各層の役割を明確化し、モジュール間の独立性を高める<br>Clarify each layer's role and enhance module independence |
| **FSMモデルからVerilog化への手順**<br>FSM Modeling to Verilog Flow | 状態遷移図 → ステートマシン → Verilog構造化<br>State transition → FSM diagram → Verilog implementation |
| **PID制御器のSoC統合設計**<br>SoC Integration of PID Controller | デジタル/アナログ選択とインターフェース設計<br>Digital/Analog choice and interface integration |
| **LLMとのソフト連携設計**<br>Software Integration with LLM | RISC-Vベースでのデータ受渡・I/O制御<br>Data exchange and I/O via RISC-V |
| **統合制御SoCの設計パターン理解**<br>Understanding SoC Design Patterns | 三層連携時の設計テンプレート習得<br>Mastering templates for integrated layered control |

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
