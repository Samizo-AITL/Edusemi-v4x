---
layout: default
title: Edusemi-v4x/index.md
---

# 🎓 **Edusemi-v4x｜半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*

---

## 🔗 公式リンク | Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![🌐 GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) | [![💻 GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| 🇺🇸 English | [![🌐 GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/en/) | [![💻 GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |

---

## 📑 **目次 | Table of Contents**

1. [✍️ はじめに / Introduction](#-はじめに--introduction)
2. [📘 プロジェクト概要 / Project Overview](#-プロジェクト概要--project-overview)
3. [🧭 基礎編 / Fundamentals](#-基礎編--fundamentals)
4. [🧩 応用編 / Applications](#-応用編--applications)
5. [🛠 実践編 / Practice](#-実践編--practice)
6. [📦 特別編 / Special Topics](#-特別編--special-topics)
7. [🔗 関連プロジェクト / Related Projects](#-関連プロジェクト--related-projects)
8. [👤 執筆者情報 / Author](#-執筆者情報--author)
9. [📄 ライセンス / License](#-ライセンス--license)
10. [💬 フィードバック / Feedback](#-フィードバック--feedback)

---

## ✍️ **はじめに | Introduction**

半導体技術は **トランジスタの発明** に始まり、**MOS構造** によって飛躍的に発展しました。  
*Semiconductor technology began with the **invention of the transistor** and advanced rapidly with the **MOS structure**.*

**微細化と高集積化** はムーアの法則に沿って進み、LSIは社会のあらゆる分野を支えています。  
*Driven by Moore’s Law, miniaturization and integration have made LSIs ubiquitous.*

一方で、教育現場では **物性・回路・プロセス・テスト** が分断して教えられることが少なくありません。  
*However, education often treats **device physics, circuits, processes, and testing** as separate topics.*

実務では、これらは不可分です。  
**回路はデバイス原理に依存し、設計はプロセスと信頼性に支えられています。**  
*In practice, circuits depend on device physics, and designs are grounded in process technology and reliability.*

**Edusemi** は、こうした **基礎技術のつながり** を軸に、応用につながる **構造的理解** を育てる教材です。  
***Edusemi** focuses on the **structural connections between fundamentals**, fostering understanding that leads to real applications.*

> 💡 **Design follows physics. Productization follows verification.**  
> *物性 → 回路 → 実装 → 検証* の流れを可視化します。  
> *Visualizing the flow: Physics → Circuits → Implementation → Verification*

---

## 📘 **プロジェクト概要 | Project Overview**

**Edusemi-v4x** は、**設計・製造・検査・品質保証** を一貫して学ぶための **オープン教材** です。  
***Edusemi-v4x** is an *open educational resource* for integrated learning of **design, manufacturing, testing, and quality assurance**.*

- 🎯 **対象 / Target**  
  工学系学生・若手技術者・教育者  
  *Engineering students, junior engineers, and educators*

- ⭐ **特徴 / Features**  
  基礎のつながりを重視し、設計から量産検査までを体系化  
  *Emphasizes foundational connections, from design to mass-production testing*

- 🧪 **実習 / Practice**  
  Sky130 / OpenLane / Python / GitHub / ChatGPT  
  *Hands-on practice with Sky130, OpenLane, Python, GitHub, and ChatGPT*
  
---

## 🧭 **基礎編 | Fundamentals**
> 半導体の**物性・論理回路・プロセス技術**など、すべての応用の土台となる基礎領域を体系的に学びます。  
> *Covers semiconductor physics, logic design, and process fundamentals essential for all applications.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🧭 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter1_materials/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter1_materials) | **半導体物性とMOS構造の基礎**<br>*Fundamentals of Semiconductor Physics and MOS Structure* | **MOSトランジスタ・CMOS回路設計の物理基盤**を、バンド構造からCMOSインバータまで段階的に学ぶ。<br>*Learn the semiconductor physics underlying MOS transistors and CMOS circuit design, from band structure to CMOS inverters, step by step.* |
| 🧭 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter2_comb_logic/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter2_comb_logic) | **デジタル論理と論理回路設計**<br>*Digital Logic and Logic Circuit Design* | **基本論理ゲート・複合論理・MUX・加算器・FSM設計**を通じて、CMOS論理回路設計の基礎を学ぶ。<br>*Covers the fundamentals of CMOS logic circuit design, from basic logic gates to complex logic, multiplexers, adders, and FSM design.* |
| 🧭 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter3_process_evolution/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter3_process_evolution) | **プロセス技術と設計限界の理解**<br>*Process Evolution and Design Limits in CMOS* | **CMOS微細化・物理限界・設計制約**が回路設計に与える影響を、0.5µmから90nm世代まで体系的に学ぶ。<br>*Learn the evolution of CMOS technology from 0.5µm to 90nm and the impact of physical limits on circuit design.* |
| 🧭 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter4_mos_characteristics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter4_mos_characteristics) | **MOSトランジスタ特性と設計基盤**<br>*MOS Transistor Characteristics and Design Infrastructure* | **MOSFETの物理・寸法・設計ルール・PDK構造**を整理し、設計者視点での動作・信頼性・限界を理解する。<br>*Organize the physics, dimensions, design rules, and PDK structure of MOSFETs to understand their operation, reliability, and limits from a designer’s perspective.* |
| 🧭 **第5a章 / Chapter5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5a_spec_module_if/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5a_spec_module_if) | **仕様策定とIF設計**<br>*Spec Definition & Interface Design* | **上流工程・仕様策定・モジュール選定・PoC接続**を通じて、SoC設計の出発点を学ぶ。<br>*Covers upstream design, specification definition, module selection, and PoC integration.* |
| 🧭 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5_soc_design_flow/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5_soc_design_flow) | **SoC設計フローとEDAツール**<br>*SoC Design Flows and EDA Tools* | **SoC開発フロー・標準セル設計・物理設計・STA・DFT**など、量産設計に必要な基礎を体系的に学ぶ。<br>*Learn the full SoC development flow, the connection points between standard cell and physical design, and the basics of STA and DFT verification.* |
| 🧭 **第6章 / Chapter6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter6_test_and_package/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter6_test_and_package) | **テスト・パッケージ・製品化**<br>*Test, Packaging, and Productization* | **検査・モニタリング・信頼性確認・出荷判定**を通じて、量産品質と市場責任を理解する。<br>*Understand mass production processes (inspection, monitoring, reliability checks, shipment decisions) to prevent defective products from reaching the market.* |
| 🧭 **第7章 / Chapter7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter7_design_review_and_org/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter7_design_review_and_org) | **デザインレビューと開発組織連携**<br>*Design Review and Cross-Functional Collaboration* | **Design Review（DR）・多部門協働・組織連携構造**を理解し、半導体製品開発の実務を俯瞰する。<br>*Gain a systematic understanding of the purpose, structure, and cross-functional collaboration mechanisms of Design Reviews in semiconductor product development.* |

---

## 🧩 **応用編 | Applications**
> 半導体の応用技術や特殊設計領域を深く掘り下げ、実用レベルの設計力を養います。  
> *Delves into applied semiconductor technologies and specialized design fields to develop practical design skills.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🧩 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) | **メモリ技術の構造と選定指針**<br>*Memory Technologies – Structure and Selection Guidelines* | **SRAM・DRAM・FeRAM・MRAM・NAND**の構造と動作原理を理解し、速度・不揮発性・耐久性・面積効率・消費電力の評価軸で比較し、**SoC設計における統合・選択・接続方法**を学ぶ。<br>*Understand the structure and operation of SRAM, DRAM, FeRAM, MRAM, and NAND; learn to compare them based on speed, non-volatility, endurance, area efficiency, and power consumption; and master integration, selection, and connection methods in SoC design.* |
| 🧩 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter2_high_voltage_devices/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter2_high_voltage_devices) | **高耐圧デバイス**<br>*High Voltage Devices* | **HV-CMOS・LDMOS**の構造とレイアウト設計技術を学び、**パワー制御・センサIF・高電圧ドライバ回路**への応用を理解する。<br>*Learn the structure and layout design techniques of HV-CMOS and LDMOS devices, and understand their applications in power control, sensor interfaces, and high-voltage driver circuits.* |
| 🧩 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) | **ESD設計**<br>*ESD Protection Design* | **ESD信頼性リスク・保護素子構造・レイアウト戦略・試験規格・破壊解析**を体系的に学び、ICの信頼性設計力を養う。<br>*Understand ESD reliability risks in semiconductor ICs, and systematically learn protection device structures, layout strategies, test standards, and failure analysis.* |
| 🧩 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter4_layout_optimization/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter4_layout_optimization) | **レイアウト設計と最適化**<br>*Layout Design and Optimization* | **配置・配線・幾何構造の最適化**により、**性能・信頼性・製造適合性（DFM）**を確保する設計手法を学ぶ。<br>*Learn methods for optimizing placement, routing, and geometric structures in IC layouts to ensure performance, reliability, and manufacturability.* |
| 🧩 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) | **アナログ／ミックスドシグナル**<br>*Analog / Mixed-Signal Design* | **オペアンプ・コンパレータ**などの基本回路から、**レイアウト設計・ノイズ対策・ADC/DAC混載課題**まで、AMS設計全体像を学ぶ。<br>*Understand the overall scope of AMS design, from basic circuits such as op-amps and comparators to layout design, noise countermeasures, and integration challenges with ADC/DAC.* |
| 🧩 **第5a章 / Chapter5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5a_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5a_analog_mixed_signal) | **0.18µm AMS設計技法**<br>*0.18µm AMS Design Techniques* | **ばらつき・ノイズ・寄生要素対策**を中心に、**広い電源電圧・周波数帯域**に対応可能なAMS設計手法を習得する。<br>*Learn countermeasures for variability, noise, and parasitics in 0.18µm AMS circuit design, and acquire techniques adaptable to a wide range of supply voltages and frequency bands.* |
| 🧩 **第5b章 / Chapter5b**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5b_ams_block_and_pdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5b_ams_block_and_pdk) | **製造技術で切り拓くアナログ差別化**<br>*Differentiated Analog Modules via Manufacturing Technology* | **1/fノイズ50%以上低減**を実現するための、**低ノイズMOS素子設計・製造プロセス活用戦略**を学ぶ。<br>*Learn design and manufacturing strategies to leverage fabrication processes for reducing 1/f noise by over 50% and achieving low-noise MOS devices.* |
| 🧩 **第6章 / Chapter6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) | **PDKとEDA環境**<br>*PDK and EDA Environment* | **PDK構成要素・EDA連携・DRC・プロセス互換性・BSIMモデル**の関係を理解する。<br>*Understand the components of a PDK, its integration with EDA tools, design rule checking, process compatibility, and the relationship with BSIM models.* |
| 🧩 **第7章 / Chapter7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter7_automation_and_verification/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter7_automation_and_verification) | **自動化と実装検証技術**<br>*Automation and Implementation Verification* | **Lint・DRC・LVS・STA**に加え、**RTL〜物理検証の自動化・CI/CD検証フロー構築**を学ぶ。<br>*Learn automation techniques from RTL design to physical layout verification, and master CI/CD verification flows alongside Lint, DRC, LVS, and STA.* |
| 🧩 **第8章 / Chapter8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) | **FSM設計（有限状態機械）**<br>*FSM Design (Finite State Machine)* | **Moore型／Mealy型FSM・状態遷移図・Verilog三段階記述**を理解し、制御設計の基礎を固める。<br>*Understand the structure and operation of Moore and Mealy FSMs, and learn three-stage description methods in Verilog with state diagrams.* |
| 🧩 **第9章 / Chapter9**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) | **PLLとクロック設計**<br>*PLL and Clock Design* | **PLL動作原理・スキュー／ジッタ対策・クロックツリー設計**を体系的に学び、高精度クロック設計技術を習得する。<br>*Learn PLL principles, skew/jitter countermeasures, and clock tree design to acquire high-precision clock generation and distribution techniques.* |

