---
layout: default
title: Appendix 2.3 - Interposer and Redistribution Layer (RDL) Stack Structures
---

---

# 📘 Appendix 2.3：インターポーザと再配線層（RDL）の積層構造  
**Appendix 2.3: Interposer and Redistribution Layer (RDL) Stack Structures**

---

## 📌 概要 / Overview

本資料では、2.5D・3Dパッケージにおける**インターポーザ構造とRDL（Redistribution Layer）構成**について、**代表的な設計例**をもとに解説します。  
*This appendix presents typical structures of silicon interposers and RDL stacks used in 2.5D/3D packaging.*

それぞれが**多チップ接続・熱分散・信号配線**の中核技術として機能します。  
They are essential for **multi-die interconnects, thermal management, and high-density routing.**

---

## 🧩 インターポーザ（Si）構造例  
**Silicon Interposer: Structural Example**

### ✦ 上面図（Top View）

```
Top View:
┌─────────────┐
│  Die1  Die2 │  ← 複数ロジックダイ / Multiple Logic Dies
│   │     │   │
└────┬───────┘
     │  TSV  ↓
     │───────┐
     ▼       │
Bottom: RDL + bump array
```

### ✦ 積層断面構成 / Cross-Section Layers

| 🧩 層 / Layer | 🔧 内容 / Description | 📘 特徴 / Characteristics |
|---------------|------------------------|----------------------------|
| **Die層**<br>Die Layer | ロジック/メモリダイ群<br>Logic/memory dies | μ-bumpで接続<br>μ-bump interconnect |
| **接続層**<br>Connection Layer | TSV + RDL | 垂直ビアと再配線層<br>Vertical vias and redistribution |
| **配線層**<br>Metal Layer | Cu + PI (2–4層) | 高密度配線＋絶縁<br>High-density routing and insulation |
| **バンプ層**<br>Bump Layer | C4/Sn バンプ | 基板接続（FC-BGAなど）<br>Connection to package substrate |

---

## 🔄 RDL構造（Fan-Out / WLP）  
**Fan-Out and WLP-Type RDL Structures**

### ✦ 典型構成 / Typical Fan-Out RDL Stack

| 🧩 層 / Layer | 🔧 材料 / Material | 📘 目的 / Purpose |
|--------------|---------------------|---------------------|
| **上部配線層**<br>Top Metal | Cu + PI | 信号配線ルーティング<br>Signal routing |
| **中間配線層**<br>Mid Metal Layers | Cu + PI (2–6層) | 多層再配線構成<br>Multilayer redistribution |
| **チップ埋込層**<br>Embedded Die Layer | Mold樹脂<br>Mold Resin | Fan-Outスペース確保<br>Supports die and area expansion |
| **I/O層**<br>Bottom I/O Layer | Cuバンプ<br>Cu Bumps | LGA/BGA接続<br>Board-level interconnects |

---

### ✦ 特徴 / Characteristics

- ✅ **超薄型パッケージ**が可能（コアレス設計）  
  Enables **ultra-thin packaging** with coreless design  
- 🔄 **チップ外周への信号拡張（Fan-Out）**  
  Signal redistribution from chip to package edge  
- 🔗 **μ-bump / Hybrid Bondingと高相性**  
  Compatible with advanced bonding techniques like μ-bump and hybrid bonding  

---

## 🏗️ 多層化における設計観点  
**Key Considerations for Multilayer Design**

| 🔍 観点 / Aspect | 🛠️ 留意点 / Design Considerations |
|------------------|-----------------------------------|
| **寸法制御**<br>Dimensional Accuracy | 膜厚・ライン幅・ギャップの精密制御<br>Accurate thickness, line width, spacing |
| **熱応力管理**<br>Thermal Stress Control | CTE差による応力とクラックに注意<br>Handle stress from CTE mismatch |
| **レジスト整合性**<br>Resist Alignment | 各層のマスク合わせ精度が重要<br>Precise mask alignment between layers |
| **平坦性維持**<br>Planarity / CMP | CMP工程での平坦化が不可欠<br>Ensure flat surface via CMP for lithography |

---

## 📌 まとめ / Summary

インターポーザとRDLは、**チップレット技術や先端実装**を支える不可欠な基盤技術です。  
*Interposers and RDLs are foundational technologies in chiplet-based and advanced packaging.*

➡ 電気・熱・信号配線の複合的制約を同時に扱うため、**構造設計と材料選定の統合的最適化**が求められます。  
➡ Their complexity demands a **co-optimized structural and material design** approach.

---

## 🔗 特別編 第2章 トップへ戻る  
[📎 戻る｜Back to Chapter 2 Top](./README.md)
