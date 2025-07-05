# 🤖 応用編 第7章：自動化と実装検証技術

---

## 📘 概要

本章では、RTLからレイアウト検証までを対象とした自動チェック技術について解説します。  
`Lint`、`DRC`、`LVS`、`STA`といった設計検証の自動化に加えて、OpenLaneやGitHub Actionsを活用した  
CI/CDによる継続的検証ループの構築までを対象としています。

---

## 📂 セクション構成

| ファイル名 | 内容 |
|------------|------|
| [`lint_and_static_check.md`](./lint_and_static_check.md) | Verilogの静的解析とLintチェックの基本 |
| [`drc_lvs_erc.md`](./drc_lvs_erc.md) | DRC / LVS / ERC の検証フローとツール操作 |
| [`openlane_validation.md`](./openlane_validation.md) | OpenLaneによる配置配線後の自動検証とログ解析 |
| [`ci_cd_designflow.md`](./ci_cd_designflow.md) | CI/CDでの設計検証自動化とGitHub Actionsの活用 |

---

© 2025 Shinichi Samizo / MIT License
