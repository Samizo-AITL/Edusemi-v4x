---
layout: default
title: 5a.1 ポリ抵抗のばらつきと精度制御 
---

---

# 🎚️ 5a.1 ポリ抵抗のばらつきと精度制御  
**🎚️ 5a.1 Poly Resistor Mismatch and Precision Control**

---

## 📘 概要｜Overview

ポリシリコン抵抗（Poly Resistor）は、AMS設計において電流源、バイアス生成、電圧リファレンスなど多用途で使用されますが、その**ばらつき（Mismatch）や温度依存性**はアナログ性能に大きな影響を与えます。

Poly resistors are widely used in AMS design for current sources, bias generation, and voltage references. However, **mismatch and temperature dependence** can significantly impact analog performance.

---

## ⚠️ 主な課題｜Key Issues

| 項目｜Issue | 内容｜Description |
|---------------|----------------|
| 抵抗値の面内ばらつき | 膜厚・ドーピング濃度の不均一性 |
| レイアウト依存のばらつき | ストレス効果や形状差（L × W） |
| 温度係数（TCR） | PTAT / CTAT傾向の誤差増大要因 |
| モデル誤差 | コーナーモデルと実測値の乖離 |

---

## 📏 代表値と仕様例｜Typical Characteristics

| 項目｜Item | 代表値（例：0.18μm）｜Typical (0.18μm Node) | 備考｜Remarks |
|------------------|------------------------|---------------------|
| シート抵抗 Rs    | 約 2k–4k Ω/□          | ノンドープ、サリサイドなし構造 |
| 温度係数 TCR     | +2000 ppm/°C          | 正TCR：温度上昇で抵抗増加 |
| 面内ばらつき     | ±10〜20%（通常）<br>±1〜2%（マッチング設計時） | 統計的ばらつき要素 |
| 使用例           | バイアス、基準電圧、電流源 | 高精度用途では補償必須 |

---

## 🔥 工程由来のばらつき｜Process-Induced Variation

> **バッチ炉（例：TEL α-8）におけるシート抵抗ばらつきは最大 ±15〜20% に達する場合がある。**

| 要因 | 内容 |
|------|------|
| 温度勾配 | 炉内位置（上下）で温度差が発生 |
| ガス流量分布 | POCl₃, BBr₃ などの注入ガス不均一 |
| アニールによる拡散変動 | ドーパントの再分布が生じる可能性 |

**対策：**

- ダミーウエハ配置によるエッジ効果低減
- ウエハ枚数制限による均一性改善
- ドーピング・アニールレシピ最適化

---

## 🔧 設計による補正手法｜Design Mitigation Techniques

| 手法｜Technique | 説明｜Description |
|--------|---------|
| **長尺構造化（L≫ΔL）** | 短距離による統計誤差を抑制 |
| **共通中心配置（Centroid）** | 勾配誤差を相殺する幾何配置 |
| **ミラー構成＋ダミー追加** | ストレス分布の均一化 |
| **温度補償回路併用** | PTAT / CTAT傾向のキャンセル |
| **自己整合型構造（Spacer等）** | リソグラフィ誤差の抑制設計 |

---

## 🧪 実務での影響例｜Practical Impact

| 回路 | ばらつきの影響例 |
|------|----------------|
| バンドギャップ基準 | 出力電圧のオフセット・温度傾斜誤差 |
| DAC / ADC | オフセット・ゲイン誤差（LSB単位で顕在化） |
| 電流ミラー | バイアス精度劣化、出力誤差 |

---

## 🧠 用語解説｜Glossary

| 用語｜Term | 意味｜Meaning |
|----------|----------------|
| Rs       | シート抵抗（Ω/□） |
| TCR      | Temperature Coefficient of Resistance（ppm/°C） |
| PTAT     | Proportional To Absolute Temperature |
| CTAT     | Complementary To Absolute Temperature |

---

## 📎 関連ファイル｜Related Files

- [`layout_considerations.md`](../d_chapter5_analog_mixed_signal/layout_considerations.md)
- [`2_transistor_matching.md`](./2_transistor_matching.md)
- [`ams_node_selection.md`](../d_chapter5_analog_mixed_signal/ams_node_selection.md)

---

## ✅ まとめ｜Summary

Poly抵抗は便利かつ汎用的ですが、ばらつき・TCR・レイアウト依存性など多くの課題を含みます。AMS回路での高精度化には、**工程理解とレイアウト手法の両輪による補償設計が必須**です。

Poly resistors are versatile but demand careful design due to mismatch, temperature variation, and layout sensitivity. In precision analog systems, both **process-aware design and layout best practices** are critical.

---
