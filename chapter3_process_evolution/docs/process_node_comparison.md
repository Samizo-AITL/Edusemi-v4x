# プロセスノード比較：180nm / 130nm / 90nm  
# Process Node Comparison: 180nm / 130nm / 90nm

本資料では、180nm・130nm・90nm 各世代のCMOSロジックプロセスを比較し、技術進化・製造要素・設計上のポイントを明確にします。  
This document compares CMOS logic processes across the 180nm, 130nm, and 90nm nodes, highlighting technology evolution, manufacturing features, and design implications.

---

## 🔶 世代別プロセス比較表  
### Process Comparison Table by Node

| 項目 / Item | **180nm (0.18μm)** | **130nm (0.13μm)** | **90nm (0.09μm)** |
|-------------|-------------------|--------------------|-------------------|
| **時期 / Era** | 1999–2002 | 2002–2004 | 2004–2006 |
| **チャネル長 / L<sub>eff</sub>** | 約90nm | 約70nm | 約50nm |
| **ゲート酸化膜 / Gate Oxide** | SiO₂ 約2.5nm | SiON 約1.5nm | SiON 約1.2nm |
| **サリサイド / Salicide** | CoSi₂ | CoSi₂ or NiSi | NiSi |
| **配線金属 / Interconnect** | Al-Cu（多くはWプラグ） | Cu（Dual Damascene） | Cu（Dual Damascene） |
| **絶縁膜 / ILD** | SiO₂ / FSG | Low-k（k~3.0） | ULK（k~2.5） |
| **ゲート電極 / Gate Poly** | 単一n⁺ Poly | Dual（n⁺ / p⁺）Poly | Dual（標準化） |
| **隔離構造 / Isolation** | STI | STI | STI（縮小対応） |
| **応力技術 / Strain** | なし / None | 一部導入開始 | Strained-Si, SiGe |
| **電源電圧 / V<sub>dd</sub>** | 1.8V / 3.3V | 1.2V / 2.5V | 1.0V / 2.5V |
| **用途 / Application** | 汎用SoC、MCU | 携帯向けSoC、GPU | 高速MPU、DSP |
| **製造難易度 / Complexity** | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **技術的限界 / Limiting Factor** | RC遅延・面積 | ゲートリーク電流 | SCE, リーク, ULK信頼性 |

---

## 🔸 解説付きまとめ  
### Summary with Notes

### 🔹 180nm（0.18μm）
- 最後の主流Al配線世代。Wプラグ＋Al-Cu配線。
- ゲート酸化膜はSiO₂、SCE（短チャネル効果）はLDD構造で対応。
- CMOS混載やマイコン系製品で広く普及。

### 🔹 130nm（0.13μm）
- Cu配線とLow-k膜の本格採用。
- SiON酸化膜＋デュアルゲートポリの導入によりリーク抑制。
- サリサイドはCoからNiへ移行が始まる。

### 🔹 90nm（0.09μm）
- ゲート酸化膜厚が物理限界（1.2nm）に到達。
- NiSi、Strained-Si、ULK膜など多数の新技術を同時に導入。
- 信頼性・歩留まり確保に最も困難を伴った世代の1つ。

---

## 📚 関連教材 / Related Materials

- [0.18μm Logic Process Flow](./0.18um_Logic_ProcessFlow.md)
- [0.13μm Logic Process Flow](./0.13um_Logic_ProcessFlow.md)
- [0.09μm Logic Process Flow](./0.09um_Logic_ProcessFlow.md)
- [MOS Characteristics and Scaling](../chapter4_mos_characteristics/)
- [FinFET and Scaling Limits](../chapter4_mos_characteristics/4.8_scaling_limits_and_finfet.md)

---

## ✍️ 教育的活用例 / Educational Use Cases

- 世代別の設計制約とプロセス技術を対比して理解
- ゲート酸化膜の薄膜化とリークの関係を定量的に把握
- Cu/ULKの導入と配線信頼性への影響を評価
- FinFET登場前夜の限界要素を議論・演習

---
