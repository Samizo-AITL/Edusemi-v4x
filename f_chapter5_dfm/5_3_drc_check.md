# 5.3 DRCルールとその根拠（例：metal spacing）

## 🎯 本節の目的

- Magicを用いた DRC（Design Rule Check）の実施方法を学ぶ  
- Sky130 PDKにおける代表的なDRCルール（例：metal spacing）を理解する  
- DRC違反の例とその根拠、対策を実践的に把握する

---

## 🧪 DRCとは？

DRCは、レイアウトが製造可能な物理ルールに従っているかを検証するステップです。  
Sky130 PDKでは、多数の設計ルールが `magic` 向けに記述されています。

---

## 🔍 MagicによるDRC実行手順

### 【1】GDSファイルの読み込み

```bash
magic -T sky130A.tech soc_top.gds
```

### 【2】DRCチェックの実行

```magic
drc euclidean on
drc check
```

### 【3】違反箇所の表示

```magic
drc find
```

違反箇所がGUI上にハイライト表示され、メッセージにルール違反内容が表示されます。

---

## 📏 代表的なDRCルール（例：metal spacing）

| ルール名 | 内容 | 備考 |
|----------|------|------|
| `metal1 spacing > 0.14um` | メタル1間の最小間隔 | 密度が高いと違反しやすい |
| `poly enclosure of contact` | ポリがコンタクトを十分に覆うこと | トランジスタ形成に関与 |
| `li1 width >= 0.17um` | li1配線の最小幅 | 製造歩留まりに影響 |
| `via enclosure` | viaが十分に金属で囲まれている | 信頼性・接続安定性に関与 |

---

## 🧩 DRC違反の原因と対策

| 原因 | 対策 |
|------|------|
| floorplan密度が高すぎる | `FP_CORE_UTIL`や`PL_TARGET_DENSITY`を調整 |
| 自動配置でvia配置が過密 | 手動floorplanやルーティング指示の挿入 |
| 設計規模に対しセルライブラリが不足 | 標準セル選定の見直し or 複数セルライブラリ使用 |

---

## ✅ 本節まとめ

- DRCは物理的な製造可能性を保証するための基本チェック  
- Magicで簡易DRC実行可能だが、OpenLane後工程でも必ず確認する  
- ルールの背景を理解しながら設計することで、DFM適合率が向上する

---

👉 [5.4 LVSの仕組みと等価性判定の論理](5_4_lvs_check.md)
