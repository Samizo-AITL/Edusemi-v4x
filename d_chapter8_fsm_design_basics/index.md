---
layout: default
title: 応用編 第8章 FSM設計（有限状態機械）
---

---

# 🔁 応用編 第8章：FSM設計（有限状態機械）  
**Applied Chapter 8: FSM Design (Finite State Machine)** 

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) |

---

## 📘 概要｜Overview

FSM（Finite State Machine：有限状態機械）は、制御回路や通信プロトコルなど、  
**時間的な順序性を持つ動作**を記述するための基本的な設計手法です。

FSM is a fundamental design method used to describe **temporally ordered behaviors**,  
common in control logic, communication protocols, and embedded systems.

本章では、**状態遷移の基本概念**から、**Moore型／Mealy型の違い**、  
そして**Verilogでの3段構成によるFSM記述**までを段階的に学習します。

---

## 🧩 セクション構成｜Section Structure

| ファイル名｜Filename | 内容｜Contents |
|----------------------|------------------------------|
| [`fsm_overview.md`](fsm_overview.md) | FSMの基本概念、分類（Moore / Mealy）<br>Basics and classification of FSM |
| [`fsm_state_transition.md`](fsm_state_transition.md) | 状態遷移図・状態遷移表の記法<br>State diagrams and state tables |
| [`fsm_hdl_description.md`](fsm_hdl_description.md) | VerilogによるFSMの3段階記述法<br>Three-stage FSM coding in Verilog |

---

## 🎯 到達目標｜Learning Objectives

- FSMの**構造と動作原理**を理解する  
  Understand the **structure and operation** of FSMs  
- 状態遷移図・状態遷移表を**自分で設計できる**  
  Be able to design **state diagrams and tables**  
- FSMを**Verilogで正しく記述できる**（3段構成）  
  Write correct FSMs in **three-part Verilog HDL**  
- **Moore型とMealy型**の違いを説明できる  
  Distinguish between **Moore and Mealy types**

---

## 📚 関連章リンク｜Related Chapters

FSMは以下の基礎章と深く関連しています：  
FSM is tightly connected with the following fundamental chapters:

- [📘 第2章 デジタル論理と論理回路設計｜Chapter 2: Digital Logic Design](../chapter2_comb_logic/README.md)  
  ↳ 組み合わせ論理と順序論理の接続点としてFSMを導入  
  ↳ FSM is introduced as the bridge between combinational and sequential logic  

- [📘 第5章 SoC設計フローとEDAツール｜Chapter 5: SoC Design Flow and EDA](../chapter5_soc_design_flow/README.md)  
  ↳ FSMはRTL設計の一部として論理合成に活用される  
  ↳ FSMs are synthesized as part of RTL design for SoCs

---

## 🛠 応用展開例（今後追加予定）｜Planned Extensions

- UART / I2C プロトコルを用いたFSM制御設計例  
  FSMs applied to UART / I2C protocol controllers  
- YosysFSM や Xilinx FSM Editor 等との統合  
  Integration with FSM generation tools (YosysFSM, Xilinx FSM Editor)  
- 状態遷移ログの自動チェックやAssertionとの連携  
  Automatic log checking and assertion-based verification

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
**🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)**

