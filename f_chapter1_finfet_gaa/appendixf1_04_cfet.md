---
layout: default
title: Appendix F1-04 CFETの構造進化と技術的課題 
---

---

# Appendix F1-04: CFETの構造進化と技術的課題  
**Appendix F1-04: Structure Evolution and Technical Challenges of CFET**

---

## 📘 概要｜Overview

**CFET（Complementary FET）は、nFETとpFETを垂直方向に積層したポストGAAの有力候補構造であり、面積縮小・設計対称性・配線自由度の向上が期待されています。**  
この補足資料では、**構造進化の流れ、FinFET・GAAとの比較、製造・設計上の主な課題**を整理し、将来的な設計適用に向けた技術基盤を解説します。

**CFET (Complementary FET)** represents a potential post-GAA transistor structure in which nFET and pFET are stacked vertically.  
This appendix reviews **the structural evolution of CFET, comparison with FinFET and GAA, major process/design challenges**, and future considerations for practical deployment.

---

## 🔁 構造進化｜Structural Evolution Path

Planar MOS → FinFET → GAA (Nanosheet) → CFET (Stacked n/p)

- **FinFET**：ゲート包囲面増加（Fin構造）
- **GAA**：ゲート全面包囲（ナノシート）
- **CFET**：n/pを別層に積層（n-over-p or p-over-n）

> CFET is not just an extension of GAA but a radical shift in vertical device integration.

---

## 📊 技術比較｜Comparison Table

| 項目｜Feature | FinFET | GAA | CFET |
|----------------|--------|-----|------|
| ゲート制御性 | △ | ◎ | ◎ |
| 配線密度 | ○ | ○ | ◎ |
| マッチング性 | △ | ○ | ◎（n/p同セル中心配置） |
| 製造難易度 | ○ | △ | ×（積層プロセス） |
| 熱影響管理 | ○ | △ | ×（熱干渉あり） |
| EDA対応 | ○ | ○ | △（抽象モデル未整備） |

---

## 🏭 主な製造技術課題｜Key Process Challenges

- **ドーピング分離技術（Doping Isolation）**
  - 選択エピタキシャル成長とパターン制御が鍵
- **熱処理のバジェット制御（Thermal Budget Balancing）**
  - 上層工程が下層デバイスに影響
- **構造整合と平坦化（Planarity and Stacking Alignment）**
  - 高アスペクト比・ナノレベルのレジスト整合が必要
- **BEOLとの接続最適化**
  - TSVやMOL（Middle of Line）を含む3D配線適用が前提

---

## 🧩 設計技術の観点｜Design Considerations

- **スタック構造の抽象化が必要**
  - 回路レベルでは単一MOSと同等に扱いたい
- **PDKの抽象モデル定義**
  - 電気モデル・熱モデルの新規定義が必要
- **レイアウト上の対称性強化**
  - 1セル内にn/p両デバイスを自然配置できる可能性

---

## 🔮 教育・展開への示唆｜Educational & Strategic Implications

- **教育分野では、CFETを“技術収束点”として紹介する意義が大きい**
- **FinFET → GAA → CFETという進化系統の整理により、設計思想・製造困難性の本質を理解できる**
- **Edusemiでは、CFETを扱うことで「先端トランジスタ設計の終着点」を網羅可能**

---

### 🔙 関連リンク｜Backlinks

- [1.5 CFET構造とスタック型MOSの展望](f1_5_cfet.md)
- [補足F1-02：GAAプロセス](appendixf1_02_gaaflow.md)

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)
