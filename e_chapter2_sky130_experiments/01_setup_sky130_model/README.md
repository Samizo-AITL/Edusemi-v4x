# 📘 01_setup_sky130_model

本フォルダでは、Sky130 PDK に含まれる MOS トランジスタの SPICE モデルを準備し、最小限の回路で動作確認を行います。  
教育目的で `ngspice` を使用し、nMOS/pMOS の初期動作を可視化するところから始めます。

---

## 📁 フォルダ構成

| ファイル名 | 内容 |
|------------|------|
| `nfet_vgid.spice` | `nfet_01v8` の `Vg–Id` 特性を得る最小回路例 |
| `pfet_vgid.spice` | `pfet_01v8` の `Vg–Id` 特性を得る回路例 |
| `sky130_model_paths.inc` | `.lib` 定義を含む Sky130 PDK モデル参照ファイル |
| `run_check.sh` | `ngspice` による基本動作チェック用シェルスクリプト |
| `output/` | `.raw` や `.log` 出力を格納（自動生成） |

---

## 🔧 前提条件

- Sky130 PDK をローカルに導入済みであること  
  例：`~/pdks/sky130A/`

- `ngspice` がインストールされていること  
  推奨バージョン：`ngspice-35` 以降

---

## 🚀 実行方法

### 1. `.spice` ファイルの準備

Sky130 PDK に合わせて以下のように `.lib` パスを指定：

```spice
.include "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice"
.lib "~/pdks/sky130A/libs.tech/ngspice/sky130.lib.spice" tt
```

## 2. シミュレーション実行

コマンドラインから以下を実行：
ngspice nfet_vgid.spice

ログ出力や .raw 波形が output/ に生成されます。

---

## 📈 結果確認

可視化には ngspice のグラフ表示機能や、Python + matplotlib の plot_vgid.py が利用可能です。
出力ログに Id, Vg のスイープデータが記録されています。

---

## 📝 備考
	•	.lib のコーナー条件は tt（typical-typical）を使用
	•	教材では sky130_fd_pr__nfet_01v8 や pfet_01v8 を基本素子とする
	•	本フォルダの .spice 回路は、以降の章で Python による自動制御対象となります

---

## 🔗 関連リンク
	•	Sky130 PDK GitHub
	•	ngspice 公式
	•	02_plot_vgid/：出力ログの可視化

---
