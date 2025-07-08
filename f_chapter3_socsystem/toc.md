# 📘 特別編 第3章：FSM×PID×LLMによる統合制御システムのSoC実装手法

本章では、FSM（Finite State Machine）、PID制御、LLM（Large Language Model）という三層制御アーキテクチャを統合したSoC実装手法を解説します。

---

## 📑 章目次

| 節番号 | 節タイトル | 概要 |
|--------|-------------|------|
| [3.1](docs/3_1_aitl_architecture.md) | AITL-Hアーキテクチャと層分離設計 | 三層制御（FSM・PID・LLM）の設計原理と役割分離 |
| [3.2](docs/3_2_fsm_design.md) | FSM設計とRTLモジュール構成 | 行動モデルを状態機械としてRTL化する手法 |
| [3.3](docs/3_3_pid_design.md) | PID制御のASIC実装（デジタル／アナログ） | PID制御器のRTL実装とFSMとの連携構成 |
| [3.4](docs/3_4_llm_interface.md) | LLMとの接続設計（RISC-V・I/O連携） | LLM層とFSM・PIDの接続インターフェース設計 |
| [3.5](docs/3_5_soc_integration.md) | SoC統合とバス構造・通信設計 | 各モジュールを統合するSoCトップ設計 |
| [3.6](docs/3_6_case_study.md) | ケーススタディ：三層制御によるPoC実装例 | 倒立振子・ロボット制御の実装例と評価視点 |

---

## 🔗 関連リンク

- [章トップ README.md](README.md)
- [PoC仕様書（AITL-H/PoC）](https://github.com/Samizo-AITL/AITL-H/tree/main/docs)
- [FSM・PIDコード実装（AITL-H/implementary）](https://github.com/Samizo-AITL/AITL-H/tree/main/implementary)
- [AITL-H構想解説（AITL-H/theory）](https://github.com/Samizo-AITL/AITL-H/tree/main/theory)

---
