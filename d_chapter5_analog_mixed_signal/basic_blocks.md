---
layout: default
title: アナログ基本回路構成：Op-Amp、Buffer、Comparator
---

---

# 🔧 アナログ基本回路構成：Op-Amp、Buffer、Comparator  
# 🔧 Basic Analog Building Blocks: Op-Amp, Buffer, Comparator

---

## 📘 概要｜Overview

アナログ／ミックスドシグナル設計では、**演算増幅器（Op-Amp）やコンパレータ、バッファなどの基本ブロック**が多くの回路の構成要素となります。  
これらの構成と動作原理を理解することは、**ADC/DAC設計や電源制御などの応用回路**へ進む上での基盤となります。

In AMS design, **basic analog blocks such as operational amplifiers (Op-Amps), comparators, and buffers** are fundamental components.  
Understanding their structure and operating principles is essential for progressing toward **ADC/DAC design and power control applications**.

---

## 🧪 1. 演算増幅器（Operational Amplifier, Op-Amp）

| ⭐ **特徴｜Features** | 📘 **説明｜Description** |
|----------------------|-------------------------|
| 高ゲイン<br>High Gain | 微小な差分入力でも大きな出力変化を生成<br>Generates large output for small differential input |
| 差動入力<br>Differential Input | 2つの入力端子（Vin+ / Vin−）を持つ<br>Has two inputs: Vin+ and Vin− |
| 負帰還設計<br>Negative Feedback | 安定動作や所望のゲイン制御に使用される<br>Used for stable operation and gain control |
| 主用途<br>Main Uses | 電圧増幅、積分器、フィルタ、電圧フォロワ等<br>Voltage amplification, integrators, filters, voltage followers |

📌 **基本構成｜Typical Structure**  
- 差動入力ペア（NMOS or PMOS）  
  *Differential input pair (NMOS or PMOS)*  
- 電流ミラー型アクティブ負荷  
  *Active load using current mirrors*  
- 出力ステージ（クラスAB等）  
  *Output stage (e.g., class AB)*

📎 **設計指標｜Key Design Metrics**  
- DCゲイン（DC gain）、帯域幅（bandwidth）、スルーレート（slew rate）、CMRR、PSRR

---

## 🔁 2. バッファ（Voltage Follower）

| ⭐ **特徴｜Features** | 📘 **説明｜Description** |
|----------------------|--------------------------|
| ゲイン1（ユニティ）<br>Unity Gain | 入力をそのまま出力へコピー<br>Output follows the input exactly |
| 高入力インピーダンス<br>High Input Impedance | 信号源への負荷を軽減<br>Minimizes loading on signal sources |
| 低出力インピーダンス<br>Low Output Impedance | 後段駆動能力を向上<br>Enhances driving ability of next stage |
| 主用途<br>Main Uses | センサ出力、ADC入力、信号絶縁、レベルシフト後段など<br>Sensor output, ADC input, isolation, post level-shift driving |

📎 **代表構成｜Typical Configuration**  
Op-Amp＋負帰還による「ユニティゲイン構成」  
*A unity-gain configuration using Op-Amp and negative feedback*

---

## ⚖️ 3. コンパレータ（Comparator）

| ⭐ **特徴｜Features** | 📘 **説明｜Description** |
|----------------------|--------------------------|
| 2つの入力電圧を比較<br>Voltage Comparison | Vin+ > Vin− ならHigh出力、逆ならLow出力<br>Outputs High if Vin+ > Vin−, else Low |
| 高速応答<br>Fast Response | ゲインが高く、ヒステリシス制御可能<br>High gain, supports hysteresis control |
| クロスオーバ判定<br>Threshold Detection | ゼロクロス検出やしきい値超過判定に使用<br>Used for zero-cross and threshold detection |
| 主用途<br>Main Uses | A/D変換、ゼロクロス検出、デジタル制御回路のトリガ等<br>ADC, zero-cross detection, digital control trigger circuits |

📎 **構成上の違い｜Design Distinction**  
オペアンプに似ているが、**負帰還をかけない構成**  
*Unlike Op-Amp, designed without negative feedback*

---

## ⚙️ 補足ブロック：電流ミラー、バイアス回路  
## ⚙️ Supplemental Blocks: Current Mirror & Bias Circuits

- **電流ミラー｜Current Mirror**  
  一定電流源としてOp-Ampやバッファの動作を安定化  
  *Provides stable current source for Op-Amps and buffers*

- **バイアス回路｜Bias Circuit**  
  リファレンス電圧・電流生成に用いる。Bandgap型など、**温度補償付き構成**が一般的。  
  *Generates reference voltages/currents; often includes temperature compensation (e.g., bandgap references)*

---

## 🎯 教材的ポイント｜Learning Points

- 各回路の**入力／出力関係と動作原理**を理解  
  *Understand input-output relationships and operation principles*
- SPICEシミュレーションによる**DCスイープ、過渡応答、ステップ応答**の観察  
  *Practice DC sweep, transient, and step response using SPICE simulation*
- **レイアウトでの対称性やマッチングの重要性**を次章でさらに学習  
  *Layout-dependent matching and symmetry will be covered in the next section*

---

## 🔗 次のセクション｜Next Section

▶️ [`layout_considerations.md`](./layout_considerations.md)：アナログレイアウトの設計注意点へ  
*Analog layout design considerations*

---

### 📘 応用編 第5章：アナログ／ミックスドシグナル｜Analog / Mixed-Signal Design  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 **Shinichi Samizo** / MIT License
