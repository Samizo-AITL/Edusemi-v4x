# 🔄 PDKの世代と互換性  
# 🔄 PDK Generations and Compatibility

---

## 📘 概要｜Overview

PDK（Process Design Kit）は、特定の半導体プロセスに合わせた設計支援ファイル群です。  
世代をまたぐ互換性や移行性、設計資産の再利用性は、**実務でも教育でも極めて重要**な観点です。

PDKs are design-support file packages tailored to specific semiconductor processes.  
Compatibility across generations and reuse of design assets are critical in both **practical design and education**.

---

## 🏗️ PDKの基本構成とバージョン管理｜PDK Structure and Versioning

| 📦 **項目｜Item** | 📘 **内容｜Description** |
|------------------|--------------------------|
| デザインルール<br>Design Rules (DRC) | 層間距離・配線幅・リソ制限など<br>Spacing, width, lithographic rules |
| デバイスモデル<br>Device Models | SPICE用のMOS/BJT等の振る舞い<br>Behavioral models for SPICE simulations |
| レイアウト構成<br>Layout Elements | GDS層・マクロセル・ダミー定義<br>GDS layers, macros, dummy rules |
| 抽出ルール<br>Extraction Rules (LPE) | RC抽出用のパラメータセット<br>Parasitic extraction models |
| シンボル／回路図<br>Symbols/Schematics | Schematic entry対応ライブラリ<br>Libraries for schematic tools |
| スクリプト群<br>Scripts | DRC/LVS実行・Makefile・設定等<br>Verification scripts and flows |

- **PDKは通常プロセスごとに個別設計され、EDAツールごとに最適化**される  
  *Each PDK is tailored to a specific process and optimized for the EDA toolchain.*
- Sky130では、`sky130A`, `sky130B` など**Gitベースでバージョン管理**される例がある  
  *Sky130 demonstrates Git-based versioning with multiple variants.*

---

## 📈 プロセス世代ごとの差異｜PDK Differences Across Generations

| 🧭 **世代｜Generation** | 🧪 **主な違い｜Key Differences** | ⚠️ **設計注意点｜Design Considerations** |
|------------------------|------------------------------|------------------------------------------|
| 0.35–0.18µm | 単純構造・長チャネル設計<br>Simple, long-channel design | 手動設計中心、PDKも簡易<br>Manual layout, simplified PDKs |
| 0.13–90nm | 配線RC支配・寄生考慮<br>Interconnect-dominated delay | RC抽出が性能に直結<br>Accuracy of extraction is critical |
| 65–28nm | 方位・DFM制限強化<br>Orientation rules, DFM limits | レイアウト依存効果が増大<br>Layout-dependent effects dominate |
| FinFET世代 | 非平面構造・ゲート3D化<br>Non-planar, 3D gate structures | モデル精度・寄生再評価必須<br>Modeling and parasitic precision required |

---

## 🔄 互換性と設計資産の再利用｜Compatibility & Reusability of Design Assets

### ❌ **PDK間の完全互換は困難**  
**Complete compatibility is difficult between PDKs**

- レイアウトや回路図は**層構成・ピン配置・命名規則**に依存  
  *Layouts and schematics depend heavily on PDK-specific conventions*
- 寄生抽出モデルやスケーリングルールも異なる  
  *Parasitic models and scaling behavior vary across generations*

### ✅ **再利用可能な設計資産**  
**Reusable assets across PDKs**

| 再利用対象 | 内容 |
|------------|------|
| RTL / Verilog / SystemC | プロセス非依存な機能設計コード |
| テストベンチ / シミュレーション環境 | SPICEモデルを入れ替えることで再利用可能 |
| フロアプラン案 / ネーミングルール | 柔軟性が高い設計資産として流用可能 |

---

## 🧪 教育・研究での応用：Sky130の例｜Educational Use Case: Sky130

- `sky130A` はOSSベースPDKの代表例  
  *sky130A is a representative open-source PDK*

| 特徴 | 内容 |
|------|------|
| ツール連携 | Magic, Xschem, ngspice, OpenROAD などに対応 |
| 学習用途 | 半導体教育・研究に最適。プロセス理解を深める教材構成 |
| 拡張性 | Sky90, Sky65 などの世代追加が期待されている |

---

## 🎯 教材的意義｜Educational Significance

- **PDK互換性と設計依存性**を理解することで、設計資産の限界と活用可能性を判断できる  
  *Understanding PDK compatibility clarifies the limits and potential of design reuse.*
- **プロセス進化と物理制約**の関係を可視化できる  
  *Clarifies the correlation between process scaling and physical constraints.*
- **Sky130などのOSS PDK**を活用することで、教育実験における柔軟性を確保できる  
  *Open PDKs like Sky130 offer flexibility in hands-on learning environments.*

---

## 🔗 関連資料｜Related Materials

- [`pdk_structure.md`](./pdk_structure.md)：PDKの基本構成とファイル群  
  *Structure and components of a PDK*
- [`eda_toolchain.md`](./eda_toolchain.md)：EDAツールとの接続構成  
  *EDA tool integration with PDKs*
- [`rule_check_flow.md`](./rule_check_flow.md)：設計検証フロー（DRC/LVS/ERC）  
  *Design verification flow*

---

### 🛠️ 応用編 第6章：PDKとEDA環境｜PDK and EDA Environment  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 **Shinichi Samizo** / MIT License
