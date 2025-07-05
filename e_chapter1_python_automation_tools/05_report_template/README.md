# 05_report_template：レポート生成テンプレート

このフォルダでは、SPICE・OpenLane・信頼性モデルで得られた実験結果を  
自動的にまとめ、MarkdownやJupyter形式でレポート出力できるテンプレートを提供します。

## 📌 主な用途

- 教育実習レポートの半自動生成
- `Zenn`や`GitHub Pages`向けのMarkdown出力
- Jupyter Notebookでの対話式レポート

## 📄 想定テンプレート形式

- `report_template.md`
- `report_filler.py`（結果埋め込みスクリプト）
- `report.ipynb`（ノートブック形式）

## 🐍 使用予定ライブラリ

- `jinja2`（Markdown展開）
- `nbformat` / `markdown`
