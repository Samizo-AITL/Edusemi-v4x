---
layout: default
title: 2.3 3D積層技術 - TSVとハイブリッドボンディング
---

---

# 🧱 2.3 3D積層技術：TSVとハイブリッドボンディング  
**2.3 3D Stacking Technologies: TSV and Hybrid Bonding**

---

## 🏗️ 3D積層とは？｜What is 3D Stacking?

**3Dパッケージング**とは、複数のチップを**垂直方向に積層し、TSVやバンプなどで直接接続**する実装技術です。  
**3D packaging** stacks multiple chips **vertically**, connecting them using **TSVs, bumps, or hybrid bonding**.

| 💡 技術 / Technology | 📝 説明 / Description |
|----------------------|------------------------|
| **TSV** | シリコン基板を貫通する垂直配線<br>Vertical wiring through the silicon substrate |
| **Hybrid Bonding** | 金属層と絶縁層の同時接合<br>Simultaneous bonding of metal and dielectric layers |
| **μ-bump stacking** | 微細バンプによる階層接続<br>Hierarchical stacking via micro-bumps |

---

## 🔩 TSV：スルーシリコンビア｜Through-Silicon Via

### ✦ 概要 / Overview

- シリコンを垂直に貫通する導通ビア  
  *Conductive vias penetrating silicon vertically*  
- 寸法：**直径 3–10 µm、深さ 50–150 µm（AR > 10）**  
  *Typical: 3–10 µm diameter, 50–150 µm depth (AR > 10)*

### ✦ 形成プロセス｜Fabrication Steps

1. **DRIEによる深堀りエッチング**  
   *Deep Reactive Ion Etching (DRIE)*  
2. **絶縁膜形成（SiO₂）**  
   *Oxide layer deposition*  
3. **バリア・シード層堆積（TaN, Cu）**  
   *Barrier/seed layer deposition (TaN, Cu)*  
4. **Cu電解めっき → CMPで研磨**  
   *Cu plating → Chemical Mechanical Polishing*

### ✦ 利点と課題｜Pros and Cons

| ✅ 項目 / Item | 内容 / Description |
|----------------|---------------------|
| **利点**<br>Advantages | 高密度／低遅延／小面積<br>High density, low latency, compact footprint |
| **課題**<br>Challenges | 歩留まり／熱／応力クラック<br>Yield, thermal dissipation, stress cracking |

---

## ⚡ Hybrid Bonding（ハイブリッドボンディング）

### ✦ 原理 / Principle

- **金属–金属**と**絶縁体–絶縁体**を**同時に接合**  
  *Simultaneous bonding of metal and dielectric layers*  
- **中間材不要のダイレクト接合方式**  
  *No adhesive or bumps – pure direct bonding*

### ✦ 代表技術 / Key Techniques

| 💡 技術名 / Technique | 特徴 / Features | 採用例 / Applications |
|------------------------|------------------|------------------------|
| **Direct Cu-Cu Bonding** | 極小ピッチ・高密度<br>Ultra-fine pitch, high density | TSMC SoIC, Sony CIS |
| **DBI (Direct Bond Interconnect)** | バンプレス・高速伝送<br>Bumpless, high-speed | Intel Foveros Direct, Xperi DBI |

---

## 🔍 μ-bumpとの比較｜Comparison with μ-bump

| 🔧 パラメータ / Parameter | μ-bump接続 / μ-bump | Hybrid Bonding |
|---------------------------|----------------------|----------------|
| **ピッチ**<br>Pitch | 40–100 µm | 1–10 µm |
| **伝送帯域**<br>Bandwidth | ～10 GHz | ～40 GHz 以上 |
| **結合界面**<br>Bond Interface | バンプ＋接着層<br>Bump + adhesive | ダイレクト（金属＋絶縁体）<br>Direct metal & dielectric |

---

## 🧊 熱とテストの制約｜Thermal and Test Challenges

| 🧩 項目 / Item | 🛠️ 課題 / Challenge | 💡 解決策 / Solution |
|----------------|-----------------------|------------------------|
| **熱拡散**<br>Thermal Spread | 下層チップが冷却困難<br>Bottom dies hard to cool | サーマルビア・ヒートスプレッダ<br>Thermal vias, heat spreaders |
| **テスト**<br>Testing | 中間層アクセスが困難<br>Mid-layer test access difficult | BIST導入・個別テスト設計<br>BIST, pre-stack testable dies |

---

## 🌐 実用例と今後｜Applications and Outlook

| 🏢 企業 / Company | 技術 / Technology | 内容 / Description |
|------------------|-------------------|---------------------|
| **Intel** | Foveros / Foveros Direct | ロジック同士の3D積層<br>Logic-on-logic stacking |
| **TSMC** | SoIC | ダイレクトボンディング技術<br>Die-to-die direct bonding |
| **Sony** | Stacked CIS | 画像センサの3D集積<br>3D-integrated CMOS image sensors |

---

## 📎 次節への接続｜Connection to Next Section

次節 [**2.4：実例紹介**](./f2_4_pkg_case_study.md) では、これらの**2.5D/3D技術の実用化事例**を紹介し、**企業ごとの採用戦略と構成**に着目します。  
*In the next section [**2.4: Case Studies**](./f2_4_pkg_case_study.md), we explore real-world use cases of 2.5D/3D technologies and how different companies implement them.*

---

## 🏁 特別編 第2章 トップへ戻る｜Back to Chapter 2 Top

🔗 [📚 特別編 第2章 トップに戻る](./README.md)
