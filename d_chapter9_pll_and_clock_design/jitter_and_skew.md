---
layout: default
title: ジッタとスキューの理解と対策 
---

---

# ⏱ `jitter_and_skew.md` – ジッタとスキューの理解と対策  
**Understanding and Mitigation of Jitter and Skew**

---

## 📘 概要｜Overview

高性能LSI設計では、**クロック信号の安定性と整合性**が非常に重要です。  
特に、`ジッタ（Jitter）`と`スキュー（Skew）`はタイミング設計上の大きな課題です。

In high-performance LSI design, **clock signal stability** is crucial.  
This section explains the definitions, causes, effects, and mitigation of **jitter** and **skew**.

---

## 🔄 ジッタとは？｜What is Jitter?

| 項目｜Item | 説明｜Description |
|---------|------------------------------------|
| **定義**｜Definition | クロックエッジの**時間的ばらつき** |
| **種類**｜Types | `ランダムジッタ（RJ）`: ノイズや電源変動による揺らぎ<br>`周期ジッタ（PJ）`: 定周期ノイズによる揺らぎ |
| **影響**｜Impact | ・セットアップマージンの減少<br>・ビットエラー率（BER）悪化（特にSerDes） |

---

## 🔁 スキューとは？｜What is Skew?

| 項目｜Item | 説明｜Description |
|---------|------------------------------------|
| **定義**｜Definition | 同じクロックが**異なる場所に届く時間差** |
| **原因**｜Causes | ・配線距離の不均一<br>・クロックツリーの非対称性<br>・バッファ数やセルばらつき |
| **影響**｜Impact | ・セットアップ／ホールド違反<br>・グリッチや競合動作のリスク |

---

## ✅ 対策技術｜Mitigation Techniques

| 問題｜Issue | 対策｜Mitigation |
|------------|------------------|
| **ジッタ** | ・PLLループ設計最適化<br>・電源ノイズ対策（LDO, デカップリング）<br>・シールド配線／GND参照強化 |
| **スキュー** | ・対称的なクロックツリー構成（H-Tree）<br>・バッファ挿入とCTSの最適化<br>・Post-CTS STAによる検証 |

---

## 🧪 測定と解析｜Measurement and Simulation

- **ジッタ**：アイパターン観測（オシロスコープ）、ジッタアナライザによる波形測定  
  *Jitter is evaluated using oscilloscope, eye-diagram analysis, or jitter analyzers.*

- **スキュー**：レイアウト段階でSTA（Static Timing Analysis）を用いて解析  
  *Skew is analyzed during layout using static timing analysis tools.*

---

## 📚 関連章｜Related Chapters

- [`pll_basics.md`](./pll_basics.md)：ジッタ源としてのPLL構造と特性  
- [`clock_tree_design.md`](./clock_tree_design.md)：スキュー対策のためのCTS技術  

---

### ⏰ 応用編 第9章：PLLとクロック設計｜Applied Chapter 9: PLL and Clock Design  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 Shinichi Samizo / MIT License
