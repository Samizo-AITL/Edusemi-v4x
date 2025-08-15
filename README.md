---
layout: default
title: Edusemi-v4x/README.md  
---

---

# 🎓 **Edusemi-v4x｜半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/) 

--- 

## 🔗 公式リンク | Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![🌐 GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) | [![💻 GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| 🇺🇸 English | [![🌐 GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/en/) | [![💻 GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |

<div align="right">
  
![Last Update](https://img.shields.io/badge/Last%20Update-2025--08--15-orange)  
[![📄 ChangeLog](https://img.shields.io/badge/View-ChangeLog-blue?logo=markdown)](revision_history.md)  

</div>

---

## 📑 目次 | Table of Contents
1. [はじめに / Introduction](#-はじめに--introduction)
2. [プロジェクト概要 / Project Overview](#-プロジェクト概要--project-overview)
3. [基礎編 / Fundamentals](#-基礎編--fundamentals)
4. [応用編 / Applications](#-応用編--applications)
5. [実践編 / Practice](#-実践編--practice)
6. [特別編 / Special Topics](#-特別編--special-topics)
7. [関連プロジェクト / Related Projects](#-関連プロジェクト--related-projects)
8. [執筆者情報 / Author](#-執筆者情報--author)
9. [ライセンス / License](#-ライセンス--license)
10. [フィードバックと改訂履歴 / Feedback & ChangeLog](#-フィードバックと改訂履歴--feedback--changelog)
   
---

## ✍️ **はじめに | Introduction**

半導体技術は **トランジスタの発明** から始まり、**MOS構造** の登場によって急速に進化しました。  
*Semiconductor technology began with the **invention of the transistor**, and advanced rapidly with the advent of the **MOS structure**.*  

**微細化と集積化** はムーアの法則に沿って進み、LSIはあらゆる分野に浸透しています。  
*Miniaturization and integration progressed in line with Moore's Law, and LSIs have penetrated into all fields.*  

しかし、**物性・回路・プロセス・テスト** などの基礎分野は教育現場で分断されがちです。  
*However, in education, **fundamental areas such as device physics, circuit design, process technology, and testing** are often taught separately.*  

実務ではこれらは密接に関連しており、**回路はデバイス原理に依存し、設計はプロセスと信頼性に支えられています**。  
*In practice, these areas are deeply interconnected — **circuits depend on device principles, and designs are supported by process technology and reliability**.*  

**Edusemi** は、この「**基礎技術間の構造的つながり**」に焦点を当て、応用を見据えた **構造的理解** を育成する教材です。  
***Edusemi** focuses on this "**structural connection between fundamental technologies**" and fosters **structural understanding** with an eye toward applications.*  

> 💡 **Design follows physics, and productization follows verification.**  
> *💡 Design follows physics, and productization follows verification.*  
> *物性 → 回路 → 実装 → 検証* の接続を可視化します。  
> *Visualizing the flow: Physics → Circuits → Implementation → Verification*  

---

## 📘 **プロジェクト概要 | Project Overview**

**Edusemi-v4x** は、**設計・製造・検査・品質保証** を一貫して学べる **オープン教材** です。  
***Edusemi-v4x** is an *open educational resource* for learning **design, manufacturing, inspection, and quality assurance** in an integrated way.*  

- 🎯 **対象 / Target**：工学系学生・若手技術者・教育者  
  *🎯 Target: Engineering students, junior engineers, and educators*  
- ⭐ **特徴 / Features**：基礎のつながり重視、設計〜量産検査まで網羅  
  *⭐ Features: Emphasis on foundational connections, covering everything from design to mass-production testing*  
- 🧪 **実習 / Practice**：sky130・OpenLane・Python・GitHub・ChatGPT 対応  
  *🧪 Practice: Compatible with Sky130, OpenLane, Python, GitHub, and ChatGPT*  
---

## 🧭 **基礎編 | Fundamentals**
> 半導体の**物性・論理回路・プロセス技術**など、すべての応用の土台となる基礎領域を体系的に学びます。  
> *Covers semiconductor physics, logic design, and process fundamentals essential for all applications.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🧭 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter1_materials/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter1_materials) | 半導体物性とMOS構造の基礎<br>*Fundamentals of Semiconductor Physics and MOS Structure* | MOSトランジスタやCMOS回路設計の物理的基盤となる半導体物性を、バンド構造からCMOSインバータまで段階的に学ぶ。<br>*Learn the semiconductor physics underlying MOS transistors and CMOS circuit design, from band structure to CMOS inverters, step by step.* |
| 🧭 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter2_comb_logic/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter2_comb_logic) | デジタル論理と論理回路設計<br>*Digital Logic and Logic Circuit Design* | 基本論理ゲートから複合論理、MUXや加算器、FSM設計まで、CMOS論理回路設計の基礎を学ぶ。<br>*Covers the fundamentals of CMOS logic circuit design, from basic logic gates to complex logic, multiplexers, adders, and FSM design.* |
| 🧭 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter3_process_evolution/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter3_process_evolution) | プロセス技術と設計限界の理解<br>*Process Evolution and Design Limits in CMOS* | 0.5µmから90nmへのCMOS技術の進化と物理限界が回路設計に与える影響を体系的に学ぶ。<br>*Learn the evolution of CMOS technology from 0.5µm to 90nm and the impact of physical limits on circuit design.* |
| 🧭 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter4_mos_characteristics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter4_mos_characteristics) | MOSトランジスタ特性と設計基盤<br>*MOS Transistor Characteristics and Design Infrastructure* | MOSFETの物理・寸法・設計ルール・PDK構造を整理し、設計者視点での動作・信頼性・限界を理解する。<br>*Organize the physics, dimensions, design rules, and PDK structure of MOSFETs to understand their operation, reliability, and limits from a designer’s perspective.* |
| 🧭 **第5a章 / Chapter5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5a_spec_module_if/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5a_spec_module_if) | 仕様策定とIF設計<br>*Spec Definition & Interface Design* | 上流工程・モジュール選定・PoC接続。<br>*Covers upstream design, module selection, and PoC integration.* |
| 🧭 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5_soc_design_flow/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5_soc_design_flow) | SoC設計フローとEDAツール<br>*SoC Design Flows and EDA Tools* | SoC開発の全体フロー、標準セル設計と物理設計の接続点、STAやDFTなどの検証基礎を学ぶ。<br>*Learn the full SoC development flow, the connection points between standard cell and physical design, and the basics of STA and DFT verification.* |
| 🧭 **第6章 / Chapter6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter6_test_and_package/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter6_test_and_package) | テスト・パッケージ・製品化<br>*Test, Packaging, and Productization* | 製品品質を守る量産工程（検査・モニタリング・信頼性確認・出荷判定）を理解し、不良品の市場流出を防ぐ責任と実践を学ぶ。<br>*Understand mass production processes (inspection, monitoring, reliability checks, shipment decisions) to prevent defective products from reaching the market.* |
| 🧭 **第7章 / Chapter7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter7_design_review_and_org/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter7_design_review_and_org) | デザインレビューと開発組織連携<br>*Design Review and Cross-Functional Collaboration* | 半導体製品開発におけるDR（Design Review）の目的・構造・多部門協働の仕組みを体系的に理解する。<br>*Gain a systematic understanding of the purpose, structure, and cross-functional collaboration mechanisms of Design Reviews in semiconductor product development.* |

---

## 🧩 **応用編 | Applications**
> 半導体の応用技術や特殊設計領域を深く掘り下げ、実用レベルの設計力を養います。  
> *Delves into applied semiconductor technologies and specialized design fields to develop practical design skills.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🧩 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) | メモリ技術の構造と選定指針<br>*Memory Technologies – Structure and Selection Guidelines* | SRAM、DRAM、FeRAM、MRAM、NANDの構造と動作原理を理解し、速度・不揮発性・耐久性・面積効率・消費電力などの評価軸で比較できる力を養い、SoC設計での統合・選択・接続方法を学ぶ。<br>*Understand the structure and operation of SRAM, DRAM, FeRAM, MRAM, and NAND; learn to compare them based on speed, non-volatility, endurance, area efficiency, and power consumption; and master integration, selection, and connection methods in SoC design.* |
| 🧩 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter2_high_voltage_devices/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter2_high_voltage_devices) | 高耐圧デバイス<br>*High Voltage Devices* | HV-CMOSやLDMOSの構造・レイアウト設計技術を学び、パワー制御、センサインターフェース、高電圧ドライバ回路への応用を理解する。<br>*Learn the structure and layout design techniques of HV-CMOS and LDMOS devices, and understand their applications in power control, sensor interfaces, and high-voltage driver circuits.* |
| 🧩 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) | ESD設計<br>*ESD Protection Design* | 半導体ICにおけるESD信頼性リスクを理解し、保護素子構造、レイアウト戦略、試験規格、破壊解析などを体系的に学ぶ。<br>*Understand ESD reliability risks in semiconductor ICs, and systematically learn protection device structures, layout strategies, test standards, and failure analysis.* |
| 🧩 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter4_layout_optimization/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter4_layout_optimization) | レイアウト設計と最適化<br>*Layout Design and Optimization* | ICレイアウトにおける配置・配線・幾何構造の最適化により、性能・信頼性・製造適合性を確保する手法を学ぶ。<br>*Learn methods for optimizing placement, routing, and geometric structures in IC layouts to ensure performance, reliability, and manufacturability.* |
| 🧩 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) | アナログ／ミックスドシグナル<br>*Analog / Mixed-Signal Design* | AMS設計全体像を理解し、オペアンプ・コンパレータなどの基本回路からレイアウト設計、ノイズ対策、ADC/DACの混載課題まで学ぶ。<br>*Understand the overall scope of AMS design, from basic circuits such as op-amps and comparators to layout design, noise countermeasures, and integration challenges with ADC/DAC.* |
| 🧩 **第5a章 / Chapter5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5a_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5a_analog_mixed_signal) | 0.18µm AMS設計技法<br>*0.18µm AMS Design Techniques* | 0.18µm世代のAMS回路設計におけるばらつき・ノイズ・寄生要素対策を学び、幅広い電源電圧・周波数帯域に対応可能な設計手法を習得する。<br>*Learn countermeasures for variability, noise, and parasitics in 0.18µm AMS circuit design, and acquire techniques adaptable to a wide range of supply voltages and frequency bands.* |
| 🧩 **第5b章 / Chapter5b**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5b_ams_block_and_pdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5b_ams_block_and_pdk) | 製造技術で切り拓くアナログ差別化 — 1/fノイズ半減の実現<br>*Differentiated Analog Modules via Manufacturing Technology — Realizing 50% Reduction in 1/f Noise* | 製造工程を活用して1/fノイズを50%以上低減し、低ノイズMOS素子を実現する設計・製造戦略を学ぶ。<br>*Learn design and manufacturing strategies to leverage fabrication processes for reducing 1/f noise by over 50% and achieving low-noise MOS devices.* |
| 🧩 **第6章 / Chapter6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) | PDKとEDA環境<br>*PDK and EDA Environment* | PDKの構成要素、EDAツールとの連携、設計ルールチェック、プロセス互換性、BSIMモデルの関係を理解する。<br>*Understand the components of a PDK, its integration with EDA tools, design rule checking, process compatibility, and the relationship with BSIM models.* |
| 🧩 **第7章 / Chapter7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter7_automation_and_verification/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter7_automation_and_verification) | 自動化と実装検証技術<br>*Automation and Implementation Verification* | RTL設計から物理レイアウト検証までの自動化手法を学び、Lint、DRC、LVS、STAに加えてCI/CD検証フロー構築を習得する。<br>*Learn automation techniques from RTL design to physical layout verification, and master CI/CD verification flows alongside Lint, DRC, LVS, and STA.* |
| 🧩 **第8章 / Chapter8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) | FSM設計（有限状態機械）<br>*FSM Design (Finite State Machine)* | Moore型／Mealy型FSMの構造と動作原理を理解し、状態遷移図やVerilogによる3段階記述法を学ぶ。<br>*Understand the structure and operation of Moore and Mealy FSMs, and learn three-stage description methods in Verilog with state diagrams.* |
| 🧩 **第9章 / Chapter9**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) | PLLとクロック設計<br>*PLL and Clock Design* | PLLの動作原理からスキュー／ジッタ対策、クロックツリー設計までを体系的に学び、高精度クロック生成・配布の設計技術を習得する。<br>*Learn PLL principles, skew/jitter countermeasures, and clock tree design to acquire high-precision clock generation and distribution techniques.* |

