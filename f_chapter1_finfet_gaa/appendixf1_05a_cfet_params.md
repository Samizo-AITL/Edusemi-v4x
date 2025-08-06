---
layout: default
title: CFET パラメータ補足資料
---

---

# CFET パラメータ補足資料  
**CFET Parameter Supplement (Extension of appendixf1_05_node_params.md)**

---

## 🧭 概要 / Overview

**CFET（Complementary FET）**は、**NMOSとPMOSを垂直方向に積層**する構造により、面積効率と微細化限界の突破を目指す次世代トランジスタ技術です。  
**CFET (Complementary FET)** is a next-generation transistor technology that **vertically stacks NMOS and PMOS**, aiming to overcome scaling limits and enhance area efficiency.

---

## 🧱 CFET構造の特徴 / Structural Features

| 比較項目 / Feature         | CFET                                | GAA (Nanosheet FET)               |
|----------------------------|-------------------------------------|-----------------------------------|
| 配置構造 / Layout          | NMOS（下段）+ PMOS（上段）           | 横並列 / Stacked horizontally     |
| ゲート構造 / Gate Style    | GAA or Forksheet                    | GAA（Multi-nanosheet）            |
| 面積効率 / Area Efficiency | 非常に高い / Very High              | 高い / High                       |
| 静電制御 / Electrostatics  | 優れる（GAAベース）/ Excellent      | 優れる / Excellent                |
| 製造難易度 / Processability| 非常に高い / Very challenging       | 高いが量産実績あり / Proven      |
| 配線密度 / Routing Density | 配線競合あり / Routing congestion  | 比較的自由 / Relatively free     |

---

## 📊 想定パラメータ例 / Projected Parameter Table

| ノード<br>Node | 構造<br>Structure     | 概要<br>Description             | $V_{\mathrm{DD}}$ (V) | $L_g$ (nm) | $T_{\mathrm{ox}}$ (nm) | 備考 / Note |
|----------------|------------------------|-------------------------------|------------------------|------------|-------------------------|-------------|
| 1.0nm          | CFET (GAA上下積層)     | NMOS + PMOS stacked vertically | 0.45                   | ~8         | ~0.4                    | Based on Intel and IMEC research |
| 0.7nm          | CFET (Forksheet構想)   | Gate-Fin decoupled stack       | TBD                    | ~6–7       | TBD                     | Conceptual by IMEC / model TBD   |

---

## 🧠 実効幅と電流密度に関する注意点  
### Notes on Effective Width and Current Estimation

CFETはNMOS/PMOSを物理的に上下積層する構造であり、以下の点に注意が必要です：

- **$W_{\mathrm{total}}$ の再定義が必要**
  - FinFET: $W_{\mathrm{total}} = n(2H + W)$  
  - GAA: $W_{\mathrm{total}} = 2(H + W)n$  
  - → CFETでは、**垂直積層構造のため従来式が適用できず、新たな定義が必要**

- **$I_{\mathrm{dsat}}$ の評価**
  - 同一セル面積に対して **2デバイス（n/p）が重なる構造**となるため、$I_{\mathrm{dsat}}$ ≒ 2倍とみなす研究も存在
  - ただし、正確なBSIMモデルには未反映

---

## 🔬 モデル整備状況 / Model Availability

| モデル / Model | CFET対応 / CFET Ready | 備考 / Note |
|----------------|------------------------|----------------|
| BSIM-CMG       | ×                      | Up to GAA only. CFET not supported yet. |
| BSIM-BULK      | ×                      | For planar CMOS. Not applicable.        |
| BSIM6（研究中）| △                      | Some Verilog-A level CFET attempts exist. |

---

## 📌 技術課題と展望 / Challenges and Outlook

- **プロセス整合性**
  - 製造順序、熱処理、ドーピング分離などの高精度制御が必要
- **熱干渉**
  - 下層NMOSの熱が上層PMOSに伝播し、性能劣化の懸念あり
- **配線とレイアウト制約**
  - 上下ビア交差、GND/VDDの分離に新たな設計指針が必要
- **設計ツールとモデル未整備**
  - PDK未整備のため、**現時点では定量的設計が困難**

---

## 📗 関連補足資料 / Related Materials

- [`appendixf1_05_node_params.md`](./appendixf1_05_node_params.md)  
  ↳ Node-wise parameter table for FinFET and GAA  
- [`appendixf1_04_cfet.md`](./appendixf1_04_cfet.md)  
  ↳ CFET structure and fabrication challenges  
- [`appendixf1_06_node_params_structural.md`](./appendixf1_06_node_params_structural.md)  
  ↳ Node structural parameters including $n$, $H$, $W$

---

## 📝 注記 / Notes

- 本資料は教育・設計戦略検討用にまとめたものであり、**実製品や設計開発の直接的な基準にはなりません。**
- CFET対応のBSIMモデルが将来整備された場合、本資料も適宜更新予定です。
- 教育用教材・PoC構想・設計指針整理などにご自由にご活用ください。

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)

