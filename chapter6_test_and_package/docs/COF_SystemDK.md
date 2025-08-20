---
title: "COF Packaging and System-Level Evaluation"
lang: ja-en
layout: default
---

---

# 📦 COF Packaging and System-Level Evaluation  
**COFパッケージングとシステムレベル評価**

---

## ⚠️ 本資料の前提 / Disclaimer

本資料は **COF (Chip on Film) 技術に関する一般的かつ教育的な解説**を目的として作成したものです。  
- 特定企業・製品固有のプロセス条件や設計仕様には触れていません。  
- 記載されている数値・フロー・試験内容は **公開情報や教育資料レベルの一般知識**に基づくものであり、実際の量産条件を示すものではありません。  
- 本資料は **教育・学習用途に限定**され、設計・製造に直接使用することは意図されていません。  

> This document is intended as a **general and educational overview of COF (Chip on Film) technology**.  
> - It does not disclose any company-specific processes or proprietary specifications.  
> - All numerical values, flows, and test descriptions are based on **public domain or educational-level knowledge**, not production parameters.  
> - The content is for **learning purposes only**, and is not intended for direct use in design or manufacturing.  

---

## 1. 🧩 COF基材製造 / COF Substrate Fabrication
- **FCCL基材**: 薄型Cu箔 (約8 µm) とポリイミドフィルムの積層  
- **加工**: ロールから短冊にスリット加工、搬送用スプロケットホール形成  
- **パターニング**: フォトリソ＋エッチングで微細配線形成  
- **保護膜**: ソルダーレジストで配線を被覆、パッドのみ開口  
- **パッド処理**: 直Auめっき（~0.5 µm）、Cu拡散は限定的  

---

## 2. ⚙️ COF IC実装 / COF IC Assembly
- **接合方式**: フリップチップAuバンプ接合  
- **補強**: アンダーフィル樹脂で充填し、機械的強度と絶縁性を確保  
- **デザインルール**: 特に異電位配線間には確実に樹脂が入り込むことを保証  
- **検証試験**: HTS/HAST/85-85によりシート抵抗やリーク安定性を確認  

---

## 3. 🔗 COFアクチュエータ実装 / COF–Actuator Assembly
- **COF端子 (Au) ⇔ アクチュエータ配線 (Au)** を **NCP (Non-Conductive Paste)** で接合  
- **導通機構**: Au–Au金属接触、NCPは空隙充填・補強・防湿に寄与  
- **実装ルール**  
  - Au表面の洗浄・活性化を必須  
  - Pad周囲にNCP逃げ領域を設計  
  - 信頼性試験（85/85, HAST, Thermal Cycle）で接触抵抗のドリフトを評価  

---

## 4. 🧪 接合方式の比較 / Bonding Methods

| 項目 / Item          | **NCP** | **ACP** | **ACF** |
|-----------------------|---------|---------|---------|
| 材料形態 / Form       | ペースト (非導電) | ペースト (導電粒子含) | フィルム (導電粒子含) |
| 導通機構 / Conduction | Au–Au直接接触 | 粒子が垂直方向で導通 | 粒子が垂直方向で導通 |
| 絶縁性 / Insulation   | 高い | 粒子分散に依存 | 粒子分散に依存 |
| 実装ピッチ / Pitch    | 超狭ピッチ対応 | 狭ピッチ対応 | 狭ピッチ対応 |
| リワーク性 / Rework   | 一部可能 | 困難 | 困難 |
| 主な応用 / Application| MEMS, Auバンプ | 小型モジュール, センサー | LCDドライバIC, FPC接続 |

---

## 5. 🔥 熱設計 / Thermal Design
- **COF基材の特徴**  
  - PI部分は熱伝導率が低く、隣接素子（例：アクチュエータ）への不要な熱流入を抑制  
  - 一方で、IC局所発熱の放熱は難しく、COF単体での熱拡散自由度は低い  
- **まとめ**  
  - COFの低熱伝導性は「利点（熱遮断）」と「制約（放熱性不足）」を併せ持つ  
  - 実際のシステムでは、基板・モジュール・筐体レベルで放熱パスを設計することが必須  

---

## 6. 📡 System評価 / System-Level Evaluation

### (1) COF単体評価  
- 開放/短絡検査 (Open/Short Test)  
- ICリーク測定 (Leak Current Measurement)  
- ファンクションテスト (Logic/Functionality Test)  
- 耐久試験: Heat Cycle  

### (2) COF + アクチュエータ実装評価  
- 開放/短絡検査  
- PZTセグメントのオープン/ショート検査  
- 耐久試験  
  - Heat Cycle  
  - **PZT耐久試験（例: 180億パルスで特性劣化5%以内）**  

### (3) ヘッドモジュール評価  
- 印字機能検査（Functional Printing Test）  
- 吐出特性試験（Jetting Characteristics Test）  
- 耐久試験  
  - Heat Cycle  
  - PZT耐久（パルス駆動による劣化確認）  
  - 吐出安定性試験（Jetting Stability over Long Duration）  

### (4) プリンタ機体実装評価  
- 印字品質検査（Print Quality Test）  
- 耐久試験  
  - 長時間運転試験（印字品質維持、搬送・駆動系の安定性確認）  
  - 環境試験（温湿度、振動、塵埃影響など）  
- EMC試験  
  - **COFがプリンタ全体に与える影響**  
  - **プリンタ環境がCOF挙動に与える影響**
  
---

## 7. 🧠 SystemDK視点まとめ / SystemDK Perspective
- COFは **基材 → IC実装 → アクチュエータ実装 → モジュール → システム** の階層構造で評価すべき  
- 熱・電気・信号・EMC特性が階層を超えて相互作用する  
- SystemDK的には、  
  **材料物性 → 実装信頼性 → 信号伝送特性 → EMI/EMC挙動**  
  を因果関係として把握することが重要  

---

## 8. 📚 学習課題例 / Learning Exercises
- **Q1.** COF基材の誘電率Dkが+0.5変化した場合、特性インピーダンス・EMC挙動にどう影響するか？  
- **Q2.** NCPとACFの接合方式を比較し、アクチュエータ実装に最適な方式を論じよ。  
- **Q3.** COFの低熱伝導率が「利点」と「制約」になる事例をそれぞれ挙げよ。  

---

## 🔗 関連章 / Linked Chapters
- [`f_chapter2_chiplet_pkg/`](../f_chapter2_chiplet_pkg/) — Chiplet & Package Basics  
- [`d_chapter5_analog_mixed_signal/`](../d_chapter5_analog_mixed_signal/) — AMS & Physical Constraints  
- [`f_chapter4_fsm_pid_llm/`](../f_chapter4_fsm_pid_llm/) — Control SoC PoC Integration  
- [`chapter6_test_and_package/6.4_packaging.md`](../chapter6_test_and_package/6.4_packaging.md) — Package Process Basics  
