---
layout: default
title: EDAツールチェーン
---

---

# 🧰 EDAツールチェーン：商用・OSSツールとの接続  
**🧰 EDA Toolchain: Integration with Commercial and OSS Tools**

---

## 📘 概要｜Overview

PDKを用いたSoC設計には、**EDAツールとの連携が不可欠**です。  
本資料では、**商用EDAツールとオープンソースEDAツールの役割と分担**、および**PDKとのインタフェース関係**を整理し、設計フロー全体を俯瞰します。

EDA tool integration is essential for SoC design using PDKs.  
This document outlines the roles of **commercial and open-source EDA tools**, and clarifies **PDK interface structures** across the design flow.

---

## 🔧 商用EDAツールの例｜Examples of Commercial EDA Tools

| 🛠️ **ツール名｜Tool** | 🏢 **提供企業｜Vendor** | 📘 **主な用途｜Main Use** |
|------------------------|-------------------------|----------------------------|
| Virtuoso | Cadence | 回路図・レイアウト・アナログ設計<br>Schematic, layout, analog simulation |
| Spectre / HSPICE | Cadence / Synopsys | 回路シミュレーション（SPICE）<br>Circuit simulation |
| ICC2 / Innovus | Synopsys / Cadence | 配置配線、タイミング検証<br>Place-and-route, timing |
| Calibre | Siemens EDA | DRC / LVS / PEX（物理検証）<br>Design rule and layout verification |

- 商用PDKはこれらツールと**セットで提供されることが多く**、**ツール依存性が高い**。  
  *Commercial PDKs are tightly coupled with these tools and often vendor-locked.*

---

## 🧪 オープンソースEDAツールの例｜Open Source EDA Toolchain

| 🧰 **ツール名｜Tool** | 🧩 **主な機能｜Function** | 💡 **備考｜Notes** |
|----------------------|-----------------------------|--------------------|
| Magic | レイアウトエディタ<br>Layout editor | Sky130対応、標準的 |
| Xschem | 回路図エディタ<br>Schematic editor | Verilog/SPICE混載対応 |
| ngspice | 回路シミュレータ<br>SPICE simulator | Sky130モデルと連携可 |
| KLayout | GDSビューア、DRC<br>GDS viewer, DRC engine | Pythonスクリプト拡張可 |
| OpenROAD | 配置配線、STA、DRC連携<br>Place & Route tool | OpenLane構成に統合 |

- Sky130のような**OSS PDKとの親和性が高く、教育・研究に向く**。  
  *Well suited for open education and research applications.*

---

## 🔁 ツール間のPDK接続構成（例：Sky130）  
## 🔁 PDK Toolchain Flow Example (Sky130)

```
回路図 (Xschem)
↓
シミュレーション (ngspice) ← スパイスモデル
↓
レイアウト (Magic)
↓
DRC / LVS / PEX (Magic, Netgen)
↓
配置配線 (OpenROAD)
↓
最終検証 (KLayout, custom scripts)
```

- `sky130A` PDK には、**各ツール専用の設定フォルダが整備**されており、ツール間の接続が容易。  
- 各ツールは共通PDK内の**モデルファイルや検証ルール**を参照して設計を進める。

---

## 🏫 教材的意義｜Educational Significance

- 商用EDAは**高機能だがブラックボックス化**しやすいため、基礎教育では**OSSツールの活用が推奨される**  
  *Commercial tools are powerful but opaque; OSS is better for learning.*
- 設計フローの構造を理解することで、**PDKとの相互依存関係を明確に把握可能**  
  *Understanding the flow clarifies PDK dependencies and verification scope.*
- Sky130やOpenLaneは、**PDK＋OSSツールの統合教育環境**として最適な実例  
  *Sky130 + OpenLane is a best-practice educational platform.*

---

## 🔗 関連資料｜Related Materials

- [`pdk_structure.md`](./pdk_structure.md)：PDKの構成とモデルの詳細  
  *Details of PDK structure and device models*
- [`rule_check_flow.md`](./rule_check_flow.md)：DRC/LVS等の検証フローへ  
  *Physical verification flow (DRC/LVS/PEX)*

---

### 🛠️ 応用編 第6章：PDKとEDA環境｜PDK and EDA Environment  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 **Shinichi Samizo** / MIT License
