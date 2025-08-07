---
layout: default
title: 使用方法：01_spice_runner
---

# 🧪 使用方法：01_spice_runner  
**How to Use: 01_spice_runner**

このフォルダでは、`Python` スクリプトにより `ngspice` を自動制御し、`Vg–Id` 特性のシミュレーションを一括実行します。  
パラメータスイープやデバイスサイズの違いを簡単に切り替えられる構成になっています。  
This folder uses a Python script to automate `ngspice` for batch simulation of `Vg–Id` characteristics,  
allowing easy switching between parameter sweeps and device dimensions.

---

## 🔧 前提環境 / Requirements

以下の環境が整っていることを推奨します：  
The following environment is recommended:

| 項目 / Item | 推奨設定 / Recommended |
|-------------|------------------------|
| Python | 3.9+ |
| SPICE | `ngspice` v35+ |
| PDK | `sky130_fd_pr__nfet_01v8.spice` |
| 使用ライブラリ | `json`, `subprocess`, `pathlib` |

> 📦 必要に応じて `requirements.txt` や `environment.yml` を活用してください。  
> Use `requirements.txt` or `environment.yml` as needed.

---

## 📁 構成ファイル一覧 / File Structure

| ファイル名 / Filename | 説明 / Description |
|------------------------|---------------------|
| `run_spice_sweep.py` | メインスクリプト：テンプレート展開＋SPICE 実行<br>Main script: expands template and runs ngspice |
| `vgid_template.spice` | プレースホルダ形式の SPICE テンプレート<br>SPICE template with placeholders |
| `config.json` | パラメータ設定ファイル（W/L/VDS 等）<br>Parameter config file |
| `output/` | 出力ログ・生成ファイル格納先<br>Output folder for logs and .spice files |

---

## 🚀 実行方法 / How to Run

### 1️⃣ 準備 / Setup

テンプレート・設定ファイルを同一フォルダに設置し、出力フォルダを作成します：  
Place template and config files in the same folder and create the output directory:

```bash
mkdir -p output
```

---

### 2️⃣ スクリプト実行 / Run Script

以下のコマンドで実行します：  
Run the script with:

```bash
python3 run_spice_sweep.py
```

この実行により以下の処理が行われます：  
The following actions will be performed:

- テンプレートに対し W/L 組み合わせごとの `.spice` ファイル生成  
  Generates `.spice` files based on W/L combinations  
- `ngspice` によるシミュレーション実行  
  Runs ngspice simulations  
- `.log` ファイルとして結果出力（`output/`内）  
  Stores results as `.log` files in `output/`

---

## 📂 出力例 / Output Example

```text
output/
├── vgid_W1.0_L0.15.spice
├── vgid_W1.0_L0.15.log
├── vgid_W2.0_L0.3.spice
└── vgid_W2.0_L0.3.log
```

※ `.log` ファイルは、次ステップ `02_plot_vgid/` にて可視化されます。  
These `.log` files can be parsed and visualized in the next step: `02_plot_vgid/`.

---

## 🔗 関連ツール / Related Tools

| フォルダ / Folder | 機能 / Function |
|------------------|------------------|
| `02_plot_vgid/` | SPICE ログの可視化（matplotlib）<br>Visualization of SPICE logs |
| `03_degradation_model/` | BTI・TDDB 劣化モデルとの連携解析<br>Degradation model integration |
| `05_report_template/` | レポート出力支援テンプレート（Jupyter / Markdown）<br>Report generation template |

---

## 📝 備考 / Notes

- `vgid_template.spice` 内で `sky130_fd_pr__nfet_01v8.spice` を `.include` しておく必要があります  
  Ensure `.include "sky130_fd_pr__nfet_01v8.spice"` is present in the template  
- `{{W}}`, `{{L}}`, `{{VDS}}` などの変数は Python によってテンプレートに挿入されます  
  These placeholders are dynamically inserted by Python  
- `.dc` ステートメントにより Vgs を 0〜1.2V、ステップ0.01V でスイープします  
  `.dc Vgs 0 1.2 0.01` is defined in the template

---

## 🔙 戻る / Back to Top

📂 [実践編 第1章：Python自動化ツール群トップに戻る / Back to Chapter 01 Top](../README.md)
