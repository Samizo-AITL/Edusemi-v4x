---
layout: default
title: 5.1 PDK構造の理解とSky130レイヤー体系
---

---

# 🧱 5.1 PDK構造の理解とSky130レイヤー体系  
**Understanding the PDK Structure and Layer System of Sky130**

---

## 🎯 本節の目的｜Objectives

- Sky130 PDKにおける設計層（layer）の分類と役割を理解する  
  **Understand the classification and roles of layers in the Sky130 PDK**
- レイアウトとマスクの対応関係を把握し、物理設計の基本的な階層構造を学ぶ  
  **Learn the basic hierarchical structure of physical layout and masks**
- DRC/LVSなど後工程で必要となる層理解の基盤を築く  
  **Build a foundation for understanding layers essential for DRC/LVS**

---

## 🧱 Sky130 レイヤー一覧｜Layer List in Sky130

| 🏷️ **レイヤー名**<br>**Layer Name** | 🛠️ **用途**<br>**Purpose** | 🔢 **GDS番号**<br>**GDS [layer/datatype]** | 📝 **備考**<br>**Notes** |
|----------------------------------|-----------------------------|---------------------------------------------|---------------------------|
| `nwell`                          | N型ウェル形成<br>N-well    | `64/20`                                     | N-MOSの基板形成など       |
| `pwell`                          | P型ウェル形成<br>P-well    | `64/44`                                     | P-MOS用途                 |
| `poly`                           | ゲート電極<br>Gate Electrode | `66/20`                                   | ゲート形成・寸法制限あり   |
| `li1`                            | ローカル配線<br>Local Interconnect | `67/20`                           | Polyや接点との接続に使用   |
| `met1`                           | メタル1配線<br>Metal1      | `68/20`                                     | 配線密度が高い             |
| `met2`〜`met5`                   | 上位配線層<br>Upper Metals | `69/20`〜`72/20`                             | ワイドな配線               |
| `via1`〜`via4`                   | ビア<br>Vias               | `70/44`〜`73/44`                             | 金属層間の接続              |
| `nimplant`                       | Nドーピング<br>N-Implant   | `65/20`                                     | Vth調整等に使用            |
| `pimplant`                       | Pドーピング<br>P-Implant   | `65/44`                                     | 同上（P型）                |
| `dnwell`                         | Deep N-Well                | `64/18`                                     | 高耐圧デバイス用           |

> 📌 **GDS番号**は `[layer_number/datatype]` 形式で、MagicやKLayoutで必要となります。  
> **GDS codes follow the `[layer/datatype]` format**, important in Magic/KLayout.

---

## 📁 PDKディレクトリ構成（例）｜Example PDK Directory Structure

```plaintext
sky130A/
├── libs.tech/
│   ├── magic/             ← Magic用レイヤー定義 (Layer definitions for Magic)
│   ├── klayout/tech/      ← KLayout用 (For KLayout)
│   ├── openlane/          ← OpenLane設定 (OpenLane configuration)
│   └── netgen/            ← LVSルール定義 (LVS rules)
└── libs.ref/
    └── sky130_fd_pr/      ← 標準セル・ライブラリ本体 (Standard cell libraries)
```

---

## 🧩 レイヤー階層の理解｜Layer Hierarchy Overview

| 📚 **カテゴリ**<br>**Category** | 🔍 **代表レイヤー**<br>**Representative Layers** | 📘 **説明**<br>**Description** |
|-------------------------------|-----------------------------------------------|-------------------------------|
| **デバイス層**<br>Device Layer | `nwell`, `pwell`, `poly`, `implant`          | トランジスタ形成に関与        |
| **配線層**<br>Routing Layer   | `li1`, `met1`〜`met5`, `via1`〜`via4`        | 接続・ルーティングに使用      |
| **注釈層**<br>Annotation      | `np`, `pp`, `boundary`, `text` など           | シミュレーションや図面補助用 |

---

## 📎 用語解説｜Term Explanation

| 🏷️ **用語**<br>**Term** | 💡 **意味**<br>**Meaning** |
|------------------------|-----------------------------|
| **コンタクト（Contact）** | `li1`〜`met1`を接続する構造<br>Connection between `li1` and `met1` |
| **ビア（Via）**           | 上位メタル間の接続（例：`met2` → `met3`）<br>Connection between metal layers |
| **ピッチ（Pitch）**       | 配線間の最小間隔<br>Minimum wire spacing per layer |

---

## ✅ 本節のまとめ｜Summary

- Sky130 PDKは**階層的なレイヤー構造**を持ち、各層の役割を理解することで物理設計の土台が形成される  
  **Understanding the layer hierarchy is fundamental to physical design with Sky130**
- **GDS番号とレイヤー名の対応関係**は、KLayoutやMagicでの解析やDRC設定に不可欠  
  **Mapping between GDS codes and names is essential for layout tools**
- 次節では、実際に**Magicを使ってGDS構造を可視化**し、これらのレイヤーがどう現れるかを確認する  
  **In the next section, we'll visualize actual GDS structures using Magic**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [特別編 第5章 READMEに戻る](README.md)  
- ▶️ [5.2 MagicによるGDS階層と層構成の可視化](5_2_magic_gds.md)
