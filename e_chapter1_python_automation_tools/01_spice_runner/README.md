---
layout: default
title: 01_spice_runner：SPICEシミュレーション自動化スクリプト
---

# 🐍 01_spice_runner：SPICEシミュレーション自動化スクリプト  
**01_spice_runner: Automated SPICE Simulation Scripts**

このフォルダでは、Sky130 の SPICE モデルを使用したトランジスタ特性のシミュレーションを  
Python によって自動化・バッチ実行するためのスクリプトを提供します。  
This folder provides Python-based scripts to automate and batch-run SPICE simulations  
of transistor characteristics using the Sky130 PDK.

---

## 🎯 目的 / Objective

| 日本語 | English |
|--------|---------|
| MOS 特性（Id–Vg）の取得を自動化 | Automate extraction of MOS characteristics (Id–Vg) |
| W/L スケーリングや Vth 変化を簡易に比較 | Easily compare W/L scaling and Vth variation |
| 再現性の高い実験フレームワークを構築 | Build a reproducible experimental framework |

---

## 📁 構成ファイル / File Structure

| 📄 ファイル名 / Filename | 📝 内容 / Description |
|-------------------------|------------------------|
| **[vgid_template.spice](vgid_template.spice)** | プレースホルダ付き SPICE テンプレート（Vth, W, L, Vds）<br>SPICE template with placeholders for Vth, W, L, Vds |
| **[config.json](config.json)** | 実験設定を定義（Sweep条件・サイズなど）<br>Defines simulation conditions such as sweep settings and sizes |
| **[run_spice_sweep.py](run_spice_sweep.py)** | SPICE 実行自動化スクリプト<br>Automates SPICE execution from template |
| **[output/](output/)** | 結果保存フォルダ（CSV/ログ/raw）<br>Directory for output logs, raw files, and CSVs |

---

## ⚙️ 実行方法 / How to Run

以下のコマンドを実行してください：  
Run the following command:

```bash
python3 run_spice_sweep.py
```

※ `ngspice` がインストールされている必要があります。  
`ngspice` must be installed.

📦 Ubuntu 系での導入方法：  
For Ubuntu-based systems:

```bash
sudo apt install ngspice
```

---

## 📘 後続処理 / Post-processing

出力された CSV ファイルは以下のスクリプトでグラフ化できます：  
The generated CSV can be visualized with:

🔗 **[../02_plot_vgid/plot_vgid.py](../02_plot_vgid/plot_vgid.py)**  
→ Id–Vg カーブを可視化（Plot Id–Vg characteristics）

---

## 🔗 参考環境 / Environment Reference

| 項目 / Item | バージョン・設定 / Version / Setting |
|-------------|-------------------------------------|
| **PDK モデル** | `sky130_fd_pr__nfet_01v8` |
| **ngspice バージョン** | **v35 以降推奨 / v35+ recommended** |
| **Python バージョン** | **3.9+**（使用モジュール：`pandas`, `subprocess`, `pathlib`） |

---

## ✍️ 補足 / Notes

- 今後、**Vth, W, L, Vds, 温度, モデルコーナー** の切り替えを動的にサポート予定  
  Future plans include dynamic switching of **Vth, W, L, Vds, temperature, model corners**
- 本スクリプトは以下と連携可能：  
  These scripts are designed to integrate with:

| 🔗 関連フォルダ / Related Folders | 説明 / Description |
|----------------------------------|--------------------|
| **[../03_degradation_model/](../03_degradation_model/)** | 劣化モデル解析との連携<br>For degradation modeling |
| **[../04_openlane_log_parser/](../04_openlane_log_parser/)** | OpenLane ログ解析との連携<br>For OpenLane log parsing |

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
