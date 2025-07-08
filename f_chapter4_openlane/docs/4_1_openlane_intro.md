# 4.1 OpenLane導入とプロジェクト構成

## 🎯 本節の目的

- OpenLaneを用いた **RTL-to-GDSII設計フローの全体像**を把握する
- FSM・PIDモジュールごとの**独立プロジェクト構成**を準備する
- Sky130 PDKを利用する**教育向け自動設計環境**を構築する

---

## 🧰 必要な環境・ツール

| ツール | 説明 |
|--------|------|
| Docker | OpenLane実行環境（Linux/Mac/WSL対応） |
| OpenLane | 自動配置配線ツール一式 |
| sky130 PDK | SkyWater製のオープンPDK（OpenLaneにバンドル） |
| Git（任意） | 設計資産のバージョン管理 |

> ✅ 推奨バージョン：OpenLane v2（v1でも可）

---

## 🛠️ OpenLaneのインストール（簡易手順）

```bash
# リポジトリのクローン
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane

# PDKを含めた初期化（Docker自動DL＋PDK構築）
make

# OpenLane GUI確認（任意）
make gui
```
※詳細は OpenLane公式の README.md を参照
※約10〜20GBのディスク容量と安定した回線が必要です

---

## 🧱 プロジェクト構成（本教材）

本教材では、各モジュール（FSM, PID, SoC）ごとに独立したOpenLaneプロジェクトを用意し、  
それぞれで**個別に配置配線→評価→レイアウト可視化**を行います。
```
f_chapter4_openlane/
└── openlane/
├── fsm_engine/
│   ├── config.tcl
│   ├── floorplan.tcl（必要に応じて）
│   └── src/
│       └── fsm_engine.v
├── pid_controller/
│   └── …
└── soc_top/
└── …
```

> 各プロジェクトは `flow.tcl` を用いて個別に実行します。

---

## 📦 config.tcl の最低構成（例：fsm_engine）

```tcl
# openlane/fsm_engine/config.tcl

set ::env(DESIGN_NAME) fsm_engine
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/fsm_engine.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"

set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
> 各プロジェクトは `flow.tcl` を用いて個別に実行します。

---

## 📦 config.tcl の最低構成（例：fsm_engine）

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

## ▶️ 次節に続く

4.2 FSMモジュールの配置配線 にて、
上記プロジェクトを用いた**実際のflow実行手順（openlane CLI）**を紹介します。

---
