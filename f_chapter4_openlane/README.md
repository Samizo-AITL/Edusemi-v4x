---
layout: default
title: 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装
---

---

# 📘 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装  
**Special Chapter 4: RTL-to-GDSII Implementation of FSM×PID×LLM Control System with OpenLane**

---

本章では、FSM・PID・統合SoCモジュールを対象に、Sky130 PDKを用いた  
**OpenLaneによる配置配線フロー（RTL-to-GDSII）**を学習します。  
This chapter focuses on implementing **place-and-route (RTL-to-GDSII)** using OpenLane and Sky130 PDK for FSM, PID, and integrated SoC modules.

---

## 🧭 章構成と内容一覧｜Chapter Structure and Overview

| 🔢 **節番号**<br>**Sec.** | 📖 **タイトル（日本語）**<br>**Title (JP)** | 📘 **Title (EN)** | 📝 **概要**<br>**Summary** |
|--------------------------|---------------------------------------------|-------------------|-----------------------------|
| **4.1** | [OpenLane導入とプロジェクト構成](docs/4_1_openlane_intro.md) | Introduction to OpenLane and Project Setup | ディレクトリ構成と config 準備の基本<br>Directory structure and config setup |
| **4.2** | [FSMモジュールの配置配線](docs/4_2_fsm_layout.md) | Place-and-Route of FSM Module | FSM単体の配置配線（RTL-to-GDSII）<br>RTL-to-GDSII of FSM module |
| **4.3** | [PIDモジュールの配置配線](docs/4_3_pid_layout.md) | Place-and-Route of PID Module | PID制御モジュールのレイアウト実装<br>Place-and-route of the PID controller |
| **4.4** | [SoC統合モジュールの実装](docs/4_4_soc_layout.md) | Implementation of Integrated SoC | FSM＋PID統合回路のGDSII化<br>Full integration of FSM and PID |
| **4.5** | [設計評価レポートと比較](docs/4_5_evaluation.md) | Design Evaluation and Comparison | 面積・DRC・タイミング比較分析<br>Area, DRC, and timing comparison |
| **4.6** | [GDSレイアウトの可視化と考察](docs/4_6_gds_view.md) | GDS Visualization and Analysis | KLayoutやMagicによる視覚検証<br>GDS layout visualization using KLayout/Magic |

---

## 🧱 OpenLane プロジェクト構造（教材用）  
## 🧱 Project Structure for OpenLane (Educational Version)

```plaintext
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

> 📂 `openlane/`以下に、各モジュールのOpenLaneプロジェクトを個別構成しています。  
> Each module under `openlane/` is configured as an independent OpenLane project.

---

## 🛠️ 使用ツール・バージョン｜Tools and Versions Used

| ツール｜Tool | バージョン例｜Example Version |
|-------------|----------------------|
| **OpenLane** | v2.0+ |
| **PDK** | Sky130A |
| **レイアウト可視化**<br>Layout Viewer | KLayout / Magic |

---

## 📌 補足｜Notes

- 本章は、**特別編 第3章のRTL設計結果**を前提としています。  
  This chapter assumes RTL modules developed in **Appendix Chapter 3**.
- 実行には **OpenLaneのDocker環境** または **手動インストール**が必要です。  
  Execution requires either the **Dockerized OpenLane environment** or manual installation.
- 各モジュールは `flow.tcl` により個別にフローを起動します。  
  Each module is run individually using `flow.tcl`.

---

## 🎓 学習目標｜Learning Objectives

| 項目｜Item | 内容｜Description |
|------|------|
| **OpenLaneの基礎操作**<br>Basic Use of OpenLane | ディレクトリ構成・設定ファイルの理解 |
| **FSM / PID / SoCの実装**<br>FSM / PID / SoC Layout Flow | RTLからGDSIIまでの手順を習得 |
| **レイアウト比較評価**<br>Layout Evaluation & Analysis | 面積・DRC・タイミングなどの指標比較 |
| **KLayout/Magicの可視化操作**<br>Visualization via KLayout/Magic | 実レイアウトを視覚的に理解する技術 |

---

## 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

## 🔙 戻る｜Back to Top
**🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)**
