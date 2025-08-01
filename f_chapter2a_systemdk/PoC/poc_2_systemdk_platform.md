# 🧰 poc_2_systemdk_platform.md  
**SystemDKプラットフォームの概要と役割**  
**SystemDK Platform: Overview and Functions**

---

## 📘 概要｜Overview

SystemDKは、チップレット統合設計において複数の物理制約（SI/PI・熱・応力・EMI/EMC）を  
**統合的に定義・伝播・最適化**するための設計支援プラットフォームです。

SystemDK is a design support platform that enables **integrated definition, propagation, and optimization**  
of multiple physical constraints (SI/PI, thermal, stress, EMI/EMC) in chiplet-based design.

---

## 🧩 主な機能｜Key Functions

| 機能 / Function | 説明 / Description |
|----------------|--------------------|
| 制約テンプレート生成<br>Constraint Template Generator | 各物理領域（SI/PI, 熱など）に応じた設計テンプレートを提供 |
| ブロック属性DB連携<br>Block Attribute DB Interface | 各ダイやIPのノード/電圧/熱感度/信号特性などのメタ情報管理 |
| パッケージ階層対応<br>Hierarchical Package Modeling | InterposerやRDL、封止材などを含むマルチ階層の構造記述対応 |
| FEM/EM解析連携<br>FEM/EM Simulation Interface | 外部ツールと連携して構造・電場・熱・応力解析を可能に |
| Constraint-Driven Placement | 制約マップに基づくブロック配置最適化支援 |

---

## 🏗️ 教材PoCでの適用例｜Use in This PoC

- **GAAブロック**の高密度実装における**熱集中評価と緩和配置**
- **AMSダイ**と**MRAMダイ**間の**電源ネットワーク階層伝播**
- **RDL層設計の応力集中リスク管理**と**シミュレーション連携**

Applied in this PoC as:

- Thermal hotspot modeling and placement relaxation for **GAA block**
- Hierarchical **PDN integrity** propagation between **AMS** and **MRAM** dies
- Structural analysis of **stress-concentrated RDL regions** and verification support

---

## 🧠 教育的ポイント｜Educational Highlights

- **Constraint-driven design thinking** を習得するための教材支援基盤
- 複数の物理制約が**並列・交差的に設計に影響**する様子を視覚化
- PDK / IPDK / PKGDK → SystemDK という**階層的設計の全体像**を体得

---

## 🔗 関連リンク｜Related Links

- [poc_1_motivation.md](./poc_1_motivation.md)
- [poc_3_block_spec.md](./poc_3_block_spec.md)
- [f2a_1_systemdk_overview.md](../f2a_1_systemdk_overview.md)
- [f2a_4_emiemc.md](../f2a_4_emiemc.md)
