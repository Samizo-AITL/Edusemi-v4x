---
layout: default
title: DRC・LVS・ERC の自動検証
---

---

# 🧪 DRC・LVS・ERC の自動検証  
**🧪 Automated Checks: DRC, LVS, ERC**

---

## 📘 概要｜Overview

物理設計の完成後、レイアウトと回路の整合性を確認するために行われるのが  
**DRC（Design Rule Check）**、**LVS（Layout vs. Schematic）**、**ERC（Electrical Rule Check）**です。

These checks—**DRC (Design Rule Check)**, **LVS (Layout vs. Schematic)**, and **ERC (Electrical Rule Check)**—are conducted  
after completing the physical design to ensure consistency between layout and schematic.

これらは **設計ミスの早期発見と製造性の確保** に不可欠であり、  
OpenLaneなどの自動設計フローにも組み込まれています。

They are essential for **early bug detection and manufacturability**, and are embedded in automated flows like OpenLane.

---

## 🔍 各種チェックの目的と役割｜Purpose and Roles

| 項目｜Check Type | 検査対象｜Scope | 主なエラー例｜Typical Errors |
|----------------|--------------|--------------------------|
| `DRC` | レイアウトルール違反<br>*Layout rule violations* | 配線幅不足、層間距離違反、オーバーラップ<br>*Insufficient width, spacing violations, overlaps* |
| `LVS` | 回路図とレイアウトの論理一致<br>*Logical match between schematic and layout* | ネット名・端子名不整合、マクロのミス接続<br>*Net/Pin mismatch, incorrect macro connections* |
| `ERC` | 電気的制約違反<br>*Electrical constraints violations* | フローティングノード、複数ドライバ、短絡<br>*Floating nodes, multiple drivers, shorts* |

---

## ⚙️ チェックツールと実行例（Sky130の場合）  
## ⚙️ Tools and Execution Examples (Sky130)

### ✔️ Magic による DRC｜DRC via `Magic`

```bash
magic -d XR -rcfile sky130A.magicrc
```

- **GUI上でDRC違反箇所を視覚的に確認可能**  
  *View DRC violations visually via GUI*

- **設計者がルール意図を理解し、自ら修正することが重要**  
  *Manual correction by the designer is recommended*

---

### ✔️ Netgen による LVS｜LVS via `Netgen`

- 回路図とレイアウトの**ネット構成比較**を行う  
  *Compares net connectivity between schematic and layout*

- **Blackboxマクロや階層構造の整合性に注意**  
  *Be cautious of black-box modules and hierarchy*

---

### ✔️ ERC スクリプトによる検証｜ERC Scripts

- `Xschem`, `Magic` 等と連携し、**補助的ERCスクリプトを実行**  
  *Uses ERC helper scripts alongside tools like Xschem and Magic*

- 例：  
  - 未接続ノードの自動検出  
    *Auto-detection of floating nodes*  
  - 電源・GNDのショートチェック  
    *VDD-GND short checks*

---

### ✔️ Makefile による自動化｜Automation via Makefile

- ターゲット例：`make drc`、`make lvs`、`make erc`  
  *Run automated checks via Makefile targets*

- **ログ解析、結果統計、CI連携にも活用可能**  
  *Can be integrated into CI pipelines with parsed logs and summaries*

---

## 🎯 教材的意義｜Educational Significance

- **DRC/LVS/ERCの構造を理解することで、設計と製造の橋渡しが可能になる**  
  *Understanding DRC/LVS/ERC bridges design and manufacturability*

- **ツール操作を自動化することで、設計検証の再現性と効率が向上**  
  *Automation enhances reproducibility and efficiency of verification*

- **OSSツールの利用により、教育環境での構造的学習が促進される**  
  *Open-source tools facilitate structured learning in academic settings*

---

### 🤖 応用編 第7章：自動化と実装検証技術｜Applied Chapter 7: Automation and Implementation Verification  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 Shinichi Samizo / MIT License
