---
layout: default
title: 02_idvg_experiment - Vg–Id 特性実験
---

# 📘 02_idvg_experiment：Vg–Id 特性実験  
**MOSFET Vg–Id Characterization Using Sky130 PDK**

---

## 📄 概要｜Overview

このフォルダでは、Sky130 PDK の `nfet_01v8` / `pfet_01v8` を用いた  
**MOSトランジスタの Vg–Id 特性評価実験**を行います。  
ゲート電圧 Vg をスイープし、しきい値電圧やトランジスタ特性の違いを観察します。

This folder contains experiments for **evaluating Vg–Id characteristics**  
of `nfet_01v8` / `pfet_01v8` using **Sky130 PDK**.  
By sweeping gate voltage Vg, we observe threshold voltage and device behavior.

---

## 🎯 学習目的｜Learning Objectives

| ✅ 日本語 | ✅ English |
|----------|-----------|
| MOS の Vg–Id カーブを取得・可視化 | Visualize MOSFET Vg–Id curves |
| W/L や Vds の影響を定量的に把握 | Quantitatively understand effects of W/L and Vds |
| Python による自動描画スクリプト体験 | Use Python scripts for automatic plotting |

---

## 📁 フォルダ構成｜Folder Structure

```text
02_idvg_experiment/
├── spice/              # SPICE回路ファイル｜SPICE Circuit Files
│   ├── nfet_W1.0_L0.15.spice
│   ├── pfet_W2.0_L0.3.spice
├── output/             # SPICEログ出力先｜Simulation Logs
│   ├── nfet_W1.0_L0.15.log
├── plot/               # 可視化スクリプト｜Plotting Scripts
│   └── plot_vgid.py
└── README.md
```

---

## 🔧 実験条件の例｜Example Simulation Conditions

| デバイスタイプ｜Device | 幅 W [µm] | 長さ L [µm] | Vds [V] | Vg 掃引範囲｜Sweep Range |
|----------------------|-------------|-------------|---------|--------------------------|
| `nfet_01v8` | 1.0 | 0.15 | 0.8 | 0.0 → 1.2 V |
| `pfet_01v8` | 2.0 | 0.3  | -0.8 | 0.0 → -1.2 V |

---

## 🚀 実行方法｜How to Run

### 🔹 1. 単体シミュレーション｜Single Simulation

```bash
ngspice spice/nfet_W1.0_L0.15.spice
```

- `.log` ファイルが `output/` フォルダに出力されます。

---

### 🔹 2. 一括実行（bash）｜Batch Execution

```bash
for file in spice/*.spice; do
    ngspice "$file"
done
```

- 各 `.spice` ファイルごとに `.log` が生成されます。

```text
output/
├── nfet_W1.0_L0.15.log
├── nfet_W2.0_L0.3.log
├── pfet_W1.0_L0.15.log
└── pfet_W2.0_L0.3.log
```

---

## 📈 結果の可視化｜Plotting Vg–Id Curves

出力された `.log` ファイルは、Python スクリプトで描画可能です。

### 🔸 単一ファイルの描画｜Single File

```bash
python3 plot/plot_vgid.py output/nfet_W1.0_L0.15.log
```

### 🔸 複数ファイルの一括描画｜Multiple Files

```bash
python3 plot/plot_vgid.py output/*.log
```

- 系列ごとに色分けしてプロットされます。  
- Vg–Id カーブが重ねて表示され、特性比較が容易になります。

---

## 🛠️ カスタマイズのヒント｜Customization Tips

| 項目｜Item | 説明｜Description |
|---------|----------------------------------------------|
| `.dc`  | Vg のスイープ範囲やステップ幅を変更可能<br>Modify Vg sweep range and step |
| `.lib` | `tt`, `ff`, `ss` などのプロセス条件を切替可能<br>Switch process corners |
| `.meas` | Vth や特定電圧の Id を自動抽出可能<br>Enable automated Vth extraction |

---

## 🔗 関連リンク｜Related Links

| 📁 フォルダ / ページ | 内容 |
|----------------------|------|
| [../01_setup_sky130_model/README.md](../01_setup_sky130_model/README.md) | Sky130 モデル設定と初期確認 |
| [../../e_chapter1_python_automation_tools/02_plot_vgid/README.md](../../e_chapter1_python_automation_tools/02_plot_vgid/README.md) | Python による Vg–Id グラフ描画ツール |

---

## 🔙 戻る｜Back to Chapter Top

[🏠 実践編 第2章 トップへ戻る](../README.md)
