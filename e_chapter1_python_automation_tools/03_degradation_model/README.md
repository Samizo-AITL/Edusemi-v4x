# 03_degradation_model：信頼性劣化モデルの可視化

このフォルダでは、`BTI` や `TDDB` のようなトランジスタ信頼性劣化モデルを  
Pythonで数式化し、寿命予測や特性変化をグラフで視覚化します。

## 📌 主な内容

- `ΔVth(t) = A × tⁿ` などのBTIモデルのグラフ化
- `tbd = A · exp(B/E)` 型のTDDB寿命推定
- 動作点ごとの寿命差や設計限界の視覚化

## 🐍 使用予定ライブラリ

- `numpy`
- `matplotlib`
- `scipy.optimize`（必要に応じて）
