# 🧱 応用編 第4章：レイアウト設計と最適化

---

## 📘 概要

ICレイアウト設計では、回路の性能や信頼性を確保するために、**物理配置・配線・空間構造**を最適化する必要があります。  
本章では、以下の要素を中心に、**実装制約と設計上の工夫**を学びます。

- 配線遅延・IRドロップ・カップリングノイズといった**物理劣化要因**
- CMP（化学機械研磨）やDPT（Double Patterning）に対応する**配置パターン**
- 電源・GND・クロックツリーの**レイアウト戦略**
- 寄生素子（寄生トランジスタ・ダイオード）や**ラッチアップ対策**

---

## 📂 セクション構成

| ファイル名 | 内容概要 |
|------------|-----------|
| [`layout_principles.md`](layout_principles.md) | レイアウトの基本：幅、間隔、層構成、電源配線など |
| [`cmp_dummy_pattern.md`](cmp_dummy_pattern.md) | CMP対応ダミーパターン：均一化と露光制御の工夫 |
| [`ir_drop_and_em.md`](ir_drop_and_em.md) | IRドロップ・エレクトロマイグレーション対策 |
| [`latchup_prevention.md`](latchup_prevention.md) | ガードリング・寄生トランジスタ抑制とラッチアップ対策 |
| [`layout_case_study.md`](layout_case_study.md) | 実際のレイアウト構造（実装例・DRCルール適用）の紹介 |

---

## 🎯 対象読者

- 回路設計から物理実装まで視野を広げたい若手技術者
- PDKルールや実装制約に触れたい学生
- レイアウト最適化と品質保証の関係に関心のある方

---

## 🔧 本章のキーワード

`DRC` `LVS` `CMP Dummy` `Latch-up` `IR Drop` `Metal Fill` `Guard Ring` `Well Tap` `Double Patterning` `Spacing Rule` `Density Check`

---

## 🔗 関連章との接続

- [基礎編　第5章 SoC設計フローとEDAツール](../chapter5_soc_design_flow/)
- [基礎編　第3章 プロセス技術と微細化の制約](../chapter3_process_evolution/)
- [応用編　第6章 PDKとEDA環境](../d_chapter6_pdk_and_eda_environment/)

---

© 2025 Shinichi Samizo / MIT License
