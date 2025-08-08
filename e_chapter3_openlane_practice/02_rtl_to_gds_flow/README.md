---
layout: default
title: RTLからGDSへの設計フロー実習　
---

---

# 🛠️ RTLからGDSへの設計フロー実習  
**RTL-to-GDS Flow Practice Using OpenLane**

---

## 📘 概要｜Overview

この章では、OpenLaneを用いて **Verilog RTLからGDS生成までの設計フロー**を実体験します。  
Sky130 PDKと連携し、**合成（synthesis）→ 配置（placement）→ 配線（routing）→ 検証（DRC/LVS）**までの工程を順に実行します。

This chapter walks through a full **RTL-to-GDS digital design flow** using OpenLane,  
from Verilog source code to GDS layout, integrated with the Sky130 PDK.

---

## 📋 使用例｜Design Example: `inverter`

最小構成の練習用として、以下のような単純な **反転器回路（inverter）** を対象にします。

```verilog
module inverter(
    input wire a,
    output wire y
);
    assign y = ~a;
endmodule
```

> 💡 より大規模な設計（例：`gcd`, `picorv32`）は後続章で扱います。

---

## 🔁 実行手順｜Execution Flow

### 1. OpenLaneリポジトリへ移動し、Dockerを起動

```bash
cd OpenLane/
make mount
```

### 2. Docker内でフロー実行（例：`inverter`を`run1`タグで実行）

```bash
./flow.tcl -design inverter -tag run1
```

このコマンドにより、以下のステップが**自動的に一括処理**されます：

| ステップ | 説明 | 使用ツール |
|----------|------|------------|
| ① Synthesis | 論理合成 | `yosys` |
| ② Floorplan | 初期配置設計 | `init_floorplan` |
| ③ Placement | セル配置 | `OpenROAD` |
| ④ CTS | クロックツリー合成 | `OpenROAD` |
| ⑤ Routing | 自動配線 | `OpenROAD` |
| ⑥ DRC/LVS | 物理検証 | `Magic`, `Netgen` |
| ⑦ GDS Output | GDSファイル出力 | `Magic`, `KLayout` |

---

## 📁 出力ディレクトリ構成｜Output Directory Layout

```text
designs/inverter/runs/run1/
├── results/
│   ├── synthesis/
│   ├── floorplan/
│   ├── placement/
│   ├── routing/
│   ├── gds/
│   └── reports/
└── logs/
```

---

## 📈 出力ファイル例｜Example Artifacts

| ファイルパス | 内容 |
|--------------|------|
| `results/gds/inverter.gds` | GDSレイアウト（版下データ） |
| `reports/synthesis/synthesis.log` | 論理合成結果のログ |
| `reports/placement/placement.rpt` | 配置段階での統計情報 |
| `reports/routing/route.rpt` | ワイヤ長・ビア数・電力推定 |
| `reports/signoff/` | DRC/LVSチェック結果（設計ルールの整合性） |

---

## 🎓 教育的意義｜Educational Insights

- ✅ RTL → ゲートネットリスト → 配置・配線 → GDS の流れを実感  
- ✅ 各工程の目的・役割・制約を理解  
- ✅ 出力レポートを通じて **設計品質（QoR）を多角的に評価**  
- ✅ 商用フローに近いプロセスを **無償ツール**で実践可能  

---

## 🔗 次のステップ｜Next Step

➡️ [📊 第3章：電力・タイミングレポート解析へ](../03_power_timing_report/README.md)

---
