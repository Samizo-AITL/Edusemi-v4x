# 🔋 IRドロップとエレクトロマイグレーション（EM）対策  
# 🔋 IR Drop and Electromigration Countermeasures

---

## 📘 概要 | Overview

配線抵抗や電流密度が設計限界を超えると、**電圧降下（IRドロップ）**や**金属損傷（EM）**が発生し、  
回路の動作不良や製品寿命の劣化を引き起こします。  
When interconnect resistance or current density exceeds design limits, **IR drop** and **electromigration (EM)** occur,  
leading to circuit malfunction and reduced product lifetime.

本節では、**電源レイアウトの設計技術と物理的な破壊メカニズム**を体系的に学びます。  
This section covers **power layout design strategies and the physical failure mechanisms** involved.

---

## ⚡ IRドロップとは | What is IR Drop?

| 要因 / Cause | 内容 / Description |
|---------------|--------------------|
| **配線抵抗（R）<br>Wire Resistance** | GND/VDD配線が細く長いと抵抗が大きくなる<br>Thin or long power lines have high resistance |
| **電流（I）<br>Current** | 大電流を消費するロジック／I/O負荷<br>High current drawn by logic or I/O circuits |
| **電圧降下（V = I×R）<br>Voltage Drop** | 電源経路で想定外の電圧降下が発生<br>Unexpected voltage drop along power routes |
| **影響 / Effect** | ゲートVthの変化、タイミング遅延、誤動作の可能性<br>Changes in gate threshold, timing delays, malfunction risk |

---

## 🔥 エレクトロマイグレーション（EM）とは | What is Electromigration?

| 要因 / Cause | 内容 / Description |
|--------------|---------------------|
| **高電流密度<br>High Current Density** | 金属中の原子が電流によって移動（原子フラックス）<br>Metal atoms migrate due to current (atomic flux) |
| **断線・盛り上がり<br>Void / Hillock** | Void形成で断線、Hillock形成で短絡の危険性<br>Voids cause opens; hillocks cause shorts |
| **信頼性劣化<br>Reliability Degradation** | 時間経過で劣化が進行 → 製品寿命短縮<br>Degradation accumulates over time → reduced lifetime |
| **対象領域 / Target Areas** | Metal層、Via、コンタクト等の全導通部<br>All conductive parts: metal, vias, contacts |

---

## 🛠️ 設計対応と実装ポイント | Design Techniques and Practical Measures

| 対策項目 / Countermeasure | 内容 / Description |
|---------------------------|---------------------|
| **パワーグリッド強化<br>Power Grid Enhancement** | VDD/GNDを多層かつ太線で構成<br>Use wide, multi-layer power lines |
| **IRシミュレーション<br>IR Simulation** | Static/Dynamic IRをEDAツールで解析<br>Analyze IR drop using EDA tools |
| **Via冗長化<br>Via Redundancy** | 複数Viaを並列配置し電流分散<br>Place multiple vias to reduce current concentration |
| **EMチェック<br>EM Verification** | EM解析ツールで電流密度分布を可視化<br>Visualize current density via EM tools |
| **Current Aware Routing** | 電流制約を反映した自動配線設計<br>Auto-routing that accounts for current limits |
| **除外領域設定<br>Exclusion Regions** | 高速クロックやアナログ部をIR/EM解析から除外設定<br>Exclude critical analog/clock regions from EM/IR analysis |

---

## 📐 設計ルールの一例（0.18μm世代）  
## 📐 Example Design Rules (0.18μm Node)

- **IRドロップ許容値 / IR Drop Allowance**：最大 ±100 mV  
  *Typical IR drop threshold: ±100 mV for timing integrity*
- **EM電流密度限界 / EM Current Density Limit**：1–2 MA/cm²（温度依存）  
  *Typical limit: 1–2 MA/cm², varies with temperature*
- **Via当たり電流許容 / Via Current Tolerance**：1 Via ≒ 最大 2–5 mA  
  *Each via typically tolerates 2–5 mA*

---

## 🎯 教材的意義 | Educational Perspective

- 🧠 「IRドロップ」を**電圧降下×タイミング変動**として物理的に理解  
  Understand IR drop through **voltage drop × timing impact**
- 🛡 EM対策を**製品信頼性と寿命設計**の核として捉える  
  See EM prevention as core to **reliability and lifetime design**
- 🛠 配線設計が物理現象と密接に関係していることを実感  
  Realize how **layout design directly links to physical failure mechanisms**

---

## 🔗 次のセクション | Next Section

➡ [`latchup_prevention.md`](./latchup_prevention.md)：寄生構造とラッチアップ対策へ  
➡ *Parasitic Structures and Latch-up Prevention*

---

🧱 応用編 第4章：レイアウト設計と最適化 /  
🧱 *Applied Chapter 4: Layout Design and Optimization*  
[📘 セクション一覧 / Section Index](../d_chapter4_layout_optimization/README.md)

---

© 2025 Shinichi Samizo / MIT License
