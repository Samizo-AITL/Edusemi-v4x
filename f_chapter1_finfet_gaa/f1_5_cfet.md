# 1.5 CFET構造とスタック型MOSの展望  
# 1.5 CFET Structure and Outlook for Stacked MOS

---

## 📘 概要｜Overview

**CFET（Complementary FET）は、nFETとpFETを垂直方向に積層することで面積効率と配線自由度をさらに向上させる、ポストGAA時代のトランジスタ構造です。**  
本節では、FinFETやGAAとの連続性を踏まえ、CFETの構造、動作原理、製造課題、設計影響、今後の展望について整理します。

**Complementary FET (CFET)** refers to a future transistor structure in which **nFET and pFET are vertically stacked**, enabling further improvements in area scaling and layout flexibility beyond GAA.  
This section explains the CFET concept in the context of FinFET and GAA evolution, focusing on its structure, operating principles, manufacturing challenges, design implications, and future outlook.

---

## 🧱 構造原理｜Structural Concept

- GAAでは **複数の水平ナノシート**を積層（n/pが同一層）。
- CFETでは **nFETとpFETを縦に積層**（例：n-FET上にp-FET）。
- 垂直積層により、**配線層・セル面積・レイアウト対称性**を改善可能。

> In GAA, multiple horizontal nanosheets are stacked, but both nFET and pFET are placed side-by-side.  
> CFET vertically stacks nFET and pFET, enabling denser integration and better symmetry.
```
 p-FET   ← Upper layer
 ─────
 Oxide
 ─────
 n-FET   ← Lower layer
 ─────
 Substrate
```
 ---

## ⚡ 電気的特徴と設計影響｜Electrical Characteristics & Design Impact

| 項目｜Item | CFETの特性｜CFET Features |
|-----------|--------------------------|
| ゲート制御 | GAAと同等（4面制御）<br>Same as GAA (gate-all-around) |
| 対称性 | 垂直構造によりn/pの配置が対象<br>Vertical symmetry for n/p |
| クロストーク | ソース/ドレイン間の干渉に注意が必要<br>Increased risk of crosstalk |
| 配線自由度 | 配線層の空間が広がる<br>More routing flexibility |
| 設計難易度 | PDK整備・抽象化レイヤ必須<br>Requires advanced PDK support |

---

## 🏭 製造課題｜Manufacturing Challenges

- **チャネルごとのドーピング独立性**：nFETとpFETのドーピング分離が難しい
- **熱処理のステップ分離**：下層が熱予算を超えやすい
- **エピ成長と選択エッチング**：複数ステップの精度が極めて重要
- **BEOLとの整合性**：金属層との高さ調整やIRドロップ対応が必須

> Key challenges include independent doping control, thermal budget balancing between layers, selective epitaxy, and integration with BEOL (Back-End of Line).

---

## 🔮 今後の展望｜Future Outlook

- **2030年以降のCFET実装**がIntelやIMECロードマップに登場
- **システム・オン・スタック（SoS）**時代に向けた準備段階
- **EDA/PDKの仮想抽象設計**に対応した設計者教育が求められる

> CFET is positioned as a post-GAA solution, expected to emerge in the 2030s. Education and design must prepare for stack-aware abstractions.

---

### 🔗 関連補足｜Related Appendices

- [`appendixf1_04_cfet.md`](appendixf1_04_cfet.md)：CFETの構造変遷と技術的課題の詳細  
  *Detailed discussion of CFET structure evolution and key technical issues*

---

### 🏠 [特別編トップへ戻る｜Back to Special Edition Top](README.md)
