---
layout: default
title: 2a.6 物理制約のトレードオフ設計
---

---

# 2a.6 物理制約のトレードオフ設計  
**2a.6 Trade-off Design for Physical Constraints**

---

## 📘 概要｜Overview

本節では、SystemDKにおける複数の物理制約（熱・電気・機械・EMIなど）を同時に考慮した  
**トレードオフ設計（Constraint Trade-off Design）**の基本指針を解説します。

This section explains basic principles of **constraint trade-off design**,  
which addresses multiple physical domains (thermal, electrical, mechanical, EMI) concurrently in SystemDK.

パッケージ設計・SoC配置・配線構成などの実装レイヤでは、  
**単一制約の最適化が他領域で不具合を生む**ことが多く、バランス重視の設計が求められます。

---

## 🔁 代表的なトレードオフ例｜Representative Trade-offs

| 領域A | 領域B | トレードオフ内容 | 対策例 |
|--------|--------|------------------|--------|
| 熱放熱（Thermal） | EMI/EMC | メタル板による熱拡散 vs 放射ノイズ増加 | 導電性フィルム、接地設計最適化 |
| SI（信号整合） | PI（電源整合） | リターンパス最短化 vs プレーン分割によるノイズ | GNDスティッチ、マルチレイヤGND |
| 応力緩和 | 放熱性 | 柔軟バッファ層 vs 熱伝導率低下 | サーマルバッファ材の選定 |
| 配線密度 | 熱拡散 | 高密度配線 vs 層間熱流妨害 | 熱ビア配置、レイヤ構成最適化 |
| EMI対策 | 高速信号 | 終端・抑制フィルタ vs シグナルディグレ | 差動伝送、スルーレート制御 |

---

## 📐 トレードオフ設計のフレームワーク｜Design Framework for Trade-offs

1. **Constraint Mapping（制約可視化）**  
   - 各ドメインの制約因子と影響範囲を構造図にマッピング  
   - e.g. 熱源、信号経路、応力集中、GNDループ

2. **Conflict Detection（衝突検出）**  
   - 同一領域に複数制約が交差していないか検証  
   - FEMやEMCシミュレーションによる定量評価

3. **Priority Decision（優先順位決定）**  
   - 信頼性・性能・製造性の観点から優先制約を明示

4. **Design Iteration（反復設計）**  
   - 設計ツールやパラメータ調整によりバランス設計を繰り返す

---

## 🛠 実装支援ツールとトレードオフ評価｜Tools for Trade-off Evaluation

| ツール / Tool | 用途 / Purpose |
|----------------|----------------|
| ANSYS Icepak / Fluent | 熱流解析（Thermal Simulation） |
| ANSYS SIwave / HFSS | SI/PI/EMI電磁界解析 |
| ABAQUS / COMSOL | 応力分布シミュレーション |
| Cadence Sigrity / Allegro | 多領域配線と制約設計 |
| Constraint Map Sheet (CMS) | 手動による制約設計ドキュメント表現（教育向け） |

---

## 🎓 教育的メッセージ｜Educational Message

> 「部分最適は全体不良」  
> 複合制約の中で“ほどほどの最適”を見出す技術が、SystemDK設計力の核心。

> “Local optimization leads to global degradation.”  
> The essence of SystemDK design lies in balancing conflicting constraints, not in optimizing each in isolation.

---

## 🔗 関連節｜Linked Sections

- [`f2a_1_systemdk_overview.md`](f2a_1_systemdk_overview.md)：SystemDK設計の全体像
- [`f2a_2_sipi.md`](f2a_2_sipi.md)：SI/PIトレードオフの詳細
- [`f2a_3_thermal.md`](f2a_3_thermal.md)：熱と信号のバランス設計
- [`f2a_4_mechanical.md`](f2a_4_mechanical.md)：応力設計と熱との衝突
- [`f2a_5_emi_emc.md`](f2a_5_emi_emc.md)：ノイズ制約との整合

---

## 📎 参考資料｜References

- “System Design Methodology for Multi-Domain Constraints,” IEEE Access  
- “Multiphysics Aware Package Design,” SEMI Whitepaper  
- JEITA/JEDEC Design-for-Reliability Guidelines  
- Educational Workshop on System Constraint Co-Design (DCA / Jisso Univ.)

---

**[← 戻る / Back to Special Chapter 2 Top](./README.md)**
