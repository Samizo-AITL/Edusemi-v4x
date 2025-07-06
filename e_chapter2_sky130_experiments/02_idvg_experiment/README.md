# 📘 02_idvg_experiment

本フォルダでは、Sky130 PDK の `nfet_01v8` / `pfet_01v8` モデルを用いて、MOSトランジスタの `Vg–Id` 特性を評価します。  
複数の W/L 条件や電源電圧 Vds に対して、ゲート電圧 Vg をスイープし、しきい値電圧（Vth）や線形/飽和領域の特性を可視化します。

---

## 🎯 教材のねらい

- MOSトランジスタのバイアス特性（Vg–Id）を定量的に観察
- デバイス寸法（W/L）や電源条件の影響を比較
- Pythonによるプロット自動化と可視化を体験

---

## 📁 フォルダ構成（予定）

```text
02_idvg_experiment/
├── spice/
│   ├── nfet_W1.0_L0.15.spice
│   ├── pfet_W2.0_L0.3.spice
│   └── ...
├── output/
│   ├── nfet_W1.0_L0.15.log
│   └── ...
├── plot/
│   └── plot_vgid.py
└── README.md
```

---

## 🔧 実験条件の例

```text
| デバイスタイプ | W [µm] | L [µm] | Vds [V] | Vg sweep  |
|----------------|--------|--------|---------|-----------|
| nfet_01v8      | 1.0    | 0.15   | 0.8     | 0 → 1.2 V |
| pfet_01v8      | 2.0    | 0.3    | -0.8    | 0 → -1.2 V |
```

---

## 🚀 実行方法（手動）

```bash
ngspice spice/nfet_W1.0_L0.15.spice
```
出力ファイルは output/ 以下に保存されます：
```
output/
├── nfet_W1.0_L0.15.log
└── ...
```
## 📈 可視化スクリプトの実行
```
python3 plot/plot_vgid.py output/nfet_W1.0_L0.15.log
```
複数ログを重ねて比較することも可能です。

## 🔗 関連リンク
- ../01_setup_sky130_model/README.md
- ../../e_chapter1_python_automation_tools/02_plot_vgid/README.md

## 📝 備考
- `ngspice` の `.dc` 指令を活用し、Vg を固定ステップで掃引
- `.meas` を併用することで Vth の抽出も可能（後続教材で扱います）
- 教材として定番のMOS特性を、自作SPICE回路で得られる実感を重視

---
