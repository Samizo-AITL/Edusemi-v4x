# 🌟 特別編 | Special Chapters

---

## 🧬 第1章：先端ノード技術（FinFET、GAA、CFET）
*Advanced Node Technologies – FinFET, GAA & CFET*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa)

### 📖 概要 | Overview
FinFET・GAA・CFET構造の物理特性・電気特性・設計影響を体系的に解説。  
プレーナMOSの限界を超える先端CMOS技術を紹介。

### 📂 節構成 | Chapter Structure (v1.1)
| 節番号 | ファイル名 / Filename | 内容概要 / Description |
|-------|----------------------|------------------------|
| 1.1 | f1_1_planar_limitations.md | プレーナMOSの限界と微細化の壁 / Limits of Planar MOSFETs |
| 1.2 | f1_2_finfet.md | FinFET構造の原理とプロセス概要 / FinFET Structure & Process |
| 1.3 | f1_3_gaa.md | GAA構造とMulti-Nanosheet技術 / GAA and Nanosheet Technology |
| 1.4 | f1_4_comparison.md | プレーナ vs FinFET vs GAAの特性比較 / Comparison of Planar / FinFET / GAA |

---

## 🛠 第2章：チップレットと先端パッケージ技術
*Chiplets and Advanced Packaging*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg)

### 📖 概要 | Overview
2.5D/3D実装技術やチップレットアーキテクチャの設計・実装・信頼性を体系的に解説。  
異種集積による柔軟な設計とスケーラビリティを可能にする技術群。

### 📂 節構成 | Main Sections
| 番号 | ファイル名 / Filename | 内容概要 / Description |
|------|----------------------|------------------------|
| 2.1 | f2_1_overview.md | チップレット化の背景と技術潮流 / Background and technology trends |
| 2.2 | f2_2_25d_pkg.md | 2.5D実装技術（CoWoS、インターポーザ） / 2.5D integration technologies (CoWoS, interposer) |
| 2.3 | f2_3_3d_pkg.md | 3D積層技術（TSV、ハイブリッド接合） / 3D stacking (TSV, hybrid bonding) |
| 2.4 | f2_4_pkg_case_study.md | 商用事例（AMD、Intel、Appleなど） / Commercial cases (AMD, Intel, Apple, etc.) |
| 2.5 | f2_5_design_challenges.md | 熱設計・テスト・タイミング課題 / Thermal, test, and timing challenges |

---

## 📦 第2a章：SystemDKにおける熱・応力・ノイズ制約の設計対応
*Design Handling of Thermal, Stress, and Noise Constraints in SystemDK*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk)

### 📖 概要 | Overview
System Design Kit (SystemDK) の概念と、物理制約（SI/PI、熱、応力、EMI/EMC）の設計的取り扱いを解説。

### 📂 節構成 | Section Structure
| 番号 | ファイル名 / Filename | タイトル / Title |
|------|----------------------|------------------|
| 2a.1 | f2a_1_systemdk_overview.md | SystemDKの全体像と設計階層 / Overview and Hierarchy of SystemDK |
| 2a.2 | f2a_2_sipi.md | SI/PIとPDN構造 / Signal/Power Integrity and PDN Design |
| 2a.3 | f2a_3_thermal.md | 熱拡散と材料分布 / Thermal Behavior and Material Distribution |
| 2a.4 | f2a_4_mechanical.md | 実装応力と界面信頼性 / Mechanical Stress and Interface Reliability |
| 2a.5 | f2a_5_emi_emc.md | EMI/EMC設計原則 / Principles of EMI/EMC Design |

---

## 🧠 第3章：FSM×PID×LLMによる統合制御システムのSoC実装手法
*SoC Implementation of Integrated Control System with FSM × PID × LLM*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsysten)

### 📖 概要 | Overview
AITL-H三層制御アーキテクチャをベースに、機能分離・階層連携・SoC統合の手法を学習。

### 📂 節構成 | Chapter Structure
| 節番号 | 日本語タイトル | 英語タイトル |
|--------|--------------|--------------|
| 3.1 | AITL-Hアーキテクチャと層分離設計 | AITL-H Architecture and Layered Design |
| 3.2 | FSM構成とRTLモジュール設計 | FSM Design and RTL Module Structure |
| 3.3 | PID制御モジュールの設計 | PID Controller Design |
| 3.4 | LLMインタフェース設計 | LLM Interface Design |
| 3.5 | SoC統合とシミュレーション | SoC Integration and Simulation |

---

## 📘 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装
*RTL-to-GDSII Implementation of FSM×PID×LLM Control System with OpenLane*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane)

### 📖 概要 | Overview
Sky130 PDKを用い、FSM・PID・統合SoCモジュールの配置配線（RTL-to-GDSII）を実践。

### 📂 節構成 | Chapter Structure and Overview
| 節番号 | タイトル（JP） | Title (EN) | 概要 / Summary |
|--------|--------------|------------|---------------|
| 4.1 | OpenLane導入とプロジェクト構成 | Introduction to OpenLane and Project Setup | ディレクトリ構成とconfig準備の基本 |
| 4.2 | FSMモジュールの配置配線 | Place-and-Route of FSM Module | FSM単体の配置配線（RTL-to-GDSII） |
| 4.3 | PIDモジュールの配置配線 | Place-and-Route of PID Module | PID制御モジュールのレイアウト実装 |
| 4.4 | SoC統合モジュールの実装 | Implementation of Integrated SoC | FSM＋PID統合回路のGDSII化 |
| 4.5 | 設計評価レポートと比較 | Design Evaluation and Comparison | 面積・DRC・タイミング比較分析 |

---

## 🧪 第5章：PDKとレイアウト検証による物理整合とDFM設計指針
*Physical Verification and DFM Design Guidelines with PDK*  
[📂 View Repo](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm)

### 📖 概要 | Overview
Sky130 PDKによるレイアウト検証と、量産性を考慮したDFM設計指針を習得。

### 📂 節構成 | Section Overview
| 節番号 | タイトル（JP） | Title (EN) | 概要 / Summary |
|--------|--------------|------------|---------------|
| 5.1 | PDK構造の理解とSky130レイヤー体系 | Understanding PDK and Sky130 Layer System | レイヤー命名・マスク体系を解説 |
| 5.2 | GDS可視化と階層解析 | GDS Visualization and Hierarchy Analysis | Magic/KLayoutによる階層構造の確認 |
| 5.3 | レイアウト検証の基礎 | Basics of Layout Verification | DRC / LVS / ERCの仕組みと活用法 |
| 5.4 | DFM設計指針の習得 | Learning DFM Design Principles | 寄生・ストレス・量産対応設計を実践 |

---
