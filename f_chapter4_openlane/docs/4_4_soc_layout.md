# 4.4 SoC統合モジュールの実装（FSM + PID）

## 🎯 本節の目的

- FSMおよびPIDを統合した `soc_top.v` を配置配線し、GDSII を生成する  
- 複数モジュール統合における floorplan・面積・配線のスケーリングを観察する  
- SoCレベルの物理設計課題（I/O配置、リソース制約）に触れる

---

## 🛠️ ディレクトリ構成の準備

以下のように `soc_top` 用のプロジェクトディレクトリを構成します：

```
f_chapter4_openlane/
└── openlane/
    └── soc_top/
        ├── config.tcl
        └── src/
            └── soc_top.v
```

`soc_top.v` には、FSMとPIDモジュールのトップ統合RTLが含まれます。

---

## 📦 config.tcl（最小構成例）

```tcl
set ::env(DESIGN_NAME) soc_top
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/soc_top.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 45
set ::env(PL_TARGET_DENSITY) 0.5
```

---

## 🚀 flow.tcl の実行手順

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/soc_top
```

---

## 📂 成果物構成とレポート出力

```
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

## 📊 評価と観察ポイント

| 項目        | 内容                                                  |
|-------------|-------------------------------------------------------|
| ✅ 統合面積 | FSM + PID 単体面積の合算に対する増減を観察             |
| ✅ 配線密度 | クロックや制御信号配線の混雑度、密度の最適化           |
| ✅ I/O配置  | 統合モジュールにおけるI/O port配置とDRC違反の抑制確認 |

---

## 🖼️ レイアウト可視化手順

```bash
klayout runs/soc_top/results/final/gds/soc_top.gds
```

または

```bash
magic -T sky130A.tech runs/soc_top/results/final/gds/soc_top.gds
```

---

## ✅ まとめ

- FSMとPIDを統合したSoC構成もOpenLaneで一括自動配置配線が可能  
- 複数モジュール統合により floorplan・配線戦略が重要となる  
- 次節では FSM / PID / SoC 各設計の物理評価を比較・分析する

---

👉 [4.5 設計評価レポートと比較へ進む](4_5_evaluation.md)
