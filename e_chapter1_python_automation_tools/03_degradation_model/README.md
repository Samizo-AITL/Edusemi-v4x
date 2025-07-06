# 📉 03_degradation_model：信頼性モデルによる劣化予測

本フォルダでは、MOSトランジスタにおける代表的な信頼性劣化現象である BTI（Bias Temperature Instability）や TDDB（Time Dependent Dielectric Breakdown）の理論モデルに基づき、**しきい値電圧（Vth）やリーク電流の劣化挙動をPythonで計算・可視化**するツールを提供します。

---

## 📄 内容と目的

| モデル | 対象現象 | 代表式・特徴 |
|--------|-----------|--------------|
| BTIモデル | Vthのドリフト | ΔVth ∝ (t)^n・exp(-Ea/kT) |
| TDDBモデル | 絶縁破壊寿命 | Weibull分布やEモデルによる寿命予測 |

---

## 🧪 使用例（想定スクリプト）

```bash
python3 plot_bti_model.py     # ΔVth vs 時間のプロット
python3 plot_tddb_model.py    # 寿命 vs 電界強度 のプロット
```

## 🔧 スクリプト依存
Python 3.8+
matplotlib
numpy

インストール例：

pip install numpy matplotlib

## 🔗 関連リンク
	•	../01_spice_runner/：初期特性の取得（Vthなど）
	•	../02_plot_vgid/：SPICEログからの特性抽出
	•	../../e_chapter2_sky130_experiments/：Sky130実験と劣化評価への応用
 
## 📁 予定スクリプト例（今後実装）

| スクリプト名 | 概要 |
|--------------|------|
| `plot_bti_model.py` | BTI（Bias Temperature Instability）によるしきい値電圧 ΔVth の時間変化をプロット。指数則 ΔVth ∝ (t)^n・exp(-Ea/kT) に基づく |
| `plot_tddb_model.py` | TDDB（Time-Dependent Dielectric Breakdown）の寿命予測を、Eモデル・Weibullモデルを用いて可視化。MOSゲート酸化膜の絶縁破壊寿命を推定 |

---

## 🎯 教育的意義

- 信頼性設計の基礎モデルを **定量的に体験**
- **Vthの劣化挙動**と**寿命分布の傾向**を視覚的に把握
- モデルパラメータ（温度T、時間t、電界Eなど）の感度分析が可能
- 設計マージンと製品寿命評価への理解を深める演習教材として活用可能

---

## 📌 備考

- 本スクリプト群は **教育目的の疑似モデル** です。
- 実際の製品評価には、詳細な物理モデル・実測データ・信頼性試験が必要です。
- 各モデル式の導出・背景は、教材別章で解説予定です。
