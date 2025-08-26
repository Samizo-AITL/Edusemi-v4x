---
layout: default
title: 応用編 第6章　PDKとEDA環境
---

---

# 🛠️ 応用編 第6章：PDKとEDA環境 
**Applied Chapter 6: PDK and EDA Environment**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) |

---

## 📘 概要｜Overview

**PDK（Process Design Kit）** は、特定の半導体プロセスに最適化された **設計ルール・SPICEモデル・レイアウト情報・EDA統合ファイルの集合体** です。  
本章では、PDKの構成要素、EDAツールとの関係、設計ルールチェックのフロー、プロセス互換性、**BSIMモデルとの関係**など、**実務に直結する設計基盤構築の視点**を整理します。

The **Process Design Kit (PDK)** is a collection of files optimized for a specific semiconductor process, including **design rules, SPICE models, layout data, and EDA tool integration files**.  
This chapter organizes practical knowledge of design foundations, including the internal structure of PDKs, their relationship with EDA tools, rule check flows, **and BSIM modeling standards**.

---

## 📂 セクション構成｜Section Structure

| 📄 **ファイル名｜Filename** | 📚 **内容｜Description** |
|----------------------------|--------------------------|
| [`pdk_structure.md`](./pdk_structure.md) | PDKの内部構成（デザインルール、モデル、シンボル等）<br>PDK internals: design rules, models, symbols |
| [`eda_toolchain.md`](./eda_toolchain.md) | 商用・オープンソースEDAツールとPDKの連携構成<br>EDA-PDK integration using commercial & open-source tools |
| [`rule_check_flow.md`](./rule_check_flow.md) | DRC、LVS、ERCなどの設計ルールチェックと検証フロー<br>Design rule and verification flows: DRC, LVS, ERC |
| [`pdk_compatibility.md`](./pdk_compatibility.md) | プロセス互換性、ノード間の移行、教育適用視点<br>Process portability, node migration, educational adaptation |
| [`bsim_models.md`](./bsim_models.md) | BSIM4 / BSIM-CMG モデルとPDKとの関係<br>BSIM4 / BSIM-CMG and their role in PDKs |

---

## 🧮 BSIMモデルとPDKの関係  
### BSIM Models and PDKs

PDKは、各ノードの **MOSデバイス物性を忠実に反映したSPICEモデル** を含みます。その中心となるのが **BSIM（Berkeley Short-channel IGFET Model）** 系列であり、プロセスノードによって以下のようなモデルが用いられます：

| モデル名｜Model | 対応ノード例｜Applicable Nodes | 構造｜Structure | コメント｜Notes |
|-------------|--------------------------|------------------|--------------------------|
| BSIM3       | ～0.25μm                 | Bulk MOSFET      | 教育用にも適し、Sky130等に採用されることもある |
| BSIM4       | ～65nm〜28nm             | Bulk MOSFET      | SCE対応。FinFET前の主流 |
| BSIM-CMG    | 22nm〜3nm FinFET/GAA     | FinFET, GAA      | 多ゲート対応（Level 54）、業界標準 |
| BSIM6       | 研究段階（CFET等）       | GAA, CFET        | BSIM-CMGを発展させた次世代構造対応モデル |

**BSIMモデルはPDKに含まれる `.model` 定義群や `.lib` ファイルに格納され、回路設計者がSPICEやSpectreなどで回路シミュレーションを行う際に不可欠な要素**となります。

---

## 🎯 対象読者｜Target Audience

- **PDK選定やEDA環境構築に関心のある設計者**  
  *Engineers interested in PDK selection and EDA integration*
- **Sky130やOpenLaneなど、教育用PDKに取り組む学習者**  
  *Learners exploring open-source PDKs like Sky130 with OpenLane*
- **商用PDKの制約や設計ルールを理解したい実務者**  
  *Professionals analyzing constraints and rule sets in commercial PDKs*
- **BSIMモデルを理解し、物理設計に反映したい学生・研究者**  
  *Students and researchers exploring BSIM models for accurate physical simulation*

---

## 🔗 関連章｜Related Chapters

| 🧩 **章｜Chapter** | 📘 **内容｜Details** |
|------------------|------------------------|
| [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/) | PDKが提供するMOS物性とSPICEパラメータの理解<br>Device physics and SPICE parameters within PDKs |
| [`chapter5_soc_design_flow/`](../chapter5_soc_design_flow/) | EDAツールとPDKを用いたSoC設計フロー<br>SoC design flows integrating PDKs and EDA tools |
| [`appendixf1_05_node_params.md`](../f_chapter1_finfet_gaa/appendixf1_05_node_params.md) | FinFET/GAAのBSIM-CMG対応パラメータリスト<br>Node-specific parameters aligned with BSIM-CMG |

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