---

## 🛠 **実践編 | Practice**
> Python自動化・Sky130実験・OpenLane設計など、実務に近い演習を通じてスキルを定着させます。  
> *Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design to solidify skills.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🛠 **第0章 / Chapter0**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter0_environment_setup/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter0_environment_setup) | **環境構築とツールセットの準備**<br>*Environment Setup and Toolchain Preparation* | **Python・VS Code・Git・ngspice・Sky130 PDK・OpenLane・Magic・Netgen・KLayout・Docker・WSL2**など、**実践編（第1〜6章）を進めるためのフルツールチェーン**をセットアップする。<br>*Set up the full toolchain required for subsequent chapters, including Python, VS Code, Git, ngspice, Sky130 PDK, OpenLane, Magic, Netgen, KLayout, Docker, and WSL2.* |
| 🛠 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) | **Pythonによる自動化ツール群**<br>*Python-Based Automation Tools for Semiconductor Design* | **Sky130 PDK・OpenLaneフロー**と連携し、**SPICEシミュレーション・信頼性モデル評価・レポート解析**を自動化するPythonスクリプト群を構築する。<br>*Develop Python scripts to automate SPICE simulations, reliability model evaluations, and report analysis in conjunction with the Sky130 PDK and OpenLane flow.* |
| 🛠 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter2_sky130_experiments/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter2_sky130_experiments) | **Sky130実験とSPICE特性評価**<br>*Sky130 Experiments and SPICE-Based Characterization* | **MOS特性（Vg–Idカーブ・Vth抽出）・BTI/TDBB予測**を行い、**SPICEベースの設計検証**を実践する。<br>*Use the SkyWater Sky130 PDK to evaluate MOS characteristics (Vg–Id curves, Vth extraction) and predict BTI/TDBB, performing SPICE-based design verification.* |
| 🛠 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter3_openlane_practice/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter3_openlane_practice) | **OpenLaneによるデジタル設計実習**<br>*Digital Design Practice Using OpenLane* | **Verilog RTL〜GDS生成**までのLSI設計フローを体験し、**合成・配置・配線・DRC**など各段階の目的とツールを理解する。<br>*Experience the LSI design flow from Verilog RTL to GDS generation, understanding the objectives and tools for synthesis, placement, routing, and DRC.* |

