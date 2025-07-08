# 4.3 PIDモジュールの配置配線（Place & Route）

## 🎯 本節の目的

- PIDモジュール（`pid_controller.v`）を OpenLane で配置配線し、GDSII まで生成する  
- FSMモジュールとの比較評価のための設計条件統一  
- 面積・タイミング・DRC などの物理設計パラメータを取得する

---

## 🛠️ ディレクトリ構成の準備

以下のように `pid_controller` 用のプロジェクトディレクトリを構成します：

```
f_chapter4_openlane/
└── openlane/
    └── pid_controller/
        ├── config.tcl
        └── src/
            └── pid_controller.v
```

---

## 📦 config.tcl（最小構成例）

```tcl
set ::env(DESIGN_NAME) pid_controller
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/pid_controller.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
```

---

## 🚀 flow.tcl の実行手順

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/pid_controller
```

---

## 📂 成果物構成とレポート出力

```
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

## 📊 評価ポイントと比較観点

| 項目        | 内容                                                         |
|-------------|--------------------------------------------------------------|
| ✅ DRC      | DRC違反数が 0 であること                                     |
| ✅ 面積     | FSMとの相対比較。算術演算の分だけインスタンス数は多くなる想定 |
| ✅ タイミング | Slack 確保とタイミング収束                                   |

---

## 🖼️ レイアウト可視化手順

```bash
klayout runs/pid_controller/results/final/gds/pid_controller.gds
```

または

```bash
magic -T sky130A.tech runs/pid_controller/results/final/gds/pid_controller.gds
```

---

## ✅ まとめ

- PID制御回路もFSM同様にOpenLaneで自動配置配線が可能  
- 計算ロジックの複雑性に応じた面積・インスタンス増加を観察  
- 次節では FSM + PID 統合SoC を物理設計対象とする

---

👉 [4.4 SoC統合モジュールの実装へ進む](4_4_soc_layout.md)
