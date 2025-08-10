---
layout: default
title: "付録B1: 0.18µm / 0.13µm MOSトランジスタ基礎特性 | Appendix B1: Basic MOSFET Characteristics for 0.18µm / 0.13µm"
---

# 📎 付録B1: 0.18µm / 0.13µm MOSトランジスタ基礎特性  
**Appendix B1: Basic MOSFET Characteristics for 0.18µm / 0.13µm**

---

## 📝 概要 / Overview
**日本語**  
本付録では、0.18µmおよび0.13µmロジックプロセスにおけるMOSトランジスタの代表的な基礎特性を整理します。閾値電圧、ゲート酸化膜厚、移動度、飽和電流、リーク電流などを比較し、設計・教育における指針とします。

**English**  
This appendix summarizes representative basic characteristics of MOS transistors in 0.18µm and 0.13µm logic processes. Key parameters such as threshold voltage, gate oxide thickness, mobility, saturation current, and leakage current are compared to serve as design and educational references.

---

## 📊 基礎パラメータ比較 / Basic Parameter Comparison

| 項目 / Parameter | 単位 / Unit | **0.18 µm NMOS** | **0.18 µm PMOS** | **0.13 µm NMOS** | **0.13 µm PMOS** |
|---|---|---|---|---|---|
| チャネル長 L<sub>eff</sub> | nm | 180 | 180 | 130 | 130 |
| ゲート酸化膜厚 T<sub>ox</sub> | nm | 3.8〜4.0 | 3.8〜4.0 | 2.5〜2.7 | 2.5〜2.7 |
| 閾値電圧 V<sub>th</sub> | V | 0.40〜0.45 | -0.40〜-0.45 | 0.35〜0.40 | -0.35〜-0.40 |
| 飽和電流 I<sub>dsat</sub> @ V<sub>gs</sub>=V<sub>dd</sub> | mA/µm | 0.55〜0.65 | 0.25〜0.30 | 0.70〜0.80 | 0.35〜0.40 |
| リーク電流 I<sub>off</sub> | nA/µm | 0.1〜1 | 0.1〜1 | 0.5〜5 | 0.5〜5 |
| 移動度 μ<sub>n</sub>/μ<sub>p</sub> | cm²/V·s | 500〜550 | 200〜250 | 450〜500 | 180〜220 |
| ゲート容量密度 C<sub>ox</sub> | fF/µm² | 8.6〜9.0 | 8.6〜9.0 | 12〜13 | 12〜13 |
| 供給電圧 V<sub>dd</sub> | V | 1.8 | 1.8 | 1.2〜1.5 | 1.2〜1.5 |

---

## 📈 特性グラフ / Characteristic Graphs

> 軸表記 / Axis labels: **横軸 (x)** = 電圧 (V<sub>g</sub> または V<sub>d</sub>)、**縦軸 (y)** = 電流 (I<sub>d</sub>) または 容量 (C<sub>g</sub>)

- **Vg–Id 特性**（Vd固定、V<sub>th</sub>抽出に使用）
- **Vd–Id 特性**（Vgをパラメータにしたドレイン掃引）
- **Vg–Cg 特性**（酸化膜厚の違いを反映したゲート容量）

![Vg-Id Characteristics 0.18um vs 0.13um](../assets/images/mosfet_vg_id_018_013.png)  
![Vd-Id Characteristics 0.18um vs 0.13um](../assets/images/mosfet_vd_id_018_013.png)  
![Vg-Cg Characteristics 0.18um vs 0.13um](../assets/images/mosfet_vg_cg_018_013.png)

---

## 🔍 教育的ポイント / Educational Insights

**日本語**
- 酸化膜の薄膜化によりゲート容量密度が増加し、高速動作に寄与。  
- V<sub>th</sub>の低下に伴うリーク電流増加は、低電力設計における重要課題。  
- 0.18µmはsky130と同様に1.8V駆動で扱いやすく、教育向け評価に最適。  
- 0.13µmは低電圧駆動・高周波動作の理解に適し、先端設計の橋渡しとして有効。

**English**
- Thinner oxide increases gate capacitance density, enabling higher-speed operation.  
- Lower V<sub>th</sub> results in higher leakage current, a critical issue in low-power design.  
- 0.18µm, like sky130, operates at 1.8V, making it ideal for educational evaluation.  
- 0.13µm suits understanding of low-voltage, high-frequency operation, bridging to advanced nodes.

---

## 📚 関連リンク / Related Links
- [基礎編 第4章: MOSトランジスタ特性と設計基盤](../f_chapter4_mos_basics/README.md)
- [付録: プロセスノード進化と物理パラメータ](../appendix_f1_node_evolution.md)

---

🔙 [第4章に戻る / Back to Chapter 4](../f_chapter4_mos_basics/README.md)
