---
layout: default
title: 5.6 チップ完成に向けた最終検証ステップ
---

---

# 🧪 5.6 チップ完成に向けた最終検証ステップ  
**Final Verification Toward Tapeout**

---

## 🎯 本節の目的｜Objectives

- **GDS完成後に必要な最終検証項目**を体系的に整理する  
  **Understand the final verification items required before chip tapeout**
- **ERC・Antenna Check・Fill構造などの要点**を把握する  
  **Learn key checks such as ERC, antenna effect, and fill structure**
- **tapeout-ready GDS**を目指した整合性の取り方を理解する  
  **Grasp how to ensure manufacturability before final tapeout**

---

## 🧪 最終検証ステップ一覧｜Final Sign-off Checklist

| ✅ **検証ステップ**<br>Check Step | 📋 **内容概要**<br>Description |
|----------------------|------------------------------|
| **DRC** | 物理ルール検証<br>Design Rule Check |
| **LVS** | 論理等価性検証<br>Layout vs Schematic |
| **ERC** | 電源・ピンの整合性確認<br>Electrical Rule Check |
| **Antenna Check** | 帯電破壊リスク確認<br>Plasma charge damage check |
| **Fill Cell確認** | メタル密度均一化<br>Metal density equalization |
| **Boundary構造** | PADとChipエッジ確認<br>Chip I/O and corner structure |
| **GDS整合性** | 出力ファイル・命名・圧縮など<br>GDS output readiness |

---

## 🔍 ERC｜Electrical Rule Check

| 🔍 **チェック項目**<br>Item | 🛠️ **例**<br>Examples |
|----------------------|------------------------------|
| 未接続ピン | フローティング出力がないか |
| 電源の短絡・断線 | GND/VDDネットが正しく接続されているか |
| 階層電源の整合性 | 上位モジュールとのPower Pin一致 |

📌 **OpenLaneまたはMagic抽出Netlist**を用いて確認可能です。

---

## ⚡ Antenna Check｜Antenna効果対策

- **製造中の帯電破壊**を防ぐための重要チェック  
- ポリやメタルが長く露出していると酸化膜が破壊されるリスク  
- 対策として：
  - `antenna diode`セルの挿入
  - OpenLaneのAntenna自動チェックを使用

```tcl
set ::env::ANTENNA_CHECK_FULL true
```

---

## 🧱 Fill Cell確認｜Metal Density Equalization

- 配線密度のムラを防ぎ、**CMP工程での平坦性確保**  
- 自動的に `fill_cells`, `tap_cells` を追加可能（OpenLane対応）

```tcl
set ::env::FILL_INSERTION true
```

📌 特に**大面積のSoC**ではこの処理が重要です。

---

## 📐 Chip Boundary構造の確認

| ⚙️ **要素** | 💡 **内容** |
|-------------|------------|
| PAD配置     | 入出力ピンとその保護セル配置 |
| Corner Cell | Chip角部に必須のセル配置 |
| I/O Tap     | 境界付近の電源整合用セル |

📦 **パッケージ実装**との整合を視野に、正確な配置が求められます。

---

## 📋 Tapeout前のチェックリスト｜Final Tapeout Checklist

| 📌 **項目**<br>Item | ✅ **チェック内容**<br>What to Check |
|-------------|------------------------------|
| DRC | All physical rules are satisfied |
| LVS | Logical equivalence confirmed |
| ERC | Power, pins, unconnected nets |
| Fill Cell | Metal density balanced |
| Antenna | No violation or diode inserted |
| GDS | Proper output, compression, naming |

---

## ✅ 本節まとめ｜Summary

- **最終検証は、製造に耐えるチップかどうかを決定づける重要工程**  
  **Final verification ensures manufacturable, reliable chip designs**
- Sky130 + OpenLane により、多くのチェックが**自動化可能**  
  **Most checks can be automated in the Sky130 flow**
- **GDS出力前にERC/Antenna/Fillを含む包括的チェック**が必要  
  **Include ERC, antenna, and fill structure in your final sign-off**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [5.5 DFM設計：量産対応のためのレイアウト指針](5_5_dfm_guideline.md)  
- 🏠 [特別編 第5章 README に戻る](README.md)
