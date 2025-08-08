---
layout: default
title: 5.2 MagicによるGDS階層と層構成の可視化
---

---

# 🧪 5.2 MagicによるGDS階層と層構成の可視化  
**Visualizing GDS Hierarchy and Layer Composition using Magic**

---

## 🎯 本節の目的｜Objectives

- Magicを用いてGDSファイルを開き、各レイヤーとセル階層を視覚的に確認する  
  **Open GDS files using Magic and visually examine layers and cell hierarchy**
- Sky130の物理レイヤー構成を可視化し、設計対象のGDS構造を直感的に把握する  
  **Understand the physical layer composition of Sky130 through visual exploration**

---

## 🖥️ 使用ツール：Magic｜Tool Used: Magic

MagicはSky130 PDKと統合されたオープンソースのレイアウトエディタです。  
Magic is an open-source layout editor integrated with the Sky130 PDK.

以下のように、GDSファイルをMagicで開くことができます：  
To open a GDS file in Magic, use the following command:

```bash
cd runs/soc_top/results/final/gds/
magic -T sky130A.tech soc_top.gds
```

> 🔧 MagicはSky130の`.tech`ファイルを利用してGDSを解釈・表示します。  
> Magic interprets and displays GDS using the corresponding `.tech` file of Sky130.

---

## 🧭 Magic上での主な操作｜Main Operations in Magic

| 🎮 **操作内容**<br>**Operation** | ⌨️ **コマンド／GUI**<br>**Command / GUI** |
|-----------------------------|--------------------------------------------|
| 層の表示切り替え<br>Toggle Layer View | `Option → Display Styles` または `Layer Selection` |
| セル階層の展開<br>Expand Cell Hierarchy | `F5` キー または `expand` コマンド |
| レイヤー情報の確認<br>Check Layer Info | `what` コマンド or 右クリック |
| GDS層番号の確認<br>GDS Layer Code Lookup | `sky130A.tech` の内容を確認 or 表示欄から確認 |

---

## 🔍 可視化の観察ポイント｜Key Visualization Points

| 🔬 **観察対象**<br>Observation | 📝 **内容**<br>Description |
|------------------------------|-----------------------------|
| `nwell`, `poly`, `li1`, `met1〜met4` | 各層の物理的配置・重なり方 |
| セルインスタンス（例：DFF, INV） | 各モジュールの階層・配置構造 |
| `via1`, `via2` などのビア | 層間接続の位置関係と構造 |
| `licon`, `mcon`, `via` | コンタクトの種類と配置密度 |

---

## 🧩 観察例｜Examples of Observations

- ✅ `poly` と `nimplant` の重なり → **ゲート構造**（MOSトランジスタ）  
- 🔁 `li1` → `met1` → `met2` への接続構造（ビアの連結）  
- 🧠 `soc_top` モジュール内の `FSM` や `PID` のレイアウト領域分離  
- 🔍 DRC違反が起こりやすい箇所の直感的把握

---

## ✅ 本節のまとめ｜Summary

- MagicはSky130PDKと連携し、GDS構造や層構成を**階層的・視覚的に確認可能**  
  **Magic allows for hierarchical and visual inspection of GDS and layers**
- 実際のセル構成や接続構造を目で見ることで、**設計の理解が大きく深まる**  
  **Visualizing physical layout deepens design comprehension**
- 次節では、**DRCルール**とその**論理的根拠**に注目し、ルールチェックを体験します  
  **Next, we will focus on DRC rules and explore their logic and application**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [5.1 PDK構造の理解とSky130レイヤー体系](5_1_pdk_layers.md)  
- ▶️ [5.3 DRCルールとその根拠（例：metal spacing）](5_3_drc_rules.md)  
- 🏠 [特別編 第5章 READMEに戻る](README.md)
