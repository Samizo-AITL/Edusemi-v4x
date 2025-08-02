# MRAM Stress Distribution Map（MRAM応力分布図）

## 1. Overview / 概要
- MRAMセルにおける機械的応力の重要性
- 書き込み動作・信頼性（MTJ破壊・熱障壁低下）への影響

## 2. Simulation Setup / シミュレーション設定
- FEMソルバー：Ansys / COMSOL / Sky130版OpenFEM（仮想例可）
- 材料構成：MTJ層（CoFeB / MgO / CoFeB）、BE / TE
- 熱源：書き込みパルスによる Joule 発熱

## 3. Stress Map Results / 応力分布結果
- 熱起因応力（熱-機械連成解析）
- 応力集中領域（MTJ周辺、Cu BEとの界面）
- 下図参照（例：色マップ付き2D断面図）

## 4. Interpretation / 解釈と設計フィードバック
- ストレスのピーク値とMTJ損傷の相関
- 配線設計／層間構成変更による緩和例

## 5. SystemDK DesignKit への反映
- BRDK/IPDKへの応力耐性パラメータ追加
- AMS / MRAM混載設計時の警告マーカー設定案

## 6. References / 参考文献
- [1] J. Kim et al., IEEE TED, 2023.
- [2] 内製PoC構造モデル、熱-応力FEM結果（図挿入）

---

（例図挿入）

![stress_map](figures/mram_stress_map_sample.png)
