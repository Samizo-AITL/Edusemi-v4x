# 🧪 SystemDK PoC教材：GAA・AMS・MRAM 統合設計  
**Proof of Concept: Heterogeneous Integration with GAA / AMS / MRAM**

---

## 📘 概要｜Overview

このPoC教材では、GAA (Gate-All-Around), AMS (Analog/Mixed Signal), MRAM (Magnetoresistive RAM) の異種ノードを、  
**SystemDKを用いて統合設計する教育用ケーススタディ**を提示します。

This case study demonstrates an educational PoC of heterogeneous integration combining GAA, AMS, and MRAM nodes,  
designed and analyzed using SystemDK to manage multi-physical constraints.

---

## 🧩 構成例｜Example Integration Overview

| ブロック | ノード技術 | 主な役割 |
|----------|------------|----------|
| GAA CPU | 2nm | 高性能・低電力演算 |
| AMS IF | 22nm BCD | センサ・アナログ制御 |
| MRAM | 28nm | 不揮発性キャッシュ・状態保持 |

---

## 🔧 対応する物理制約とSystemDKの統合管理

### 1. SI/PI（Signal/Power Integrity）  
- 高速クロスチップ通信（GAA ↔ MRAM）に対する反射・アイ開口検証  
- PDNインピーダンス解析（Sパラ／インピーダンスアナライザ併用）

### 2. Thermal（熱設計）  
- GAA CPUとMRAMの熱耐性差に基づくレイアウト戦略  
- SystemDKにより熱分布・冷却制約を連携最適化

### 3. Mechanical Stress（応力）  
- CTE差の大きい異種材料（MRAM/AMS）間の界面設計  
- 樹脂充填やRDLのFEM応力解析との連携

### 4. EMI/EMC  
- AMS/RFモジュール周辺の遮蔽・フィルタ設計  
- SystemDKによるグラウンディング・EMノイズ評価

---

## 🧪 PoCモデル構成例

- **TSV搭載 2.5Dインターポーザ構造**  
- **Fan-Out Wafer-Level Packaging（FOWLP）** 対応も比較候補  
- **SystemDK ⇔ PKGDK ⇔ IPDK** 連携による階層PoC設計管理

---

## 📊 評価手法例（→ 詳細：[`../f2a_9_evaluation_methods.md`](../f2a_9_evaluation_methods.md)）

| 項目 | 評価手法 | 備考 |
|------|----------|------|
| SI/PI | Sパラメータ、IBISモデル、PDNシミュレーション | Keysight ADSなど |
| 熱 | FEM熱解析（熱拡散・Junction温度） | ANSYS Icepakなど |
| 応力 | FEM応力解析、界面信頼性モデル | COMSOL / JMAGなど |
| EMI/EMC | Near/Far Field EMI解析、遮蔽シミュレーション | CST Studio Suite等 |

---

## 🎯 教育的意義

- **最先端ノードの適材適所設計力**を養成  
- **物理制約を横断した設計思考**を学習  
- PDK → IPDK → PKGDK → **SystemDK** の設計連携を体験  
- **SoC統合設計におけるリアルな意思決定構造**を学ぶ教材

---

## 🔗 関連教材

- [SystemDK概要（f2a_1）](../f2a_1_systemdk_overview.md)  
- [物理制約管理（f2a_2〜f2a_6）](../README.md)  
- [SystemDK評価法（f2a_9）](../f2a_9_evaluation_methods.md)

---

## 👤 著者・ライセンス

| 項目 | 内容 |
|------|------|
| 著者 | 三溝 真一（Shinichi Samizo） |
| Email | shin3t72@gmail.com |
| GitHub | https://github.com/Samizo-AITL |
| ライセンス | MIT License（再配布・改変自由） |

---
