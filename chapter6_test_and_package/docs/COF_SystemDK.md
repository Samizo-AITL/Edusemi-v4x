---
title: "COF Packaging and System-Level Evaluation"
lang: ja-en
layout: default
---

# COF Packaging and System-Level Evaluation  
# COFパッケージングとシステムレベル評価

## 1. 基材と材料 / Substrate and Materials
- 薄型銅箔（約 8 µm）＋ポリイミドフィルムによるフレキシブル基材 (FCCL)  
- ロールから短冊に加工し、搬送用のスプロケットホールを形成  
- Cu 表面粗さ (Ra, Rz) は実装信頼性と導通に直結  

## 2. パターニングと表面処理 / Patterning and Surface Treatment
- フォトリソ＋エッチングにより微細配線を形成  
- 緑色ソルダーレジストで配線を保護し、実装パッドのみを開口  
- PAD 表面は直 Au めっき（約 0.5 µm）で酸化防止と実装性を確保  
  - Ni バリアなしでも Cu 拡散の影響は限定的  
  - 加速試験でシート抵抗変化はほぼなし  

## 3. IC実装とアンダーフィル / IC Assembly and Underfill
- **フリップチップ実装**（Au バンプ接合）を基本方式とする  
- アンダーフィル樹脂で補強  
  - 特に異電位配線間は確実に樹脂を充填し、リーク防止  
  - 配線間デザインルールとして「必ず樹脂が入り込む」ことを保証  

## 4. システム評価 / System Evaluation
- COF単体ではなく、**ヘッドモジュールに実装 → プリンタ機体に組込み**  
- 電波暗室で EMC 評価を実施（放射／伝導／感受性）  
- 結果：基材の誘電特性（Dk, Df, 吸湿特性）が**システム全体のEMI/EMC挙動に影響**  
- EMC試験を通じて、基材変更の影響を実機レベルで検証可能  

## 5. NCP接合の適用例 / Example of NCP Bonding
- アクチュエータの Au 配線と IC 接続に **NCP (Non-Conductive Paste)** を利用  
- **Au–Au金属接触**で導通を確保し、NCPは補強・空隙充填・防湿を担う  
- 実装ルール  
  - Au 表面の清浄化必須  
  - NCPは過不足なく、Pad周囲に逃げ領域を設ける  
  - 信頼性試験（HTS/85-85/HAST）で接触抵抗ドリフトを監視  

## 6. プロセスフロー / Process Flow

### 概要フロー
```mermaid
flowchart LR
    A[FCCL基材準備<br/>Cu ~8µm + PI] --> B[短冊化<br/>スリット/外形]
    B --> C[スプロケットホール形成]
    C --> D[フォトリソ/エッチング]
    D --> E[ソルダーレジスト形成]
    E --> F[Pad Auめっき ~0.5µm]
    F --> G[IC実装 (Auバンプ)]
    G --> H[アンダーフィル充填]
    H --> I[ヘッドモジュール化]
    I --> J[プリンタ機体に実装]
    J --> K[電波暗室でEMC評価]
    K --> L[設計フィードバック]
```

### NCP接合フロー
```mermaid
flowchart LR
  A[Au配線面洗浄/活性化] --> B[NCP塗布(基板側)]
  B --> C[高精度位置合わせ]
  C --> D[熱圧着(TC/TS)<br/>Au–Au接触+NCP硬化]
  D --> E[ポストキュア/外観・電気検査]
  E --> F[必要に応じ追加アンダーフィル/封止]
```

## 7. 比較・検討事項 / Comparative Considerations
- **Ni/Au vs 直Auめっき**：保存性 vs 実装性  
- **ロール基材 vs 短冊基材**：量産性 vs 精度  
- **アンダーフィル有無**：信頼性と絶縁性に影響  
- **NCP vs NCF vs ACF**：狭ピッチ・接合方式による選択肢  

## 8. SystemDK視点のまとめ / SystemDK Summary
- COF基材の変更は「材料 → パッケージ → モジュール → システム」全体に波及  
- EMC評価は、単なる材料選択以上に **システム設計上の重要なフィードバックループ**  
- SystemDK的には、**材料物性 → 実装信頼性 → 信号伝送特性 → EMC挙動** の因果連鎖を理解することが必須  

## 9. 学習課題例 / Learning Exercise
- Q1. 基材の誘電率 Dk が 0.5 増加した場合、伝送線路の特性インピーダンスとEMC特性にどう影響するか推定せよ。  
- Q2. NCP接合とACF接合の違いを整理し、アクチュエータ実装に最適な方式を説明せよ。
