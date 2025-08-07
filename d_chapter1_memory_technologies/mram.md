---
layout: default
title: MRAM
---

---

# 🧲 MRAM（Magnetoresistive Random Access Memory）

---

## 📘 概要 / Overview

MRAMは、**磁気トンネル接合（MTJ: Magnetic Tunnel Junction）**を利用して情報を記憶する**不揮発性メモリ**です。  
MRAM is a **non-volatile memory** that stores information using **Magnetic Tunnel Junctions (MTJs)**.

スピン偏極電流で磁化状態を制御することで、「1」または「0」を記録・保持でき、**電源OFFでもデータが消えません**。  
Using spin-polarized currents to switch magnetic states allows data retention even when the power is off.

- **高速・高耐久・不揮発性**という特性を兼ね備え  
- Combines **high-speed, high-endurance, and non-volatility**

---

## 🧩 構造：MTJセル（磁気トンネル接合） / Structure: MTJ Cell

```
 ┌───────────────┐
 │  磁性固定層（方向一定） │  Fixed Magnetic Layer
 ├───────────────┤
 │  絶縁トンネル層       │  Tunnel Barrier
 ├───────────────┤
 │  磁性可変層（書換可能） │  Free Magnetic Layer
 └───────────────┘
```

### 📌 動作原理 / Operating Principle

| 状態 / State | 磁化方向 / Magnetic Orientation | 抵抗 / Resistance | 論理値 / Logic |
|--------------|-------------------------------|------------------|----------------|
| 平行 / Parallel | ↑↑ or ↓↓ | Low / 低 | 1 |
| 反平行 / Antiparallel | ↑↓ or ↓↑ | High / 高 | 0 |

- 書き込み：スピン偏極電流により**可変層の磁化を反転**  
  Write: Flip the free layer's magnetization with spin-polarized current  
- 読み出し：**非破壊読み出し**で抵抗を検出  
  Read: **Non-destructive readout** by sensing resistance

---

## 🔁 書き込み方式の種類 / Types of Write Mechanisms

| 方式 / Type | 特徴 / Feature | 状況 / Status |
|-------------|----------------|----------------|
| STT-MRAM（Spin-Transfer Torque） | セルを通る電流で磁化反転 / Current through cell flips spin | 量産中 / Mass production |
| SOT-MRAM（Spin-Orbit Torque） | 横電流で高速書込 / Fast write via transverse current | 開発中 / Under development |

💡 **STT**はシンプル構造、**SOT**は高性能。設計トレードオフが重要です。  
💡 STT offers simpler design; SOT provides better performance — tradeoffs matter.

---

## 📊 特性比較表 / Comparison Table

| 項目 / Feature | MRAM | SRAM | DRAM | Flash |
|----------------|------|------|------|--------|
| 不揮発性 / Non-volatility | ◎ | × | × | ◎ |
| 書換回数 / Write Endurance | ◎（>10¹⁵） | ◎ | ◎ | △（10⁴〜10⁵） |
| 書換速度 / Write Speed | ◎（SRAM並 / Comparable to SRAM） | ◎ | ○ | ×（µs〜ms） |
| 消費電力 / Power Consumption | ○（中 / Medium） | ○ | △ | ◎ |
| 面積効率 / Area Efficiency | ○（1T1MTJ） | △（6T） | ◎（1T1C） | ◎ |

---

## 🧪 技術展開と製品化 / Technology and Commercialization

- **PDK対応**：TSMC / Samsung / GlobalFoundries などで eMRAM 対応  
  Supported by major foundries (TSMC, Samsung, GF) in PDKs
- **28nmプロセスでeFlash代替に採用例あり**  
  Used as eFlash replacement at 28nm nodes
- **用途例**：マイコン、IoT、センサ、AIチップ  
  Applications: MCUs, IoT, sensors, AI SoCs

---

## 🚧 技術課題 / Technical Challenges

- 高電流による熱問題 / Heat management for high write current  
- CMOSとの統合難易度 / Integration challenges with CMOS  
- 面積効率の改善 / Improving cell area efficiency  

---

## 🧭 SoC設計での意義 / Value in SoC Design

| 活用例 / Use Case | 効果 / Benefit |
|------------------|----------------|
| eFlash代替 | 高耐久・高速書換え |
| キャッシュ | 不揮発キャッシュによる即起動 |
| IoT/省電力SoC | 待機電力削減、リーク抑制 |
| セキュア用途 | 電源断でも状態保持（セキュアブート） |

---

## 📚 教材的価値 / Educational Value

- スピントロニクス応用の好例 / Example of spintronics in action  
- Flash, FeRAM との比較教材 / Comparative memory education  
- STT vs SOT の設計選定力育成 / Learning to choose design options

---

## 🔗 関連章・リンク / Related Chapters

- [feram.md](./feram.md)：FeRAMとの構造比較 / FeRAM comparison  
- [基礎編 第4章](../chapter4_mos_characteristics/)：CMOS回路と不揮発素子設計  
- [応用編 第5章](../d_chapter5_analog_mixed_signal/)：混載LSIと記憶制御

---

🏘 [応用編 第1章：メモリ技術｜Applied Chapter 1: Memory Technologies](../d_chapter1_memory_technologies/README.md)

---

© 2025 Shinichi Samizo / MIT License

