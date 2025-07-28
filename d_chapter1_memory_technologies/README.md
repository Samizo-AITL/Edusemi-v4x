# 💾 応用編 第1章｜メモリ技術の構造と選定指針  
# 💾 Applied Chapter 1 | Memory Technologies – Structure and Selection Guidelines

---

## 🎯 章のねらい｜Chapter Objectives

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

- 組込み（SRAM/FeRAM/MRAM）と外部（DRAM/NAND）メモリの**構造的違い**  
  Structural differences between embedded and external memories  
- **速度・揮発性・耐久性・面積効率・電力**によるトレードオフ分析  
  Trade-off analysis among speed, volatility, endurance, area, and power  
- **OpenLane/Sky130でのSRAMマクロ呼出・統合例**  
  SRAM macro instantiation via OpenLane (e.g., Sky130)  
- **eMRAMによるeFlash代替検討／FeRAMの混載SoC適用例**  
  eMRAM as eFlash alternative; FeRAM in sensor SoCs  
- NAND向け**FTL, ECC, 読み出し干渉対策**などの制御回路設計  
  NAND controller design: FTL, ECC, read disturbance mitigation  

---

## 🔗 他章・技術記録との接続｜Cross-Chapter and Archive Links

| 章・資料 | 内容 | 本章との関係 |
|-----------|------|-------------|
| [第4章：MOSトランジスタ特性](../chapter4_mos_characteristics/) | MOSの動作原理と構造 | メモリセル（6T, 1T1C, MTJ等）理解の前提 |
| [第5章：SoC設計フローとEDAツール](../chapter5_soc_design_flow/) | 合成・PDK統合・配置配線 | SRAMマクロの設計・呼出に関与 |
| [第6章：テスト・パッケージ技術](../chapter6_test_and_package/) | 書換耐久・リテンション・信頼性 | メモリ評価・不良解析との接続 |
| [Edusemi-Plus/archive/in1998/DRAM_Startup_64M_1998.md](../../Edusemi-Plus/archive/in1998/DRAM_Startup_64M_1998.md) | **1998年 DRAM立ち上げ記録** | DRAMセル信頼性、酸化膜ダメージ対策など実録 |
| [Edusemi-Plus/archive/in2001/VSRAM_2001.md](../../Edusemi-Plus/archive/in2001/VSRAM_2001.md) | **2001年 VSRAM開発記録** | DRAM応用SRAMの設計と歩留まり改善の教材化 |

---

## 🧩 章のキーワード｜Keywords

SRAM, DRAM, FeRAM, MRAM, 3D NAND, PDK, Macro, Non-volatile, Endurance, FTL, ECC, Sky130

---

## 📌 補足情報｜Supplement

- Open PDK examples: [Sky130 PDK – Google/SkyWater](https://skywater-pdk.readthedocs.io)  
- Memory taxonomy references: ISSCC papers, JEDEC standards  
- NAND flash controller design: Error correction, FTL layering, wear leveling techniques  

---

🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---
