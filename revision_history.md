---
layout: default
title: 改訂履歴 / ChangeLog  
---

---

# 📘 改訂履歴 / ChangeLog

このファイルは、Edusemi プロジェクトのバージョン別改訂内容を記録するものです。  
v4.0 以降は、新リポジトリ `Edusemi-v4x` にて管理されています。  
This file records version-based updates of the Edusemi project.  
From version 4.0 onward, updates are maintained in the new repository `Edusemi-v4x`.

---

## 🆕 v4.7（2025年11月16日 / November 16, 2025）  
**実践編 第7章「BSIM4 MOS特性解析基盤」を追加し、BSIM4ベースのMOS解析環境を教材化**  
**Added Practice Chapter 7 “BSIM4 MOSFET Characteristics Analysis Base” and formalized a BSIM4-based MOS analysis environment**

🔹 **実践編 第7章「BSIM4 MOS特性解析基盤」を新規追加**  
  - ngspice + BSIM4 モデルを用いた MOSFET 特性解析環境を構築  
  - Vg–Id、Vth（const-Id / sqrt(Id)）、gm/Id、Subthreshold Swing、DIBL を Python で自動抽出  
  - 図版（`vgid_all.png`、`gm_id.png`、`ss.png`、`dibl.png` など）を自動生成して `figs/` に保存  
  - 対応ディレクトリ：`e_chapter7_bsim4_analysis_base/`  
Added Practice Chapter 7 “BSIM4 MOSFET Characteristics Analysis Base”  
  - Built a MOSFET analysis environment using ngspice with BSIM4 models  
  - Automated extraction of Vg–Id, Vth (const-Id / sqrt(Id)), gm/Id, Subthreshold Swing, and DIBL via Python  
  - Auto-generates plots (e.g., `vgid_all.png`, `gm_id.png`, `ss.png`, `dibl.png`) into the `figs/` directory  
  - Directory: `e_chapter7_bsim4_analysis_base/`

🔹 **フォルダ構成とスクリプト群を教材向けに整備**  
  - `spice/netlists/`：BSIM4用ネットリスト（nMOS / pMOS、Vd=0.05V / 1.0V）  
  - `data/raw/`：`wrdata` 出力ログ（`vgid_*.log`）を格納  
  - `src/`：`plot_vgid.py`、`gm_id.py`、`ss_extract.py`、`dibl_extract.py` などの解析スクリプト  
  - `figs/`：全自動生成図版を集約  
Organized folder structure and scripts for educational use  
  - `spice/netlists/`: BSIM4 netlists (nMOS / pMOS, Vd=0.05V / 1.0V)  
  - `data/raw/`: `wrdata` output logs (e.g., `vgid_*.log`)  
  - `src/`: analysis scripts such as `plot_vgid.py`, `gm_id.py`, `ss_extract.py`, and `dibl_extract.py`  
  - `figs/`: collection of all auto-generated plots

🔹 **実践編「Practice」目次に第7章を追加し、リンク構造を更新**  
  - 第0〜6章と同形式のバッジリンク（View Site / View Repo）を第7章にも適用  
  - 日本語タイトル＋英語サブタイトル併記で、他章と構成を統一  
Updated the Practice table of contents to include Chapter 7  
  - Added Chapter 7 with the same badge-style links (View Site / View Repo) as Chapters 0–6  
  - Unified structure with Japanese title plus English subtitle

🔹 **教材ページ `e_chapter7_bsim4_analysis_base` の README を整備**  
  - 目的・フォルダ構成・使用手順（ngspice → Python）・生成図一覧を明記  
  - 「環境構築（第0章）→ Sky130/SPICE実験（第2章・第6章）→ BSIM4解析（第7章）」の学習接続を提示  
Refined the README for `e_chapter7_bsim4_analysis_base`  
  - Documented objectives, folder structure, usage flow (ngspice → Python), and generated figures  
  - Clarified the learning path from environment setup (Chapter 0) and Sky130/SPICE practice (Chapters 2 & 6) to BSIM4 analysis (Chapter 7)

---

