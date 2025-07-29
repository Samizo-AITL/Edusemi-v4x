# 🛠️ 応用編 第6章：PDKとEDA環境  
# 🛠️ Applied Chapter 6: PDK and EDA Environment

---

## 📘 概要｜Overview

**PDK（Process Design Kit）** は、特定の半導体プロセスに最適化された**設計ルール・SPICEモデル・レイアウト情報・EDA統合ファイルの集合体**です。  
本章では、PDKの構成要素、EDAツールとの関係、設計ルールチェックのフロー、プロセス互換性など、**実務に直結する設計基盤構築の視点**を整理します。

The **Process Design Kit (PDK)** is a collection of files optimized for a specific semiconductor process, including **design rules, SPICE models, layout data, and EDA tool integration files**.  
This chapter organizes practical design foundation knowledge, such as the internal structure of PDKs, their relationship with EDA tools, rule check flows, and process portability.

---

## 📂 セクション構成｜Section Structure

| 📄 **ファイル名｜Filename** | 📚 **内容｜Description** |
|----------------------------|--------------------------|
| [`pdk_structure.md`](./pdk_structure.md) | PDKの内部構成（デザインルール、モデル、シンボル等）<br>PDK internals: design rules, models, symbols |
| [`eda_toolchain.md`](./eda_toolchain.md) | 商用・オープンソースEDAツールとPDKの連携構成<br>EDA-PDK integration using commercial & open-source tools |
| [`rule_check_flow.md`](./rule_check_flow.md) | DRC、LVS、ERCなどの設計ルールチェックと検証フロー<br>Design rule and verification flows: DRC, LVS, ERC |
| [`pdk_compatibility.md`](./pdk_compatibility.md) | プロセス互換性、ノード間の移行、教育適用視点<br>Process portability, node migration, educational adaptation |

---

## 🎯 対象読者｜Target Audience

- **PDK選定やEDA環境構築に関心のある設計者**  
  *Engineers interested in PDK selection and EDA integration*
- **Sky130やOpenLaneなど、教育用PDKに取り組む学習者**  
  *Learners exploring open-source PDKs like Sky130 with OpenLane*
- **商用PDKの制約や設計ルールを理解したい実務者**  
  *Professionals analyzing constraints and rule sets in commercial PDKs*

---

## 🔗 関連章｜Related Chapters

| 🧩 **章｜Chapter** | 📘 **内容｜Details** |
|------------------|------------------------|
| [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/) | PDKが提供するMOS物性とSPICEパラメータの理解<br>Device physics and SPICE parameters within PDKs |
| [`chapter5_soc_design_flow/`](../chapter5_soc_design_flow/) | EDAツールとPDKを用いたSoC設計フロー<br>SoC design flows integrating PDKs and EDA tools |

---

## 👤 著者・ライセンス｜Author & License

| 🏷️ **項目｜Item** | 📝 **内容｜Details** |
|------------------|----------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>*Redistribution and modification allowed* |

---

#### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)
