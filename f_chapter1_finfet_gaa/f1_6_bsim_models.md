---
layout: default
title: 1.6　BSIM4 → BSIM-CMG → CFET版構想
---

---

# ⚙️ 1.6　BSIM4 → BSIM-CMG → CFET版構想  
**1.6　From BSIM4 to BSIM-CMG, and Toward a CFET Compact Model**

---

## 🔰 概要 / *Overview*
本節では、プレーナMOS世代から FinFET / GAA 世代、そして CFET 時代に向けて進化してきた  
**コンパクトモデル（Compact Model）** の流れを解説します。  
設計・EDA・教育を結ぶ **「標準モデル」** の役割を整理し、将来的な **CFET版の必要性** を展望します。  

*In this section, we explain the evolution of **compact models** from the planar MOS era (BSIM4)  
to the FinFET/GAA era (BSIM-CMG), and explore the prospects for a future **CFET-oriented model**.*

---

## 🧱 1.6.1　BSIM4 ― プレーナMOS世代 / *BSIM4 – Planar MOS Era*
- **適用範囲 / *Coverage***：90nm〜32nm プレーナMOSFET  
- **特徴 / *Features***  
  - 短チャネル効果、移動度劣化、DIBL を高精度に記述  
  - BSIM3 を改良し、寄生抵抗・容量を詳細にモデル化  
- **限界 / *Limitations***  
  - 3D構造（FinFET, GAA）には非対応  
  - **$W$・$L$ ベースの寸法定義**がフィンやナノシート構造に適用できない  

---

## 🌀 1.6.2　BSIM-CMG ― FinFET/GAA世代 / *BSIM-CMG – FinFET & GAA Era*
- **開発 / *Developer***：UC Berkeley Compact Model Group (CMG)  
- **標準化 / *Standardization***：Si2/CSTF により国際標準モデル化  
- **特徴 / *Features***  
  - **多ゲート構造を統一的に扱える**（FinFET・GAA・ナノワイヤ）  
  - フィン高さ $H_{fin}$、幅 $W_{fin}$、シート数 $N_{sheet}$ を明示的にパラメータ化  
  - 量子化効果・サブバンド効果・温度依存性を組込み  
- **意義 / *Significance***  
  - FinFET と GAA を **同じフレームワークで比較可能**  
  - 現在の先端 EDA / 回路設計における **必須標準モデル**  

---

## 🧬 1.6.3　CFET ― 新モデルの必要性 / *CFET – The Need for a New Model*
- **背景 / *Background***  
  - nMOS と pMOS を **垂直積層**する CFET には、従来の BSIM-CMG では不十分  
- **課題 / *Challenges***  
  - 上下段FET間の **熱結合 / *thermal coupling***  
  - **ゲート間寄生容量 / *gate-to-gate parasitics*** によるクロストーク  
  - **ドレイン遅延・リーク結合 / *drain delay & leakage coupling***  
- **必要な拡張要素 / *Required Extensions***  
  - `thermal_resistance_stack`（熱結合パラメータ）  
  - `coupling_cap_np`（n/p間寄生容量）  
  - `delay_propagation`（信号結合遅延）  

---

## 🌍 1.6.4　標準化への展望 / *Outlook for Standardization*
- **現状 / *Current status***：CFET専用の国際標準モデルは存在しない  
- **研究レベル / *At research level***：Verilog-A による拡張モデルや二段合成が試作段階  
- **将来 / *Future***：  
  - 「**BSIM-CFET**」として標準化される可能性  
  - Si2/CSTF Compact Model Council での検討が期待される  
- **教育的価値 / *Educational value***：  
  - 「**新デバイスの普及には標準モデルが不可欠**」であることを理解できる  
  - MOS進化の歴史と並行して **モデル進化の系譜** を学習可能  

---

## 📘 学習まとめ / *Summary*
- **BSIM4**：プレーナMOS用（90nm〜32nm世代）  
  *For planar MOSFETs (90nm–32nm era)*  
- **BSIM-CMG**：FinFET/GAA 統一モデル（22nm〜2nm世代）  
  *Unified model for FinFET & GAA (22nm–2nm era)*  
- **CFET版構想**：ポスト2nm世代に必須、熱・遅延・結合を組み込む次世代標準  
  *Next-generation standard required for the post-2nm CFET era, incorporating thermal, delay, and coupling effects*  

---

## 🔙 関連リンク / *Related Links*
- [📘 1.5 CFET構造 / *CFET Structure*](f1_5_cfet.md)  
- [📘 Appendix F1_07（予定）：CFETモデル実習 / *Planned: CFET Modeling Practice*](appendixf1_07_cfet_modeling.md)  
