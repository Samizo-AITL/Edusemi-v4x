# 🎓 Edusemi-v4x：半導体プロダクト開発のための基礎教育教材

✍️ はじめに | Introduction

半導体技術は、トランジスタの発明から始まり、MOS構造の登場で急速に進化しました。  
微細化と集積化はムーアの法則に沿って進み、LSIはあらゆる分野に広がっています。

しかし、**物性・回路・プロセス・テスト**などの分野は分業化が進み、教育現場では分断されがちです。  
実務ではこれらは密接につながっており、**回路はデバイスの動作原理に依存し、設計はプロセスや信頼性に支えられています**。

**Edusemi** は、このような「基礎技術同士の構造的つながり」に焦点を当てた教育教材です。  
**応用に向けた視野を意識しつつも、「基礎技術同士の構造的つながり」に集中**し、実務に活きる“構造的理解”を育てることを目指します。

---

- 🇺🇸 [English README](./README_en.md)  
　→ Foundational Educational Materials for Semiconductor Product Development

---

📘 **プロジェクト概要**

**Edusemi-v4x** は、**半導体の設計・製造・検査・品質保証に関する一貫した基礎知識**を、体系的かつ実践的に学ぶためのオープン教材プロジェクトです。

- 対象：工学系の学生、若手技術者、教育者
- 特徴：**基礎のつながり重視**、**回路設計から量産検査までの一貫理解**
- 実習対応：**sky130、OpenLane、Python、GitHub に加え、**ChatGPTを活用した対話型学習を統合**した現代的な学習スタイル

---

## 🧭 基礎編　章構成一覧

| 章 | タイトル | 概要 |
|--------|----------|------|
| [1](chapter1_materials/README.md) | 半導体物性と材料基礎 | バンド構造、PN接合、MOS電界効果などの基礎物性 |
| [2](chapter2_comb_logic/README.md) | デジタル論理と論理回路設計 | 組み合わせ回路、順序回路、FSMとHDL記述の導入 |
| [3](chapter3_process_evolution/README.md) | プロセス技術と微細化の制約 | ノード変遷、配線、リソグラフィ、信頼性と変動要因 |
| [4](chapter4_mos_characteristics/README.md) | MOSトランジスタ特性と設計基盤 | 寸法・特性・信頼性、PDKとの関係、デザインルール |
| [5](chapter5_soc_design_flow/README.md) | SoC設計フローとEDAツール | RTL設計、合成、配置配線、DRC/LVS、タイミング検証 |
| [6](chapter6_test_and_package/README.md) | テスト・パッケージ・製品化 | ETEST・ウエハテスト・不良解析・信頼性試験・出荷管理 |
| [7](chapter7_design_review_and_org/README.md) | デザインレビューと開発組織連携 | DR構造、ケース比較、SRAM不良事例、組織的合意形成 |

---

## 🧩 応用編　章構成一覧

| 章 | タイトル | 概要 |
|--------|----------|------|
| [1](d_chapter1_memory_technologies/README.md) | メモリ技術 | SRAM・DRAM・FeRAM・MRAMなどの構造・特性・用途とSoC設計との関係 |
| [2](d_chapter2_high_voltage_devices/README.md) | 高耐圧デバイス | LDMOS等に代表される電界制御構造と、高電圧動作のためのデバイス設計 |
| [3](d_chapter3_esd_protection_design/README.md) | ESD設計 | 静電破壊対策の基本、保護素子、レイアウト注意点、試験規格と破壊事例 |
| [4](d_chapter4_layout_optimization/README.md) | レイアウト設計と最適化 | CMPダミー、IRドロップ、ラッチアップ防止など、物理実装とその工夫 |
| [5](d_chapter5_analog_mixed_signal/README.md) | アナログ／ミックスドシグナル | アナログブロック設計とノイズ、レイアウト、混載設計における課題と対策 |
| [6](d_chapter6_pdk_and_eda_environment/README.md) | PDKとEDA環境 | PDKの構成、EDAツールとの接続、DRC/LVS/ERCチェックフローの理解 |
| [7](d_chapter7_automation_and_verification/README.md) | 自動化と実装検証技術 | Lint、OpenLaneによる論理・物理検証とログ解析、CI/CDの導入例 |
| [8](d_chapter8_fsm_design_basics/README.md) | FSM設計（有限状態機械） | Moore/Mealy型、状態遷移図、Verilog記述までの構造的理解 |
| [9](d_chapter9_pll_and_clock_design/README.md) | PLLとクロック設計 | PLLの構造、周波数合成、ジッタ/スキュー、STAにおける設計配慮点 |

---

## 🛠 実践編　章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [1](e_chapter1_python_automation_tools/README.md) | Pythonによる自動化ツール群 | SPICEシミュレーション、特性プロット、OpenLaneログ解析など、半導体設計現場に役立つ実務的スクリプト群の実装例 |
| [2](e_chapter2_sky130_experiments/README.md) | Sky130実験とSPICE特性評価 | Sky130 MOSモデルを用いた Vg–Id 特性抽出、しきい値電圧 (Vth) 推定、BTI/TDDB 劣化予測などのSPICE実験フロー |
| [3](e_chapter3_openlane_practice/README.md) | OpenLaneによるデジタル設計実習 | RTL記述からGDS出力まで、OpenLaneツールによる論理合成・配置配線・レポート解析を通じて、物理設計の流れを体験的に学ぶ |
| [4](e_chapter4_poc_spec_and_design/README.md) | PoC仕様書と設計展開 | FSM・MUX・Adder の最小構成PoC仕様を策定し、Verilog設計とテストベンチを通じてRTL設計の基本構造と意図を明確化 |
| [5](e_chapter5_evaluation_and_report/README.md) | 設計結果の評価とレポート | 波形解析、面積・タイミング・DRC/LVSの設計評価を行い、比較・改善提案まで含めた設計フィードバック力を実践的に育成 |

