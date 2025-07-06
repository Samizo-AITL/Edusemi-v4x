# 🛠️ RTLからGDSへの設計フロー実習

この章では、OpenLaneを用いて **Verilog RTL記述からGDS生成**までの一連のデジタルLSI設計フローを体験します。  
Sky130 PDKと連携し、合成、配置、配線、検証の各ステップを順に実行します。

---

## 📋 使用例：最小構成の`inverter`

以下は、標準的なOpenLane実習の最小単位である `inverter` 設計をベースにします。

---

## 🚦 設計対象（例）

```verilog
module inverter(
    input wire a,
    output wire y
);
    assign y = ~a;
endmodule
```

> ※ より大規模な設計（`gcd`, `picorv32` 等）は後続章で扱います

---

## 🔁 実行手順（基本フロー）

以下のコマンドで、RTLからGDSまで一括実行が可能です：

```bash
cd OpenLane/
make mount
```

その後、Docker内で以下を実行：

```bash
./flow.tcl -design inverter -tag run1
```

実行ステップ（自動処理）：

1. 論理合成（`synthesis`）
2. 初期配置（`floorplan`）
3. 配置最適化（`placement`）
4. クロックツリー合成（`cts`）
5. 配線（`routing`）
6. 物理検証（`drc`, `lvs`）
7. GDS生成（`gds`, `lef`）

---

## 📁 出力ディレクトリ構成（例）

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

## 📈 生成物の例

- `results/gds/inverter.gds`：GDS版下ファイル
- `reports/synthesis/`：セル数・面積・クロック情報
- `reports/routing/`：ワイヤ長・ビア数・電力推定

---

## 🧠 教育的意義

- **RTL→ゲート→レイアウト**のフローを1ステップずつ体験
- 各ステージでのログ・出力ファイルの意味を理解
- 面積・タイミング・DRCエラーなど**設計品質の多面評価**に触れる

---

## 🔗 次のステップ

- [第3章：電力・タイミングレポートの解析へ](../03_power_timing_report/README.md)
