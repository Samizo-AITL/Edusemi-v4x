---
layout: default
title: Lintと形式検証（Static Verification）
---

---

# 🧪 Lintと形式検証（Static Verification）  
**🧪 Lint and Formal (Static) Verification**

---

## 📘 概要｜Overview

本節では、RTL設計段階において論理的な誤りや不整合を検出するための  
**Lint（構文・論理チェック）** および **形式検証（Formal Verification）** の基本を解説します。  
特にSoC設計では、**実装前の静的検証がバグの早期発見と設計品質の確保に不可欠**です。

This section introduces the basics of **Lint (syntactic/logical checks)** and **Formal Verification**  
to detect logic errors and inconsistencies at the RTL design stage.  
Especially in SoC development, **static verification is essential for early bug detection and design quality assurance**.

---

## 🔍 Lintとは？｜What is Lint?

Lintは、HDL記述に潜む**構文エラーや論理的な非推奨記述**を検出する静的解析手法です。  
Lint is a static analysis method to detect **syntactic errors and bad coding practices** in HDL descriptions.

### ✔️ チェック内容例｜Examples of Checks

- 未接続ポート／未使用信号  
  *Unconnected ports / unused signals*
- 同名変数のスコープ衝突  
  *Variable name scope collisions*
- 推奨されない記述（非同期リセット、複雑な if-case）  
  *Discouraged descriptions (e.g., asynchronous resets, complex if-cases)*
- 信号幅のミスマッチ  
  *Bit-width mismatches*
- `case` 文の漏れ、`default` の欠如  
  *Missing `case` branches or lacking `default`*

### ✔️ 主なツール｜Popular Tools

| ツール名｜Tool | 種類｜Type | 備考｜Remarks |
|--------------|------------|---------------------------|
| `Verilator` | OSS | Verilog専用。C++変換によるシミュレーションも可能<br>*Verilog only; also supports C++ simulation* |
| `SpyGlass` | 商用｜Commercial | LintやCDC解析の業界標準<br>*Industry standard for Lint and CDC* |
| `Ascent Lint` | 商用｜Commercial | スタイルガイド準拠、高速処理<br>*Fast analysis with style guide compliance* |

---

## 📐 形式検証とは？｜What is Formal Verification?

形式検証は、設計仕様とRTLが**常に論理的に一致しているかを証明する手法**です。  
Formal verification is a method to **mathematically prove that RTL behavior matches the intended specification**.

### ✔️ 検証技術｜Verification Techniques

- **等価性検証（Equivalence Check）**：  
  *Verify logical equivalence between RTL and gate netlist*

- **プロパティ検証（Property Checking）**：  
  *Verify if system behaviors always satisfy specified properties (e.g., SystemVerilog Assertions)*

### ✔️ 特徴｜Characteristics

- **ベクトル非依存**：すべての状態を網羅  
  *Vector-independent: explores all possible states*
- **高カバレッジ**：バグの早期発見に有効  
  *High coverage: effective for early bug detection*
- **状態空間爆発のリスク**：収束しない場合もあり  
  *Risk of state explosion: may not converge*

---

## 🧰 CDC解析｜Clock Domain Crossing (CDC) Analysis

複数のクロックドメインを持つ設計において、**非同期動作による不整合**を静的に検出します。  
CDC analysis statically detects **inconsistencies caused by asynchronous clock domains**.

### ✔️ チェック内容｜Check Items

- 非同期間の信号伝播の問題  
  *Signal transition issues across asynchronous domains*
- 同期化FF（2段など）の不足  
  *Missing synchronizer flip-flops*
- リセットや enable 信号の配線ミス  
  *Issues with global reset or enable signal distribution*

### ✔️ 主なツール｜Popular Tools

| ツール名｜Tool | 種類｜Type | 備考｜Remarks |
|--------------|------------|-----------------------------|
| `SpyGlass CDC` | 商用 | CDC特化の静的検証ツール<br>*Specialized CDC static checker* |
| `Conformal CDC` | 商用 | 機能ブロック単位の詳細解析<br>*Detailed block-level analysis* |
| `OpenTimer` | OSS | 一部CDC解析に対応<br>*Partial CDC checking support* |

---

## 🎯 教材的意義｜Educational Significance

- **Lint** は構文とスタイルの理解を助け、**記述品質を向上**させる  
  *Lint improves coding style and HDL syntax awareness.*

- **形式検証** は仕様を**論理的に理解・証明する能力を育成**する  
  *Formal verification trains the ability to validate logic against intent.*

- **CDC解析** により、非同期設計に必要な**信頼性の視点が身に付く**  
  *CDC checks provide insights into reliability for asynchronous designs.*

---

## 🔗 関連章｜Related Chapters

- [`chapter5_soc_design_flow`](../chapter5_soc_design_flow/README.md)：RTL記述と論理合成フロー  
  *RTL and synthesis process overview*

- [`openlane_validation.md`](./openlane_validation.md)：配置配線後の検証との連携  
  *Verification after physical design via OpenLane*

---

### 🤖 応用編 第7章：自動化と実装検証技術｜Applied Chapter 7: Automation and Implementation Verification  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 Shinichi Samizo / MIT License
