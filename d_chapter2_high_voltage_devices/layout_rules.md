# 📐 高耐圧デバイスのレイアウト設計と最適化｜Layout Design and Optimization for High-Voltage Devices

---

## 📘 概要｜Overview

**高耐圧デバイス（LDMOS、HV-CMOS等）の信頼性には、物理レイアウト上の工夫が不可欠です。**  
**Physical layout optimization is essential for the reliability of high-voltage devices such as LDMOS and HV-CMOS.**

本章では以下の観点から最適化手法を紹介します：  
This section covers optimization from the following viewpoints:

- **ガードリング設計**｜Guard ring implementation  
- **セル間距離の確保**｜Spacing between devices  
- **CMPダミーパターン配置**｜CMP dummy fill strategy  
- **絶縁境界と熱設計**｜Isolation and thermal planning

---

## 🏗️ 設計項目と目的｜Design Items and Objectives

| 設計項目｜Item | 目的｜Purpose | 実装工夫｜Implementation |
|-------------|------------------|----------------------------|
| **ガードリング**<br>Guard Ring | 寄生トランジスタ抑制、電界集中緩和<br>Suppress latch-up and field stress | N+/P+接地リング、深ウェル併用<br>N+/P+ guard ring with deep well |
| **セル間スペース**<br>Spacing | 空乏層拡張、デバイス間絶縁<br>Depletion zone spacing, isolation | 3〜5μm以上の空白確保<br>≥ 3–5μm spacing |
| **CMPダミー**<br>CMP Dummy | 研磨ムラ抑制（dishing/erosion）<br>Reduce CMP dishing | Dummy metal配置による密度調整<br>Dummy metal for density balance |
| **熱設計**<br>Thermal Design | 熱集中回避、放熱促進<br>Prevent thermal hotspots | 拡張パッド、幅広配線など<br>Wide traces and thermal pads |

---

## 🧪 CMPダミーパターン｜CMP Dummy Fill

**CMP（Chemical Mechanical Polishing）工程ではパターン密度差が問題となります。**  
**Pattern density variations can cause dishing or erosion during CMP.**

```
配線層例｜Interconnect Example

┌─────┐      ┌─────┐
│配線A│      │配線B│      ← 密度差あり
└─────┘      └─────┘

↓ Dummy挿入（非機能）
░░░░░░░      ░░░░░░░
```

- **電気的には機能しないが、機械加工での均一性を確保**  
  *Dummy metal does not carry current but improves polish uniformity*
- **PDKでの密度制限（例：10〜70%）に従う必要あり**  
  *Follow dummy density rules in PDK (e.g., 10–70%)*

---

## 🧯 ガードリングとラッチアップ対策｜Guard Rings & Latch-up Protection

- **N+/P+リングを高電圧端子周囲に配置**  
  *Place N+/P+ guard rings around HV nodes*
- **GNDまたはウェルへ接続し、寄生npn/pnpを封じ込め**  
  *Tie to GND or well to block parasitic paths*
- **LDMOSではリング多重化やDeep N-Wellの利用**  
  *In LDMOS, use multiple rings and deep wells*

---

## 📚 教材的意義｜Educational Relevance

- **量産レベルの物理設計感覚**を身につける  
  *Develop layout awareness for mass production*
- **微細な製造制約**（ばらつき、ノイズ、ラッチアップ）を実感  
  *Understand real-world limits like variation and latch-up*
- **テープアウト設計段階での必須視点**を学ぶ  
  *Acquire critical knowledge for tape-out phase*

---

## 🔗 関連リンク｜Related Topics

- [📘 応用編 第2章｜高耐圧デバイス 全体README](../d_chapter2_high_voltage_devices/README.md)  
  **章全体の構成と関連技術の導入**  
  *Chapter 2 Top: Overview of high-voltage devices and structure of this section*
  
- [`dvdt.md`](./dvdt.md)  
  **dv/dt破壊と連動するレイアウト的配慮**  
  *Layout design for dv/dt protection*

- [chapter5_soc_design_flow](../chapter5_soc_design_flow/)  
  **配置配線設計とDRCルール**  
  *Place-and-route and DRC considerations*

- [chapter6_test_and_package](../chapter6_test_and_package/)  
  **CMPばらつきと電気テスト品質の関係**  
  *CMP variation and its test impact*

---

© 2025 Shinichi Samizo / MIT License

---
