---
layout: default
title: 5.3 DRCルールとその根拠（例：metal spacing）
---

---

# 🧪 5.3 DRCルールとその根拠（例：metal spacing）  
**Understanding DRC Rules and Their Basis (e.g., Metal Spacing)**

---

## 🎯 本節の目的｜Objectives

- Magicを用いた **DRC（Design Rule Check）** の実施方法を学ぶ  
  **Learn how to perform DRC checks using Magic**
- Sky130 PDKにおける代表的なDRCルール（例：metal spacing）を理解する  
  **Understand common Sky130 DRC rules like metal spacing**
- DRC違反の例・根拠・対策を実践的に把握する  
  **Explore DRC violations, their reasoning, and practical fixes**

---

## 🧪 DRCとは？｜What is DRC?

**DRC（Design Rule Check）** とは、レイアウトが製造上の物理ルールを守っているかを検証するステップです。  
Design Rule Check (DRC) ensures that a layout complies with physical manufacturing constraints.

Sky130 PDKでは、Magicに対応した詳細なDRCルールが提供されています。  
Sky130 PDK provides detailed DRC rules compatible with Magic.

---

## 🧭 MagicによるDRC実行手順｜Running DRC in Magic

### 【1】📂 GDSファイルの読み込み｜Load GDS

```bash
magic -T sky130A.tech soc_top.gds
```

### 【2】🔍 DRCチェックの実行｜Perform DRC

```tcl
drc euclidean on
drc check
```

### 【3】⚠️ 違反箇所の表示｜Display Violations

```tcl
drc find
```

🔎 違反箇所がGUIにハイライト表示され、ターミナルにもルール違反の内容が出力されます。  
Violations will be highlighted in the GUI and reported in the terminal.

---

## 📏 代表的なDRCルール｜Typical DRC Rules (Sky130)

| 📘 **ルール名**<br>Rule Name | 📝 **内容**<br>Description | 🔧 **備考**<br>Notes |
|---------------------------|----------------------------|-----------------------|
| `metal1 spacing > 0.14um` | メタル1の最小間隔<br>Minimum spacing for Metal1 | 高密度配置で違反しやすい<br>Often violated in dense layouts |
| `poly enclosure of contact` | ポリがコンタクトを十分に覆うこと<br>Poly must enclose contact | ゲート形成に関係<br>Important for transistor gates |
| `li1 width >= 0.17um` | li1層の最小配線幅<br>Minimum width for li1 | 微細配線で要注意<br>Critical for yield |
| `via enclosure` | viaが金属に十分囲まれているか<br>Via must be enclosed by metal | 信頼性に影響<br>Key to connection reliability |

---

## 🧩 DRC違反の原因と対策｜Causes and Countermeasures

| ❌ **原因**<br>Cause | ✅ **対策**<br>Solution |
|-------------------|-------------------------|
| Core密度が高すぎる<br>High core utilization | `FP_CORE_UTIL` や `PL_TARGET_DENSITY` を調整 |
| via配置が過密<br>Congested via placement | floorplanの見直しやルーティング改善 |
| セルが不足・サイズ不均衡<br>Library mismatch | セルライブラリの変更や組み合わせ調整 |

---

## ✅ 本節まとめ｜Summary

- DRCは、設計が製造可能な状態かどうかを確認する**基本チェック手法**です  
  **DRC is essential to ensure manufacturability of the layout**
- Magicを使えば手軽にGUIとコマンドでチェックが可能  
  **Magic allows easy checking through GUI and scripting**
- 各ルールの**意味を理解することが、良い物理設計への第一歩**です  
  **Understanding the rationale behind rules is key to DFM**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [5.2 MagicによるGDS階層と層構成の可視化](5_2_magic_gds.md)  
- ▶️ [5.4 LVSの仕組みと等価性判定の論理](5_4_lvs_check.md)  
- 🏠 [特別編 第5章 READMEに戻る](README.md)
