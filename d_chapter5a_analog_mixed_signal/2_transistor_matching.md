# ⚖️ 5a.2 隣接トランジスタのマッチングとレイアウト設計  
# ⚖️ 5a.2 Matching of Adjacent Transistors and Layout Techniques

---

## 📘 概要｜Overview

アナログ回路においては、**隣接トランジスタの特性一致（マッチング）**が回路性能に直結します。  
入力オフセット、ゲイン誤差、CMRR、電流ミラー精度などは、**ペアMOSのしきい値 $V_{\mathrm{th}}$ や寸法のばらつき**に強く依存します。

In analog circuits, **matching between adjacent transistors** is directly tied to performance.  
Input offset, gain error, CMRR, and current mirror accuracy are highly dependent on **threshold voltage ($V_{\mathrm{th}}$) and dimensional variation** of paired MOS devices.

---

## ⚠️ マッチングに影響する要因｜Factors Affecting Matching

| 要因｜Factor | 内容｜Description |
|-------------|----------------|
| 寸法ばらつき | $L/W$ のミスマッチ。リソグラフィやエッチングの寸法誤差 |
| ドーピングプロファイルの差 | チャネル不均一性による $V_{\mathrm{th}}$ ずれ |
| 酸化膜厚の違い | Gate酸化膜の局所ばらつき（中心 vs 周辺） |
| ストレスやレイアウト配置 | ウェル形状・金属配線による機械的ストレスの影響 |
| 温度勾配・電源勾配 | 大規模チップでの局所温度やIRドロップの差 |

---

## 🔧 マッチングを高めるレイアウト技術｜Layout Techniques for Improved Matching

| 手法｜Technique | 説明｜Description |
|--------|---------|
| **共通中心配置（Common Centroid）** | グラジエント（温度/勾配）を平均化する対称配置 |
| **ミラー配置＋ダミートランジスタ** | エッジ効果・ストレス緩和。ABBA型が典型 |
| **等距離配線＋同長Metal** | 配線インピーダンスの差によるバイアス誤差を防ぐ |
| **ウェルシールド（Nwell or Pwellリング）** | サブストレートノイズやバルク変動の低減 |
| **レイアウト単位の正規化** | 同一レイアウトセルをインスタンスで使用し、EDA設計でもマッチング維持を図る |

---

### 🧮 モデル的なマッチングの指標：Pelgromモデル  
**Pelgrom's Law for $V_{\mathrm{th}}$ Mismatch**

$$
\sigma_{V_{\mathrm{th}}} = \frac{A_{V_{\mathrm{th}}}}{\sqrt{W \cdot L}}
$$

- $A_{V_{\mathrm{th}}}$：プロセス固有のマッチング係数（例：3–5 mV·μm）
- $W, L$：トランジスタの幅と長さ（μm）
- → 面積が大きいほどマッチングは向上する

---

## 🧪 実務的な問題例｜Practical Impact Examples

- オペアンプの入力オフセットが ±5mV 以上に悪化  
  *Op-amp input offset degradation exceeding ±5mV*
- カレントミラーの出力電流が +10% ずれる  
  *Current mirror output deviates by +10%*
- 差動対が温度勾配に敏感でオフセットが変動  
  *Differential pair offset varies with thermal gradients*

---

## 🧭 関連項目｜Related Topics

- [`1_poly_resistor_mismatch.md`](./1_poly_resistor_mismatch.md)：抵抗ミスマッチの補償回路との連携  
- [`layout_considerations.md`](../d_chapter5_analog_mixed_signal/layout_considerations.md)：AMSレイアウト全般の注意点  
- [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/)：$V_{\mathrm{th}}$ や SS のばらつき物理

---

## 🧠 用語解説｜Glossary

| 用語｜Term | 意味｜Meaning |
|----------|----------------|
| Common Centroid | 中心を共有するようにAB配置を対称に並べる配置法 |
| Dummy Transistor | 実回路に関与しないが周囲のばらつきを抑える補助素子 |
| Pelgrom Coefficient | $V_{\mathrm{th}}$ ミスマッチに対する統計モデルパラメータ |

---

## ✅ まとめ｜Summary

AMSにおけるトランジスタマッチングは、レイアウト技術・寸法設計・プロセス理解のすべてが交差する領域です。  
精度の高い回路を実現するには、**設計段階からマッチングレイアウトを徹底する文化と検証技術の整備が鍵**です。

Matching in AMS design sits at the intersection of layout, sizing, and process understanding.  
To ensure high-precision circuits, **intentional matching layout practices and validation tools must be embedded from the design stage**.

---

[🎛️ 応用編　第5章a：0.18um AMS設計技法　トップに戻る](./README.md)




