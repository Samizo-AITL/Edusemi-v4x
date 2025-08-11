---
layout: default
title: 3. GAA / AMS / MRAMブロックの仕様と構成定義  
---

---

# 🧱 3. GAA / AMS / MRAMブロックの仕様と構成定義  
**3. Specification and Composition of GAA, AMS, and MRAM Blocks**

---

## 🎯 目的｜Objective

この章では、SystemDKベースPoCで統合される主要ブロック群：

- **GAA Logic**（Gate-All-Aroundトランジスタによる先端SoCロジック）
- **AMS**（Analog-Mixed Signal：アナログIFやセンサモジュール）
- **MRAM**（不揮発性メモリブロック）

の基本構成、I/O、動作条件、周辺とのインタフェースについて定義する。

> This section defines the key specification points of each block  
> to support layout integration and constraint derivation for the PoC.

---

## ⚙️ 各ブロックの基本仕様｜Core Specifications

### 📌 GAA Logic Block

| 項目 | 内容 |
|------|------|
| ノード | 3nm / 5nm相当（FinFETより後のプロセス） |
| 主機能 | データ制御、FSM、クロック制御 |
| 電源 | 0.7–0.9V |
| 周波数 | 最大2GHz想定 |
| インタフェース | AXI, SPI（PoC内ではシンプル構成） |

---

### 📌 AMS Block

| 項目 | 内容 |
|------|------|
| 機能 | ADC, DAC, センサIF, PLL |
| 電源 | アナログ1.2V, デジタル1.0V |
| 感度 | 外来ノイズ/EMIに弱い：**物理隔離設計が必須** |
| 要件 | バイアス安定性、レイアウトシンメトリ、寄生成分対策 |

---

### 📌 MRAM Block

| 項目 | 内容 |
|------|------|
| タイプ | STT-MRAM（Spin-Transfer Torque） |
| 容量 | 数Mbit程度 |
| 電源 | 1.2V書込 / 0.9V読込（2電圧必要） |
| 特徴 | 書込中に高電流・熱が発生（熱応力制約あり） |
| 信頼性 | 書込パルス幅、データ保持特性を要考慮 |

---

## 🔌 インタフェース構成｜Interface Overview

| 接続 | 信号種別 | 備考 |
|------|----------|------|
| GAA ⇄ AMS | SPI / GPIO | 制御用 |
| GAA ⇄ MRAM | バス接続 / SRAM-Like | 読書用アクセス |
| 外部⇄AMS | アナログライン / クロック | EMI対策・アイソレーション領域必要 |
| 全体制御 | FPGA経由 / JTAG | 実評価環境用 |

---

## 📐 ブロック配置とPDN要件｜Placement and Power Profile

- GAAは中心部、AMSは**エッジ or シールド領域**に配置  
- MRAMは**熱拡散パス**を確保できる配置が望ましい  
- AMS用PDNは**独立的なLDO or 電源アイソレータ**が推奨される

---

## 📘 本章のまとめ｜Summary

GAA / AMS / MRAM の仕様定義を明示することで：

- 統合設計時の**制約評価（熱、EMI、応力）**が可能となる  
- **PDN・フロアプラン・ピン配置**の整合性を事前検討できる  
- SystemDKにおける**設計テンプレート化**への基盤が整う

> Proper specification helps unify constraint-driven integration  
> and accelerates SystemDK-based reusability in future projects.
