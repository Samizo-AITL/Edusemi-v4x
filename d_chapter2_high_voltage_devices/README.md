# ⚡ 応用編 第2章｜Chapter 2: 高耐圧デバイス｜High Voltage Devices

---

## 📘 概要｜Overview

本章では、SoCやアナログ混載LSIにおいて不可欠な  
**高耐圧デバイス（High Voltage Devices）** の構造と設計技術について学びます。  
代表的なデバイスには、**HV-CMOS（High Voltage CMOS）** や **LDMOS（Lateral Diffused MOS）** があり、  
通常のCMOSに比べて **高電圧印加への耐性** を持ち、以下のような用途に活用されます：

- **パワー制御（Power Control）**
- **センサ入力（Sensor Interface）**
- **高電圧駆動（Level Shifting / Driver）**

設計においては、**電界集中の緩和・寄生素子の抑制・レイアウト最適化** といった  
微細かつ高信頼性が要求されるノウハウが重要です。

---

## 🗂️ セクション構成｜Section Structure

| ファイル名｜Filename | 内容概要｜Description | 耐圧範囲｜Voltage Rating |
|------------------------|-------------------------------------------------------------|-------------------------|
| [`hvcmos.md`](./hvcmos.md) | **HV-CMOS設計**：標準CMOSとの互換性を維持した高耐圧技術<br>**HV-CMOS Design** – CMOS-compatible high-voltage integration | 約10V〜40V<br>~10V to 40V |
| [`ldmos.md`](./ldmos.md) | **LDMOS構造と動作**：高電圧・高電流用途の基本構造とドリフト領域設計<br>**LDMOS Devices** – High-voltage/high-current MOS with lateral drift extension | 約20V〜100V以上<br>~20V to 100V+ |
| [`junction_isolation.md`](./junction_isolation.md) | **接合絶縁技術**：寄生トランジスタとリーク防止のための絶縁構造<br>**Junction Isolation** – Structure and biasing against latch-up and leakage | — |
| [`dvdt.md`](./dvdt.md) | **dv/dt耐性とデバイス破壊**：急峻な電圧変化による電界破壊とその対策<br>**dv/dt Immunity** – Prevention of avalanche breakdown by transient voltage | — |
| [`layout_rules.md`](./layout_rules.md) | **高耐圧デバイスのレイアウト工夫**：ガードリングやCMPダミーの配置ルール<br>**Layout Guidelines** – Guard rings, dummy fills, and reliability-aware layout | — |

---

## 🎯 対象読者｜Target Audience

- 高耐圧デバイスの**基礎構造と応用例**を理解したい初学者  
  *Beginners seeking fundamental understanding of HV devices*
- アナログ混載設計やPMIC開発に関心のある若手技術者  
  *Junior engineers working on analog/mixed-signal or PMIC*
- センサ入力・電源・駆動回路などの**I/O設計担当者**  
  *Designers working on sensor input, power I/O, and driver circuits*

---

## 🎯 本章の到達目標｜Learning Objectives

- ✅ **HV-CMOSおよびLDMOSの構造と動作原理**を理解する  
  *Understand the structure and operation of HV-CMOS and LDMOS*
- ✅ **寄生素子や接合絶縁**を意識したレイアウト設計に慣れる  
  *Design layouts with awareness of parasitic elements and isolation*
- ✅ **電圧印加時の破壊モードと対策**を学ぶ  
  *Prevent HV-induced failures through robust device design*

---

## 🔗 関連リンク・参照章｜Related Chapters

- 📘 [応用編 第1章｜メモリ技術｜Memory Technologies](../d_chapter1_memory_technologies/README.md)  
  組込みSRAMと高耐圧I/Oドライバ設計の接続  
  *Embedded SRAM with HV I/O driver integration*

- 📘 [応用編 第5章｜アナログ・ミックスドシグナル設計](../d_chapter5_analog_mixed_signal/README.md)  
  高電圧ブロックとの回路接続と設計視点  
  *Connectivity to HV analog blocks and design insights*

- 📘 [基礎編 第4章｜MOSトランジスタ特性](../chapter4_mos_characteristics/README.md)  
  MOS構造と短チャネル効果、寄生素子理解の基礎  
  *MOS fundamentals including short-channel effects and parasitics*

---

## 🏁 備考｜Note

- 本章は **Edusemi 応用編** の一部であり、実装指向・設計実務の観点から構成されています。  
  *This chapter is part of Edusemi Advanced Edition, focusing on practical and implementation-level perspectives.*

---

© 2025 Shinichi Samizo / MIT License  
🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---
