---
layout: default
title: 0.18μm CMOS (1.8V/3.3V) + 1.8V FeFET Gate-Last Module
---

# 📋 0.18μm 多電圧ロジック + 1.8V FeFET（HfO₂/HZO）

**JP**：本ドキュメントは **1.8V/3.3V ロジック**に **1.8V動作の FeFET**（書換時は内部チャージポンプで ±2–3V パルス）を **Gate-Last**でモノリシック統合する工程を示す。  
**EN**: This document adds a **1.8 V FeFET** (program/erase via on-chip charge-pump ±2–3 V) on top of a **1.8 V/3.3 V logic** baseline using a **gate-last** monolithic integration.

---

## 🔌 電源ドメイン / Power Domains

| ドメイン | 用途 / Use | 名目電圧 | 備考 |
|---|---|---:|---|
| CORE | デジタル/周辺 | **1.8 V** | 標準薄膜ゲート |
| I/O  | 入出力 | **3.3 V** | 厚膜GOX/ルール分離（既存） |
| NVM  | FeFETセル | **1.8 V** | 書換は **±2–3 V**（内部昇圧） |

*FeFET は 1.8 V ドメインに配置、I/O 3.3 V は従来どおり。*

---

## 🧱 FEOL 要点 / FEOL Essentials

- **ゲート酸化（ロジック）**：LV≈35 Å / MV≈70 Å（G2/G3 のみ）。  
- **3.3 V I/O**：厚膜GOX + I/O デバイス（既存章を維持）。  
- **5 V/HV 系**：**全削除**（不要）。

---

## 🆕 9. FeFET Gate-Last Module (HfO₂/HZO)

**狙い / Purpose**：既存 FEOL/サリサイド完了後に **FeFET ゲートのみ置換**し、熱予算を守って強誘電 o-phase を得る。

### 9.1 プロセスフロー / Process Flow (FeFET Regions Only)

| No. | Mask | 工程 / Step | 分類 | 代表条件 / Typical |
|---:|---|---|---|---|
| 901 | FE-OPN | FeFETゲート開口（ILD 上） | Litho | KrF |
| 902 | — | ダミー Poly 除去 | Etch | HBr/Cl₂ RIE |
| 903 | — | 旧GOX リフレッシュ | Wet | ~0.5% HF, tens-s |
| 904 | FE-IL | 界面層 **Al₂O₃ 1–2 nm** | ALD | 200–250 ℃ |
| 905 | FE-HZO | **Hf₀․₅Zr₀․₅O₂ 8–12 nm** | ALD | 200–300 ℃ |
| 906 | FE-CAP | キャップ **Al₂O₃ 1–2 nm**（任意） | ALD | — |
| 907 | FE-TiN | **TiN 30–50 nm**（ゲート） | PVD/ALD | — |
| 908 | FE-GP | ゲートパターニング | Litho/RIE | KrF |
| 909 | FE-ANL | **結晶化 RTA 450–500 ℃, 30–60 s** | RTA | N₂ |
| 910 | FE-FGA | **Forming-Gas 350 ℃, 20–30 min** | Furnace | H₂/N₂ |
| 911 | FE-ISO | 充填/平坦化（HDP/TEOS + CMP） | Dielectric | — |

**Integration Notes**  
- **サリサイド先行**：S/D 側は先に完了。TiN 近傍の金属反応に注意。  
- **熱予算**：結晶化後は >500–600 ℃ を回避（以降BEOLは低温系）。  
- **電圧**：セル動作 1.8 V、P/E は内部昇圧 **±2–3 V** を短パルスで印加。  

### 9.2 書換/駆動ブロック / P/E Driver (Sketch)

- **Charge Pump**：Dickson/跨り式、目標 ±2.5 V @ 数百 µs 負荷。  
- **Clamp/Limiter**：セルストレス抑制（V\_GS, V\_GD 両端監視）。  
- **センス**：ヒステリシス読み出し（ΔV\_T or Id–Vg ウィンドウ）。

---

## 🧪 E-test テンプレ / Wafer-Level Templates

| Test | 条件例 | 合格目安 |
|---|---|---|
| Id–Vg 2方向 | 25 ℃, V\_DS=50 mV | 2 ループで安定ヒステリシス |
| P/E 耐性 | ±2.5 V, 1 µs–100 µs, **1k–10k** cycles | 窓幅劣化 <20% |
| 保持 | 85 ℃, 10³–10⁴ s 等価 | 窓幅 >70% 維持 |
| Wake-up | 10–100 軽サイクル | 初期ドリフト収束 |

---

## 📐 レイアウト/DRC メモ

- FeFET 窓の **密度・段差** ルール（CMP 島・ディッシング対策）。  
- TiN エッジの **モールド/オーバーエッチ** マージン。  
- I/O 3.3 V 区画との **ルール分離**（ゲート厚・間隔）。

---

## 📎 関連資料 / Related
- **FeFET Overview (HZO stack & reliability)** → `fefet_hzo_overview.md`  
- **E-test Scripts & CSV Templates** → `etests_fefet_templates.md`

[← 戻る / Back](../README.md)
