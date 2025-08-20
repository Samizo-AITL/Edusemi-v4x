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
本資料は **COF (Chip on Film) に関する一般技術的な内容**を教育目的で整理したものであり、  
特定企業・製品固有の機密情報には触れていません。  
> This document summarizes **general COF packaging technology** for educational use.  
> It does not include confidential or company-specific data.

---

## 1. 🧩 基材と材料 / Substrate and Materials
- **FCCL基材**: 薄型銅箔（約 8 µm）＋ポリイミドフィルム  
- **加工**: ロールから短冊にスリット加工し、搬送用スプロケットホールを形成  
- **表面粗さ (Ra, Rz)**: 実装信頼性や導通に直結するため重要  

---

## 2. 🖌 パターニングと表面処理 / Patterning and Surface Treatment
- **配線形成**: フォトリソ＋エッチングで微細配線を形成  
- **保護膜**: 緑色ソルダーレジストを塗布し、パッドのみを開口  
- **パッド処理**: 直 Au めっき（約 0.5 µm）  
  - Ni バリアなしでも Cu 拡散影響は限定的  
  - 加速試験（HTS/HAST/85-85）でシート抵抗変化はほぼなし  

---

## 3. ⚙️ IC実装とアンダーフィル / IC Assembly and Underfill
- **方式**: フリップチップ実装（Au バンプ接合）  
- **補強**: アンダーフィル樹脂で機械的・絶縁的強化  
  - 異電位配線間は確実に樹脂を充填  
  - デザインルール: 「必ず樹脂が配線間に入り込む」ことを保証  

---

## 4. 📡 システム評価 / System Evaluation
- **実装階層**: COF単体 → ヘッドモジュール → プリンタ機体  
- **EMC評価**: 電波暗室で放射・伝導・感受性を評価  
- **知見**: 基材の誘電率 (Dk)、誘電正接 (Df)、吸湿特性が  
  **システム全体のEMI/EMC挙動に大きく影響**  

---

## 5. 🧪 NCP接合の適用例 / Example of NCP Bonding
- **用途**: アクチュエータの Au 配線と IC 接続  
- **導通機構**: Au–Au 金属接触、NCPは補強・空隙充填・防湿  
- **実装ルール**  
  - Au 表面の洗浄・活性化必須  
  - Pad 周囲に NCP 逃げ領域を設計  
  - 信頼性試験で接触抵抗ドリフトを監視  

---

## 6. 🔄 プロセスフロー / Process Flow

### 📜 概要フロー
```mermaid
flowchart TB
    A[FCCL基材準備 Cu 8um + PI] --> B[短冊化 スリット・外形]
    B --> C[スプロケットホール形成]
    C --> D[フォトリソ エッチング]
    D --> E[ソルダーレジスト形成]
    E --> F[Pad Auめっき 0.5um]
    F --> G[IC実装 Auバンプ]
    G --> H[アンダーフィル充填]
    H --> I[ヘッドモジュール化]
    I --> J[プリンタ機体に実装]
    J --> K[電波暗室でEMC評価]
    K --> L[設計フィードバック]
```

### 🔧 NCP接合フロー
```mermaid
flowchart TB
    A[Au配線面洗浄 活性化] --> B[NCP塗布 基板側]
    B --> C[高精度位置合わせ]
    C --> D[熱圧着 TC TS Au-Au接触 NCP硬化]
    D --> E[ポストキュア 外観・電気検査]
    E --> F[追加アンダーフィル 封止]
```

---

## 7. 📊 比較・検討事項 / Comparative Considerations

### Ni/Au vs 直Auめっき
- Ni/Au: 保存性高い、だがコスト増  
- 直Au: 実装性良、シート抵抗安定  

### ロール基材 vs 短冊基材
- ロール: 高スループット、搬送自動化  
- 短冊: 高精度、試作向き  

### アンダーフィル有無
- 有: 信頼性高い、絶縁性良  
- 無: 熱伝導改善、だがリークリスク  

---

## 8. 🔍 接合方式の比較 / Bonding Method Comparison

| 項目 / Item          | **NCP** (Non-Conductive Paste) | **ACP** (Anisotropic Conductive Paste) | **ACF** (Anisotropic Conductive Film) |
|-----------------------|--------------------------------|-----------------------------------------|---------------------------------------|
| 材料形態 / Form       | ペースト (液状)               | ペースト (液状, 導電粒子含む)           | フィルム状 (導電粒子含む)              |
| 導通機構 / Conduction | Au–Au直接接触                  | 粒子が垂直方向で局所導通                | 粒子が垂直方向で局所導通                |
| 絶縁性 / Insulation   | 高い                          | 粒子分散に依存                          | 粒子分散に依存                          |
| 実装ピッチ / Pitch    | 超狭ピッチ対応可               | 狭ピッチ対応可                           | 狭ピッチ対応可 (FPCで実績多)           |
| プロセス性 / Process  | 塗布 → 熱圧着                  | 塗布 → 熱圧着                            | ラミネーション → 熱圧着                |
| リワーク性 / Rework   | 一部可能                       | 困難                                    | 困難                                   |
| 応用例 / Application  | Auバンプ実装, MEMS             | 小型モジュール, センサー                 | LCDドライバIC, FPC接続                  |
| 特徴 / Notes          | 接触抵抗安定性が高い           | 粒子均一性課題                          | 量産性高い、実績豊富                   |

---

## 9. 🧠 SystemDK視点のまとめ / SystemDK Summary
- COF基材の変更は「**材料 → パッケージ → モジュール → システム**」へ波及  
- EMC評価は **フィードバックループ**として機能し、単なる材料選択を超える  
- SystemDK的には、  
  **材料物性 → 実装信頼性 → 信号伝送特性 → EMC挙動**  
  の因果連鎖を理解することが必須  

---

## 10. 📚 学習課題例 / Learning Exercises
- **Q1.** 基材の誘電率 Dk が 0.5 増加した場合、特性インピーダンスと EMC 特性にどう影響するか？  
- **Q2.** NCP接合と ACF接合の違いを整理し、アクチュエータ実装に最適な方式を説明せよ。  

---

## 11. 🔥 熱伝導と放熱性 / Thermal Conduction and Heat Dissipation

- **材料の限界 / Material Limits**  
  - PI基材の熱伝導率は **約 0.2 W/mK** と極めて低い  
  - 銅配線は高伝導性だが、幅・厚みが小さいため十分な放熱経路にはならない  

- **実装上の結果 / Practical Outcome**  
  - 駆動ICで発生した熱は **アクチュエータ側にはほとんど伝わらない**  
  - 主な熱流路は **IC背面 → 接着材 → モジュールフレーム** となる  

- **対策アプローチ / Design Approaches**  
  - IC背面に **放熱パッド / サーマルスプレッダ**を追加  
  - **モジュール筐体（金属フレーム）** に直接熱を逃がす設計  
  - **高熱伝導エポキシ**や **サーマルビア**を利用し、熱拡散を補助  

> 💡 COF単体での熱設計自由度は低い。  
> **SystemDK視点では「モジュール全体での放熱設計」が不可欠**。
