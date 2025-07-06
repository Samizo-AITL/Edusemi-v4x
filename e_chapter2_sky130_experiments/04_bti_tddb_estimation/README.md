# 🧪 04_BTI・TDDB 劣化モデルの数式可視化

本ディレクトリでは、MOSトランジスタの信頼性課題である **BTI（Bias Temperature Instability）** や  
**TDDB（Time-Dependent Dielectric Breakdown）** に関する基本モデルを Python により数式評価・グラフ化します。

---

## 📚 目的

- MOS劣化の基礎方程式（寿命予測式）を理解する
- 時間、電圧、温度による影響を定量的に見る
- 設計マージンや信頼性試験への理解を深める

---

## 🔧 モデル例

### 🔸 BTIモデル（しきい値変化 ΔVth）

```text
ΔVth(t) = A × (t)^n × exp(-Ea / kT)
```

	•	t：ストレス時間
	•	n：時間依存係数（0.1〜0.3）
	•	Ea：活性化エネルギー（例：0.15〜0.2 eV）
	•	T：絶対温度（K）
	•	k：ボルツマン定数（8.617e-5 eV/K）

## 🔸 TDDBモデル（寿命予測）
```
MTTF ∝ exp(γ × E)       （Eモデル）
MTTF ∝ 1 / E^n          （フィールドパワーモデル）
```
	•	E：酸化膜電界（V/nm）
	•	γ：感度係数（材料依存）
	•	n：指数（2〜4）

## 🛠 スクリプト構成
```
04_bti_tddb_estimation/
├── plot_bti_model.py      ... ΔVth(t) を時間軸で可視化
├── plot_tddb_model.py     ... MTTF vs 電界E を複数モデルで可視化
├── model_constants.py     ... 共通パラメータ（Ea, k, 温度など）
└── output/                ... PNG出力など
```

## 📊 実行例
```
python3 plot_bti_model.py
python3 plot_tddb_model.py
```

それぞれ以下のようなグラフを出力：
```
	•	BTI：しきい値電圧 ΔVth vs 時間（log-logスケール）
	•	TDDB：MTTF vs 酸化膜電界E（Weibull or Eモデル）
```

---

## 💡 教育的意義
	•	劣化現象を 定量モデル として体験
	•	ストレス条件による寿命変動の大きさを直感的に理解
	•	設計時マージン設定・デバイス寿命設計の理解に貢献

---

## 🔗 関連章リンク
	•	第2章：Sky130実験とSPICE特性評価
	•	第3章：OpenLaneによるデジタル設計実習

---

