---
layout: default
title: SRAM (Static Random Access Memory)
---

---

# 🧠 SRAM (Static Random Access Memory)

---

## 📘 概要｜Overview

**SRAM（Static RAM）** は、**高速で揮発性のメモリ**として、SoC内部に組み込まれる主要な構成です。  
SRAM (Static RAM) is a **fast and volatile memory**, widely embedded in SoCs.

DRAMのようにリフレッシュを必要とせず、6T構成セルで安定した保持が可能です。  
Unlike DRAM, it does not require refresh and can stably retain data using a 6-transistor (6T) cell.

**主な用途**：キャッシュ、レジスタファイル、LUTなど。組込みメモリとして活用。  
**Typical uses**: Cache memory, register files, LUTs. Widely used as embedded memory.

---

## 🔧 セル構造｜Cell Structure: 6T SRAM Cell

### 📐 構成図｜Schematic

```
               VDD
                |
              +---+
              | P1|───┐
              +---+   |
                |     |
                |    Q (保存ノード / Storage Node)
                |     |
  BL───AX1──────┘     └──────AX2───BL_bar
       |                        |
      WL -----------------------
                |     |
              +---+  +---+
              | N1|  | N2|   ← インバータ下部 / Bottom inverters
              +---+  +---+
                |     |
               GND   GND
```

### 🔍 各構成要素の説明｜Component Description

| 日本語 | English |
|--------|---------|
| P1/N1, P2/N2 | インバータを交差接続しラッチ構成<br>Cross-coupled inverters forming a latch |
| AX1 / AX2 | アクセスFET。WLによりON/OFF制御<br>Access transistors controlled by WL |
| Q / Q_bar | データ保持ノード<br>Data storage nodes |
| WL（Word Line） | セル選択信号線<br>Row select line |
| BL / BL_bar（Bit Line） | 読み書きデータ線（差動）<br>Differential data lines for read/write |

---

## 📊 特性と設計観点｜Characteristics and Design Considerations

| 日本語 | English |
|--------|---------|
| データ保持性：電源ONで安定<br>Stable as long as powered | Data retention: stable while powered |
| 面積：DRAMより大きい<br>Larger than DRAM | Area: larger than DRAM (6T) |
| 消費電力：書込大、待機小<br>High for write, low standby | Power consumption: high during write, low in standby |
| レイアウト：対称性重視<br>Symmetric layout critical | Layout: symmetry important |
| SNM設計：読み出し破壊対策<br>SNM tuning to avoid read disturb | SNM: static noise margin design is crucial |
| スピード：非常に高速<br>Very fast | Speed: extremely fast (suitable for cache) |

---

## 🏗 組込み設計での活用｜Use in Embedded Design

| 日本語 | English |
|--------|---------|
| SRAMマクロをPDKから呼出し（例：sky130） | Invoke SRAM macros from PDK (e.g., sky130) |
| OpenLaneでBlackBoxとして配置 | Integrate as black-box via OpenLane |
| キャッシュやバッファに階層配置 | Hierarchically embedded for cache or buffers |

---

## 🔁 他メモリとの比較｜Comparison with Other Memories

| 項目 | SRAM | DRAM | Flash |
|------|------|------|-------|
| 高速性<br>Speed | ◎ | ○ | × |
| 容量<br>Capacity | △ | ◎ | ◎ |
| 面積効率<br>Area Efficiency | △ | ◎ | ○ |
| 不揮発性<br>Non-volatility | × | × | ◎ |
| 組込み性<br>Embeddability | ◎ | △ | △ |

---

## 🧩 補足と応用｜Supplemental Info

- **構成のバリエーション**：8T, 10T, Dual-Port など用途に応じ多様化  
  Variants include 8T, 10T, dual-port designs depending on application.
- **微細化の課題**：FinFET/GAAではレイアウト困難  
  Scaling challenges arise with FinFET/GAA structures.
- **SNM設計重要**：読み出し破壊や書込失敗回避に必要  
  SNM tuning is critical to avoid read disturbance and write failure.

---

## 🔗 関連章｜Related Chapters

| 日本語 | English |
|--------|---------|
| [基礎編 第2章](../chapter2_comb_logic/)：レジスタ構造 | Basic Chapter 2: Register logic structures |
| [基礎編 第4章](../chapter4_mos_characteristics/)：MOS特性 | Basic Chapter 4: MOS characteristics |
| [応用編 第4章](../d_chapter4_layout_optimization/)：SRAM配置 | Applied Chapter 4: SRAM layout and DFM |

---

## 📦 技術アーカイブ（Edusemi-Plus）｜Technical Archive (Edusemi-Plus)

| ドキュメント | 概要（日本語） | Summary (English) |
|--------------|----------------|-------------------|
| [`DRAM_Startup_64M_1998.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in1998/DRAM_Startup_64M_1998.md) | 0.25μm世代64M DRAM立ち上げ記録 | 0.25μm 64M DRAM ramp-up history |
| [`VSRAM_2001.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/VSRAM_2001.md) | DRAM応用の擬似SRAM設計記録 | Pseudo SRAM based on DRAM process |
| [`MoSys_1T_SRAM_Links.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/MoSys_1T_SRAM_Links.md) | 1T-SRAM技術の参考リンク集 | Reference links for MoSys 1T-SRAM |

---

🏘 [応用編 第1章：メモリ技術｜Applied Chapter 1: Memory Technologies](../d_chapter1_memory_technologies/README.md)

---

© 2025 Shinichi Samizo / MIT License
