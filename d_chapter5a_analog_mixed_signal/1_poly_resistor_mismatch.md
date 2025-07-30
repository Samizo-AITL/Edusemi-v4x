# 🎚️ 5a.1 ポリ抵抗のばらつきと精度制御  
# 🎚️ 5a.1 Poly Resistor Mismatch and Precision Control

---

## 📘 概要｜Overview

ポリシリコン抵抗（Poly Resistor）は、AMS設計において電流源、バイアス生成、電圧リファレンスなど多用途で使用されますが、その**ばらつき（Mismatch）や温度依存性**はアナログ性能に大きな影響を及ぼします。

Poly resistors are widely used in AMS design for current sources, bias generation, and voltage references. However, **mismatch and temperature dependence** can significantly impact analog performance.

---

## ⚠️ 主な課題｜Key Issues

| 項目｜Issue | 内容｜Description |
|---------------|----------------|
| 抵抗値の面内ばらつき | フィルム厚さ、ドーピング濃度の微小不均一 |
| レイアウト依存のばらつき | 配線ストレス、形状効果（Length × Width） |
| 温度係数（TCR） | PTAT/CTAT動作における傾き誤差 |
| モデル誤差 | コーナーごとのSPICEモデルと実測乖離 |

---

## 📏 ポリ抵抗の代表値｜Typical Values of Poly Resistors

| 項目｜Item | 代表値（0.18μm例）｜Typical Value (0.18μm Node) | 備考｜Remarks |
|----------------|--------------------------|----------------------|
| シート抵抗 Rs | 約 100–500 Ω/□ | 高抵抗ポリ：> 500 Ω/□ |
| 温度係数 TCR | 約 +2000 ppm/°C | 正TCR（温度上昇で抵抗増加） |
| 面内ばらつき | ±10〜20%（通常）<br>±1〜2%（マッチング設計時） | レイアウト制御に依存 |
| 使用用途 | 電流ミラー、バイアス生成、リファレンス電圧 | 高精度回路では補償回路と併用 |

---

### 🔥 実工程における注意：バッチ処理炉の位置依存性  
### 🔥 Caution in Practice: Batch Furnace Rs Variation

TEL α-8 などのバッチ処理炉（Vertical Furnace）では、炉内のウエハ位置によって **シート抵抗（Rs）に最大±15〜20%の差**が生じる場合があります。  
これは、**ガス流量分布の非一様性**や**温度勾配**が主因であり、AMS用途における高精度設計では無視できません。

| 要因 | 内容 |
|------|------|
| 温度分布の非一様性 | 熱電対制御は炉中心に集中。端部は温度が低下しやすい |
| ガス流量勾配 | POCl₃/BBr₃などのドーピングガス分布が上下で不均一 |
| ドーパント再分布 | 高温アニール中の再拡散によってドープ量が変動 |

**対策例：**

- 最外周ウエハはダミー用途に使用（回路マスク除外）
- ドーピングガスとキャリアガスの流量均一化（Recipe調整）
- ウエハ枚数制限によるバッチ均一性の最適化

---

## 🔧 設計対策｜Design Techniques

| 手法｜Technique | 説明｜Description |
|--------|---------|
| **長尺化（L≫ΔL）** | 短寸法での相対ばらつきを抑える |
| **共通中心配置（Centroid）** | 面内勾配による系統誤差を相殺 |
| **ミラー配置＋ダミー追加** | 対称性確保とストレスキャンセル |
| **温度補償回路との併用** | PTAT/CTAT補償でTCR影響を緩和 |
| **自己アライメント抵抗構造** | リソグラフィばらつき低減（例：Spacer Resistor） |

---

## 🧪 実務的影響｜Practical Impact Examples

- バンドギャップ・リファレンス電圧の不安定化  
  *Inaccuracy in bandgap reference output*
- DAC出力オフセットやゲイン誤差の顕在化  
  *DAC offset and gain mismatch*
- 電流ミラー構成におけるバイアス誤差拡大  
  *Biasing errors in current mirrors*

---

## 🧭 関連項目｜Related Topics

- [`layout_considerations.md`](../d_chapter5_analog_mixed_signal/layout_considerations.md)：マッチングレイアウトの基本  
- [`2_transistor_matching.md`](./2_transistor_matching.md)：隣接MOSのばらつき抑制  
- [`ams_node_selection.md`](../d_chapter5_analog_mixed_signal/ams_node_selection.md)：プロセス特性と抵抗オプション

---

## 🧠 用語解説｜Glossary

| 用語｜Term | 意味｜Meaning |
|----------|----------------|
| TCR | Temperature Coefficient of Resistance（温度係数） |
| PTAT | Proportional To Absolute Temperature（絶対温度比例） |
| CTAT | Complementary To Absolute Temperature（絶対温度反比例） |

---

## ✅ まとめ｜Summary

ポリ抵抗は便利で汎用的な素子ですが、ばらつき・温度依存・レイアウト感度を適切に設計で扱うことが求められます。AMS設計では、**配線とパターン精度、温度特性補償の組み合わせが鍵**となり、加えて**工程ばらつき（炉内位置やレシピ）も実務上は見逃せない要因**です。

Poly resistors are versatile but require careful design to manage mismatch, temperature effects, and layout sensitivity. In AMS design, **precision layout, temperature compensation, and process variation awareness** are all critical to success.

---
