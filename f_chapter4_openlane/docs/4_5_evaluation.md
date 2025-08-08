---
layout: default
title: 4.5 設計評価レポートと比較（FSM / PID / SoC）
---

# 4.5 設計評価レポートと比較（FSM / PID / SoC）  
**Design Evaluation and Comparison (FSM / PID / SoC)**

---

## 🎯 本節の目的｜Purpose of This Section

| 📝 日本語｜Japanese | 📘 English |
|--------------------|-----------|
| FSM / PID / SoC 各構成の物理設計結果を比較する | Compare physical design results of FSM / PID / SoC |
| 教育用として設計評価の観点を整理する | Define evaluation metrics for educational use |
| 論理構成と物理実装の関係性を把握する | Understand correlation between logic and layout |

---

## 📐 面積・インスタンス数の比較  
**Comparison of Area and Instance Count**

| 🧩 モジュール<br>Module | 🧱 セル面積<br>Cell Area (example) | 🔢 インスタンス数<br>Instances (example) |
|------------------|----------------------------|----------------------------|
| FSM              | 1200 µm²                   | 150                        |
| PID              | 3500 µm²                   | 420                        |
| SoC (FSM + PID)  | 5400 µm²                   | 610                        |

> 📎 値は一例であり、OpenLane条件や設計内容によって異なります。  
> *Numbers may vary based on flow settings and logic design.*

---

## ⏱️ タイミング評価｜Timing Evaluation (Setup Slack)

- レポート位置：`reports/synthesis/timing.rpt` または `signoff/timing.rpt`
- **Slack > 0** ➝ タイミングOK  
- **Violation = 0** が望ましい（setup margin確保）

---

## 📏 配線密度とCore Utilization  
**Routing Density and Core Utilization**

| モジュール<br>Module | `FP_CORE_UTIL` | 実効配線密度<br>Effective Routing Density | 備考｜Remarks |
|----------------------|----------------|------------------------------------------|--------------|
| FSM                  | 30             | 約 20%                                     | シンプル配置 |
| PID                  | 30             | 約 28%                                     | 算術演算密度高め |
| SoC                  | 45             | 約 35%                                     | 統合による密度上昇 |

> 配線密度が高すぎるとDRC違反やタイミング不良を誘発するため、適切な調整が必要です。

---

## 🧪 DRC / LVS 成否比較  
**DRC / LVS Result Comparison**

| モジュール<br>Module | ✅ DRC | ✅ LVS |
|----------------------|--------|--------|
| FSM                  | OK     | OK     |
| PID                  | OK     | OK     |
| SoC                  | OK     | OK     |

> ❗ DRC違反が出た場合は `PL_TARGET_DENSITY` や floorplan 指定を見直しましょう。

---

## 💬 考察の視点｜Evaluation Insights

- FSMは論理が単純でコンパクトな物理設計が可能  
  → 高い面積効率・低密度でDRC通過しやすい  
- PIDは加算器・乗算器を含み、インスタンス数や配線密度が高くなる  
- SoCでは統合による面積・I/O数の増加と、配線長の最適化が課題となる

---

## ✅ まとめ｜Summary

| 🇯🇵 日本語 | 🇺🇸 English |
|------------|------------|
| FSM / PID / SoC をOpenLaneで統一評価可能 | Unified evaluation via OpenLane is feasible |
| 教材として数値評価・構造比較に活用できる | Useful for structured educational assessment |
| 面積・DRC・タイミングなどの物理特性を比較検証 | Quantitative comparison of physical metrics |

---

## 📎 前後の節｜Previous / Next Sections

- ◀️ 前の節｜Previous: [4.4 SoC統合モジュールの実装](docs/4_4_soc_layout.md)  
- ▶️ 次の節｜Next: [4.6 GDSレイアウトの可視化と考察](docs/4_6_gds_view.md)

📚 [🔙 特別編 第4章 README に戻る](../README.md)