---

## 🛠 **実践編 | Practice**
> Python自動化・Sky130実験・OpenLane設計など、実務に近い演習を通じてスキルを定着させます。  
> *Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design to solidify skills.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🛠 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) | Pythonによる自動化ツール群<br>*Python-Based Automation Tools for Semiconductor Design* | Sky130 PDKやOpenLaneフローと連携し、SPICEシミュレーション、信頼性モデル評価、レポート解析を自動化するPythonスクリプト群を構築する。<br>*Develop Python scripts to automate SPICE simulations, reliability model evaluations, and report analysis in conjunction with the Sky130 PDK and OpenLane flow.* |
| 🛠 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter2_sky130_experiments/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter2_sky130_experiments) | Sky130実験とSPICE特性評価<br>*Sky130 Experiments and SPICE-Based Characterization* | SkyWater Sky130 PDKを用いてMOS特性（Vg–Idカーブ、Vth抽出）、BTI/TDBB予測を行い、SPICEベースの設計検証を実施する。<br>*Use the SkyWater Sky130 PDK to evaluate MOS characteristics (Vg–Id curves, Vth extraction) and predict BTI/TDBB, performing SPICE-based design verification.* |
| 🛠 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter3_openlane_practice/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter3_openlane_practice) | OpenLaneによるデジタル設計実習<br>*Digital Design Practice Using OpenLane* | Verilog RTLからGDS生成までのLSI設計フローを体験し、合成・配置・配線・DRCなど各段階の目的とツールを理解する。<br>*Experience the LSI design flow from Verilog RTL to GDS generation, understanding the objectives and tools for synthesis, placement, routing, and DRC.* |
| 🛠 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter4_poc_spec_and_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter4_poc_spec_and_design) | PoC仕様書と設計展開<br>*PoC Specifications and Design Implementation* | Sky130 PDKを用いた最小限のPoC回路（FSM/MUX/Adder）を題材に、仕様作成からRTL設計・物理実装までのプロセスを体験する。<br>*Using minimal PoC circuits (FSM/MUX/Adder) with the Sky130 PDK, experience the process from specification creation to RTL design and physical implementation.* |
| 🛠 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter5_evaluation_and_report/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter5_evaluation_and_report) | 設計結果の評価とレポート<br>*Evaluation and Reporting of Design Results* | 実装したPoC回路に対して、シミュレーション結果、面積・タイミング評価、DRC/LVS解析、改善提案を行い、設計フィードバックを実践する。<br>*Evaluate implemented PoC circuits by analyzing simulation results, area/timing metrics, DRC/LVS checks, and propose improvements as part of the design feedback cycle.* |

