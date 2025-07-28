# 📘 第5章｜SoC設計フローとEDAツール  
# 📘 Chapter 5 | SoC Design Flows and EDA Tools

---

### 📎 前章へのリンク｜Back to Previous Chapter  
➡️ [📘 **第4章：MOSトランジスタ特性と設計基盤**](../chapter4_mos_basics/README.md) に戻る  
➡️ [📘 **Chapter 4: MOS Characteristics and Design Infrastructure**](../chapter4_mos_basics/README.md) (EN)

---

## 🎯 章のねらい｜Chapter Objectives

| 🇯🇵 日本語                                                                                   | 🇺🇸 English                                                                                      |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| - SoC開発の**全体フローと各設計要素**の役割を体系的に理解する                                     | - Understand the **overall SoC development flow** and the role of each design stage.         |
| - 標準セル設計と物理設計の**接続点・制約条件**を実務的に把握する                                    | - Learn how **standard-cell-based design links** to physical design in real-world scenarios. |
| - STAやDFTなど**現代SoCに不可欠な検証技術の基礎**を習得する                                       | - Acquire a foundation in **essential SoC verification techniques**, such as STA and DFT.    |

---

## 📚 節構成｜Chapter Structure

| No. | セクション名（日本語）                                                             | Section Title (English)                                       | リンク |
|-----|-------------------------------------------------------------------------------------|----------------------------------------------------------------|--------|
| 5.1 | SoC設計全体フローと開発視点<br>_Overview of SoC Design Flow and Development Cycle_ | RTL to GDS: flow overview and project lifecycle               | [📎](5.1_soc_design_flow.md) |
| 5.2 | 標準セルとセルベース設計<br>_Standard Cell and Cell-Based Design_                  | Standard cell libraries, logic synthesis, cell structure       | [📎](5.2_standard_cell_based_design.md) |
| 5.3 | クロックとタイミング設計（STA入門）<br>_Clock and Timing Design (Intro to STA)_     | Setup/hold, clock tree design, static timing analysis basics   | [📎](5.3_clock_and_sta.md) |
| 5.4 | 電源・リセット・I/O設計の基礎<br>_Power, Reset, and I/O Design Basics_              | Power schemes, reset circuits, pad ring, I/O considerations    | [📎](5.4_power_io_design.md) |
| 5.5 | テスト構造（スキャン、JTAG、BIST）<br>_Test Structures (Scan, JTAG, BIST)_          | DFT basics, scan chain, boundary scan, BIST introduction       | [📎](5.5_test_structures.md) |

---

## 🔄 前章との接続｜Connection to Previous Chapter

| 🇯🇵 日本語                                                                                                     | 🇺🇸 English                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 第4章では、MOSトランジスタの**動作・寸法ルール・PDK**を通して「製造可能な設計基盤」を構築しました。                      | Chapter 4 established a **manufacturable design base** via MOS characteristics, rules, and PDKs.                |
| 本章では、それを活用して**SoCとして機能する回路設計・検証プロセス**へと進みます。                                 | In this chapter, we apply that foundation to the **design and verification flow of a functional SoC**.          |

---

## 🔜 次章への導入｜Lead-in to Next Chapter

| 🇯🇵 日本語                                                                                                   | 🇺🇸 English                                                                                              |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 第6章では、完成したSoCが**ウエハ上でのテスト、パッケージング、製品化**を経て市場に出るまでの工程を学びます。           | Chapter 6 will cover how a completed SoC is **tested, packaged, and finalized** for production on wafer. |

📎 [📘 **第6章：SoCテストとパッケージ工程の理解**](../chapter6_test_and_package/README.md) に進む  
📎 [📘 **Chapter 6: SoC Test and Packaging Process**](../chapter6_test_and_package/README.md) (EN)

---

## 🧩 章のキーワード｜Keywords

```
RTL, GDSII, Standard Cell, Logic Synthesis, STA, Clock Tree, Power Grid, Reset, Pad Ring, Scan Chain, JTAG, BIST, DFT
```

---

## 📌 補足情報｜Supplement

- **Open-source EDA Tools**:  
  OpenROAD, Yosys, KLayout, Magic, Verilator, OpenSTA

- **関連教材リンク｜Related Material Links**:  
  - [Sky130 PDK Docs](https://skywater-pdk.readthedocs.io)  
  - [The OpenROAD Project](https://theopenroadproject.org)  
  - [EDA Playground](https://www.edaplayground.com/)  

---
