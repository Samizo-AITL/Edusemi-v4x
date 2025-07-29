# 🧪 Lintと形式検証（Static Verification）

---

## 📘 概要

本節では、RTL設計段階において論理的な誤りや不整合を検出するための  
`Lint（構文・論理チェック）` および `形式検証（Formal Verification）` の基本を解説します。

特にSoC設計では、実装前の静的検証がバグの早期発見と設計品質の確保に不可欠です。

---

## 🔍 Lintとは？

`Lint` は、HDL記述に潜む**構文エラーや論理的な非推奨記述**を検出する静的解析手法です。

### ✔️ チェック内容例

- 未接続ポート／未使用信号
- 同名変数のスコープ衝突
- 推奨されない記述（非同期リセットや複雑な if-case）
- 信号幅のミスマッチ
- `case` 文の漏れ、`default` の欠如

### ✔️ 主なツール

| ツール名 | 種類 | 備考 |
|----------|------|------|
| `Verilator` | OSS | Verilog専用。C++変換によるシミュレーション兼用 |
| `SpyGlass` | 商用 | 業界標準のLintとCDC解析機能 |
| `Ascent Lint` | 商用 | 高速解析、スタイルガイド対応 |

---

## 📐 形式検証とは？

`Formal Verification` は、設計仕様とRTL記述が**常に論理的に一致しているかを証明**する手法です。

### ✔️ 検証技術

- **等価性検証（Equivalence Check）**：論理合成前後の RTL ⇔ Gate netlist の等価性確認
- **プロパティ検証（Property Checking）**：期待動作を記述してそれが常に成立するか検証（SystemVerilog Assertions）

### ✔️ 特徴

- **ベクトル非依存**：すべての状態空間を網羅的に検証  
- **抽象度が高い**：検証のカバレッジが高く、バグの早期発見に有効  
- **収束条件に注意**：状態空間が大きいと検証完了しないこともある

---

## 🧰 CDC（Clock Domain Crossing）の静的チェック

複数クロックドメインを持つ設計において、**不整合やメタ安定状態のリスク**を検出するための静的検証。

### ✔️ チェック内容

- 非同期クロック間での信号遷移タイミングの不整合
- 同期化FF（2段FFなど）の挿入不足
- グローバルリセットや enable 信号の伝播確認

### ✔️ 主なツール

- `SpyGlass CDC`、`Conformal CDC` など（商用）
- `OpenTimer` など一部 OSS も支援

---

## 🎯 教材的意義

- `Lint` は、**構文理解と設計スタイルの習熟**に最適  
- `形式検証` は、**動作仕様を論理的に理解・証明する力**を養う  
- `CDC解析` は、**非同期設計における信頼性設計の視点**を与える

---

## 🔗 関連章

- [`chapter5_soc_design_flow`](../chapter5_soc_design_flow/README.md)：RTL記述と論理合成フロー  
- [`openlane_validation.md`](./openlane_validation.md)：配置配線後の検証との連携

---

### 🤖 応用編 第7章：自動化と実装検証技術｜Automation and Implementation Verification  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 Shinichi Samizo / MIT License
