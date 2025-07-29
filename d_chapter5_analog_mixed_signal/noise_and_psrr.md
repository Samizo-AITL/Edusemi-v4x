# 🔇 ノイズ設計とPSRR（電源変動耐性）  
# 🔇 Noise Design and PSRR (Power Supply Rejection Ratio)

---

## 📘 概要｜Overview

アナログ回路は、微小な信号を扱うため**ノイズや電源変動**の影響を強く受けます。  
本節では、回路・レイアウトの両視点からノイズ対策を整理し、**PSRR（Power Supply Rejection Ratio）**という代表的な設計指標を中心に解説します。

Analog circuits are highly sensitive to **noise and power supply variations** due to their small signal levels.  
This section organizes countermeasures from both circuit and layout perspectives, focusing on the key metric **PSRR (Power Supply Rejection Ratio)**.

---

## 🧭 ノイズの種類と発生源｜Noise Types and Sources

| 🎧 **ノイズ種別｜Noise Type** | 📘 **特徴｜Characteristics** | ⚙️ **主な発生源｜Main Source** |
|------------------------------|------------------------------|-----------------------------|
| 熱雑音（熱ノイズ）<br>Thermal Noise | 白色ノイズ、温度比例<br>White noise, proportional to temperature | 抵抗、MOSチャネル<br>Resistors, MOS channels |
| 1/fノイズ（フリッカ）<br>Flicker Noise | 低周波数で増加<br>Increases at low frequencies | MOSトランジスタ（特にPMOS）<br>MOSFETs, especially PMOS |
| 電源ノイズ<br>Supply Noise | リップルやスパイク<br>Ripple and spikes | 電源配線、レギュレータ<br>Power rails, regulators |
| クロストーク<br>Crosstalk | 隣接配線の干渉<br>Inductive or capacitive coupling | 長い並走配線、クロック系<br>Parallel wires, clock signals |
| サブストレートノイズ<br>Substrate Noise | 基板経由の干渉伝播<br>Coupling through substrate | デジタル→アナログ領域<br>Digital to analog domains |

---

## 🧪 PSRR（Power Supply Rejection Ratio）

| 🧩 **内容｜Item** | 📘 **説明｜Description** |
|------------------|--------------------------|
| **定義｜Definition** | 電源変動が出力にどれだけ影響するかを表す（dB単位）<br>Indicates how much supply variation affects the output |
| **理想｜Ideal Behavior** | PSRRが高いほど電源ノイズに強い<br>Higher PSRR means better noise immunity |
| **項目｜Components** | PSRR+（正電源側）／PSRR−（負電源・GND側）<br>Evaluate both VDD and GND paths |
| **計算式｜Formula** | `PSRR = 20 × log10(ΔVDD / ΔVOUT)` |

---

## ⚙️ 対策例（回路側）｜Circuit-Level Countermeasures

- **カスコード構成**：出力インピーダンスを上げ、電源変動をブロック  
  *Use cascode stages to raise output impedance and suppress supply influence*
- **負帰還回路**：出力安定化とノイズ除去  
  *Negative feedback stabilizes output and suppresses noise*
- **差動構成**：共通モードノイズの除去効果  
  *Differential circuits cancel common-mode noise*

---

## 🧱 対策例（レイアウト側）｜Layout-Level Countermeasures

| 🧩 **対策｜Technique** | 📘 **内容｜Description** |
|-----------------------|--------------------------|
| アナログ・デジタル電源分離<br>Separate Power Rails | 別バス・LDO介在・専用レギュレータなど<br>Separate buses, LDO insertion, dedicated regulators |
| ガードリングとウェル隔離<br>Guard Ring & Well Isolation | 寄生経路・ノイズ注入の遮断<br>Block parasitic paths and noise injection |
| サブストレートコンタクト密度<br>Substrate Contact Density | GNDの等電位化・振動除去<br>Equalize substrate potential and prevent disturbance |

---

## 🧰 SPICEシミュレーション指標｜SPICE Simulation Metrics

- **AC解析（.AC）**：PSRRの周波数特性評価  
  *Frequency-domain PSRR analysis*
- **過渡解析（.TRAN）**：電源リップル応答の確認  
  *Transient response to supply ripple*
- **ノイズ解析（.NOISE）**：熱雑音・1/fノイズのスペクトル観察  
  *Spectral analysis of thermal and flicker noise*

---

## 🎯 教材的意義｜Educational Significance

- 「ノイズに弱い＝設計ミス」とならないよう、**物理構造と伝播経路の理解**が重要  
  *Designing for noise immunity requires structural awareness, not just fixing flaws*
- **混載環境でのノイズ管理**はデジタル設計者にも必須の知識  
  *Noise management is essential knowledge for digital engineers in mixed-signal SoC*
- **PSRRを“環境耐性”として捉え、定量評価できる習慣**を持つ  
  *Treat PSRR as an environmental robustness metric and evaluate it quantitatively*

---

## 🔗 次のセクション｜Next Section

▶️ [`mixed_signal_interface.md`](./mixed_signal_interface.md)：ADC/DACなどのデジアナ境界設計へ  
*Mixed-signal interface design (ADC/DAC)*

---

### 📘 応用編 第5章：アナログ／ミックスドシグナル｜Analog / Mixed-Signal Design  
[➡️ 章の詳細へ進む｜Go to Chapter](./d_chapter5_analog_mixed_signal/README.md)

---

© 2025 **Shinichi Samizo** / MIT License
