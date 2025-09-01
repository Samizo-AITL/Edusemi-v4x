---
layout: default
title: 0.18μm CMOS (1.8V/3.3V) + 1.8V FeFET Gate-Last Module
---

---

# 📋 0.18μm 多電圧ロジック + 1.8V FeFET（HfO₂/HZO）

**日本語**：本ドキュメントは **1.8V/3.3V CMOSロジック**に、**1.8V動作の FeFET** を **Gate-Last方式**でモノリシック統合する戦略を示す。FeFETは大容量化を狙わず、**SRAMマクロの補助NVM用途**に限定する。応用対象は **車載ECU** や **産業IoTノード**。  
*English*: This document describes the **monolithic integration of a 1.8 V FeFET** on a **1.8 V/3.3 V CMOS logic** baseline using a **gate-last** approach. FeFETs are used not for large arrays but as **auxiliary NVM to support SRAM macros**, targeting **automotive ECUs** and **industrial IoT nodes**.

---

## 🔌 電源ドメイン / Power Domains

| ドメイン | 用途 | 電圧 | 備考 |
|----------|------|------|------|
| CORE | デジタル / 周辺回路 | **1.8 V** | 標準薄膜ゲート |
| I/O  | 入出力 | **3.3 V** | 厚膜酸化膜（従来通り） |
| SRAM | 揮発性メモリ | **1.8 V** | 主メモリマクロ |
| NVM  | FeFET補助セル | **1.8 V** | 書換は **±2–3 V**（内部昇圧）、容量は小規模補助 |

**日本語**：FeFETはSRAMを補完する補助メモリとして使用し、大容量化は目指さない。  
*English*: FeFETs serve as auxiliary NVM supporting SRAM, without aiming for large-capacity scaling.

---

## 🧱 FEOL 要点 / FEOL Essentials

- **日本語**：ゲート酸化膜（ロジック）は LV≈35 Å / MV≈70 Å（G2/G3 のみ）。  
  *English*: Logic gate oxide: LV ≈ 35 Å / MV ≈ 70 Å (using G2/G3 only).  

- **日本語**：3.3 V I/O は厚膜酸化膜をそのまま維持。  
  *English*: 3.3 V I/O devices retain thick oxide.  

- **日本語**：5 V/HV デバイスは不要のため削除。  
  *English*: 5 V / HV devices are removed.  

---

## 🆕 9. FeFET Gate-Last Module (HfO₂/HZO)

**日本語**：既存 FEOL およびサリサイド工程完了後にFeFET領域のダミーゲートを置換し、熱予算を守って強誘電相を誘起する。TiN電極は **既存スパッタ（ロングスロー / コリメータ）装置で対応可能**。  
*English*: After FEOL and salicide, dummy gates in FeFET regions are replaced to induce the ferroelectric phase under the thermal budget. TiN electrodes can be deposited using **existing sputter tools with long-throw or collimator configuration**.

### 9.1 プロセスフロー / Process Flow (FeFET領域)

| No. | マスク | 工程 | 分類 | 代表条件 |
|----:|--------|------|------|----------|
| 901 | FE-OPN | FeFETゲート開口（ILD上） | Litho | KrF |
| 902 | —      | ダミーポリ除去 | Etch | HBr/Cl₂ RIE |
| 903 | —      | 旧GOXリフレッシュ | Wet | ~0.5% HF |
| 904 | FE-IL  | 界面層 **Al₂O₃ 1–2 nm** | ALD | 200–250 ℃ |
| 905 | FE-HZO | **Hf₀․₅Zr₀․₅O₂ 8–12 nm** | ALD | 200–300 ℃ |
| 906 | FE-CAP | キャップ **Al₂O₃ 1–2 nm**（任意） | ALD | — |
| 907 | FE-TiN | **TiN 30–50 nm**（ゲート） | **PVD（ロングスロー/コリメータ対応） or ALD** | — |
| 908 | FE-GP  | ゲートパターニング | Litho/RIE | KrF |
| 909 | FE-ANL | **結晶化 RTA 450–500 ℃, 30–60 s** | RTA | N₂ |
| 910 | FE-FGA | **Forming Gas 350 ℃, 20–30 min** | Furnace | H₂/N₂ |
| 911 | FE-ISO | 充填・平坦化 | HDP/TEOS + CMP | — |

---

## 🧪 E-test テンプレート / Wafer-Level Templates

| テスト | 条件 | 合格基準 |
|--------|------|----------|
| Id–Vg 特性 | 25 ℃, V_DS=50 mV | 安定したヒステリシス（2ループ） |
| P/E 耐性 | ±2.5 V, 1–100 µs, 1k–10k cycles | 窓幅劣化 <20% |
| 保持 | 85 ℃, 10³–10⁴ s 等価 | 窓幅維持率 >70% |
| Wake-up | 10–100 軽サイクル | 初期ドリフト収束 |

---

## ⚠️ 信頼性課題 / Reliability Challenges

- **Endurance**  
  **日本語**：書換寿命は 10⁴〜10⁵ サイクル程度で、SRAM/DRAMに比べて制約が大きい。  
  *English*: Endurance is typically 10⁴–10⁵ cycles, limited compared to SRAM/DRAM.  

- **TDDB（絶縁破壊）**  
  **日本語**：酸素空孔由来のリークパスにより寿命短縮の懸念がある。  
  *English*: TDDB lifetime is limited due to oxygen-vacancy induced leakage paths.  

- **Retention / Wake-up**  
  **日本語**：初期サイクルでの窓幅変動（Wake-up）や高温保持での劣化が課題。  
  *English*: Window shift during early cycles (wake-up) and high-temperature retention remain issues.  

### 戦略的割り切り / Strategic Approach
**日本語**：これらの課題から、大容量メモリを目指さず **SRAM補助NVM（Instant-On / 設定保持 / セキュアキー保存）** に特化することで、実用性と歩留まりの両立が可能となる。  
*English*: Due to these limitations, the strategy is not to target large-capacity memory, but to focus on **auxiliary NVM for SRAM backup, instant-on, configuration storage, and secure key retention**, achieving practical usability and yield benefits.

---

## 🎯 戦略ポイント / Strategic Notes

- **日本語**：老朽化した 0.18 µm CMOS ラインを活用し、**最小限の追加投資（ALD導入）**で新しい補助NVM（FeFET）を統合できる。  
  *English*: Legacy 0.18 µm CMOS lines can be revitalized by **minimal additional investment (ALD introduction)**, enabling integration of new auxiliary NVM (FeFET).  

- **日本語**：ALD導入とTiNスパッタの流用により、既存設備を生かしたプロセス実装が可能。  
  *English*: FeFET integration is feasible by adding ALD and reusing existing TiN sputter tools.  

- **日本語**：FeFETは補助的用途に限定し、大容量化は狙わない。  
  *English*: FeFET is restricted to auxiliary use only, without pursuing large memory arrays.  

- **日本語**：応用分野は **車載ECU、産業IoT、Instant-Onノード、セキュアキー保持**。  
  *English*: Target domains include **automotive ECUs, industrial IoT, instant-on nodes, and secure key storage**.  

---

## 📎 関連資料 / Related
- **FeFET Overview (HZO stack & reliability)** → `fefet_hzo_overview.md`  
- **E-test Scripts & CSV Templates** → `etests_fefet_templates.md`

[← 戻る / Back](../README.md)
