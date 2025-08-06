---
layout: default
title: Edusemi トップページ
---

---

# 🎓 **Edusemi-v4x：半導体プロダクト開発のための基礎教育教材**

🇺🇸 **[English README](./README_en.md)**  
　*Foundational Educational Materials for Semiconductor Product Development*

---

✍️ **はじめに | Introduction**

半導体技術は、**トランジスタの発明**から始まり、**MOS構造**の登場で急速に進化しました。  
**微細化と集積化**はムーアの法則に沿って進み、LSIはあらゆる分野に広がっています。

しかし、**物性・回路・プロセス・テスト**などの分野は分業化が進み、教育現場では分断されがちです。  
実務ではこれらは密接につながっており、**回路はデバイスの動作原理に依存し、設計はプロセスや信頼性に支えられています**。

**Edusemi** は、このような「**基礎技術同士の構造的つながり**」に焦点を当てた教育教材です。  
**応用に向けた視野**を意識しつつも、「基礎技術同士の構造的つながり」に集中し、実務に活きる**構造的理解**を育てることを目指します。

---

📘 **プロジェクト概要**

**Edusemi-v4x** は、**半導体の設計・製造・検査・品質保証に関する一貫した基礎知識**を、**体系的かつ実践的**に学ぶための**オープン教材プロジェクト**です。

- 🎯 対象：**工学系の学生、若手技術者、教育者**
- ⭐ 特徴：**基礎のつながり重視**、**回路設計から量産検査までの一貫理解**
- 🧪 実習対応：**sky130、OpenLane、Python、GitHub、ChatGPT** による**対話型学習統合**

---

## 🧭 **基礎編　章構成一覧**

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](chapter1_materials/README.md) | **半導体物性と材料基礎** | **バンド構造・PN接合・MOS電界効果**などの基礎物性 |
| [2](chapter2_comb_logic/README.md) | **デジタル論理と論理回路設計** | **組み合わせ回路・順序回路・FSM・HDL**の基礎 |
| [3](chapter3_process_evolution/README.md) | **プロセス技術と微細化の制約** | **ノード変遷・配線・リソグラフィ・信頼性**の基盤理解 |
| [4](chapter4_mos_characteristics/README.md) | **MOSトランジスタ特性と設計基盤** | **寸法・特性・PDK・デザインルール**との関係 |
| [5](chapter5_soc_design_flow/README.md) | **SoC設計フローとEDAツール** | **RTL設計・配置配線・DRC/LVS・タイミング検証**など |
| [6](chapter6_test_and_package/README.md) | **テスト・パッケージ・製品化** | **ETEST・不良解析・信頼性試験・出荷管理**まで |
| [7](chapter7_design_review_and_org/README.md) | **デザインレビューと開発組織連携** | **SRAM不良事例・DR構造・合意形成**の実践視点 |

---

## 🧩 **応用編　章構成一覧**

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](d_chapter1_memory_technologies/README.md) | **メモリ技術** | **SRAM・DRAM・FeRAM・MRAM**の構造・特性・用途 |
| [2](d_chapter2_high_voltage_devices/README.md) | **高耐圧デバイス** | **LDMOS・電界制御構造・高電圧デバイス設計** |
| [3](d_chapter3_esd_protection_design/README.md) | **ESD設計** | **保護素子・破壊事例・試験規格・レイアウト注意点** |
| [4](d_chapter4_layout_optimization/README.md) | **レイアウト設計と最適化** | **CMPダミー・IRドロップ・ラッチアップ防止**など |
| [5](d_chapter5_analog_mixed_signal/README.md) | **アナログ／ミックスドシグナル** | **アナログ設計・ノイズ・混載設計の課題と対策** |
| [5a](d_chapter5a_analog_mixed_signal/README.md) | **0.18μm AMS設計技法** | **ばらつき・マッチング・1/fノイズ・Q値改善**など設計的最適化 |
| [5b](d_chapter5b_ams_block_and_pdk/README.md) | **製造技術によるアナログ差別化** | **1/fノイズ半減・製造起点のAMSモジュール創出と製品展開** |
| [6](d_chapter6_pdk_and_eda_environment/README.md) | **PDKとEDA環境** | **DRC/LVS/ERC・PDK構成・EDAフロー**の理解 |
| [7](d_chapter7_automation_and_verification/README.md) | **自動化と実装検証技術** | **OpenLane・CI/CD・Lint・ログ解析**の導入例 |
| [8](d_chapter8_fsm_design_basics/README.md) | **FSM設計（有限状態機械）** | **Moore/Mealy型・状態遷移図・Verilog記述** |
| [9](d_chapter9_pll_and_clock_design/README.md) | **PLLとクロック設計** | **PLL構造・ジッタ/スキュー・STA設計配慮** |

---

## 🛠 **実践編　章構成一覧**

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](e_chapter1_python_automation_tools/README.md) | **Pythonによる自動化ツール群** | **SPICE解析・OpenLaneログ処理・特性可視化スクリプト** |
| [2](e_chapter2_sky130_experiments/README.md) | **Sky130実験とSPICE特性評価** | **Vg–Id特性・Vth推定・BTI/TDDB評価**など |
| [3](e_chapter3_openlane_practice/README.md) | **OpenLaneによるデジタル設計実習** | **合成〜配置配線〜GDS出力までの流れを体験** |
| [4](e_chapter4_poc_spec_and_design/README.md) | **PoC仕様書と設計展開** | **FSM・MUX・Adder設計とVerilogテストベンチ演習** |
| [5](e_chapter5_evaluation_and_report/README.md) | **設計結果の評価とレポート** | **面積・波形・タイミング・DRC/LVS結果の分析と改善提案** |

---

## 📦 **特別編：章構成一覧**

