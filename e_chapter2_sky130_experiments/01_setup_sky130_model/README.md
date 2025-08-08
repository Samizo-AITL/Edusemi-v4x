---
layout: default
title: 01_setup_sky130_model - Sky130モデル準備と初期動作確認
---

---

# ⚙️ 01_setup_sky130_model  
**Sky130 MOS Model Setup and Initial Simulation**

---

## 📘 概要｜Overview

本フォルダでは、Sky130 PDK に含まれる **MOSトランジスタのSPICEモデルをセットアップ**し、  
`ngspice` を用いた **最小回路の動作確認と可視化** を行います。

This folder provides an initial setup of **MOSFET SPICE models from the Sky130 PDK**,  
followed by simple simulations using `ngspice` to **verify and visualize device behavior**.

---

## 📁 フォルダ構成｜Folder Contents

| ファイル名｜Filename | 説明｜Description |
|----------------------|--------------------------------------------------|
| [`nfet_vgid.spice`](./nfet_vgid.spice) | `nfet_01v8` の Vg–Id 特性を得る回路例<br>Example circuit to obtain Vg–Id for `nfet_01v8` |
| [`pfet_vgid.spice`](./pfet_vgid.spice) | `pfet_01v8` の特性評価用回路<br>SPICE setup for `pfet_01v8` |
| [`sky130_model_paths.inc`](./sky130_model_paths.inc) | `.lib` 定義を記述した Sky130 PDK 用 include ファイル<br>Includes PDK model paths |
| [`run_check.sh`](./run_check.sh) | `ngspice` による動作チェック用シェルスクリプト<br>Shell script to verify SPICE execution |
| [`output/`](./output/) | `.raw` や `.log` 出力を格納（自動生成）<br>Auto-generated SPICE output directory |

---

## 🔧 前提条件｜Requirements

| 項目｜Item | 内容｜Details |
|--------|---------------------------------------------|
| Sky130 PDK | [GitHub リンク](https://github.com/google/skywater-pdk)<br>例: `~/pdks/sky130A/` に導入 |
| ngspice | バージョン `35+` 推奨<br>[ngspice 公式サイト](http://ngspice.sourceforge.net/) |

---

## 🚀 実行方法｜How to Run

### 1. `.spice` ファイルに `.lib` パスを設定  
**Set `.lib` path inside your .spice file**

```spice
.include "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice"
.lib "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice" tt
```

- `tt` は typical corner 条件です（**typical-typical**）

---

### 2. `ngspice` によるシミュレーション実行  
**Run simulation via terminal**

```bash
ngspice nfet_vgid.spice
```

- 実行後、`output/` フォルダに `.raw` `.log` が生成されます  
- Linux環境で `run_check.sh` を使って一括実行も可能です

---

## 📈 結果の確認｜Check Simulation Output

- `ngspice` のグラフ表示機能で Vg–Id 特性を確認できます  
- `.log` ファイルにはスイープ結果がテキスト出力されます  
- **Python + matplotlib による可視化ツールは → [`plot/`](../plot/)** にあります

---

## 📝 備考｜Notes

- Sky130の基本素子は `sky130_fd_pr__nfet_01v8`, `pfet_01v8` を使用  
- `.meas` や `.param` を使った自動抽出は後続フォルダで導入  
- 本フォルダは **SPICE × 教育実験** の基礎出発点です

---

## 🔗 関連リンク｜References

- 🌐 [Sky130 PDK GitHub](https://github.com/google/skywater-pdk)  
- 🌐 [ngspice Official Site](http://ngspice.sourceforge.net/)  
- 📁 [02_plot_vgid/](../02_plot_vgid/) — 出力ログの Python 可視化へ

---

## 🔙 実践編 第2章 トップに戻る｜Back to Practical Chapter 2

📘 **[戻る → 実践編 第2章：Sky130実験とSPICE特性評価](../README.md)**
