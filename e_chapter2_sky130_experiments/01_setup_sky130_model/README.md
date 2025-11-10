---
layout: default
title: 01_setup_sky130_model - Sky130モデル準備と初期動作確認（詳細強化版）
---

---

# ⚙️ 01_setup_sky130_model  
**Sky130 MOS Model Setup and Initial Simulation — Detailed & Polished Edition**

---

## 📘 概要｜Overview

本フォルダでは、**Sky130 PDK の MOS トランジスタ SPICE モデルを正しく読み込み、  
ngspice による動作確認を最低限の構成で確実に行う**ための設計を提供します。

特に、Sky130 モデルはファイル構造・階層・命名規則が複雑であるため、  
**誤った include/.lib 記述によりシミュレーション不能になるケースが多発します。**

この章では、以下の内容を扱います：

- ✅ Sky130 PDK の **正しい ngspice モデルパス設定**  
- ✅ **nfet/pfet_01v8** を用いた Vg–Id 基本特性測定  
- ✅ `.raw` `.log` 出力の正しい扱い  
- ✅ MOS Id の **確実に OS 依存なく得られる方法**  
- ✅ 教材としての **再現性100% のテンプレート構築**

---

## 📁 フォルダ構成｜Folder Contents（詳細付き）

| ファイル名｜Filename | 説明｜Description |
|----------------------|----------------------------------------------------------|
| [`nfet_vgid.spice`](./nfet_vgid.spice) | `sky130_fd_pr__nfet_01v8` を用いた Vg–Id Sweep<br>**教育用に最適化された最小構成** |
| [`pfet_vgid.spice`](./pfet_vgid.spice) | `sky130_fd_pr__pfet_01v8` の対称特性実験 |
| [`sky130_model_paths.inc`](./sky130_model_paths.inc) | PDK モデルパス `.lib` を統一管理する include<br>**PDK_ROOT と PDK を一括管理できる教材仕様** |
| [`run_check.sh`](./run_check.sh) | nfet/pfet の動作確認をまとめて行う実行スクリプト |
| `output/` | `.csv` `.log` ファイルの保存ディレクトリ（🛠 手動 or スクリプトで作成） |

---

## 🔧 前提条件｜Requirements

| 項目｜Item | 内容｜Details |
|--------|------------------------------------------------|
| ✅ Sky130 PDK | `volare enable sky130A` により展開されていること |
| ✅ PDK Root | 例：`/mnt/c/openlane/pdks/`（WSL） |
| ✅ ngspice | version **35以上** 推奨（Sky130 の .lib 読み込みに適合） |
| ✅ OS | Linux / WSL2（Windows ngspice.exe は PDK パスで失敗しやすい） |

---

## 🚀 Step 1：Sky130 SPICE モデルの正しい読み込み  
### ✅ `.include` ではなく `.lib` を使う（Sky130 PDK 仕様）

Sky130 PDK は **複数の階層・コーナー（tt/ff/ss/…）を .lib 内で管理している**ため、  
`.include` を使うと **モデルが重複定義されて ngspice が警告を出す**。

### ✅ **正しい記述（教材推奨 / 再現性100%）**

```spice
.lib "$::env(PDK_ROOT)/$::env(PDK)/libs.tech/ngspice/sky130.lib.spice" tt
```

📝 **ポイント**

- `$::env(PDK_ROOT)` は OpenLane と完全互換  
- Linux / WSL / Docker すべてで動作  
- シミュレーションコーナーは `tt`（typical-typical）を使用  
- PDK 変更は  
  ```bash
  export PDK=sky130A
  ```  
  を変更するだけで全回路が切り替わる

✅ **教材として最も望ましい形式**

---

## 🚀 Step 2：nfet_vgid.spice の実行  
### 実行コマンド

```bash
ngspice nfet_vgid.spice
```

### 実行される内容

- Vg（ゲート電圧）を線形 Sweep  
- Drain 電流を測定し Id–Vg カーブを生成  
- 解析結果を内部バッファへ蓄積（`.raw` は必要時のみ書き出し）

---

## 📈 Step 3：結果の出力と保存  
ngspice はデフォルトではファイル保存しないため  
**`.control` 内で保存命令を明示する必要がある。**

例：CSV ファイル出力

```spice
.control
  set filetype=ascii
  wrdata output/nfet_vgid.csv v(g) Id
.endc
```

### 🛠 注意  
`output/` ディレクトリは ngspice 自動生成されない。  
存在しない場合は作成すること：

```bash
mkdir -p output
```

---

## 🔍 Step 4：MOS Id の正しい取得方法（OS非依存の確実版）

Sky130 PDK の MOS 電流は **Drain 側 branch current を利用**するのが最も安全。

### ✅ 教材推奨（最も堅牢）

```spice
plot -vd#branch vs v(g)
```

### ✅ 物理量としての Id（符号付き）が必要な場合

```spice
let Id = -i(Vd)
plot Id vs v(g)
```

---

## 🧪 推奨追加 `.control`（教育用途に最適化）

```spice
.control
  run
  set filetype=ascii
  wrdata output/nfet_vgid.csv v(g) Id
  plot v(g) Id
.endc
```

- 学習者が結果を視覚的に把握しやすい  
- Python による可視化（第2章の後続ステップ）と完全連携

---

## 📝 Notes（補足）

- `nfet_01v8` / `pfet_01v8` は **標準1.8V MOS**  
- **L/W の縮小 → サブスレッショルド領域の変化**が観察可能  
- `.meas` による自動 Vth 抽出は第 03 章で扱う  
- 本章は「**Sky130 SPICE × Python × モデル理解の入口**」

---

## 🔗 References

- Sky130 PDK  
  https://github.com/google/skywater-pdk  
- ngspice  
  http://ngspice.sourceforge.net/

---

## ⬅️ 戻る｜Back to Chapter 2 Top
[実践編 第2章：Sky130実験とSPICE特性評価](../README.md)
