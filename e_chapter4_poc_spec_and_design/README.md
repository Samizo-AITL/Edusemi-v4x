# 🧩 実践編 第4章：PoC仕様書と設計展開

本章では、Sky130 PDKを用いた最小限の半導体設計PoC（Proof of Concept）を通じて、論理回路の仕様書作成から物理設計に至る一連のプロセスを実体験します。設計対象はFSM（有限状態機械）、MUX（多重器）、Adder（加算器）など、教育的かつ再利用性の高い基本ブロックで構成されます。

---

## 🎯 本章の目的

- PoCベースの設計仕様書を通じた設計要求の明確化  
- Sky130プロセスに準拠した設計制約の実践的理解  
- 回路設計・論理合成・物理設計の一連フローの習得  
- HDL記述、Makefile、自動化スクリプトとの接続理解  

---

## 🏗️ 対象プロセスと前提環境

- **使用PDK**：SkyWater Sky130  
- **使用ツール**：OpenLane v2, Magic, KLayout, Pythonベース自動化  
- **HDL言語**：Verilog 2005準拠  

---

## 📚 章構成とリンク

| 節番号 | ファイル名 | 内容概要 |
|--------|------------|-----------|
| [4.1](4.1_poc_spec_overview.md) | `4.1_poc_spec_overview.md` | 設計PoCの仕様全体と目的の整理 |
| [4.2](4.2_poc_block_definition.md) | `4.2_poc_block_definition.md` | 最小構成ブロック（FSM, MUX, Adder）の機能仕様とI/O |
| [4.3](4.3_sky130_design_constraints.md) | `4.3_sky130_design_constraints.md` | Sky130における設計制約とPDK依存項目の解説 |
| [4.4](4.4_verilog_and_testbench.md) | `4.4_verilog_and_testbench.md` | Verilog設計記述と検証ベンチの構成方法 |
| [4.5](4.5_physical_design_flow.md) | `4.5_physical_design_flow.md` | OpenLaneを用いた物理設計フロー（synth→place→route） |
| [4.6](4.6_layout_result_and_discussion.md) | `4.6_layout_result_and_discussion.md` | 成果検証、設計結果と波形の確認、まとめと展望 |

---

## 🧱 最小PoCブロック構成案

1. **FSM（有限状態機械）**  
   - 状態数：4状態（例：IDLE → LOAD → EXEC → DONE）  
   - 入出力：クロック、リセット、制御信号、出力フラグ  
   - 設計目的：状態遷移と制御信号の生成の学習  

2. **MUX（2:1 多重器）**  
   - 入力：A, B, SEL  
   - 出力：Y = SEL ? B : A  
   - 設計目的：シンプルな組み合わせ回路とその物理レイアウト確認  

3. **Adder（4ビット加算器）**  
   - 入力：A[3:0], B[3:0]  
   - 出力：SUM[3:0], COUT  
   - 設計目的：ゲートレベル最適化、ルーティング密度、タイミング検証など  

---

## 📏 Sky130設計制約項目（基本セット）

| 区分 | 制約項目 | 説明 |
|------|----------|------|
| 回路規模 | Gate数制限 | 合計1,000ゲート以下（OpenLane無理なく通す範囲） |
| タイミング | クロック周波数 | 最大25MHz想定（setup/hold margin確保） |
| 電源制約 | VDD, VSS | Sky130準拠（1.8Vドメイン基準） |
| IO制約 | スペース制限 | IO pad配置考慮（マクロサイズに収める） |
| レイアウト | DRC, LVS | Magic + Netgenにて制約通過可能レベル |
| ネーミング | Verilog信号名 | snake_case推奨、OpenLaneコンパチブル対応 |
| バス構造 | 入出力の表記 | [3:0]などのbit範囲付き記述で統一 |
| 設計エリア | 設計サイズ | MUX・FSMで <100µm × 100µm 程度を目安 |

---

## 📁 ソースディレクトリ構成

- [`src_rtl/`](src_rtl/)：RTL設計（FSM, MUX, Adder）
- [`src_tb/`](src_tb/)：テストベンチ（fsm_tb.v, adder_tb.vなど）

---

## 🛠 Makefile

- [`Makefile`](Makefile)：ビルド、シミュレーション、OpenLane実行の自動化コマンド集  

---

ご不明点があれば [Issue](https://github.com/Samizo-AITL/Edusemi-v4x/issues) または Discussions にてお問い合わせください。
