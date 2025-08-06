---
layout: default
title: 基礎編　第4章｜MOSトランジスタ特性と設計基盤
---

# 📘 基礎編 第4章 : MOSトランジスタ特性と設計基盤  
**Fundamentals-Chapter 4: MOS Transistor Characteristics and Design Infrastructure**

---

## 🔄 前章との接続｜Connection to Previous Chapter

| 日本語 – Japanese                                                                                  | English – English                                                                                  |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| 第3章では、微細化によるプロセス限界と信頼性課題を整理しました。                                     | Chapter 3 examined **process limits and reliability challenges** under scaling.                     |
| 本章では、それを受けて「設計者が実際に扱うMOSトランジスタ」の物理・寸法・設計ルール・PDKを体系的に整理します。 | Here, we focus on **the MOSFET as handled by designers**, and clarify its physical, dimensional, and PDK-based structure. |

➡️ [📘 **第3章：プロセス技術と設計限界の理解**](../chapter3_process_evolution/README.md) に戻る  
➡️ [📘 **Chapter 3: Process Evolution and Design Limits in CMOS**](../chapter3_process_evolution/README.md) (EN)

---

## 🎯 章のねらい｜Chapter Objectives

| 日本語 – Japanese                                                                                         | English – English                                                                                   |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| - MOSトランジスタの**動作・信頼性・寸法ルール**を設計者視点で体系的に理解する                                      | - Understand **MOS operation, reliability, and design rules** from a design perspective.            |
| - PDKに含まれる**ルール・モデル・保証値**が、どのような物理的背景から導かれるかを学ぶ                              | - Learn how **PDK rules, models, and reliability guarantees** stem from physical effects.           |
| - **sky130や0.18µm**といった教育向けプロセスを通じて、設計・評価の接続点を体感する                                  | - Use **sky130/0.18µm** educational processes to experience the design-evaluation link.             |
| - **寿命や限界電圧の物理的起源（TDDB、Qbdなど）**を理解し、設計限界の根拠をつかむ                                 | - Understand **physical origins of design limits** (e.g., TDDB, Qbd) for reliability.               |

---

## 📚 節構成｜Chapter Structure

| No. | セクション名（日本語）                                                                 | Section Title (English)                                                   | リンク |
|-----|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|--------|
| 4.1 | 教材としてのMOS寸法と対象プロセス<br>_MOS Dimensions and Target Processes_             | Meaning of device scaling in sky130 and 0.18µm educational processes      | [📎](4.1_mos_dimension_and_target.md) |
| 4.2 | MOSトランジスタの動作原理と特性<br>_MOS Operation and Key Characteristics_             | Threshold voltage, Id-Vg, gm, subthreshold slope                          | [📎](4.2_mos_characteristics.md) |
| 4.3 | 個別信頼性（BTI, HCIなど）<br>_Device Reliability (BTI, HCI, etc.)_                    | Bias Temperature Instability, Hot Carrier Injection, aging effects       | [📎](4.3_reliability_effects.md) |
| 4.3a| ゲート酸化膜の信頼性評価（TDDB／Qbd）<br>_Gate Oxide Reliability (TDDB, Qbd, TZDB)_    | CDF, bathtub curves, breakdown modes (A/B/C), dielectric lifetime         | [📎](4.3a_gate_oxide_reliability.md) |
| 4.4 | デザインルールと寸法規則の意味<br>_Meaning Behind Design Rules_                        | Why rules exist: process margin, lithography, yield limits               | [📎](4.4_design_rules.md) |
| 4.5 | PDKと設計基盤の構築（sky130を中心に）<br>_PDK and Design Infrastructure (sky130)_     | Structure of PDK: models, rules, libraries, layout & DRC integration      | [📎](4.5_pdk_and_design_infra.md) |
4.6 | LDD構造と短チャネル効果（SCE）<br>_LDD Structure and Short Channel Effects (SCE)_      | Electric field relaxation, hot carrier suppression, Vth roll-off          | [📎](4.6_LDD_and_SCE.md) |
| 4.7 | パンチスルー対策技術<br>_Punch-Through Suppression Techniques_                          | Halo implant, well design, Vbs control, lateral barrier reinforcement     | [📎](4.7_Punchthrough.md) |
| 4.8 | 短チャネルMOSの限界とFinFET構造<br>_Scaling Limits of Short-Channel MOS and FinFET Architecture_ | Physical limits of planar CMOS, basic FinFET structure, control improvement | [📎](4.8_scaling_limits_and_finfet.md) |

---

## 🔜 次章への導入｜Lead-in to Next Chapter

| 日本語 – Japanese                                                                                          | English – English                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 次章（第5章）では、本章で扱った**PDKや設計ルールの知識**を活用し、**SoC設計フローとEDAツール**の実践に進みます。 | Chapter 5 builds on this by applying **PDK knowledge and design rules** to **SoC design flows and EDA tools**. |
| PDKの読み解きや、信頼性モデルの物理的裏付けは、ツールを用いた設計と検証の前提になります。                        | Understanding **PDK structures and reliability modeling** is foundational for successful digital/analog design. |

➡️ [📘 **第5章：SoC設計フローとEDAツール**](../chapter5_soc_design_flow/README.md) に進む  
➡️ [📘 **Chapter 5: SoC Design Flows and EDA Tools**](../chapter5_soc_design_flow/README.md) (EN)

---

## 🧩 章のキーワード｜Keywords

```
MOSFET, Vth, Id-Vg, gm, Subthreshold, BTI, HCI, TDDB, Qbd, Design Rule, PDK, sky130, 0.18µm
```

---

## 📌 補足情報｜Supplement

- sky130 PDK: [https://skywater-pdk.readthedocs.io](https://skywater-pdk.readthedocs.io)  
- Open-source EDA tools: Magic, Xyce, KLayout, Ngspice, OpenROAD  
- Reliability references: JEDEC JESD 61-A, TDDB models, Weibull analysis  

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
