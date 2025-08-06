---
layout: default
title: プロセス技術の進化と物理パラメータ推移  
---

---

# 📈 プロセス技術の進化と物理パラメータ推移  
## Evolution of Process Nodes and Key Physical Parameters

---

本資料では、**90nm以降のCMOSプロセス技術の進化**について、構造形式・物理パラメータ・主要課題の観点からまとめます。  
This document summarizes the **evolution of CMOS process technology since the 90nm node**, focusing on structure types, physical parameters, and key challenges.

---

## 📊 プロセス進化表｜Process Evolution Table

| ノード / **Node** | 構造 / **Structure** | 電源電圧 / **V<sub>DD</sub>** | **T<sub>ox</sub> [nm]** | 最小L / **Min L [nm]** | 主な特徴 / **Key Features** | 技術課題 / **Challenges** |
|------------------|----------------------|-------------------------------|--------------------------|-------------------------|------------------------------|----------------------------|
| **90nm**         | プレーナMOS<br>Planar MOS | 1.2V | ~2.0 | ~65 | NiSi導入、Strained-Si、LDD最適化<br>NiSi, strained-Si, optimized LDD | リーク電流、寄生容量、リソグラフィ限界<br>Leakage, parasitics, lithography |
| **65nm**         | プレーナMOS<br>Planar MOS | 1.1V | ~1.7 | ~50 | 高濃度チャネル、Low-k材料導入<br>Heavily doped channel, Low-k ILD | 短チャネル効果、配線遅延<br>SCE, interconnect delay |
| **45nm**         | プレーナMOS<br>Planar MOS | 1.0V | ~1.3 | ~35 | HKMG導入準備、ULK試験導入<br>HKMG prep, ULK intro | ゲート制御限界、Variability拡大<br>Gate control limit, variability |
| **32nm**         | HKMGプレーナ<br>HKMG Planar | 0.9V | ~1.0 | ~28 | High-k / Metal Gate正式採用<br>HK/MG full adoption | V<sub>t</sub>ばらつき、T<sub>inv</sub>制御困難<br>V<sub>t</sub> variation, T<sub>inv</sub> control |
| **22nm**         | FinFET（初代）<br>1st Gen FinFET | 0.85V | ~0.9 | ~20 | Tri-Gate構造採用、3Dチャネル化<br>Tri-Gate, 3D channel | Finばらつき、設計難度増加<br>Fin variation, design complexity |
| **14/10nm**      | 主流FinFET<br>Mainstream FinFET | 0.75–0.80V | ~0.8 | ~16 | マルチパターニング化、BEOL低誘電率化<br>Multi-patterning, low-k BEOL | SRAM縮小限界、配線混雑<br>SRAM scaling limit, routing congestion |
| **7nm**          | FinFET＋EUV<br>FinFET + EUV | 0.65–0.70V | ~0.7 | ~12 | EUV導入開始、LELELEパターン形成<br>EUV intro, LELELE patterning | 遮光膜設計、熱分布管理<br>Mask design, thermal issues |
| **5nm**          | GAA試験導入<br>GAA Pilot | 0.60–0.65V | ~0.6 | ~8 | Nanosheet構造試験導入<br>Nanosheet trials | シート幅制御、Routing困難<br>Sheet width control, poor routability |
| **3nm**          | GAA主流化<br>GAA Mainstream | 0.55–0.60V | ~0.5 | ~5 | TSMC/Samsungで本格導入<br>Adopted by TSMC & Samsung | 高密度寄生、ばらつき管理<br>Parasitics, process variability |
| **＜2nm**        | CFET構造開発中<br>CFET in R&D | ~0.5V以下 | ~0.4 | ~4 | NMOS・PMOS縦積層（stack）化<br>Complementary FET stacking | 熱干渉、電源/配線分離難<br>Thermal interference, power-routing split |

---

## 🧠 用語補足｜Glossary

| 用語 / Term | 意味 / Meaning |
|-------------|----------------|
| **HKMG** | High-k / Metal Gate：高誘電率材料とメタルゲート構造<br>High dielectric gate oxide and metal gate |
| **ULK** | Ultra Low-k：極低誘電率の層間絶縁膜<br>Extremely low-k ILD |
| **CFET** | Complementary FET：NMOS・PMOSの縦積層構造<br>Stacked NMOS and PMOS transistors |

---

## 🔗 関連補足資料｜Linked Appendices

| ファイル名 / Filename | 内容 / Description |
|------------------------|---------------------|
| [`appendixf1_01_finfetflow.md`](appendixf1_01_finfetflow.md) | FinFETプロセス詳細（48工程）<br>Detailed FinFET Process |
| [`appendixf1_02_gaaflow.md`](appendixf1_02_gaaflow.md) | GAAプロセス構造解説<br>GAA Nanosheet Process |
| [`appendixf1_03_finfet_vs_gaa.md`](appendixf1_03_finfet_vs_gaa.md) | FinFET vs GAA 比較<br>Structural & Process Comparison |
| [`appendixf1_04_cfet.md`](appendixf1_04_cfet.md) | CFET構造と課題整理<br>CFET Architecture and Issues |

---

## 🧩 今後の教材連携｜Planned Integration

- `appendix_f1_02_gaaflow.md` と連動し、**GAA構造と工程**の教育資料を拡張  
  Linked to `appendix_f1_02_gaaflow.md` for expanding GAA-related teaching
- `appendix_f1_04_cfet.md` で、**CFET縦構造と課題**を深掘り  
  Elaborated in `appendix_f1_04_cfet.md` on vertical stacking challenges
- `process_node_comparison.md` の進化系統図と連携し、90nm以前とも対比  
  Compared with pre-90nm data in `process_node_comparison.md`

---

## 📄 ライセンス｜License

MIT License に基づき、**非営利・教育目的での再配布・改変を歓迎**します。  
Released under the **MIT License**, permitting free use and modification for educational and non-commercial purposes.

---

📎 **[目次に戻る / Back to Appendix Index](./)**  
