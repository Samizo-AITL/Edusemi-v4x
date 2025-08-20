---
title: "COF Packaging and System-Level Evaluation"
lang: ja-en
layout: default
---

# 📦 COF Packaging and System-Level Evaluation  
**COFパッケージングとシステムレベル評価**

---

## ⚠️ 本資料の前提 / Disclaimer
本資料は **COF (Chip on Film) に関する一般技術的内容**を教育目的で整理したものであり、  
特定企業や製品固有の機密情報には触れていません。  

> This document summarizes **general COF packaging technology** for educational use,  
> and does not include confidential or company-specific data.

---

## 1. 🏭 COF基材製造 / COF Substrate Fabrication
- **基材構成 / Substrate Structure**  
  - FCCL (Flexible Copper Clad Laminate)  
  - 銅箔: 約 8 µm / Cu foil: ~8 µm  
  - ポリイミド (PI): 20–50 µm / Polyimide (PI): 20–50 µm  

- **加工プロセス / Process**  
  - ロールから短冊にスリット加工 / Slitting roll FCCL into strips  
  - 搬送用スプロケットホール形成 / Punching sprocket holes  
  - フォトリソ＋エッチングで配線形成 / Circuit patterning via photolithography & etching  
  - ソルダーレジスト塗布、Padのみ開口 / Solder resist coating with pad openings  
  - Pad直Auめっき（約0.5 µm） / Direct Au plating (~0.5 µm)  

- **設計要点 / Design Notes**  
  - 表面粗さ (Ra, Rz) は導通信頼性に直結 / Surface roughness critical for reliability  
  - Ni/Au構造は保存性向上だがコスト増 / Ni/Au improves stability but adds cost  

---

## 2. ⚙️ COF IC実装 / IC Assembly on COF
- **接合方式 / Bonding Method**  
  - フリップチップ実装 / Flip-chip bonding  
  - IC側 Auバンプ ⇔ COF側 Auパッド / IC Au bumps ⇔ COF Au pads  

- **補強 / Reinforcement**  
  - アンダーフィル樹脂で機械的・絶縁強化 / Underfill resin for mechanical & insulation reliability  
  - 異電位配線間には確実に樹脂充填 / Ensure resin fills between different potentials  

- **リスク管理 / Risk Control**  
  - ボイドや樹脂不足はショートリスク / Voids or resin shortage may cause shorts  
  - 熱サイクル試験で界面クラック監視 / Interface cracks checked by thermal cycle tests  

---

## 3. 🔗 COF アクチュエータ実装 / Actuator Connection
- **接続対象 / Target Connection**  
  - COF端子 Au ⇔ アクチュエータ配線 Au / COF pad Au ⇔ Actuator wiring Au  

- **接合方式 / Bonding Method**  
  - NCP (Non-Conductive Paste) による Au–Au接合 / Au–Au bonding with NCP  
  - NCPは補強・空隙充填・防湿を担う / NCP provides reinforcement, void filling, moisture barrier  

- **実装ルール / Assembly Rules**  
  - Au表面の洗浄・活性化必須 / Au surface cleaning & activation mandatory  
  - Pad周囲にNCP逃げ領域設計 / Provide NCP escape areas around pads  
  - 信頼性試験で接触抵抗変化を監視 / Monitor resistance drift in reliability tests  

---

