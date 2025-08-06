---
layout: default
title: 2a.2 SI/PIとPDN設計
---

# 2a.2 SI/PIとPDN設計  
**2a.2 Signal/Power Integrity and PDN Design**

---

## 📘 概要｜Overview

本節では、SystemDKにおける中核物理制約である  
**SI（Signal Integrity）と PI（Power Integrity）**の基礎と設計論を扱います。

This section focuses on the fundamentals and design methods of  
**Signal Integrity (SI)** and **Power Integrity (PI)**, which are key physical constraints in SystemDK.

SI/PIは、パッケージ設計・基板設計・チップ間I/Oにおいて  
**「信号が正しく届くか」「電圧が正しく供給されるか」**を保証するための設計概念です。

---

## 🔍 SI（Signal Integrity）とは｜What is SI?

| 要素 | 説明 / Description |
|------|-------------------|
| 反射（Reflection） | インピーダンス不整合による波形の跳ね返り |
| クロストーク（Crosstalk） | 近傍信号線間の電磁結合による干渉 |
| 遅延（Delay）・スキュー（Skew） | 信号の伝搬遅延と経路長差によるタイミングずれ |
| リングイング（Ringing） | 過渡波形が収束せずに振動する現象 |
| パッケージ経路 | Bump → RDL → Substrate配線により構成されるSI経路 |

**設計対策**：
- トレースのインピーダンス整合（例：50Ω）
- 適切なターン数、スタブ抑制、終端抵抗
- チップレットI/F（UCIe等）の物理検証

---

## ⚡ PI（Power Integrity）とは｜What is PI?

| 要素 | 説明 / Description |
|------|-------------------|
| IRドロップ（IR Drop） | 電源供給経路の抵抗成分による電圧低下 |
| Ldi/dt ノイズ | 急激な電流変化による誘導ノイズ（パッケージインダクタンス） |
| グランドバウンス | GNDラインでの電位上昇（ノイズ源） |
| デカップリング容量 | ローカルな電源安定化のためのコンデンサ配置 |
| PDN（Power Delivery Network） | 電源供給パスのモデル：VRM → パッケージ → ダイ内部へ |

**設計対策**：
- PDNシミュレーション（Z特性：インピーダンス vs 周波数）
- 低ESLコンデンサ配置、インダクタンス抑制
- 複数電源階層の分離・配電戦略

---

## 🧰 PDNとSI/PIの統合設計｜PDN-Aware Design

PDN設計は、SI/PIの両面から整合が求められる：

- 電源層の配置とGNDリターンパス整備  
  → SI: クロストーク抑制、リターンパス整合  
  → PI: IRドロップ最小化、共通GNDの維持  
- 層構造（Layer Stackup）の制御  
  → 信号層–電源層–GND層の適切なサンドイッチ配置  
- モデル連携（Sパラメータ、IBIS、Spice）による検証

---

## 🎓 教育的メッセージ｜Educational Message

> 信号は“電圧”ではなく“電流経路”で伝わる。  
> 回路図にないリターンパスを、実装設計で“描く”のがSI/PI設計である。

> Signal transmission is not just voltage propagation —  
> it's the complete current-return loop that must be designed and verified.

---

## 🔗 関連節｜Linked Sections

- [`f2a_3_thermal.md`](f2a_3_thermal.md)：熱設計とのトレードオフ
- [`f2a_5_emi_emc.md`](f2a_5_emi_emc.md)：ノイズ対策と共通設計原則
- [`f2a_6_constraint_tradeoff.md`](f2a_6_constraint_tradeoff.md)：制約連成の設計意思決定

---

## 📎 参考資料｜References

- “Power Integrity for I/O Interfaces,” Intel Whitepaper  
- “SI/PI Co-Design Methodology,” JEDEC & IEEE 2401  
- Keysight / Ansys PDN Impedance Viewer Tools  
- UCIe PHY Spec v1.1, Section 6 (Electrical Specs)

---

**[← 戻る / Back to Special Chapter 2 Top](./README.md)**
