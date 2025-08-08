---
layout: default
title: 2.2 2.5D実装技術 - シリコンインターポーザとCoWoS
---

---

# 🏗️ 2.2 2.5D実装技術：シリコンインターポーザとCoWoS  
**2.2 2.5D Integration Technologies: Silicon Interposer and CoWoS**

---

## 🧭 2.5Dパッケージとは｜What is 2.5D Packaging?

**2.5Dパッケージ**とは、複数のチップ（チップレット）を**シリコンインターポーザ**や**再配線層（RDL）**の上に**横並び**で実装する技術です。  
*Unlike 3D stacking (vertical), 2.5D packages place chips side-by-side on an interposer or RDL, enabling better thermal and test characteristics.*

| 🧩 特徴 / Feature | 📝 説明 / Description |
|------------------|----------------------|
| **配置**<br>Placement | チップを水平に並べる<br>Side-by-side chip arrangement |
| **比較対象**<br>Compared To | 3D実装（垂直積層）に対する中間形態<br>Intermediate between 2D and 3D stacking |
| **利点**<br>Advantages | 放熱性・デバッグ性に優れる<br>Good for thermal dissipation and testability |

---

## 🧱 シリコンインターポーザ（Si Interposer）｜Silicon Interposer

### ✦ 構造 / Structure

- 多層メタル配線を備えた**シリコン基板**
- TSVを用いない**貫通孔なしインターポーザ**（TSV-less）
- μバンプによりロジック・HBM等と接続
- 下層は**FC-BGAサブストレート**に接続

### ✦ 特徴 / Features

| 🔍 項目 / Item | 📘 内容 / Description |
|----------------|------------------------|
| **配線幅・間隔**<br>Wire Width / Spacing | 約1〜5 µm（高密度）<br>High-density routing (1–5 µm) |
| **バンプピッチ**<br>Bump Pitch | 約40〜100 µm（μ-bump）<br>μ-bump spacing: 40–100 µm |
| **主用途**<br>Main Application | HBM/GPUやASICとの接続<br>HBM-GPU/ASIC integration |

---

## 🏗️ 実装例：TSMC CoWoS｜Example: TSMC CoWoS

### ✦ 概要 / Overview

- TSMCが提供する代表的な**2.5D商用技術**  
  *TSMC’s flagship commercial 2.5D packaging technology*
- **HBM + 高性能GPU/ASIC**向けに多数実績  
  *Widely adopted for HBM + high-performance chip integration*

### ✦ 工程概要 / Process Flow

1. **チップダイをシリコンインターポーザ上に実装**  
   *Mount chips on silicon interposer*
2. **μバンプでインターポーザと接合**  
   *μ-bump connection between interposer and dies*
3. **Waferレベル封止とテスト**  
   *Wafer-level encapsulation and testing*
4. **FC-BGA基板へ最終接合**  
   *Final bonding to FC-BGA substrate*

---

## 🔧 その他の2.5D手法｜Other 2.5D Approaches

| 実装 / Method | 概要 / Description | 企業 / Company |
|---------------|--------------------|----------------|
| **EMIB** | 小型インターポーザによるポイント接続<br>Small bridge interposer for local die links | Intel |
| **RDL-Interposer** | 高密度RDL層での接続<br>Redistribution layers used for die-to-die links | ASE, Amkor |
| **有機インターポーザ**<br>Organic Interposer | 樹脂基板ベースの低コスト方式<br>Cost-efficient organic interposer | Low-cost SoCs 等 |

---

## 🔎 メリットと制約｜Advantages and Limitations

| 項目 / Item | ✅ メリット / Advantages | ⚠️ 制約 / Limitations |
|-------------|--------------------------|------------------------|
| **配線密度**<br>Wiring Density | 高密度・低遅延の短距離配線<br>Short, low-latency interconnects | インターポーザ面積に制約あり<br>Limited by interposer size |
| **熱特性**<br>Thermal Profile | 放熱性に優れる<br>Excellent thermal spreading | HBMなど局所発熱への対処が課題<br>Hotspots (e.g., HBM) remain |
| **テスト性**<br>Testability | 各ダイ単体でのテストが可能<br>Die-level test possible | バンプ不良の検出が困難<br>Bump failure hard to isolate |
| **コスト**<br>Cost | 3D実装より低コスト<br>Cheaper than full 3D stack | インターポーザ製造自体は高価<br>Interposer fabrication costly |

---

## 📎 次節への接続｜Connection to Next Section

次節 [**2.3：3D積層技術**](./f2_3_3d_pkg.md) では、**TSVやハイブリッドボンディング**を活用した**垂直方向の集積技術**について詳しく解説します。  
*In the next section [**2.3: 3D Stacking Technologies**](./f2_3_3d_pkg.md), we dive into vertical integration using **TSVs** and **hybrid bonding**.*

---

## 🏁 特別編 第2章 トップへ戻る｜Back to Chapter 2 Top

🔗 [📚 特別編 第2章 トップに戻る](./README.md)