## 4. 🧪 接合方式の比較 / Bonding Methods Comparison
| 項目 / Item          | **NCP** (Non-Conductive Paste) | **ACP** (Anisotropic Conductive Paste) | **ACF** (Anisotropic Conductive Film) |
|-----------------------|--------------------------------|-----------------------------------------|---------------------------------------|
| 材料形態 / Form       | ペースト (液状) / Paste (liquid) | ペースト (導電粒子含) / Paste (w/ conductive particles) | フィルム / Film (w/ conductive particles) |
| 導通機構 / Conduction | Au–Au直接接触 / Direct Au–Au contact | 粒子による垂直局所導通 / Vertical conduction via particles | 粒子による垂直局所導通 / Vertical conduction via particles |
| 絶縁性 / Insulation   | 高い / High                  | 粒子分散に依存 / Depends on dispersion | 粒子分散に依存 / Depends on dispersion |
| 実装ピッチ / Pitch    | 超狭ピッチ対応 / Ultra-fine pitch | 狭ピッチ対応 / Fine pitch capable       | 狭ピッチ対応 / Fine pitch capable      |
| プロセス性 / Process  | 塗布 → 熱圧着 / Dispense → Thermocompression | 塗布 → 熱圧着 / Dispense → Thermocompression | ラミネート → 熱圧着 / Laminate → Thermocompression |
| リワーク性 / Rework   | 一部可能 / Partially possible | 困難 / Difficult                       | 困難 / Difficult                       |
| 応用例 / Application  | Auバンプ, MEMS / Au bump, MEMS | 小型モジュール / Small modules         | LCDドライバ, FPC / LCD drivers, FPC   |

---

## 5. 🔥 熱設計 / Thermal Considerations
- **PI基材の熱特性 / PI Thermal Properties**  
  - 低熱伝導率 (~0.2 W/mK) → 熱クロストーク低減 / Low thermal conductivity reduces crosstalk  
  - Cu配線以外は放熱パスになりにくい / Poor heat spreading except via Cu traces  

- **利点 / Advantages**  
  - 隣接素子への熱流入を抑制 / Suppresses heat flow to neighboring devices  
  - 温度安定性に寄与 / Contributes to stability  

- **課題 / Challenges**  
  - IC発熱拡散が困難 / Difficult to dissipate IC heat  
  - COF単体での熱設計自由度が小さい / Limited thermal design freedom at COF level  

- **対応策（システム設計） / System-Level Solutions**  
  - モジュール側でヒートスプレッダ利用 / Heat spreaders at module level  
  - 実装基板で熱パス設計 / Thermal paths via mounting substrate  

---

## 6. 📡 System評価 / System-Level Evaluation
- **評価階層 / Evaluation Levels**  
  1. COF単体 / COF itself  
  2. モジュール（ヘッドなど）/ Module (head or subsystem)  
  3. システム全体（機体）/ Whole system  

- **EMC評価 / EMC Evaluation**  
  - 電波暗室で放射・伝導・感受性を確認 / Radiation, conduction, immunity in anechoic chamber  
  - 誘電率 Dk・誘電正接 Df・吸湿性が影響大 / Dk, Df, moisture absorption strongly affect EMC  

- **SystemDK視点 / SystemDK Perspective**  
  - 材料 → パッケージ → モジュール → システム / Material → Package → Module → System  
  - 物性変化が信号伝送・EMCに直結 / Material property change directly affects EMC  
  - 評価は設計フィードバックループとして機能 / Evaluation works as design feedback loop  

---

## 📚 学習課題例 / Learning Exercises
- **Q1.** COF基材の誘電率 Dk が +0.5 変化した場合、特性インピーダンスとEMC特性はどう変化するか？  
> If the dielectric constant Dk of the COF substrate increases by +0.5, how will characteristic impedance and EMC behavior change?  

- **Q2.** IC ⇔ COF ⇔ アクチュエータ接続で、NCPとACFを比較し、長期信頼性の観点から適性を論ぜよ。  
> Compare NCP and ACF in IC ⇔ COF ⇔ actuator connection, and discuss suitability in terms of long-term reliability.  

- **Q3.** COF基材の低熱伝導率が「利点」と「制約」になる事例を挙げよ。  
> Give examples where low thermal conductivity of COF substrate is both an advantage and a limitation.  

---

## 🔗 関連章 / Linked Chapters
- [`f_chapter2_chiplet_pkg/`](../f_chapter2_chiplet_pkg/) — Chiplet & Package Basics  
- [`d_chapter5_analog_mixed_signal/`](../d_chapter5_analog_mixed_signal/) — AMS & Physical Constraints  
- [`f_chapter4_fsm_pid_llm/`](../f_chapter4_fsm_pid_llm/) — Control SoC PoC Integration  
- [`chapter6_test_and_package/6.4_packaging.md`](../chapter6_test_and_package/6.4_packaging.md) — Package Process Basics
