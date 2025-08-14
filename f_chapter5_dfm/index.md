---
layout: default
title: 特別編 第5章　PDKとレイアウト検証による物理整合とDFM設計指針 
---

---

# 🧬 特別編 第5章：PDKとレイアウト検証による物理整合とDFM設計指針

## 📘 概要

本章では、Sky130 PDKベースのチップ物理設計において、  
**DRC / LVS / ERC / Antenna check / Fill / Tapeout** など、  
GDS生成後に必要となる検証とDFM設計手法を体系的に学びます。

---

## 📖 各節へのリンク

- [5.1 PDK構造の理解とSky130レイヤー体系](docs/5_1_pdk_layer.md)
- [5.2 MagicによるGDS階層と層構成の可視化](docs/5_2_magic_gds.md)
- [5.3 DRCルールとその根拠（例：metal spacing）](docs/5_3_drc_check.md)
- [5.4 LVSの仕組みと等価性判定の論理](docs/5_4_lvs_check.md)
- [5.5 DFM設計：量産対応のためのレイアウト指針](docs/5_5_dfm_guideline.md)
- [5.6 チップ完成に向けた最終検証ステップ](docs/5_6_final_check.md)

---

## 🛠️ 使用ツールと環境

- Sky130A PDK（Open_PDK準拠）
- Magic / KLayout（レイアウト可視化・抽出）
- Netgen（LVS）
- OpenLane（DRC / Antenna Check / Fill など）

---

## 📦 本章の教材構成

```
f_chapter5_dfm/
├── README.md
├── index.md
├── _sidebar.md
├── toc_f_chapter5_dfm.md
├── docs/
└── layout/（GDSやLVS用データ例など）※任意
```

---

## 🔗 関連章リンク

- [特別編 第4章：OpenLaneによるRTL-to-GDSII実装](../f_chapter4_openlane/README.md)
- [実践編：Python自動化とGDS評価（予定）](../p_chapter6_practice/README.md)

