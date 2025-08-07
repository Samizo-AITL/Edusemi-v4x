# 使用方法：05_report_template

本フォルダでは、各章で得られた図表や数値データをレポートとしてまとめるテンプレートを提供します。  
`Jupyter Notebook` 形式や `Markdown` 自動生成スクリプトを用いて、教育レポートや技術記録の自動化を支援します。

---

## 🔧 前提環境

- `Python 3.9+`
- `jupyter`（Notebook 実行用）
- `nbconvert`（PDF / HTML 出力用）
- `matplotlib`, `pandas`（グラフ出力処理用）

インストール例：

`pip install jupyter nbconvert matplotlib pandas`

---

## 📁 構成ファイル一覧

| ファイル名 | 説明 |
|------------|------|
| `template_report.ipynb` | Notebook形式の基本テンプレート。実行結果と図を含むレポート出力が可能 |
| `insert_results.py` | 他章のCSVやPNGを読み込み、自動的にMarkdown形式のレポートに整形 |
| `images/` | グラフやデバイス構成図などの図表フォルダ（自動または手動で追加） |
| `report_output/` | Notebook実行やMarkdown生成の結果フォルダ |

---

## 🚀 実行方法

### 1. Notebook を起動して編集

`jupyter notebook template_report.ipynb`

- セルに分析結果を貼り付けたり、Pythonコードを実行してグラフを挿入できます。

### 2. Markdown or PDF への変換（必要に応じて）

`jupyter nbconvert template_report.ipynb --to pdf`

または

`python3 insert_results.py`

- 各章で生成されたグラフやCSVを読み取り、`report_output/auto_report.md` に自動整形出力。

---

## 📈 出力例

```text
report_output/
├── auto_report.md
├── auto_report.pdf
└── embedded_figures/
    ├── VgId_W1.0_L0.15.png
    ├── bti_vth_shift.png
    └── power_comparison.png
```

## 🔗 関連ツール
	•	01_spice_runner/：SPICE実行結果の図表化
	•	03_degradation_model/：寿命予測グラフ
	•	04_openlane_log_parser/：面積・電力の自動分析

---

## 📝 備考
	•	Notebook は .ipynb 形式で配布。カスタマイズにより大学課題や研究用途にも適応可能。
	•	自動挿入スクリプト insert_results.py は、指定ディレクトリの .csv や .png を動的に挿入します。
	•	複数の結果を一括で整形・統合することが可能です。

---

[🐍 実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
