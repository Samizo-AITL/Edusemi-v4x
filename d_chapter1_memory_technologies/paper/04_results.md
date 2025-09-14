# 4. 実験結果

## 4.1 TZDB特性
- 測定条件：DCランプ印加 (0.1 V/s)、温度 室温〜125 ℃  
- 評価構造：FeCAP (MIM)  
- 絶縁膜破壊電圧 Vbd の分布を抽出し、初期欠陥由来の早期破壊を確認  
- 高温での Vbd シフトは界面欠陥密度の増加と相関  
- 意義：TDDB結果と組み合わせ、**初期故障／偶発故障／真性破壊**を分離評価可能  

**図3**: TZDB分布（破壊電圧ヒストグラムまたはCDF）  
<img src="./figures/fig3_tzdb.png" alt="TZDB" width="80%">

---

## 4.2 TDDB特性
- 測定条件：ゲート電圧ストレス ±2.7 V、温度 85 ℃  
- 評価構造：FeCAP (MIM)  
- Weibull解析により、形状パラメータ β ≈ 1.3、特性寿命 η ≈ 1200 s を抽出  
- 式： ln[-ln(1–F)] = β·ln(t) – β·ln(η)  
- 意義：酸素空孔由来のリークを Al₂O₃ IL (1–2 nm) が抑制していることを確認  

**図4**: TDDBワイブルプロット（外挿式・β・ηを明示）  
<img src="figures/fig4_tddb_withFit_clear.png" alt="TDDB Weibull" width="80%">

---

## 4.3 Endurance特性（Fatigue含む）
- 測定条件：書込/消去電圧 ±2.5 V、パルス幅 10 µs、周波数 10 kHz  
- 評価構造：FeFETセル (100 × 100 µm²)  
- 10⁵サイクル以上で動作を確認、しきい値窓 ΔVth は約20–30%縮小  
- フィット式： ΔVth = 1.12 – 0.05·log(cycles)  
- 意義：分極疲労 (Fatigue) を Endurance データとして包含し、実使用レベルでの耐久性を裏付け  

**図5**: 書換耐久性カーブ（実測点＋外挿線）  
<img src="figures/fig5_endurance_corrected.png" alt="Endurance" width="80%">

---

## 4.4 Retention特性
- 測定条件：温度 25 ℃, 85 ℃, 125 ℃ にて保持時間 τ を測定  
- 評価構造：FeFETセル  
- Arrhenius 外挿により、85 ℃で10年以上の保持を予測  
- 外挿式： ln(τ) = a·(1/T) + b  
- 活性化エネルギー： Ea ≈ 1.1 eV  
- 意義：長期データ保持信頼性を定量的に証明  

**図6**: 保持特性（Arrheniusプロット、外挿式とEa明示）  
<img src="figures/fig6_retention_withEa.png" alt="Retention" width="80%">
