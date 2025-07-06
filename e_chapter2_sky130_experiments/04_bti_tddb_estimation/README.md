# 🧪 BTI・TDDB 劣化モデルの数式可視化

本章では、MOSトランジスタの信頼性課題である **BTI（Bias Temperature Instability）** および  
**TDDB（Time-Dependent Dielectric Breakdown）** に関する基本モデルを Python により可視化します。

---

## 🎯 目的

- 劣化現象を数学モデルとして理解する
- 時間、温度、電界と寿命の関係を直感的に掴む
- SPICEでは扱いづらい「時間軸の劣化」を可視化する

---

## 🔧 スクリプト構成

| ファイル名 | 説明 |
|------------|------|
| `plot_bti_model.py` | BTIによるΔVthの変化（時間・温度依存）をプロット |
| `plot_tddb_model.py` | TDDBに基づくMTTF（寿命）を電界強度で可視化 |
| `model_constants.py` | モデル定数（Ea、n、温度、ボルツマン定数など）を一元管理 |
| `output/` | 出力図の保存先ディレクトリ（PNG形式） |

---

## 📈 出力グラフ例

### BTI劣化（ΔVth vs 時間）

```bash
python3 plot_bti_model.py
```

出力：
- ΔVthの時間依存変化（log-log）
- 温度別に複数プロット

![BTI劣化グラフ](output/bti_degradation.png)

---

### TDDBモデル（MTTF vs 電界強度）

```bash
python3 plot_tddb_model.py
```

出力：
- 電界強度Eに対する寿命の変化（log表示）
- 指数モデル（Eモデル）とパワーモデルの比較

![TDDBモデルグラフ](output/tddb_models.png)

---

## 🧠 教育的意義

- 劣化メカニズムを **時間と温度・電界の関数** として理解
- 実設計における **信頼性マージン** や **寿命設計** の考え方を体験
- 各種モデルの **式・グラフ・設計インパクト** の相関を実感

---

## 🔗 関連リンク

- [Sky130実験とSPICE特性評価（第2章）](../README.md)
- [OpenLaneによるデジタル設計実習（第3章）](../../e_chapter3_openlane_practice/README.md)

---

## 📦 必要なPythonパッケージ

```bash
pip install numpy matplotlib
```

---

## 📚 補足：モデル式（理論背景）

### 🔸 BTIモデル

```text
ΔVth(t) = A × t^n × exp(-Ea / kT)
```

- A：スケーリング定数  
- n：時間係数（0.1〜0.3）  
- Ea：活性化エネルギー [eV]  
- k：ボルツマン定数（8.617e-5 eV/K）  
- T：絶対温度 [K]  

---

### 🔸 TDDBモデル

```text
MTTF ∝ exp(γ × E)      （指数モデル）  
MTTF ∝ 1 / E^n         （フィールドパワーモデル）
```

- E：酸化膜電界（V/nm または MV/cm）  
- γ：感度係数（材料・膜厚依存）  
- n：指数（2〜4）