---

## 📦 **特別編 | Special Topics**
> 先端ノード・チップレット・統合制御SoCなど、最先端テーマを扱います。  
> *Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 📦 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter1_finfet_gaa/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa) | **先端ノード技術（FinFET・GAA・CFET）**<br>*Advanced Node Technologies – FinFET, GAA & CFET* | **FinFET・GAA・CFET構造**の**物理特性・電気特性・設計影響**を体系的に解説し、**プレーナMOSの限界を超える先端CMOS技術**を理解する。<br>*Comprehensively explains the physical and electrical characteristics and design impacts of FinFET, GAA, and CFET structures, introducing advanced CMOS technologies beyond planar MOS limits.* |
| 📦 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2_chiplet_pkg/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg) | **チップレットと先端パッケージ技術**<br>*Chiplets and Advanced Packaging* | **2.5D／3D実装・TSV・異種集積**による**チップレットアーキテクチャの設計・実装・信頼性**を学び、**柔軟な設計とスケーラビリティ**を可能にする技術を理解する。<br>*Covers 2.5D/3D integration, TSV, and heterogeneous integration for chiplet architecture design, implementation, and reliability, enabling flexible design and scalability.* |
| 📦 **第2a章 / Chapter2a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk) | **SystemDKにおける物理制約設計対応**<br>*Design Handling of Thermal, Stress, and Noise Constraints in SystemDK* | **SystemDK概念・SI/PI・熱・応力・EMI/EMC**といった**物理制約を設計的に扱う手法**を学び、SoC〜システムレベルでの統合設計力を養う。<br>*Explains the concept of SystemDK and methods for addressing physical constraints such as SI/PI, thermal, stress, and EMI/EMC in design.* |

