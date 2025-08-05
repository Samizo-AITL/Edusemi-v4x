# 📐 BSIMモデルとPDKの関係  
# 📐 BSIM Models and Their Role in PDKs

---

## 🎯 概要｜Overview

BSIM（Berkeley Short-channel IGFET Model）モデルは、MOSFETの物理動作をSPICEで忠実に再現するための業界標準モデルです。  
PDKに含まれるBSIMモデルは、**ノード世代・トランジスタ構造（バルク／FinFET／GAA）に応じて最適化されており、EDA環境でのシミュレーション精度に直結します**。

BSIM (Berkeley Short-channel IGFET Model) is the industry-standard SPICE model for accurately simulating MOSFET behavior.  
PDKs include BSIM models that are tailored to the process node and device architecture (Bulk, FinFET, GAA), ensuring high simulation fidelity in EDA environments.

---

## 📚 モデル世代と適用構造｜BSIM Generations and Device Compatibility

| モデル名<br>Model | 対応ノード例<br>Applicable Nodes | 構造<br>Device Type | 備考｜Notes |
|------------------|------------------------------|---------------------|-------------------------|
| **BSIM3**        | ～0.25μm                     | Bulk CMOS           | Sky130 など教育PDKで使用されることもある |
| **BSIM4**        | 130nm〜28nm                  | Bulk CMOS           | HCI・DIBL対応、DRC準拠の商用PDKで主流 |
| **BSIM-CMG**     | 22nm〜3nm                    | FinFET / GAA        | 多ゲート対応。Level=54、Fin/GAA対応の標準モデル |
| **BSIM6**        | 研究中（1.4nm以下）          | GAA / CFET          | 高精度物理モデル、今後の主流候補（要検証） |

---

## 🔬 BSIM-CMG：先端FinFET/GAA対応の標準モデル  
### BSIM-CMG: Standard Model for FinFET and GAA

BSIM-CMG（Common Multi-Gate）は、FinFETやGAA構造に特化したBSIMモデルで、**Fin高さ・幅、シート数、酸化膜厚、チャネル制御**など、物理パラメータを詳細に扱います。PDK内では `.model` ブロックに記述され、Spectre / HSPICE / ngspice等で利用されます。

BSIM-CMG is designed for FinFET and GAA devices, enabling detailed modeling of fin height/width, nanosheet count, oxide thickness, and electrostatic control.  
It appears in PDK `.model` blocks and is supported by Spectre, HSPICE, ngspice, and others.

---

## 🧾 BSIMモデルの主要パラメータ例  
### Key Parameters in BSIM Models

| パラメータ名 | 説明｜Description |
|--------------|------------------|
| `Vth0`       | 初期しきい値電圧（Threshold Voltage） |
| `tox` / `epsrox` | 酸化膜厚／誘電率（Oxide Thickness / Permittivity） |
| `finH` / `finW` / `nfin` | Fin高さ・幅・本数（GAAではH/W/sheet数） |
| `u0` / `vsat` | 移動度・飽和速度（Mobility / Saturation Velocity） |
| `rdsw` / `rd` / `rs` | ソース・ドレインの寄生抵抗（Parasitic Resistance） |
| `eta`, `theta`, `alpha` | モデル補正係数（Mobility degradation, DIBL, SCEなど） |
| `geo`, `rgate`, `rbody` | 抵抗・寄生構造の詳細制御用パラメータ |

---

## 🧪 SPICEモデルファイル構成例  
### Typical SPICE Model File Structure

```spice
.model nmos bsimcmg \
+ type = n \
+ nch = 1 \
+ Vth0 = 0.42 \
+ finH = 50n \
+ finW = 8n \
+ nfin = 4 \
+ tox = 1.2n \
+ u0 = 450 \
+ vsat = 1.2e7 \
+ rdsw = 100 \
+ ...
```

- 多くのPDKでは `.model`, `.lib`, `.params` のような構成で提供  
- モデル階層は `.include` により分割可能

---

## 📎 PDKにおけるBSIMの役割  
### BSIM's Role in PDKs

- **回路設計者向け：** BSIMモデルは、シミュレーション精度を担保し、設計マージン・性能評価の基礎となります  
- **PDK開発者向け：** モデル更新により、リーク特性・短チャネル効果・バラつき解析などに対応可能  
- **教育用途：** Sky130等ではBSIM3/4が用いられ、BSIM-CMGは最先端ノード設計演習にも適用可能

---

## 🧠 教育的補足｜Educational Notes

- **BSIMモデルはノードの縮小とともに進化**：  
  例）BSIM3 → BSIM4（バルク）→ BSIM-CMG（FinFET/GAA）→ BSIM6（将来）  
- **SPICEとの親和性が高く、汎用的に使用可能**  
- **BSIMパラメータ表とのリンク教材**  
  → [`appendixf1_05_node_params.md`](../appendix/appendixf1_05_node_params.md)

---

## 📘 参考リンク・資料｜Reference Links

- [BSIM公式ページ（UC Berkeley）](https://bsim.berkeley.edu/)  
- [BSIM-CMG GitHub（Verilog-A / モデルコード）](https://github.com/ucbsimgroup)  
- [Sky130 PDK (Google/Skywater)](https://github.com/google/skywater-pdk)  
- [OpenLane / Efabless PDK統合](https://github.com/The-OpenROAD-Project/OpenLane)

---

## 📦 関連セクション｜Related Sections

| セクション | 内容 |
|------------|------|
| [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/) | MOS特性としきい値／チャネルモデル解析 |
| [`chapter6_pdk_eda/`](../chapter6_pdk_eda/) | 本章全体（PDK/EDA連携） |
| [`appendixf1_05_node_params.md`](../appendix/appendixf1_05_node_params.md) | 各ノード別パラメータ・BSIM対応表 |

---

## 👤 著者・ライセンス｜Author & License

| 🏷️ 項目｜Item | 📝 内容｜Details |
|---------------|-------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **License** | MIT License（再配布・改変自由） |

---
