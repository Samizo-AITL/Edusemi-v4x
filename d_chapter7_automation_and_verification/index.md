---
layout: default
title: 応用編 第7章　自動化と実装検証技術　
---

---

# 🤖 応用編 第7章：自動化と実装検証技術  
**Applied Chapter 7: Automation and Implementation Verification**

---

## 📘 概要｜Overview

本章では、RTL設計から物理レイアウト検証までに対応した  
**設計品質の静的チェックおよび自動検証フローの体系化**を扱います。

From RTL to physical layout, this chapter focuses on  
**systematic quality verification and automation techniques** for hardware design.

`Lint`, `DRC`, `LVS`, `STA` といった各段階の検証手法に加えて、  
**OpenLaneやGitHub ActionsによるCI/CDフロー構築**も取り上げます。

In addition to `Lint`, `DRC`, `LVS`, and `STA`,  
you will learn how to build a **modern CI/CD design flow using OpenLane and GitHub Actions**.

---

## 📂 セクション構成｜Section Structure

| 📄 **ファイル名｜Filename** | 📚 **内容｜Description** |
|----------------------------|--------------------------|
| [`lint_and_static_check.md`](./lint_and_static_check.md) | Verilogの静的解析とLintチェックの基本<br>Static analysis and style checking for Verilog |
| [`drc_lvs_erc.md`](./drc_lvs_erc.md) | 物理設計におけるDRC / LVS / ERC検証<br>Physical verification techniques (DRC, LVS, ERC) |
| [`openlane_validation.md`](./openlane_validation.md) | OpenLaneによる物理レイアウトの自動検証<br>Automated physical verification using OpenLane |
| [`ci_cd_designflow.md`](./ci_cd_designflow.md) | GitHub Actionsを用いたCI/CDの構築<br>CI/CD design flow with GitHub Actions |

---

## 🎯 対象読者｜Target Audience

- RTL設計の品質検証を学びたい**初学者・学生**  
  *Beginners and students interested in RTL design quality*
- DRC/LVSなどの**物理検証に習熟したい設計者**  
  *Engineers seeking practical skills in physical verification*
- 教育目的でEDAフローを**体系的に運用したい講師・研究者**  
  *Educators and researchers aiming for structured EDA flows*

---

## ✅ 本章のねらい｜Objectives of This Chapter

- 設計初期から物理段階までの**検証手法とツール操作を体系的に理解**  
  *Understand verification techniques and tool usage from RTL to physical stages*
- Lint〜DRC/LVS〜CI/CDまでの**一貫した検証フローを自動化**  
  *Automate a unified verification flow*
- OpenLaneとGitHub Actionsを活用し、**教育・PoC向けの再現性ある開発環境を構築**  
  *Build reproducible design environments for education and PoC development*

---

## 🔗 関連章リンク｜Related Chapters

- [📘 基礎編 第5章：SoC設計フローとEDAツール｜SoC Design Flow and EDA Tools](../chapter5_soc_design_flow/)  
- [🧰 応用編 第6章：PDKとEDA環境｜PDK and EDA Environment](../d_chapter6_pdk_and_eda_environment/)

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **連絡先 / Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [X / Twitter](https://x.com/shin3t72)<br>💻 [Samizo-AITL Portal](https://samizo-aitl.github.io/) |
| **ライセンス / License** | **Hybrid License**<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top
**🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)**

