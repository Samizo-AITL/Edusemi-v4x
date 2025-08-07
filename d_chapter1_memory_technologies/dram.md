---
layout: default
title: DRAM（Dynamic Random Access Memory）
---

---

# 🧠 DRAM（Dynamic Random Access Memory）

---

## 📘 概要 | Overview

DRAM（Dynamic RAM）は、**1ビットあたり「1トランジスタ＋1キャパシタ（1T1C）」**で構成される揮発性メモリです。  
DRAM is a volatile memory composed of **one transistor and one capacitor (1T1C) per bit**.

高密度・低コストを実現できるため、PC・スマートフォン・組込み機器などの**外部メモリ（メインメモリ）**として広く採用されています。  
Its high density and low cost make it widely used as **external (main) memory** in PCs, smartphones, and embedded systems.

ただし、**キャパシタに蓄えた電荷は自然に失われる**ため、定期的に**リフレッシュ動作が必要**です。  
However, **the capacitor charge leaks over time**, so **refresh operations are required** periodically.

---

## 🔧 セル構造：1T1C DRAMセル | DRAM Cell Structure: 1T1C

```
WL（ワード線）
│
├──┐
│  ｜ アクセスFET（スイッチ）
▼  ●─────────┐
ゲート       ソース│
▼
┌────────┐
│ キャパシタ │ ← データを電荷で保持
└────────┘
▲
ビット線（BL）
```

### 🔍 要素の説明 | Description of Components

| 構成要素 | 説明 | Component | Description |
|----------|------|-----------|-------------|
| WL（Word Line） | アクセスFETのゲート制御（行選択） | Word Line (WL) | Gate control of access transistor (row select) |
| アクセスFET | 読み書きタイミングで開閉するスイッチ（1T） | Access FET | Switch turned on/off during read/write |
| キャパシタ | 電荷を蓄える記憶素子（論理1 or 0） | Capacitor | Stores charge representing 1 or 0 |
| BL（Bit Line） | 読み書きデータのやりとり（列選択） | Bit Line (BL) | Transfers data during read/write (column select) |

---

## ⏱ リフレッシュとタイミング | Refresh and Timing

| 項目 | 説明 | Item | Description |
|------|------|------|-------------|
| リフレッシュ | 通常64ms以内に全ビットを再書き込み | Refresh | All bits must be refreshed within ~64ms |
| RAS/CAS | 行/列アドレス制御信号 | RAS/CAS | Row/Column address strobe |
| プリチャージ | ビット線を中間電位に戻す処理 | Precharge | Resets BL voltage after access |
| バーストアクセス | 複数データ一括読み出し | Burst Access | Fast sequential reads |

---

## 📊 SRAMとの比較 | Comparison with SRAM

| 項目 | DRAM | SRAM | Item | DRAM | SRAM |
|------|------|------|------|------|------|
| 集積度 | ◎ | △ | Density | ◎ | △ |
| 面積効率 | ◎ | △ | Area Efficiency | ◎ | △ |
| 消費電力 | △（リフレッシュ） | ○（待機時小） | Power | △ (needs refresh) | ○ (low standby) |
| 速度 | △ | ◎ | Speed | △ | ◎ |
| 制御 | 外部コントローラ要 | マクロ内完結可 | Control | Needs controller | Embedded macro |

---

## 🧪 DRAMの種類 | Types of DRAM

| 種類 | 特徴 | 用途 | Type | Feature | Usage |
|------|------|------|------|---------|-------|
| SDRAM | クロック同期 | 組込み用途など | SDRAM | Clock-synced | Embedded use |
| DDR1-5 | 世代別高速化 | メインメモリ | DDR1–5 | Increasing speed | Main memory |
| LPDDR | 低消費電力 | モバイル | LPDDR | Low power | Mobile devices |
| eDRAM | SoC内蔵 | キャッシュ等 | eDRAM | Embedded in SoC | Cache, graphics |

---

## 🏗 SoCとの接続 | SoC Integration

- AXI/AHBバスで外部接続  
- リフレッシュ制御・バースト制御・スケジューリング  
- キャッシュ階層と連携し、待ち時間を隠蔽

Connected externally via AXI/AHB bus.  
Controlled by memory controller: refresh, burst, arbitration.  
Integrated with cache hierarchy to hide latency.

---

## 🔁 補足比較 | Supplementary Comparison

| 項目 | SRAM | DRAM | Item | SRAM | DRAM |
|------|------|------|------|------|------|
| セル構造 | 6T | 1T1C | Cell Structure | 6T | 1T1C |
| 安定性 | 非破壊読み出し | 読み出しで破壊 | Stability | Non-destructive | Destructive read |
| リフレッシュ | 不要 | 必要 | Refresh | Not required | Required |
| 動作原理 | ラッチ | 電荷保持 | Principle | Latch | Charge-based |
| 実装 | 組込み | 外付け or eDRAM | Integration | Embedded | External or embedded |

---

## 📚 関連リンク | Related Sections

- [sram.md](./sram.md)：SRAMとの比較 | Comparison with SRAM  
- [基礎編 第4章](../chapter4_mos_characteristics/)：MOSばらつき | MOS variation  
- [応用編 第6章](../d_chapter6_pdk_and_eda_environment/)：eDRAM制約 | eDRAM design constraints

---

## 📦 技術アーカイブ（Edusemi-Plus） | Archive References

- [`DRAM_Startup_64M_1998.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in1998/DRAM_Startup_64M_1998.md)：1998年DRAM立ち上げ | 64M DRAM ramp-up  
- [`VSRAM_2001.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/VSRAM_2001.md)：擬似SRAM開発 | pseudo-SRAM dev  
- [`MoSys_1T_SRAM_Links.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/MoSys_1T_SRAM_Links.md)：1T-SRAM参考リンク | 1T-SRAM links

---

🏘 [応用編 第1章：メモリ技術｜Applied Chapter 1: Memory Technologies](../d_chapter1_memory_technologies/README.md)

---

© 2025 Shinichi Samizo / MIT License
