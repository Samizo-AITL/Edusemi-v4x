# 📐 高耐圧デバイスのレイアウト設計と最適化

---

## 📘 概要

高耐圧デバイス（LDMOS、HV-CMOS等）の信頼性を確保するには、**物理レイアウトにおける工夫**が不可欠です。  
電界分布・熱拡散・製造ばらつきに影響する要素を理解し、**量産設計レベルの最適化**を行う必要があります。

この章では、以下の観点から設計ルールと実践的な最適化手法を解説します：

- ガードリング設計
- セル間距離の確保
- CMPダミーパターン配置
- 絶縁境界・熱経路の工夫

---

## 🏗️ レイアウト設計項目と目的

| 設計項目 | 目的 | 実装上の工夫 |
|----------|------|--------------|
| ガードリング | 寄生ラッチアップ・電界集中の緩和 | N+/P+リング＋接地／ウェル接続 |
| セル間スペース | 空乏層の拡張／絶縁保持 | 3〜5μm以上の空白領域 |
| CMPダミーパターン | 平坦化工程のばらつき低減 | 規則的なdummy配列（配線密度維持） |
| 熱経路設計 | 熱集中防止／放熱制御 | 熱拡散層追加・配線幅拡大など |

---

## 🧪 CMPダミーパターンとは

CMP（Chemical Mechanical Polishing）工程では、パターン密度に差があると**研磨ムラ（dishing・erosion）**が生じ、デバイス性能にばらつきが出ます。
```
配線層（例）

┌─────┐      ┌─────┐
│配線A│      │配線B│      ← 密度差あり
└─────┘      └─────┘
```
↓ CMPダミーを挿入
```
░░░░░░░      ░░░░░░░
```
- ダミー金属は電気的機能を持たず、**研磨密度の調整**目的
- **ツール制限（dummy密度10〜70%など）**をPDKで確認

---

## 🧯 ガードリングとESD/ラッチアップ対策

- 高電圧端子周囲に**N+/P+リング構造**
- **接地／ウェルバイアス強化**により寄生トランジスタの起動を抑制
- 高耐圧LDMOSでは**複数重ねリングや深ウェル接続**が使われる

---

## 📚 教材的意義

- プロセス実装との関係を踏まえた**設計実務感覚**を養成  
- 見落とされがちな**微細な物理制約**への感度を高める  
- テープアウト／量産に向けた**最終チェック視点**として活用可能

---

## 🔗 関連項目・章

- [`dvdt.md`](./dvdt.md)：物理破壊を防ぐためのレイアウト視点との連動  
- [chapter5_soc_design_flow](../chapter5_soc_design_flow/)：配置配線、DRC制約との関係  
- [chapter6_test_and_package](../chapter6_test_and_package/)：CMPばらつきがETESTに与える影響

---

© 2025 Shinichi Samizo / MIT License
