# 🔁 応用編 第8章：FSM設計（有限状態機械）

---

## 📘 概要

FSM（Finite State Machine：有限状態機械）は、制御回路や通信プロトコルなど、**時間的な順序性を持つ動作**を記述するための基本的な設計手法です。

この章では、**状態遷移の概念**から始まり、**Moore型／Mealy型の使い分け**、そして**VerilogによるFSM記述**までを、段階的に学びます。

FSMは、組込み回路・インタフェース制御・プロトコル制御など、**あらゆるSoC設計の中核技術**であり、順序論理を理解するための重要な教材となります。

---

## 🧩 セクション構成

| ファイル名 | 内容 |
|------------|------|
| [`fsm_overview.md`](fsm_overview.md) | FSMの基本概念、分類（Moore型 / Mealy型） |
| [`fsm_state_transition.md`](fsm_state_transition.md) | 状態遷移図・状態遷移表の書き方 |
| [`fsm_hdl_description.md`](fsm_hdl_description.md) | VerilogによるFSMの3段構成記述法 |

---

## 🎯 到達目標

- 状態機械の**基本構造と動作原理**を理解する
- 状態遷移図と状態遷移表を**自分で設計できる**
- FSMを**Verilogで正しく記述できる**（次状態・状態更新・出力の3分割）
- **Moore型とMealy型**の使い分けが説明できる

---

## 📚 関連章リンク

FSMは、次の基礎章と深く関連しています：

- [第2章 デジタル論理と論理回路設計](../chapter2_comb_logic/README.md)  
  ↳ 組み合わせ論理と順序論理の接続点としてFSMを導入  
- [第5章 SoC設計フロー](../chapter5_soc_design_flow/README.md)  
  ↳ FSMを含む制御ロジックをRTLで設計し、合成〜物理設計へ接続

---

## 🛠 応用展開例（今後追加予定）

- UARTやI2CプロトコルのFSM制御例
- FSM生成ツール（YosysFSM、Xilinx FSM Editorなど）との連携
- 状態遷移ログの自動チェック（Assertionベース検証との統合）

---

© 2025 Shinichi Samizo / MIT License
