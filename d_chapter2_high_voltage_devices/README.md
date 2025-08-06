---
layout: default
title: 応用編  第2章　高耐圧デバイス 
---

# ⚡ 応用編  第2章　高耐圧デバイス
**Applied Chapter 2 High Voltage Devices**

---

## 📘 概要｜Overview

本章では、SoCやアナログ混載LSIにおいて不可欠な  
**高耐圧デバイス（High Voltage Devices）** の構造と設計技術について学びます。  
代表的なデバイスには、**HV-CMOS（High Voltage CMOS）** や **LDMOS（Lateral Diffused MOS）** があり、  
通常のCMOSに比べて **高電圧印加への耐性** を持ち、以下のような用途に活用されます：

- **パワー制御｜Power Control**
- **センサ入力｜Sensor Interface**
- **高電圧駆動｜Level Shifting / Driver**

設計においては、**電界集中の緩和・寄生素子の抑制・レイアウト最適化** といった  
微細かつ高信頼性が要求されるノウハウが重要です。

> This chapter covers **device structures and layout design** for HV-CMOS and LDMOS,  
> essential for power interface, sensor input, and high-voltage driver circuits in SoC and analog LSI.

---

## 🗂️ セクション構成｜Section Structure

| 📄 ファイル名｜Filename | 📘 内容概要｜Description | ⚡ 耐圧範囲｜Voltage Rating |
|----------------------------|-------------------------------------------------------------|---------------------------|
| [`hvcmos.md`](./hvcmos.md) | **HV-CMOS設計**：標準CMOSとの互換性を維持した高耐圧技術<br>**HV-CMOS Design** – CMOS-compatible high-voltage integration | 約10V〜40V<br>~10V to 40V |
| [`ldmos.md`](./ldmos.md) | **LDMOS構造と動作**：高電圧・高電流用途の基本構造とドリフト領域設計<br>**LDMOS Devices** – High-voltage/high-current MOS with lateral drift extension | 約20V〜100V以上<br>~20V to 100V+ |
| [`junction_isolation.md`](./junction_isolation.md) | **接合絶縁技術**：寄生トランジスタとリーク防止のための絶縁構造<br>**Junction Isolation** – Structure and biasing against latch-up and leakage | ― |
| [`dvdt.md`](./dvdt.md) | **dv/dt耐性とデバイス破壊**：急峻な電圧変化による電界破壊とその対策<br>**dv/dt Immunity** – Prevention of avalanche breakdown by transient voltage | ― |
| [`layout_rules.md`](./layout_rules.md) | **高耐圧デバイスのレイアウト工夫**：ガードリングやCMPダミーの配置ルール<br>**Layout Guidelines** – Guard rings, dummy fills, and reliability-aware layout | ― |

---

## 🎯 対象読者｜Target Audience

- 🎓 **高耐圧デバイスの基礎構造と応用例を理解したい初学者**  
  *Beginners seeking fundamental understanding of HV devices*

- 👨‍🔧 **アナログ混載設計やPMIC開発に関心のある若手技術者**  
  *Junior engineers working on analog/mixed-signal or PMIC*

- 🔌 **センサ入力・電源・駆動回路などのI/O設計担当者**  
  *Designers involved in sensor, power, and driver I/O circuits*

---

## 🎯 本章の到達目標｜Learning Objectives

| ✅ 到達目標｜Objectives | 説明｜Details |
|---------------------------|----------------|
| HV-CMOS / LDMOSの構造理解<br>Understand HV-CMOS and LDMOS | 動作原理と構造の違いを把握し、用途ごとの選択が可能となる |
| 寄生素子と絶縁設計の習得<br>Design against parasitic effects | サブストレートカップリングやラッチアップの回避方法を理解 |
| 耐圧と信頼性確保の実装技術<br>Reliability-aware HV design | dv/dt破壊やレイアウト最適化による製品歩留まり向上 |

---

## 🔗 関連リンク｜Related Topics

- [📘 応用編 第2章｜高耐圧デバイス 全体README](../d_chapter2_high_voltage_devices/README.md)  
  **章全体の構成と関連技術の導入**  
  *Chapter 2 Top: Overview of high-voltage devices and structure of this section*

- [`hvcmos.md`](./hvcmos.md)  
  **CMOSプロセス互換での高耐圧化技術**  
  *High-voltage CMOS with process compatibility*

- [`ldmos.md`](./ldmos.md)  
  **LDMOSによる高電流対応技術**  
  *LDMOS for high-current, high-voltage applications*

- [`junction_isolation.md`](./junction_isolation.md)  
  **寄生素子を防ぐ絶縁設計**  
  *Isolation to prevent parasitic transistors*

- [`layout_rules.md`](./layout_rules.md)  
  **CMPとガードリングの最適設計指針**  
  *CMP-aware layout and guard ring design*

- [chapter5_soc_design_flow](../chapter5_soc_design_flow/)  
  **SoC設計フローと高耐圧ブロック統合**  
  *SoC design flow with HV IP block integration*

---

## 🏁 備考｜Note

- 本章は **Edusemi 応用編** の一部であり、**高信頼・実装指向**の教育を重視しています。  
  *This chapter is part of Edusemi Advanced Edition, focused on reliability-aware, implementation-level education.*

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)

---
