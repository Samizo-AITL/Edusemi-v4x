# 📘 第5章｜SoC設計フローとEDAツール  
# 📘 Chapter 5 | SoC Design Flows and EDA Tools

---

## 🔄 前章との接続｜Connection to Previous Chapter

| 🇯🇵 日本語                                                                                                     | 🇺🇸 English                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| 第4章では、MOSトランジスタの**動作・寸法ルール・PDK**を通して「製造可能な設計基盤」を構築しました。                      | Chapter 4 established a **manufacturable design base** via MOS characteristics, rules, and PDKs.                |
| 本章では、それを活用して**SoCとして機能する回路設計・検証プロセス**へと進みます。                                 | In this chapter, we apply that foundation to the **design and verification flow of a functional SoC**.          |

➡️ [📘 **第4章：MOSトランジスタ特性と設計基盤**](../chapter4_mos_characteristics/README.md) に戻る  
➡️ [📘 **Chapter 4: MOS Characteristics and Design Infrastructure**](../chapter4_mos_characteristics/README.md) (EN)

---

## 🎯 章のねらい｜Chapter Objectives

| 🇯🇵 日本語                                                                                   | 🇺🇸 English                                                                                      |
|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| - SoC開発の**全体フローと各設計要素**の役割を体系的に理解する                                     | - Understand the **overall SoC development flow** and the role of each design stage.         |
| - 標準セル設計と物理設計の**接続点・制約条件**を実務的に把握する                                    | - Learn how **standard-cell-based design links** to physical design in real-world scenarios. |
| - STAやDFTなど**現代SoCに不可欠な検証技術の基礎**を習得する                                       | - Acquire a foundation in **essential SoC verification techniques**, such as STA and DFT.    |

---

## 📚 節構成｜Chapter Structure

| No. | セクション名（日本語）                                                         | Section Title (English)                                              | 設計段階                  | リンク |
|-----|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|---------------------------|--------|
| 5.1 | SoC設計全体フローと開発視点（RTLからGDSIIまで）                                  | RTL to GDSII: Overall SoC Design Flow and Development Cycle          | 全体（上流〜下流）        | [📎](5.1_soc_design_flow.md) |
| 5.2 | 標準セルと論理合成（フロントエンド設計の中核）                                    | Standard Cells and Logic Synthesis (Core of Front-End Design)        | 論理設計                  | [📎](5.2_standard_cell_based_design.md) |
| 5.3 | クロック設計とタイミング解析（STA入門）                                           | Clock Design and Timing Analysis (Introduction to STA)              | タイミング検証            | [📎](5.3_clock_and_sta.md) |
| 5.4 | 電源・リセット・I/O設計の基礎（物理設計の重要要素）                               | Power, Reset, and I/O Design (Key Elements in Physical Design)       | 物理設計（中盤）          | [📎](5.4_power_io_design.md) |
| 5.5 | テスト構造（DFT技術の実践：Scan/JTAG/BIST）                                       | Test Structures (Practical DFT: Scan, JTAG, BIST)                    | 検証（設計全体に関与）    | [📎](5.5_test_structures.md) |

---

## 🔜 次章への導入｜Lead-in to Next Chapter

| 🇯🇵 日本語                                                                                                         | 🇺🇸 English                                                                                              |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 第6章では、設計完了後のSoCが**実チップとして現実世界に出るまで**のプロセス──**ウエハテスト、パッケージ、出荷**──を学びます。 | Chapter 6 will cover how a completed SoC is **tested, packaged, and finalized** into a real-world product. |

📎 [📘 **第6章：SoCテストとパッケージ工程の理解**](../chapter6_test_and_package/README.md) に進む  
📎 [📘 **Chapter 6: SoC Test and Packaging Process**](../chapter6_test_and_package/README.md) (EN)

---

## 🧩 章のキーワード｜Keywords

- **設計フロー・成果物**:  
  RTL, GDSII, Logic Synthesis, DFT

- **ライブラリ・構成要素**:  
  Standard Cell, Pad Ring, Power Grid

- **検証・解析技術**:  
  STA, Setup/Hold, Clock Tree, Scan Chain, JTAG, BIST

---

## 📌 補足情報｜Supplement

- **Open-source EDA Tools**:  
  OpenROAD, Yosys, KLayout, Magic, Verilator, OpenSTA

- **関連教材リンク｜Related Material Links**:  
  - [Sky130 PDK Docs](https://skywater-pdk.readthedocs.io)  
  - [The OpenROAD Project](https://theopenroadproject.org)  
  - [EDA Playground](https://www.edaplayground.com/)  

---

🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---
