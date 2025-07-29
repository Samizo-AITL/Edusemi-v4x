# 📘 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装

本章では、FSM・PID・統合SoCモジュールを対象に、Sky130 PDKを用いた**OpenLaneによる配置配線フロー（RTL-to-GDSII）**を学びます。

## 🧭 章構成と内容一覧

| 節 | タイトル | 概要 |
|----|----------|------|
| 4.1 | [OpenLane導入とプロジェクト構成](docs/4_1_openlane_intro.md) | ディレクトリ構成とconfig準備の基本 |
| 4.2 | [FSMモジュールの配置配線](docs/4_2_fsm_layout.md) | FSM単体をOpenLaneで配置配線 |
| 4.3 | [PIDモジュールの配置配線](docs/4_3_pid_layout.md) | PID制御モジュールの配置配線 |
| 4.4 | [SoC統合モジュールの実装](docs/4_4_soc_layout.md) | FSM+PIDの統合回路のGDSII化 |
| 4.5 | [設計評価レポートと比較](docs/4_5_evaluation.md) | 面積・DRC・タイミング比較分析 |
| 4.6 | [GDSレイアウトの可視化と考察](docs/4_6_gds_view.md) | KLayout/Magicでのレイアウト可視化 |

---

## 🧱 OpenLane プロジェクト構造（教材用）

```
f_chapter4_openlane/
├── README.md
├── docs/
│   ├── 4_1_openlane_intro.md
│   ├── 4_2_fsm_layout.md
│   ├── 4_3_pid_layout.md
│   ├── 4_4_soc_layout.md
│   ├── 4_5_evaluation.md
│   └── 4_6_gds_view.md
└── openlane/
    ├── fsm_engine/
    ├── pid_controller/
    └── soc_top/
```

> `openlane/` 以下に各モジュールのプロジェクトを独立構成しています。

---

## 🛠️ 使用ツール・バージョン例

- OpenLane v2.0+
- Sky130A PDK
- KLayout / Magic (レイアウト可視化)

---

## 📌 補足

- 本章の実習は、Edusemi特別編 第3章のRTL設計結果を前提とします。
- 実行にはOpenLaneのDocker環境またはマニュアルインストールが必要です。
- `flow.tcl` により各モジュールを個別に実行します。

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)

---