---

## 🔗 関連プロジェクト一覧 | Related Projects

> 本教材体系と連動する拡張・応用プロジェクトの一覧です。  
> *A list of extension and application projects linked to this educational framework.*

| 🌐 プロジェクト / Project | 概要 / Overview | 主な特徴・内容 / Key Features |
|---|---|---|
| ➕ **Edusemi-Plus**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-Plus/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-Plus) | **地政学・製品戦略・AI・量子・投資**などを通じて、**半導体産業構造を読み解く応用教材**。<br>*Applied learning materials analyzing geopolitics, product strategy, AI, quantum, and investment.* | - **Apple Silicon・CHIPS法・Cryo-CMOS**の実例解説<br>- **技術と社会・政策・市場の接点**を多角的に探究 |
| 🎛️ **EduController**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) | **制御理論（PID・状態空間）からAI制御（NN・RL・LLM）まで**を体系的に網羅。<br>*Covers control theory (PID, state-space) to AI control (NN, RL, LLM).* | - **PoC設計・OpenLane制御実装**との連動<br>- **Python設計演習・RTL検証・FSM生成支援** |

---

## 👤 **執筆者情報 | Author**
> 本教材の企画・執筆者。半導体・インクジェット分野での実務経験を持ち、**教育と実装を融合した教材開発**を行う。  
> *Author with professional background in semiconductors and inkjet actuators, creating materials integrating theory and practice.*

| 📌 項目 / Item | 内容 / Details |
|------|------|
| **氏名 / Name** | **三溝 真一（Shinichi Samizo）**<br>*Shinichi Samizo* |
| **経験領域 / Expertise** | **半導体デバイス（ロジック・メモリ・高耐圧混載）**<br>*Semiconductor devices (logic, memory, high-voltage mixed integration)*<br>**インクジェット薄膜ピエゾアクチュエータ**<br>*Inkjet thin-film piezo actuators*<br>**PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**<br>*Productization of PrecisionCore printheads, BOM management, and ISO training* |
| **💻 GitHub** | **Samizo-AITL**<br>[![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 **ライセンス | License**
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)
> 教材・コード・図表の性質に応じたハイブリッドライセンスを採用。  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 項目 / Item | ライセンス / License | 説明 / Description |
|------|------|------|
| **コード（Code）** | [**MIT License**](https://opensource.org/licenses/MIT) | 自由に使用・改変・再配布が可能<br>*Free to use, modify, and redistribute* |
| **教材テキスト（Text materials）** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) または [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | 著者表示必須、継承条件あり（BY-SAの場合）<br>*Attribution required, share-alike for BY-SA* |
| **図表・イラスト（Figures & diagrams）** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | 非商用利用のみ許可<br>*Non-commercial use only* |
| **外部引用（External references）** | 元ライセンスに従う<br>*Follow the original license* | 引用元を明記<br>*Cite the original source* |

---

## 💬 **フィードバック | Feedback**
> 改善提案や議論はGitHub Discussionsからお願いします。  
> *Propose improvements or start discussions via GitHub Discussions.*

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
