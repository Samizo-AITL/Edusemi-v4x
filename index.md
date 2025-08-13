---
layout: default
title: Edusemi-v4x/index.md
---

---

# 🎓 **Edusemi-v4x｜半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*

📄 **[English README →](./en/README.md)**  

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

| 🧭 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| **🧭 1** | **半導体物性と材料基礎**<br>*Semiconductor Physics & Materials* | バンド構造・PN接合・MOS電界効果 |
| **🧭 2** | **デジタル論理と回路設計**<br>*Digital Logic & Circuit Design* | 組み合わせ回路・順序回路・FSM・HDL |
| **🧭 3** | **プロセス技術と微細化制約**<br>*Process Technology & Scaling* | ノード変遷・配線・リソ・信頼性 |
| **🧭 4** | **MOSトランジスタ特性**<br>*MOS Characteristics* | 寸法・特性・PDK・デザインルール |
| **🧭 5a** | **仕様策定とIF設計**<br>*Spec Definition & Interface Design* | 上流工程・モジュール選定・PoC接続 |
| **🧭 5** | **SoC設計フロー**<br>*SoC Design Flow* | RTL・P&R・DRC/LVS・タイミング |
| **🧭 6** | **テスト・パッケージ**<br>*Test & Packaging* | ETEST・不良解析・信頼性試験・出荷 |
| **🧭 7** | **デザインレビューと組織連携**<br>*Design Review & Collaboration* | SRAM不良事例・DR構造・合意形成 |

---

## 🧩 **応用編 | Applications**
> 基礎を踏まえて**メモリ・高耐圧・ESD・アナログ設計**など専門領域へ展開します。  
> *Expands into specialized areas such as memory, high-voltage, ESD, and analog design.*

| 🧩 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| **🧩 1** | **メモリ技術**<br>*Memory Technologies* | SRAM・DRAM・FeRAM・MRAM |
| **🧩 2** | **高耐圧デバイス**<br>*High-Voltage Devices* | LDMOS・電界制御・高電圧設計 |
| **🧩 3** | **ESD設計**<br>*ESD Protection Design* | 保護素子・破壊事例・試験規格 |
| **🧩 4** | **レイアウト最適化**<br>*Layout Optimization* | CMPダミー・IRドロップ・ラッチアップ |
| **🧩 5** | **アナログ／MIX信号**<br>*Analog / Mixed-Signal* | アナログ設計・ノイズ・混載設計 |
| **🧩 5a** | **0.18μm AMS設計技法**<br>*0.18μm AMS Design* | ばらつき・マッチング・1/fノイズ |
| **🧩 5b** | **製造起点のAMS差別化**<br>*AMS Differentiation from Manufacturing* | 1/fノイズ低減・製造技術応用 |
| **🧩 6** | **PDKとEDA環境**<br>*PDK & EDA Environment* | DRC/LVS/ERC・PDK構成 |
| **🧩 7** | **自動化と検証**<br>*Automation & Verification* | OpenLane・CI/CD・Lint |
| **🧩 8** | **FSM設計**<br>*FSM Design* | Moore/Mealy・状態遷移図・Verilog |
| **🧩 9** | **PLLとクロック**<br>*PLL & Clock Design* | PLL構造・ジッタ・STA配慮 |

---

## 🛠 **実践編 | Practice**
> **Python自動化・Sky130実験・OpenLane設計**など、実務に近い演習を通じてスキルを定着させます。  
> *Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design.*

| 🛠 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| **🛠 1** | **Python自動化ツール**<br>*Python Automation Tools* | SPICE解析・OpenLaneログ処理 |
| **🛠 2** | **Sky130実験**<br>*Sky130 Experiments* | Vg–Id・Vth推定・BTI/TDDB評価 |
| **🛠 3** | **OpenLane実習**<br>*OpenLane Practice* | 合成〜配置配線〜GDS出力 |
| **🛠 4** | **PoC設計展開**<br>*PoC Design Development* | FSM・MUX・Adder・テスト |
| **🛠 5** | **評価とレポート**<br>*Evaluation & Reporting* | 面積・波形・タイミング・DRC/LVS |

---

## 📦 **特別編 | Special Topics**
> **先端ノード・チップレット・統合制御SoC**など最先端テーマを扱います。  
> *Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.*

| 📦 章 / Chapter | 📚 タイトル / Title | 📝 概要 / Summary |
|----|------------|----------------|
| **📦 1** | **先端ノード**<br>*Advanced Nodes* | FinFET・GAA・CFETと設計影響 |
| **📦 2** | **チップレットと先端パッケージ**<br>*Chiplets & Advanced Packaging* | 2.5D/3D・TSV・異種集積 |
| **📦 2a** | **SystemDK実装制約設計**<br>*SystemDK Design Constraints* | SI/PI・熱・応力・EMI/EMC |
| **📦 3** | **統合制御SoC実装**<br>*Integrated Control SoC* | FSM×PID×LLM（AITL） |
| **📦 4** | **OpenLane実装**<br>*OpenLane Implementation* | 統合制御RTLの配置配線 |
| **📦 5** | **DFM設計**<br>*Design for Manufacturability* | DRC・LVS・DFM指針・Sky130 |

---

## 🔗 **関連プロジェクト | Related Projects**
> Edusemiと連動し、制御理論・社会構造・先端技術を横断的に学べる姉妹プロジェクト群。  
> *Sister projects linked with Edusemi, covering control theory, socio-industrial structures, and advanced technologies.*

| 🌐 プロジェクト / Project | 概要 / Overview | 主な特徴・内容 / Key Features |
|--------------|------|----------------|
| 🌐 [**Edusemi-Plus**](https://github.com/Samizo-AITL/edusemi-plus) | 地政学・製品戦略・AI・量子・投資など、産業構造を読み解く応用教材<br>*Applied learning materials analyzing geopolitics, product strategy, AI, quantum, and investment.* | - Apple Silicon・CHIPS法・Cryo-CMOSの実例解説<br>- 技術だけでなく社会との接点や背景を探究 |
| 🎛️ [**EduController**](https://github.com/Samizo-AITL/EduController) | 制御理論（PID・状態空間）からAI制御（NN・RL・LLM）まで網羅<br>*Covers control theory (PID, state-space) to AI control (NN, RL, LLM).* | - PoC設計・OpenLane制御実装との連動<br>- Pythonによる設計演習・RTL検証・FSM生成支援 |
| 🤖 [**AITL-H**](https://github.com/Samizo-AITL/AITL-H) | FSM（本能）＋PID（理性）＋LLM（知性）の三層制御アーキテクチャ<br>*Three-layer control architecture: FSM (instinct) + PID (reason) + LLM (intelligence).* | - 人型ロボット・統合制御のPoC実装<br>- Edusemi特別編3・4章と構造的に連携 |

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

💬 **[Edusemi教材に関する議論はこちら → Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)**  
📄 **[改訂履歴 / ChangeLog](revision_history.md)**

