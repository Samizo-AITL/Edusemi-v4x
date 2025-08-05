# 📊 appendixf1_05_node_params_FULLv2.md  
**FinFET / GAA 各ノード世代のパラメータ比較と完全設計応用資料**

---

## ✅ 1. ノード別パラメータ表

| Node (nm) | Idsat (nA/nm) | Rs (Ω·μm) | Tox (nm) | Vth (V) |
|-----------|----------------|------------|-----------|----------|
| 22        | 1000           | 46         | 1.2       | 0.45     |
| 14        | 1100           | 44         | 1.0       | 0.40     |
| 10        | 1200           | 42         | 0.85      | 0.35     |
| 7         | 1300           | 40         | 0.75      | 0.30     |
| 5         | 1400           | 38         | 0.65      | 0.28     |
| 3         | 1400           | 35         | 0.60      | 0.25     |
| 2         | 1500           | 30         | 0.55      | 0.23     |

---

## 📐 2. 有効チャネル幅の数式

- FinFET:
  $$
  W_{\mathrm{total}} = n \cdot (2H_{\mathrm{fin}} + W_{\mathrm{fin}})
  $$
- GAA:
  $$
  W_{\mathrm{total}} = 2 \cdot (H + W) \cdot n
  $$

---

## 💾 3. BSIM-CMG `.model` 記述例

### FinFET – 7nm
```verilog
.model n7nm_FinFET BSIMCMG level=54
+ type=n tox=0.75e-9 lgate=16e-9 vth0=0.35
+ nfin=4 finheight=55e-9 finwidth=6e-9
+ u0=300 rdsw=160 rs=46 rd=48
+ vsat=1.5e7
+ cgso=0.9e-10 cgdo=0.9e-10
+ version=4.7
```

### GAA – 2nm
```verilog
.model n2nm_GAA BSIMCMG level=54
+ type=n tox=0.55e-9 lgate=12e-9 vth0=0.23
+ nsheet=4 sheetwidth=25e-9 sheetheight=6e-9
+ u0=370 rdsw=110 rs=30 rd=32
+ vsat=2.2e7
+ cgso=0.65e-10 cgdo=0.65e-10
+ version=4.7
```

---

## 🔧 4. 設計応用例：GAA + MRAM統合

### 条件設定
- GAA Idsat: 1500 nA/nm, Rs: 30 Ω·μm
- MRAM 書き込み電流: 200 μA, パルス幅: 5 ns

### 発熱計算:
$$
P = I^2 R = (200 \, \mu A)^2 \times 30 \, \Omega = 1.2 \, \mu W
$$

### 電流密度:
$$
J = \frac{I}{W \cdot t} = \frac{200e^{-6}}{248e^{-9} \cdot 5e^{-9}} \approx 1.6 \times 10^{13} \, A/m^2
$$

### 設計影響まとめ
| 項目 | 影響 | 対応策 |
|------|------|--------|
| 熱 | ΔT ≈ 11.5°C | FEM設計制約に反映 |
| リーク | GAAリーク増加3–5% | stress_map.mdに接続 |
| 信頼性 | MRAM動作変動 | PoCパルス整合に展開 |

---

## 📈 5. ノードトレンドグラフ

(別ファイルのグラフ参照)

---

## 📘 6. モデル出典と文献リンク

| 項目 | 出典 | URL |
|------|------|-----|
| BSIM-CMG | UC Berkeley | https://bsim.berkeley.edu/models/bsimcmg/ |
| GAA構造 | Samsung VLSI 2022 | https://ieeexplore.ieee.org/document/9744284 |
| 抵抗要素 | IEDM 2021, Intel | https://ieeexplore.ieee.org/document/9632273 |

---

## 📎 関連リンク

- `appendixf1_01_finfetflow.md`
- `appendixf1_02_gaaflow.md`
- `appendixf1_03_finfet_vs_gaa.md`
- `fem_constraints.md`
- `stress_map.md`
- `poc_4.md`, `poc_6.md`

---

*Last updated: 2025-08-05*
