---
layout: default
title: 02_plot_vgid：SPICEログのVg–Id特性可視化
---

# 📈 02_plot_vgid：SPICEログのVg–Id特性可視化  
**02_plot_vgid: Visualization of Vg–Id Characteristics from SPICE Logs**

このフォルダは、Sky130 PDK を用いた `.spice` シミュレーション結果（`.log`ファイル）から、  
ゲート電圧 Vg に対するドレイン電流 Id の特性（Vg–Id カーブ）を描画する Python スクリプトを格納しています。  
This folder contains a Python script that reads `.log` files generated from SPICE simulations and plots the Vg–Id curve.

---

## 📄 スクリプト概要 / Script Overview

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| [`plot_vgid.py`](plot_vgid.py) | `.log` ファイルから Vg–Id 特性を抽出しプロット<br>Reads `.log` files and plots the Vg–Id characteristics |

---

## 🔧 前提環境 / Requirements

以下の環境が必要です：  
The following environment is required:

| 項目 / Item | バージョン・内容 / Details |
|-------------|-----------------------------|
| Python | 3.8 以上 / 3.8 or later |
| ライブラリ | `matplotlib`（グラフ描画） |

🔽 インストール例 / Installation:

```bash
pip install matplotlib
```

---

## 🚀 使用方法 / How to Use

1️⃣ `.spice` シミュレーションを実行し、`output/` フォルダに `.log` ファイルを出力しておく  
Run `.spice` simulation and ensure `.log` files are saved in `output/`

2️⃣ 以下のコマンドでプロットを生成：  
Run the following command:

```bash
python3 plot_vgid.py output/nfet_W1.0_L0.15.log
```

📂 複数ファイルを一括プロットする場合：  
To plot multiple logs at once:

```bash
python3 plot_vgid.py output/*.log
```

プロットはターミナルに表示され、同時に `figures/` に保存されます。  
Plots are shown interactively and also saved into the `figures/` folder.

---

## 📊 出力プロット例 / Example Plot

- 📏 **横軸 / X-axis**：ゲート電圧 Vg [V] / Gate Voltage Vg [V]  
- 🔌 **縦軸 / Y-axis**：ドレイン電流 Id [A] / Drain Current Id [A]  
- 🏷️ **凡例 / Legend**：ファイル名（例：`nfet_W1.0_L0.15`）

---

## 📂 ログファイル形式 / Log File Format Example

SPICE `.log` ファイルの一例：  
Example `.log` file output from SPICE:

```
V(G)         I(VD)
0.000000e+00 0.000000e+00
2.000000e-02 1.153210e-06
4.000000e-02 2.885102e-06
...
```

この形式の2列データを読み取り、プロットを生成します。  
The script reads this two-column format and plots Vg vs Id.

---

## 🔗 関連リンク / Related Links

| フォルダ / Folder | 機能 / Description |
|------------------|---------------------|
| [`../01_spice_runner/`](../01_spice_runner/) | SPICE シミュレーションの自動実行<br>Automated SPICE execution |
| [`../../e_chapter2_sky130_experiments/`](../../e_chapter2_sky130_experiments/) | Sky130 実験と特性評価教材<br>Sky130 experiments and evaluation materials |

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
