# 第3章：プロセス技術の変遷と設計制約の歴史的理解

本章では、0.5µm〜90nm世代のCMOSプロセス技術の進化を、設計者視点で丁寧にたどります。  
寸法縮小、構造変化、配線技術、信頼性問題など、回路設計に直接関係するトピックに絞って構成しています。

sky130やTSMC 0.18µmなどの教育用プロセスを扱うにあたり、  
それらがどのような技術背景の上に成り立っているのかを理解することが本章の目的です。

---

## 🎯 本章の学習目標

- CMOSの技術ノード縮小とともに、何が変わり、何が制約されたかを理解する
- トランジスタ構造・配線・リソグラフィの進化とその設計への影響を把握する
- HCIやDIBLなどの信頼性・短チャネル効果が、設計ルールや回路設計に与えた制限を理解する
- 教材対象プロセス（例：sky130）の設計的限界と背景技術を正しく位置づける

---

## 📘 章構成

| 節番号 | ファイル | 内容概要 |
|--------|----------|----------|
| 3.1 | [`3.1_node_scaling_history.md`](./3.1_node_scaling_history.md) | 0.5µm〜90nmのノード進化と寸法ルールの変遷。i線→KrF→ArFへの露光技術推移も含む。 |
| 3.2 | [`3.2_cmos_structure_shift.md`](./3.2_cmos_structure_shift.md) | LOCOSからSTIへ。浅接合、LDD、サリサイド構造の導入と設計制約への影響。 |
| 3.3 | [`3.3_interconnect_and_litho.md`](./3.3_interconnect_and_litho.md) | Al→Al-Cu→Cu配線の遷移。RC遅延、EM対策、多層化、OPC、ハーフトーン技術など。 |
| 3.4 | [`3.4_variation_and_reliability.md`](./3.4_variation_and_reliability.md) | DIBL、Vthばらつき、リーク電流、HCIなどの信頼性劣化と設計への影響。 |
| 3.5 | [`3.5_summary_and_scope.md`](./3.5_summary_and_scope.md) | 教材対象プロセス（sky130、0.18µm）の技術的立ち位置と適用可能な設計前提の確認。 |

---

## 🧠 補足されるキーワード・図版例

- 技術ノード一覧表と寸法比較（L, W, コンタクト、配線幅等）
- STI断面図、LDD構造、サリサイド形成工程の図
- 多層配線構造とRCモデル図
- OPC前後のパターン比較図
- HCI・DIBLの現象イメージと信頼性劣化曲線
- 各図は `/images/chapter3_*.png` として別途整理予定

---

## 📂 ディレクトリ構成（予定）

```
Edusemi-v4x/
└── chapter3_process_evolution/
    ├── README.md
    ├── 3.1_node_scaling_history.md
    ├── 3.2_cmos_structure_shift.md
    ├── 3.3_interconnect_and_litho.md
    ├── 3.4_variation_and_reliability.md
    └── 3.5_summary_and_scope.md
```

---

## 🔄 次章とのつながり

- 第4章では、本章で扱った構造・寸法が**具体的にどのようなトランジスタ特性・設計ルールに結びつくか**を学びます。
- また、BTI・HCI などの信頼性劣化がモデル化され、PDKへと受け渡される仕組みを扱います。

---

## © ライセンス

この教材は MIT ライセンスの下で公開されています。  
詳細はプロジェクトルートの [LICENSE](../LICENSE) をご確認ください。
