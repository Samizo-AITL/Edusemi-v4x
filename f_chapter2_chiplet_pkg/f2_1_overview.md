# 2.1 チップレット化の背景と技術潮流  
# 2.1 Background and Technological Trends of Chiplet Integration

---

## 🔰 なぜチップレットなのか？  
## 🔰 Why Chiplet?

SoC（System-on-Chip）による高集積化は長らく主流でしたが、以下のような限界が現れつつあります：  
Monolithic SoCs have long been the mainstream, but several limitations have emerged:

| 課題 / Challenges | 説明 / Description |
|------------------|-------------------|
| **製造コストの急増**<br>Increasing Manufacturing Cost | 微細化によりEUV装置導入や歩留まり低下に伴いコストが急増。<br>Advanced nodes require costly EUV tools and suffer from yield loss. |
| **リスクの集中**<br>Risk Centralization | 巨大SoCではリスピン時の損失が大きく、製品化遅延に直結。<br>Single-chip failures result in expensive respins and delays. |
| **プロセス適合性のトレードオフ**<br>Process Incompatibility | 高速ロジックと高精度アナログを同時に最適化するのが困難。<br>Hard to co-optimize logic, analog, RF, and memory in one die. |

➡ **機能分離・再利用性・リスク分散**を可能にする **チップレット（Chiplet）** という選択肢が登場。  
➡ *Chiplet* architecture enables **modularization**, **reuse**, and **risk mitigation**.

---

## 🔧 チップレット技術の要素  
## 🔧 Key Elements of Chiplet Technology

| 項目 / Element | 内容 / Description |
|----------------|--------------------|
| **構成単位**<br>Chiplet Units | 機能ごとに分割された複数の小型ダイ<br>Multiple small dies each handling a specific function |
| **接続手法**<br>Interconnection | インターポーザ、μバンプ、Hybrid Bondingなどの高密度接続<br>High-density links such as interposers, μ-bumps, TSVs, hybrid bonding |
| **設計思想**<br>Design Philosophy | 再利用可能なIPチップレット化・異種混載・歩留まり改善<br>Optimized for reuse, heterogeneous integration, and better yield |

---

## 🌐 代表的な実装例（後節に詳細）  
## 🌐 Representative Implementations (Detailed Later)

| 企業 / Company | 技術 / Technology | 製品例 / Example Products |
|----------------|------------------|--------------------------|
| **AMD** | Infinity Fabricによるマルチダイ接続<br>Multi-die via Infinity Fabric | Ryzen, EPYC |
| **Intel** | Foveros（3D）＋EMIB（2.5D）<br>Foveros + EMIB | Lakefield, Ponte Vecchio |
| **Apple** | UltraFusionによる大規模チップ結合<br>Large-scale die bridging with UltraFusion | M1 Ultra |

---

## 🌀 技術潮流と今後の動向  
## 🌀 Trends and Future Directions

| 年代 / Era | トレンド / Trend | 備考 / Remarks |
|------------|------------------|----------------|
| **〜2020** | モノリシックSoC主流<br>Monolithic SoCs | 高集積・低遅延だが柔軟性に欠ける<br>Efficient but inflexible |
| **2020〜** | 2.5Dパッケージ登場<br>Rise of 2.5D Packaging | Siインターポーザ＋HBMの組み合わせ<br>Interposer + HBM adopted |
| **2023〜** | 3D集積の本格化<br>Adoption of 3D Stacking | TSVやHybrid Bondingで垂直接続<br>Vertical links via TSV/hybrid |
| **今後** | チップレットの標準化<br>Chiplet Standardization | UCIeなどの業界標準I/Fへ<br>Industry-wide interfaces like UCIe |

---

## 🧩 次節への接続  
## 🧩 Connection to Next Section

次節 [**2.2：2.5D実装技術**](./f2_2_25d_pkg.md) では、シリコンインターポーザやTSMCのCoWoSといった**具体的な実装技術**について詳しく解説します。  
In the next section [**2.2: 2.5D Integration Technologies**](./f2_2_25d_pkg.md), we explore specific implementation techniques such as **silicon interposers** and **TSMC's CoWoS** in detail.

---
