---
layout: default
title: 3D NAND Flash Memory
---

---

# 🗂️ 3D NAND Flash Memory | 3D NANDフラッシュメモリ

---

## 📘 Overview | 概要

3D NAND is a flash memory technology that achieves **non-volatility, high capacity, and cost efficiency**.  
3D NANDは、**不揮発・大容量・コスト効率**を実現したフラッシュメモリ技術です。

While 2D NAND (planar) faced challenges such as **scaling limits and reliability degradation**,  
the 3D structure stacks memory cells **vertically** to continue capacity improvements.  
従来の2D NAND（平面構造）では**微細化限界や信頼性劣化**が問題化したため、  
セルを**垂直方向に積層（3D構造）**することでスケーリングが継続されています。

- Widely used in SSDs, eMMC, UFS, and other **storage devices**  
- 電源オフでもデータを保持し、**長期保存が可能**  
- Large capacities are achieved by **storing multiple bits per cell (TLC/QLC)**  
  **1セルで複数ビット記憶（TLC/QLC）**を実現

---

## 🧱 Structure and Evolution | 構造と進化

```mermaid
flowchart TB
    Controller[Controller<br>コントローラ<br>ECC, wear-leveling, I/F control]
    CellArray[Cell Array (3D Stacked)<br>セルアレイ（垂直積層）<br>64 → 500+ layers]

    Controller --> CellArray
```

### 🔍 Key Elements | 基本構造と技術要素

| Element 要素 | Description 説明 |
|--------------|------------------|
| Charge Trap / Floating Gate | Stores data via trapped charge (non-volatile) <br> 電荷を絶縁層に閉じ込めてデータを保持 |
| TLC / QLC | Triple-/Quad-Level Cell (3 or 4 bits per cell) <br> 1セルで3〜4ビット記憶 |
| Page / Block / Die | Hierarchical access units <br> 階層的な単位で読み書き・消去を管理 |

---

## 📊 Memory Comparison | メモリ比較

| Feature 特性 | 3D NAND | MRAM | SRAM | DRAM |
|---------------|---------|------|------|------|
| Non-volatility 不揮発性 | ◎ | ◎ | × | × |
| Endurance 書換回数 | △ (10⁴–10⁵) | ◎ (10¹⁵+) | ◎ | ◎ |
| Write Speed 書換速度 | × (µs–ms) | ◎ | ◎ | ○ |
| Capacity 容量 | ◎ (TB-scale) | ○ | △ | ◎ |
| Area Efficiency 面積効率 | ◎ (3D stacked) | △ | △ | ◎ |

---

## 🧭 SoC Integration | SoC設計との関係

| Item 項目 | Details 内容 |
|-----------|--------------|
| Connection 接続方式 | Typically external (eMMC, UFS, NVMe) |
| Role 役割 | Stores boot code, logs, data |
| Control 制御技術 | Requires ECC (LDPC, etc.), wear-leveling, caching |
| Filesystem | Co-design with software (FTL required) <br> ソフトウェア連携が重要 |

---

## 📌 Hierarchy and Design Aspects | 階層構成と設計観点

| Level 階層 | Description 概要 |
|------------|-----------------|
| Cell | Stores 1–4 bits using trapped charge |
| Page | Minimum write unit (2–16KB) |
| Block | Erase unit (multiple pages) |
| Die / Channel | Physical chip structure (controls blocks) |

> 💡 NAND erases in **block units**, requiring **copy and relocation**.  
> This makes the **controller (FTL: Flash Translation Layer)** crucial for performance and endurance.  
> NANDは**ブロック単位での消去**が必要であり、**書き換えのたびにコピー＆再配置が発生**。  
> **コントローラ設計（FTL）**が性能・寿命に大きく影響します。

---

## ⚠️ Design Considerations | 設計・使用上の注意点

| Issue 課題 | Details 内容 |
|------------|--------------|
| Endurance 書換え寿命 | TLC/QLC typically limited to 1K–100K writes |
| Retention 劣化 | Data loss due to charge leakage over time/temperature |
| Read Disturb 読み出し干渉 | Inter-cell interference during frequent reads |
| ECC 誤り訂正 | Trade-off between correction strength and latency |

---

## 📚 Educational Value | 教材的意義

- Illustrates **co-design between memory, controller, and software**  
- Demonstrates **trade-offs in capacity, speed, endurance**  
- Connects to **storage protocols and lifetime evaluation**

---

## 🔗 Related Chapters | 関連章

- [mram.md](./mram.md)：Comparison with MRAM  
- [Chapter 6: Testing & Packaging](../chapter6_test_and_package/)：Reliability testing (temperature, aging)  
- [Applied Chapter 7: Automation & Verification](../d_chapter7_automation_and_verification/)：Write wear and storage test automation

---

🏘 [Applied Chapter 1: Memory Technologies｜応用編 第1章：メモリ技術](../d_chapter1_memory_technologies/README.md)

---

© 2025 Shinichi Samizo / MIT License
