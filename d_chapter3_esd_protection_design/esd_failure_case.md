# 💥 ESD破壊の実例と物理解析（Failure Analysis）  
# 💥 ESD Failures and Physical Failure Analysis

---

## 📘 概要 / Overview

ESD設計の妥当性は、**製品評価段階や市場後の不良解析（FA）によって検証される**ことが多くあります。  
ここでは、ESDによる代表的な破壊モードと、その物理的解析手法、設計改善へのフィードバック事例を紹介します。

ESD design validity is often **validated through failure analysis (FA)** during evaluation or after product release.  
This section introduces **common ESD failure modes**, analysis techniques, and design improvement feedback examples.

---

## 🔎 主なESD破壊モードと観察例 / Typical Failure Modes and Observations

| 破壊モード / Mode | 発生メカニズム / Cause | 物理観察例 / Physical Evidence |
|------------------|-------------------------|-------------------------------|
| **ゲート酸化膜破壊**<br>Gate Oxide Breakdown | 高電界による絶縁破壊<br>Dielectric breakdown under high E-field | TEMで酸化膜破壊を観察<br>TEM cross-section shows rupture |
| **S/Dメルト**<br>Source/Drain Melt | 局所加熱・溶融<br>Local heating by high current | OBIRCHで加熱点特定、SEMで溶融痕<br>OBIRCH + SEM reveal damage |
| **メタル断線**<br>Metal Burnout | 過電流による溶断<br>Excessive current melting metal | FIBで空洞・焦げ観察<br>FIB/SEM show voids |
| **パッド下層短絡**<br>Pad Short | ESD素子無効化・直撃<br>Direct damage due to missing clamp | EMMIで光点、FIBで貫通観察<br>EMMI + FIB confirm short |

---

## 🧪 代表的な解析手法 / Representative Failure Analysis Methods

| 手法 / Method | 概要 / Description | 適用例 / Use Cases |
|----------------|--------------------|---------------------|
| **OBIRCH** | 電流加熱による発熱点を可視化<br>Visualizes hot spots due to current | ESDリーク・ショート箇所特定<br>Locate ESD failure points |
| **FIB** (Focused Ion Beam) | 高精度で層を断面切削<br>High-resolution layer cross-sectioning | 層間短絡・膜破壊の観察<br>View short or rupture |
| **SEM** | 表面・断面の形状観察<br>Surface/topography inspection | 金属の溶断・クラック観察<br>Burnout/crack evidence |
| **EDX** | 元素分析（EDS）<br>Elemental analysis | 異物混入・腐食検出<br>Detect contamination or corrosion |
| **EMMI** | 微弱発光の可視化<br>Detects light from failure sites | 放電箇所・リークパスの探索<br>Locate weak discharge or leakage |

---

## 📂 不良事例：設計フィードバックの流れ / Case Studies and Design Feedback

### 🧭 ケース①：GNDパスのDPP距離が長く過電流集中  
**Case 1: Inadequate GND path and long DPP**

- 💥 **症状 / Symptom**：I/O短絡、初期故障率が高い  
- 🔍 **解析 / Analysis**：GND配線が1μm未満、DPP距離5μm以上  
- 🔧 **対応 / Action**：GNDメタル2層化、ビア密度増加で低インダクタンス化

---

### 🧭 ケース②：アナログ入力にESD素子が接続されていなかった  
**Case 2: ESD Protection Missing on Analog Pin**

- 💥 **症状 / Symptom**：高温高湿で不良再現  
- 🔍 **解析 / Analysis**：CDMによりゲート酸化膜が破壊、EMMIにて発光観察  
- 🔧 **対応 / Action**：クランプダイオード追加、入力パスに制限抵抗挿入

---

## 🔄 設計改善との連携 / Feedback Loop for Design Improvement

- 🔁 **FA結果をPDKルールや設計仕様に反映**  
  Use FA insights to refine **PDK constraints and layout guidelines**

- 🤝 **設計者と品質・製造技術者との定期的レビューが不可欠**  
  Establish regular reviews between **design and quality teams**

- 📘 **解析事例は教育教材・設計マニュアルに活用可能**  
  Use FA cases as material for **training and design handbooks**

---

## 📚 教材的意義 / Educational Significance

- 🚨 ESDによる「死に方（Failure Modes）」を具体的に理解  
  Helps visualize how circuits fail due to ESD

- 🧠 **電気現象 ⇄ 物理損傷** の対応を訓練できる  
  Trains mapping between **electrical failure and physical damage**

- 💬 設計と品質の**対話的プロセス**を教材化  
  Promotes a dialog-driven approach to ESD-aware design

---

## 🔗 本章まとめ / Chapter Summary

ESD対策は「設計・配置・評価・解析」が一体化した**防御的設計思想（Defensive Design）**であり、  
**電気・物理・組織をつなぐ重要な教育テーマ**です。

ESD protection requires integration of **design, layout, evaluation, and failure analysis** —  
a prime educational model of **cross-disciplinary engineering**.

---

## 🧭 章全体への導線 / Link to Chapter Overview

📂 [ESD保護設計の章トップへ](../d_chapter3_esd_protection_design/README.md)  
📂 [Back to Chapter Overview: ESD Protection Design](../d_chapter3_esd_protection_design/README.md)

---

© 2025 Shinichi Samizo / MIT License
