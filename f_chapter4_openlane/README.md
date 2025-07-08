# 🧱 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装

本章では、AITL-H三層制御アーキテクチャ（FSM・PID・LLM）に基づいて設計されたRTLモジュール群を、  
**OpenLane** ツールを用いて **RTL（Verilog）からGDSII（レイアウト）まで自動生成**するプロセスを解説します。

---

## 🎯 本章の目的

- FSM/PIDモジュールを対象とした**配置配線実験（Place & Route）**
- RTL-to-GDSIIまでの**設計フローの実体験**
- OpenLaneの**構成ファイル・制約設計・評価レポートの理解**
- SoC設計の**物理的実現可能性**や**設計ボトルネック**の検出

---

## 📚 章構成

| 節 | 内容 | 対象モジュール |
|----|------|----------------|
| 4.1 | OpenLane導入とプロジェクト構成 | ─ |
| 4.2 | FSMモジュールの配置配線 | `fsm_engine.v` |
| 4.3 | PIDモジュールの配置配線 | `pid_controller.v` |
| 4.4 | SoC統合モジュールのGDSII化 | `soc_top.v` |
| 4.5 | 面積・タイミング・配線密度の評価 | 各モジュール共通 |
| 4.6 | 図面生成とレイアウト可視化（KLayout連携） | GDS出力全体 |

---

## 🧪 実験対象の概要

| モジュール | 機能 | ファイル |
|------------|------|----------|
| FSM | 状態遷移・行動決定 | `verilog/fsm_engine.v` |
| PID | 安定化制御（e演算） | `verilog/pid_controller.v` |
| SoC Top | FSM＋PIDの統合構成 | `verilog/soc_top.v` |

---

## ⚙️ 使用ツール

| ツール名 | 用途 |
|----------|------|
| OpenLane | RTL-to-GDSII設計フロー |
| Sky130 | PDK（Google/SkyWater） |
| KLayout | GDSIIレイアウト表示 |
| GTKWave | シミュレーション波形確認（補助） |

> 💡 本教材は **OpenLane v2（またはv1系）** に対応しています。

---
```
## 📦 ディレクトリ構成（教材）

f_chapter4_openlane/
├── README.md
├── docs/
│   ├── 4_1_openlane_intro.md
│   ├── 4_2_fsm_layout.md
│   ├── 4_3_pid_layout.md
│   ├── 4_4_soc_layout.md
│   ├── 4_5_evaluation.md
│   └── 4_6_gds_view.md
├── openlane/
│   ├── fsm_engine/       ← 各モジュールのconfig.tcl
│   ├── pid_controller/
│   └── soc_top/
├── verilog/              ← RTLファイル（リンク or コピー）
├── results/              ← GDS, reports, logs
└── images/               ← 結果図、配置図など
```

---

---

## 📝 注意事項

- OpenLaneの実行には Docker 環境が必要です。
- PDKインストール、`config.tcl`設計、`floorplan.tcl`設定などは各節で順次解説します。
- FSMやPIDの設計内容は、**特別編 第3章**を参照してください。

---

## 🔗 関連リンク

- [特別編 第3章：FSM×PID×LLMによる統合制御システムのSoC実装手法](../f_chapter3_socsystem/README.md)
- [OpenLane公式](https://github.com/The-OpenROAD-Project/OpenLane)
- [Sky130 PDK](https://github.com/google/skywater-pdk)

---
