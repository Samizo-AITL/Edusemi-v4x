---
layout: default
title: 4.2 FSMモジュールの配置配線（Place & Route）
---

---

# 4.2 FSMモジュールの配置配線（Place & Route）  
**Place-and-Route of FSM Module**

---

## 🎯 本節の目的｜Purpose of This Section

| 📝 日本語｜Japanese | 📘 English |
|----------------------|-----------|
| FSMモジュールをOpenLaneで配置配線しGDSII生成 | Run place-and-route of FSM module using OpenLane |
| `config.tcl` による最小構成のflowを確認 | Execute the flow with minimal `config.tcl` |
| 面積・DRC・タイミングなどをレポートで確認 | Analyze reports on area, DRC, and timing |

---

## 🛠️ ディレクトリ構成の準備｜Directory Structure

以下のように FSM 用のプロジェクト構成を準備します：  
Set up your FSM project directory as follows:

```text
f_chapter4_openlane/
└── openlane/
    └── fsm_engine/
        ├── config.tcl
        └── src/
            └── fsm_engine.v
```

> `fsm_engine.v` は特別編 第3章の FSM RTL を流用します。  
> Use the FSM RTL design from Chapter 3.

---

## ⚙️ `config.tcl` の最小構成｜Minimal `config.tcl`

以下は FSM の簡易設定例です：  
Here is an example of a minimal configuration file for FSM:

```tcl
set ::env(DESIGN_NAME) fsm_engine
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/fsm_engine.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"

set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
```

> ⚠️ `CLOCK_PORT` は仮に `clk` として指定（FSMに明示クロックがない場合も必要）

---

## 🚀 フローの実行｜Running the Flow

OpenLaneディレクトリに移動し、以下のように実行：  
Run OpenLane flow using:

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/fsm_engine
```

> 必要に応じて `-tag` や `-run_path` で出力先を変更可能です。

---

## 📂 成果物とレポート構成｜Output Structure and Reports

```text
runs/fsm_engine/
├── config.tcl
├── logs/
├── reports/
│   ├── synthesis/area.rpt
│   ├── signoff/drc.rpt
│   └── signoff/lvs.rpt
└── results/
    └── final/
        ├── gds/fsm_engine.gds
        ├── def/fsm_engine.def
        └── verilog/final.v
```

---

## 📊 評価項目と確認ポイント｜Evaluation Metrics

| ✅ 項目｜Metric | 🔍 確認内容｜Check Points |
|------------------|---------------------------|
| 論理合成<br>Synthesis | `area.rpt` にてセル数・合成結果確認 |
| DRCチェック<br>DRC | `drc.rpt` で違反 0 を目指す |
| LVS検証<br>LVS | `lvs.rpt` で論理とレイアウトの一致を確認 |
| タイミング<br>Timing | SlackやViolationの有無を確認 |

---

## 🖼️ レイアウトの可視化｜GDS Layout Visualization

### 🔍 KLayoutの場合｜Using KLayout

```bash
klayout runs/fsm_engine/results/final/gds/fsm_engine.gds
```

### 🔍 Magicの場合｜Using Magic

```bash
magic -T sky130A.tech runs/fsm_engine/results/final/gds/fsm_engine.gds
```

> 配置状態、セル密度、I/O配置などの視覚確認に最適  
> Useful to inspect placement, density, I/O locations visually

---

## ✅ まとめ｜Summary

| 日本語｜Japanese | English |
|------------------|---------|
| FSMモジュールの GDSII 自動生成を確認 | Confirmed GDSII generation from FSM RTL |
| `config.tcl` 設定と `flow.tcl` 実行だけで完結 | Minimal configuration enables full flow |
| 次節では PID モジュールへの展開へ | Next, move on to PID module design |

---

## 📎 前後の節｜Previous / Next Sections

- ◀️ 前の節｜Previous: [4.1 OpenLane導入とプロジェクト構成](./4_1_openlane_intro.md)  
- ▶️ 次の節｜Next: [4.3 PIDモジュールの配置配線](./4_3_pid_layout.md)

📚 [🔙 特別編 第4章 README に戻る](../README.md)
