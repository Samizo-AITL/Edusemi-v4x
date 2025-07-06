# 使用方法：02_plot_vgid

本フォルダでは、`SPICE` シミュレーション結果（`.log` ファイル）を読み取り、`Vg–Id` 特性グラフとして可視化します。  
`matplotlib` および `pandas` を使用し、複数デバイスサイズやバイアス条件をまとめて描画可能です。

---

## 🔧 前提環境

- `Python 3.9+`
- `pandas`
- `matplotlib`

必要に応じて以下でインストール：

`pip install pandas matplotlib`

---

## 📁 構成ファイル一覧

| ファイル名 | 説明 |
|------------|------|
| `plot_vgid.py` | メインスクリプト。指定フォルダ内の `.log` ファイルを読み取り、グラフとして描画 |
| `output/` | `01_spice_runner/` によって生成された `.log` ファイル群 |
| `figures/` | 出力される `PNG` や `PDF` 形式のグラフ保存先（自動生成されます） |

---

## 🚀 実行方法

### 1. 出力フォルダの準備

`output/` フォルダに `.log` ファイルが格納されていることを確認してください。  
通常は `01_spice_runner/` により生成されます。

### 2. 可視化スクリプトの実行

`python3 plot_vgid.py`

- 同一フォルダ内の全 `.log` を自動認識し、デバイスごとに `Vgs–Id` カーブを描画します。
- 結果グラフは `figures/` 以下に保存されます。

---

## 📈 出力例

```text
figures/
├── VgId_W1.0_L0.15.png
├── VgId_W2.0_L0.3.png
└── VgId_summary.pdf
```

※ 端末上にも matplotlib によって即時表示されます。

---

## 🔗 関連ツール
	•	01_spice_runner/：SPICEログの生成元
	•	03_degradation_model/：劣化による Vth 変化などをモデル化

---

## 📝 備考
	•	.log ファイルから Vgs / Id をパースする正規表現はスクリプト内に定義済み
	•	出力形式（PNG/PDF）は matplotlib.pyplot.savefig() にて指定可能
	•	軸範囲やタイトル書式は必要に応じて変更できます

---
 
