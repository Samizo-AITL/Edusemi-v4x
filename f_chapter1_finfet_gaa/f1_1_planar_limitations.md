---
layout: default
title: 1.1 プレーナMOSの限界と微細化の壁
---

---

# 🧬 1.1 プレーナMOSの限界と微細化の壁  
## 1.1 Scaling Limits of Planar MOSFET

---

## 📘 概要 / Overview

プレーナ型MOSFET（Planar MOS）は、90nm以前のCMOS世代において**性能・面積効率・製造性**に優れた構造でした。  
しかし40nmを下回るノードでは、以下のような**スケーリング限界（Scaling Limits）**が顕在化し、FinFETやGAAなど**構造的な転換**が求められるようになります。

Planar MOSFETs were dominant in CMOS technologies prior to the 90nm node, offering excellent performance and manufacturability. However, as feature sizes dropped below 40nm, fundamental **scaling limits** emerged, leading to structural innovations such as **FinFETs and GAA FETs**.

---

## 🔹 1.1.1 プレーナMOS構造の基本  
### Basic Structure of Planar MOSFET

- **チャネル領域**は基板表面に形成され、**ゲートは上面から1方向制御**  
- 構造が単純で、**高い歩留まりと量産性**を持つ  
- 90nm〜65nm世代では主流構造

> 🧠 **However:** 電界制御が単一方向であり、**ゲート長が30nm未満になると制御が不完全に**

---

## 🔸 1.1.2 微細化とともに発生する問題  
### Scaling-Induced Issues in Planar Devices

| **課題 / Issue** | **内容 / Description** |
|------------------|-------------------------|
| **短チャネル効果（SCE）** | チャネルが短くなると、ゲートが電位を制御できず、リーク増加・しきい値低下へ |
| **DIBL** | ドレイン電圧がソース側のバリアを下げてしまい、誤動作リスク増加 |
| **サブスレッショルド特性の劣化** | SS（Subthreshold Slope）が 60mV/dec → 80〜100mV/dec に悪化 |
| **オフリーク電流の増加** | 電源OFF時でも電流が流れ、静的消費電力の増加に直結 |
| **バルク効果・寄生容量** | 接地面積の増大により、高速動作時に遅延・ノイズ要因となる |

---

## 🔧 1.1.3 プロセス技術による一時的対処  
### Temporary Remedies via Process Enhancements

- **Halo Well / スーパーソース・ドレイン構造**  
  → 短チャネル下での電界制御を改善

- **チャネルドーピング増加**  
  → しきい値電圧V<sub>th</sub>の制御強化（ばらつき問題あり）

- **応力エンジニアリング（Strain Engineering）**  
  → SiGeソース・ドレイン / CESL により移動度改善

- **ハイk／メタルゲートの導入（45nm〜）**  
  → ゲートリーク電流の抑制と特性安定化

> ⚠️ これらの技術は**“場当たり的な緩和策”**にすぎず、根本解決にはならない。

---

## 🧠 1.1.4 設計上の限界とスケーリングの終焉  
### Design Constraints and End of Dennard Scaling

| **設計限界 / Limitation** | **具体内容 / Details** |
|----------------------------|--------------------------|
| **V<sub>th</sub>ばらつき** | ドーピング揺らぎ・界面粗さなどでチップ間／トランジスタ間の差が拡大 |
| **駆動電流の限界** | ゲート長の短縮ではI<sub>on</sub>が頭打ちになる |
| **RC遅延の支配** | ゲートのスピードは上がっても、**配線遅延が律速に** |

---

## 🚧 1.1.5 構造的ブレイクスルーの必要性  
### Structural Breakthroughs Needed

| **次世代技術 / Technology** | **特徴 / Key Features** |
|------------------------------|---------------------------|
| **FinFET** | ゲートが3面からチャネルを包囲（Tri-Gate）→ SCE抑制、22nm以降に主流化 |
| **GAA FET（Gate-All-Around）** | ゲートがナノシートを4面から完全包囲 → 制御性・スケーリングに優れる（2nm以降） |
| **CFET / VTFET** | 垂直方向にn/p型FETを積層 → 究極の集積密度・短距離・低電力化に寄与 |

> ✅ **FinFETやGAA構造は、プレーナ型では克服困難な電界制御の限界を突破するための技術革新である。**

---

## 🖼 図版リンク（予定 / Planned Images）

- `images/planar_scaling_limit.png`  
  → プレーナ構造におけるスケーリング限界の概念図  
- `images/sce_effect.png`  
  → SCEによるしきい値低下とバリア変形の模式図  
- `images/gate_control_comparison.png`  
  → Planar / FinFET / GAA のゲート包囲面の比較図

---

## ✅ まとめ / Summary

プレーナMOSは、長年にわたりCMOS技術を支えてきた**実績ある構造**でしたが、20nmを下回るノードでは**電気的・物理的制御の限界**が顕在化しました。  
この限界を乗り越えるため、**FinFET（22nm〜）やGAA FET（2nm〜）といった3D構造への転換**が必然となりました。

本節の内容は、次節以降の「FinFET構造（1.2）」および「GAA構造（1.3）」の背景理解として重要な基盤となります。

---

📘 次節：[1.2 FinFET構造の原理とプロセス概要](f1_2_finfet.md)

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)


