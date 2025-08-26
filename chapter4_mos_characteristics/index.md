---
layout: default
title: 基礎編　第4章｜MOSトランジスタ特性と設計基盤　　
---

---

# 📘 基礎編 第4章 : MOSトランジスタ特性と設計基盤  
**Fundamentals-Chapter 4: MOS Transistor Characteristics and Design Infrastructure**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter4_mos_characteristics/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter4_mos_characteristics) |

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

## 📎 関連付録｜Related Appendix

- [付録B1: 0.18µm / 0.13µm MOSトランジスタ基礎特性](appendix_b1_018um_013um_mos_basics.md)  
  Representative parameters, characteristic graphs (educational model), and BSIM3 simulation package link.

---

## 🔜 次章への導入｜Lead-in to Next Chapter

| 日本語 – Japanese                                                                                          | English – English                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 次章（第5a章）では、本章で扱った**PDKや設計ルールの知識**を基に、**SoC設計の上流工程（仕様策定・モジュール選定・IF設計）**に進みます。 | Chapter 5a builds on this by applying **PDK knowledge and design rules** to the **upstream stages of SoC design (specification, module selection, interface design)**. |
| ここで整理した寸法・特性・制約の理解が、上流での仕様決定やモジュール構成、IF設計の前提となります。                  | The understanding of dimensions, characteristics, and constraints gained here forms the basis for upstream specification decisions, module configurations, and interface design. |

➡️ [📘 **第5a章：仕様策定・モジュール選定・インターフェース設計**](../chapter5a_spec_module_if/README.md) に進む  
➡️ [📘 **Chapter 5a: Specification, Module Selection, and Interface Design**](../chapter5a_spec_module_if/README.md) (EN)

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

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)
