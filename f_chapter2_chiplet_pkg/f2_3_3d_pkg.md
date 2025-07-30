# 2.3 3D積層技術：TSVとハイブリッドボンディング  
# 2.3 3D Stacking Technologies: TSV and Hybrid Bonding

---

## 🏗️ 3D積層とは？  
## 🏗️ What is 3D Stacking?

**3Dパッケージング**とは、複数のチップを**垂直方向に積層し、TSVやバンプなどで直接接続**する実装技術です。  
**3D packaging** refers to stacking multiple dies **vertically** and connecting them using **TSVs, bumps, or hybrid bonding**.

| 技術 | 説明 |
|------|------|
| **TSV** | シリコン基板を貫通する垂直配線<br>Vertical wiring through the silicon substrate |
| **Hybrid Bonding** | 金属層と絶縁層の同時接合<br>Simultaneous bonding of metal and dielectric layers |
| **μ-bump stacking** | 微細バンプによる階層接続<br>Hierarchical connection via micro-bumps |

---

## 🔩 TSV：スルーシリコンビア  
## 🔩 TSV: Through-Silicon Via

### ✦ 概要 / Overview

- シリコン基板を縦方向に貫通する導通ビア  
  Conductive vias penetrating the silicon substrate vertically  
- 一般寸法：**直径 3–10 µm、深さ 50–150 µm（AR > 10）**  
  Typical dimensions: **Diameter: 3–10 µm, Depth: 50–150 µm (AR > 10)**

### ✦ 形成プロセス概要 / Fabrication Steps

1. **深堀りエッチング**（DRIE）  
   Deep Reactive Ion Etching (DRIE)  
2. **絶縁層形成**（SiO₂）  
   Oxide insulation deposition  
3. **バリア・シード層堆積**（TaN, Cu）  
   Barrier and seed layer deposition (TaN, Cu)  
4. **Cu電解めっき → CMP → メタル露出**  
   Cu plating → CMP → Via exposure

### ✦ 利点と課題 / Pros and Cons

| 項目 / Item | 内容 / Description |
|-------------|---------------------|
| **利点**<br>Advantages | 高密度／短遅延／小面積<br>High density, low latency, small footprint |
| **課題**<br>Challenges | 歩留まり／熱管理／応力によるクラック<br>Yield, thermal spread, mechanical stress (cracking) |

---

## ⚡ Hybrid Bonding（ハイブリッドボンディング）  
## ⚡ Hybrid Bonding

### ✦ 原理 / Principle

- **金属–金属**と**絶縁体–絶縁体**を同時に接合  
  Direct bonding of **metal-to-metal** and **dielectric-to-dielectric**
- **中間材料不要なダイレクト接合**方式  
  No intermediate layers – a **direct bonding** approach

### ✦ 代表技術 / Representative Techniques

| 技術名 / Name | 特徴 / Features | 採用例 / Use Cases |
|---------------|------------------|---------------------|
| **Direct Cu-Cu Bonding** | 高密度・極小ピッチ<br>Ultra-fine pitch | TSMC SoIC, Sony CIS |
| **DBI (Direct Bond Interconnect)** | バンプレス・高速伝送<br>Bumpless and high-speed | Xperi, Intel Foveros Direct |

---

### ✦ 技術比較（μ-bump vs Hybrid）  
### ✦ Technology Comparison: μ-bump vs Hybrid Bonding

| 項目 / Parameter | μ-bump接続 / μ-bump | Hybrid Bonding |
|------------------|----------------------|----------------|
| **ピッチ**<br>Pitch | 40–100 µm | 1–10 µm |
| **対応周波数**<br>Bandwidth | ～10 GHz | ～40 GHz以上 |
| **結合層**<br>Bonding Interface | バンプ＋接着層<br>Bump + adhesive | 接着層なし（ダイレクト）<br>Direct contact (no adhesive) |

---

## 🧊 熱とテストの制約  
## 🧊 Thermal and Test Challenges

| 項目 / Item | 課題 / Challenge | 解決策 / Solution |
|-------------|-------------------|--------------------|
| **熱拡散**<br>Heat Dissipation | 下層チップが冷却困難<br>Bottom dies hard to cool | サーマルビア、チップ薄化、ヒートスプレッダ<br>Thermal vias, die thinning, heat spreaders |
| **テスト**<br>Testing | 中間層アクセス困難<br>Access to mid-layers is difficult | BIST、チップ単体テスト構成<br>BIST and pre-stack individual die testing |

---

## 🌐 適用例と今後の展望  
## 🌐 Applications and Future Outlook

| 企業 / Company | 製品・技術名 / Product or Tech | 内容 / Description |
|----------------|-------------------------------|---------------------|
| **Intel** | Foveros, Foveros Direct | ロジック同士の3D積層<br>Logic-on-logic stacking |
| **TSMC** | SoIC | チップ間のダイレクト接続<br>Direct bonding between dies |
| **Sony** | Stacked CIS | 画像センサの3D積層<br>3D stacking of image sensors |

---

## 📎 次節への接続  
## 📎 Connection to Next Section

次節 [**2.4：実例紹介**](./f2_4_pkg_case_study.md) では、これらの**2.5D/3D技術がどのように製品化されているか**、**主要企業の事例**に焦点を当てて解説します。  
In the next section [**2.4: Case Studies**](./f2_4_pkg_case_study.md), we will explore how these **2.5D and 3D technologies** are **implemented in real-world products** from major companies.

---