## 🆕 v4.6（2025年11月10日 / November 10, 2025）  
**実践編 第0章〜第6章の完全統合と、環境構築ドキュメント（第0章）を全面整備**  
**Integrated all Practice Chapters (0–6) and fully rebuilt the Environment Setup documentation**

🔹 **実践編 第0章「環境構築とツールセット」フル教材を追加**  
  - Python / VS Code / Sky130 PDK / ngspice  
  - WSL2 / Docker / OpenLane  
  - Magic / Netgen / KLayout  
  - 9構成ファイル（01〜09）を体系化  
  - GitHub Pages に完全対応した Jekyll 形式で整備  

🔹 **実践編の全章リンクを更新（第0〜6章）**  
  - `Practice` 目次に Chapter 0 を追加  
  - 各章の View Site / View Repo バッジを統一  
  - ディレクトリ構成を v4.6 仕様に統一  

🔹 **Mermaid 図・セットアップ図版の統一アップデート**  
  - 01〜09 の各節に環境構成図を追加  
  - Sky130 / OpenLane / ngspice 依存関係を統一表現に変更  

🔹 **改訂履歴ページに “実践編 第0章〜第6章” の反映**  
  - 実践編の教材更新が ChangeLog に追従  
  - 教育用の理解構造（環境 → SPICE → PDK → OpenLane → DRC/LVS）を一貫化  

🔹 **ファイル生成（*.md）を GitHub Pages 互換で再構成**  
  - front matter（YAML）を統一  
  - レイアウト `default` 対応  
  - CSS / 絵文字 / 表記スタイルの統一  
  
---

## 🆕 v4.5（2025年9月6日 / September 6, 2025）  
**実践編に第6章「SPICE実践演習」を追加し、デバイス特性・CMOSインバータ・WBG比較を教材化**  
**Added Practice Chapter 6: SPICE Exercises, covering device I–V, CMOS inverter, and WBG switching comparisons**

🔹 実践編 第6章「SPICE実践演習」を新設  
  - `devices/nmos_iv_characteristics.spice` による Id–Vds / Id–Vgs 特性  
  - `circuits/inv_cmos_finfet.spice` / `inv_cmos_gaa.spice` による FinFET vs GAA インバータ比較  
  - `power/gan_vs_sic_switching.spice` による GaN vs SiC スイッチング特性評価  
  - 結果グラフを PNG 出力し、教材ページに統合  
Established Practice Chapter 6: SPICE Exercises  
  - Id–Vds / Id–Vgs via `devices/nmos_iv_characteristics.spice`  
  - FinFET vs GAA inverter comparison (`inv_cmos_finfet.spice` / `inv_cmos_gaa.spice`)  
  - GaN vs SiC switching analysis (`gan_vs_sic_switching.spice`)  
  - Generated PNG plots and embedded them in the materials

🔹 実践編 README の章一覧を更新し、第6章を追加  
  - 「Practice」表に SPICE 実習リンクを追加  
  - GitHub Pages / Repo 双方のバッジリンクを整備  
Updated Practice README  
  - Added Chapter 6 to Practice table  
  - Linked GitHub Pages and Repo with badges

---

## 🆕 v4.4（2025年8月14日 / August 14, 2025）  
**関連プロジェクト・著者情報・フィードバック部分のUI改善と英語版整備**  
**Improved UI for Related Projects, Author Info, and Feedback sections; added English version**

🔹 関連プロジェクト一覧を **「View Site / View Repo」バッジ式** に統一  
  - 日英両版に対応  
  - 外部リンクとリポジトリリンクを視覚的に明確化  
Standardized Related Projects list with “View Site / View Repo” badges  
  - Supports both JP and EN versions  
  - Clear visual separation of site and repo links

🔹 著者情報テーブルの英語版を作成  
  - 名前・経歴・専門領域・連絡先を日英併記で明確化  
Added English Author Info table  
  - Name, career, expertise, and contact in bilingual format

🔹 フィードバック＆改訂履歴のリンクをバッジ化  
  - GitHub Discussions と ChangeLog をカラー識別  
Converted Feedback & ChangeLog links into badges  
  - Color-coded GitHub Discussions and ChangeLog links

