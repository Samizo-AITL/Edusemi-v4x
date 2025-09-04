---
layout: default
title: "1.6 統合メモリ：LPDDR＋FeRAMによるモバイルエッジAI"
---

---

# 1.6 統合メモリ：LPDDR＋FeRAMによるモバイルエッジAI  
*Hybrid Memory (LPDDR + FeRAM) for Mobile/Edge AI*  

---

## 📑 Table of Contents
- [1.6.1 概要 / Overview](#-161-概要--overview)
- [1.6.2 目標と制約 / Goals & Constraints](#-162-目標と制約--goals--constraints)
- [1.6.3 アーキテクチャ / Architecture ＋ プロセスノード対応](#-163-アーキテクチャ--architecture--プロセスノード対応)
- [1.6.4 動作シナリオ / Operation Scenarios](#-164-動作シナリオ--operation-scenarios)
- [1.6.5 実装方式 / Implementation Options](#-165-実装方式--implementation-options)
- [1.6.6 技術比較 / Technology Parameters](#-166-技術比較--technology-parameters)
- [1.6.7 システム効果 / System-Level Impact](#-167-システム効果--system-level-impact)
- [1.6.8 開発フロー / Development Flow](#-168-開発フロー--development-flow)
- [1.6.9 比較グラフ / Comparison Charts](#-169-比較グラフ--comparison-charts)
- [1.6.10 FEM解析 / FEM Analysis](#-1610-fem解析--fem-analysis)
- [1.6.11 時系列シーケンス / Sequence of Operations](#-1611-時系列シーケンス--sequence-of-operations)
- [1.6.12 応用ユースケース / Mobile Edge AI Use Cases](#-1612-応用ユースケース--mobile-edge-ai-use-cases)
- [1.6.13 広範な含意 / Broader Implications](#-1613-広範な含意--broader-implications)
- [1.6.14 将来展開 / Future Path](#-1614-将来展開--future-path)
- [1.6.15 関連文書 / References](#-1615-関連文書--references)

---

## 📌 1.6.1 概要 / Overview

現在、モバイルエッジAI向けの標準メインメモリは **LPDDR** である。  
我々は **FeRAM** をチップレットとして実装し、不揮発機能を付与することで、低待機電力と  
**インスタントレジューム（電源断後も状態を保持し、即時復帰できる機能）** を実現する。  
*In mobile edge AI, LPDDR is the dominant working memory. By adding FeRAM as a chiplet with non-volatility,  
we enable low standby power and instant resume.*  

この方式は **LPDDRの帯域効率を維持しつつ、チェックポイントやリフレッシュ抑制をFeRAMにオフロード**できるため、  
バランスの取れたハイブリッド構成を提供する。  
*This approach preserves LPDDR’s bandwidth efficiency while offloading checkpoints and refresh suppression to FeRAM,  
offering a balanced hybrid memory architecture.*  

---

## 🎯 1.6.2 目標と制約 / Goals & Constraints

| **項目** | **内容 (日本語)** | *Description (English)* |
|----------|------------------|-------------------------|
| **目標 / Goals** | 帯域効率維持・低待機電力・インスタントレジューム | *Maintain bandwidth efficiency, minimize standby power, enable instant resume* |
| **制約 / Constraints** | 実装面積・BOMコスト・FeRAM耐久性 | *Die area, BOM cost, FeRAM endurance* |

---

## 🏗️ 1.6.3 アーキテクチャ / Architecture ＋ プロセスノード対応

- **LPDDR** = メインワーキングメモリ  
  *LPDDR = main working memory*  

- **FeRAM** = チェックポイント／OS状態／Cold領域の不揮発層  
  *FeRAM = persistent tier for checkpoints, OS state, and cold data*  

- **統合** = チップレット／SiP統合＋SystemDK制御  
  *Integration = chiplet/SiP packaging with SystemDK supervision*  

```mermaid
flowchart TD
  CPU["🖥️ CPU / Accelerator (5–3nm FinFET/GAAFET)"]
  LPDDR["📗 LPDDR: working memory (14–10nm DRAM nodes)"]
  NV["💾 FeRAM: persistent tier (22–28nm CMOS)"]

  CPU --> LPDDR
  LPDDR <---> NV
  note1{SystemDK<br/>checkpoint / refresh offload}
  NV -.-> note1
  LPDDR -.-> note1
```

### 🔬 プロセスノード対応 / Process Node Mapping

| **対象 / Target** | **ノード (日本語)** | *Process Node (English)* | **備考 / Notes** |
|-------------------|---------------------|--------------------------|------------------|
| **SoC ロジック** | 5〜3nm FinFET/GAAFET | *5–3nm FinFET/GAAFET* | モバイル/エッジSoC世代 |
| **LPDDR** | 1α〜1γ世代 (14〜10nm DRAM) | *1α–1γ DRAM nodes (14–10nm)* | LPDDR5/5X対応 |
| **FeRAM** | 22〜28nm CMOS | *22–28nm CMOS nodes* | MCU/IoTで量産済、チップレット実装が現実的 |
| **将来FeFET** | <10nm CMOS互換 | *sub-10nm CMOS compatible* | Monolithic統合シナリオ |

---

## 🔄 1.6.4 動作シナリオ / Operation Scenarios

| **フェーズ** | **日本語説明** | *English Description* |
|--------------|----------------|-----------------------|
| **推論時 / Inference** | LPDDR がアクティブに動作し、FeRAM がバックグラウンドでチェックポイント保存 | *LPDDR active, FeRAM stores checkpoints in background* |
| **スリープ時 / Sleep** | LPDDR 内容を消去、FeRAM が不揮発的に状態を保持 | *LPDDR cleared, FeRAM retains OS/application state* |
| **復帰時 / Resume** | FeRAM から状態をロード → 即時レジューム | *Reload from FeRAM enables instant resume* |

---

## 🏗️ 1.6.5 実装方式 / Implementation Options

| **方式** | **日本語説明** | *English Description* |
|----------|----------------|-----------------------|
| **Chiplet/SiP 統合** | LPDDRとFeRAMを2.5D/3D技術で統合。SystemDKで制御 | *Chiplet/SiP integration with SystemDK supervision* |
| **Monolithic困難性** | LPDDRは >700°C 高温アニール必須、FeRAMは 350–450°C で安定化。プロセス温度不一致 | *LPDDR requires >700°C anneal, FeRAM stabilizes at 350–450°C → process mismatch* |

---

## 📊 1.6.6 技術比較 / Technology Parameters

| **項目** | **LPDDR (typ.)** | **FeRAM (typ.)** |
|----------|------------------|------------------|
| **アクセス遅延 / Access latency** | 15–60 ns | 80–150 ns |
| **保持特性 / Retention** | 揮発性 (32–64 ms) | 不揮発 (10⁷–10⁸ s ≈ years) |
| **書込みエネルギー / Write energy** | 中程度 | 低い |
| **耐久性 / Endurance** | >10¹⁶ アクセス | 10¹⁰–10¹² 書込み |
| **プロセス温度 / Process temp.** | >700 °C | 350–450 °C |
| **役割 / Role** | メインメモリ | チェックポイント／状態保持 |

---

## ⚡ 1.6.7 システム効果 / System-Level Impact

| **指標** | **LPDDRのみ** | **LPDDR+FeRAM** |
|----------|----------------|-----------------|
| **スタンバイ電力 / Standby power** | 100% | 80–90% (10–20%削減) |
| **レジューム遅延 / Resume latency** | ms オーダー | 100–500 µs |
| **効率 / Effective energy efficiency** | 1.0× | 1.15–1.25× |

---

## 🛠️ 1.6.8 開発フロー / Development Flow

| **工程 / Step** | **内容 (日本語)** | *Description (English)* |
|-----------------|------------------|-------------------------|
| **CPU仕様策定 / CPU Specification** | アプリ要件に基づき演算性能・低消費電力・メモリ帯域を定義 | *Define compute, power, and memory requirements* |
| **モジュール選定 / Module Selection** | LPDDR・FeRAM容量・インタフェースを決定 | *Select LPDDR, FeRAM, interfaces* |
| **FPGA設計検証 / FPGA Prototype** | FPGA上でプロトタイプ構築・FeRAM連携検証 | *Prototype on FPGA, verify FeRAM integration* |
| **RTL設計 / RTL Design** | メモリコントローラ・チェックポイント制御をRTL化 | *Implement memory controller & checkpoint logic* |
| **物理設計検証 / Physical Design** | 配線遅延・電力・面積を解析 | *Verify layout timing, power, area* |
| **GDS / GDSII** | マスクデータ生成 | *Generate GDSII mask layout* |
| **IC製造 / Fabrication** | CMOS＋NVMプロセスでチップ製造 | *Fabricate IC with CMOS + NVM* |
| **ウエハテスト / Wafer Test** | BIST・プローブカードで特性確認 | *Wafer-level test with probe cards* |
| **BR/IPDK・PKGDK** | プロセス・パッケージ設計キットで実装最適化 | *Optimize design using BR/IPDK, PKGDK* |
| **SystemDK** | アーキテクチャ／パッケージ／OSの協調制御 | *System-level co-design with SystemDK* |

```mermaid
flowchart TD
  SPEC["📝 CPU仕様策定"]
  MOD["📦 モジュール選定<br/>(LPDDR, FeRAM)"]
  FPGA["🔧 FPGA設計検証"]
  RTL["💻 RTL設計"]
  PHY["📐 物理設計検証"]
  GDS["📂 GDSII"]
  FAB["🏭 IC製造"]
  WAF["🔬 ウエハテスト"]
  PKG["📦 BR/IPDK・PKGDK"]
  SYS["🧩 SystemDK"]

  SPEC --> MOD --> FPGA --> RTL --> PHY --> GDS --> FAB --> WAF --> PKG --> SYS
```

---

## 📈 1.6.9 比較グラフ / Comparison Charts

**スタンバイ電力 / Standby Power**  
*Normalized (LPDDR only = 100). Lower is better.*  

![Standby Power](./fig_lpddr_feram_standby_power.png)

**レジューム遅延 / Resume Latency**  
*Milliseconds. Lower is better.*  

![Resume Latency](./fig_lpddr_feram_resume_latency.png)

> 備考 / Notes: グラフは本章の代表値（10–20%低減、100–500 µs クラスの復帰）を視覚化した概略値です。*Illustrative values consistent with chapter figures.*

---

## 🔍 1.6.10 FEM解析 / FEM Analysis

| **解析領域 / Domain** | **内容 (日本語)** | *Description (English)* |
|-----------------------|------------------|-------------------------|
| **熱解析 / Thermal** | LPDDRとFeRAMの発熱分布をシミュレーションし、冷却設計を最適化 | *Simulate heat distribution and optimize cooling* |
| **応力解析 / Mechanical Stress** | TSV・バンプ・接着層での応力集中を評価し、パッケージ信頼性を確認 | *Evaluate stress at TSVs, bumps, adhesives for reliability* |
| **電磁界解析 / EM Field** | LPDDR高速I/OとFeRAM制御配線のクロストーク、SI/PIを検証 | *Verify crosstalk, SI/PI, EMI between LPDDR and FeRAM interconnects* |

```mermaid
flowchart LR
  THERM["🌡️ Thermal Analysis"] --> RESULT1["最適冷却設計<br/>Optimized cooling"]
  STRESS["🔧 Stress Analysis"] --> RESULT2["高信頼パッケージ<br/>Reliable packaging"]
  EM["📡 EM Field Analysis"] --> RESULT3["SI/PI・EMI対策<br/>Signal & Power Integrity"]

  RESULT1 --> SYS
  RESULT2 --> SYS
  RESULT3 --> SYS
```
### 1.6.10 🔍 FEM解析 / FEM Analysis

本節では **熱解析 / Thermal**, **応力解析 / Mechanical Stress**, **電磁界解析 / EM Field** の3観点で  
LPDDR + FeRAM チップレット統合時の設計検証フローを示す。/  
This section describes FEM workflows for Thermal, Mechanical Stress, and EM Field in LPDDR + FeRAM chiplet integration.

#### 1.6.10.0 共通前提 / Common Assumptions
- プロセス・パッケージ：LPDDR（PoP相当）＋ FeRAM チップレット（インターポーザ or UBM経由）  
- 代表ケース：ピーク帯域動作、チェックポイント・オフロード時のBurst、低電力Standby  
- モデル粒度：ダイ（熱は粗メッシュ→詳細局所化）、TSV/バンプ近傍は細分化  
- 代表方程式 / Governing Eqs  
  - Heat: \\(\partial T/\partial t = \alpha \nabla^2 T + q/(\rho c)\\)  
  - Stress: \\(\nabla \cdot \boldsymbol{\sigma} + \mathbf{f} = 0,\ \boldsymbol{\sigma} = \mathbf{C}:\boldsymbol{\varepsilon}\\)  
  - EM: \\(\nabla \times \mathbf{H} = \mathbf{J} + \partial \mathbf{D}/\partial t,\ \nabla \times \mathbf{E} = -\partial \mathbf{B}/\partial t\\)

---

#### 1.6.10.1 熱解析 / Thermal Analysis
**目的 / Objective**  
- LPDDR・FeRAMの同時発熱時における温度分布、ホットスポット、冷却設計の最適化  
**代表入力 / Inputs**  
- 消費電力マップ（LPDDR: アクティブ/スタンバイ、FeRAM: 書込パルス時）  
- パッケージ/ヒートスプレッダ/ヒートシンク/TIMの熱パラメータ（k, ρ, c, Rθ）  
- 環境境界条件（自然/強制対流、放射）  
**評価指標 / Metrics**  
- 最高温度 \\(T_{max}\\)、温度勾配 \\(|\nabla T|\\)、熱時定数、Rθ_jc・Rθ_ja  
**合否の目安 / Pass-Fail**  
- \\(T_{max} < T_{spec}\\)、勾配が応力閾値を誘発しないこと

**結果例 / Example**  
![Thermal](assets/img/ch1/fig_1_6_fem_thermal_example.png)  
*温度分布の一例（ダミー図）。ホットスポットとスプレッダ効果の比較に使用。*

---

#### 1.6.10.2 応力解析 / Mechanical Stress
**目的 / Objective**  
- TSV/バンプ/接着層界面の応力集中、サーマルサイクル信頼性、はんだクラック起点の特定  
**代表入力 / Inputs**  
- CTE・ヤング率・ポアソン比、接着層の粘弾性モデル  
- 熱サイクル条件（JEDEC相当）と実動作温度プロファイル  
- 幾何（TSV径/ピッチ、UBM厚、Underfill有無）  
**評価指標 / Metrics**  
- 等価ミーゼス応力、界面せん断、塑性ひずみ蓄積、ΔCTE起因の損傷指標  
**合否の目安 / Pass-Fail**  
- クリティカル界面での安全率 > 規定値、塑性累積 < 閾値

**結果例 / Example**  
![Stress](assets/img/ch1/fig_1_6_fem_stress_example.png)  
*TSV周りの応力コンター（ダミー図）。半径方向の集中と界面付近のピークを可視化。*

---

#### 1.6.10.3 電磁界解析 / EM Field (SI/PI/EMI)
**目的 / Objective**  
- LPDDR高速I/O と FeRAM制御パルスの**相互干渉**（クロストーク）および電源インテグリティを確認  
**代表入力 / Inputs**  
- パッケージ/基板配線幾何、誘電率/損失、PDNスタック（デカップ値・配置）  
- ドライバ/レシーバモデル（IBIS/Spice）、アクティビティパターン  
**評価指標 / Metrics**  
- 波形オーバー/アンダーシュート、ジッタ、アイ開口、Sパラメータ、PDNインピーダンスピーク  
**合否の目安 / Pass-Fail**  
- 受信閾値マージン確保、EMI規格内、PDN Z(ω) ピーク < 目標

**結果例 / Example**  
![EM](assets/img/ch1/fig_1_6_fem_em_example.png)  
*隣接配線のクロストーク波形（ダミー図）。アグレッサとビクティムの振る舞い比較。*

---

#### 1.6.10.4 ワークフロー / Workflow
```mermaid
flowchart LR
  PWR[消費電力プロファイル] --> TH(Thermal Solve)
  PKG[幾何・材料] --> TH
  TH --> ST(Stress Solve)
  TH --> EM(EM/SI-PI Solve)
  ST --> SYS[Reliability Margin]
  EM --> SYS
  TH --> SYS
```

---

## 🧭 1.6.11 時系列シーケンス / Sequence of Operations

*Power state transitions with checkpoint offload and instant resume.*

```mermaid
sequenceDiagram
    autonumber
    participant App as 🧠 App/AI Runtime
    participant OS as 🧩 OS / SystemDK
    participant DRAM as 📗 LPDDR (volatile)
    participant NVM as 💾 FeRAM (non-volatile)

    Note over App,OS: 推論中 / Inference
    App->>DRAM: Read/Write activations & weights
    OS-->>NVM: Background checkpoint (periodic)

    Note over OS,NVM: スリープ移行 / Enter Sleep
    OS->>NVM: Final checkpoint (OS state, app state)
    OS->>DRAM: Quiesce & flush working set
    OS->>DRAM: Power-down / self-refresh minimization
    DRAM-->>OS: Acknowledge

    Note over OS,NVM: 復帰 / Resume
    OS->>NVM: Restore OS/app state
    OS->>DRAM: Rapid re-init
    App->>DRAM: Resume execution (instant)
```

---

## 📱 1.6.12 応用ユースケース / Mobile Edge AI Use Cases

- 🔋 **On-device inference**: アイドル時のスタンバイ電力削減  
  *Reduce standby energy during idle periods*  

- 🔄 **Federated / continual learning**: 頻繁なモデル更新のチェックポイントをFeRAMに退避  
  *Enable frequent model update checkpoints without DRAM refresh overhead*  

- 🎮 **Interactive AR/VR & Sensor Fusion**: サブms復帰でUX改善  
  *Support instant resume for AR/VR and sensor fusion*  

---

## 🌐 1.6.13 広範な含意 / Broader Implications

- ✅ **DRAMを主メモリとして維持**しつつ、FeRAMを補助層として導入  
- 📏 **小容量FeRAM**（数MB〜数十MB）で十分効果を発揮  
- 🛠️ **SystemDKによる協調最適化**: アーキテクチャ・パッケージ・OSを統合制御  

---

## 🚀 1.6.14 将来展開 / Future Path

将来の高帯域用途では **HBM＋FeFET** への置換が可能である。  
ただし、現行のモバイルSoC設計においては **LPDDR＋FeRAM** がより現実的かつ低コストであり、  
実装性と効率のバランスが取れている。  
*For future high-bandwidth use cases, HBM + FeFET can replace this scheme.  
However, in today’s mobile SoC designs, LPDDR + FeRAM offers a more practical and cost-efficient balance.*  

---

## 📄 1.6.15 関連文書 / References

👉 [📄 LPDDR+FeRAM Chiplet Integration (PDF)](./LPDDR_FeRAM.pdf)  
👉 [📄 HBM+FeRAM Chiplet Integration (PDF)](./HBM_FeRAM_Chiplet_MobileEdgeAI.pdf)  
