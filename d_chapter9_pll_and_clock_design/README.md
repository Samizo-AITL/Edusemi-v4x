# ⏱️ 応用編 第9章：PLLとクロック設計

---

## 📘 概要

PLL（Phase-Locked Loop）は、外部クロックを基準として内部クロックを生成・制御する回路であり、SoC・ASIC設計において必須のタイミング要素です。

本章では、PLLの基本構造・動作原理から、クロックツリー設計、ジッタ・スキュー、クロックゲーティングといった**クロック設計全般の要点**を解説します。

---

## 🧩 セクション構成

| ファイル名 | 内容 |
|------------|------|
| [`pll_basics.md`](pll_basics.md) | PLLの構成要素（PFD, VCO, Divider）と動作原理 |
| [`clock_tree_design.md`](clock_tree_design.md) | クロックツリー設計、CTS（Clock Tree Synthesis）の基礎 |
| [`jitter_and_skew.md`](jitter_and_skew.md) | ジッタ・スキューの定義と対策技術 |
| [`clock_gating_techniques.md`](clock_gating_techniques.md) | クロックゲーティングによる消費電力削減手法 |
| [`real_chip_examples.md`](real_chip_examples.md) | 実際のSoC・ASICにおけるPLL/クロック設計事例 |

---

## 🎯 到達目標

- PLLの構成と動作原理を理解する
- クロックツリーとその設計制約を把握する
- ジッタ・スキューの発生要因と対策を説明できる
- クロックゲーティングによる低消費電力化の基本を理解する

---

## 📚 関連章リンク

- [第5章 SoC設計フロー](../chapter5_soc_design_flow/README.md)  
  ↳ タイミングクロージャ・CTS設計との接続
- [第7章 デザインレビューと開発組織連携](../chapter7_design_review_and_org/README.md)  
  ↳ PLL仕様や時系列設計の設計レビュー項目として重要

---

## 🔭 応用発展

- マルチPLLアーキテクチャとクロックドメイン分離
- スプレッドスペクトラムPLL（EMI低減）
- PLLレイアウト上のノイズ・干渉対策（Guard Ring, Substrate Isolation）

---

© 2025 Shinichi Samizo / MIT License
