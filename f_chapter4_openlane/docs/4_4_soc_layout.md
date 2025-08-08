---
layout: default
title: 4.4 SoC統合モジュールの実装（FSM + PID）
---

---

# 4.4 SoC統合モジュールの実装（FSM + PID）  
**Implementation of Integrated SoC Module (FSM + PID)**

---

## 🎯 本節の目的｜Purpose of This Section

| 📝 日本語｜Japanese | 📘 English |
|--------------------|-----------|
| FSM＋PIDを統合した `soc_top.v` の配置配線とGDS生成を行う | Perform P&R and GDSII generation for `soc_top.v` |
| 複数モジュール統合に伴う floorplan・配線の最適化を観察 | Observe floorplan and routing for multiple modules |
| SoCレベル設計のI/O配置や制約を把握する | Understand I/O placement and design constraints |

---

## 🛠️ ディレクトリ構成｜Project Directory Structure

以下のように `soc_top` 用プロジェクトを準備します：  
Set up the following structure for the `soc_top` project:

```text
f_chapter4_openlane/
└── openlane/
    └── soc_top/
        ├── config.tcl
        └── src/
            └── soc_top.v
```

> `soc_top.v` includes integrated RTL of FSM and PID.

---

## ⚙️ config.tcl の構成例｜Sample `config.tcl`

```tcl
set ::env(DESIGN_NAME) soc_top
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/soc_top.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 45
set ::env(PL_TARGET_DENSITY) 0.5
```

> 複数モジュール統合のため `FP_CORE_UTIL` を上方調整しています。  
> Core utilization increased due to integration.

---

## 🚀 フロー実行｜Running the Flow

以下のコマンドでOpenLaneを実行：  
Run OpenLane with the following command:

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/soc_top
```

---

## 📂 成果物とレポート構成｜Output Artifacts and Reports

```text
runs/soc_top/
├── config.tcl
├── logs/
├── reports/
│   ├── synthesis/area.rpt
│   ├── signoff/drc.rpt
│   └── signoff/lvs.rpt
└── results/
    └── final/
        ├── gds/soc_top.gds
        ├── def/soc_top.def
        └── verilog/final.v
```

---

## 📊 評価と観察ポイント｜Evaluation Metrics

| ✅ 項目｜Metric | 🔍 内容・目的｜Purpose |
|----------------|------------------------|
| 統合面積<br>Total Area | FSM + PID合計面積との比較 |
| 配線密度<br>Routing Density | 配線混雑とfloorplan調整 |
| I/O配置<br>I/O Placement | I/Oの配置とDRC影響の確認 |

---

## 🖼️ レイアウト可視化｜Layout Visualization

### 🔍 KLayout を使用する場合｜Using KLayout

```bash
klayout runs/soc_top/results/final/gds/soc_top.gds
```

### 🔍 Magic を使用する場合｜Using Magic

```bash
magic -T sky130A.tech runs/soc_top/results/final/gds/soc_top.gds
```

> 各モジュールのレイアウト領域やI/O配置を視覚確認できます。  
> Useful for inspecting layout regions and port placements.

---

## ✅ まとめ｜Summary

| 🇯🇵 日本語 | 🇺🇸 English |
|------------|------------|
| FSMとPIDの統合SoCがOpenLaneでGDS化可能 | FSM and PID SoC can be implemented via OpenLane |
| Floorplanや配線の工夫が重要になる | Floorplan and routing strategy become critical |
| 次節では全モジュールの設計比較・分析を実施 | Next: Compare all modules’ metrics and performance |

---

## 📎 前後の節｜Previous / Next Sections

- ◀️ 前の節｜Previous: [4.3 PIDモジュールの配置配線](./4_3_pid_layout.md)  
- ▶️ 次の節｜Next: [4.5 設計評価レポートと比較](./4_5_evaluation.md)

📚 [🔙 特別編 第4章 README に戻る](../README.md)
