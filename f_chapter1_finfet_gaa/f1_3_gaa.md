---
layout: default
title: 1.3 GAA構造：完全ゲート包囲による短チャネル制御の極限へ  
---

---

# 🧬 1.3 GAA構造：完全ゲート包囲による短チャネル制御の極限へ  
## 1.3 GAA Structure: Ultimate Short-Channel Control with Gate-All-Around

---

## 📘 概要 / Overview

**GAA（Gate-All-Around）Multi-Nanosheet FET**は、FinFETの後継として登場した**完全ゲート包囲型**のトランジスタ構造です。  
チャネルとなる**ナノシート（Nanosheet）**をゲートが**四方向から完全に包囲**することで、FinFET以上の電界制御性と短チャネル耐性を実現します。

GAA FETs are next-generation transistors that **fully surround the channel** using a gate from all four sides. With nanosheet channels, GAA offers improved electrostatic control compared to FinFETs, and is becoming standard for nodes at 2nm and below.

---

## 🔹 1.3.1 GAA Multi-Nanosheet の構造原理  
### Structural Principle of GAA FET

- **ナノシート構造 / Nanosheet Stacking**  
  - Si/SiGeを交互に積層し、**Siナノシートを空間中に浮かせる構造**  
  - Selective etchingで**SiGe層を除去 → Si層だけが残る**

- **ゲート構造 / Gate Wrap-Around**  
  - 各ナノシートを**全面（4面）から包囲**する形でゲートが形成される  
  - HfO₂などのハイk酸化膜とTiNなどのメタルゲートを**コンフォーマル（均一）に成膜**

- **シート並列構造 / Multi-Nanosheet Stack**  
  - 通常3〜5枚のシートを垂直方向に積層  
  - **電流駆動力を段階的にスケーリング**可能

> 💡 GAA構造はFinFETよりもさらに優れたスケーリングポテンシャルと制御性を持ちます。

---

## 🔸 1.3.2 FinFETとの比較  
### Comparison with FinFET

| **項目 / Item** | **FinFET** | **GAA FET** |
|-----------------|------------|-------------|
| ゲート包囲面 / Gate Control | 3面（Top + Sides） | 4面（All Around） |
| チャネル構造 / Channel | Fin構造（縦型） | Nanosheet構造（横積層） |
| DIBL特性 / DIBL | ~70 mV/V | ~50 mV/V以下 |
| オフリーク電流 / I<sub>off</sub> | 数nA/µm | 更に低い（完全ゲート支配） |
| ゲート容量 / Capacitance | 中程度 | やや大きい（多層包囲） |

---

## 🏗 1.3.3 製造プロセス上の特徴  
### Process Characteristics of GAA

- **Si/SiGeエピタキシャル積層 / Superlattice Formation**  
  - 高精度のエピタキシャル成長（膜厚誤差 ≦ 1nm）

- **選択エッチング / Selective Etch**  
  - SiGe層をHCl等で除去し、**空中に浮いたナノシート**を形成

- **ゲート成膜の難易度 / Gate Deposition Challenge**  
  - 内部空間に対し**均一なコンフォーマル堆積**が必要 → ALD（原子層堆積）が必須

- **ストレスエンジニアリング / Strain Engineering**  
  - ナノシートに直接ストレスを加え、キャリア移動度を向上

> 📎 詳細なプロセスフローは [`appendixf1_02_gaaflow.md`](./appendixf1_02_gaaflow.md) を参照

---

## 🧠 1.3.4 設計への影響とPDK制約  
### Design Implications and PDK Constraints

- **シート数の離散設計 / Discrete Width**  
  - Fin数に代わって**「3シートセル」「4シートセル」**のようにライブラリが構成される

- **寄生容量とRC制御 / Parasitic Capacitance & RC**  
  - 包囲面積が大きく、**ゲート-チャネル間容量が増加**  
  - RC抽出は3Dモデル精度が求められる（特にBEOLとの結合）

- **レイアウト制約 / Layout Considerations**  
  - 空洞構造形成のため、**サポート構造やリリース方向**への配慮が必要

---

## 🔭 1.3.5 今後の展望と融合技術  
### Future Directions and Integration

| **観点 / Aspect** | **展望 / Outlook** |
|-------------------|---------------------|
| スケーリング限界突破 | L<sub>ch</sub> ≦ 10nmに対応可能 |
| CFETとの融合 | P/Nを垂直積層 → Vertical CFETへ |
| 3D実装対応性 | 薄型・高密度ゆえ、3D-ICに適応性あり |

---

## 🖼 図版（予定 / Planned Diagrams）

- `images/gaa_stack_structure.png`：Si/SiGe積層構造と除去ステップ  
- `images/gaa_gate_all_around.png`：4面ゲート包囲構造断面図  
- `images/gaa_release_process.png`：ナノシート解放プロセス模式図

---

## ✅ まとめ / Summary

GAA Multi-Nanosheet FETは、FinFETの物理限界を超えて**完全ゲート包囲制御**を実現する革新的トランジスタです。  
2nm以降の標準構造として導入されつつあり、**設計自由度、寄生制御、製造プロセスの複雑さ**が今後のカギとなります。

GAA offers excellent scalability and superior short-channel control. While manufacturing is complex, it enables high-performance logic at the most advanced nodes.

---

📘 次節：[1.4 プレーナ vs FinFET vs GAAの特性比較](f1_4_comparison.md)

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)


