---
layout: default
title: OpenLane導入とフローの全体像
---

# 🚀 OpenLane導入とフローの全体像  
**Introduction and Full Flow of OpenLane-Based Digital Design**

---

## 📘 概要｜Overview

本節では、オープンソースEDAフロー「**OpenLane**」の導入方法と、  
**RTL（Verilog）からGDS（物理レイアウト）までの全体ステップ**を解説します。

This section explains how to set up **OpenLane** and provides an overview of  
the **digital design flow from RTL to GDS**, using open-source EDA tools.

---

## 📦 OpenLaneとは｜What is OpenLane?

OpenLaneは、The-OpenROAD Projectが開発する **自動デジタルLSI設計フロー**です。  
**Sky130 PDK**と組み合わせることで、Verilog RTLからGDSファイルの生成まで一貫して実行できます。

| 項目｜Component | 説明｜Description |
|----------------|------------------|
| 🧠 ベースツール | OpenROAD（配置・配線・解析） |
| ⚙️ 論理合成 | `yosys` |
| 📐 物理検証 | `Magic`, `Netgen` |
| 📦 実行環境 | Dockerベース or ローカル環境（Python + Make） |

---

## 🔧 導入手順｜Installation Steps

### 1. リポジトリのクローン

```bash
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
```

### 2. OpenLane本体とSky130 PDKを取得

```bash
make pull-openlane
make pull-sky130-pdk
```

> ⚠️ 初回ダウンロードには 1 時間以上かかる場合があります。

---

## 🗂️ ディレクトリ構成（抜粋）｜Directory Structure

```text
OpenLane/
├── flow/                   # 実行スクリプト類（Makefile, Python）
├── designs/                # ユーザーデザイン（例: picorv32, gcd）
├── PDK_ROOT/               # Sky130 PDK保存ディレクトリ（自動生成）
└── config.tcl              # グローバル設定ファイル
```

---

## 📈 設計フロー全体像｜Full Flow Overview

OpenLaneは以下のフローを一括実行する構成になっています：

| ステップ | 説明｜Description | 使用ツール｜Tool |
|---------|------------------|------------------|
| 1️⃣ Synthesis | RTLをゲートレベルに論理合成 | `yosys` |
| 2️⃣ Floorplan | コア領域やピン位置を定義 | `init_floorplan` |
| 3️⃣ Placement | 論理セルの初期・詳細配置 | `OpenROAD` |
| 4️⃣ CTS | クロックツリーの合成 | `OpenROAD` |
| 5️⃣ Routing | 自動配線処理 | `OpenROAD` |
| 6️⃣ DRC/LVS | 物理検証（設計ルール・接続） | `Magic`, `Netgen` |
| 7️⃣ GDS Output | レイアウトGDSの出力 | `KLayout`, `Magic` |

---

## ✅ 教育的意義｜Why It Matters for Education

- 🔓 **商用EDAと同等の設計フロー**を無償で体験できる  
- 🔍 **PDK連携や制約記述（floorplan, SDC）**を実装を通じて学べる  
- 📊 実設計に近い **ログ・レポート・GDS出力**を生成でき、分析に活用可能  

---

## 📎 関連教材リンク｜Related Chapter Links

- [📘 02_rtl_to_gds_flow - 実設計フロー実習](../02_rtl_to_gds_flow/README.md)  
- [🏠 第3章トップへ戻る](../README.md)  
- [🏗️ OpenLane公式GitHub](https://github.com/The-OpenROAD-Project/OpenLane)  

---

## 📝 備考｜Notes

- 本教材では `gcd` や `inverter` など最小設計から学習を開始します  
- 実務では SoCや複雑なIPマクロへ応用が可能です  
- 今後の章で各フローの実行手順・設定ファイルの編集方法も学習します

---
