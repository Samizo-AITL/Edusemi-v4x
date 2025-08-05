# 🧬 appendixf1_05a_cfet_params.md  
## CFET パラメータ補足資料  
**CFET Parameter Supplement (Extension of appendixf1_05_node_params.md)**

---

## 🧭 概要 / Overview

**CFET（Complementary FET）**は、**NMOSとPMOSを垂直方向に積層**する構造により、面積効率と微細化限界の突破を目指す次世代トランジスタ技術です。

CFET (Complementary FET) is a next-generation transistor technology that vertically stacks NMOS and PMOS to push the boundaries of area efficiency and device scaling.

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
| 1.0nm          | CFET (GAA上下積層)     | NMOS + PMOS stacked vertically | 0.45                   | ~8         | ~0.4                    | Intel, IMECによる研究発表ベース |
| 0.7nm          | CFET (Forksheet構想)   | GateとFinの分離＋積層構造     | TBD                    | ~6–7       | TBD                     | IMEC構想中 / Model未確定        |

---

## 🧠 実効幅・電流定義に関する注意点  
### Notes on Effective Width and Current Estimation

従来の FinFET や GAA と異なり、CFET は NMOS / PMOS が上下に物理的に積層されているため、次の点に注意が必要です：

- **$W_{\mathrm{total}}$ の従来定義は適用不可**
  - FinFET: $W_{\mathrm{total}} = n(2H + W)$  
  - GAA: $W_{\mathrm{total}} = 2(H + W)n$
  - → CFETでは **垂直積層構造のため新たな定義が必要**

- **積層電流密度の推定**
  - 同一面積で 2デバイスが重なるため、**$I_{\mathrm{dsat}}$ を2倍相当とみなす研究もある**
  - ただし正確なモデルは存在しない

---

## 🔬 モデル整備状況 / Model Availability

| モデル / Model | CFET対応 | 備考 / Note |
|----------------|-----------|----------------|
| BSIM-CMG       | ×         | GAAまで対応。CFETは未対応。 |
| BSIM-BULK      | ×         | Planar CMOS用。非対象。     |
| BSIM6（研究中）| △         | 一部でCFET記述例あり（Verilog-Aレベル） |

---

## 📌 技術課題と展望 / Challenges and Outlook

- **プロセス整合性**
  - NMOSとPMOSの製造順序・熱プロファイル・材料整合が必要
- **熱干渉と放熱**
  - 下層NMOSの自己発熱が上層PMOSの性能に影響を与える懸念あり
- **レイアウト制約**
  - GND/VDDネットの分離と上下層ビアの交差制御が困難
- **モデル未整備**
  - BSIMベースの定量設計がまだ不可能 → 設計ツールとの統合が困難

---

## 📗 関連補足資料 / Related Materials

- [appendixf1_05_node_params.md](./appendixf1_05_node_params.md)  
  ↳ 本資料のベースとなる FinFET / GAA の構造・パラメータ表  
- [appendixf1_04_cfet.md](./appendixf1_04_cfet.md)  
  ↳ CFET構造の概論・製造プロセス上の課題と整理  
- [appendixf1_06_node_params_structural.md](./appendixf1_06_node_params_structural.md)  
  ↳ 全ノード構造パラメータ（$n, H, W$）付き設計比較表

---

## 📝 注記 / Notes

- 本資料は、CFETの構造的・設計的検討の方向性を補足するためのものであり、現時点では**定量モデルに基づいた設計は不可能**である。
- 将来的に BSIM-CMG や BSIM6 で CFETが正式サポートされた際、本資料は更新される予定である。
- 教育・PoC・将来設計戦略立案のための参考資料として利用可。
