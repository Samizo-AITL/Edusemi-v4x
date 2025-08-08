---
layout: default
title: 4.1 OpenLane導入とプロジェクト構成
---

---

# 4.1 OpenLane導入とプロジェクト構成  
**Introduction to OpenLane and Project Setup**

---

## 🎯 本節の目的｜Purpose of This Section

| 📝 日本語｜Japanese | 📘 English |
|------------------|-------------|
| OpenLaneを用いた **RTL-to-GDSII設計フローの全体像**を把握する | Understand the **overall RTL-to-GDSII flow** using OpenLane |
| FSM・PIDモジュールごとの**独立プロジェクト構成**を準備する | Prepare **individual OpenLane project setup** per module |
| Sky130 PDKを利用した**教育向け設計環境**を構築する | Build an **educational design environment** with Sky130 PDK |

---

## 🧰 必要な環境・ツール｜Required Tools and Environment

| 🔧 ツール｜Tool | 📝 説明｜Description |
|----------------|----------------------|
| Docker | OpenLane実行環境（Linux/Mac/WSL対応）<br>Execution environment for OpenLane |
| OpenLane | 自動配置配線ツール一式<br>Automated place-and-route toolset |
| sky130 PDK | SkyWater提供のオープンPDK（OpenLaneに同梱）<br>Open PDK bundled with OpenLane |
| Git（任意） | 設計資産のバージョン管理<br>Version control for design assets |

> ✅ **推奨バージョン｜Recommended**: OpenLane v2（v1でも可）

---

## 🛠️ OpenLaneのインストール手順｜OpenLane Installation Steps

```bash
# リポジトリのクローン
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane

# PDKを含めた初期化（Docker + PDK DL）
make

# GUI起動（任意）
make gui
```

> 💡 **注意**：初回DL時は **10〜20GBの空き容量**と**高速回線**が必要です。

---

## 🧱 教材用プロジェクト構成｜Project Structure in This Course

教材では、以下のようにモジュール単位で分離した OpenLane プロジェクトを構成しています。  
Each module is handled with an independent OpenLane directory as shown:

```text
f_chapter4_openlane/
└── openlane/
    ├── fsm_engine/
    │   ├── config.tcl
    │   ├── floorplan.tcl（任意）
    │   └── src/
    │       └── fsm_engine.v
    ├── pid_controller/
    │   └── ...
    └── soc_top/
        └── ...
```

> ✅ 各プロジェクトは `flow.tcl` により個別に実行します。

---

## ⚙️ `config.tcl` 最低構成例｜Minimal Configuration Example

以下は FSM 用プロジェクトの `config.tcl` 最小構成例です：  
Example `config.tcl` file for FSM project:

```tcl
# openlane/fsm_engine/config.tcl

set ::env(DESIGN_NAME) fsm_engine
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/fsm_engine.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"

set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
```

---

## 🔜 次節への導入｜Transition to Next Section

| 🚀 次節｜Next Section | 📘 内容概要｜Overview |
|----------------------|-------------------------|
| [4.2 FSMモジュールの配置配線](docs/4_2_fsm_layout.md) | FSMプロジェクトを使った **OpenLane実行例（RTL-to-GDSII）** を実演します。<br>We will demonstrate the RTL-to-GDSII flow using the FSM project. |

---

## 📎 前後の節｜Previous / Next Sections

- ◀️ 前の節｜Previous: [特別編第3章 3.6 ケーススタディ](../f_chapter3_socsystem/docs/3_6_case_study.md)  
- ▶️ 次の節｜Next: [4.2 FSMモジュールの配置配線](docs/4_2_fsm_layout.md)

📚 [🔙 特別編 第4章 README に戻る](../README.md)
