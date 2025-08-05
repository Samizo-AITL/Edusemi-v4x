# 📊 FinFET / GAA 各ノード世代のパラメータ比較表  
**Parameter Comparison Table for FinFET and GAA Generations**

---

## ✅ FinFET 世代別パラメータ比較  
**FinFET Generation-wise Parameters**

| ノード<br>Node | $H_{\mathrm{fin}}$ (nm)<br>Fin Height | $W_{\mathrm{fin}}$ (nm)<br>Fin Width | $n$<br># of Fins | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (nA/nm)<br>Linear Current | $I_{\mathrm{dsat}}$ (nA/nm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/nm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|---------------|------------------------|----------------------|------------|-----------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **22nm**      | ~40                   | ~10                 | 2          | $2 \times 40 + 10 = 90 \times 2 = \mathbf{180}$ | 25                   | 1.2（EOT換算）            | ~0.4–0.5                    | ~500                         | ~1000                         | ~10                         | ~100                          | ~2.0                         |
| **14nm**      | ~45                   | ~8                  | 3          | $2 \times 45 + 8 = 98 \times 3 = \mathbf{294}$ | 20                   | 1.0                       | ~0.35–0.45                  | ~550                         | ~1100                         | ~5                          | ~50                           | ~1.8                         |
| **10nm**      | ~50                   | ~7                  | 3–4        | ~300–400                         | 18                   | 0.85                      | ~0.3–0.4                    | ~600                         | ~1200                         | ~1–2                        | ~10–20                        | ~1.6                         |
| **7nm**       | ~55                   | ~6                  | 4–5        | ~400–500                         | 16                   | 0.75                      | ~0.3                        | ~650                         | ~1300                         | <1                          | ~5                            | ~1.5                         |
| **5nm**       | ~60                   | ~5                  | 5–6        | ~500–600                         | 14                   | 0.65                      | ~0.25–0.3                   | ~700                         | ~1400                         | <0.5                        | ~1–2                          | ~1.3                         |

---

## ✅ GAA 世代別パラメータ比較  
**GAA (Nanosheet) Generation-wise Parameters**

| ノード<br>Node | $W$ (nm)<br>Sheet Width | $H$ (nm)<br>Sheet Height | $n$<br># of Sheets | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (nA/nm)<br>Linear Current | $I_{\mathrm{dsat}}$ (nA/nm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/μm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|------------------------|------------------|-------------------|----------------|------------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **3nm (Samsung SF3E)** | ~20             | ~5                | 3              | $2 \times (5 + 20) \times 3 = \mathbf{150}$ | 14–15                | ~0.6                      | ~0.25                       | ~700                         | ~1400                         | <1                          | ~5                            | ~1.3                         |
| **2nm (TSMC N2)**       | ~25             | ~6                | 4              | $2 \times (6 + 25) \times 4 = \mathbf{248}$ | ~12                  | ~0.55                     | ~0.23                       | ~750                         | ~1500                         | <0.5                        | ~2                            | ~1.2                         |
| **1.4nm (予測値)**       | ~30             | ~6                | 4–5            | $\sim 288$–$360$                     | ~10                  | ~0.5                      | ~0.20                       | ~800                         | ~1600                         | <0.3                        | ~1                            | ~1.1                         |

---

## 🧠 チャネル構造別の有効幅計算式  

- **FinFET**：

$$
W_{\mathrm{total}} = n \cdot (2H_{\mathrm{fin}} + W_{\mathrm{fin}})
$$

- **GAA**：

$$
W_{\mathrm{total}} = 2 \cdot (H + W) \cdot n
$$

---

## 🧯 ノード別 抵抗要素比較表  
**Generation-wise Resistance Components**

> ※ コンタクトチェーン抵抗／ビアチェーン抵抗は、代表的なテスト構造における**全体直列抵抗**であり、n本のコンタクト・ビアで構成された合計値を示す（n数は参考値として表示）。