---

## 📦 特別編：章構成一覧

| 章 | タイトル | 概要 |
|--------|----------|------|
| [1](f_chapter1_finfet_gaa/README.md) | 先端ノード（FinFET、GAA等） | 微細化対応の新構造トランジスタの物理・電気特性と設計影響 |
| [2](f_chapter2_chiplet_pkg/README.md) | チップレットと先端パッケージ技術 | 異種集積における2.5D/3Dパッケージ技術、TSV・インターポーザ事例 |
| [3](f_chapter3_socsystem/README.md) | FSM×PID×LLMによる統合制御システムのSoC実装手法 | AITLアーキテクチャのSoC実装への適用と統合制御手法の展開 |
| [4](f_chapter4_openlane/README.md) | FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装 | OpenLaneを用いた統合制御ロジックの配置配線・DRC対応 |
| [5](f_chapter5_dfm/README.md) | PDKとレイアウト検証による物理整合とDFM設計指針 | Sky130 PDKを用いたDRC・LVS・DFM設計手法の実践的習得 |
| [6](f_chapter6_actuator_system/README.md) | 圧電アクチュエータ制御システムの構成と実装 | 分極処理、ヒステリシス補償、FSM制御、COF実装などを統合した実践教材 |
| [7](f_chapter7_product_docs/README.md) | 完成体製品における開発ドキュメントとワークフロー | BOM構成、部品管理、試作・評価、DR・量産Gateなどを体系化した実務ドキュメント教材 |

---

## 🤖 ChatGPTとの連携活用

Edusemi は、ChatGPT との連携を前提に設計されています。  
学習者は、コードの添削やエラー解析、ツール操作のガイド、概念の再説明、実験レポートの構成補助など、あらゆる場面で ChatGPT を“学習パートナー”として活用できます。  
現代の設計現場に即した **対話型・実務直結型の学習**を支える教材として設計されています。

---

## 🔗 関連プロジェクト

本教材は、以下の教育プロジェクト・制御フレームワークと連携しています。  
半導体の論理設計や自動化実装と密接に関わる制御技術・AI統合手法を、横断的に学ぶことが可能です。

### 🎛️ [EduController](https://github.com/Samizo-AITL/EduController)

古典制御・現代制御から、ニューラルネット・強化学習・LLM連携などの次世代AI制御までを網羅した教育教材。  
**Pythonベースでの制御設計演習や実装・検証手法**が学べ、**PoC仕様書作成やOpenLane連携**も含む。

- 制御理論（PID・状態空間・H∞など）からAI制御（RL・NN制御・LLM統合）までを体系的に学習  
- Edusemiの「PoC設計」「LLM制御SoC実装」との連動を意識した構成  
- RTL-to-GDSIIまで一貫した制御ロジック設計の学習を支援  

### 🤖 [AITL-H](https://github.com/Samizo-AITL/AITL-H)

FSM（本能）＋PID（理性）＋LLM（知性）の三層制御構造を特徴とする**構造知能制御フレームワーク**。  
人型ロボットや知能化装置への応用を想定し、**PoC設計・FSM制御・LLM推論による統合制御**を実証可能。

- FSM×PID×LLMを軸としたハイブリッド知能制御構造  
- Edusemiの「特別編3・4章（統合制御SoC/RTL-to-GDSII実装）」と対応  
- 制御設計からSoC実装までを横断した教育・開発が可能

### 🌐 [Edusemi-Plus](https://github.com/Samizo-AITL/edusemi-plus)

半導体技術を**地政学・企業戦略・市場動向・量子技術**など多角的な視点で深掘りする応用教材シリーズ。  
**技術と社会の接点**を重視し、技術者・マネジメント・教育者の視野拡大と意思決定支援を目的としています。

- 米中対立・TSMC戦略・AI/量子半導体・Apple Siliconなどの分析を収録  
- Edusemiの技術教材を背景に「なぜその技術が生まれ、どう影響するか」を理解  
- 技術・経済・政策のつながりを学ぶ産業横断的アプローチを提供

---

## 📘 関連ドキュメント

- [はじめに（教材の構想と目的）](introduction.md)
- [改訂履歴（ChangeLog）](revision_history.md)

---

## 🧑‍🔬 執筆者情報

- **氏名**：三溝 真一（Shinichi Samizo）  
- **学歴**：信州大学大学院 電気電子工学修士課程 修了  

- **職歴**：  
  1997年 セイコーエプソン株式会社 入社  
  以下の開発・製品化に従事：  
  - 半導体デバイス技術（0.35µm〜0.18µmノード）  
  - ロジックデバイス、メモリデバイス、高耐圧インテグレーション技術の開発・量産化  
  - インクジェット薄膜ピエゾアクチュエータ開発  
  - PrecisionCoreプリントヘッド製品展開にも参画  

- **連絡先**：  
  GitHub：[Samizo-AITL](https://github.com/Samizo-AITL)  
  Email：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

## 📄 ライセンス

本教材は **MITライセンス** に基づき、自由に使用・改変・再配布が可能です。  
教育機関・企業内研修などでの活用も歓迎します。

---

💬 [Edusemi教材に関する議論はこちら → Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)

---
