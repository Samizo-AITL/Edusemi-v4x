# 🛠 第1章：Pythonによる自動化ツール群

本章では、半導体設計実務における反復作業や評価工程を効率化するために、Pythonを用いた自動化ツールの実装例を紹介します。  
対象は、SPICEシミュレーションの自動化・特性プロット・OpenLaneログ解析・信頼性モデル可視化・レポート出力など、多岐にわたります。

---

## 📁 フォルダ構成一覧

| フォルダ名 | 内容 |
|-----------|------|
| [`01_spice_runner/`](01_spice_runner/README.md) | `ngspice` を `Python` から自動実行し、パラメータスイープ・`Vth` 変化などを制御 [[使用方法]](01_spice_runner/usage.md) |
| [`02_plot_vgid/`](02_plot_vgid/README.md) | `Vg–Id` 特性など `SPICE` 出力ログの読み取りと可視化（`matplotlib`） [[使用方法]](02_plot_vgid/usage.md) |
| [`03_degradation_model/`](03_degradation_model/README.md) | `BTI`・`TDDB` など信頼性モデルの数式計算とグラフ化 [[使用方法]](03_degradation_model/usage.md) |
| [`04_openlane_log_parser/`](04_openlane_log_parser/README.md) | `OpenLane` フローの結果（遅延・面積・電力）を抽出し `CSV` 化・可視化 [[使用方法]](04_openlane_log_parser/usage.md) |
| [`05_report_template/`](05_report_template/README.md) | 自動レポート出力用テンプレート（`Jupyter` / `Markdown`） [[使用方法]](05_report_template/usage.md) |

---

## 🔗 関連章リンク

- [実践編 第2章：Sky130実験とSPICE特性評価](../e_chapter2_sky130_experiments/README.md)
- [実践編 第3章：OpenLaneによるデジタル設計実習](../e_chapter3_openlane_practice/README.md)

---

## 📦 想定される活用法

- 教育用：学生が自らSPICEやPDKと向き合いながら“自動評価スクリプト”を構築する実習に最適
- 実務用：OpenLaneによる複数構成比較・信頼性設計の初期検討・報告書生成の高速化
- 応用展開：スクリプトを拡張し、回路最適化・AI設計支援・EDA連携にも応用可能

---

## 📝 備考

- すべて教育用として設計されており、Sky130 PDK や ngspice に準拠
- 教材構成は MITライセンスの下で提供され、自由な改変・再利用が可能です