---

## 📦 **特別編 | Special Topics**
> 先端ノード・チップレット・統合制御SoCなど、最先端テーマを扱います。  
> *Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 📦 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter1_finfet_gaa/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa) | 先端ノード技術（FinFET、GAA、CFET）<br>*Advanced Node Technologies – FinFET, GAA & CFET* | FinFET・GAA・CFET構造の物理特性・電気特性・設計影響を体系的に解説し、プレーナMOSの限界を超える先端CMOS技術を紹介する。<br>*Comprehensively explains the physical and electrical characteristics and design impacts of FinFET, GAA, and CFET structures, introducing advanced CMOS technologies beyond planar MOS limits.* |
| 📦 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2_chiplet_pkg/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg) | チップレットと先端パッケージ技術<br>*Chiplets and Advanced Packaging* | 2.5D/3D実装技術、TSV、異種集積によるチップレットアーキテクチャの設計・実装・信頼性を解説し、柔軟な設計とスケーラビリティを可能にする技術を学ぶ。<br>*Covers 2.5D/3D integration, TSV, and heterogeneous integration for chiplet architecture design, implementation, and reliability, enabling flexible design and scalability.* |
| 📦 **第2a章 / Chapter2a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk) | SystemDKにおける熱・応力・ノイズ制約の設計対応<br>*Design Handling of Thermal, Stress, and Noise Constraints in SystemDK* | System Design Kit (SystemDK)の概念を解説し、SI/PI、熱、応力、EMI/EMCといった物理制約を設計的に扱う手法を学ぶ。<br>*Explains the concept of SystemDK and methods for addressing physical constraints such as SI/PI, thermal, stress, and EMI/EMC in design.* |
| 📦 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | FSM×PID×LLMによる統合制御システムのSoC実装手法<br>*SoC Implementation of Integrated Control System with FSM × PID × LLM* | AITL-H三層制御アーキテクチャを基盤とし、機能分離・階層連携・SoC統合の手法を学習する。<br>*Based on the AITL-H three-layer control architecture, learn methods for functional separation, hierarchical collaboration, and SoC integration.* |
| 📦 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | FSM×PID×LLM制御系のOpenLane実装<br>*RTL-to-GDSII Implementation of FSM×PID×LLM Control System with OpenLane* | Sky130 PDKを用い、FSM・PID・統合SoCモジュールの配置配線（RTL-to-GDSII）を実践する。<br>*Using the Sky130 PDK, implement placement and routing (RTL-to-GDSII) for FSM, PID, and integrated SoC modules.* |
| 📦 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | PDKとレイアウト検証による物理整合とDFM設計指針<br>*Physical Verification and DFM Design Guidelines with PDK* | Sky130 PDKによるレイアウト検証を行い、量産性を考慮したDFM設計指針を習得する。<br>*Perform layout verification with the Sky130 PDK and acquire DFM design guidelines considering manufacturability.* |

