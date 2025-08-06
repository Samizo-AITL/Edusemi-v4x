---
layout: default
title: プロセスノード比較：180nm / 130nm / 90nm
---

---

# 📐 プロセスノード比較：180nm / 130nm / 90nm  
**Process Node Comparison: 180nm / 130nm / 90nm**

本資料では、180nm・130nm・90nm 各世代のCMOSロジックプロセスを比較し、技術進化・製造要素・設計上のポイントを明確にします。  
This document compares CMOS logic processes across the 180nm, 130nm, and 90nm nodes, highlighting technology evolution, manufacturing features, and design implications.

---

## 🔶 世代別プロセス比較表  
### Process Comparison Table by Node

| 項目 / Item | **180nm (0.18μm)** | **130nm (0.13μm)** | **90nm (0.09μm)** |
|-------------|--------------------|---------------------|--------------------|
| **時期 / Era** | 1999–2002 | 2002–2004 | 2004–2006 |
| **チャネル長 / L<sub>eff</sub>** | 約90nm | 約70nm | 約50nm |
| **ゲート酸化膜 / Gate Oxide (T<sub>ox</sub>)** | SiO₂ ~2.5–4.0nm | SiON ~2.2nm | SiON ~1.4nm |
| **有効電界 / E<sub>ox</sub>** | ~4.5 MV/cm | ~5.5 MV/cm | ~7.1 MV/cm |
| **サリサイド / Salicide** | CoSi₂ | CoSi₂ → NiSi 移行期 | NiSi |
| **配線金属 / Interconnect** | Al-Cu（Wプラグ） | Cu（Dual Damascene） | Cu（Dual Damascene） |
| **絶縁膜 / ILD** | SiO₂ / FSG | Low-k（k ≈ 3.0） | ULK（k ≈ 2.5） |
| **ゲート電極 / Gate Poly** | 単一n⁺ Poly | Dual Poly（n⁺ / p⁺） | Dual Poly（標準化） |
| **隔離構造 / Isolation** | STI | STI | 高密度対応STI |
| **応力技術 / Strain Engineering** | なし / None | 一部導入開始 | Strained-Si, SiGe |
| **電源電圧 / V<sub>dd</sub>** | 1.8V / 3.3V | 1.2V / 2.5V | 1.0V / 2.5V |
| **用途 / Application** | MCU、汎用SoC | 携帯・GPU向けSoC | 高速MPU、DSP |
| **製造難易度 / Complexity** | ★★★☆☆ | ★★★★☆ | ★★★★★ |
| **技術的限界 / Limiting Factor** | RC遅延・デバイス面積 | ゲートリーク電流 | SCE、リーク、ULK信頼性 |

---

## 🔬 デバイス特性比較（NMOS, W=10μm / L=L<sub>typ</sub>）  
### Device Characteristics Comparison (W=10μm)

| 特性 / Parameter | 180nm | 130nm | 90nm |
|------------------|--------|--------|--------|
| **T<sub>ox</sub> (nm)** | ~4.0 | ~2.2 | ~1.4 |
| **E<sub>ox</sub> (MV/cm)** | ~4.5 | ~5.5 | ~7.1 |
| **V<sub>th</sub> (V)** | ~0.45 | ~0.35 | ~0.30 |
| **I<sub>d,lin</sub> (μA)** | ~550 | ~600 | ~650 |
| **I<sub>d,sat</sub> (μA)** | ~850 | ~950 | ~1000 |
| **I<sub>off</sub> (nA)** | ~10 | ~50 | ~200 |
| **BV<sub>ds</sub> (V)** | ~3.3 | ~2.5 | ~2.0 |

> 📘 条件：W = 10μm、L = L<sub>typ</sub>（ノードに応じて90nm〜50nm）、V<sub>ds</sub> = V<sub>dd</sub>  
> ※ 代表的な業界平均・公開モデルに基づく近似値。温度・バイアス条件によって変動あり。

---

## 🔸 解説付きまとめ  
### Summary with Commentary

### 🔹 180nm（0.18μm）ノード
- 最後の主流 **Al配線** 世代。RC遅延対策に **WプラグやFSG** 導入。
- Toxは厚く **リークは少ない** が、速度制約あり。
- 静電信頼性・耐圧設計に優れる。

### 🔹 130nm（0.13μm）ノード
- **Cu + Low-k** 本格導入、Id向上とRC遅延のバランスを取る。
- Vth低下とともにIoff増加傾向、**リーク制御が設計課題** に。
- CoSi₂からNiSiへの転換期。

### 🔹 90nm（0.09μm）ノード
- Toxが限界の **1.2nm台** に到達し、**トンネルリーク顕在化**。
- NiSi、Strained-Si、ULK導入で高速化と消費電力のバランス追求。
- Ioff急増。静止電力制御にマルチV<sub>th</sub>設計が必須。

---

## 📚 関連教材 / Related Materials

- [0.18μm Logic Process Flow](./0.18um_Logic_ProcessFlow.md)
- [0.13μm Logic Process Flow](./0.13um_Logic_ProcessFlow.md)
- [0.09μm Logic Process Flow](./0.09um_Logic_ProcessFlow.md)
- [MOS Characteristics and Scaling](../chapter4_mos_characteristics/)
- [FinFET and Scaling Limits](../chapter4_mos_characteristics/4.8_scaling_limits_and_finfet.md)

---

## ✍️ 教育的活用例 / Educational Use Cases

- プロセスノードごとの **電気特性スケーリングの可視化**
- ゲート酸化膜厚と電界強度（E<sub>ox</sub>）の関係を数式・図で理解
- V<sub>th</sub>・I<sub>off</sub>・BV<sub>ds</sub> が設計に与える影響を実感
- FinFET導入前のCMOSスケーリングの限界と設計工夫を議論

---

[← 戻る / Back to Chapter 3: Process Evolution Top](../chapter3_process_evolution/README.md)

