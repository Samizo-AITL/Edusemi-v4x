---
layout: default
title: レイアウトの基本原則と設計ルールの意図
---

---

# 📐 レイアウトの基本原則と設計ルールの意図  
**📐 Layout Principles and Design Rule Intentions**

---

## 📘 概要 | Overview

レイアウト設計とは、論理回路を**物理的構造としてシリコン上に実装する工程**です。  
Layout design is the process of **implementing logic circuits as physical structures on silicon**.

PDK（Process Design Kit）に従って設計ルールを遵守しながら、  
**性能・信頼性・歩留まり**のトレードオフを最適化することが求められます。  
Following the PDK rules, designers must balance **performance, reliability, and yield**.

このセクションでは、**基本的なレイアウト構造と設計意図の理解**を目的とします。  
This section focuses on understanding the **basic layout structures and the intent behind design rules**.

---

## 🧱 幅（Width）と間隔（Spacing） | Line Width and Spacing

| 項目 / Item | 説明 / Description | 教育的意義 / Educational Significance |
|-------------|--------------------|----------------------------------------|
| **最小幅<br>Minimum Width** | 各層（Poly、Metal等）に定義される最小線幅<br>Minimum line width defined for each layer (Poly, Metal, etc.) | プロセス限界や露光限界の反映<br>Reflects process and lithography limits |
| **最小間隔<br>Minimum Spacing** | 同一層・異層間の必要な距離制約<br>Required spacing between same or different layers | ショート・リーク・干渉の防止<br>Prevents shorts, leakage, and interference |
| **W/Sルール（Width/Spacing Rule）** | PDKで定義される層ごとの幅と間隔の組み合わせ<br>Combined rules for width and spacing per layer in PDK | 歩留まり・耐電圧・CMP対応設計の基礎<br>Basis for yield, breakdown voltage, and CMP |

> 例：Metal1 の最小幅 0.14 μm、最小間隔 0.14 μm（ピッチ = 0.28 μm）  
> Example: Metal1 minimum width = 0.14 μm, spacing = 0.14 μm (pitch = 0.28 μm)

---

## 🛤️ 配線層と層構成 | Routing Layers and Stack Structure

| 層 / Layer | 方向 / Direction | 主用途 / Primary Use |
|------------|------------------|-----------------------|
| **Poly** | 任意 / Arbitrary | ゲート構造 / Gate structure |
| **Metal1** | 横方向 / Horizontal | ローカル信号配線 / Local signal routing |
| **Metal2** | 縦方向 / Vertical | 電源/GND配線（中間層）<br>Power/GND routing (mid-level) |
| **Metal3〜n** | 交互 / Alternating | グローバル配線、パワーグリッド、クロック等<br>Global routing, power grids, clocks |

- 🔄 **層を交互に使うことでクロストークとIRドロップを抑制**  
  Alternating layers suppress crosstalk and IR drop.
- 🔌 **電源層は太く短く、信号層は高密度に配置**  
  Power layers should be wide and short; signal layers dense and compact.

---

## 🔌 パワーグリッドとウェルタップ | Power Grids and Well Taps

- **パワーグリッド（Power Grid）**：Metal層で構成されたGND/VDDの網状配線  
  A mesh structure of GND/VDD using metal layers.  
  - 🎯 **IRドロップの抑制、ノイズの低減**  
    Reduces IR drop and suppresses noise.

- **ウェルタップ（Well Tap）**：P/NウェルをGND/VDDに接続する構造  
  Connects P-well or N-well to GND or VDD.  
  - 🛡 **ラッチアップ防止と寄生バイポーラの抑制**  
    Prevents latch-up and suppresses parasitic bipolar action.

---

## 🧩 レイアウト基本ルールと意図 | Layout Design Rules and Their Intent

| 項目 / Item | 意図 / Intent |
|-------------|----------------|
| **Min Width** | フォトリソ精度・プロセス下限の確保<br>Ensures lithographic accuracy and process limitations |
| **Min Spacing** | 金属間ショートやリークの防止<br>Prevents shorts and leakage between lines |
| **Enclosure** | コンタクトやViaの**完全被覆**を確保し接続信頼性向上<br>Ensures full coverage of contacts/Vias for reliable connections |
| **Notch** | 鋭角・隙間によるストレス集中を防ぐ<br>Prevents stress concentration from narrow gaps or corners |
| **Density** | CMP均一性を保つため**Metal Fill**を適用<br>Maintains CMP uniformity using metal fill |
| **Overlap / Overlap Margin** | 層間の**意図的な重なり**を定義（例：コンタクトとMetal）<br>Defines intentional overlaps between layers (e.g., contact-to-metal) |
| **Overlay（オーバーレイ）** | マスク合わせずれの許容範囲<br>Allowed misalignment tolerance between masks |

---

## 🎯 教材的意義 | Educational Perspective

- ✨ 数値ルールではなく**物理的背景と目的**を理解  
  Understand not just numbers, but the **physical rationale behind rules**
- 🤝 手動レイアウトと自動P&R双方に対応する知識基盤  
  Knowledge applicable to both manual layout and automated P&R
- 🧠 **DRC違反の背景を“構造×プロセス”視点で考察**  
  Analyze DRC violations from **structural and process perspectives**

---

## 🔗 次のセクション | Next Section

➡ [`cmp_dummy_pattern.md`](./cmp_dummy_pattern.md)：CMP均一性のためのパターン工夫  
➡ *CMP Dummy Patterns: Layout techniques for planarization control*

---

🧱 応用編 第4章：レイアウト設計と最適化 /  
🧱 *Applied Chapter 4: Layout Design and Optimization*  
[📘 セクション一覧 / Section Index](../d_chapter4_layout_optimization/README.md)

---

© 2025 Shinichi Samizo / MIT License

