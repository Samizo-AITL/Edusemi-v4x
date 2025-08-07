# 使用方法：01_spice_runner

本フォルダでは、`Python` スクリプトにより `ngspice` を自動制御し、`Vg–Id` 特性のシミュレーションを一括実行します。  
パラメータスイープやデバイスサイズの違いを簡単に切り替えられる構成になっています。

---

## 🔧 前提環境

以下の環境が整っていることを推奨します：

- `Python 3.9+`
- `ngspice`（バージョン 35 以降）
- Sky130 PDK の `sky130_fd_pr__nfet_01v8.spice` を取得済み
- 使用ライブラリ：`json`、`subprocess`、`pathlib`

> 📦 必要に応じて `requirements.txt` や `environment.yml` を活用してください。

---

## 📁 構成ファイル一覧

| ファイル名 | 説明 |
|------------|------|
| `run_spice_sweep.py` | メインスクリプト：テンプレート展開＋`ngspice` 実行 |
| `vgid_template.spice` | プレースホルダ形式の SPICE テンプレート |
| `config.json` | `W/L/VDS` などのパラメータ設定ファイル |
| `output/` | 出力ログおよび生成された `.spice` ファイル群 |

---

## 🚀 実行方法

### 1. 準備

テンプレートと設定ファイルを同一フォルダに設置し、`output/` を作成しておきます：

`mkdir -p output`

### 2. Python スクリプトの実行

`python3 run_spice_sweep.py`

この実行により、以下が自動的に行われます：

- `vgid_template.spice` をベースにした `.spice` ファイルの生成（各 `W` / `L` の組み合わせごと）
- `ngspice` を使った `.spice` ファイルの実行
- 出力ログは `.log` ファイルとして `output/` フォルダに保存されます

---

## 📂 出力例

```text
output/
├── vgid_W1.0_L0.15.spice
├── vgid_W1.0_L0.15.log
├── vgid_W2.0_L0.3.spice
└── vgid_W2.0_L0.3.log
```

※ .log ファイルは次ステップ（02_plot_vgid/）で読み取り・可視化されます。

## 🔗 関連ツール
	•	02_plot_vgid/：SPICE ログの可視化（matplotlib）
	•	03_degradation_model/：BTI・TDDB 劣化モデルとの連携解析
	•	05_report_template/：レポート出力支援テンプレート（Jupyter / Markdown）

---

## 📝 備考
	•	sky130_fd_pr__nfet_01v8.spice が vgid_template.spice 内で .include されている必要があります
	•	スクリプト run_spice_sweep.py により、{{W}} / {{L}} / {{VDS}} がテンプレートに挿入されます
	•	.dc Vgs のスイープ範囲（0 ～ 1.2）とステップ（0.01）はテンプレート側で定義されています
 
---

[🐍 実践編 第1章：Python自動化ツール群トップに戻る](../README.md)