| ノード | アクティブ抵抗<br>Active Region Resistance (Ω/□) | ゲート抵抗<br>Gate Resistance (Ω/□) | コンタクトチェーン抵抗<br>Contact Chain Resistance (Ω, n ≈ contacts) | ビアチェーン抵抗<br>Via Chain Resistance (Ω, n ≈ vias) | 配線抵抗<br>Metal Interconnect Resistance (Ω/□) |
|--------|----------------------------------------------|-----------------------------------|--------------------------------------------------------|---------------------------------------------------|-----------------------------------------------|
| 22nm   | ~80                                          | ~2.5                              | ~100 (n≈100)                                           | ~120 (n≈100)                                     | ~0.12                                          |
| 14nm   | ~70                                          | ~2.0                              | ~80 (n≈80)                                             | ~100 (n≈90)                                      | ~0.10                                          |
| 10nm   | ~60                                          | ~1.8                              | ~70 (n≈70)                                             | ~90 (n≈80)                                       | ~0.09                                          |
| 7nm    | ~50                                          | ~1.5                              | ~60 (n≈60)                                             | ~80 (n≈70)                                       | ~0.08                                          |
| 5nm    | ~40                                          | ~1.3                              | ~50 (n≈50)                                             | ~70 (n≈60)                                       | ~0.07                                          |
| 3nm (GAA) | ~35                                       | ~1.0                              | ~45 (n≈45)                                             | ~60 (n≈50)                                       | ~0.06                                          |
| 2nm (GAA) | ~30                                       | ~0.9                              | ~40 (n≈40)                                             | ~55 (n≈45)                                       | ~0.055                                         |
| 1.4nm (予測) | ~25                                     | ~0.8                              | ~35 (n≈35)                                             | ~50 (n≈40)                                       | ~0.05                                          |

---

## 🧩 FinFET vs GAA 構造の要点比較表

| 比較項目 | FinFET | GAA (Nanosheet) |
|----------|--------|------------------|
| ゲート接触面 | 3面（両側＋上） | 4面（上下左右すべて） |
| チャネル形状 | Fin（立体リッジ） | ナノシート（薄板積層） |
| 有効幅の式 | $n \cdot (2H + W)$ | $2 \cdot (H + W) \cdot n$ |
| 面積効率 | △（Fin配置制限） | ◎（層数で柔軟対応） |
| 静電制御性 | ◎ | ★優（完全囲み） |
| 微細化限界 | ～5nm | ～1.4nm以下も想定可 |

---

## 📎 補足：BSIM-CMGモデルと先端ノード対応  
**BSIM-CMG Model and Advanced Node Compatibility**

**BSIM-CMG（Common Multi-Gate）モデル**は、FinFETやGAA、将来のCFETなどに対応する、標準的なSPICEモデリングフレームワークです。先端ノードのPVTシミュレーションやSystemDK/PoC設計における評価モデルとして活用されます。

| モデル名 | 対応構造 | 特徴 |
|----------|----------|------|
| BSIM-CMG | FinFET, GAA, Nanowire | 多ゲート構造に対応。物理ベースのパラメータ化。階層設計（Level=54） |
| BSIM-BULK | バルクMOS | 従来のプレFinFET時代の標準モデル（Level=52） |
| BSIM6（参考） | GAA, CFET など | 次世代向けの詳細物理モデル（研究中） |

### 🧠 CMGの主要パラメータ例（抜粋）

| パラメータ | 内容 |
|------------|------|
| `nfin`, `finH`, `finW` | Fin本数、高さ、幅（GAA時は層数） |
| `tox`, `epsrox` | ゲート酸化膜の厚み、誘電率 |
| `Vth0`, `u0`, `vsat` | 初期閾値電圧、移動度、飽和速度 |
| `rdsw`, `rd`, `rs` | S/D寄生抵抗成分 |
| `eta`, `theta`, `alpha` | モビリティ変調、SCE近似項 |

> 各パラメータは、本資料のノード別特性と対応しており、設計演習やSPICEモデル設定において直接参照可能です。

### 📘 参考リンク

- BSIM-CMG公式： [https://bsim.berkeley.edu/models/bsimcmg/](https://bsim.berkeley.edu/models/bsimcmg/)
- GitHub（モデルソース/Verilog-A含む）： [https://github.com/ucbsimgroup](https://github.com/ucbsimgroup)

---

## 📘 関連資料への導線

- ノード進化一覧： [`appendix_f1_node_evolution.md`](appendix_f1_node_evolution.md)
- FinFETフロー： [`appendixf1_01_finfetflow.md`](appendixf1_01_finfetflow.md)
- GAAプロセス： [`appendixf1_02_gaaflow.md`](appendixf1_02_gaaflow.md)
- FinFET vs GAA 比較： [`appendixf1_03_finfet_vs_gaa.md`](appendixf1_03_finfet_vs_gaa.md)
- CFET構造： [`appendixf1_04_cfet.md`](appendixf1_04_cfet.md)
- FEM評価： [`fem_constraints.md`](fem_constraints.md)

---
