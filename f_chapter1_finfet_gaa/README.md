# 特別編 第1章：先端ノード（FinFET、GAA等）

## 概要

本章では、微細化技術の限界を超えるために導入された**FinFET**および**GAA（Gate-All-Around）Multi-Nanosheet FET**について、その構造・電気特性・製造プロセス・設計影響を総合的に解説します。

これらのトランジスタ構造は、従来のプレーナ型MOSFETが抱える**短チャネル効果（SCE）**や**ゲート制御性の劣化**といった問題を克服するために登場し、現在の先端ノード（5nm/3nm世代）以降で主流となっています。

---

## 節構成（予定）

| 節番号 | タイトル | 内容概要 |
|--------|----------|----------|
| 1.1 | プレーナMOSの限界と微細化の壁 | SCE, DIBL, リーク電流などの課題整理 |
| 1.2 | FinFET構造の原理とプロセス概要 | 立体チャネル、包囲ゲート、主要プロセス |
| 1.3 | GAA構造とMulti-Nanosheet技術 | 犠牲層エッチとナノシート形成の詳細 |
| 1.4 | 特性比較：プレーナ vs FinFET vs GAA | 電気特性と設計性の観点から定量比較 |
| 1.5 | 設計上の制約とPDKの変化 | レイアウト制限、寄生、RC抽出など |
| 1.6 | 次世代トレンド：CFET・3D統合など | Fin/GAA以降の技術潮流と展望 |

---

## 補足資料

| ファイル名 | 概要 |
|------------|------|
| [`finfet_process_flow.md`](./finfet_process_flow.md) | FinFETの48ステップ製造プロセス |
| [`gaa_process_flow.md`](./gaa_process_flow.md) | GAA Multi-Nanosheet FETの48ステップ製造プロセス |
| [`finfet_vs_gaa_summary.md`](./finfet_vs_gaa_summary.md) | FinFETとGAAの構造・特性・設計影響まとめ |

---

## 教材のねらい

- FinFET/GAAの**物理構造と製造技術の理解**
- **設計ルールやPDKの背景**の把握
- 現実の**製品実装に必要な制約意識**の獲得

---

## ライセンスと著者

本教材は MIT ライセンスで公開されています。  
著者：三溝 真一（@Samizo-AITL）  
連絡先：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)
