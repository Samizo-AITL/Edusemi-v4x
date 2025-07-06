# 📐 03_Vth抽出：`.meas` による自動評価

本ディレクトリでは、`ngspice` の `.meas` コマンドを用いて、`Vg–Id` 特性からMOSトランジスタのしきい値電圧（Vth）を自動抽出する手法を示します。

---

## 🔧 使用技術

- `Sky130` PDKのNFETモデル（例：`sky130_fd_pr__nfet_01v8`）
- `ngspice` の `.meas` コマンド
- 自動生成された `.spice` ファイルに `.meas` 文を追加

---

## 🧪 実験構成

```text
03_vth_extraction/
├── run_vth_sweep.py         ... Vg–Id特性を掃引し、.meas付きspiceを生成
├── templates/
│   └── meas_template.spice  ... .meas文を含むSPICEベーステンプレート
├── output/
│   ├── vth_W1.0_L0.15.log   ... ngspice出力ログ
│   └── vth_W1.0_L0.15.dat   ... 抽出されたVth結果
└── plot_vth.py              ... 抽出Vthをグラフ表示（複数W/L条件対応）
```

## 📏 .meas 文の例
.meas vth find VGS when I(D) = 1e-6

この例では、ドレイン電流が 1µA となるゲート電圧 VGS をしきい値 Vth と定義しています。

## 🚀 実行例
python3 run_vth_sweep.py

指定したW/L条件で複数の.spiceファイルを生成し、.meas評価込みで ngspice を実行します。ログから .meas 結果をパースし、CSV保存・グラフ化が可能です。

---

## 🔍 出力例（グラフ）
	•	W/LごとのVthの傾向を視覚化
	•	電源電圧・温度などの影響を比較することで特性ばらつきや設計限界を把握

---

## 💡 応用展開
	•	.meas による Idsat 抽出（ドレイン電流の最大値など）
	•	P型素子（pfet）や高耐圧素子への拡張
	•	温度スイープ対応による温度依存性の評価

---

## 🔗 関連章リンク
	•	第2章：Sky130実験とSPICE特性評価
	•	第1章：Pythonによる自動化ツール群

---
