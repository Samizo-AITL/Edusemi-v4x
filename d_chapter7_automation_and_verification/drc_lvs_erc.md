# 🧪 DRC・LVS・ERC の自動検証

---

## 📘 概要

物理設計の完成後、レイアウトと回路の整合性を確認するために行われるのが  
`DRC（Design Rule Check）`、`LVS（Layout vs. Schematic）`、`ERC（Electrical Rule Check）`です。

これらは**設計ミスの早期発見と製造性の確保**に不可欠であり、  
OpenLaneなどのツールでも自動化フローとして組み込まれています。

---

## 🔍 各種チェックの目的と役割

| 項目 | 検査対象 | 主なエラー例 |
|------|----------|--------------|
| `DRC` | レイアウトの寸法・ルール違反 | 配線幅不足、層間距離違反、オーバーラップ |
| `LVS` | 回路図とレイアウトの論理的一致 | インスタンスの不一致、端子名の不整合 |
| `ERC` | 電気的制約違反 | 未接続ノード、複数ドライバ、メタ安定懸念 |

---

## ⚙️ チェックツールと実行例（Sky130の場合）

### ✔️ `Magic` を用いた DRC

```bash
magic -d XR -rcfile sky130A.magicrc
```

- `DRC違反箇所をGUIで表示`
- `自動修正ではなく、設計者が意図を理解して修正` する

---

### ✔️ `Netgen` による LVS

- `回路図とレイアウトのネット構成を比較`
- `blackboxモジュールやマクロ使用時は注意`

---

### ✔️ `ERC` スクリプト実行

- `Xschem` や `Magic` と連携した `ERC補助スクリプト` を使用可能
- 例：`未接続ノードの自動検出`、`VDD-GND間の短絡確認` など

---

### 🧰 自動化スクリプト（Makefile）の活用

- `make drc`、`make lvs` などのターゲットで `自動実行可能`
- `ログをパースしてエラー箇所の統計を取得` したり、`トレーサビリティ構築` に活用できる
