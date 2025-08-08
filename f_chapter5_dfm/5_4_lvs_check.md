---
layout: default
title: 5.4 LVSの仕組みと等価性判定の論理
---

---

# 🧪 5.4 LVSの仕組みと等価性判定の論理  
**Understanding LVS and Logical Equivalence Checking**

---

## 🎯 本節の目的｜Objectives

- **LVS（Layout vs. Schematic）の意義と目的**を理解する  
  **Understand the purpose and role of LVS checks**
- **Netgenを用いたSky130環境でのLVS実行方法**を学ぶ  
  **Learn how to run LVS using Netgen in Sky130 PDK**
- **物理レイアウトと論理ネットリストの等価性確認手法**を把握する  
  **Grasp the process for ensuring logical and layout equivalence**

---

## 🧪 LVSとは？｜What is LVS?

**LVS（Layout vs. Schematic）** とは、以下の2つが**等価かどうかを検証する工程**です：

- レイアウトで作成された**物理構造（Physical Layout）**  
- 回路図またはVerilogから得られる**論理構造（Netlist / Schematic）**

📌 等価性の確認により、製造されるチップが**設計通り動作することを保証**します。

---

## 🔧 使用ツール：Netgen｜Tool: Netgen

Sky130 PDK には、LVS 用の設定ファイル（`setup.tcl`）が付属しています。  
**Netgen** は、物理と論理のネットリストを比較して等価性を検証します。

---

## 🔍 LVS実行の基本手順（Netgen）｜Running LVS with Netgen

### 【1】🧪 実行例：FSMモジュールのLVSチェック

```bash
netgen -batch lvs \
  "fsm_engine.spice fsm_engine" \
  "fsm_engine.scs fsm_engine" \
  setup.tcl | tee lvs_report.log
```

| ファイル名 | 説明（JP） | 説明（EN） |
|------------|------------|------------|
| `fsm_engine.spice` | Magicで抽出したレイアウトSPICE | Extracted layout netlist |
| `fsm_engine.scs`   | Verilogを変換した参照SPICE    | Reference schematic netlist |
| `setup.tcl`        | Sky130付属のLVSルール設定      | LVS rules provided in PDK |

---

## 📋 LVSチェック項目の例｜LVS Check Items

| ✅ **チェック項目**<br>Check Item | 🔍 **内容**<br>Description |
|----------------------------|-----------------------------|
| ノード数一致<br>Node Count Match | ピン・配線のノード数が一致しているか<br>Matching number of nodes |
| 接続関係一致<br>Connectivity Match | 各ピンが正しく接続されているか<br>Correct wiring of each pin |
| デバイス一致<br>Device Match | トランジスタやセルの種類・数の一致<br>Same number and type of devices |

---

## ⚠️ LVS不一致の原因と対策｜Mismatch Causes and Solutions

| ❌ **原因**<br>Cause | ✅ **対策**<br>Solution |
|--------------------|--------------------------|
| ネット名不一致<br>Net name mismatch | Verilogと抽出結果の名前を統一する<br>Ensure consistent naming |
| 抽出失敗（DRC未解決）<br>Extraction failure due to DRC errors | 先にDRCを完全クリア<br>Clear all DRC issues first |
| I/Oピン未整合<br>I/O port mismatch | 入出力の方向・命名を見直す<br>Review I/O declaration and order |

---

## ✅ 本節まとめ｜Summary

- LVSは、**レイアウトと論理の整合性を保証する重要工程**です  
  **LVS ensures the layout matches the intended logic design**
- **Netgen + setup.tcl** を用いれば、Sky130でのLVSを自動化可能  
  **LVS can be scripted with Netgen for reproducible checks**
- LVS成功には、**DRCの完了・ネット名整合・設計ルール準拠**が不可欠  
  **Success requires DRC completion and naming consistency**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [5.3 DRCルールとその根拠（例：metal spacing）](5_3_drc_check.md)  
- ▶️ [5.5 DFM設計：量産対応のためのレイアウト指針](5_5_dfm_guideline.md)  
- 🏠 [特別編 第5章 README に戻る](README.md)
