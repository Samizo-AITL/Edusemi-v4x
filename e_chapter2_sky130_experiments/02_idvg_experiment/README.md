# 📘 02_plot_vgid - Vg–Id 特性の可視化

このフォルダでは、前章で取得した SPICE ログ (`.log`) を読み取り、nMOS / pMOS の Vg–Id 特性を Python で可視化します。  
教材目的で `matplotlib` の基本機能を使い、MOSFET の電気的挙動を視覚的に理解できるように設計されています。

---

## 📁 フォルダ構成

| ファイル名 | 内容 |
|------------|------|
| [`plot_vgid.py`](./plot_vgid.py) | `.log` ファイルから Vg–Id 特性を描画する Python スクリプト |
| `output/` | `.log` ファイルが保存されるディレクトリ（`01_setup_sky130_model/` で生成） |

---

## 🔧 前提条件

- Python 3.x がインストール済みであること
- 以下の Python ライブラリが使用可能であること：
  - `matplotlib`

インストール例：

```bash
pip install matplotlib
```

---

## 🚀 実行方法

```bash
python plot_vgid.py
```

正常に実行されると、以下の2曲線が表示されます：

- `sky130_fd_pr__nfet_01v8`（nMOS）
- `sky130_fd_pr__pfet_01v8`（pMOS）

---

## 📈 出力例

プロットされるグラフは以下のような形式です：

- X軸：Gate電圧 Vg [V]
- Y軸：Drain電流 Id [μA]
- 両特性を同一グラフ上に表示
- 0μAラインの補助線付き

---

## 🔗 関連リンク

- 📁 [01_setup_sky130_model/](../01_setup_sky130_model/) — SPICE モデルとログ生成
- 📘 [Sky130 PDK GitHub](https://github.com/google/skywater-pdk)
- 🐍 [matplotlib 公式](https://matplotlib.org/)

---
