---
layout: default
title: 4.3 PIDモジュールの配置配線（Place & Route）
---

---

# 4.3 PIDモジュールの配置配線（Place & Route）  
**Place-and-Route of PID Controller Module**

---

## 🎯 本節の目的｜Purpose of This Section

| 📝 日本語｜Japanese | 📘 English |
|----------------------|-----------|
| PIDモジュールをOpenLaneで配置配線し、GDSIIまで生成 | Run place-and-route of PID controller using OpenLane |
| FSMモジュールとの設計条件統一 | Use same design conditions as FSM for fair comparison |
| 面積・DRC・タイミング等のパラメータ取得 | Obtain physical metrics such as area, DRC, timing |

---

## 🛠️ ディレクトリ構成の準備｜Directory Structure

以下のように `pid_controller` 用プロジェクトを構成します：  
Set up your project directory for the PID controller:

```text
f_chapter4_openlane/
└── openlane/
    └── pid_controller/
        ├── config.tcl
        └── src/
            └── pid_controller.v
```

---

## ⚙️ `config.tcl` の最小構成｜Minimal `config.tcl`

PIDモジュール用の `config.tcl` は以下の通りです：  
Sample configuration for PID:

```tcl
set ::env(DESIGN_NAME) pid_controller
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/pid_controller.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
```

> FSMと同条件で設計評価を行います（公平な比較のため）

---

## 🚀 フロー実行｜Running the Flow

OpenLaneディレクトリに移動し、以下のように実行：  
Execute the flow with the following command:

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/pid_controller
```

> `-tag`や`-run_path`オプションで出力ディレクトリ指定も可能です。

---

## 📂 成果物とレポート構成｜Output Artifacts and Reports

```text
runs/pid_controller/
├── config.tcl
├── logs/
├── reports/
│   ├── synthesis/area.rpt
│   ├── signoff/drc.rpt
│   └── signoff/lvs.rpt
└── results/
    └── final/
        ├── gds/pid_controller.gds
        ├── def/pid_controller.def
        └── verilog/final.v
```

---

## 📊 評価観点と比較ポイント｜Evaluation Metrics

| ✅ 評価項目｜Metric | 🔍 内容・目的｜Purpose |
|------------------|------------------------|
| DRCチェック<br>DRC | `drc.rpt` にて違反数 0 を確認 |
| 面積比較<br>Area | FSMと比較し演算器の影響を評価 |
| タイミング<br>Timing | Slack収束と遅延最小化を確認 |

---

## 🖼️ レイアウトの可視化｜Layout Visualization

### 🔍 KLayoutを使用する場合｜Using KLayout

```bash
klayout runs/pid_controller/results/final/gds/pid_controller.gds
```

### 🔍 Magicを使用する場合｜Using Magic

```bash
magic -T sky130A.tech runs/pid_controller/results/final/gds/pid_controller.gds
```

> 配置密度・I/O配置・ロジック構造を視覚的に確認可能  
> Useful for checking placement density and structure

---

## ✅ まとめ｜Summary

| 🇯🇵 日本語 | 🇺🇸 English |
|------------|------------|
| PID回路もFSM同様に自動GDS生成可能であることを確認 | Confirmed GDSII generation for PID module |
| FSMに比べ演算器が多く、面積・セル数が増加 | More logic = larger area compared to FSM |
| 次節でFSM+PID統合SoCを実装 | Next: Integration of FSM + PID into SoC layout |

---

## 📎 前後の節｜Previous / Next Sections

- ◀️ 前の節｜Previous: [4.2 FSMモジュールの配置配線](./4_2_fsm_layout.md)  
- ▶️ 次の節｜Next: [4.4 SoC統合モジュールの実装](./4_4_soc_layout.md)

📚 [🔙 特別編 第4章 README に戻る](../README.md)
