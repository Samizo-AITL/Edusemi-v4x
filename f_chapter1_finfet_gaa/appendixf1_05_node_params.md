# 📊 FinFET / GAA 各ノード世代のパラメータ比較表  
**Parameter Comparison Table for FinFET and GAA Generations**

---

## ✅ FinFET 世代別パラメータ比較  
**FinFET Generation-wise Parameters**

| ノード<br>Node | $H_{\mathrm{fin}}$ (nm)<br>Fin Height | $W_{\mathrm{fin}}$ (nm)<br>Fin Width | $n$<br># of Fins | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (μA/μm)<br>Linear Current | $I_{\mathrm{dsat}}$ (μA/μm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/μm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|---------------|------------------------|----------------------|------------|-----------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **22nm**      | ~40                   | ~10                 | 2          | $2 \times 40 + 10 = 90 \times 2 = \mathbf{180}$ | 25                   | 1.2（EOT換算）            | ~0.4–0.5                    | ~500                         | ~1000                         | ~10                         | ~100                          | ~2.0                         |
| **14nm**      | ~45                   | ~8                  | 3          | $2 \times 45 + 8 = 98 \times 3 = \mathbf{294}$ | 20                   | 1.0                       | ~0.35–0.45                  | ~550                         | ~1100                         | ~5                          | ~50                           | ~1.8                         |
| **10nm**      | ~50                   | ~7                  | 3–4        | ~300–400                         | 18                   | 0.85                      | ~0.3–0.4                    | ~600                         | ~1200                         | ~1–2                        | ~10–20                        | ~1.6                         |
| **7nm**       | ~55                   | ~6                  | 4–5        | ~400–500                         | 16                   | 0.75                      | ~0.3                        | ~650                         | ~1300                         | <1                          | ~5                            | ~1.5                         |
| **5nm**       | ~60                   | ~5                  | 5–6        | ~500–600                         | 14                   | 0.65                      | ~0.25–0.3                   | ~700                         | ~1400                         | <0.5                        | ~1–2                          | ~1.3                         |

---

## ✅ GAA 世代別パラメータ比較  
**GAA (Nanosheet) Generation-wise Parameters**

| ノード<br>Node | $W$ (nm)<br>Sheet Width | $H$ (nm)<br>Sheet Height | $n$<br># of Sheets | $W_{\mathrm{total}}$ (nm)<br>Effective Width | $L_g$ (nm)<br>Gate Length | $T_{\mathrm{ox}}$ (nm)<br>Oxide Thickness | $V_{\mathrm{th}}$ (V)<br>Threshold Voltage | $I_{\mathrm{dlin}}$ (μA/μm)<br>Linear Current | $I_{\mathrm{dsat}}$ (μA/μm)<br>Saturation Current | $I_{\mathrm{off}}$ (nA/μm)<br>Leakage | $I_{\mathrm{cutoff}}$ (nA)<br>Cutoff Current | $B_{V\mathrm{ds}}$ (V)<br>Breakdown Voltage |
|------------------------|------------------|-------------------|----------------|------------------------------------|----------------------|----------------------------|------------------------------|-------------------------------|--------------------------------|------------------------------|--------------------------------|------------------------------|
| **3nm (Samsung SF3E)** | ~20             | ~5                | 3              | $2 \times (5 + 20) \times 3 = \mathbf{150}$ | 14–15                | ~0.6                      | ~0.25                       | ~700                         | ~1400                         | <1                          | ~5                            | ~1.3                         |
| **2nm (TSMC N2)**       | ~25             | ~6                | 4              | $2 \times (6 + 25) \times 4 = \mathbf{248}$ | ~12                  | ~0.55                     | ~0.23                       | ~750                         | ~1500                         | <0.5                        | ~2                            | ~1.2                         |
| **1.4nm (予測値)**       | ~30             | ~6                | 4–5            | $\sim 288$–$360$                     | ~10                  | ~0.5                      | ~0.20                       | ~800                         | ~1600                         | <0.3                        | ~1                            | ~1.1                         |

---

## 🧠 計算式の補足  

- **FinFET の有効チャネル幅**：

$$
W_{\mathrm{total}} = n \cdot (2H_{\mathrm{fin}} + W_{\mathrm{fin}})
$$

- **GAA の有効チャネル幅**：

$$
W_{\mathrm{total}} = 2 \cdot (H + W) \cdot n
$$

---

## 📘 関連資料への導線

- FEM・熱/応力解析対応： [fem_constraints.md](fem_constraints.md)
- GAA/FinFET設計演習テンプレート： [systemdk_poc.md](systemdk_poc.md)
- パラメトリック設計用Pythonツール： [id_calc_tool.ipynb](id_calc_tool.ipynb)
