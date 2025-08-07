---
layout: default
title: 05_report_template：自動レポート出力テンプレート
---

# 📝 05_report_template：自動レポート出力テンプレート  
**05_report_template: Auto-Generated Reports for Simulation and Design Evaluation**

このフォルダでは、`SPICE` や `OpenLane` のシミュレーション結果をもとに、  
**MarkdownやJupyter Notebookで設計・評価レポートを自動生成するテンプレート群**を提供します。  
This folder provides templates to auto-generate evaluation reports (Markdown/Jupyter) from simulation results like SPICE and OpenLane.

Python解析と可視化をそのまま教育・プレゼン・報告に活用可能です。

---

## 📄 テンプレート一覧 / Template List

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`report_template.ipynb`](report_template.ipynb) | Vg–IdやVth・BTI・TDDBなどのグラフ付きJupyterレポート |
| [`report_template.md`](report_template.md) | MarkdownベースのCLI向けレポートテンプレート |
| [`auto_report_generator.py`](auto_report_generator.py) | CSV・グラフを読み取りMarkdownまたはNotebookに自動挿入するスクリプト |

※テンプレートファイルは順次整備予定です。

---

## 🧰 活用例 / Use Cases

- `output/` フォルダを走査し、特性グラフと計算値をNotebookでまとめてレポート化  
- 劣化モデル（BTI/TDDB）の結果を時系列で挿入し、説明を可視化  
- OpenLaneの設計Runごとの遅延・面積・電力をグラフで比較し傾向を記述

---

## 📦 必要パッケージ / Required Packages

```bash
pip install jupyter pandas matplotlib
```

---

## 🎓 教育的意義 / Educational Purpose

- Python解析 → 結果整形 → レポート作成 の一貫自動化体験  
- Jupyter Notebook により **手を動かしながらのレポート作成** が可能  
- Markdown形式は **GitHubや印刷向けに最適化可能**

---

## 🔗 関連リンク / Related Links

| フォルダ | 説明 |
|---------|------|
| [`../02_plot_vgid/`](../02_plot_vgid/) | SPICE特性の可視化スクリプト |
| [`../04_openlane_log_parser/`](../04_openlane_log_parser/) | OpenLaneログの解析＋グラフ出力 |
| [`../../e_chapter1_python_automation_tools/`](../../e_chapter1_python_automation_tools/) | 実践編 第1章：Python自動化ツール教材 |

---

## 🚀 今後の拡張案 / Future Enhancements

- [`nbconvert`](https://nbconvert.readthedocs.io/) による PDF レポート自動変換対応  
- `auto_report_generator.py` の軽量版CLI作成（CSV＋グラフ自動整形）  
- GitHub Actions での定期レポート出力自動化  

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
