---
layout: default
title: 応用編 第1章｜メモリ技術の構造と選定指針
---

---

# 💾 応用編 第1章｜メモリ技術の構造と選定指針  
**Applied Chapter 1 | Memory Technologies – Structure and Selection Guidelines**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) |

---

## 🎯 章のねらい｜Chapter Objectives

| 🇯🇵 日本語                                                                                                      | 🇺🇸 English                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| - 各種メモリ（SRAM / DRAM / FeRAM / MRAM / NAND）の**構造と動作原理**を理解する                                 | - Understand the **structure and operation principles** of SRAM, DRAM, FeRAM, MRAM, and NAND                 |
| - **速度・不揮発性・書換耐性・面積効率・消費電力**などの**評価軸を比較検討**できる                              | - Be able to evaluate memory types across axes such as **speed, non-volatility, endurance, area, power**     |
| - SoCにおける**メモリ統合・選定・接続方法**を習得し、設計判断の基盤を築く                                       | - Learn how to **integrate, select, and interface memory** in SoC design with a solid engineering foundation |

---

## 📚 節構成｜Chapter Structure

| No. | セクション名（日本語）                             | Section Title (English)                                    | リンク |
|-----|----------------------------------------------------|-------------------------------------------------------------|--------|
| 1.1 | SRAM（Static RAM）：高速・揮発                      | High-speed volatile memory for cache/registers              | [📎](sram.md) |
| 1.2 | DRAM（Dynamic RAM）：大容量・リフレッシュ必要       | High-density memory requiring refresh (e.g., DDR, LPDDR)    | [📎](dram.md) |
| 1.3 | FeRAM：強誘電体RAM・不揮発                          | Non-volatile memory for low-power / analog-mixed LSI        | [📎](feram.md) |
| 1.4 | MRAM：磁気RAM・不揮発・高耐久                        | Durable non-volatile memory (STT/SOT); eFlash replacement    | [📎](mram.md) |
| 1.5 | 3D NAND：大容量・不揮発・ストレージ用途              | Large-capacity flash for storage (eMMC, SSD, UFS, etc.)     | [📎](3dnand.md) |
| 1.6 | LPDDR＋FeRAM：ハイブリッドメモリによるモバイルAI応用 | Hybrid memory (LPDDR + FeRAM) for mobile/edge AI | [📎](1_6_lpddr_feram.md) |
| 1.7 | FeFET（HfO₂/HZO, Gate-Last）                        | CMOS-compatible FeFET for auxiliary NVM (SRAM backup, Instant-On) | [📎](018u_fefet.md) |

---

## 🧠 設計観点のトピック｜Design-Oriented Topics

- 組込み（SRAM / FeRAM / MRAM）と外部（DRAM / NAND）メモリの**構造的違い**  
  ➤ Structural differences between **embedded** and **external** memories  
- **速度・揮発性・耐久性・面積効率・電力**によるトレードオフ分析  
  ➤ Trade-off analysis among **speed, volatility, endurance, area, and power**  
- **OpenLane / Sky130でのSRAMマクロ呼出・統合例**  
  ➤ SRAM macro instantiation via **OpenLane** (e.g., Sky130 PDK)  
- **eMRAMによるeFlash代替検討 / FeRAMの混載SoC適用例**  
  ➤ Use cases of **eMRAM as eFlash alternative** and **FeRAM in sensor SoCs**  
- NAND向け**FTL, ECC, 読み出し干渉対策**などの制御回路設計  
  ➤ NAND controller design including **FTL, ECC, and read disturbance mitigation**

---

## 🔗 他章・技術記録との接続｜Cross-Chapter and Archive Links

| 章・資料 | 内容 | 本章との関係 |
|-----------|------|-------------|
| [第4章：MOSトランジスタ特性](../chapter4_mos_characteristics/) | MOSの動作原理と構造 | メモリセル（6T, 1T1C, MTJ等）理解の前提 |
| [第5章：SoC設計フローとEDAツール](../chapter5_soc_design_flow/) | 合成・PDK統合・配置配線 | SRAMマクロの設計・呼出に関与 |
| [第6章：テスト・パッケージ技術](../chapter6_test_and_package/) | 書換耐久・リテンション・信頼性 | メモリ評価・不良解析との接続 |

---

## 🧩 章のキーワード｜Keywords

`SRAM`, `DRAM`, `FeRAM`, `MRAM`, `3D NAND`, `PDK`, `Macro`, `Non-volatile`, `Endurance`, `FTL`, `ECC`, `Sky130`

---

## 📌 補足情報｜Supplement

- 🔗 Open PDK examples: [Sky130 PDK – Google/SkyWater](https://skywater-pdk.readthedocs.io)  
- 📄 Memory taxonomy references: **ISSCC論文**, **JEDEC標準**など  
- 📘 NAND flash controller design: **Error correction**, **FTL layering**, **wear leveling techniques**

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)
