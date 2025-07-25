# 5.4 LVSの仕組みと等価性判定の論理

## 🎯 本節の目的

- LVS（Layout vs Schematic）の目的と実行方法を理解する  
- Sky130での LVS 検証ツール（Netgen）と手順を学ぶ  
- ネットリストとレイアウトの等価性を保証するための設計方法を把握する

---

## 🧪 LVSとは？

LVS（Layout vs. Schematic）は、**レイアウトで作成された物理構造**と、  
**回路図（またはVerilog）で定義された論理構造**が等価かどうかを確認する工程です。

---

## 🔧 使用ツール：Netgen

Sky130 PDKには `netgen` 用のLVSルールファイルが含まれています。

---

## 🔍 LVS実行の基本手順（Netgen）

### 【1】実行例：FSMモジュールのLVS

```bash
netgen -batch lvs   "fsm_engine.spice fsm_engine"   "fsm_engine.scs fsm_engine"   setup.tcl   | tee lvs_report.log
```

- `.spice`：レイアウト抽出SPICE（Magicで生成）
- `.scs`：参照回路（通常は合成後のVerilog→SPICE変換）
- `setup.tcl`：Sky130 PDKに付属のLVSルール

---

## 🧱 LVSチェック項目の例

| チェック項目 | 内容 |
|--------------|------|
| ノード数一致 | レイアウトとスキマティックのノード数が等しいか |
| 接続一致     | 各ノードのピンとネットの接続関係が一致するか |
| デバイス一致 | トランジスタやセルの種類・数が一致しているか |

---

## 🧩 LVS不一致の主な原因

| 原因 | 対策 |
|------|------|
| ネット名不整合 | Verilogと抽出結果でネット命名を揃える |
| DRC違反による抽出失敗 | DRCクリア後に再抽出 |
| I/Oピンやセルの未マッチ | ステートメント順やポート定義の見直し |

---

## ✅ 本節まとめ

- LVSは物理構造と論理回路の一致性を保証する要所  
- Netgenを使えば自動照合が可能だが、名前の整合・ルール準拠が前提  
- DRCとLVSの両立が物理検証の成功を左右する

---

👉 [5.5 DFM設計：量産対応のためのレイアウト指針](5_5_dfm_guideline.md)
