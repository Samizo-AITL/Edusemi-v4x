# 📘 02_idvg_experiment：Vg–Id 特性実験

Sky130 PDK の `nfet_01v8` / `pfet_01v8` を用いた MOSトランジスタのバイアス特性（Vg–Id）評価実験です。  
複数の W/L 条件と Vds に対してゲート電圧 Vg をスイープし、MOS のしきい値電圧や特性の違いを観察します。

---

## 🎯 目的とねらい

- Vg–Id カーブの取得を通じて MOS動作を可視化
- W/L や Vds による影響の定量的な把握
- Pythonプロットによる実験データの見える化

---

## 📁 フォルダ構成

```text
02_idvg_experiment/
├── spice/              # SPICE回路ファイル
│   ├── nfet_W1.0_L0.15.spice
│   ├── pfet_W2.0_L0.3.spice
├── output/             # SPICEログ出力先
│   ├── nfet_W1.0_L0.15.log
├── plot/               # 可視化スクリプト
│   └── plot_vgid.py
└── README.md
```

---

## 🔧 実験条件の例

以下は代表的なシミュレーション条件です。W/LサイズやVdsを変えて特性変化を観察します。

| デバイスタイプ | W [µm] | L [µm] | Vds [V] | Vg sweep       |
|----------------|--------|--------|---------|----------------|
| nfet_01v8      | 1.0    | 0.15   | 0.8     | 0.0 → 1.2 V    |
| pfet_01v8      | 2.0    | 0.3    | -0.8    | 0.0 → -1.2 V   |

---

## 🚀 実行方法（手動）

`.spice` ファイルを直接 `ngspice` で実行します。

```bash
ngspice spice/nfet_W1.0_L0.15.spice
```

実行結果として、ログファイルが output/ フォルダに出力されます。
```
output/
├── nfet_W1.0_L0.15.log
└── ...
```
---

## 🔁 複数条件の一括実行（bash例）

複数の `.spice` ファイルがある場合、以下のように `for` ループを使って一括シミュレーションが可能です：

```bash
for file in spice/nfet_*.spice; do
    ngspice "$file"
done
```

実行後、各ログファイルが output/ ディレクトリに生成されます。
```
output/
├── nfet_W1.0_L0.15.log
├── nfet_W2.0_L0.3.log
├── pfet_W1.0_L0.15.log
└── pfet_W2.0_L0.3.log
```
## 📈 可視化スクリプトの実行

出力された .log ファイルは、Pythonスクリプト plot_vgid.py によってプロット可能です。

単一ファイルの表示
```
python3 plot/plot_vgid.py output/nfet_W1.0_L0.15.log
```
複数ファイルを一括描画
```
python3 plot/plot_vgid.py output/*.log
```
スクリプトは各 .log ファイルのVg–Idデータを読み取り、系列ごとに色分けしてプロットします。

---

## 📝 カスタマイズのヒント
- `.dc` ステートメントを編集して Vg の掃引範囲やステップ幅を変更可能
- `.lib` 行のコーナー指定（例：tt, ff, ss）を変更すればプロセスばらつきを考慮可能
- `.meas` ステートメントを追加すれば、Vth自動抽出や特定電圧でのId計測が可能

---

## 🔗 関連リンク
	•	../01_setup_sky130_model/README.md：初期設定とSPICEモデル確認
	•	../../e_chapter1_python_automation_tools/02_plot_vgid/README.md：ログ読み取りとVg–Idプロット自動化

 ---



