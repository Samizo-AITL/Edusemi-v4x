# 🎓 Edusemi-v4x：半導体設計・製造 教育教材

---

## ✍️ はじめに | Introduction

半導体技術は、トランジスタの発明から始まり、MOS構造の登場で急速に進化しました。微細化と集積化はムーアの法則に沿って進み、LSIはあらゆる分野に広がっています。

しかし、物性・回路・プロセス・テストなどの分野は分業化が進み、教育現場では分断されがちです。実務ではこれらは密接につながっており、回路はデバイス原理に依存し、設計はプロセスや信頼性に支えられています。

Edusemi は、このような「基礎同士のつながり」に焦点を当てた教育教材です。応用や先端に飛びすぎず、“基礎を構造的に理解する”ことに徹することで、設計実務に必要な視点を育てます。
---

## 📘 プロジェクト概要

**Edusemi-v4x** は、半導体の設計・製造・検査・品質保証に関する一貫した知識を、体系的かつ実践的に学ぶためのオープン教材プロジェクトです。

対象は、工学系の学生、若手技術者、教育者。**回路設計から量産現場、レビュー体制まで**、現場の構造を理解しながら学べます。

---

## 🧭 基礎編　章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [1](chapter1_materials/README.md) | 半導体物性と材料基礎 | バンド構造、PN接合、MOS電界効果などの基礎物性 |
| [2](chapter2_comb_logic/README.md) | デジタル論理と論理回路設計 | 組み合わせ回路、順序回路、FSMとHDL記述の導入 |
| [3](chapter3_process_evolution/README.md) | プロセス技術と微細化の制約 | ノード変遷、配線、リソグラフィ、信頼性と変動要因 |
| [4](chapter4_mos_characteristics/README.md) | MOSトランジスタ特性と設計基盤 | 寸法・特性・信頼性、PDKとの関係、デザインルール |
| [5](chapter5_soc_design_flow/README.md) | SoC設計フローとEDAツール | RTL設計、合成、配置配線、DRC/LVS、タイミング検証 |
| [6](chapter6_test_and_package/README.md) | テスト・パッケージ・製品化 | ETEST・ウエハテスト・不良解析・信頼性試験・出荷管理 |
| [7](chapter7_design_review_and_org/README.md) | デザインレビューと開発組織連携 | DR構造、ケース比較、SRAM不良事例、組織的合意形成 |

---

---

## 🧩 応用編　章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [1](d_chapter1_memory_technologies/README.md) | メモリ技術 | SRAM・DRAM・FeRAM・MRAMなどの構造・特性・用途とSoC設計との関係 |
| [2](d_chapter2_high_voltage_devices/README.md) | 高耐圧デバイス | LDMOS等に代表される電界制御構造と、高電圧動作のためのデバイス設計 |
| [3](d_chapter3_esd_protection_design/README.md) | ESD設計 | 静電破壊対策の基本、保護素子、レイアウト注意点、試験規格と破壊事例 |
| [4](d_chapter4_layout_optimization/README.md) | レイアウト設計と最適化 | CMPダミー、IRドロップ、ラッチアップ防止など、物理実装とその工夫 |
| [5](d_chapter5_analog_mixed_signal/README.md) | アナログ／ミックスドシグナル | アナログブロック設計とノイズ、レイアウト、混載設計における課題と対策 |
| [６](d_chapter6_pdk_and_eda_environment/README.md) | PDKとEDA環境 | PDKの構成、EDAツールとの接続、DRC/LVS/ERCチェックフローの理解 |
| [７](d_chapter7_automation_and_verification/README.md) | 自動化と実装検証技術 | Lint、OpenLaneによる論理・物理検証とログ解析、CI/CDの導入例 |
| [８](d_chapter8_fsm_design_basics/README.md) | FSM設計（有限状態機械） | Moore/Mealy型、状態遷移図、Verilog記述までの構造的理解 |
| [９](d_chapter9_pll_and_clock_design/README.md) | PLLとクロック設計 | PLLの構造、周波数合成、ジッタ/スキュー、STAにおける設計配慮点 |

---

## 🛠 実践編　章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [1](e_chapter1_python_automation_tools/README.md) | Pythonによる自動化ツール群 | SPICEシミュレーション、特性プロット、OpenLaneログ解析など実務的自動化スクリプト群の実装例 |

---

## 📦 特別編：章構成一覧

| 章番号 | タイトル | 概要 |
|--------|----------|------|
| [1](f_chapter1_finfet_gaa/README.md) | 先端ノード（FinFET、GAA等） | 微細化対応の新構造トランジスタの物理・電気特性と設計影響 |
| [2](f_chapter2_chiplet_pkg/README.md) | チップレットと先端パッケージ技術 | 異種集積における2.5D/3Dパッケージ技術、TSV・インターポーザ事例 |

---

## 📄 ライセンス

本教材は **MITライセンス** に基づき、自由に使用・改変・再配布が可能です。  
教育機関・企業内研修などでの活用も歓迎します。

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
- **設計思想**：  
　デバイス・プロセスから制御理論、AI融合まで、構造的に貫く設計アーキテクチャの構築と教育展開に注力
- **連絡先**：
- GitHub：[Samizo-AITL](https://github.com/Samizo-AITL)  
- Email：shin3t72@gmail.com  
- お問い合わせは GitHub の [Issue](https://github.com/Samizo-AITL/Edusemi-v4x/issues) または [Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions) にてお気軽にどうぞ。

---
