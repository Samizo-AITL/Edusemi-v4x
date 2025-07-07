# 基礎編 第3章：プロセス技術の変遷と設計限界

本章では、0.5µmから90nmノードに至るCMOS技術の変遷を通して、  
**設計可能性を左右するプロセス技術の進化と限界**を学びます。

寸法の微細化だけでなく、**STI・LDD・サリサイド・多層配線・CMP・OPC**といった構造・材料・描画技術がどのように相互連携して発展してきたかを体系的に整理します。  
また、**Short Channel Effect（SCE）**や**Hot Carrier Injection（HCI）**といった信頼性限界にも触れ、教育に適したプロセス（sky130や0.18µm）を選定する視点も提示します。

---

## 📘 節構成（`chapter3_process_evolution/`）

| 節番号 | ファイル名 | 内容概要 |
|--------|------------|----------|
| 3.1 | [`3.1_node_scaling_history.md`](./3.1_node_scaling_history.md) | CMOSプロセスの世代変遷（0.5µm〜90nmの技術展開） |
| 3.2 | [`3.2_cmos_structure_shift.md`](./3.2_cmos_structure_shift.md) | トランジスタ構造：STI、浅接合、LDD、サリサイド |
| 3.3 | [`3.3_interconnect_and_litho.md`](./3.3_interconnect_and_litho.md) | 配線と描画技術：Cu、多層配線、CMP、OPCなど |
| 3.4 | [`3.4_variation_and_reliability.md`](./3.4_variation_and_reliability.md) | 微細化による設計限界：SCE、DIBL、Vthばらつき、HCIなど |
| 3.5 | [`3.5_summary_and_scope.md`](./3.5_summary_and_scope.md) | 教育向きプロセス：sky130や0.18µmの意義と活用 |

---

## 🧠 学習のねらい

- プロセス技術を「**設計にどう効いてくるか**」の視点で体系的に理解する  
- 構造革新・描画精度・信頼性問題が**設計制約として顕在化**することを学ぶ  
- sky130や0.18µmのような**教材適用可能なプロセス技術を選べる判断力**を養う

> ※ フォトリソグラフィ・エッチング・成膜・洗浄といった基本工程は、3.1や3.2の背景技術として随所に含まれています。

---

## 📂 ディレクトリ構成

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

## 🔄 次章への接続

第4章では、sky130や0.18µmプロセスを具体的に取り上げ、  
MOSトランジスタの電気特性、設計ルール、PDKの活用方法を深掘りしていきます。

---

## © ライセンス

この教材は MIT ライセンスの下で公開されています。  
詳細はプロジェクトルートの [`LICENSE`](../LICENSE) をご参照ください。
