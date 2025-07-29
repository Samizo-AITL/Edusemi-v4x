# 🧬 特別編 第5章：PDKとレイアウト検証による物理整合とDFM設計指針

本章では、Sky130 PDKを用いたレイアウト検証と、  
GDSレベルでの物理整合・製造配慮（DFM）に関する設計指針を学びます。

---

## 🎯 本章の目的

- PDKの構造とレイヤー体系を理解する
- MagicやKLayoutを用いたGDSの可視化と階層構造解析
- DRC / LVS / ERC などレイアウト検証技術の基礎と運用
- DFM（Design for Manufacturability）の視点で設計指針を習得

---

## 📖 節構成

| 節番号 | タイトル | 概要 |
|--------|----------|------|
| 5.1 | PDK構造の理解とSky130レイヤー体系 | PDKのレイヤー命名・マスク対応関係を解説 |
| 5.2 | MagicによるGDS階層と層構成の可視化 | セル構造やmetal構成を視覚的に確認 |
| 5.3 | DRCルールとその根拠（例：metal spacing） | MagicによるDRCチェックとルール背景の学習 |
| 5.4 | LVSの仕組みと等価性判定の論理 | Netlist⇔GDSの比較と仕組み |
| 5.5 | DFM設計：量産対応のためのレイアウト指針 | 寄生・ストレス・バウンダリ設計など |
| 5.6 | チップ完成に向けた最終検証ステップ | Tapeout準備、ERC、プロービング対応 |

---

## 🛠️ 使用ツール

- Sky130A PDK
- Magic（PDK付属）
- KLayout（GDS可視化）
- Netgen（LVS用）

---

## 🔗 関連教材

- [特別編 第4章：OpenLane配置配線とGDS生成](../f_chapter4_openlane/README.md)
- [実践編：Sky130自動化・DFM評価（予定）](../p_chapter6_practice/README.md)

---

## ✅ 備考

- 本章はSky130ベースのPDK構造・レイアウト検証知識を中心に構成しています
- 論理設計から物理整合へ、さらに量産・製造段階へつながる教育章です

---

### 👤 著者・ライセンス｜Author & License

| 項目｜Item | 内容｜Details |
|------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)

---
