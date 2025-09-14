# 4. 実験結果

## 4.1 TZDB特性
- **測定条件**: DCランプ印加 (0.1 V/s)、温度範囲 室温〜125 ℃  
- **評価構造**: FeCAP (MIM)  
- **結果**: 絶縁膜破壊電圧 $V_{\mathrm{bd}}$ の統計分布を抽出し、初期欠陥に起因する早期破壊を確認。高温側で $V_{\mathrm{bd}}$ が低下する傾向は、界面欠陥密度の増加と相関。  
- **意義**: 後述の TDDB 結果と組み合わせることで、**初期故障 (infant mortality)／偶発故障 (random)／真性破壊 (intrinsic)** を分離して評価可能。  

**図3**: TZDB分布（破壊電圧ヒストグラムまたは CDF）  
<img src="./figures/fig3_tzdb.png" alt="TZDB" width="80%">

---

## 4.2 TDDB特性
- **測定条件**: ゲート電圧ストレス $\pm 2.3 / 2.5 / 2.7\ \mathrm{V}$、温度 85 ℃・125 ℃  
- **評価構造**: FeCAP (MIM)  

### Weibull解析
- **結果**: Weibull フィットにより、形状パラメータ $\beta \approx 1.3$、特性寿命 $\eta$ を各条件で抽出。  
- **解析式**:

$$
\ln[-\ln(1-F)] = \beta \cdot \ln(t) - \beta \cdot \ln(\eta)
$$  

- **意義**: 初期欠陥の寄与を分離しつつ、真性破壊モードを定量化可能。  

**図4a**: TDDB CDFプロット  
<img src="figures/fig4_tddb_cdf.png" alt="TDDB CDF" width="80%">

**図4b**: TDDB ワイブルプロット（フィット直線と $\beta$, $\eta$ を明示）  
<img src="figures/fig4_tddb_weibull.png" alt="TDDB Weibull" width="80%">

### Arrhenius外挿

- **外挿式**
  
$$
\ln(\eta) = \ln(\eta_0) + \frac{E_a}{kT}
$$

- **抽出結果**
  - ストレス電圧 2.3 V: $E_a \approx 0.78\ \mathrm{eV}$
  - ストレス電圧 2.5 V: $E_a \approx 0.84\ \mathrm{eV}$
  - ストレス電圧 2.7 V: $E_a \approx 0.88\ \mathrm{eV}$

- **寿命外挿（Weibullフィットから抽出 η 値）**
  | Stress V | Temp | η (scale) [s] |
  |----------|------|---------------|
  | 2.3 V    | 85 ℃  | $2.7 \times 10^3$ |
  | 2.3 V    | 125 ℃ | $5.1 \times 10^4$ |
  | 2.5 V    | 85 ℃  | $1.5 \times 10^3$ |
  | 2.5 V    | 125 ℃ | $2.8 \times 10^4$ |
  | 2.7 V    | 85 ℃  | $8.2 \times 10^2$ |
  | 2.7 V    | 125 ℃ | $1.5 \times 10^4$ |

- **意義**
  - 実測 η（85 ℃・125 ℃）から Arrhenius プロットを構築。  
  - 活性化エネルギー $E_a \sim 0.8–0.9\ \mathrm{eV}$ は酸素空孔拡散律速モデルと一致。  
  - 任意の動作温度（例: 105 ℃, 150 ℃）での寿命を外挿可能。  

---

## 4.3 Endurance特性（Fatigueを含む）
- **測定条件**: 書込/消去電圧 $\pm 2.5\ \mathrm{V}$、パルス幅 10 µs、繰返し周波数 10 kHz  
- **評価構造**: FeFETセル ($100 \times 100\ \mu\mathrm{m}^2$)  
- **結果**: $10^5$ サイクル以上の動作を確認。しきい値窓 $\Delta V_{\mathrm{th}}$ は約 20–30% 縮小。  
- **フィット式**:  
  $\Delta V_{\mathrm{th}} = 1.12 - 0.05 \cdot \log(\text{cycles})$  
- **意義**: 分極疲労 (Fatigue) の影響を Endurance データに包含し、実使用レベルでの耐久性を定量的に裏付け。  

**図5**: 書換耐久性カーブ（実測点＋外挿線）  
<img src="figures/fig5_endurance_corrected.png" alt="Endurance" width="80%">

---

## 4.4 Retention特性
- **測定条件**: 温度 25 ℃, 85 ℃, 125 ℃ にて保持時間 $\tau$ を測定  
- **評価構造**: FeFETセル  
- **結果**: Arrhenius プロットにより、85 ℃で 10 年以上の保持を予測。  
- **外挿式**:  
  $\ln(\tau) = a \cdot \frac{1}{T} + b$  
- **活性化エネルギー**: $E_{\mathrm{a}} \approx 1.1\ \mathrm{eV}$  
- **意義**: 高温保持データに基づき、長期データ保持信頼性を定量的に証明。  

**図6**: 保持特性（Arrhenius プロット、外挿式と $E_{\mathrm{a}}$ を明示）  
<img src="figures/fig6_retention_withEa.png" alt="Retention" width="80%">
