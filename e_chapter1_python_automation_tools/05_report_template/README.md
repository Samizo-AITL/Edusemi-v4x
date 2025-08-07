---
layout: default
title: 使用方法：05_report_template
---

# 📝 使用方法：05_report_template  
**How to Use: 05_report_template – Automated Reporting Templates**

本フォルダでは、各章で得られた図表や数値データをレポートとしてまとめるテンプレートを提供します。  
`Jupyter Notebook` 形式や `Markdown` 自動生成スクリプトを用いて、**教育レポートや技術記録の自動化を支援**します。  
This folder provides tools to automatically compile simulation results into technical or educational reports using Jupyter or Markdown.

---

## 🔧 前提環境 / Requirements

| 項目 / Item | 推奨バージョン / Recommended |
|-------------|-------------------------------|
| Python | 3.9+ |
| 使用ライブラリ / Required | `jupyter`, `nbconvert`, `matplotlib`, `pandas` |

📦 インストール例 / Install Example:

```bash
pip install jupyter nbconvert matplotlib pandas
```

---

## 📁 構成ファイル一覧 / File Structure

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`template_report.ipynb`](template_report.ipynb) | Notebook形式のテンプレート。図付きレポートを作成可能<br>Jupyter Notebook template with figures |
| [`insert_results.py`](insert_results.py) | CSVやPNGをMarkdownへ自動整形するスクリプト<br>Script to auto-generate Markdown report |
| `images/` | グラフ・図表の格納用フォルダ（手動 or 自動）<br>Folder for images |
| `report_output/` | MarkdownやPDFの出力先フォルダ<br>Exported reports directory |

---

## 🚀 使用方法 / How to Run

### 1️⃣ Notebook を使う場合（対話形式）

```bash
jupyter notebook template_report.ipynb
```

- セルを順に実行してレポートを作成  
- 画像・表・計算結果を自由に挿入可能

---

### 2️⃣ Markdown / PDF 形式で自動出力

#### 自動Markdownレポート出力（スクリプト）：

```bash
python3 insert_results.py
```

#### PDF変換（Notebook → PDF）：

```bash
jupyter nbconvert template_report.ipynb --to pdf
```

📁 出力フォルダ例：

```text
report_output/
├── auto_report.md
├── auto_report.pdf
└── embedded_figures/
    ├── VgId_W1.0_L0.15.png
    ├── bti_vth_shift.png
    └── power_comparison.png
```

---

## 🎯 教育的意義 / Educational Purpose

- Pythonによる設計結果の **自動解析〜レポート出力** を一貫体験  
- Notebook形式により **インタラクティブな学習** が可能  
- Markdown形式は **GitHub提出や共有、PDF化にも便利**

---

## 🔗 関連ツール / Related Tools

| フォルダ | 機能概要 |
|---------|----------|
| [`../01_spice_runner/`](../01_spice_runner/) | SPICE実行とログ生成 |
| [`../03_degradation_model/`](../03_degradation_model/) | 信頼性モデル出力（BTI, TDDB） |
| [`../04_openlane_log_parser/`](../04_openlane_log_parser/) | 面積・電力などのレポート自動生成 |

---

## 📝 備考 / Notes

- Notebook形式は `.ipynb` に対応し、Google Colab などでも活用可能  
- `insert_results.py` は指定ディレクトリの `.csv` や `.png` を自動抽出・整形  
- カスタマイズにより研究レポート、学会資料にも応用可能です

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
