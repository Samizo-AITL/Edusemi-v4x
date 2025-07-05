# 01_spice_runner：SPICEシミュレーション自動化スクリプト

このフォルダでは、Sky130 の SPICE モデルを使用したトランジスタ特性のシミュレーションを  
`Python` によって自動化・バッチ実行するためのスクリプトを提供します。

---

## 🎯 目的

- `MOS` 特性（`Id–Vg`）の取得を自動化  
- `W/L` スケーリングや `Vth` 変化を簡易に比較  
- 再現性の高い実験フレームワークを構築  

---

## 📁 構成ファイル

| ファイル名              | 内容 |
|------------------------|------|
| `vgid_template.spice`  | `Vth`、`W`、`L`、`Vds` をプレースホルダで記述したテンプレート SPICE ファイル |
| `config.json`          | 実験条件（`Vds`、`W`、`L`、スイープ設定など）を定義する設定ファイル |
| `run_spice_sweep.py`   | テンプレート展開 → `ngspice` 実行 → `CSV` 出力を自動化する Python スクリプト |
| `output/`              | 実行後のログ、`raw` ファイル、抽出 `CSV` の保存先ディレクトリ |

---

## ⚙️ 実行方法

`python3 run_spice_sweep.py` を実行してください。

> ※ `ngspice` がインストールされている必要があります。  
> Ubuntu 系であれば、次のコマンドで導入できます：  
> `sudo apt install ngspice`

---

## 📘 後続処理

出力された `CSV` ファイルは、  
[`../02_plot_vgid/plot_vgid.py`](../02_plot_vgid/README.md) を用いて  
`Id–Vg` 特性のグラフとして可視化できます。

---

## 🔗 参考環境

- `Sky130 PDK モデル`：`sky130_fd_pr__nfet_01v8`  
- `ngspice バージョン`：`v35` 以降推奨（`.dc` 出力互換性のため）  
- `Python バージョン`：`3.9+` 推奨（`pandas`、`subprocess`、`pathlib` など使用）

---

## ✍️ 補足

- 今後、`Vth`、`W`、`L`、`Vds`、`温度`、`モデルコーナー` などを動的に切り替えて、  
  `信頼性評価` や `設計最適化演習` に展開予定です。
- 本フォルダのスクリプトは、  
  `03_degradation_model/` や `04_openlane_log_parser/` フォルダと連携して使用可能です。

---

技術監修・執筆：`三溝 真一（Shinichi Samizo）`  
GitHub：[`Samizo-AITL`](https://github.com/Samizo-AITL)  
Email：`shin3t72@gmail.com`
