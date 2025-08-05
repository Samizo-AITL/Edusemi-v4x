---
title: Parameter Comparison Table for FinFET and GAA Generations
layout: default
---

# 📊 Parameter Comparison Table for FinFET and GAA Generations

---

## 🔄 NMOS / PMOS Parameter Comparison Table (22nm–1.4nm, Typical @25℃, BSIM-CMG)

全項目は 25℃ / BSIM-CMG モデルに基づいて算出。  
Effective Width（ $W_{\mathrm{total}}$ ）は FinFET / GAA に応じて以下の式で算出：

- FinFET: $W_{\mathrm{total}} = n \cdot (2H + W)$  
- GAA: $W_{\mathrm{total}} = 2 \cdot (H + W) \cdot n$

| Node | Structure | Type | $V_{\mathrm{DD}}$ (V)<br>Supply Voltage | $n$ | $H$ (nm)<br>Height | $W$ (nm)<br>Width | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (nA/nm)<br>Linear Current | $I_{\mathrm{dsat}}$ (nA/nm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/nm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $BV_{DS}$ (V)<br>Breakdown Voltage | Note |
|----------------|------------------|----------------|----------------------|-----|-----------|-----------|-------------------------|----------------|------------------------|-------------------------|----------------------------|-----------------------------|-----------------------------|----------------------------|-------------------------|------------------------|
| 22nm | FinFET | **NMOS** | 0.8 | 2 | 40 | 10 | 180 | 25 | 1.2 | ~0.45 | ~500 | ~1000 | ~10 | ~100 | ~2.0 | 25℃ / BSIM-CMG |
|      |        | **PMOS** | 0.8 | 2 | 40 | 10 | 180 | 25 | 1.2 | ~−0.45 | ~350 | ~750 | ~10 | ~100 | ~2.0 | 25℃ / BSIM-CMG |
| 14nm | FinFET | **NMOS** | 0.75 | 3 | 45 | 8 | 294 | 20 | 1.0 | ~0.40 | ~550 | ~1100 | ~5 | ~50 | ~1.8 | 25℃ / BSIM-CMG |
|      |        | **PMOS** | 0.75 | 3 | 45 | 8 | 294 | 20 | 1.0 | ~−0.40 | ~385 | ~825 | ~5 | ~50 | ~1.8 | 25℃ / BSIM-CMG |
| 10nm | FinFET | **NMOS** | 0.7 | 3 | 50 | 10 | 320 | 18 | 0.85 | ~0.35 | ~600 | ~1200 | ~1–2 | ~10–20 | ~1.6 | 25℃ / BSIM-CMG |
|      |        | **PMOS** | 0.7 | 3 | 50 | 10 | 320 | 18 | 0.85 | ~−0.35 | ~420 | ~900 | ~1–2 | ~10–20 | ~1.6 | 25℃ / BSIM-CMG |
| 7nm | FinFET | **NMOS** | 0.65 | 4 | 55 | 10 | 480 | 16 | 0.75 | ~0.30 | ~650 | ~1300 | <1.0 | ~5 | ~1.5 | 25℃ / BSIM-CMG |
|     |        | **PMOS** | 0.65 | 4 | 55 | 10 | 480 | 16 | 0.75 | ~−0.30 | ~460 | ~950 | <1.0 | ~5 | ~1.5 | 25℃ / BSIM-CMG |
| 5nm | FinFET | **NMOS** | 0.60 | 5 | 55 | 8 | 550 | 14 | 0.65 | ~0.30 | ~700 | ~1400 | <0.5 | ~1–2 | ~1.3 | 25℃ / BSIM-CMG |
|     |        | **PMOS** | 0.60 | 5 | 55 | 8 | 550 | 14 | 0.65 | ~−0.30 | ~500 | ~1000 | <0.5 | ~1–2 | ~1.3 | 25℃ / BSIM-CMG |
| 3nm | GAA    | **NMOS** | 0.55 | 4 | 30 | 15 | 360 | 14–15 | 0.60 | ~0.25 | ~700 | ~1400 | <1.0 | ~5 | ~1.2 | 25℃ / BSIM-CMG |
|     |        | **PMOS** | 0.55 | 4 | 30 | 15 | 360 | 14–15 | 0.60 | ~−0.25 | ~500 | ~1000 | <1.0 | ~5 | ~1.2 | 25℃ / BSIM-CMG |
| 2nm | GAA    | **NMOS** | 0.50 | 4 | 28 | 14 | 336 | ~12 | 0.55 | ~0.23 | ~750 | ~1500 | <0.5 | ~2 | ~1.1 | 25℃ / BSIM-CMG |
|     |        | **PMOS** | 0.50 | 4 | 28 | 14 | 336 | ~12 | 0.55 | ~−0.23 | ~550 | ~1100 | <0.5 | ~2 | ~1.1 | 25℃ / BSIM-CMG |
| 1.4nm | GAA (Est.) | **NMOS** | 0.45 | 5 | 28 | 16 | 440 | ~10 | 0.50 | ~0.20 | ~800 | ~1600 | <0.3 | ~1 | ~1.0 | 25℃ / BSIM-CMG |
|        |             | **PMOS** | 0.45 | 5 | 28 | 16 | 440 | ~10 | 0.50 | ~−0.20 | ~600 | ~1200 | <0.3 | ~1 | ~1.0 | 25℃ / BSIM-CMG |

> **📝 備考：**  
> - Breakdown Voltage ($BV_{DS}$) は設計電圧より高い安全マージンを持つよう設計される傾向があり、ノード縮小により漸減傾向。  
> - 全値は BSIM-CMG モデルおよび文献を基にした代表的推定値。

## 🧠 補足式： $W_{\mathrm{total}}$  の計算方法

- **FinFET**：
  
$$
W_{\mathrm{total}} = n \cdot (2H_{\mathrm{fin}} + W_{\mathrm{fin}})
$$

- **GAA**：

$$
W_{\mathrm{total}} = 2 \cdot (H + W) \cdot n
$$

## 📝 備考
- 各パラメータは代表的な文献値・モデル値・BSIM-CMGを基に推定。
- $W_{\mathrm{total}}$ は幾何パラメータ $(n, H, W)$ に基づいて再計算済み。
- GAA構造は **multi-nanosheet (Nanosheet FET)** を前提とする。

---

## 🧩 FinFET vs GAA の構造比較  
**Structural Comparison of FinFET vs GAA**

| 比較項目 / Feature         | FinFET                            | GAA (Nanosheet)                     |
|----------------------------|-----------------------------------|-------------------------------------|
| ゲート接触面 / Gate Faces   | 3面 (top + sidewalls)            | 4面 (top, bottom, sidewalls)       |
| チャネル形状 / Channel    | Fin構造 / Ridge                   | シート積層 / Stacked sheets        |
| 有効幅式 / $W_\text{total}$ Formula | $n(2H + W)$                        | $2(H + W)n$                         |
| 面積効率 / Area Efficiency | 中程度 / Moderate                | 高 / Excellent                      |
| 静電制御 / Electrostatics  | 優 / Good                         | 非常に優 / Excellent               |
| 微細化限界 / Scaling Limit | ～5nm                            | ～1.4nm またはそれ以下 / ~1.4nm or less |

---

## 🧯 NMOS / PMOS Resistance Comparison Table (22nm–1.4nm, Typical @25℃, BSIM-CMG)

> ※すべて25℃での設計代表値であり、Metal層は共通材料（例：Cu）を前提としています。  
> Typical resistance values at 25℃. Metal layers assume common materials (e.g., Cu).  
> ただし、**NMOS / PMOS 間でMetalシート抵抗（Ω/□）が“実効的に異なる”**ことがあります。  
> However, **effective metal sheet resistance (Ω/□) may differ between NMOS and PMOS** due to design/layout factors.  
> **これらの数値は、BSIM-CMGモデルに基づいて算出された代表値です。**  
> **These values are estimated based on the BSIM-CMG model.**

| Node | Type | $R_{\mathrm{active}}$ (Ω/□)<br>Diffusion | $R_{\mathrm{gate}}$ (Ω/□)<br>Gate | $R_{\mathrm{contact}}$ (Ω)<br>Contact Chain | $R_{\mathrm{via}}$ (Ω)<br>Via Chain | $R_{\mathrm{metal}}$ (Ω/□)<br>Metal |
|----------------|----------------|------------------------------|-------------------------|----------------------------------|-------------------------|--------------------------|
| 22nm           | **NMOS**       | ~80                         | ~2.5                    | ~100                             | ~120                    | ~0.12                   |
|                | **PMOS**       | ~90                         | ~2.6                    | ~110                             | ~130                    | ~0.13                   |
| 14nm           | **NMOS**       | ~70                         | ~2.0                    | ~80                              | ~100                    | ~0.10                   |
|                | **PMOS**       | ~80                         | ~2.1                    | ~90                              | ~110                    | ~0.11                   |
| 10nm           | **NMOS**       | ~60                         | ~1.8                    | ~70                              | ~90                     | ~0.09                   |
|                | **PMOS**       | ~70                         | ~1.9                    | ~80                              | ~95                     | ~0.095                  |
| 7nm            | **NMOS**       | ~50                         | ~1.5                    | ~60                              | ~80                     | ~0.08                   |
|                | **PMOS**       | ~60                         | ~1.6                    | ~70                              | ~85                     | ~0.085                  |
| 5nm            | **NMOS**       | ~40                         | ~1.3                    | ~50                              | ~70                     | ~0.07                   |
|                | **PMOS**       | ~50                         | ~1.4                    | ~60                              | ~80                     | ~0.075                  |
| 3nm            | **NMOS**       | ~35                         | ~1.0                    | ~45                              | ~60                     | ~0.06                   |
|                | **PMOS**       | ~45                         | ~1.1                    | ~55                              | ~70                     | ~0.065                  |
| 2nm            | **NMOS**       | ~30                         | ~0.9                    | ~40                              | ~55                     | ~0.055                  |
|                | **PMOS**       | ~38                         | ~1.0                    | ~48                              | ~60                     | ~0.060                  |
| 1.4nm          | **NMOS**       | ~25                         | ~0.8                    | ~35                              | ~50                     | ~0.05                   |
|                | **PMOS**       | ~33                         | ~0.9                    | ~42                              | ~55                     | ~0.055                  |

---

### 📘 Metalシート抵抗がNMOSとPMOSで異なる設計的理由  
### 📘 Why Metal Sheet Resistance Differs between NMOS and PMOS (Design Perspective)

| 要因 / Factor | NMOS | PMOS | 説明 / Explanation |
|---------------|------|------|--------------------|
| 配線層 / Metal Layer | 主にM1–M2 | M3以降も使用 | 上層ほど厚くRsが低い / Higher metal layers have lower Rs |
| 電流密度 / Current Density | 高い / Higher | 低い / Lower | NMOSは電流大きく、幅広が必要 / NMOS requires wider lines |
| 熱分布 / Thermal Profile | 高温になりやすい | 安定しやすい | 熱上昇でRsが増加 / Heat increases Rs |
| レイアウト配置 / Layout | GND側密集 | VDD側余裕あり | GNDネットは混雑、抵抗上昇 / GND routes are congested |

> ✏️ **設計上は、Metal Rs を等しくするために Via 多重化、層選定、幅拡張が必要です。**  
> In practice, **metal Rs is equalized via layout optimization: via redundancy, wider routing, and layer selection.**

---

## 📗 出力根拠と生成方法  
**Basis of Estimations**

1. **🧾 公開情報ベース**  
   - 各種公式ロードマップ（IEDM, ISSCC, VLSI等）やメーカー発表を再構成  
   - Samsung, TSMC, IMEC, Intelなどの発表資料に基づく

2. **🔬 BSIM-CMGベース構造モデル**  
   - BSIM-CMG準拠のモデルで $W_{\mathrm{total}}$ を定義し、 $J_{\mathrm{dsat}}$ の経験値から $I_{\mathrm{dsat}}$ を計算

3. **⚙️ スケーリング則による補完**  
   - $T_{\mathrm{ox}}$ や $V_{\mathrm{th}}$ など未公表項目は、電気的整合性と物理制約を基に推定

> **Note:** 本表の数値は絶対的な仕様値ではなく、設計指針・教育目的での相対比較を主眼にしています。

---

## 📎 参考リンク / References

- [`appendix_f1_node_evolution.md`](appendix_f1_node_evolution.md) – ノード進化一覧 / Node Evolution
- [`appendixf1_01_finfetflow.md`](appendixf1_01_finfetflow.md) – FinFET工程詳細
- [`appendixf1_02_gaaflow.md`](appendixf1_02_gaaflow.md) – GAAプロセス詳細
- [`appendixf1_03_finfet_vs_gaa.md`](appendixf1_03_finfet_vs_gaa.md) – FinFET vs GAA 比較
- [`appendixf1_04_cfet.md`](appendixf1_04_cfet.md) – CFET構造と課題
- [`appendixf1_05a_cfet_params.md`](appendixf1_05a_cfet_params.md) – CFETパラメータ補足（FinFET/GAA拡張版）
- [`fem_constraints.md`](fem_constraints.md) – FEM熱応力制約

---

## 🧪 モデル情報：BSIM-CMG  
**BSIM-CMG for Advanced Node Modeling**

| モデル / Model | 対応構造 / Supported | 特徴 / Features |
|----------------|----------------------|-----------------|
| BSIM-CMG       | FinFET, GAA, NW      | 多ゲート, Level 54, Verilog-Aあり |
| BSIM-BULK      | Planar CMOS          | 古典MOSFET, Level 52 |
| BSIM6（参考）  | CFET, GAA 次世代     | 研究中モデル, 詳細物理パラメータ対応予定 |

🔗 [BSIM-CMG 公式サイト](https://bsim.berkeley.edu/models/bsimcmg/)  
🔗 [GitHub - UC Berkeley BSIM Group](https://github.com/ucbsimgroup)

---
