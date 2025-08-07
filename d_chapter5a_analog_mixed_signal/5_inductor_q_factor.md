---
layout: default
title: 5a.5 インダクタのQ値改善と配線・基板設計
---

---

# 🌀 5a.5 インダクタのQ値改善と配線・基板設計  
**🌀 5a.5 Improving Inductor Q-Factor via Wiring and Substrate Design**

---

## 📘 概要｜Overview

オンチップインダクタは、RF回路、PLL、フィルタなどに不可欠ですが、**高周波域での損失によってQ値（Quality Factor）が大幅に低下**しやすい構造です。  
その性能は主に、**直流抵抗（R）・基板損失・寄生容量・金属材質**に依存しています。

On-chip inductors are essential in RF circuits, PLLs, and filters, but their **Q-factor degrades significantly due to high-frequency losses**.  
Q performance depends mainly on **DC resistance, substrate losses, parasitic capacitance, and metal stack properties**.

---

## ⚠️ Q値を制限する要因｜Q-Limiting Factors

| 要因｜Factor | 内容｜Description |
|--------|------------------------------|
| 直流抵抗（R） | 金属配線が細い／薄いと損失が増える |
| 基板導電損 | 配線下のシリコン基板に誘導電流が流れエネルギー損失 |
| 寄生容量 | 配線間や配線-基板間の容量が共振周波数を下げる |
| スキン効果 | 高周波で電流が金属表面に集中し、有効断面積が低下 |
| エディ電流 | シールド無し基板に電磁誘導による渦電流が生じる |

---

## 📈 Qの定義と周波数依存性｜Q Definition and Frequency Behavior

インダクタのQ値は以下の式で定義されます：

$$
Q(f) = \frac{2\pi f L}{R(f)}
$$

- $f$：周波数  
- $L$：インダクタンス  
- $R(f)$：周波数依存の抵抗（スキン効果含む）

Qはあるピーク周波数で最大となり、それ以降は寄生容量や抵抗で低下します。

---

## 🔧 Q値向上の技術｜Techniques to Improve Q

| 対策｜Technique | 効果・説明｜Effect / Description |
|--------|------------------------------|
| **トップメタルの活用** | 厚いAl層やCu層を使用し、配線抵抗を大幅に低減 |
| **幅広配線設計** | 電流密度を下げてスキン効果の影響を緩和 |
| **Patterned Ground Shield（PGS）** | GND下地にスリット入り金属を敷設 → 基板誘導損の抑制 |
| **高抵抗基板の選択** | 複数kΩ·cmのP型基板やDeep N-Wellで基板電流を遮断 |
| **マルチターン最適化** | ターン数と自己共振周波数（SRF）のバランス調整 |

---

## 🧪 実務的な影響｜Practical Impact Examples

- **PLL出力のジッタが高くなる**  
  *Increased jitter in PLL output due to low-Q inductor*
- **RFフィルタの選択度が不十分**  
  *Poor selectivity in RF filters from inductor loss*
- **LCタンク回路のQが不足し、ゲインが減衰**  
  *LC tank gain reduction due to inadequate Q-factor*

---

## 📏 Q向上の設計パラメータ例｜Example Parameters

| 設計項目 | 代表値（0.18μm） | 備考 |
|----------|------------------|------|
| 金属層 | Top Al層（3〜5μm厚） | 抵抗最小化 |
| 線幅 | 10〜20μm程度 | スキン効果抑制 |
| ターン数 | 1〜3回 | SRFとのトレードオフ |
| 基板 | P-type 1–5kΩ·cm + Deep N-Well | 誘導損低減 |
| Qピーク周波数 | 1〜5GHz | 高Q時で10〜20が目安 |

---

## 🔗 関連研究リンク｜Related Research Link

以下は、薄膜磁性膜と導体層を組み合わせたインダクタ構造のFEM解析により、周波数帯別のQ値劣化要因と材料選定指針（Al vs Cu）を示した初期研究です。  
今日のオンチップRFインダクタ設計にも通じる知見を提供しています。

📄 [🧪 Thin-Film Inductor Development (1996–1997)](https://samizo-aitl.github.io/Edusemi-Plus/archive/in1996/thinfilm_microreactor.md)  
（信州大学におけるFEMベースの薄膜リアクトル設計／磁性膜とスパイラルAl構造）

---

## 🧭 関連項目｜Related Topics

- [`ams_node_selection.md`](../d_chapter5_analog_mixed_signal/ams_node_selection.md)：高周波特性と金属層設計の視点  
- [`chapter6_test_and_package/`](../chapter6_test_and_package/)：RFテスト時のQ測定手法  
- [`basic_blocks.md`](../d_chapter5_analog_mixed_signal/basic_blocks.md)：LC回路構成例との接続

---

## 🧠 用語解説｜Glossary

| 用語｜Term | 意味｜Meaning |
|--------|--------------------------|
| Q値 | Quality Factor。インダクタの性能指標（高いほど理想） |
| SRF | Self-Resonant Frequency。インダクタがキャパシタと共振する周波数 |
| PGS | Patterned Ground Shield。誘導損を抑えるグランド構造 |
| スキン効果 | 高周波で電流が導体表面に集中する現象 |

---

## ✅ まとめ｜Summary

オンチップインダクタのQ値は、**配線設計・基板構造・電磁結合制御**によって大きく改善可能です。  
AMS設計において高Qが必要な場合は、**プロセス設計段階から金属層と基板条件の最適化**が必要です。

The Q-factor of on-chip inductors can be greatly improved by **optimized wiring, substrate isolation, and EM shielding**.  
For AMS designs requiring high-Q inductors, **metal and substrate planning must be addressed from the process level**.

---

[🎛️ 応用編　第5章a：0.18um AMS設計技法　トップに戻る](./README.md)



