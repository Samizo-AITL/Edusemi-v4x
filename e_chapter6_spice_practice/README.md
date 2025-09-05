---
title: "🛠 第6章: SPICE実践演習"
layout: default
---

---

# 🛠 第6章: SPICE実践演習 | SPICE Practice for Devices and Circuits

本章では、**Edusemi-v4x 基礎編**で学んだ FinFET / GAA / CFET の概念や  
**Wide Bandgap (SiC / GaN)** の特徴を、SPICEシミュレーションで再現して確認します。  
*This chapter reinforces concepts from the basics through hands-on SPICE simulations.*

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter6_spice_practice/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter6_spice_practice) |

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
```

---

## ✅ 注意事項 | Notes
	•	モデルは教育用の簡易パラメータ（Level=1 MOS, VSWITCH）。
	•	厳密な設計には BSIM-CMG, ASM-HEMT, PDKモデル への置換が必要。
	•	実行環境: NGSpice / LTspice で動作確認済み。

---

## 📘 `devices/nmos_iv_characteristics.spice`

```spice
* ============================================================
* NMOS Id–Vds / Id–Vgs Characteristics (Educational Example)
* Compatible: NGSpice / LTspice
* ============================================================
.option numdgt=6
.temp 25

* Bias sources
Vgs g 0 0
Vds d 0 0

* Device under test (simple Level-1 MOS for clarity)
M1 d g 0 0 NMOS_L1 L=1u W=10u

.model NMOS_L1 NMOS(Level=1 VTO=0.6 KP=150e-6 LAMBDA=0.02)

* ---- Sweep 1: Id–Vds at multiple Vgs
.dc Vds 0 2.5 0.01 sweep Vgs 0.8 2.0 0.4
.print dc V(d) I(Vds) V(g)

* ---- Sweep 2: (optional) Id–Vgs at fixed Vds
*.dc Vgs 0 2.5 0.01
*.param VDS_FIX=1.0
*Vds d 0 {VDS_FIX}
*.print dc V(g) I(Vds)

.end
```

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)

