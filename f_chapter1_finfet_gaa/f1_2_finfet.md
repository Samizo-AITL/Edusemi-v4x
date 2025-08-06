---
layout: default
title: 1.2 FinFET構造：立体ゲートによる制御強化
---

---

# 🧬 1.2 FinFET構造：立体ゲートによる制御強化  
## 1.2 FinFET Structure: Enhanced Electrostatic Control via 3D Gate

---

## 📘 概要 / Overview

**FinFET（Fin Field-Effect Transistor）**は、プレーナ型MOSFETが抱えるスケーリング限界—特に**短チャネル効果（SCE）**や**DIBL（Drain-Induced Barrier Lowering）**—を克服するために開発された革新的構造です。  
ゲート電極がチャネルを**3面から包囲する立体構造（Tri-Gate）**により、従来を超える制御性と性能を実現します。

FinFET is a 3D transistor structure designed to overcome the scaling limitations of planar MOSFETs. By wrapping the gate around the channel on **three sides**, FinFETs achieve superior electrostatic control, reducing leakage and enhancing performance.

---

## 🔹 1.2.1 FinFETの構造原理  
### Structural Principle of FinFET

- **Fin構造（Fin Structure）**  
  - チャネルはシリコン基板から立ち上がる**ヒレ状構造（Fin）**上に形成される  
  - Finの**幅（W<sub>fin</sub>）×高さ（H<sub>fin</sub>）**がチャネル断面積を決定

- **ゲート構造（Gate Structure）**  
  - ゲート電極はFinの**上面＋側面（左右）**を包囲し、**三面制御（Tri-Gate）**を実現  
  - 包囲率が高いため、**しきい値電圧の制御性が向上**し、DIBLやSCEを抑制

- **制御効果 / Control Benefits**  
  - SS ≒ 70 mV/dec、リーク電流の大幅低減  
  - 複数Finの並列設計により、**電流スケーリングが段階的に可能**

---

## 🔸 1.2.2 プレーナMOSとの構造比較  
### Comparison with Planar MOSFET

| **特性項目 / Feature**       | **プレーナMOSFET / Planar** | **FinFET** |
|------------------------------|-------------------------------|------------|
| チャネル配置 / Channel Location | 基板面上 / On substrate surface | Fin構造（立体） / Vertical fin |
| ゲート包囲面 / Gate Coverage   | 上面のみ / Top only            | 三面（Top + Sides） |
| SCE制御性 / SCE Control        | 弱い / Limited                 | 強力 / Excellent |
| チャネル幅設計 / Channel Width Design | 連続量 / Continuous          | 離散値（1Fin, 2Fin…） / Discrete (by Fin count) |

---

## 🏗 1.2.3 プロセス概要  
### Process Overview of FinFET Fabrication

1. **STI（Shallow Trench Isolation）**  
   Finの土台となる分離構造を形成  
2. **Finパターニング（Patterning）**  
   ArF液浸/EUVで微細Fin形状を形成 → RIEで高アスペクト比化（CD精度：≦2nm）  
3. **Fin酸化処理（Optional）**  
   熱酸化でFinエッジをラウンド化・寸法微調整  
4. **ゲートスタック形成（Gate Stack）**  
   ハイk酸化膜（例：HfO₂）＋メタルゲート（例：TiN）を**3面成膜**  
5. **ゲートパターニング・ソース/ドレイン形成**  
   Dummy Gate方式やGate First方式。シリサイド形成やエピ成長など含む

> 📎 詳細は補足資料 [appendixf1_01_finfetflow.md](./appendixf1_01_finfetflow.md) を参照

---

## 🧠 1.2.4 FinFETと設計の関係  
### Design Implications of FinFET

- **Fin数 = チャネル幅の単位（Discrete Width）**  
  → 1Fin, 2Fin, 3Fin…と**段階的な設計**になる（連続W指定不可）

- **PDK制約（Design Rules）**  
  - 最小Finピッチ、Fin高さ制限、ゲート下Fin切断可否などが決まっている  
  - **配置は設計グリッドに整合**させる必要がある

- **寄生要素 / Parasitic Effects**  
  - 高アスペクトFinによる**寄生容量・GIDL・SS劣化**などに注意  
  - 配線との3D RC抽出が必須

---

## 🖼 図版リンク（予定 / Planned Images）

- `images/finfet_structure.png`  
  → FinFETの断面構造図（Fin＋ゲートの関係）  
- `images/finfet_gate_wrap.png`  
  → 三面ゲート制御の模式図（Tri-Gate vs Planar）

---

## ✅ まとめ / Summary

FinFETは、プレーナ構造では制御できなかったSCEやDIBLといった**物理限界を根本から解決する構造改革**でした。  
22nm世代以降の主流トランジスタであり、Fin数による設計スケーリングや**PDK依存のレイアウト制約**への理解が必要不可欠です。

FinFET overcomes the fundamental limitations of planar MOSFETs by introducing 3D gate control. It has become the mainstream transistor architecture from the 22nm node onward. Designers must understand discrete fin-based scaling and PDK constraints to effectively utilize FinFET technology.

---

📘 次節：[1.3 GAA構造とMulti-Nanosheet技術](f1_3_gaa.md)

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)
