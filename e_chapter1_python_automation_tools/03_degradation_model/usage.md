# 使用方法：03_degradation_model

本フォルダでは、`MOSトランジスタ` の信頼性劣化（`BTI` / `TDDB`）に関するモデルを `Python` で数式化・可視化します。  
電圧・温度・動作時間などを変数とした簡易的な寿命予測モデルの構築に利用できます。

---

## 🔧 前提環境

- `Python 3.9+`
- `numpy`
- `matplotlib`

インストール例：

`pip install numpy matplotlib`

---

## 📁 構成ファイル一覧

| ファイル名 | 説明 |
|------------|------|
| `bti_model.py` | `NBTI`（負バイアス温度不安定性）モデルの定式化とグラフ描画 |
| `tddb_model.py` | `TDDB`（絶縁破壊）寿命推定モデルの描画スクリプト |
| `common_plot.py` | 軸設定・描画スタイルなどの共通関数定義 |
| `figures/` | 出力された劣化特性グラフの保存先（自動生成されます） |

---

## 🚀 実行方法

### 1. 劣化モデルの描画（例：BTI）

`python3 bti_model.py`

- 温度、印加電圧、動作時間などを変数とし、しきい値電圧の変化 `ΔVth(t)` を可視化します。
- 結果は `figures/bti_vth_shift.png` に保存されます。

### 2. 絶縁破壊寿命の可視化（例：TDDB）

`python3 tddb_model.py`

- 酸化膜厚や印加電界に基づき、寿命予測曲線を表示します。

---

## 📈 出力例

```text
figures/
├── bti_vth_shift.png
├── tddb_lifetime_plot.png
```

## 🔗 関連ツール
	•	02_plot_vgid/：初期特性との比較可視化
	•	05_report_template/：グラフ出力の自動挿入に対応

---

## 📝 備考
	•	本モデルは教育用の簡易式（例：ΔVth ∝ t^n）に基づいています。
	•	実際の信頼性試験データやJEITA / JEDEC標準との整合は別途検討が必要です。
	•	出力画像形式は matplotlib.pyplot.savefig() により変更可能です（PNG / PDFなど）。

---

[🐍 実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
