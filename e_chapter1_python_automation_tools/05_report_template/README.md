# 📝 05_report_template：自動レポート出力テンプレート

本フォルダでは、SPICEやOpenLaneのシミュレーション結果をもとに、**MarkdownやJupyter Notebookで設計・評価レポートを自動生成するためのテンプレート群**を提供します。

Pythonによる解析結果を、そのまま教育・プレゼン・報告に使える形で記録・出力できます。

---

## 📄 テンプレート一覧（予定）

| ファイル名 | 説明 |
|------------|------|
| `report_template.ipynb` | Jupyter Notebook形式：Vg–Id特性グラフ、Vth抽出、信頼性プロットなどを可視化しながら報告可能 |
| `report_template.md` | Markdown形式：CLIやテキストベースのレポート出力用テンプレート |
| `auto_report_generator.py` | 各結果（CSV/グラフ）を自動挿入してレポートを構成するスクリプト例 |

---

## 🧰 活用例

- 実験毎の `output/` フォルダを読み取り、特性グラフ＋計算結果を1つのノートにまとめる
- BTIやTDDBの劣化プロットを時系列で並べ、劣化傾向を説明
- OpenLaneの各Run結果を比較し、遅延/面積の設計傾向を視覚化

---

## 📦 必要なパッケージ

```bash
pip install jupyter pandas matplotlib
```

## 📌 教育的意義
	•	Python → 解析 → レポート生成の 一貫した自動化体験
	•	Jupyter形式により、手を動かしながら理解を深める
	•	Markdownにより、GitHubなどでの成果共有や公開が容易

---

## 🔗 関連リンク
	•	../02_plot_vgid/：SPICE特性の可視化結果
	•	../04_openlane_log_parser/：OpenLaneログのCSV出力
	•	../../e_chapter1_python_automation_tools/：実践編 第1章（全体構成）

---

## ✅ 今後の拡張案
	•	nbconvert によるPDF自動変換
	•	グラフやCSVを自動で読み込む「軽量レポートジェネレータ」
	•	GitHub Actionsと連携した定期レポート生成

---
