---
layout: default
title: plot：Sky130 SPICE出力の可視化ツール
---

# 📊 plot：Sky130 SPICE出力の可視化ツール  
**Plotting Tool for Sky130 SPICE Output**

---

## 📘 概要｜Overview

本フォルダには、Sky130デバイスの `.spice` 出力ログ（例：Id–Vg特性）を読み取り、  
**Python（matplotlib）でグラフ化するスクリプト**を格納しています。  
This folder contains scripts for **visualizing SPICE simulation results** using `matplotlib`.

---

## 📁 フォルダ構成｜Folder Contents

| ファイル名 | 説明 |
|------------|------|
| `plot_vgid.py` | `.log` ファイルから Vg–Id 特性を抽出して描画するPythonスクリプト |

---

## ⚙️ 実行方法｜Usage

ターミナルで以下を実行してください：

```bash
python3 plot_vgid.py
```

- 入力：`nfet_vgid.log`, `pfet_vgid.log`（例：`01_setup_sky130_model/output/` など）
- 出力：`Vg–Id` 特性グラフ（PNGまたはPDF形式）

---

## 📌 依存ライブラリ｜Dependencies

- `matplotlib`
- `pandas`

インストール（未導入の場合）：

```bash
pip install matplotlib pandas
```

---

## 📈 出力例｜Example Output

- nMOS / pMOS の Id–Vg 曲線（横軸：$V_{GS}$、縦軸：$I_D$）
- グラフは自動保存され、レポート用に使用可能です

---

## 🔗 関連フォルダ・スクリプト

- [`../01_setup_sky130_model/`](../01_setup_sky130_model/) — SPICEモデル準備とログ生成
- [`../02_idvg_experiment/`](../02_idvg_experiment/) — Vg–Id 特性の実験設定
- [`../05_data_summary/`](../05_data_summary/) — レポートへの統合

---

## 🔙 実践編 第2章 READMEに戻る  
[🏠 `e_chapter2_sky130_experiments` トップへ戻る](../README.md)
