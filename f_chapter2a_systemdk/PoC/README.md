# 📦 SystemDK PoCマニュアル  
**Physical Constraint Co-Design with SystemDK for GAA / AMS / MRAM Integration**

---

## 📘 概要｜Overview

本マニュアルでは、System Design Kit（SystemDK）に基づく物理制約の統合設計と、  
**GAA（Gate-All-Around） / AMS（Analog-Mixed Signal） / MRAM（Magnetoresistive RAM）** を統合する  
チップレットPoC（概念実証）構成を体系的に解説します。

This manual presents a PoC-based design process integrating physical constraints  
using **SystemDK**, applied to chiplet-based architectures with **GAA**, **AMS**, and **MRAM** blocks.

---

## 📊 構造図｜Block Diagram

<div align="center">
  <img src="./images/Physical_Design_PoC_Manual_Flowchart.png" alt="Physical Design PoC Manual Diagram" width="80%">
</div>

---

## 📚 セクション構成｜Section Structure

| 節 | ファイル | 内容 |
|----|----------|------|
| 1 | [`poc_1_motivation.md`](./poc_1_motivation.md) | なぜSystemDKによるPoCが必要か？設計動機と狙い |
| 2 | [`poc_2_systemdk_platform.md`](./poc_2_systemdk_platform.md) | SystemDKによる制約管理プラットフォーム概要 |
| 3 | [`poc_3_block_spec.md`](./poc_3_block_spec.md) | GAA / AMS / MRAMブロックの仕様とノード構成 |
| 4 | [`poc_4_constraint_profiles.md`](./poc_4_constraint_profiles.md) | SI/PI・熱・応力・EMI/EMCの設計要件まとめ |
| 5 | [`poc_5_integration.md`](./poc_5_integration.md) | チップレット統合における物理整合と配置評価 |
| 6 | [`poc_6_fem_analysis.md`](./poc_6_fem_analysis.md) | FEM・熱・電磁界・応力解析シナリオ例 |
| 7 | [`poc_7_summary.md`](./poc_7_summary.md) | 学習ポイントとPoC結果のまとめ |

---

## 🧩 位置づけ｜Relation to Edusemi

このPoCマニュアルは、**Edusemi-v4x 特別編 第2a章 SystemDK教材** の一部として位置づけられています：

- [f2a_8_chiplet_example_gaa_ams_mram.md](../f2a_8_chiplet_example_gaa_ams_mram.md)：設計事例の解説本体  
- 本ディレクトリ（PoC/）は、**構造設計と演習支援の詳細教材**を担当

---

## 🎯 教育的意義｜Educational Value

- **SystemDKを用いたPoC設計の具体的手順**を再現
- **物理制約（SI/PI, 熱, 応力, EMI/EMC）の相互連成を実感的に理解**
- **異種ノード統合の現実的制約と設計トレードオフ**を学ぶ
- 将来的な**Chiplet設計支援AIとの連携**も見据えた教材基盤

---

## 👤 著者・ライセンス｜Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| 著者 / Author | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |
| Email | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| ライセンス / License | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

## 🔙 戻る｜Back

[SystemDK教材トップに戻る](../README.md)
