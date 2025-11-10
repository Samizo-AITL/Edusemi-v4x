---
layout: default
title: OpenLane導入とフローの全体像（最新版）
---

---

# 🚀 OpenLane導入とフローの全体像  
**Introduction and Full Flow of OpenLane-Based Digital Design**

---

## 📘 概要｜Overview
本節では、オープンソースEDAフロー **OpenLane v2** を利用した、  
**RTL（Verilog）→ GDS（物理レイアウト）** までの ASIC 実装プロセス全体を解説します。

This section explains how to set up **OpenLane** and provides a clear overview  
of the **digital design flow from RTL to GDS**, using open-source tools and the **Sky130A PDK**.

---

## 📦 OpenLaneとは｜What is OpenLane?
OpenLane は、The-OpenROAD Project が開発する  
**自動デジタルLSI実装フロー（RTL→GDS 自動化）**です。

| Component | Description |
|-----------|-------------|
| 🧠 **OpenROAD** | Floorplan / Placement / CTS / Routing / STA |
| ⚙️ **Yosys** | RTL → Gate-Level 論理合成 |
| 📐 **Magic** | DRC（物理ルールチェック） |
| 🔎 **Netgen** | LVS（回路一致チェック） |
| 📦 **Docker** | OpenLane v2 の実行環境 |
| 🧱 **volare** | Sky130 PDK の取得・切替 |

---

## 🔧 導入手順｜Installation Steps（最新版）
最新 OpenLane v2 では **Docker + volare** 方式が標準です。

### ✅ 1. Sky130 PDK の取得（volare）
```
pip install --upgrade pip volare
volare enable sky130A
```

### ✅ 2. OpenLane v2（Dockerイメージ）
```
docker pull efabless/openlane:2024.09.11
```

### ✅ 3. OpenLane コンテナの起動
```
docker run --rm -it \
  -v $HOME/openlane/designs:/openlane/designs \
  -v $HOME/openlane/pdks:/pdks \
  -e PDK_ROOT=/pdks \
  -e PDK=sky130A \
  efabless/openlane:2024.09.11
```

---

## 🗂️ ディレクトリ構成｜Directory Structure
```
openlane/
├── designs/
│    └── inverter/
│        ├── config.tcl
│        └── src/inverter.v
└── pdks/
     └── sky130A/
```

---

## 📈 設計フロー全体像｜Full Flow Overview
| Step | Description | Tool |
|------|-------------|------|
| 1️⃣ **Synthesis** | RTL → Gate-Level Netlist | `Yosys` |
| 2️⃣ **Floorplan** | コア領域・ピン配置 | `OpenROAD` |
| 3️⃣ **Placement** | セル配置 | `OpenROAD` |
| 4️⃣ **CTS** | クロックツリー合成 | `OpenROAD` |
| 5️⃣ **Routing** | 自動配線 | `OpenROAD` |
| 6️⃣ **Signoff (DRC/LVS)** | Magic DRC / Netgen LVS | `Magic`, `Netgen` |
| 7️⃣ **GDS Output** | 製造用 GDSII | `Magic`, `KLayout` |

---

## ✅ 教育的意義｜Why It Matters for Education
- OSSで **商用EDA同等のフロー** が学べる  
- RTL〜GDS まで **バックエンド実装全体**を理解可能  
- Sky130A PDK は教育・研究用途で広く採用  
- 実際に **GDSが生成できる実践教材**になる  

---

## 📎 関連教材リンク
- [📘 02_rtl_to_gds_flow – 実設計フロー実習](../02_rtl_to_gds_flow/README.md)  
- [🏠 第3章トップへ戻る](../README.md)  
- [🏗️ OpenLane公式GitHub](https://github.com/The-OpenROAD-Project/OpenLane)

---

## 📝 備考
- 本教材では **inverter / gcd / picorv32** などを順に扱う  
- Docker＋volare は環境差異ゼロで再現性が高い  
- 次章で **config.tcl の詳細設定**を扱う