🔹 英語版 `README.md` に対応する構造を統一  
  - 日本語版との差分を最小化  
Unified structure in English `README.md`  
  - Minimized differences from JP version

---

## 🆕 v4.3（2025年8月1日 / August 1, 2025）  
**アナログ設計・製造差別化・先端ノード・メモリ評価を強化し、応用編と特別編を拡充**  
**Expanded analog design, process-driven optimization, advanced nodes, and memory evaluation – strengthening the Applied and Special Editions**

🔹 応用編 第5章「アナログ／ミックスドシグナル設計」章構成を刷新  
  - 5.0：アナログ設計の課題と対策（ノイズ・クロストーク等）  
  - 5a：0.18μm AMS設計技法（ばらつき・1/fノイズ・マッチング）  
  - 5b：製造技術によるアナログ差別化（ノイズ低減）  
  - 各章に README・教材ファイル・章リンクを整備  
Refactored structure of Applied Chapter 5  
  - 5.0: Analog design challenges and countermeasures  
  - 5a: 0.18μm AMS techniques (mismatch, 1/f noise)  
  - 5b: Analog differentiation via process technology  
  - Added README, learning materials, and links

🔹 応用編 第5a章に AMS設計構想教材を追加  
  - Poly抵抗ばらつきと設計工夫を教材化  
  - ノード選定・レイアウト戦略・ばらつき抑制技術  
  - 対応：`d_chapter5a_analog_mixed_signal/`  
Added conceptual materials to Chapter 5a  
  - Focused on poly resistor variation and design solutions  
  - Topics: node selection, layout techniques  
  - Directory: `d_chapter5a_analog_mixed_signal/`

🔹 応用編 第5b章「製造技術によるアナログ差別化」を新設  
  - 1/fノイズ低減による製造起点の改善  
  - 対応：`d_chapter5b_process_driven_design/`  
Established Chapter 5b: Analog Differentiation via Process  
  - Topics include 1/f noise reduction 
  - Directory: `d_chapter5b_process_driven_design/`

🔹 応用編 第1章「メモリ技術」に FeRAM プロセス教材を追加  
  - `0.18μm FeRAM` の48工程を日英併記で教材化  
  - Pt/PZT/Ti構造、Wプラグ、Coサリサイドなどを網羅  
  - 対応：`chapter1_memory/feram_0.18um_process.md`  
Added FeRAM process to Chapter 1  
  - Full 0.18μm FeRAM flow (48 steps), bilingual  
  - Includes Pt/PZT/Ti, W plug, Co salicide  
  - File: `chapter1_memory/feram_0.18um_process.md`

🔹 応用編 第4章に「レイヤー整合・オーバーレイ」資料を追加  
  - `layer_overlay_reference.md` に主要レイヤーとMask整合性を一覧化  
  - DFM設計・PDK学習に有用  
Added layer overlay reference to Chapter 4  
  - Tabulated key layers and overlay relations  
  - Supports DFM and PDK education

🔹 特別編 第1章に FinFET / GAA / CFET 比較教材を追加  
  - `appendixf1_03_finfet_vs_gaa.md`：構造・電気特性・設計影響を比較  
  - `appendixf1_04_cfet.md`：GAA以降の次世代構造 CFET を教材化  
  - 特別編 第1.1〜1.4節とのリンク整備  
Added comparison materials to Special Chapter 1  
  - FinFET vs GAA (structure, properties, implications)  
  - CFET overview and roadmap  
  - Linked to Sections 1.1–1.4

🔹 特別編 第2a章「SystemDKにおける物理制約管理」を新設  
  - SI/PI、熱、応力、EMI/EMCなど複合物理制約の統合設計  
  - Chiplet時代における System Design Kit（SystemDK）の概念整理  
  - PoC設計演習を含む階層的教材を構成  
  - 対応：`f_chapter2a_systemdk/`  
Established Special Chapter 2a: Physical Constraint Management in SystemDK  
  - Covers SI/PI, thermal, mechanical, and EMI/EMC constraints  
  - Introduces System Design Kit (SystemDK) in the chiplet era  
  - Includes PoC-based hierarchical learning materials  
  - Directory: `f_chapter2a_systemdk/`

