# ⚙️ 応用編 第7章：自動化と実装検証技術

---

## 📘 概要

本章では、SoC設計フローにおいて重要な**各種チェックの自動化技術**と、**実装検証の基本的考え方**を扱います。

現代の半導体設計では、設計ミスや仕様逸脱を早期に検出するために、形式的な静的検証やレイアウトルール違反の自動チェックが不可欠です。  
また、OpenLaneなどのオープンツールでもこうした検証手段が標準搭載されており、教育や研究にも応用が進んでいます。

---

## 📂 セクション構成

| ファイル名 | 内容 |
|------------|------|
| `lint_and_static_check.md` | 論理設計初期段階における `Lint`、形式検証、`CDC` などの静的チェック |
| `drc_lvs_erc.md` | 実装段階における `DRC`、`LVS`、`ERC` の基本原理と自動化フロー |
| `openlane_validation.md` | OpenLaneを用いた `物理設計検証` の実践例とログ解析手法 |
| `ci_cd_designflow.md` | `CI/CD` による設計フロー自動化と設計資産の継続的検証構築 |

---

## 🎯 対象読者

- 静的検証や自動チェックを導入したい初中級設計者
- OpenLANEなどOSSフローを活用した物理検証に興味のある教育関係者
- チェックフロー全体を体系的に理解したい学生・新人エンジニア

---

## 🔗 関連章

- [`第5章：SoC設計フロー`](../chapter5_soc_design_flow/README.md)：設計手順とEDA概要  
- [`第6章：テストとパッケージ`](../chapter6_test_and_package/README.md)：実装検証の出口である製品テストとの接続  
- [`d_chapter6_pdk_and_eda_environment`](../d_chapter6_pdk_and_eda_environment/README.md)：PDKとツールの接続性確認

---

© 2025 Shinichi Samizo / MIT License
