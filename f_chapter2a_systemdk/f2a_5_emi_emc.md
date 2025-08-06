---
layout: default
title: 2a.5 EMI/EMC設計とノイズ対策
---

---

# 2a.5 EMI/EMC設計とノイズ対策  
**2a.5 EMI/EMC Design and Noise Mitigation**

---

## 📘 概要｜Overview

本節では、SystemDKにおける物理制約の一つである  
**EMI（電磁妨害）**と**EMC（電磁両立性）**に対する  
設計的配慮と対策技術を扱います。

This section addresses design considerations and countermeasures  
for **EMI (Electromagnetic Interference)** and **EMC (Electromagnetic Compatibility)** in SystemDK.

高周波化・高速インタフェース・高密度実装により、  
**設計段階からのEMI/EMC対策が必須**となっています。

---

## 📡 EMIとEMCの定義｜Definition

| 用語 / Term | 説明 / Description |
|-------------|--------------------|
| EMI（電磁妨害） | 電磁波により他の回路・機器に悪影響を与える現象 |
| EMC（電磁両立性） | 機器が妨害も受けず、妨害も出さずに共存できる能力 |
| 放射ノイズ（Radiated EMI） | アンテナ効果で空間に放出されるノイズ |
| 伝導ノイズ（Conducted EMI） | 電源・信号ラインを通じて伝わるノイズ |
| エミッション / イミュニティ | 発する側 / 受ける側の観点による分類 |

---

## 🔍 ノイズ源とパス｜Noise Sources and Paths

| ノイズ源 | 内容 | 対策例 |
|----------|------|--------|
| 高速クロック | 周波数成分によるEM波発生 | シールド、拡散クロック、スルーレート制御 |
| スイッチング回路 | 電流急変による伝導ノイズ | デカップリング、フェライトビーズ |
| 不連続GND | GNDリターンループ生成 | GNDプレーン連続化、スティッチング |
| ケーブル／パッド | アンテナ化による放射ノイズ | 終端抵抗、差動伝送、EMIフィルタ |

---

## 🧰 EMI/EMC設計の実践的対策｜Design Mitigation Techniques

- **GNDプレーンの連続性**：分割GNDやリターンパスの検討  
- **デカップリング配置**：ノイズ源近傍に適切な容量値を配置  
- **レイアウト最適化**：差動ペア整合、ループ面積の最小化  
- **伝送線路設計**：インピーダンス整合、終端処理  
- **EMIシールド材**：導電性ガスケット、メタルカバー

---

## 🧪 EMC測定と試験規格｜EMC Evaluation and Standards

| 規格 / Standard | 内容 / Description |
|----------------|--------------------|
| CISPR 22 / 32 | IT機器の放射・伝導ノイズ試験 |
| IEC 61000-4-x | 静電気放電、サージ、ファストトランジェントなどの耐性試験 |
| FCC Part 15 | 米国におけるEMI規制 |
| MIL-STD-461 | 軍用機器の電磁適合性要件 |
| ISO 11452 | 車載機器のEMC試験規格 |

---

## 🎓 教育的メッセージ｜Educational Message

> EMIは“目に見えない設計不良”  
> **回路・配線・実装の整合性**がノイズを制御する。

> EMI is “an invisible design defect.”  
> Noise can only be controlled through **alignment of circuits, layout, and implementation.**

---

## 🔗 関連節｜Linked Sections

- [`f2a_2_sipi.md`](f2a_2_sipi.md)：PIとの干渉・共振現象  
- [`f2a_4_mechanical.md`](f2a_4_mechanical.md)：振動・変形によるノイズ影響  
- [`f2a_6_constraint_tradeoff.md`](f2a_6_constraint_tradeoff.md)：EMI対策と性能トレードオフ

---

## 📎 参考資料｜References

- “EMC Design Guide,” TI Application Notes  
- “Electromagnetic Compatibility Engineering,” Henry Ott  
- IEC / CISPR / FCC 各種EMC規格ドキュメント  
- ANSYS SIwave / Keysight EMPro

---

**[← 戻る / Back to Special Chapter 2 Top](./README.md)**
