---
layout: default
title: アナログレイアウト設計の注意点
---

---

# 🧱 アナログレイアウト設計の注意点  
**🧱 Key Considerations in Analog Layout Design**

---

## 📘 概要｜Overview

アナログ回路は、**トランジスタの微細なばらつきや配線構造の違い**によって性能が大きく変化します。  
そのため、**レイアウト段階での工夫が回路特性の安定性と信頼性に直結**します。

This section explains the **critical layout practices in analog circuit design**, where **small mismatches and layout variations** can significantly affect performance.

---

## 🧭 代表的な設計方針と対策｜Layout Strategies and Best Practices

| 🧩 **項目｜Item** | 🛠️ **説明｜Description** | 🎯 **意図｜Purpose** |
|------------------|---------------------------|----------------------|
| **対称配置**<br>Symmetric Placement | 差動対などは物理的に完全対称に配置<br>Layout differential pairs symmetrically | オフセット・ばらつき低減<br>Reduce offset and mismatch |
| **共通中心配置**<br>Common Centroid | 勾配の影響を均等に分布<br>Distributes gradient effects evenly | 温度・ストレス勾配対策<br>Mitigate temperature and stress gradients |
| **マッチング**<br>Matching | 寸法・配置・方向を一致させる<br>Match W/L, placement, orientation | トランジスタ特性一致<br>Ensure identical device behavior |
| **等長配線**<br>Iso-Length Routing | 差動配線の長さを一致<br>Match routing length of differential signals | 遅延差とクロストーク抑制<br>Suppress delay skew and coupling |
| **ウェル共有・隔離**<br>Well Sharing & Isolation | 同一バイアス素子は共有、異なる場合は隔離<br>Share wells for same bias, isolate others | クロストーク／ラッチアップ防止<br>Prevent crosstalk and latch-up |

---

## 🧪 共通中心配置（例：4分割）｜Common Centroid Example (4-Way Split)

```
A B  
B A
```

- 左右対称だけでなく、**勾配による非対称影響も打ち消す**  
- 高精度電流ミラーやバイアス生成で多用される  

Not only symmetric, but **also cancels gradient-induced mismatch**.  
Widely used in precision current mirrors and bias circuits.

---

## 🛡️ ガードリングの活用｜Use of Guard Rings

- **寄生電流やノイズを遮断**する構造的バリア  
- 電源/GNDと接続し、回路領域を囲う  
- 特に**高感度入力段や基準生成部**では必須  

Acts as a **structural barrier** to isolate noise and leakage.  
Connected to VDD or GND. Essential for sensitive nodes like inputs or references.

---

## 🧱 ウェル構成の整理｜Well Structures in Analog Layout

| 🔧 **構成｜Structure** | 📘 **説明｜Description** |
|----------------------|---------------------------|
| **P-Well / N-Well分離**<br>Separate Wells | 異なる電位間にはガードリングで絶縁<br>Isolate different potentials using guard rings |
| **Deep N-Well構造**<br>Deep N-Well | 深堀構造で寄生バイポーラをブロック<br>Reduces substrate noise and parasitic bipolar effects |
| **Analog/Deep Analog領域**<br>Analog Isolation Regions | 高アイソレーション専用領域をPDKが提供することもあり<br>Some PDKs offer special analog isolation regions |

---

## 📐 設計ルール例（0.18µm）｜Design Rule Examples (0.18µm Node)

- **最小トランジスタ間距離**：1.0 µm 以上  
  *Minimum spacing: ≥ 1.0 µm*
- **ガードリング幅**：3.0 µm 以上  
  *Guard ring width: ≥ 3.0 µm*
- **共通中心配置単位**：2×2 または 4×1  
  *Common centroid unit: 2×2 or 4×1 layout cells*

---

## 🎯 教材的意義｜Educational Significance

- アナログ設計では、**回路図よりもレイアウトが性能を決める**場面が多い  
  *Layout often dominates over schematic in analog performance*
- 対称性・マッチング・ウェル構造といった**構造上の工夫**が重要  
  *Structural symmetry and matching are key to robust analog design*
- **AMSブロックを統合するデジタル設計者**にも不可欠な知識  
  *Even digital designers must understand these when integrating AMS blocks*

---

## 🔗 次のセクション｜Next Section

▶️ [`noise_and_psrr.md`](./noise_and_psrr.md)：ノイズと電源変動耐性の設計へ  
*Noise and PSRR design considerations*

---

### 📘 応用編 第5章：アナログ／ミックスドシグナル｜Analog / Mixed-Signal Design  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 **Shinichi Samizo** / MIT License
