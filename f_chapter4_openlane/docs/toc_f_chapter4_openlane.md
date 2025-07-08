# 🧭 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装【目次】

## 📂 章ファイル構成

- `f_chapter4_openlane/`
  - `README.md`（章イントロ）
  - `docs/`
    - `4_1_openlane_intro.md`：OpenLane導入と構成
    - `4_2_fsm_layout.md`：FSMモジュールの配置配線
    - `4_3_pid_layout.md`：PIDモジュールの配置配線
    - `4_4_soc_layout.md`：SoC統合モジュール実装
    - `4_5_evaluation.md`：設計評価レポートと比較
    - `4_6_gds_view.md`：GDSレイアウトの可視化
  - `openlane/`
    - `fsm_engine/`
    - `pid_controller/`
    - `soc_top/`

---

## 📖 各節リンク集

- [4.1 OpenLane導入とプロジェクト構成](docs/4_1_openlane_intro.md)
- [4.2 FSMモジュールの配置配線](docs/4_2_fsm_layout.md)
- [4.3 PIDモジュールの配置配線](docs/4_3_pid_layout.md)
- [4.4 SoC統合モジュールの実装](docs/4_4_soc_layout.md)
- [4.5 設計評価レポートと比較](docs/4_5_evaluation.md)
- [4.6 GDSレイアウトの可視化と考察](docs/4_6_gds_view.md)

---

## 📎 前提となる教材

- 特別編 第3章：[FSM×PID×LLMによる統合制御システムのSoC実装手法](../f_chapter3_soc/README.md)
- Sky130 PDK & OpenLane の導入（Edusemi 実践編参照）

---

## ✅ 備考

- 本章は教材リポジトリに統合される形で配置されます。
- 実行には Docker 上の OpenLane 環境を推奨します。
