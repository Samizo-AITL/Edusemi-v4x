# 🧱 実践編 第3章：OpenLaneによるデジタル設計実習

本章では、Sky130 PDKとOpenLaneを用いて、**RTL記述から論理合成・配置配線・GDS出力までの完全なデジタル設計フロー**を実践します。  
各ステージのログやレポートをPythonで解析・可視化し、設計結果の理解を深めます。

---

## 🎯 学習目的

- デジタルSoC設計の一連の流れ（論理合成〜物理設計〜GDS生成）を体験
- OpenLaneの各ステップの意味と設計影響を把握
- 設計ログの自動解析による設計改善と傾向把握

---

## 📁 章内構成

| フォルダ名 | 内容 |
|------------|------|
| [`01_openlane_setup/`](01_openlane_setup/) | OpenLaneの環境セットアップとテストデザインの準備 |
| [`02_rtl_to_gds_flow/`](02_rtl_to_gds_flow/) | RTL記述からGDSまでの設計フロー（run_flow.shの実行と各ステップ） |
| [`03_report_analysis/`](03_report_analysis/) | 面積・遅延・電力レポートの読み取りとCSV変換・グラフ化 |
| [`04_constraint_tuning/`](04_constraint_tuning/) | Clock制約や配置制約の変更による設計結果の変化観察 |
| [`05_macro_integration/`](05_macro_integration/) | SoC統合に向けた小マクロの組み合わせ設計の例（予定） |

---

## 🔧 必要な環境

- OpenLane（最新版推奨）
- Dockerまたはマニュアルインストール環境
- Sky130 PDK（`sky130_fd_sc_hd`）

---

## 🔁 実習の流れ

1. OpenLaneとPDKのセットアップ
2. サンプルRTL設計の実行（`run_flow.sh`）
3. レポート出力：delay, area, power
4. PythonスクリプトでCSV・グラフ化
5. 制約条件の変更 → 結果比較・チューニング

---

## 📘 関連リンク

- [実践編 第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)
- [実践編 第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)

---

## 📌 教材の意義

- デジタルIC設計を **実務と同様のフローで学べる**
- Pythonによるレポート解析を組み合わせ、**設計→評価の一貫流れを体験**
- Sky130 + OpenLane + GitHub による **現代的な教材展開**

---

## 🧭 今後の展開

- 複数マクロ統合によるSoC設計例の構築
- SPICEベースのセル特性と設計結果の連携
- バージョン差異によるEDAツールの影響検証
