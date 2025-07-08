# 5.6 チップ完成に向けた最終検証ステップ

## 🎯 本節の目的

- SoCレベルのGDS完成後に必要となる最終検証項目を整理する  
- ERC、Antenna Check、Tapeout準備などの実施手順を確認する  
- 完全な製造可能性（tapeout-ready）に向けた設計要件を理解する

---

## 🧪 最終検証ステップの全体像

1. **DRC**（Design Rule Check）
2. **LVS**（Layout vs. Schematic）
3. **ERC**（Electrical Rule Check）
4. **Antenna Check**
5. **Fill Cell確認**
6. **バウンダリ構造チェック（Chip Edge）**
7. **GDS出力・Tapeout条件の確認**

---

## 🔍 ERC：電気的ルールチェック

| チェック内容 | 例 |
|--------------|----|
| 未接続ピンの有無 | 出力ピンのフローティング |
| GND/VDDの短絡・断線 | 電源ネットの不整合 |
| 階層をまたぐ電源接続エラー | Power Pin不一致など |

→ OpenLaneやMagicのエクスポートNetlistで確認可能。

---

## 📏 Antenna Checkとは？

製造時にポリやメタルが露出しすぎると、**帯電破壊**による不良が発生。  
Sky130ではAntennaルールに基づき、ポリの比率や接続順を検証します。

→ OpenLaneで自動挿入 or antenna diodeセルで対策。

---

## 🧱 Fill Cellの確認

- メタル密度を均一化する目的
- `fill_cell`や`tap_cell`をOpenLaneで自動追加
- 特に大面積SoCでのレイアウト均一性が重要

---

## 📦 バウンダリ構造とI/O

- PAD配置、chip boundaryの形成
- Corner CellやI/O Cellの配置が必要
- 実製造でのパッケージ対応を視野に設計

---

## ✅ Tapeout前の最終チェックリスト

| 項目 | チェック |
|------|----------|
| DRC | 全ルールpass |
| LVS | 回路等価性OK |
| ERC | 電源構造とピン構成整合 |
| Fill | 均一なmetal分布確認 |
| Antenna | Diode挿入済 or Pass |
| GDSファイル | 正常に出力・命名・圧縮済 |

---

## ✅ 本節まとめ

- チップ製造に必要な最終チェック項目は複数存在し、それぞれ目的が異なる  
- Sky130 PDKとOpenLaneはこれらの自動化支援機能を備えており、効果的に活用できる  
- 完全なtapeout-ready GDSを得るには、DRC・LVSに加え、ERC/Antenna/Fillの最終整合が必須

---

👉 [戻る：特別編 第5章 README](../README.md)