---

## 🆕 v4.2（2025年7月13日 / July 13, 2025）  
**特別編に第6章・第7章を追加し、設計実装から製品化ドキュメントまでを網羅**  
**Added Chapters 6 and 7 to the Special Edition, covering implementation to productization**

🔹 特別編 第6章「ピエゾアクチュエータ制御システム」教材を追加  
  - FSM制御・分極・ヒステリシス補償・COF実装を統合  
  - 対応：`f_chapter6_actuator_system/`  
Added Chapter 6: Piezo actuator control system  
  - Includes FSM, polarization, hysteresis, COF  
  - Directory: `f_chapter6_actuator_system/`

🔹 特別編 第7章「完成体製品における開発ドキュメントとワークフロー」教材を追加  
  - BOM、DR、Gate管理、構成管理までを体系化  
  - 対応：`f_chapter7_product_docs/`  
Added Chapter 7: Product development documentation  
  - Includes BOM, design reviews, mass production control  
  - Directory: `f_chapter7_product_docs/`

🔹 特別編 READMEの章構成を更新  
🔹 PDM/PLM図、RACI表、Mermaid ワークフローを教材に実装  
Updated README chapter list  
Added PDM/PLM diagrams, RACI chart, Mermaid workflow

> 💬 補足：第6・第7章は主にアクチュエータ制御・製品開発管理が対象であり、  
> 半導体プロセスや設計技術とは直接関係しないため、v4.3 以降の半導体教材の範囲からは除外。  
>  
> **Note:** Chapters 6 and 7 focus on actuator control and product workflow.  
> They are **not directly related to semiconductor technology**, and are thus **excluded from semiconductor-focused updates in v4.3 and beyond**.

---

## v4.1（2025年7月12日）  
**特別編：ピエゾアクチュエータ制御教材を追加し、実装系の教育対象を拡張**

🔹 特別編 第6章「ピエゾアクチュエータ制御システム」を新規追加  
  - 分極処理、ヒステリシス補償、FSM制御、COF実装を統合  
  - 教材形式：`edu_actuator_system.md`（GUI／RTL展開と連携予定）  
🔹 ディレクトリ名を `f_chapter6_actuator_system/` に統一  
🔹 特別編の章構成表を更新（README追記）  
🔹 Markdown文字化け対策として UTF-8 BOM出力を実施

---

## v4.0（2025年7月7日）  
**Edusemi-v4x：構造的理解と現代実習のための全面再構成**

🔹 教材構成を再設計し、新リポジトリとして独立  
🔹 基礎編・応用編・実践編・特別編の4部体系に統合  
🔹 Sky130・OpenLane・Python・ChatGPTによる実習環境を導入  
🔹 各章README整備、PoC設計・FSM構成、PDK・EDA連携まで拡充  
🔹 ChatGPTとの対話学習を前提とした構造に最適化

---

## 🕰 過去の改訂（旧Edusemiリポジトリ）

### v3.0（2025年7月3日）
🔹 第0章「半導体物性の基礎」を正式追加  
🔹 第1章を論理中心に再構成  
🔹 トップREADMEの目次・構成を全面見直し  

### v2.0（2025年6月15日）  
🔹 章構成と教材群を体系化（第1章〜第6章 + 特別編 + history）  
🔹 各章にREADMEと.md教材を導入  

### v1.0（2025年6月1日）  
🔹 初期教材試作・GitHub展開開始  

---

## 📌 今後の見通し（予定）

- v4.x 系列において、以下を段階的に追加予定：
  - FSM設計補強、図版整備、回路図作図の統一
  - OpenLaneログ解析の自動化、CI/CD活用例の強化
  - 英語版教材（v5.0）や高校高専向け簡易教材の展開

---

## 📝 連絡・提案

教材へのご意見・活用実績・改善案などは、GitHubの [Issue](https://github.com/Samizo-AITL/Edusemi-v4x/issues) または [Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions) にてご連絡ください。

---
