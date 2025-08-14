---
layout: default
title: Edusemi-v4x/README.md  
---

---

# 🎓 **Edusemi-v4x｜半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*

[![Samizo-AITLポータルサイトに戻る](https://img.shields.io/badge/Samizo--AITL%20ポータルサイトに戻る-brightgreen)](https://samizo-aitl.github.io/) [![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  

--- 

## 🔗 公式リンク | Official Links

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 Japanese | [![🌐 GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) | [![💻 GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| 🇺🇸 English | [![🌐 GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/en/) | [![💻 GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |

---

## ✍️ **はじめに | Introduction**

半導体技術は **トランジスタの発明** から始まり、**MOS構造** の登場によって急速に進化しました。  
**微細化と集積化** はムーアの法則に沿って進み、LSIはあらゆる分野に浸透しています。

しかし、**物性・回路・プロセス・テスト** などの基礎分野は教育現場で分断されがちです。  
実務ではこれらは密接に関連しており、**回路はデバイス原理に依存し、設計はプロセスと信頼性に支えられています**。

**Edusemi** は、この「**基礎技術間の構造的つながり**」に焦点を当て、応用を見据えた **構造的理解** を育成する教材です。

> 💡 **Design follows physics, and productization follows verification.**  
> *物性 → 回路 → 実装 → 検証* の接続を可視化します。

---

## 📘 **プロジェクト概要 | Project Overview**

**Edusemi-v4x** は、**設計・製造・検査・品質保証** を一貫して学べる **オープン教材** です。

- 🎯 **対象 / Target**：工学系学生・若手技術者・教育者  
- ⭐ **特徴 / Features**：基礎のつながり重視、設計〜量産検査まで網羅  
- 🧪 **実習 / Practice**：sky130・OpenLane・Python・GitHub・ChatGPT 対応

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
> 基礎を踏まえて**メモリ・高耐圧・ESD・アナログ設計**など専門領域へ展開します。  
> *Expands into specialized areas such as memory, high-voltage, ESD, and analog design.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🧩 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) | メモリ技術<br>*Memory Technologies* | SRAM・DRAM・FeRAM・MRAM |
| 🧩 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter2_high_voltage_devices/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter2_high_voltage_devices) | 高耐圧デバイス<br>*High-Voltage Devices* | LDMOS・電界制御・高電圧設計 |
| 🧩 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) | ESD設計<br>*ESD Protection Design* | 保護素子・破壊事例・試験規格 |
| 🧩 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter4_layout_optimization/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter4_layout_optimization) | レイアウト最適化<br>*Layout Optimization* | CMPダミー・IRドロップ・ラッチアップ |
| 🧩 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) | アナログ／MIX信号<br>*Analog / Mixed-Signal* | アナログ設計・ノイズ・混載設計 |
| 🧩 **第5a章 / Chapter5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5a_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5a_analog_mixed_signal) | 0.18μm AMS設計技法<br>*0.18μm AMS Design* | ばらつき・マッチング・1/fノイズ |
| 🧩 **第5b章 / Chapter5b**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5b_ams_block_and_pdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5b_ams_block_and_pdk) | 製造起点のAMS差別化<br>*AMS Differentiation from Manufacturing* | 1/fノイズ低減・製造技術応用 |
| 🧩 **第6章 / Chapter6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) | PDKとEDA環境<br>*PDK & EDA Environment* | DRC/LVS/ERC・PDK構成 |
| 🧩 **第7章 / Chapter7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter7_automation_and_verification/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter7_automation_and_verification) | 自動化と検証<br>*Automation & Verification* | OpenLane・CI/CD・Lint |
| 🧩 **第8章 / Chapter8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) | FSM設計<br>*FSM Design* | Moore/Mealy・状態遷移図・Verilog |
| 🧩 **第9章 / Chapter9**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) | PLLとクロック<br>*PLL & Clock Design* | PLL構造・ジッタ・STA配慮 |

---

## 🛠 **実践編 | Practice**
> **Python自動化・Sky130実験・OpenLane設計**など、実務に近い演習を通じてスキルを定着させます。  
> *Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 🛠 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) | Python自動化ツール<br>*Python Automation Tools* | SPICE解析・OpenLaneログ処理 |
| 🛠 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter2_sky130_experiments/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter2_sky130_experiments) | Sky130実験<br>*Sky130 Experiments* | Vg–Id・Vth推定・BTI/TDDB評価 |
| 🛠 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter3_openlane_practice/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter3_openlane_practice) | OpenLane実習<br>*OpenLane Practice* | 合成〜配置配線〜GDS出力 |
| 🛠 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter4_poc_spec_and_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter4_poc_spec_and_design) | PoC設計展開<br>*PoC Design Development* | FSM・MUX・Adder・テスト |
| 🛠 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter5_evaluation_and_report/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter5_evaluation_and_report) | 評価とレポート<br>*Evaluation & Reporting* | 面積・波形・タイミング・DRC/LVS |

---

## 📦 **特別編 | Special Topics**
> **先端ノード・チップレット・統合制御SoC**など最先端テーマを扱います。  
> *Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.*

| 📖 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| 📦 **第1章 / Chapter1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter1_finfet_gaa/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa) | 先端ノード<br>*Advanced Nodes* | FinFET・GAA・CFETと設計影響 |
| 📦 **第2章 / Chapter2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2_chiplet_pkg/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg) | チップレットと先端パッケージ<br>*Chiplets & Advanced Packaging* | 2.5D/3D・TSV・異種集積 |
| 📦 **第2a章 / Chapter2a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk) | SystemDK実装制約設計<br>*SystemDK Design Constraints* | SI/PI・熱・応力・EMI/EMC |
| 📦 **第3章 / Chapter3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | 統合制御SoC実装<br>*Integrated Control SoC* | FSM×PID×LLM（AITL） |
| 📦 **第4章 / Chapter4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | OpenLane実装<br>*OpenLane Implementation* | 統合制御RTLの配置配線 |
| 📦 **第5章 / Chapter5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | DFM設計<br>*Design for Manufacturability* | DRC・LVS・DFM指針・Sky130 |

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
| **氏名 / Name** | 三溝 真一（Shinichi Samizo） |
| **学歴 / Education** | 信州大学大学院 電気電子工学 修了 |
| **経歴 / Career** | 元 セイコーエプソン株式会社 技術者（1997年〜） |
| **経験領域 / Expertise** | 半導体デバイス（ロジック・メモリ・高耐圧混載）<br>インクジェット薄膜ピエゾアクチュエータ<br>PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育 |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---

## 📄 **ライセンス | License**
> オープンライセンスにより、教育・研究・社内研修などへの自由な利用が可能。  
> *Open license allowing free use for education, research, and corporate training.*

| 📌 項目 / Item | 内容 / Details |
|------|------|
| **ライセンス種別 / Type** | MITライセンス |
| **利用条件 / Usage** | 自由に使用・改変・再配布が可能 |
| **推奨利用 / Recommended Uses** | 教育・研究・社内研修など |

---

## 💬 **フィードバックと改訂履歴 | Feedback & ChangeLog**
> 改善提案や議論はGitHub Discussionsから、改訂履歴はChangeLogにて公開。  
> *Propose improvements via GitHub Discussions, and track updates in the ChangeLog.*

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
[![📄 ChangeLog](https://img.shields.io/badge/📄%20View-ChangeLog-orange?logo=markdown)](revision_history.md)
