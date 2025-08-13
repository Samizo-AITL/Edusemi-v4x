---
layout: default
title: Edusemi-v4x/index.md
---

# 🎓 Edusemi-v4x  
**半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*  
[English README →](./README_en.md)

---

## ✍️ はじめに | Introduction

半導体技術は **トランジスタの発明** から始まり、**MOS構造** の登場で急速に進化しました。  
**微細化と集積化** はムーアの法則に沿って進み、LSIはあらゆる分野に広がっています。

しかし、**物性・回路・プロセス・テスト** などの分野は分業化が進み、教育現場では分断されがちです。  
実務ではこれらは密接につながっており、**回路はデバイスの動作原理に依存し、設計はプロセスや信頼性に支えられています**。

**Edusemi-v4x** は、この「**基礎技術同士の構造的つながり**」に焦点を当てた教材です。  
応用に向けた視野を持ちつつ、実務に活きる **構造的理解** を育てます。

---

## 📘 プロジェクト概要 | Project Overview

**Edusemi-v4x** は、**半導体の設計・製造・検査・品質保証** を一貫して学べる **オープン教材プロジェクト** です。

- 🎯 **対象**：工学系学生・若手技術者・教育者  
- 🌟 **特徴**：基礎のつながり重視、設計〜量産検査まで網羅  
- 🧪 **実習対応**：sky130 / OpenLane / Python / GitHub / ChatGPT

---

## 🧭 基礎編 | Fundamentals

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](chapter1_materials/README.md) | 半導体物性と材料基礎 | バンド構造・PN接合・MOS電界効果 |
| [2](chapter2_comb_logic/README.md) | デジタル論理と回路設計 | 組み合わせ回路・順序回路・FSM・HDL |
| [3](chapter3_process_evolution/README.md) | プロセス技術と微細化の制約 | ノード変遷・配線・リソグラフィ・信頼性 |
| [4](chapter4_mos_characteristics/README.md) | MOSトランジスタ特性 | 寸法・特性・PDK・デザインルール |
| [5a](chapter5a_spec_module_if/README.md) | 仕様策定とIF設計 | 上流工程・モジュール選定・PoC接続 |
| [5](chapter5_soc_design_flow/README.md) | SoC設計フロー | RTL設計・配置配線・DRC/LVS・タイミング検証 |
| [6](chapter6_test_and_package/README.md) | テスト・パッケージ | ETEST・不良解析・信頼性試験・出荷管理 |
| [7](chapter7_design_review_and_org/README.md) | デザインレビューと組織連携 | SRAM不良事例・DR構造・合意形成 |

---

## 🧩 応用編 | Applications

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](d_chapter1_memory_technologies/README.md) | メモリ技術 | SRAM・DRAM・FeRAM・MRAM |
| [2](d_chapter2_high_voltage_devices/README.md) | 高耐圧デバイス | LDMOS・電界制御構造・高電圧設計 |
| [3](d_chapter3_esd_protection_design/README.md) | ESD設計 | 保護素子・破壊事例・試験規格 |
| [4](d_chapter4_layout_optimization/README.md) | レイアウト最適化 | CMPダミー・IRドロップ・ラッチアップ防止 |
| [5](d_chapter5_analog_mixed_signal/README.md) | アナログ／MIX信号 | アナログ設計・ノイズ・混載設計 |
| [5a](d_chapter5a_analog_mixed_signal/README.md) | 0.18μm AMS設計技法 | ばらつき・マッチング・1/fノイズ |
| [5b](d_chapter5b_ams_block_and_pdk/README.md) | 製造起点のAMS差別化 | 1/fノイズ低減・製造技術応用 |
| [6](d_chapter6_pdk_and_eda_environment/README.md) | PDKとEDA環境 | DRC/LVS/ERC・PDK構成 |
| [7](d_chapter7_automation_and_verification/README.md) | 自動化と検証 | OpenLane・CI/CD・Lint |
| [8](d_chapter8_fsm_design_basics/README.md) | FSM設計 | Moore/Mealy型・状態遷移図・Verilog |
| [9](d_chapter9_pll_and_clock_design/README.md) | PLLとクロック | PLL構造・ジッタ・STA設計配慮 |

---

## 🛠 実践編 | Practice

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](e_chapter1_python_automation_tools/README.md) | Python自動化ツール | SPICE解析・OpenLaneログ処理 |
| [2](e_chapter2_sky130_experiments/README.md) | Sky130実験 | Vg–Id特性・Vth推定・BTI/TDDB評価 |
| [3](e_chapter3_openlane_practice/README.md) | OpenLane実習 | 合成〜配置配線〜GDS出力 |
| [4](e_chapter4_poc_spec_and_design/README.md) | PoC設計展開 | FSM・MUX・Adder設計とテスト |
| [5](e_chapter5_evaluation_and_report/README.md) | 評価とレポート | 面積・波形・タイミング・DRC/LVS分析 |

---

## 📦 特別編 | Special Topics

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](f_chapter1_finfet_gaa/README.md) | 先端ノード | FinFET・GAA・CFET構造と設計影響 |
| [2](f_chapter2_chiplet_pkg/README.md) | チップレットと先端パッケージ | 2.5D/3D・TSV・異種集積 |
| [2a](f_chapter2a_systemdk/README.md) | SystemDK実装制約設計 | SI/PI・熱・応力・EMI/EMC |
| [3](f_chapter3_socsystem/README.md) | 統合制御SoC実装 | FSM×PID×LLMによるAITL制御 |
| [4](f_chapter4_openlane/README.md) | OpenLane実装 | 統合制御RTLの配置配線 |
| [5](f_chapter5_dfm/README.md) | DFM設計 | DRC・LVS・DFM指針とSky130活用 |

---

## 🤖 ChatGPT連携 | AI Integration

学習者は ChatGPT を **学習パートナー** として、  
コード添削・エラー解析・ツール操作・レポート補助などに活用可能。  
現代の設計現場に即した **対話型・実務直結型学習** を支援します。

---

## 🔗 関連プロジェクト | Related Projects

- 🎛️ [EduController](https://samizo-aitl.github.io/EduController/) – 制御理論からAI制御まで網羅  
- 🤖 [AITL-H](https://samizo-aitl.github.io/AITL-H/) – FSM＋PID＋LLMによる三層制御アーキテクチャ  
- 🌐 [Edusemi-Plus](https://samizo-aitl.github.io/Edusemi-Plus/) – 地政学・戦略・AI・量子・投資を扱う応用教材

---

## 👤 執筆者 | Author

**三溝 真一（Shinichi Samizo）**  
信州大学大学院 電気電子工学 修了  
元 セイコーエプソン株式会社 技術者（1997〜）

📌 経験領域：半導体デバイス・インクジェット薄膜アクチュエータ・製品化・ISO教育  
✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com) | 🐦 [@shin3t72](https://x.com/shin3t72) | 💻 [Website](https://samizo-aitl.github.io/)

---

## 📄 ライセンス | License

MITライセンスに基づき、自由に使用・改変・再配布が可能。  
教育・研究・社内研修への活用も歓迎します。

[改訂履歴（ChangeLog）](revision_history.md)  
[Edusemi教材に関する議論 → Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
