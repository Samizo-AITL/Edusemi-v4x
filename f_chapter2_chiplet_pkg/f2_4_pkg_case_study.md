---
layout: default
title: 2.4 実例紹介 - パッケージング戦略事例（AMD・Intel・Apple）
---

---

# 📦 2.4 実例紹介：AMD・Intel・Appleのパッケージング戦略  
**2.4 Case Studies: Packaging Strategies of AMD, Intel, and Apple**

---

## 🎯 目的｜Objective

この節では、主要半導体企業が**チップレット、2.5D、3Dパッケージ技術**をどのように活用しているかを、代表的な製品事例を通じて学びます。  
This section explores how leading semiconductor companies leverage **chiplet, 2.5D, and 3D packaging technologies** in real products.

---

## 🔶 AMD｜Infinity Fabricによるマルチチップ戦略  
**AMD: Multi-Chip Strategy via Infinity Fabric**

### ✦ Ryzen / EPYC（Zenアーキテクチャ以降）  
**Zen-based Ryzen and EPYC architectures**

- **構成**：小型CPUダイ（CCD）とI/Oダイ（IOD）を分離  
  *Separate CPU cores (CCD) and I/O die (IOD)*
- **接続**：Infinity Fabricで高速通信  
  *High-speed link via Infinity Fabric*
- **利点**：スケーラビリティ・歩留まり改善・異種混載  
  *Scalable design, improved yield, heterogeneous processes*

| 🖥️ 製品 / Product | 特徴 / Feature | 備考 / Notes |
|------------------|------------------|-------------------------|
| **Ryzen 3000 / 5000** | CCD + IOD（7nm + 12nm）<br>CCD + IOD (7nm + 12nm) | プロセス分離構成<br>Separate process nodes |
| **EPYC Rome** | 最大8CCD + 1IOD<br>Up to 8 CCDs + 1 IOD | サーバ向け高スケーラビリティ<br>High scalability for servers |

---

## 🔷 Intel｜EMIBとFoverosによる垂直・水平統合  
**Intel: Hybrid Vertical & Horizontal Integration with EMIB and Foveros**

### ✦ EMIB（Embedded Multi-die Interconnect Bridge）

- **小型インターポーザ**でローカル接続  
  *Local bridge interposer for compact inter-die links*
- **複数ダイを効率よく統合**しコストも抑制  
  *Efficient multi-die integration with cost control*

### ✦ Foveros（3D TSV積層技術）

- **TSVを使ってロジック同士を積層**  
  *Logic-on-logic stacking via TSVs*
- 初搭載：**Lakefield（2019）**

| 🔧 技術 / Technology | 製品例 / Example Product | 備考 / Notes |
|----------------------|--------------------------|---------------|
| **EMIB** | Stratix 10 | FPGAとメモリ接続<br>FPGA-memory bridging |
| **Foveros** | Lakefield / Meteor Lake | CPUコアの3D積層構成<br>3D-stacked CPU architecture |

---

## 🍏 Apple｜UltraFusionによるロジックダイ統合  
**Apple: Logic Die Integration via UltraFusion**

### ✦ M1 Ultra（2022年）

- **M1 Maxを2個融合**し**1チップのように動作**  
  *Two M1 Max dies fused into a single chip behavior*
- UltraFusionにより**高帯域かつ低レイテンシ**を実現  
  *UltraFusion enables high-bandwidth, low-latency integration*

| 📌 項目 / Item | 内容 / Description |
|----------------|---------------------|
| **帯域幅**<br>Bus Bandwidth | 最大2.5 TB/s<br>Up to 2.5 TB/s |
| **実装形式**<br>Integration Type | 2.5Dインターポーザ的構造<br>2.5D-style interposer |
| **設計目的**<br>Design Goal | 単一ダイ制限の突破<br>Breaks single-die size limits |

---

## 🧩 3社比較：戦略の違いと設計思想  
**Comparison of Strategies and Design Philosophies**

| 🧠 観点 / Aspect | **AMD** | **Intel** | **Apple** |
|------------------|---------|-----------|-----------|
| **接続構造**<br>Integration | 水平方向マルチダイ<br>Horizontal multi-die | EMIB + TSV の複合構造<br>EMIB + TSV hybrid | 2.5D ロジック融合<br>2.5D logic fusion |
| **コスト志向**<br>Cost Focus | 高コスト最小化<br>Cost reduction prioritized | コストと性能の両立<br>Balance of cost and performance | 性能最重視<br>Performance prioritized |
| **再利用性**<br>Reusability | CCD再利用で高<br>High (CCD reuse) | 中程度<br>Medium | 専用構成で低<br>Low (custom design) |

---

## 📎 次節への接続｜Connection to Next Section

次節 [**2.5：設計上の課題**](./f2_5_design_challenges.md) では、これらのパッケージを**実際に製品化する際に直面する「熱・テスト・歩留まり」問題**とその**対策技術**について詳しく解説します。  
In the next section [**2.5: Design Challenges**](./f2_5_design_challenges.md), we will explore **thermal, test, and yield issues** and the **technical solutions** adopted in real implementations.

---

## 🏁 特別編 第2章 トップへ戻る｜Back to Chapter 2 Top

🔗 [📚 特別編 第2章 トップに戻る](./README.md)
