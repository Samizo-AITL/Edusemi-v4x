# 🧭 アナログ／ミックスドシグナル設計の概要  
# 🧭 Overview of Analog / Mixed-Signal (AMS) Design

---

## 📘 概要｜Introduction

アナログ／ミックスドシグナル（**Analog Mixed Signal, AMS**）設計は、**現実世界とデジタル回路の橋渡し**を担う重要な領域です。  
温度・電圧・光・音などのアナログ信号を扱うためには、**回路・レイアウト・システムの設計観点を総合的に理解**する必要があります。

**Analog/Mixed-Signal (AMS) design** plays a critical role in **bridging real-world signals and digital circuits**.  
Designers must comprehensively understand **circuits, layout, and system-level considerations** to handle analog signals such as temperature, voltage, light, and sound.

---

## 🔌 なぜアナログが必要か？｜Why Is Analog Needed?

| 🌐 **領域｜Domain** | ⚙️ **アナログの役割｜Analog Role** |
|-------------------|-------------------------------------|
| センサIF | センサ出力の電圧信号を取得・増幅・整形<br>Capture/amplify/shape sensor voltage outputs |
| 電源管理 | リニアレギュレータ、LDO、電流検出回路など<br>Linear regulators, LDOs, current sensing |
| クロック生成 | PLL、VCO、バッファ等によるタイミング制御<br>Timing control using PLLs, VCOs, buffers |
| 通信回路 | 高周波アンプ、ミキサ、フィルタなどのRF系<br>RF circuits like high-frequency amps, mixers, filters |
| デジタル境界 | ADC/DACを介したミックスド信号変換<br>Mixed-signal conversion via ADC/DAC |

---

## 🧩 AMS回路における特徴｜Key Characteristics of AMS Circuits

- **連続量を扱う**：論理0/1ではなく「電圧レベルの変化」で動作  
  *Operates with continuous quantities, not binary logic*
- **感度が高い**：ノイズ、電源変動、温度変化に敏感  
  *Highly sensitive to noise, supply variation, and temperature*
- **レイアウト依存性が大きい**：トランジスタ間の対称性や距離が特性に直結  
  *Strongly layout-dependent (e.g., symmetry, spacing)*
- **シミュレーション時間が長い**：トランジスタレベルで波形解析が必要  
  *Longer simulation times due to transistor-level waveform analysis*

---

## 🏗️ デジタル設計との違い｜Comparison with Digital Design

| ⚙️ **項目｜Aspect** | 🔲 **デジタル回路｜Digital Circuits** | 🔄 **アナログ回路｜Analog Circuits** |
|------------------|-------------------------------|-------------------------------|
| 設計単位 | 論理ゲート、セル<br>Logic gates, cells | トランジスタ、電流源、抵抗<br>Transistors, current sources, resistors |
| 表現手段 | HDL（Verilog等）<br>HDL (e.g. Verilog) | SPICE記述、回路図入力<br>SPICE netlist or schematic |
| シミュレーション | 論理検証、STA<br>Logic check, STA | 波形解析、AC特性、ノイズ評価<br>Waveform, AC, and noise analysis |
| 主な指標 | 遅延、面積、消費電力<br>Delay, area, power | ゲイン、帯域幅、PSRR、SN比<br>Gain, bandwidth, PSRR, SNR |

---

## 📘 本章の構成｜Structure of This Chapter

本章では、AMS設計の実務的な要素を以下の観点で解説します：  
This chapter covers practical aspects of AMS design from the following perspectives:

- [`basic_blocks.md`](./basic_blocks.md)：**基本構成要素**（オペアンプ、コンパレータなど）  
  *Basic building blocks (op-amp, comparator, etc.)*
- [`layout_considerations.md`](./layout_considerations.md)：**アナログレイアウトの注意点**  
  *Analog layout considerations*
- [`noise_and_psrr.md`](./noise_and_psrr.md)：**ノイズ・電源変動耐性の設計指標**  
  *Noise and power supply rejection design metrics*
- [`mixed_signal_interface.md`](./mixed_signal_interface.md)：**デジタル-アナログ境界設計（ADC/DAC）**  
  *Digital-analog interface design (ADC/DAC)*

---

## 🎯 教材的意義｜Educational Significance

- デジタルに閉じない**SoC設計の「アナログ的な土台」**を認識する  
  *Recognize the "analog foundation" of SoC design beyond digital logic*
- **回路設計とレイアウトの連携の重要性**を学ぶ  
  *Learn the importance of coordination between circuit design and layout*
- **高度な設計ではなく、実務で必要なAMS知識に絞って解説**  
  *Focus on practical AMS knowledge rather than advanced theory*

---

### 📘 応用編 第5章：アナログ／ミックスドシグナル｜Analog / Mixed-Signal Design  
[➡️ 章の詳細へ進む｜Go to Chapter](./d_chapter5_analog_mixed_signal/README.md)

---

© 2025 **Shinichi Samizo** / MIT License
