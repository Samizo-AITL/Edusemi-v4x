# ⚗️ 実践編 第2章：Sky130実験とSPICE特性評価

本章では、SkyWaterのSky130 PDKを用いて、MOSトランジスタの基本特性（Vg–Idカーブ、Vth）や劣化予測（BTI・TDDB）まで含む **SPICEベースの設計評価実験**を構成します。

---

## 🎯 学習目的

- Sky130のMOS素子モデルを用いたSPICE実験
- Pythonと連携した特性抽出・可視化・寿命推定
- `.meas` 文やスクリプト自動化による評価効率化

---

## 📁 章内構成

| フォルダ名 | 内容 |
|------------|------|
| [`01_setup_sky130_model/`](01_setup_sky130_model/) | `ngspice`・Sky130環境の構築とモデル確認 |
| [`02_idvg_experiment/`](02_idvg_experiment/) | Vg–Id特性のSweepシミュレーション（`.spice`自動生成含む） |
| [`03_vth_extraction/`](03_vth_extraction/) | `.meas` によるVth抽出と可視化 |
| [`04_bti_tddb_estimation/`](04_bti_tddb_estimation/) | 劣化モデル（BTI, TDDB）との連携による寿命推定 |
| [`05_data_summary/`](05_data_summary/) | 実験ログ・特性グラフの集約とレポート出力準備 |

---

## 🔧 実行環境

- Sky130 PDK（`sky130_fd_pr__nfet_01v8` など）
- `ngspice 35+`
- Python 3.9 以上
- 必要なパッケージ（`matplotlib`, `pandas`, `numpy` など）

---

## 🔁 実験の流れ（概要）

1. `.spice` テンプレートとパラメータSweepでVg–Id特性を生成
2. `Python`でログ解析・グラフ化
3. `.meas` によるVth自動抽出
4. 劣化モデルと組み合わせて寿命予測

---

## 📘 関連リンク

- [実践編 第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)
- [実践編 第3章：OpenLaneによるデジタル設計実習](../e_chapter3_openlane_practice/README.md)

---

## 📌 教材の意義

- 実測に近いSPICE実験によって、**「特性＝現象」**を実感
- `.meas`や解析スクリプトにより、評価作業を構造化
- 信頼性評価や設計マージン設計へのつながりを体感

---

## 🧭 次に進むべき章

- **第3章：OpenLaneでの物理設計と結合評価**
- **応用編：高耐圧MOSやESD設計と組み合わせた特性評価**

---

🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---
