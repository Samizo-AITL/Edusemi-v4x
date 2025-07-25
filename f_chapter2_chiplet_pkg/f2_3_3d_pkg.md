# 2.3 3D積層技術：TSVとハイブリッドボンディング

## 🏗️ 3D積層とは？

3Dパッケージングとは、**複数のチップを垂直方向に積層し、TSVやバンプで直接接続する実装技術**です。以下のような方式があります：

- TSV（Through Silicon Via）による**貫通配線**
- Hybrid Bondingによる**配線層同士の直接接合**
- μ-bump積層による**階層接続**

---

## 🔩 TSV：スルーシリコンビア

### ✦ 概要

- シリコン基板を**縦方向に貫通する導通ビア**
- 直径 3–10 µm、深さ 50–150 µm（AR > 10）

### ✦ 形成プロセス概要

1. 深堀りエッチング（DRIE）
2. 絶縁層形成（SiO₂）
3. バリア・シード層堆積（TaN, Cu）
4. Cu電解めっき → CMP → メタル露出

### ✦ 利点と課題

| 項目 | 内容 |
|------|------|
| 利点 | 高密度配線／短遅延／小面積 |
| 課題 | 歩留まり／熱拡散／応力管理（Cracking） |

---

## ⚡ Hybrid Bonding（ハイブリッドボンディング）

### ✦ 原理

- **金属-金属接合と絶縁体-絶縁体接合を同時**に実現
- 中間層不要の「ダイレクトボンド」技術

### ✦ 代表技術

| 技術名 | 特徴 | 採用例 |
|--------|------|--------|
| Direct Cu-Cu Bonding | 高密度・極小ピッチ | TSMC SoIC, Sony CIS |
| DBI (Direct Bond Interconnect) | バンプレスで高速伝送 | Xperi, Intel Foveros Direct |

### ✦ 技術比較（μ-bump vs Hybrid）

| 項目 | μ-bump接続 | Hybrid Bonding |
|------|-------------|----------------|
| ピッチ | 40–100 µm | 1–10 µm |
| 対応周波数 | ～10 GHz | ～40 GHz以上 |
| 結合層 | バンプ＋接着層 | 接着層なし（密着） |

---

## 🧊 熱とテストの制約

| 項目 | 課題 | 解決策例 |
|------|------|----------|
| 熱 | 下層チップが放熱しにくい | サーマルビア、薄化・熱拡散板 |
| テスト | 中間層アクセス困難 | Built-In Self-Test（BIST）やモジュール単体テストの工夫 |

---

## 🌐 適用例と今後の展望

| 企業 | 製品・技術名 | 内容 |
|------|--------------|------|
| Intel | Foveros, Foveros Direct | ロジック同士の3D積層 |
| TSMC | SoIC | ダイ間のダイレクト接続 |
| Sony | Stacked CIS | イメージセンサの3D積層 |

---

## 📎 次節への接続

次節 [2.4：実例紹介](./f2_4_pkg_case_study.md) では、これらの2.5D/3D実装が実際にどう使われているか、主要企業の製品事例に焦点を当てて解説します。

---
