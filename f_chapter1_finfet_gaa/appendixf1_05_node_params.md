# 📊 FinFET / GAA 各ノード世代のパラメータ比較表  
**Parameter Comparison Table for FinFET and GAA Generations**

---

## ✅ FinFET 世代別パラメータ比較  
**FinFET Generation-wise Parameters**

| ノード<br>Node | $H_{\mathrm{fin}}$ (nm)<br>Fin Height | $W_{\mathrm{fin}}$ (nm)<br>Fin Width | $n$<br># of Fins | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (nA/nm)<br>Linear Current | $I_{\mathrm{dsat}}$ (nA/nm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/nm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|---------------|------------------------|----------------------|------------|-----------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **22nm**      | ~40                   | ~10                 | 2          | $2 \times 40 + 10 = 90 \times 2 = \mathbf{180}$ | 25                   | 1.2 (EOT equiv.)         | ~0.4–0.5                    | ~500                         | ~1000                         | ~10                         | ~100                          | ~2.0                         |
| **14nm**      | ~45                   | ~8                  | 3          | $2 \times 45 + 8 = 98 \times 3 = \mathbf{294}$ | 20                   | 1.0                       | ~0.35–0.45                  | ~550                         | ~1100                         | ~5                          | ~50                           | ~1.8                         |
| **10nm**      | ~50                   | ~7                  | 3–4        | ~300–400                         | 18                   | 0.85                      | ~0.3–0.4                    | ~600                         | ~1200                         | ~1–2                        | ~10–20                        | ~1.6                         |
| **7nm**       | ~55                   | ~6                  | 4–5        | ~400–500                         | 16                   | 0.75                      | ~0.3                        | ~650                         | ~1300                         | <1                          | ~5                            | ~1.5                         |
| **5nm**       | ~60                   | ~5                  | 5–6        | ~500–600                         | 14                   | 0.65                      | ~0.25–0.3                   | ~700                         | ~1400                         | <0.5                        | ~1–2                          | ~1.3                         |

---

## ✅ GAA 世代別パラメータ比較  
**GAA (Nanosheet) Generation-wise Parameters**

| ノード<br>Node | $W$ (nm)<br>Sheet Width | $H$ (nm)<br>Sheet Height | $n$<br># of Sheets | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (nA/nm)<br>Linear Current | $I_{\mathrm{dsat}}$ (nA/nm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/nm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|------------------------|------------------|-------------------|----------------|------------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **3nm (Samsung SF3E)** | ~20             | ~5                | 3              | $2 \times (5 + 20) \times 3 = \mathbf{150}$ | 14–15                | ~0.6                      | ~0.25                       | ~700                         | ~1400                         | <1                          | ~5                            | ~1.3                         |
| **2nm (TSMC N2)**       | ~25             | ~6                | 4              | $2 \times (6 + 25) \times 4 = \mathbf{248}$ | ~12                  | ~0.55                     | ~0.23                       | ~750                         | ~1500                         | <0.5                        | ~2                            | ~1.2                         |
| **1.4nm (Estimated)**   | ~30             | ~6                | 4–5            | $\sim 288$–$360$                     | ~10                  | ~0.5                      | ~0.20                       | ~800                         | ~1600                         | <0.3                        | ~1                            | ~1.1                         |

---

## 🧠 有効チャネル幅の計算式  
**Effective Channel Width Formula**

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

| ノード<br>Node | アクティブ抵抗<br>Active Region (Ω/□) | ゲート抵抗<br>Gate (Ω/□) | コンタクトチェーン<br>Contact Chain (Ω, $n$ ≈ contacts) | ビアチェーン<br>Via Chain (Ω, $n$ ≈ vias) | 配線抵抗<br>Metal (Ω/□) |
|--------|-----------------------------|--------------------|----------------------------------------------------|---------------------------------------------|---------------------------|
| 22nm   | ~80                        | ~2.5               | ~100 (n≈100)                                       | ~120 (n≈100)                                | ~0.12                    |
| 14nm   | ~70                        | ~2.0               | ~80 (n≈80)                                         | ~100 (n≈90)                                 | ~0.10                    |
| 10nm   | ~60                        | ~1.8               | ~70 (n≈70)                                         | ~90 (n≈80)                                  | ~0.09                    |
| 7nm    | ~50                        | ~1.5               | ~60 (n≈60)                                         | ~80 (n≈70)                                  | ~0.08                    |
| 5nm    | ~40                        | ~1.3               | ~50 (n≈50)                                         | ~70 (n≈60)                                  | ~0.07                    |
| 3nm    | ~35                        | ~1.0               | ~45 (n≈45)                                         | ~60 (n≈50)                                  | ~0.06                    |
| 2nm    | ~30                        | ~0.9               | ~40 (n≈40)                                         | ~55 (n≈45)                                  | ~0.055                   |
| 1.4nm  | ~25                        | ~0.8               | ~35 (n≈35)                                         | ~50 (n≈40)                                  | ~0.05                    |

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
