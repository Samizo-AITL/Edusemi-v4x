---
layout: default
title: 02_plot_vgid - Vg–Id 特性の可視化
---

# 📘 02_plot_vgid - Vg–Id 特性の可視化  
**Visualizing Vg–Id Characteristics from SPICE Output**

---

## 📄 概要｜Overview

このフォルダでは、前章で取得した SPICE ログファイル（`.log`）を Python で読み取り、  
**nMOS / pMOS の Vg–Id 特性カーブを可視化**するツールを提供します。  
基本的な `matplotlib` の機能のみを用い、MOSFET の電気特性を**教育目的で直感的に理解**できる構成としています。

This folder provides a tool to **visualize Vg–Id characteristics** of nMOS and pMOS devices,  
by reading `.log` files generated from SPICE simulations. It is designed for **educational purposes**  
using only basic `matplotlib` functionality to promote intuitive understanding of device behavior.

---

## 📁 フォルダ構成｜Folder Structure

| ファイル / フォルダ名 | 内容｜Description |
|------------------------|----------------------------------------------------------|
| [`plot/plot_vgid.py`](./plot/plot_vgid.py) | Vg–Id 特性を描画する Python スクリプト<br>Python script to plot Vg–Id curves |
| [`./output/`](./output/) | `.log` ファイルを保存するフォルダ（実行結果出力）<br>Directory for `.log` files generated from simulation |

---

## 🔧 前提環境｜Requirements

| 項目｜Item | 内容｜Details |
|------------|------------------------|
| 🐍 **Python バージョン**<br>Python Version | Python 3.x |
| 📦 **必要ライブラリ**<br>Required Libraries | `matplotlib` |

**インストール例｜Example Installation:**

```bash
pip install matplotlib
```

---

## 🚀 実行方法｜How to Run

### 🔹 基本的な実行

```bash
python plot_vgid.py
```

### 🔹 引数で `.log` ファイルを指定

```bash
python plot_vgid.py ../output/nfet_W1.0_L0.15.log
```

### 🔹 複数ファイルを一括描画（ワイルドカード対応）

```bash
python plot_vgid.py ../output/*.log
```

---

## 📈 出力例｜Example Output

プロットされるグラフ形式：

| 項目｜Item | 内容｜Details |
|--------|-----------------------------|
| **X軸｜X-axis** | ゲート電圧 Vg [V] |
| **Y軸｜Y-axis** | ドレイン電流 Id [μA] |
| **補助線｜Guides** | 0μA ラインの水平線付き |
| **表示方法｜Display** | nMOS / pMOS 両方の特性を同一グラフに重ねて表示 |

---

## 📝 補足事項｜Notes

- `.log` ファイルは `ngspice` 実行後に `output/` フォルダ内に生成されます（例：`../01_setup_sky130_model/`）。
- デバイス種別（nMOS / pMOS）はファイル名または中身から自動識別されます。
- スクリプトは `matplotlib` のみで構成されており、外部依存はありません。

---

## 🔗 関連リンク｜Related Links

| 項目｜Item | リンク｜Link |
|--------|-------------------------|
| 🛠️ SPICEモデル準備 | [../01_setup_sky130_model/](../01_setup_sky130_model/) |
| 📈 SPICE出力付き実験フォルダ | [../02_idvg_experiment/](../02_idvg_experiment/) |
| 💾 Sky130 PDK GitHub | [https://github.com/google/skywater-pdk](https://github.com/google/skywater-pdk) |
| 📊 matplotlib公式 | [https://matplotlib.org/](https://matplotlib.org/) |

---

## 🔙 戻る｜Back to Chapter Top

[🏠 実践編 第2章 トップへ戻る｜Back to `e_chapter2_sky130_experiments` Top](../README.md)
