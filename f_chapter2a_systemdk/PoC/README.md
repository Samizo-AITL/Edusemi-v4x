# 📦 SystemDK PoCマニュアル  
**SystemDK-Based PoC Manual for Physical Constraint Integration**

---

## 📘 概要｜Overview

本マニュアルでは、System Design Kit（SystemDK）に基づく物理制約の統合設計と、  
**GAA（Gate-All-Around） / AMS（Analog-Mixed Signal） / MRAM（Magnetoresistive RAM）** を統合する  
チップレットPoC（概念実証）構成を体系的に解説します。

This manual systematically introduces a PoC structure based on the **System Design Kit (SystemDK)**  
for physical constraint integration and chiplet-based heterogeneous design  
with **GAA**, **AMS**, and **MRAM** functional blocks.

---

## 📊 構造図｜Block Diagram

<div align="center">
  <img src="./images/Physical_Design_PoC_Manual_Flowchart.png" alt="Physical Design PoC Manual Diagram" width="60%">
</div>

---

## 📚 セクション構成｜Section Structure

| 節 | ファイル名 / File | 内容 / Description |
|----|-------------------|---------------------|
| 1 | [`poc_1_motivation.md`](./poc_1_motivation.md) | なぜSystemDKによるPoCが必要か？設計動機と狙い<br>Why a PoC using SystemDK is needed: motivations & goals |
| 2 | [`poc_2_systemdk_platform.md`](./poc_2_systemdk_platform.md) | SystemDKのプラットフォーム概要と評価支援<br>SystemDK overview as a constraint-aware platform |
| 3 | [`poc_3_block_spec.md`](./poc_3_block_spec.md) | GAA / AMS / MRAMブロックの仕様と構成定義<br>Node and block specifications for GAA, AMS, MRAM |
| 4 | [`poc_4_constraint_profiles.md`](./poc_4_constraint_profiles.md) | SI/PI・熱・応力・EMI/EMCの設計要件<br>Constraint profiles for SI/PI, thermal, stress, EMI/EMC |
| 5 | [`poc_5_integration.md`](./poc_5_integration.md) | Chiplet統合における制約整合とレイアウト設計<br>Physical alignment and layout in chiplet integration |
| 6 | [`poc_6_fem_analysis.md`](./poc_6_fem_analysis.md) | FEM・熱・電磁界・応力解析の事例<br>Examples of FEM, thermal, EM, and mechanical analysis |
| 7 | [`poc_7_summary.md`](./poc_7_summary.md) | 本PoCのまとめと教育的意義の整理<br>Summary and educational reflections on the PoC |

---

### 🔁 PoCDKによる実評価と制約抽出｜PoCDK Evaluation Flow

PoC設計の最終フェーズでは、**実際のPoC評価ボードを用いた混載構成の動作検証**と、  
**FEM解析による多物理場制約の抽出**を行います。

> In the final stage of the PoC, real board-level testing is combined with FEM-based analysis  
> to extract cross-domain physical constraints for SystemDK refinement.

#### ✅ 実施内容（What to Perform）

| 項目 | 内容（日本語） | 内容（英語） |
|------|----------------|----------------|
| FPGAでの動作検証 | MRAM / AMS / SoCモジュールを評価ボード上に混載し、通信/制御を実機検証 | Mixed integration on a PoC board with FPGA control, verifying actual interaction |
| FEM解析 | 熱・応力・EMI・IR dropの解析を行い、各構造の弱点を抽出 | Conduct FEM analysis for thermal, mechanical, EMI, IR-drop to identify constraints |
| 制約のDesignKit化 | 解析結果をBRDK/IPDK/PKGDKへ展開し、SystemDKに再統合 | Feed constraint results into respective kits and unify via SystemDK |

#### 📦 PoCDKからのDesignKit派生

| DesignKit | 抽出される主な情報（例） |
|-----------|--------------------------|
| **BRDK** | 熱分布マップ、電源経路IR Drop、実装材料による熱応答 |
| **IPDK** | MRAM/AMSインタフェースのピン応力・EMI干渉範囲 |
| **PKGDK** | 接続層間の応力、インタポーザ温度差、電源層カップリング |
| **SystemDK** | 全構成の制約マップ、設計再利用性、トレードオフ履歴管理 |

---

## 🧩 位置づけ｜Relation to Edusemi

このPoCマニュアルは、**Edusemi-v4x 特別編 第2a章 SystemDK教材** の一部として設計されています。

This PoC manual is part of the **SystemDK module (Special Chapter 2a)** within **Edusemi-v4x**,  
providing a deeper implementation and hands-on practice based on the conceptual contents of:

- [`f2a_8_chiplet_example_gaa_ams_mram.md`](../f2a_8_chiplet_example_gaa_ams_mram.md)

---

## 🎯 教育的意義｜Educational Value

- SystemDKを活用したPoC設計の**具体的ステップと構造理解**
- **物理制約（SI/PI, 熱, 応力, EMI/EMC）**の統合設計の実践的理解
- **異種ノード統合**における設計トレードオフと現実性の認識
- 将来的な**AI連携・自動化設計**の土台となる教材構成

- Understand **step-by-step design** using SystemDK for PoC  
- Experience **multi-constraint integration** (SI/PI, thermal, stress, EMI/EMC)  
- Learn the **trade-offs of heterogeneous integration**  
- Build foundation for future **AI-assisted or automated design flows**

---

## 👤 著者・ライセンス｜Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| 著者 / Author | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |
| Email | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| ライセンス / License | MIT License（再配布・改変自由）<br>MIT License (Free to reuse/modify/redistribute) |

---

## 🔙 戻る｜Back

[← SystemDK教材トップへ戻る｜Back to SystemDK Top](../README.md)