---

## 🔗 **関連プロジェクト | Related Projects**
> Edusemiと連動し、制御理論・社会構造・先端技術を横断的に学べる姉妹プロジェクト群。  
> *Sister projects linked with Edusemi, covering control theory, socio-industrial structures, and advanced technologies.*

| 🌐 プロジェクト / Project | 概要 / Overview | 主な特徴・内容 / Key Features |
|---|---|---|
| ➕ **Edusemi-Plus**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-Plus/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-Plus) | 地政学・製品戦略・AI・量子・投資など、産業構造を読み解く応用教材<br>*Applied learning materials analyzing geopolitics, product strategy, AI, quantum, and investment.* | - Apple Silicon・CHIPS法・Cryo-CMOSの実例解説<br>- 技術だけでなく社会との接点や背景を探究 |
| 🎛️ **EduController**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) | 制御理論（PID・状態空間）からAI制御（NN・RL・LLM）まで網羅<br>*Covers control theory (PID, state-space) to AI control (NN, RL, LLM).* | - PoC設計・OpenLane制御実装との連動<br>- Pythonによる設計演習・RTL検証・FSM生成支援 |
| 🤖 **AITL-H**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) | FSM（本能）＋PID（理性）＋LLM（知性）の三層制御アーキテクチャ<br>*Three-layer control architecture: FSM (instinct) + PID (reason) + LLM (intelligence).* | - 人型ロボット・統合制御のPoC実装<br>- Edusemi特別編3・4章と構造的に連携 |


