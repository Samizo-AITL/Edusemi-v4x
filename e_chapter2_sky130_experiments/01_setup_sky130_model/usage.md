# 使用方法：01_setup_sky130_model

本教材では、Sky130の `.lib.spice` モデルを読み込んで、基本的な `nMOS` / `pMOS` トランジスタの動作を確認します。  
SPICEファイルの構成や、`ngspice` によるシミュレーション手順を以下に示します。

---

## 📦 前提準備

### 1. Sky130 PDK をローカルに配置

Sky130 の PDK は以下のようなパスに展開されていることを想定：

```bash
~/pdks/sky130A/libs.tech/ngspice/
```

このパスを .spice ファイルの中で指定します。

## 📁 フォルダ構成（例）
```
01_setup_sky130_model/
├── nfet_vgid.spice
├── pfet_vgid.spice
├── sky130_model_paths.inc
├── run_check.sh
└── output/
```

## 🔧 1. モデルファイルの読み込み（例）

nfet_vgid.spice の先頭で以下のように .lib を読み込みます：
```
.include "./sky130_model_paths.inc"
.lib sky130.lib.spice tt
```
または直接パス指定も可能です：
```
.include "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice"
.lib "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice" tt
```

## 🚀 2. シミュレーションの実行

コマンドラインで以下を実行：
```
ngspice nfet_vgid.spice
```
または簡易スクリプト：
```
sh run_check.sh
```
出力は output/ フォルダに以下のように格納されます：
```
output/
├── vgid_W1.0_L0.15.spice
├── vgid_W1.0_L0.15.log
```

## 📈 3. 結果の可視化

ログファイル内の .DATA セクションから Vg–Id の数値を抽出

python3 ../02_plot_vgid/plot_vgid.py output/vgid_W1.0_L0.15.log

## 🔗 関連
	•	02_plot_vgid/：ログの読み取りとグラフ化
	•	01_spice_runner/：自動SPICE実行

---

## 📝 備考
	•	.lib モデルのコーナーは tt, ff, ss など複数あり、条件ごとの評価も可能です。
	•	Sky130 PDK は教育向けのモデルであり、商用の精度とは異なる点に留意してください。
	•	ファイル名やW/L条件は今後の自動スクリプトと連携するため、命名規則に準拠すると便利です。

---
