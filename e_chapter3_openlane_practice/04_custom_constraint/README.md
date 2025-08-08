---
layout: default
title: 制約ファイルのカスタマイズと設計最適化
---

---

# 🧩 制約ファイルのカスタマイズと設計最適化  
**Constraint Customization and Design Optimization in OpenLane**

---

## 📘 概要｜Overview

この章では、OpenLane設計フローにおいて使用される各種**制約ファイル（constraints）**をカスタマイズし、  
**面積・タイミング・配線効率・電力などの設計指標への影響**を体験的に学びます。

This section helps you understand how modifying design constraints  
(floorplan, timing, pin placement, etc.) impacts area, delay, routing, and power.

---

## 🎯 目的｜Objectives

- ✅ デフォルト設定に依存せず、**自分で制約を調整・適用**できるようになる  
- ✅ 各種制約の変更が**設計結果にどのように影響するかを分析**できる  
- ✅ 設計意図に合わせたカスタマイズと**設計品質のトレードオフ**を理解する  

---

## 📄 主な制約ファイル｜Main Constraint Files

| ファイル名 | 役割（Role） |
|------------|--------------------------|
| `floorplan.tcl` | コア領域・マージン・ピン密度などの初期配置制約 |
| `placement.cfg` | 初期セル配置・密度制御のカスタム設定 |
| `clock_constraints.tcl` | クロック周波数・ツリー生成に関する制約 |
| `pin_order.cfg` | I/Oピンの順序指定と端配置制御 |
| `macro_placement.cfg` | マクロブロックの位置明示（SoC設計向け） |
| `sdc.tcl` | 時間制約（タイミング）ファイル：セットアップ／ホールド |

---

## 🧪 実験例①：クロック制約を変更

```tcl
# designs/inverter/config.tcl の一部抜粋
set ::env(CLOCK_PERIOD) "10.0" ;# 例：100MHz（10ns） → 高速化で "5.0" に変更（200MHz）
```

再実行例：

```bash
./flow.tcl -design inverter -tag run2_freq200MHz
```

| 評価ポイント | 観察内容例 |
|--------------|------------|
| ⏱️ タイミング | Slackの悪化、Violation発生の有無 |
| ⚙️ セル数 | 高速化に伴うセル増加（Buffer挿入など） |
| 🔋 電力 | 消費電力の増加傾向（動的電力上昇） |

---

## 🧪 実験例②：ピン配置を手動指定

```text
# pin_order.cfg の例
a input left
y output right
```

| 効果 | 検証視点 |
|------|----------|
| 📏 配線長の最適化 | 配線密度・層数の変化を確認 |
| ❌ DRC違反の減少 | 配線混雑の緩和／層配置改善 |
| 🧭 レイアウト可読性の向上 | トポロジの意図的制御に寄与 |

---

## 📂 フォルダ構成例｜Example Folder Layout

```text
designs/inverter/
├── config.tcl             # 全体設定ファイル
├── floorplan.tcl          # 初期配置制約
├── pin_order.cfg          # I/Oピン配置順
├── sdc.tcl                # 時間制約ファイル
└── runs/                  # 実行結果の格納ディレクトリ
```

---

## 📈 評価指標｜Design Metrics to Observe

- 🔢 総セル数・面積（synthesis / placement）
- ⏳ タイミングSlack（setup / hold）
- ⚡ Power Report（total / dynamic / leakage）
- 🧱 DRC / 配線層使用率（routing logs）

---

## 🧠 教育的意義｜Educational Significance

| ✏️ 観点 | 内容 |
|---------|------|
| 📐 制約設計 | **設計制約＝レイアウト品質の起点**であると理解 |
| ⚙️ フィードバック設計 | 面積・遅延・消費電力などの出力に基づく**調整ループの体験** |
| 🧩 ブラックボックス脱却 | 商用EDAに頼らず**構造を制御する設計力**を育成 |

---

## 🔗 関連リンク｜Related Sections

- [📘 第2章：RTLからGDSへの設計実習](../02_rtl_to_gds_flow/README.md)
- [📘 第3章：電力・タイミングレポートの解析](../03_power_timing_report/README.md)
- [🏠 第3章トップに戻る](../README.md)

---

## 📝 備考｜Notes

- `config.tcl` では環境変数 `::env()` を用いて制約を明示的に変更可能
- バージョンや設計対象により `.tcl` / `.cfg` ファイル構成は一部異なる場合あり
- 複数の `run tag` を使って比較実験することで設計意図と結果の整合性が深まる

---