---

## 👤 **執筆者情報 | Author**
> 本教材の企画・執筆者。半導体・インクジェット分野での実務経験を持ち、教育と実装を融合した教材開発を行う。  
> *Author with professional background in semiconductors and inkjet actuators, creating materials integrating theory and practice.*

| 📌 項目 / Item | 内容 / Details |
|------|------|
| **氏名 / Name** | 三溝 真一（Shinichi Samizo）<br>*Shinichi Samizo* |
| **学歴 / Education** | 信州大学大学院 電気電子工学 修了<br>*M.S. in Electrical and Electronic Engineering, Shinshu University* |
| **経歴 / Career** | 元 セイコーエプソン株式会社 技術者（1997年〜）<br>*Former Engineer at Seiko Epson Corporation (since 1997)* |
| **経験領域 / Expertise** | 半導体デバイス（ロジック・メモリ・高耐圧混載）<br>*Semiconductor devices (logic, memory, high-voltage mixed integration)*<br>インクジェット薄膜ピエゾアクチュエータ<br>*Inkjet thin-film piezo actuators*<br>PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育<br>*Productization of PrecisionCore printheads, BOM management, and ISO training* |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---

## 📄 **ライセンス | License**
> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用。  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **コード（Code）** | [**MIT License**](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布が可能<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) または [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | 著者表示必須、継承条件あり（BY-SAの場合）<br>*Attribution required, share-alike for BY-SA* |
| **図表・イラスト（Figures & diagrams）** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ許可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

## 💬 **フィードバックと改訂履歴 | Feedback & ChangeLog**
> 改善提案や議論はGitHub Discussionsから、改訂履歴はChangeLogにて公開。  
> *Propose improvements via GitHub Discussions, and track updates in the ChangeLog.*

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)  
[![📄 ChangeLog](https://img.shields.io/badge/📄%20View-ChangeLog-orange?logo=markdown)](revision_history.md)

