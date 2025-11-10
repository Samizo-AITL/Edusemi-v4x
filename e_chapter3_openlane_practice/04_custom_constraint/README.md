---
layout: default
title: 制約ファイルのカスタマイズと設計最適化（OpenLane v2 完全版）
---

# 🧩 制約ファイルのカスタマイズと設計最適化（OpenLane v2 完全版）  
**Constraint Customization and Design Optimization in OpenLane v2**

---

## 📘 概要｜Overview

この章では **OpenLane v2** で使用される制約（constraints）をカスタマイズし、  
**面積・タイミング・配線効率・電力** にどのような影響が出るかを実験的に理解します。

OpenLane v1 時代の `floorplan.tcl` / `placement.cfg` に依存せず、  
**v2 正式仕様（config.tcl + optional constraints）** へ完全対応しています。

---

# ✅ OpenLane v2 の制約ファイル体系（最新版）

OpenLane v2 の制約は **config.tcl が中心**で、  
必要に応じて `.cfg` や `.tcl` を追加して拡張できます。

---

## 📂 **主要ファイル一覧（OpenLane v2 正式仕様）**

| ファイル名 | 役割 | v2 推奨度 |
|-----------|-------|-----------|
| **config.tcl** | ほぼ全ての制約を統合的に記述（🟦 標準） | ✅ 必須 |
| **sdc.tcl** | タイミング制約（setup/hold/clock） | ✅ 必須 |
| **pin_order.cfg** | I/O ピンの順序指定 | ✅ 任意 |
| **macro_placement.cfg** | マクロブロック位置（SoC設計） | ✅ 任意 |
| **pdn.tcl** | 電源配線（PDN）の上書き | ⭕ 上級者向け |
| **floorplan.tcl** | floorplan の詳細カスタム（旧 v1 方式） | ⛔ 基本非推奨（特殊時のみ使用） |

✅ 基本的には **config.tcl と sdc.tcl の 2本柱**  
✅ 必要な場合のみ `.cfg`・`.tcl` を追加する方式に v2 は統一されている

---

# 🗂️ ディレクトリ構成例（v2 正式）

```
designs/inverter/
├── config.tcl
├── sdc.tcl
├── pin_order.cfg
├── macro_placement.cfg
└── runs/
```

---

# ✅ config.tcl に記述する主要パラメータ（OpenLane v2）

OpenLane v2 の floorplan・placement 制約は可能な限り **config.tcl に統一**されている。

---

## 🔧 **Floorplan 制約（重要）**

```tcl
set ::env(FP_CORE_UTIL) "35"
set ::env(FP_ASPECT_RATIO) "1"
set ::env(FP_IO_MODE) "matching"
set ::env(FP_PDN_VPITCH) "153.6"
set ::env(FP_PDN_HPITCH) "153.6"
```

---

## 🔧 **Placement 制約**

```tcl
set ::env(PL_TARGET_DENSITY) "0.60"
set ::env(PL_ROUTABILITY_DRIVEN) "1"
```

---

## 🔧 **Clock / Timing 制約（sdc 併用）**

config.tcl:

```tcl
set ::env(CLOCK_PORT) "a"
set ::env(CLOCK_PERIOD) "10.0"
```

sdc.tcl:

```tcl
create_clock -name core_clk -period 10 [get_ports a]
```

---

# ✅ ピン配置（pin_order.cfg）

```text
# ポート名 方向 配置側
a input  left
y output right
```

---

# ✅ マクロ配置（macro_placement.cfg）

SoC / IP マクロ向け：

```text
macro_name_x macro1 50
macro_name_y macro1 120
macro_orient macro1 R0
```

---

# 🧪 実験例：制約変更が設計に与える影響

---

## ✅ 実験①：クロック制約変更（高速化）

`config.tcl`:

```tcl
set ::env(CLOCK_PERIOD) "5.0"   ;# 200MHz
```

実行：

```bash
flow.tcl -design inverter -tag fast_run
```

観察ポイント：

| 指標 | 影響 |
|------|------|
| ⏱️ Slack | 負の slack が発生しやすい |
| ⚙️ セル数 | Buffer 追加で増加 |
| 🔋 電力 | dynamic power 増加 |
| 🧱 配置・配線 | 混雑率がやや上昇 |

---

## ✅ 実験②：配置密度 (PL_TARGET_DENSITY)

`config.tcl`:

```tcl
set ::env(PL_TARGET_DENSITY) "0.45"
```

効果：

| 密度 | 影響 |
|------|------|
| 低密度（0.4〜0.5） | 配線しやすい・DRC減・面積増 |
| 高密度（0.7〜0.8） | 面積減・配線困難・DRC増 |

---

## ✅ 実験③：IO ピン配置の最適化

`pin_order.cfg` により配線混雑の緩和が可能。

例：

```text
a input left
y output right
```

効果：

- ✅ 配線長の最適化  
- ✅ 交差配線の削減  
- ✅ routing DRC の抑制  

---

# 📈 評価指標（v2 標準レポート）

OpenLane v2 の実行後、以下を観察する：

| 項目 | 参照先 |
|------|--------|
| Cell Count / Area | `reports/synthesis/1-yosys.log` |
| Slack / WNS / TNS | `reports/timing/metrics.csv` |
| Power（total/static/dynamic） | `reports/power/total_power.rpt` |
| Routing（via/length） | `reports/routing/route.rpt` |
| DRC | `reports/signoff/drc.rpt` |

---

# 🎓 教育的意義

| 観点 | 内容 |
|------|------|
| 制約の理解 | ASIC は **constraints-driven design** を理解 |
| 最適化 | 面積・速度・電力のトレードオフ設計を体験 |
| 実務力 | 商用EDAと同等の constraint-driven flow の思考を習得 |

---

# 🔗 関連リンク

- [第2章：RTLからGDSへの実装](../02_rtl_to_gds_flow/README.md)
- [第3章：レポート解析](../03_power_timing_report/README.md)
- [OpenLane Documentation](https://openlane.readthedocs.io/)
