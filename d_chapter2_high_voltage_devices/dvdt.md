# ⚡ dv/dt耐性と電界破壊対策｜dv/dt Immunity and Breakdown Protection

---

## 📘 概要｜Overview

**高耐圧デバイスでは、高電圧そのものよりも急激な電圧変化（dv/dt）がデバイス破壊を引き起こすことがあります。**  
**In high-voltage devices, it is not only the voltage magnitude but also the sharp rate of voltage change (dv/dt) that may trigger breakdown or malfunction.**

主に以下の現象が問題になります：  
Key destructive effects include:

- **ゲート絶縁膜の局所電界集中**  
  *Localized electric field breakdown of gate oxide*
- **寄生トランジスタ（npn）の不意動作**  
  *Unintentional triggering of parasitic transistors*
- **配線誘導ノイズによるスパイク電流**  
  *Inductive spike currents from interconnects*

---

## ⚠️ dv/dtによる破壊モード｜Failure Modes by dv/dt

| モード｜Mode | 発生条件｜Trigger | 対策例｜Countermeasure |
|----------------|---------------------|-------------------------|
| **ゲート酸化膜破壊**<br>Gate Oxide Breakdown | 瞬時にVgs上昇（誘導）<br>Sharp Vgs rise by induction | 酸化膜厚増、クランプ回路<br>Thicker oxide, clamp circuit |
| **ラッチアップ**<br>Latch-up | Substrateに誘導 → npn動作<br>Induced current triggers parasitic npn | ガードリング配置、ウェルバイアス強化<br>Guard ring, well bias |
| **スパイク電流**<br>Spike Current | 外部dv/dtが内部に誘導<br>External dv/dt noise couples internally | スルーレート制御、ドレイン抵抗<br>Slew-rate control, drain resistor |

---

## 🧪 dv/dtテスト手法｜Testing Methods

- **入力端子に急峻なパルス（例：100V/ns）を印加**  
  *Apply fast pulse waveform to input (e.g., 100V/ns)*  
- **絶縁破壊の閾値・ラッチ挙動を観測**  
  *Measure breakdown threshold and latch-up occurrence*  
- **誤動作やスパイク電流のログ取得**  
  *Log false operation and current spikes*

---

## 🔧 dv/dt対策設計｜Design Countermeasures

### ✅ ゲート酸化膜保護｜Gate Oxide Protection

- 酸化膜を**5〜10nm以上**で厚膜設計  
  *Use thicker gate oxide (5–10 nm or more)*
- **ゲート直列抵抗・スナバ素子**の挿入  
  *Insert gate series resistor or snubber*
- **ZenerダイオードやTVS素子**による過電圧クランプ  
  *Use Zener or TVS for overvoltage protection*

---

### ✅ 配線誘導とレイアウト｜Interconnect Noise and Layout

- **HVノードと他ノードを十分に離隔**  
  *Ensure spacing between HV and logic nodes*
- **トランジスタ間の寄生容量を抑制**  
  *Minimize parasitic capacitance between devices*
- **ガードリングによる領域隔離**  
  *Use guard rings to isolate sensitive regions*

---

## 📚 教材的意義｜Educational Relevance

- 「耐圧≠安全動作」であることを理解する  
  *Realize that breakdown depends on dv/dt, not just voltage*
- **物理設計と電気的イベント**の関係性を学べる  
  *Understand the link between physical design and electrical transients*
- **誤動作メカニズムの可視化**が行えるテスト事例  
  *Practical case for testing malfunction mechanisms*

---

## 🔗 関連リンク｜Related Topics

- [📘 応用編 第2章｜高耐圧デバイス 全体README](../d_chapter2_high_voltage_devices/README.md)  
  **章全体の構成と関連技術の導入**  
  *Chapter 2 Top: Overview of high-voltage devices and structure of this section*
  
- [`ldmos.md`](./ldmos.md)  
  **高電圧印加による構造ストレスとdv/dt感度**  
  *Structural stress and dv/dt sensitivity in LDMOS*

- [`layout_rules.md`](./layout_rules.md)  
  **高速スイッチング下のレイアウト最適化**  
  *Layout optimization under high-speed switching*

- [chapter6_test_and_package](../chapter6_test_and_package/)  
  **製品段階でのスクリーニングと破壊試験**  
  *Production-level screening and destructive testing*

---

© 2025 Shinichi Samizo / MIT License

---
