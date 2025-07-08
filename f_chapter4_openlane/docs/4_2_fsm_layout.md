# 4.2 FSMモジュールの配置配線（Place & Route）

## 🎯 本節の目的

- FSMモジュール（`fsm_engine.v`）を OpenLane で配置配線し、GDSII まで生成する  
- `config.tcl` を用いた最小構成で flow を実行する  
- 面積・DRC・タイミングなどの基本的なレポートを確認する

---

## 🛠️ ディレクトリ構成の準備

以下のように `fsm_engine` 用のプロジェクトディレクトリを構成します：

```
f_chapter4_openlane/
└── openlane/
    └── fsm_engine/
        ├── config.tcl
        └── src/
            └── fsm_engine.v
```

`fsm_engine.v` は、特別編 第3章で設計したFSM回路を流用します。

---

## 📦 config.tcl（最小構成例）

```tcl
set ::env(DESIGN_NAME) fsm_engine
set ::env(VERILOG_FILES) [glob $::env(DESIGN_DIR)/src/fsm_engine.v]
set ::env(CLOCK_PORT) "clk"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(FP_CORE_UTIL) 30
set ::env(PL_TARGET_DENSITY) 0.5
```

※ `CLOCK_PORT` は必須です。FSM内に明示的なクロックがない場合でも、ポート名 `clk` を仮定して記述してください。

---

## 🚀 flow.tcl の実行手順

OpenLane のルートディレクトリに移動して、以下のコマンドを実行します：

```bash
cd OpenLane/
./flow.tcl -design ../f_chapter4_openlane/openlane/fsm_engine
```

※ 必要に応じて `-run_path` や `-tag` オプションで出力ディレクトリを変更可能です。

---

## 📂 成果物構成とレポート出力

```
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

## 📊 評価項目と確認ポイント

| 項目        | 確認内容                                              |
|-------------|-------------------------------------------------------|
| ✅ 論理合成 | `area.rpt` にてセル面積・インスタンス数を確認         |
| ✅ DRC      | `drc.rpt` を確認し、違反数が 0 であることを目標とする |
| ✅ LVS      | `lvs.rpt` で論理とレイアウトの一致を確認              |
| ✅ タイミング | Slackの有無、Violationの有無を確認                    |

---

## 🖼️ レイアウト可視化手順

### 🔍 KLayout を使用する場合：

```bash
klayout runs/fsm_engine/results/final/gds/fsm_engine.gds
```

### 🔍 Magic を使用する場合（Sky130用）：

```bash
magic -T sky130A.tech runs/fsm_engine/results/final/gds/fsm_engine.gds
```

※ 配置されたステート、セル密度、I/O配置などを視覚的に確認できます。

---

## ✅ まとめ

- FSMモジュール単体を OpenLane で GDSII まで自動実装可能であることを確認  
- `config.tcl` の簡潔な設定と `flow.tcl` の実行でフローが完結  
- 次節では PID モジュールの実装へと進み、比較評価を行います

---

👉 [4.3 PIDモジュールの配置配線へ進む](4_3_pid_layout.md)
