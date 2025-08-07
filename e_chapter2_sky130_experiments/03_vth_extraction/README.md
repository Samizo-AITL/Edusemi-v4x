---
layout: default
title: 03_vth_extraction - `.meas` によるVth抽出
---

# 📐 03_vth_extraction：`.meas` によるしきい値電圧抽出  
**Extracting Threshold Voltage (Vth) Using `.meas` in SPICE**

---

## 📄 概要｜Overview

このフォルダでは、`ngspice` の `.meas` コマンドを活用して、  
**MOSトランジスタのしきい値電圧（Vth）を自動抽出**する手法を実践形式で解説します。  

This directory demonstrates how to **automatically extract threshold voltage (Vth)**  
from Vg–Id characteristics using the `.meas` feature in `ngspice`.

---

## 🔧 使用技術｜Technologies Used

| 項目｜Item | 内容｜Details |
|--------|-----------------------------|
| 🧱 デバイスモデル | `sky130_fd_pr__nfet_01v8` from Sky130 PDK |
| 🛠️ SPICEツール | `ngspice` with `.meas` directive |
| 📜 スクリプト生成 | Pythonで `.spice` ＋ `.meas` を自動生成 |

---

## 🧪 実験構成｜Experiment Structure

```text
03_vth_extraction/
├── run_vth_sweep.py         # .spice生成＋ngspice実行
├── templates/
│   └── meas_template.spice  # .measを含むベース回路テンプレート
├── output/
│   ├── vth_W1.0_L0.15.log   # ngspice出力ログ
│   └── vth_W1.0_L0.15.dat   # 抽出Vth値（CSV形式）
└── plot_vth.py              # Vth結果のグラフ化スクリプト
```

---

## 📏 `.meas` 文の記述例｜Sample `.meas` Command

```spice
.meas vth find VGS when I(D) = 1e-6
```

この文は、**ドレイン電流が 1µA** になるときのゲート電圧 `VGS` をしきい値 `Vth` として抽出します。  
This command extracts the VGS value when the drain current reaches **1 µA**, treating it as `Vth`.

---

## 🚀 実行方法｜How to Run

```bash
python3 run_vth_sweep.py
```

実行により：

- W/L 条件に応じた `.spice` ファイルを自動生成  
- `.meas` を含む回路で `ngspice` を実行  
- `.log` 内の `.meas` 結果を自動パースして `.dat` に保存  

---

## 📈 出力例｜Example Output (Graph)

| 特徴｜Features |
|------------------------------|
| 🔹 W/Lごとの Vth の傾向を可視化  
| 🔹 温度・電源電圧変化への感度評価  
| 🔹 設計限界やバラつきの理解に有効  

```bash
python3 plot_vth.py
```

---

## 💡 応用展開｜Advanced Applications

| 応用例｜Applications |
|----------------------|
| ✅ `.meas` による `Idsat` 抽出（最大Id点）  
| ✅ 高耐圧デバイスや PFET への適用拡張  
| ✅ `.temp` を活用した温度依存性評価  

---

## 🔗 関連リンク｜Related Chapters

| 項目｜Item | リンク｜Link |
|--------|-----------------------------|
| ⚗️ Sky130実験（第2章） | [../README.md](../README.md) |
| 🛠️ 自動化ツール群（第1章） | [../../e_chapter1_python_automation_tools/README.md](../../e_chapter1_python_automation_tools/README.md) |

---

## 🔙 戻る｜Back to Chapter Top

[🏠 実践編 第2章 トップへ戻る｜Back to `e_chapter2_sky130_experiments`](../README.md)
