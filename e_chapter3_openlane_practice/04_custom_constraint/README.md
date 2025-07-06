# 🧩 制約ファイルのカスタマイズと設計最適化

この章では、OpenLane設計フローにおける制約ファイル（`floorplan`, `timing`, `pin placement` など）を調整し、**設計結果への影響を体験的に理解**します。

---

## 🎯 目的

- デフォルト設定に依存せず、**設計制約を自ら編集・適用**する力を養う
- 制約変更による**面積・タイミング・配線長・電力**などへの影響を観察
- カスタマイズ可能な設計への理解と応用力を高める

---

## 📄 主な制約ファイル

| ファイル名 | 役割 |
|------------|------|
| `floorplan.tcl` | コア領域・ピン間隔・マージンなどの初期配置制約 |
| `placement.cfg` | セルの初期位置や密度制約 |
| `clock_constraints.tcl` | クロック定義・クロックツリー制約 |
| `pin_order.cfg` | I/Oピンの配置順序 |
| `macro_placement.cfg` | マクロブロックの位置指定（SoC設計時） |
| `sdc.tcl` | 時間制約ファイル（セットアップ・ホールド） |

---

## 🛠️ 実験例：クロック周波数を変更

```tcl
# designs/inverter/config.tcl の一部
set ::env(CLOCK_PERIOD) "10.0" ;# 100MHz → 200MHzにしたいなら "5.0"
```

再実行：

```bash
./flow.tcl -design inverter -tag run2_freq200MHz
```

→ タイミング違反が発生するか？セル数や消費電力は変わるか？

---

## 🧪 実験例：ピン配置の制御

```text
pin_order.cfg
--------------
a input left
y output right
```

→ 配線長・層数に変化あり  
→ DRC違反や配線混雑の緩和確認

---

## 📚 フォルダ構成（例）

```text
designs/inverter/
├── config.tcl
├── floorplan.tcl
├── pin_order.cfg
├── sdc.tcl
└── runs/
```

---

## 📈 評価指標

- 総セル数・面積・タイミングSlack
- DRCエラー数・配線層利用率
- Power Report（静的／動的）

---

## 🧠 教育的意義

- 「制約＝設計品質の出発点」であることを体験的に学ぶ
- ブラックボックス設計から脱却し、**構造制御の重要性**を理解
- 実設計に近い「設計意図とレイアウトの整合性」を学習

---

## 🔗 関連章

- [第2章：RTLからGDSへの設計実習](../02_rtl_to_gds_flow/README.md)
- [第3章：電力・タイミングレポートの解析](../03_power_timing_report/README.md)

---

## 📝 備考

- 制約の変更は `config.tcl` または個別 `.tcl/.cfg` で反映
- パラメトリックに複数Runを実行・比較することで理解が深まる
