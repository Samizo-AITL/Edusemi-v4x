# 🎓 f2a_7_systemdk_poc.md  
**SystemDKベースの統合PoC演習課題**  
**SystemDK-Based PoC Exercise**

---

## 📘 目的｜Objective

本演習では、SystemDKの設計思想に基づき、**物理制約（SI/PI、熱、応力、EMI/EMC）を統合的に考慮**した  
**チップレット統合設計のPoC（Proof of Concept）**を構築・評価することを目的とします。  

> This exercise aims to build and evaluate a chiplet-based system using SystemDK principles, focusing on cross-layer physical constraints such as SI/PI, thermal, mechanical stress, and EMI/EMC.

---

## 🧩 課題テーマ｜Exercise Theme

> **「2.5Dパッケージによるマルチチップ統合設計を行い、制約の相互依存性に基づく改善提案を提示せよ」**  
> **“Design a multi-chip 2.5D system and propose constraint-aware design improvements.”**

---

### ✅ 条件例｜Design Requirements

- SoCチップ（FPGAまたはCaravel MPW相当）と、**汎用MRAM / AMSチップレット**を混載
- **インタポーザ配線、電源構成、冷却設計、材料構成**などを自ら設計・評価
- 下記物理制約ごとに**設計根拠・解析手法・制約マップ**を示す：

| 項目 | 目標 |
|------|------|
| **SI/PI** | IR Drop評価、PDNインピーダンス整合、デカップリング配置 |
| **熱設計** | 熱源モデル構築、放熱経路設計、材料選定 |
| **応力** | バンプ応力、層間応力、ダイ割れ・界面剥離の防止 |
| **EMI/EMC** | 帯域内ノイズ、クロストーク、GND構造によるシールド設計 |

---

## 🧰 ツール・構成例｜Suggested Tools & Setup

| カテゴリ | 推奨ツール例（教育用） |
|----------|----------------------|
| 回路・IF記述 | SystemVerilog, Verilog-A, IBIS |
| 配置・視覚化 | CSV配置 → SVG描画 or KiCAD簡易配置 |
| SI/PI | PowerDC, Ansys SIwave, LTspice |
| 熱解析 | COMSOL, Icepak, Python可視化（簡易） |
| 応力解析 | SolidWorks Simulation, COMSOL |
| EMI評価 | HFSS, openEMS（EMCモード簡易化） |

> 教材展開では、**構造・熱・電源・電磁の因果関係を理解するための直感的な可視化と概算**を重視します。

---

## 📝 レポート構成例｜Suggested Report Structure

1. **設計概要と構成方針**（チップ構成、PKGモデル、インタフェース構成）
2. **各制約項目のモデリングと評価結果**
3. **制約間のトレードオフとその妥協判断**
4. **制約ベースでの改善設計案の提案**
5. **SystemDK構成に向けた設計判断の統合マップ**

---

## 🧪 発展：PoCDK構成への接続｜Towards PoCDK Architecture

> 本演習の成果は、SystemDK実装のための **PoCDK（PoC Design Kit）** への橋渡しを意図しています。

### 🔁 PoCDKで実施される内容：

- **混載チップ構成をFPGA上で実検証**
- **FEM解析（熱・応力・電源・EMI）により、以下DesignKitに情報展開：**

| Kit名 | 反映される構造情報 |
|-------|------------------|
| **BRDK** | 熱流路、電源プレーン、実装制約 |
| **IPDK** | MRAM/AMS I/F, EMI耐性, ピン構成 |
| **PKGDK** | バンプ配置、熱ストレス制御、インタポーザ設計 |
| **SystemDK** | 上記すべてを統合した制約・設計マップとフィードバック構造 |

---

## 🔗 関連リンク｜Related Links

- [SystemDK README](./README.md)
- [f2a_2_sipi.md](./f2a_2_sipi.md)
- [f2a_3_thermal.md](./f2a_3_thermal.md)
- [f2a_4_mechanical.md](./f2a_4_mechanical.md)
- [f2a_5_emi_emc.md](./f2a_5_emi_emc.md)
- [PoC/README.md](./PoC/README.md)

---

## 🧭 今後の展開｜Future Extensions

- PoCDKに基づく **SystemDK制約テンプレートの形式知化**
- Sky130 / Caravelと連動したRTL設計・GDS生成への拡張
- 教材展開において**物理解析 → 制約マップ → 再設計**の3層演習モデルとして応用

---

## 👨‍🏫 教育的注記｜Educational Note

本PoC演習は、EDAツールに依存せずとも「**設計判断に必要な物理現象とその連成関係を直感的に把握**」することを目的としています。  
SystemDKは単なる設計支援ツールではなく、**“制約を設計の言語とするための知識構造”**であることを体験的に学ぶ構成です。
