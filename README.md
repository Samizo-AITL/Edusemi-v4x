# 🎓 Edusemi-v4x：半導体設計・製造 教育教材

---

## ✍️ はじめに | Introduction

半導体技術は、1947年のトランジスタ発明から始まり、MOS構造の登場によって、低電圧・高集積なデジタル回路が実現されました。以降、ムーアの法則に沿って微細化と集積化が進み、LSIは社会のあらゆる分野に広がっていきました。

こうした進化の中で、**物性・回路・プロセス・設計・テスト**といった領域は分業化が進み、教育現場でも分断されがちです。しかし実務では、それらは密接につながっています。回路はデバイスの動作原理に依存し、設計はプロセスや信頼性に支えられています。

**Edusemi は、こうした“基礎のつながり”を意識的に示す教育教材**です。応用や先端には踏み込まず、あえて基礎に徹することで、実務に必要な**構造的理解**を育むことを目指しています。

---

## 📘 プロジェクト概要

**Edusemi-v4x** は、半導体の設計・製造・検査・品質保証に関する一貫した知識を、体系的かつ実践的に学ぶためのオープン教材プロジェクトです。

対象は、工学系の学生、若手技術者、教育者。**回路設計から量産現場、レビュー体制まで**、現場の構造を理解しながら学べます。

---

## 🧭 基礎編　章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [第1章](chapter1_materials/README.md) | 半導体物性と材料基礎 | バンド構造、PN接合、MOS電界効果などの基礎物性 |
| [第2章](chapter2_comb_logic/README.md) | デジタル論理と論理回路設計 | 組み合わせ回路、順序回路、FSMとHDL記述の導入 |
| [第3章](chapter3_process_variation/README.md) | プロセス技術と微細化の制約 | ノード変遷、配線、リソグラフィ、信頼性と変動要因 |
| [第4章](chapter4_mos_characteristics/README.md) | MOSトランジスタ特性と設計基盤 | 寸法・特性・信頼性、PDKとの関係、デザインルール |
| [第5章](chapter5_soc_design_flow/README.md) | SoC設計フローとEDAツール | RTL設計、合成、配置配線、DRC/LVS、タイミング検証 |
| [第6章](chapter6_test_and_package/README.md) | テスト・パッケージ・製品化 | ETEST・ウエハテスト・不良解析・信頼性試験・出荷管理 |
| [第7章](chapter7_design_review_and_org/README.md) | デザインレビューと開発組織連携 | DR構造、ケース比較、SRAM不良事例、組織的合意形成 |

---

## 🧩 応用編　章構成一覧

| 章番号 | タイトル | ディレクトリ |
|--------|----------|---------------|
| 第1章 | メモリ技術（DRAM, SRAM, Flash） | [d_chapter1_memory_technologies](d_chapter1_memory_technologies/) |
| 第2章 | 高耐圧デバイス（LDMOS等） | [d_chapter2_high_voltage_devices](d_chapter2_high_voltage_devices/) |
| 第3章 | ESD設計（静電破壊保護） | [d_chapter3_esd_protection_design](d_chapter3_esd_protection_design/) |
| 第4章 | レイアウト設計と最適化 | [d_chapter4_layout_optimization](d_chapter4_layout_optimization/) |
| 第5章 | アナログ／ミックスドシグナル | [d_chapter5_analog_mixed_signal](d_chapter5_analog_mixed_signal/) |
| 第6章 | PDKとEDA環境 | [d_chapter6_pdk_and_eda_environment](d_chapter6_pdk_and_eda_environment/) |
| 第7章 | 自動化と実装検証技術 | [d_chapter7_automation_and_verification](d_chapter7_automation_and_verification/) |
| 第8章 | FSM設計（有限状態機械） | [d_chapter8_fsm_design_basics](d_chapter8_fsm_design_basics/) |
| 第9章 | PLLとクロック設計 | [d_chapter9_pll_and_clock_design](d_chapter9_pll_and_clock_design/) |

---

## 🛠 実践編　章構成一覧

| 章番号 | タイトル | ディレクトリ |
|--------|----------|---------------|
| 第1章 | Pythonによる自動化ツール群 | [e_chapter1_python_automation_tools](e_chapter1_python_automation_tools/) |

---

## 📚 特別編　章構成一覧

| 章番号 | タイトル | ディレクトリ |
|--------|----------|---------------|
| 第1章 | 先端ノード（FinFET、GAA等） | [f_chapter1_advanced_nodes](f_chapter1_advanced_nodes/) |
| 第2章 | チップレットと先端パッケージ技術 | [f_chapter2_chiplet_and_packaging](f_chapter2_chiplet_and_packaging/) |
| 第3章 | ダイオード応用技術 | [f_chapter3_diode_applications](f_chapter3_diode_applications/) |
| 第4章 | LLM × 制御のハイブリッドASIC設計 | [f_chapter4_llm_control_hybrid](f_chapter4_llm_control_hybrid/) |
| 第5章 | インクジェット技術と半導体設計の接点 | [f_chapter5_inkjet_and_semiconductor](f_chapter5_inkjet_and_semiconductor/) |

---

## 📄 ライセンス

本教材は **MITライセンス** に基づき、自由に使用・改変・再配布が可能です。  
教育機関・企業内研修などでの活用も歓迎します。

---

## 📬 連絡先

技術監修・執筆：**三溝 真一（Shinichi Samizo）**  
GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
お問い合わせは Issue または Discussions にて

---
