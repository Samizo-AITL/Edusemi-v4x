# 💾 応用編 第1章｜メモリ技術の構造と選定指針  
# 💾 Applied Chapter 1 | Memory Technologies – Structure and Selection Guidelines

---

## 📘 概要｜Overview

SoC（System-on-Chip）設計において、演算処理回路や制御回路だけでなく、  
**適切なメモリ技術の選定と配置**が、製品の「**性能**」「**コスト**」「**消費電力**」に直結します。

In SoC (System-on-Chip) design, not only logic and control units but also  
**appropriate selection and integration of memory** directly affect product **performance**, **cost**, and **power**.

本章では、**高速なSRAMから大容量3D NANDまで**の代表的なメモリ技術を取り上げ、  
**構造・特性・用途・SoC統合方法**の観点から比較し、  
**設計上の判断力と選定力**を養うことを目的とします。

This chapter covers representative memory technologies from **high-speed SRAM to large-scale 3D NAND**,  
with the aim of fostering the ability to **compare and choose memory structures**  
based on **architecture, performance, applications, and SoC integration methods**.

---

## 🎯 学習目標｜Learning Objectives

| 日本語 – Japanese                                                                                              | English – English                                                                                             |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| - 各種メモリ（SRAM / DRAM / FeRAM / MRAM / NAND）の**構造と動作原理**を理解する                                 | - Understand **structure and operation principles** of SRAM, DRAM, FeRAM, MRAM, and NAND                     |
| - **速度・不揮発性・書換耐性・面積効率・消費電力**などの**評価軸を比較検討**できるようになる                    | - Be able to compare memory options using metrics such as **speed, non-volatility, endurance, area, power** |
| - SoCにおける**メモリ統合・選定・接続方法**を習得し、設計判断の基盤を築く                                       | - Learn how to **integrate and choose memory** in SoC design with sound engineering judgment                |

---

## 📚 節構成｜Chapter Structure

| No. | セクション名（日本語）                             | Section Title (English)                                    | リンク |
|-----|----------------------------------------------------|-------------------------------------------------------------|--------|
| 1.1 | SRAM（Static RAM）：高速・揮発                      | High-speed volatile memory for cache/registers              | [📎](sram.md) |
| 1.2 | DRAM（Dynamic RAM）：大容量・リフレッシュ必要       | High-density memory requiring refresh (e.g., DDR, LPDDR)    | [📎](dram.md) |
| 1.3 | FeRAM：強誘電体RAM・不揮発                          | Non-volatile memory for low-power / analog-mixed LSI        | [📎](feram.md) |
| 1.4 | MRAM：磁気RAM・不揮発・高耐久                        | Durable non-volatile memory (STT/SOT); eFlash replacement    | [📎](mram.md) |
| 1.5 | 3D NAND：大容量・不揮発・ストレージ用途              | Large-capacity flash for storage (eMMC, SSD, UFS, etc.)     | [📎](3dnand.md) |

---

## 🧠 設計観点のトピック｜Design-Oriented Topics

- 組込みメモリ（SRAM/FeRAM/MRAM）と外部メモリ（DRAM/NAND）の**構造的違い**  
  Structural differences between embedded and external memory types  
- **速度・揮発性・耐久性・面積効率・電力**によるトレードオフ分析  
  Trade-off analysis on speed, volatility, endurance, area, and power  
- **OpenLaneやSky130 PDKを用いたSRAMマクロ統合**の実例  
  Example of SRAM macro integration using OpenLane and Sky130 PDK  
- **eFlash代替としてのeMRAM、センサSoCへのFeRAM応用事例**  
  Case studies: eMRAM as eFlash replacement, FeRAM in sensor SoCs  
- **NAND制御におけるFTL、ECC、干渉対策技術**  
  Techniques for NAND management: FTL (Flash Translation Layer), ECC, disturbance mitigation  

---

## 🔗 関連資料・技術アーカイブ｜Related Links & Technical Archives

| 資料・章 | 概要 | 本章との関係 |
|----------|------|-------------|
| [第4章：MOSトランジスタ特性](../chapter4_mos_characteristics/) | MOS構造とスイッチング動作 | メモリセル（6T, 1T1C, MTJ等）理解に必要 |
| [第5章：SoC設計フローとEDAツール](../chapter5_soc_design_flow/) | 合成・PDK活用・IP統合 | SRAMマクロの組込みに関与 |
| [第6章：テスト・パッケージ技術](../chapter6_test_and_package/) | 信頼性試験・不良解析 | 書換寿命や保持特性評価と接続 |
| [`DRAM_Startup_64M_1998.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in1998/DRAM_Startup_64M_1998.md) | **1998年 DRAM立ち上げ記録** | 0.25µm世代のプロセス改善とリフレッシュ信頼性課題を記録 |
| [`VSRAM_2001.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/VSRAM_2001.md) | **2001年 擬似SRAM（VSRAM）技術** | DRAM応用による組込み用途SRAMの設計と歩留まり対策事例 |
| [`MoSys_1T_SRAM_Links.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/MoSys_1T_SRAM_Links.md) | **Mosys社1T-SRAM技術リンク集** | SRAMマクロ代替候補としての外部参照資料群 |

---

## 🧩 章のキーワード｜Keywords

SRAM, DRAM, FeRAM, MRAM, NAND, 1T1C, 6T, PDK, OpenLane, Non-volatile, Refresh, SoC Integration, FTL, ECC


---

© 2025 Shinichi Samizo / MIT License

---

🏘 [応用編 第1章：メモリ技術｜Applied Chapter 1: Memory Technologies](../d_chapter1_memory_technologies/README.md)

---
