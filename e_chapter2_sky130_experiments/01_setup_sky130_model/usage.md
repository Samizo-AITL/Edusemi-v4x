---
layout: default
title: 使用方法：01_setup_sky130_model（改訂・詳細強化版）
---

---

# 📘 使用方法：01_setup_sky130_model  
**Sky130 SPICE Model Usage Guide — Revised & Enhanced Edition**

本教材では、Sky130 PDK の `.lib.spice` MOS モデルを正しく読み込み、  
`nMOS` / `pMOS` の基本特性を `ngspice` で評価します。  
本改訂版では **誤動作しやすいポイントを修正し、教材全体と整合した形式に統一**しています。

---

# ✅ 0. 前提準備（PDK 位置・環境変数）

Sky130 PDK は volare により次のように展開されていることを想定します：

```
$PDK_ROOT/sky130A/libs.tech/ngspice/
```

OpenLane / 教材全体と共通化するため、**必ず環境変数方式を使用**してください：

```bash
export PDK_ROOT=/mnt/c/openlane/pdks
export PDK=sky130A
```

---

# 📁 1. フォルダ構成（教材準拠）

```
01_setup_sky130_model/
├── nfet_vgid.spice
├── pfet_vgid.spice
├── sky130_model_paths.inc
├── run_check.sh
└── output/   ← 必要に応じて作成（ngspiceは自動生成しない）
```

---

# ✅ 2. Sky130 モデルファイルの正しい読み込み

## ❌（NG例）`.include` と `.lib` の併用  
Sky130 では model の多重定義が起きるため使用不可：

```
.include "~/pdks/sky130A/.../sky130.lib.spice"
.lib "~/pdks/sky130A/.../sky130.lib.spice" tt
```

## ✅（正しい方法）`.lib` のみを使用（最小・確実・教材標準）

```spice
.include "./sky130_model_paths.inc"
```

sky130_model_paths.inc の中身は以下の通り：

```spice
.lib "$::env(PDK_ROOT)/$::env(PDK)/libs.tech/ngspice/sky130.lib.spice" tt
```

📝 これにより、  
- **volare** の PDK を直接参照  
- **OpenLane** と同一パス体系  
- **tt（typical）コーナー**を使用  
- Windows / Linux / WSL 共通化

---

# 🚀 3. シミュレーションの実行

nfet の例：

```bash
ngspice nfet_vgid.spice
```

pfet の例：

```bash
ngspice pfet_vgid.spice
```

まとめて実行したい場合：

```bash
sh run_check.sh
```

---

# 📦 4. 出力先について（重要な改訂点）

あなたの旧記述では：

❌ output/ に自動生成されると説明 → **誤り**

ngspice は **フォルダを自動作成しません**。  
CSVなどを保存する場合は `.control` 内で指定する必要があります。

---

# ✅ 5. 出力を保存する正しい方法（教材統一形式）

nfet_vgid.spice 内の推奨構成：

```spice
.control
  run
  set filetype=ascii
  wrdata output/nfet_vgid.csv v(g) Id
.endc
```

出力：

```
output/
└── nfet_vgid.csv
```

---

# 📈 6. MOS Id の正しい取得方法（OS依存を完全排除）

Sky130 では MOS 電流は **branch current** を使用するのが確実。

### ✅ 安定版（推奨）
```spice
plot -vd#branch vs v(g)
```

### ✅ 物理的な符号を意識した版
```spice
let Id = -i(Vd)
plot Id vs v(g)
```

✅ Windows / Linux / WSL 全環境で一致  
✅ sky130_fd_pr__nfet_01v8 / pfet_01v8 で確実動作

---

# 📊 7. Python による可視化（教材第2章の正式構造に統一）

本教材第2章では以下のスクリプトを使用します：

```
02_idvg_experiment/parse_plot_idvg.py
```

実行例：

```bash
python3 ../02_idvg_experiment/parse_plot_idvg.py --csv output/nfet_vgid.csv --out nfet_vgid.png
```

結果：

```
nfet_vgid.png
```

---

# 🔗 関連教材（第2章フローと整合）

- [`02_idvg_experiment/`](../02_idvg_experiment/) — Vg–Id Sweep + Python可視化  
- [`03_vth_extraction/`](../03_vth_extraction/) — .meas による Vth 抽出  
- [`04_bti_tddb_estimation/`](../04_bti_tddb_estimation/) — BTI/TDDB 劣化解析  

---

# 📝 備考（補強）

- Sky130 PDK の MOS は 1.8V 用（sky130_fd_pr__nfet_01v8 / pfet_01v8）  
- `.meas` や `.step` などの応用は後続章で扱う  
- 命名規則は教材の自動解析スクリプトと整合するよう統一済み  

---

# ⬅️ 戻る
[実践編 第2章：Sky130実験とSPICE特性評価](../README.md)
