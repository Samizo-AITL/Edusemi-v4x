---
layout: default
title: RTLからGDSへの設計フロー実習（OpenLane v2 完全版）
---

---

# 🛠️ RTLからGDSへの設計フロー実習（OpenLane v2 完全版）  
**RTL-to-GDS Flow Practice Using OpenLane v2 + Sky130A**

---

## 📘 概要｜Overview

この章では、**OpenLane v2（Docker 版）＋ Sky130A PDK** を用いて、  
**Verilog RTL → GDS（レイアウト版下）** を生成する一連の ASIC 実装フローを学びます。

扱う工程は以下の通りです：

- ✅ Synthesis（合成）
- ✅ Floorplan（フロアプラン）
- ✅ Placement（配置）
- ✅ CTS（クロックツリー合成）
- ✅ Routing（配線）
- ✅ Signoff（DRC / LVS）
- ✅ GDS Export（最終版下）

商用EDAと類似したフローを **完全OSS環境** で体験できます。

---

## 📋 使用例｜Design Example : `inverter`

最小構成デザインとして **inverter（反転器）** を使用します。

```verilog
module inverter(
    input wire a,
    output wire y
);
    assign y = ~a;
endmodule
```

---

## 🗂️ ディレクトリ構成（必須）

```
openlane/
 ├── designs/
 │    └── inverter/
 │         ├── config.tcl
 │         └── src/inverter.v
 └── pdks/
      └── sky130A/      ← volare enable sky130A が生成
```

---

## 🔧 事前準備（PDK + Docker）

### ✅ PDK を volare で取得

```bash
pip install --upgrade pip volare
volare enable sky130A
```

---

## ✅ OpenLane v2（Docker）を取得

```bash
docker pull efabless/openlane:2024.09.11
```

---

## ✅ コンテナ起動（設計とPDKをマウント）

```bash
docker run --rm -it \
  -v $HOME/openlane/designs:/openlane/designs \
  -v $HOME/openlane/pdks:/pdks \
  -e PDK_ROOT=/pdks \
  -e PDK=sky130A \
  efabless/openlane:2024.09.11
```

---

# 🔁 実行手順｜Execution Flow（OpenLane v2）

OpenLane v2 では、**flow.tcl** を直接実行します。

---

## ✅ 1. inverter デザインでフロー実行

```bash
flow.tcl -design inverter -tag run1 -overwrite
```

---

# 📈 OpenLane v2 RTL→GDS フロー（正式ステージ）

| ステップ | 説明 | 使用ツール | 出力例 |
|---------|------|-------------|--------|
| 1️⃣ Synthesis | RTL→ゲート合成 | Yosys | `*.synthesis.v` |
| 2️⃣ Floorplan | コア領域・IO配置 | OpenROAD | `*.floorplan.def` |
| 3️⃣ Placement | セルの初期／詳細配置 | OpenROAD | `*.placement.def` |
| 4️⃣ CTS | クロックツリー生成 | OpenROAD | `*.cts.def` |
| 5️⃣ Routing | global/detailed 配線 | OpenROAD | `*.route.def` |
| 6️⃣ Signoff | DRC/LVS（物理・回路検証） | Magic / Netgen | `drc.rpt`, `lvs.rpt` |
| 7️⃣ GDS Export | 製造用 GDS出力 | Magic / KLayout | `inverter.gds` |

---

# 📁 出力ディレクトリ構成（OpenLane v2）

```text
designs/inverter/runs/run1/
├── logs/                   ← 各工程のログ
├── reports/                ← QoRレポート（合成/配置/配線/DRC/LVS）
├── results/
│   ├── synthesis/
│   ├── floorplan/
│   ├── placement/
│   ├── cts/
│   ├── routing/
│   ├── signoff/            ← DRC/LVS
│   └── final/              ← ★最終成果物
│        └── gds/inverter.gds
└── config.tcl（コピー）
```

---

# 📈 出力物｜Generated Artifacts

| ファイル | 役割 |
|----------|------|
| `results/final/gds/inverter.gds` | 製造用 GDSII 版下 |
| `results/synthesis/inverter.synthesis.v` | 合成後ネットリスト |
| `signoff/drc.rpt` | DRC（設計ルール）検証結果 |
| `signoff/lvs.rpt` | LVS（回路一致）検証結果 |
| `routing/inverter.spef` | 配線遅延情報（STAで使用） |

---

# 🎓 教育的意義｜Educational Insights

- ✅ OSS で **商用EDAに非常に近い ASIC フローを学ぶ**  
- ✅ RTL→GDS の工程のつながりを一貫して理解できる  
- ✅ Sky130A は教育・研究・MPWに最適なオープンPDK  
- ✅ 各工程のログ・レポートを解析することで **設計品質（QoR）** を学べる  

---

# 🔗 次のステップ

➡️ [📊 第3章：電力・タイミング・面積レポート解析](../03_power_timing_report/README.md)
