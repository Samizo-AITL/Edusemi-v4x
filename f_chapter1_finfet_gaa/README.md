# 🧬 特別編 第1章：先端ノード技術（FinFET、GAA、CFET）  
## 📘 Chapter 1 Special Edition: Advanced Node Technologies – FinFET, GAA & CFET

---

## 🔰 概要 / Overview

**本章では、FinFET・GAA（Gate-All-Around）・CFET（Complementary FET）に代表される微細化対応の新トランジスタ構造について、物理特性・電気特性・設計影響の観点から体系的に解説します。**  
これらの構造は、プレーナMOSのスケーリング限界を超え、先端CMOSの道を拓くキーテクノロジーです。

> **In this chapter**, we provide a systematic explanation of **FinFET, Gate-All-Around (GAA), and Complementary FET (CFET)** transistor structures, focusing on their **physical structure**, **electrical characteristics**, and **design impacts**.  
These 3D transistor technologies are essential for pushing beyond the limits of traditional planar CMOS scaling.

**📌 対象読者 / Intended Audience**  
- プロセスエンジニア / Process Engineers  
- 回路設計者 / Circuit Designers  
- 半導体教育者・研究者 / Semiconductor Educators & Researchers  

---

## 📚 節構成 / Chapter Structure（v1.1）

| 節番号 / Section | ファイル名 / Filename                              | 内容概要 / Description |
|------------------|-----------------------------------------------------|-------------------------|
| 1.1              | [`f1_1_planar_limitations.md`](f1_1_planar_limitations.md) | プレーナMOSの限界と微細化の壁<br>Limits of Planar MOSFETs |
| 1.2              | [`f1_2_finfet.md`](f1_2_finfet.md)                   | FinFET構造の原理とプロセス概要<br>FinFET Structure & Process |
| 1.3              | [`f1_3_gaa.md`](f1_3_gaa.md)                         | GAA構造とMulti-Nanosheet技術<br>GAA and Nanosheet Technology |
| 1.4              | [`f1_4_comparison.md`](f1_4_comparison.md)           | プレーナ vs FinFET vs GAAの特性比較<br>Comparison of Planar / FinFET / GAA |
| 1.5              | [`f1_5_cfet.md`](f1_5_cfet.md)                       | CFET構造とスタック型MOSの展望<br>CFET Structure and Outlook for Stacked MOS |

---

## 🔄 関連章へのリンク｜Related Chapter

| 章タイトル / Title | リンク / Link |
|--------------------|---------------|
| 📘 **基礎編 第3章：プロセス技術と設計限界の理解**<br>📘 *Chapter 3: Process Technology and Design Limits* | [➡️ README（基礎編 第3章）](../chapter3_process_evolution/README.md) |

本章は、基礎編第3章における「プレーナMOS〜90nmノード」までのプロセス理解を前提に、**FinFET/GAA/CFETへの進化**を位置づける内容です。  
This chapter builds upon the process knowledge from Chapter 3 and extends it to FinFET, GAA, and CFET structures.

---

## 📎 補足資料 / Appendix

| ファイル名 / Filename                                     | 内容概要 / Description |
|-----------------------------------------------------------|-------------------------|
| [`appendix_f1_node_evolution.md`](appendix_f1_node_evolution.md) | 90nm以降のプロセス進化と物理パラメータ一覧<br>Evolution of Process Nodes (90nm–CFET) |
| [`appendixf1_01_finfetflow.md`](appendixf1_01_finfetflow.md)     | FinFETプロセスフロー詳細（48ステップ）<br>Detailed FinFET Process (48 Steps) |
| [`appendixf1_02_gaaflow.md`](appendixf1_02_gaaflow.md)           | GAA Multi-Nanosheet FETプロセス<br>GAA Multi-Nanosheet Process |
| [`appendixf1_03_finfet_vs_gaa.md`](appendixf1_03_finfet_vs_gaa.md) | FinFETとGAAの工程・特性・設計比較<br>Comparison of FinFET vs GAA |
| [`appendixf1_04_cfet.md`](appendixf1_04_cfet.md)                 | CFETの構造進化と技術的課題<br>CFET Structure Evolution and Technical Challenges |
| [`appendixf1_05_node_params.md`](appendixf1_05_node_params.md)   | FinFET / GAA 各ノード世代の構造・電気パラメータ一覧<br>Node-wise Parameters for FinFET and GAA |

---

## 🖼️ 図版フォルダ / Image Directory

構造断面図、ゲート包囲図、スケーリングロードマップ等を `images/` フォルダに順次格納します。  
Structure diagrams, gate coverage illustrations, and scaling roadmaps will be included in the `images/` directory.

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)
