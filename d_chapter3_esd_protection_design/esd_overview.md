---
layout: default
title: ESD概要と保護設計の重要性
---

---

# ⚠️ ESD概要と保護設計の重要性  
**⚠️ Overview of ESD and Importance of Protection Design**

---

## 📘 概要 / Overview

**ESD（Electrostatic Discharge：静電気放電）**とは、人体や装置などに蓄積された静電気が半導体チップに放電される現象です。  
瞬間的な高電圧（数百V〜数kV）は、ICの微細な構造を破壊し、**動作不良や故障の主因**となります。

In short, **ESD (Electrostatic Discharge)** is a sudden flow of electricity between two electrically charged objects, often occurring when a person or device touches an IC.  
Such high-voltage pulses (hundreds to thousands of volts) can **damage delicate IC structures**, leading to malfunctions or permanent failure.

> 🎯 **現代の微細CMOSでは、ESD対策は「設計段階の前提条件」かつ「信頼性設計の起点」です。**  
> 🎯 **In modern fine CMOS nodes, ESD protection is a "design prerequisite" and the starting point of reliability engineering.**

---

## 💡 なぜESDが問題なのか？ / Why is ESD a Critical Issue?

| 項目 / Factor       | 説明 / Description |
|---------------------|--------------------|
| **電圧スパイク**<br>Voltage Spike | 数ns〜数10nsの間に数kVの過渡的パルスが発生<br>Transient pulses of several kV within a few to tens of nanoseconds |
| **電流量**<br>Current Surge | ピーク1A〜10A以上流れることもある<br>Peak currents can exceed 1A–10A |
| **影響対象**<br>Target Area | I/O端子、電源/GND、アナログ端子など<br>I/O pins, power/GND lines, analog interfaces |
| **破壊結果**<br>Damage Effects | 酸化膜破壊、配線溶断、寄生トランジスタ動作<br>Gate oxide breakdown, metal fusing, latch-up |

---

## 🧪 ESDの主な発生モデル / Major ESD Models

| モデル / Model | 意味・状況 / Description | 電圧・電流の目安 / Typical Voltage & Current |
|----------------|---------------------------|---------------------------------------------|
| **HBM**<br>(Human Body Model) | 人体がICに触れたときのモデル<br>Discharge from human body | ±2kV、1A〜3A |
| **MM**<br>(Machine Model) | 機器や治具による放電<br>Discharge from equipment/tools | ±200V、数A |
| **CDM**<br>(Charged Device Model) | デバイス自体が帯電して放電<br>IC itself is charged and discharges | ±1kV〜2kV、10A以上（高速）<br>Over 10A at high speed |

> 💥 **CDMは特に高速かつ高電流で破壊力が強く、近年の主な破壊要因です。**  
> 💥 **CDM poses the greatest threat due to its high-speed, high-current discharge characteristics.**

---

## 🔧 設計におけるESD保護の基本方針  
**🔧 Basic Principles of ESD Protection in Design**

- **外部からの放電電流を素早く逃がすパスを用意する**  
  Provide a fast discharge path for incoming ESD current.
- **脆弱な領域（ゲート酸化膜など）を通させない**  
  Prevent the discharge current from passing through sensitive areas (e.g., gate oxide).
- **ESD保護素子は本回路の前に配置する**  
  Place ESD protection devices before the core circuit.

---

## 🔁 設計フローにおける位置づけ / Placement in the Design Flow

```
[外部I/O] → [ESD保護素子] → [ESD制限抵抗] → [本回路]
[External I/O] → [ESD Protection Device] → [Current-limiting Resistor] → [Core Circuit]
```

- **パッドセル内にESD素子を実装（例：GGNMOS、ダイオード等）**  
  Implement protection devices like GGNMOS or diodes within the pad cell.
- **電源電圧ごとに構造を最適化（1.8V系、3.3V系など）**  
  Separate and optimize structures by voltage domain (e.g., 1.8V, 3.3V).
- **アナログ端子やミックスド信号ラインは特に注意が必要**  
  Special care is required for analog or mixed-signal pins.

---

## 📚 教材的意義 / Educational Significance

- **回路設計者がESD対策の回路・物理構造を体系的に学べる**  
  Enables designers to learn both the **circuit-level and physical aspects** of ESD protection.
- **破壊事例と品質保証の関連を理解できる**  
  Connects real-world failure cases with **quality assurance practices**.
- **設計段階からの防御的思考（Defensive Design）を育成**  
  Cultivates a mindset of **defensive design from the early design phase**.

---

## 🔗 次のセクション / Next Section

👉 [`esd_devices.md`](./esd_devices.md)：ESD保護素子の構造と動作原理へ  
👉 [`esd_devices.md`](./esd_devices.md): Structure and Operating Principles of ESD Protection Devices

---

## 🧭 章全体への導線 / Link to Chapter Overview

📂 [ESD保護設計の章トップへ](../d_chapter3_esd_protection_design/README.md)  
📂 [Back to Chapter Overview: ESD Protection Design](../d_chapter3_esd_protection_design/README.md)

---

© 2025 Shinichi Samizo / MIT License



