# 🧠 FSM×PID×LLMによる統合制御システムのSoC実装手法

本章では、**AITL-H構想（FSM・PID・LLMによる三層制御）**をベースに、  
その統合制御システムを**SoCとして設計・実装**する手法を解説します。

---

## 🎯 目的と概要

- **FSM（状態制御）**
- **PID（安定化制御）**
- **LLM（知的判断・外部連携）**

という三層制御構造を、ASIC/SoC上で物理的に接続・実装する際の、
**モジュール設計・接続手法・インターフェース戦略**を体系的に学びます。

---

## 📚 章構成

| 節 | 内容 |
|----|------|
| 3.1 | AITL-Hアーキテクチャと層分離設計 |
| 3.2 | FSM設計とRTLモジュール構成 |
| 3.3 | PID制御のASIC実装（デジタル／アナログ） |
| 3.4 | LLMとの接続設計（RISC-V・I/O連携） |
| 3.5 | SoC統合とバス構造・通信設計 |
| 3.6 | ケーススタディ：三層制御によるPoC実装例 |

---

## 🧬 各層の役割と実装

| 層 | 役割 | 実装対象 |
|----|------|----------|
| FSM | 本能的制御・行動遷移 | Verilog RTL（`fsm_engine.v`） |
| PID | 安定化・物理制御 | Verilog or Mixed-Signal（`pid_controller.v`） |
| LLM | 知的判断・外部応答 | RISC-Vソフト連携（`llm_interface.c`） |

---

## 🛠 実装ディレクトリ構成（例）
```
f_chapter3_socsystem/
├── docs/                 # 解説Markdown
├── verilog/              # FSM, PID RTLコード
├── sw_riscv/             # LLM連携制御コード
├── integration/          # SoC統合設計（通信バス、トップ設計）
├── testbench/            # 検証用環境
└── README.md             # ← 本ファイル
```

---

## 📘 参照リンク（AITL-H連携）

- [AITL-H構想（theory/）](https://github.com/Samizo-AITL/AITL-H/tree/main/theory)
- [PoC設計マニュアル](https://github.com/Samizo-AITL/AITL-H/tree/main/docs)
- [FSMエンジン実装例](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/fsm_engine/fsm_engine.py)
- [LLM連携ソフト実装例](https://github.com/Samizo-AITL/AITL-H/blob/main/implementary/llm_interface.py)

> ※本章は Edusemi 特別編として、AITL-H実装との連携を前提としています。

---

## 🎓 学習目標

- 三層制御（FSM×PID×LLM）の責務分離と再利用設計
- FSMの状態モデルからVerilog化への手順
- PID制御器のSoC統合とアナログ/デジタル選択
- LLM接続におけるソフト制御連携設計（RISC-V連動）
- 統合制御システムのSoC実装における設計パターン

---

## 📎 ライセンスと作者情報

- 本教材は MIT ライセンスで公開されています  
- 制作者：三溝 真一（Shinichi Samizo）  
- GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)

---