| 章 | タイトル | 概要 |
|----|----------|------|
| [1](f_chapter1_finfet_gaa/README.md) | **先端ノード（FinFET・GAA・CFET）** | **Fin構造・GAA・CFETの構造・設計影響・スケーリング技術** |
| [2](f_chapter2_chiplet_pkg/README.md) | **チップレットと先端パッケージ技術** | **2.5D/3D・TSV・異種集積事例** |
| [2a](f_chapter2a_systemdk/README.md) | **SystemDKにおける熱・応力・ノイズ制約の設計対応** | **信号・電源（SI/PI）、熱、応力、電磁ノイズ（EMI/EMC）を統合的に扱う実装制約設計** |
| [3](f_chapter3_socsystem/README.md) | **FSM×PID×LLMによる統合制御SoC実装** | **AITL制御のSoC適用と統合制御展開** |
| [4](f_chapter4_openlane/README.md) | **FSM×PID×LLMのOpenLane実装** | **統合制御RTLの配置配線・DRC検証** |
| [5](f_chapter5_dfm/README.md) | **PDKと物理整合・DFM設計** | **DRC・LVS・DFM設計指針とSky130活用** |

---

## 🤖 **ChatGPTとの連携活用**

**Edusemi** は、**ChatGPTとの連携**を前提に設計されています。  
学習者は、**コードの添削・エラー解析・ツール操作ガイド・レポート補助**など、あらゆる場面で ChatGPT を“**学習パートナー**”として活用できます。  
現代の設計現場に即した **対話型・実務直結型学習** を支援します。

---

## 🧾 Edusemi総括｜Edusemi Summary

**Edusemiプロジェクト**は、半導体技術の教育と実装の架け橋となることを目指して、**デバイス設計・プロセス・EDA・制御応用**にわたる統合型教材として構築されました。  
基本から応用、そして先端技術や制御PoCまで網羅したこの教材群は、**研究者・設計者・教育者が共通の技術言語で対話するための“基盤”**となることを目的としています。

> The **Edusemi project** aims to bridge semiconductor education and practical design, providing a comprehensive curriculum spanning **device fundamentals, process evolution, EDA workflows, and advanced control applications**.  
> This educational suite aspires to become a **shared technical platform** for researchers, designers, and educators alike.

---

### 🧭 教材の意義｜Educational Significance

- 🔬 **プロセス〜設計〜製品化の一気通貫**：Sky130, FinFET, GAA, 制御SoC まで接続  
- 🧠 **実務知見の体系化**：現場経験を基にした教材設計（0.18μm AMSなど）  
- 🌐 **国際発信に対応**：日本語・英語併記、MITライセンス、GitHub公開  
- 🎓 **教育と研究の両立**：PDK演習 × PoC設計 × 歴史的背景の三位一体構成

---

### 🚀 今後の展望｜Future Possibilities

- 📘 **演習パッケージ化**（PDF/HTML/PDF講義スライド形式で展開）  
- 🏫 **大学・高専との連携展開**（講義・ワークショップ形式）  
- 🧪 **PoC教材の拡充**（FSM設計演習、制御OpenLane実装、自動評価）  
- 🌍 **国際展開と翻訳支援**（多言語版教材とGitHub Pages連携）

---

### 🏁 結び｜Final Remarks

Edusemiは単なる「教材」ではなく、**半導体技術を社会に橋渡しするための“共有知”のプラットフォーム**です。  
今後の発展は、**本教材を用いるあなた自身の手によって、教育現場や実務設計に活かされることで完成していきます。**

> *This is not the end of Edusemi — it is a beginning for those who will use it, improve it, and carry it forward into new frontiers of semiconductor design and education.*

---

## 🔗 **関連プロジェクト**

### 🎛️ **[EduController](https://github.com/Samizo-AITL/EduController)**  
- **制御理論（PID・状態空間）〜AI制御（NN・RL・LLM）**まで網羅  
- **PoC設計・OpenLane制御実装**との連動構成  
- **Pythonによる設計演習・RTL検証・FSM生成支援**も収録

### 🤖 **[AITL-H](https://github.com/Samizo-AITL/AITL-H)**  
- **FSM（本能）＋PID（理性）＋LLM（知性）**による三層制御アーキテクチャ  
- **人型ロボット・統合制御のPoC実装**が可能  
- Edusemiの**特別編3・4章**と構造的に連携

### 🌐 **[Edusemi-Plus](https://github.com/Samizo-AITL/edusemi-plus)**  
- **地政学・製品戦略・AI・量子・投資**など産業構造を読み解く応用教材  
- **Apple Silicon・CHIPS法・Cryo-CMOS**など実例を解説  
- 技術だけでなく**社会との接点や背景**を探究

---

## 📘 **関連ドキュメント**

- 📄 [はじめに（教材の構想と目的）](introduction.md)  
- 📄 [改訂履歴（ChangeLog）](revision_history.md)

---

## 👤 **執筆者情報 / Author**

**三溝 真一（Shinichi Samizo）**  
- **信州大学大学院 電気電子工学 修了**  
- 元 **セイコーエプソン**株式会社 技術者（1997年〜）

📌 **経験領域**：  
- **半導体デバイス(ロジック・メモリ・高耐圧混載)**  
- **インクジェット薄膜ピエゾアクチュエータ**  
- **PrecisionCoreプリントヘッド製品化・BOM管理・ISO教育**

📬 **連絡先**  
- ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 [https://x.com/shin3t72](https://x.com/shin3t72)  
- 💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/)

---

## 📄 **ライセンス**

本教材は **MITライセンス** に基づき、**自由に使用・改変・再配布**が可能です。  
**教育・研究・社内研修**への活用も歓迎します。

---

💬 [Edusemi教材に関する議論はこちら → Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)

---
