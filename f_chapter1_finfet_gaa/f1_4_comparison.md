---
layout: default
title: 1.4 FinFETとGAAの比較：構造・性能・設計影響の視点から
---

---

# 🧬 1.4 FinFETとGAAの比較：構造・性能・設計影響の視点から  
## 1.4 Comparison of FinFET and GAA: Structure, Performance, and Design Impacts

---

## 📘 概要 / Overview

本節では、**FinFET**と**GAA（Gate-All-Around）Multi-Nanosheet FET**の間にある構造的・電気的・設計上の違いを体系的に比較し、それぞれの**技術的優位性と限界**を明らかにします。

This section provides a systematic comparison between **FinFET** and **GAA** devices, focusing on structural, electrical, and design aspects. Understanding these differences is essential for technology selection in advanced nodes.

---

## 🔹 1.4.1 ゲート構造とチャネル制御性  
### Gate Structure and Channel Control

| **項目 / Item** | **FinFET** | **GAA FET** |
|------------------|------------|--------------|
| ゲート包囲面 / Gate Coverage | 3面（Top + Sides） | 4面（All-Around） |
| チャネル制御性 / Control | 良好（SS ~70 mV/dec） | 優秀（SS ~60 mV/dec以下） |
| DIBL特性 / DIBL | ~70 mV/V | ~50 mV/V以下 |
| オフリーク電流 / I<sub>off</sub> | 数nA/µm | 数百pA/µmまで低下可能 |

---

## 🏗 1.4.2 構造形成と製造難易度  
### Fabrication and Process Complexity

| **項目 / Item** | **FinFET** | **GAA FET** |
|------------------|------------|--------------|
| Fin形成 / Fin Formation | STI上に立てる | Si/SiGe積層 → 選択エッチでシート解放 |
| ゲート形成 / Gate Formation | 包囲性は高いが空洞なし | 空洞内へのConformal成膜（ALD）必須 |
| 歪み導入 / Stress | SiGe S/DやStress Liner | シート構造そのものにストレス適用可 |
| 成膜均一性 / Film Uniformity | 容易 | 困難（3D形状への制御要） |

---

## ⚙️ 1.4.3 性能とスケーリング適性  
### Performance and Scaling Suitability

| **項目 / Item** | **FinFET** | **GAA FET** |
|------------------|------------|--------------|
| 駆動能力 / Drive Current | 高（Fin数で拡張） | 高（シート数で拡張） |
| 電圧依存性 / V<sub>dd</sub> Sensitivity | 中程度 | 低い（変動耐性も高） |
| スケーリング限界 / Scaling Limit | 約5nm前後 | 2nm以下に最適化可能 |
| 次世代適応性 / Future Integration | CFETに制約あり | CFET統合に適応（N/P積層） |

---

## 🧠 1.4.4 設計上の違い  
### Design Perspective

| **項目 / Item** | **FinFET** | **GAA FET** |
|------------------|------------|--------------|
| チャネル幅定義 / Width Definition | Fin数（離散） | シート数（離散） |
| セル構成 / Cell Units | 2-Fin, 3-Fin など | 3-sheet, 5-sheet など |
| PDK制約 / PDK Rules | Finピッチ・高さ制約あり | シート配置・リリース工程制約あり |
| 配線影響 / Routing Impact | Fin高さによる層間容量影響 | シート層とBEOLのRC結合に注意 |

---

## 🔭 1.4.5 将来展望と技術選定指針  
### Future Outlook and Selection Criteria

| **観点 / Aspect** | **FinFET** | **GAA FET** |
|--------------------|-------------|--------------|
| 実用ノード / Current Nodes | 22nm〜5nm主流 | 3nm試作〜2nm量産期 |
| 技術成熟度 / Maturity | 高（製造・設計確立） | 発展途上（PDK・量産未成熟） |
| 今後の発展性 / Evolution | 改良止まり | CFET, VTFET等へ進化可能 |
| 設計戦略 / Design Approach | 既存Finセル継続 | GAA特化セル構築が必要（非置換型） |

---

## 🖼 図版リンク（予定 / Planned Diagrams）

- `images/finfet_vs_gaa_structure.png`  
  → FinFETとGAAの構造断面比較図  
- `images/finfet_vs_gaa_gatewrap.png`  
  → ゲート包囲構造の比較模式図  
- `images/finfet_vs_gaa_scaling.png`  
  → スケーリングロードマップ（ノード世代 vs チャネル構造）

---

## ✅ まとめ / Summary

FinFETとGAAは、いずれも**微細化時代のゲート制御を支える3D構造**であり、**構造・性能・製造・設計の全側面で明確な違い**を持ちます。  
特にGAAは、**次世代スケーリングやCFET・3D-IC技術との親和性が高く、2nm以降の戦略的選択肢**となる存在です。

FinFET and GAA represent two key approaches to 3D gate control in advanced CMOS nodes. GAA, with its full gate wrap and nanosheet scalability, is poised to lead post-2nm integration, despite manufacturing complexity.

---

📘 本章はここまでです。補足資料は以下をご参照ください：  
- [`appendixf1_03_finfet_vs_gaa.md`](./appendixf1_03_finfet_vs_gaa.md)：比較まとめ＋図解

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)
