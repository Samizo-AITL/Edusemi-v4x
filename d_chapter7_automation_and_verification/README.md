# 🤖 応用編 第7章：自動化と実装検証技術

---

## 📘 概要

本章では、RTL設計から物理レイアウト検証までに対応した**自動チェック技術の体系**を解説します。  
`Lint`、`DRC`、`LVS`、`STA`などの静的検証に加えて、**OpenLaneやGitHub Actionsを活用したCI/CD構築**まで踏み込み、  
現代的なEDA設計と教育的フローの両立を目指します。

**設計品質の自動検証と、繰り返し可能なフローの構築手法を習得することが本章の目的です。**

---

## 📂 セクション構成

| ファイル名 | 内容 |
|------------|------|
| [`lint_and_static_check.md`](./lint_and_static_check.md) | Verilogの静的解析とLintチェックの基本（構文・記述スタイル） |
| [`drc_lvs_erc.md`](./drc_lvs_erc.md) | DRC / LVS / ERC の検証フローとツール操作（物理検証の三本柱） |
| [`openlane_validation.md`](./openlane_validation.md) | OpenLaneによる配置配線後の自動検証とログ解析（フローへの統合） |
| [`ci_cd_designflow.md`](./ci_cd_designflow.md) | CI/CDでの設計検証自動化とGitHub Actionsの活用（継続的設計検証） |

---

## 🎯 対象読者

- RTL設計の品質検証を学びたい初学者・学生
- DRC/LVSなどの物理検証に実務的理解を深めたい設計者
- 教育用EDAフロー（OpenLaneなど）を体系的に運用したい講師・研究者

---

## ✅ 本章のねらい

- 設計初期から物理段階までの**検証手法とツール操作を体系的に理解**
- Lint〜DRC/LVS〜CI/CDまでの**一貫した検証フローを自動化**
- OpenLaneとGitHub Actionsを活用し、**教育・PoC向けの再現性ある開発環境を構築**

---

## 🔗 関連章リンク

- [基礎編 第5章 SoC設計フローとEDAツール](../chapter5_soc_design_flow/)  
- [応用編 第6章 PDKとEDA環境](../d_chapter6_pdk_and_eda_environment/)

---

© 2025 Shinichi Samizo / MIT License


---

🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---

