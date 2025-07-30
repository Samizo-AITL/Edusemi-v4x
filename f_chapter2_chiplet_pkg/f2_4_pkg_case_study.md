# 2.4 実例紹介：AMD・Intel・Appleのパッケージング戦略  
# 2.4 Case Studies: Packaging Strategies of AMD, Intel, and Apple

---

## 🎯 目的 / Objective

この節では、主要半導体企業が**チップレット、2.5D、3Dパッケージ技術をどのように活用しているか**を、代表的な製品事例を通じて学びます。  
This section introduces how leading semiconductor companies apply **chiplet, 2.5D, and 3D packaging technologies** in real-world products.

---

## 🔶 AMD：Infinity Fabricによるマルチチップアーキテクチャ  
## 🔶 AMD: Multi-Chip Architecture via Infinity Fabric

### ✦ Ryzen / EPYC（Zen以降）  
Zen-based Ryzen and EPYC architectures

- **構成**：小型CPUダイ（CCD）とI/Oダイ（IOD）の分離構成  
  **Structure**: Separate CPU dies (CCD) and I/O die (IOD)
- **接続**：Infinity Fabric（独自の高速インターコネクト）  
  **Connection**: Proprietary Infinity Fabric interconnect
- **利点**：歩留まり改善、コスト削減、スケーラブル設計  
  **Benefits**: Better yield, cost savings, scalable performance

| 製品 / Product | 特徴 / Feature | 備考 / Notes |
|----------------|------------------|----------------|
| **Ryzen 3000 / 5000** | CCD + IOD構成（7nm + 12nm）<br>CCD + IOD (7nm + 12nm) | 異種プロセス混載<br>Heterogeneous process |
| **EPYC (Rome)** | 最大8CCD + 1IOD<br>Up to 8 CCDs + 1 IOD | サーバ向け高スケール性<br>High scalability for servers |

---

## 🔷 Intel：EMIBとFoverosによる垂直・水平接続の両立  
## 🔷 Intel: Combining EMIB and Foveros for 2.5D/3D Integration

### ✦ EMIB（Embedded Multi-die Interconnect Bridge）

- **小型インターポーザ**を部分的に用いた**水平接続**  
  Local bridge interposer for **side-by-side connection**
- **高密度接続とコスト抑制**の両立  
  Balances **density and cost**

### ✦ Foveros（3D積層技術）

- **TSVによるロジック-ロジック積層**  
  Stacks logic-on-logic using **TSVs**
- 初搭載：**Intel Lakefield（2019）**  
  First used in **Intel Lakefield (2019)**

| 技術 / Technology | 製品例 / Product Example | 備考 / Notes |
|-------------------|--------------------------|---------------|
| **EMIB** | Stratix 10 | FPGAとメモリの連結<br>FPGA-memory interface |
| **Foveros** | Lakefield, Meteor Lake | 3D CPUチップ構造<br>3D CPU architecture |

---

## 🍏 Apple：UltraFusionによるロジックダイ連結  
## 🍏 Apple: Logic Die Fusion via UltraFusion

### ✦ M1 Ultra（2022）

- 2個のM1 Maxを**パッケージレベルで融合**  
  Two M1 Max dies **fused at the package level**
- **UltraFusion**と呼ばれるI/Fで1チップのように動作  
  Acts as a single chip via the **UltraFusion** interface

| 項目 / Item | 内容 / Description |
|--------------|---------------------|
| **バス帯域**<br>Bus Bandwidth | 最大2.5 TB/s<br>Up to 2.5 TB/s |
| **実装方式**<br>Integration Type | 2.5D的インターポーザ構造<br>2.5D-style interposer |
| **設計意図**<br>Design Intent | パッケージ内でチップサイズ限界を超える<br>Overcome single-die size limits |

---

## 🧩 事例にみる技術選定の視点  
## 🧩 Key Takeaways from Packaging Strategies

| 観点 / Aspect | **AMD** | **Intel** | **Apple** |
|---------------|---------|-----------|-----------|
| **接続構造**<br>Integration Type | 水平方向マルチダイ接続<br>Horizontal multi-die | EMIB + TSVによる混合型<br>Hybrid (EMIB + TSV) | ロジック同士の2.5D連結<br>2.5D logic fusion |
| **コスト志向**<br>Cost Focus | 高<br>High | 中<br>Medium | 高（性能最優先）<br>High (performance first) |
| **再利用性**<br>Reusability | 高（CCD再利用）<br>High (CCD reused) | 中（構成設計ごとに異なる）<br>Medium (per design) | 低（専用構造）<br>Low (application-specific) |

---

## 📎 次節への接続  
## 📎 Connection to Next Section

次節 [**2.5：設計上の課題**](./f2_5_design_challenges.md) では、これらの構造を**設計・量産**するうえで直面する「**熱・テスト・歩留まり**」の課題とその**対策技術**について詳しく解説します。  
In the next section [**2.5: Design Challenges**](./f2_5_design_challenges.md), we will discuss **thermal, test, and yield issues** in designing and mass-producing these packages.

---
