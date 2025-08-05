# 📊 FinFET / GAA 各ノード世代のパラメータ比較表  
**Parameter Comparison Table for FinFET and GAA Generations**

...

## 📘 モデルパラメータの出典と補完方法 / Sources and Derivation

| 項目 | 出典・補完方法 | 備考 |
|------|----------------|------|
| Wtotal, Lg, Tox | IEDM論文、TechInsights、IRDS | Fin数やシート構造から構成比を推定 |
| Vth, Idlin, Idsat | BSIM-CMGパラメータ例（NCSU等） | 経験値・SPICE条件下の推定含む |
| Ioff, Icutoff | Samsung SF3, TSMC N3P/N2公開値 | 最大リーク許容値ベース |
| Rg, Rs, Rd | 抵抗モデル分解論文（IEDM 2021等） | FEMモデルとの連携指標として使用 |
| BVds | 汎用MOSFETの崩壊電圧（~2V以下） | 高電圧用途は対象外（SoC基準） |

---

## 🔧 設計応用例 / Design Application Examples

1. **SPICEモデル生成**  
   - BSIM-CMGの `.model` 記述に `Lg`, `Tox`, `Vth`, `Wtotal` を反映し、高精度設計に適用。
   - GAAモデルは短チャネル効果に強く、低Vth設計にも対応。

2. **FEM制約統合**  
   - `Idsat`, `Rs`, `Rg` を使い、FEM解析（熱分布・EM解析）の境界条件に使用。
   - `stress_map.md` / `fem_constraints.md` と連携。

3. **AMS回路設計**  
   - `Icutoff` は高精度ADC, PLL, Bandgap回路に必須の設計パラメータ。
   - GAAの低リーク性が大きな設計メリットに。

4. **PoC制約連動**  
   - `BVds`, `Rs`, `Wtotal` により、PoCパルス設計・マクロ混載制約が決まる。
   - SystemDKの `poc_4.md`, `poc_6.md` と構成的に接続。

---

*Last updated: 2025-08-05*
