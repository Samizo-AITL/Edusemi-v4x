---
title: "🛠 第6章: SPICE実践演習"
layout: default
---

# 🛠 第6章: SPICE実践演習 | SPICE Practice for Devices and Circuits

本章では、**Edusemi-v4x 基礎編**で学んだ FinFET / GAA / CFET の概念や  
**Wide Bandgap (SiC / GaN)** の特徴を、SPICEシミュレーションで再現して確認します。  
*This chapter reinforces concepts from the basics through hands-on SPICE simulations.*

---

## 📑 演習内容 | Exercises

### 1) デバイス特性 | Device Characteristics
- **File**: `devices/nmos_iv_characteristics.spice`  
- **Run**: `.dc` で Id–Vds、Id–Vgs カーブを描画  
- **学びのポイント**: Vth 抽出、飽和領域・線形領域の境界  
- *Extract threshold voltage, observe linear vs saturation regions*

---

### 2) CMOSインバータ | CMOS Inverter (FinFET vs GAA)
- **Files**:  
  - `circuits/inv_cmos_finfet.spice`  
  - `circuits/inv_cmos_gaa.spice`  
  - `circuits/inv_common_models.inc`  
- **Run**: `.tran` で伝達特性（VTC）と遅延を観察  
- **学びのポイント**: Vth・gmの違いがノイズマージン・遅延に与える影響  
- *Impact of threshold voltage and gm differences on VTC and delay*

---

### 3) GaN vs SiC スイッチング | GaN vs SiC Switching
- **File**: `power/gan_vs_sic_switching.spice`  
- **Run**: `.tran` で出力電圧、負荷電流、ゲート波形を比較  
- **学びのポイント**: 高速スイッチング (GaN) vs 高耐圧・安定性 (SiC) の違い  
- *Contrast fast switching of GaN vs high-voltage stability of SiC*

---

## 🖼️ 結果画像の埋め込み（GitHub Pages対応）

```html
<img src="{{ '/e_chapter6_spice_practice/images/spice_results/inverter_vtc.png' | relative_url }}" alt="inverter_vtc" style="max-width:80%;">
