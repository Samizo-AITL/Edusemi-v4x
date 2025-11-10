# 🛠️ 06_openlane_first_run  
**OpenLane 初回実行ガイド（中厚版・最小フロー）**  
*OpenLane First Run Guide (Mid-Level / Minimal Flow)*

---

## 📘 概要｜Overview
本節では、OpenLane を **初めて実行するユーザー向け**に、  
最小の Verilog → GDS フロー（synthesis → floorplan → placement → routing → GDS）を  
確実に完走させるための手順をまとめます。  
*This section is a minimal, reliable guide for running OpenLane for the first time: from Verilog to GDS.*

---

# ✅ 1. ディレクトリ構成｜*Directory Structure*
OpenLane では **固定構造**が必要です。  

```
~/openlane/
 ├── pdks/
 └── designs/
       └── simple_inv/
            ├── config.tcl
            └── src/
                 └── inverter.v
```

---

# ✅ 2. テスト用 RTL を準備｜*Prepare Test RTL*

`designs/simple_inv/src/inverter.v`

```verilog
module inverter (
    input  wire a,
    output wire y
);
    assign y = ~a;
endmodule
```

---

# ✅ 3. config.tcl を準備｜*Create config.tcl*

`designs/simple_inv/config.tcl`

```tcl
set ::env(DESIGN_NAME) "inverter"
set ::env(VERILOG_FILES) "./src/inverter.v"
set ::env(CLOCK_PERIOD) "10.0"
set ::env(CLOCK_PORT) "a"
```

必要最低限に絞った設定。  
*A minimal configuration file for a clean first run.*

---

# ✅ 4. OpenLane コンテナを起動｜*Run OpenLane Container*

```bash
docker run --rm -it   -v "$HOME/openlane/pdks":/pdks   -v "$HOME/openlane/designs":/openlane/designs   -e PDK_ROOT=/pdks   -e PDK=sky130A   efabless/openlane:2024.09.11 bash
```

---

# ✅ 5. フローを実行｜*Run the Flow*

```bash
flow.tcl -design simple_inv -overwrite
```

成功すると：

```
runs/RUN_<timestamp>/results/final/gds/inverter.gds
```

---

# ✅ 6. 生成物｜*What Gets Generated*

| ファイル | 説明 |
|----------|------|
| `inverter.synthesis.v` | 合成後 RTL |
| `inverter.floorplan.def` | フロアプラン |
| `inverter.placement.def` | 位置配置 |
| `inverter.route.def` | 配線結果 |
| `inverter.gds` | 最終 GDS |

---

# ✅ 7. Mermaid 図：最小フロー｜*Minimal Flow Diagram*

```mermaid
graph LR
    A[RTL Verilog] --> B[Synthesis]
    B --> C[Floorplan]
    C --> D[Placement]
    D --> E[Routing]
    E --> F[GDS Export]

    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#f1f8e9,stroke:#2e7d32
    style C fill:#fffde7,stroke:#f9a825
    style D fill:#ffecb3,stroke:#ef6c00
    style E fill:#fce4ec,stroke:#c2185b
    style F fill:#ede7f6,stroke:#4527a0
```

---

# ✅ 8. よくあるエラー｜*Common Issues*

| メッセージ | 原因 | 対処 |
|------------|------|------|
| `PDK not found` | パス不一致 | `-e PDK_ROOT=/pdks` |
| `No such file inverter.v` | パス誤り | `VERILOG_FILES` を修正 |
| `flow.tcl: command not found` | コンテナ未起動 | Docker の中で実行 |
| `Magic drc` エラー | 初回では正常 | 最小例は軽微エラーでもOK |

---

# ✅ 9. チェックリスト｜*Checklist*

| 項目 | OK? |
|------|-----|
| simple_inv フォルダ作成 | ✅ |
| inverter.v 作成 | ✅ |
| config.tcl 作成 | ✅ |
| Docker + OpenLane 起動 | ✅ |
| フロー完走 | ✅ |
| GDS 生成 | ✅ |

---

## 👤 Author
三溝 真一（Shinichi Samizo）  
GitHub: https://github.com/Samizo-AITL
