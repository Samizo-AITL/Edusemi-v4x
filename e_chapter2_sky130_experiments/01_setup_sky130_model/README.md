# 📘 01_setup_sky130_model

本フォルダでは、Sky130 PDK に含まれる MOS トランジスタの SPICE モデルを準備し、最小限の回路で動作確認を行います。  
教育目的で [ngspice](http://ngspice.sourceforge.net/) を使用し、nMOS/pMOS の初期動作を可視化するところから始めます。

---

## 📁 フォルダ構成

| ファイル名 | 内容 |
|------------|------|
| [`nfet_vgid.spice`](./nfet_vgid.spice) | `nfet_01v8` の Vg–Id 特性を得る最小回路例 |
| [`pfet_vgid.spice`](./pfet_vgid.spice) | `pfet_01v8` の Vg–Id 特性を得る回路例 |
| [`sky130_model_paths.inc`](./sky130_model_paths.inc) | `.lib` 定義を含む Sky130 PDK モデル参照ファイル |
| [`run_check.sh`](./run_check.sh) | `ngspice` による基本動作チェック用シェルスクリプト |
| [`output/`](./output/) | `.raw` や `.log` 出力を格納（自動生成） |

---

## 🔧 前提条件

- [Sky130 PDK](https://github.com/google/skywater-pdk) をローカルに導入済みであること  
  例：`~/pdks/sky130A/`

- `ngspice` がインストールされていること  
  推奨バージョン：`ngspice-35` 以降

---

## 🚀 実行方法

### 1. `.spice` ファイルの準備

Sky130 PDK に合わせて以下のように `.lib` パスを指定します：

```spice
.include "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice"
.lib "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice" tt
```

### 2. シミュレーション実行

コマンドラインから以下を実行してください：

```bash
ngspice nfet_vgid.spice
```

output/ フォルダ内に .raw や .log が自動生成されます。

---

## 📈 結果確認

- `ngspice` の内蔵グラフ表示機能で Vg–Id 特性を確認できます。
- Python + matplotlib による可視化は [`02_plot_vgid/`](../02_plot_vgid/) にて実装。
- `.log` ファイルに Id–Vg のスイープデータが記録されます。

---

## 📝 備考

- `.lib` のコーナー条件は `tt`（typical-typical）を使用します。
- 教材では `sky130_fd_pr__nfet_01v8` や `pfet_01v8` を基本素子とします。
- 本フォルダの `.spice` 回路は、以降の章で Python による自動制御対象となります。

---

## 🔗 関連リンク

- 🌐 [Sky130 PDK GitHub リポジトリ](https://github.com/google/skywater-pdk)
- 🌐 [ngspice 公式サイト](http://ngspice.sourceforge.net/)
- 📁 [02_plot_vgid/](../02_plot_vgid/) — 出力ログの可視化

---


