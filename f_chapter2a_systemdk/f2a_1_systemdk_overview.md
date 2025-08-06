---
layout: default
title: 2a.1 SystemDKの全体像と設計階層
---

---

# 2a.1 SystemDKの全体像と設計階層  
**2a.1 Overview and Hierarchy of SystemDK**

---

## 📘 概要｜Overview

SystemDK（System Design Kit）は、近年のChipletベース設計や3D/2.5Dパッケージにおいて、**物理制約を包含した最上位の設計キット**です。RTL設計から始まり、GDS→IC製造→パッケージ設計を経て、**実際に“動作するシステム全体”を設計対象とする**段階に相当します。

System Design Kit (SystemDK) is the highest-level design kit in the modern Chiplet-based or 3D/2.5D integration era. It bridges RTL and GDS design with system-level considerations, enabling **physical, thermal, mechanical, and electromagnetic constraints** to be co-designed and verified.

---

## 🧭 設計階層と設計キットの関係｜Design Stack and Design Kits

| 層 / Layer | 設計対象 / Target | 設計キット / Design Kit |
|------------|------------------|---------------------------|
| ① RTL設計 | 機能記述（Verilog等） | –（合成・検証） |
| ② GDS設計 | 配置配線＋物理レイアウト | PDK（Process Design Kit） |
| ③ IC製造 | シリコン製造 | –（Foundry Process） |
| ④ Chiplet仕様 | I/O配置・電気特性 | IPDK（IP Design Kit） |
| ⑤ パッケージ設計 | RDL・Bump・熱設計 | PKGDK（Package Design Kit） |
| ⑥ システム設計 | 配置・電源・熱・EMI | **SystemDK（本章対象）** |

---

## 🔗 SystemDKの構成要素｜SystemDK Components

SystemDKは以下のような物理層制約情報を統合的に扱います：

- **PDN情報**：IRドロップ・グランドバウンス・デカップリング配置  
- **SIモデル**：インピーダンス整合・クロストーク・反射対策  
- **熱モデル**：熱拡散マップ、材料CTE、冷却構造の伝播経路  
- **応力分布**：樹脂・金属・TSV間の応力集中  
- **EMI/EMCルール**：GND層設計、ノイズ抑制、外部通信との整合性  
- **PoC用統合設計図**：配置図、BOM、モデルリンク、制約ファイル群

---

## 🎓 教育的メッセージ｜Educational Insight

> チップ単体の設計力に加えて、**“モジュールとして機能させる力”**が今後の設計者に求められる。SystemDKはその実践的な教育橋梁である。

In addition to chip-level expertise, engineers must acquire the ability to **design and verify physical implementation as a working module**. SystemDK provides the educational foundation for that capability.

---

## 🧩 本章以降との接続｜Linked Topics in This Chapter

| 次節 | 内容概要 |
|------|-----------|
| [`f2a_2_sipi.md`](f2a_2_sipi.md) | SI/PI設計とPDN構造 |
| [`f2a_3_thermal.md`](f2a_3_thermal.md) | 熱設計と材料分布 |
| [`f2a_4_mechanical.md`](f2a_4_mechanical.md) | 実装応力と界面信頼性 |
| [`f2a_5_emi_emc.md`](f2a_5_emi_emc.md) | EMI/EMC設計指針 |
| [`f2a_6_constraint_tradeoff.md`](f2a_6_constraint_tradeoff.md) | 制約間の連成とトレードオフ |
| [`f2a_7_systemdk_poc.md`](f2a_7_systemdk_poc.md) | 統合演習PoCへの応用 |

---

## 🔗 関連リンク｜Related Links

- [`f_chapter2_chiplet_pkg/`](../f_chapter2_chiplet_pkg/)：Chiplet構造とPKG技術
- [`d_chapter5_analog_mixed_signal/`](../d_chapter5_analog_mixed_signal/)：AMS設計とレイアウト制約
- [`f_chapter4_fsm_pid_llm/`](../f_chapter4_fsm_pid_llm/)：統合制御SoC設計と実装検証

---
