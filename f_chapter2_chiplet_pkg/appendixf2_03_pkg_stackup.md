# 📘 Appendix 2.3：インターポーザと再配線層（RDL）の積層構造  
# 📘 Appendix 2.3: Interposer and Redistribution Layer (RDL) Stack Structures

---

本資料では、2.5D/3Dパッケージにおける**インターポーザ構造やRDLの積層構成**を、典型的な設計例を交えて解説します。  
This appendix introduces **interposer wiring and redistribution layer (RDL) stack configurations** used in 2.5D/3D packaging technologies.

---

## 🧩 インターポーザ（Si）構造例  
## 🧩 Silicon Interposer: Structural Example

### ✦ 典型構成（上面図） / Typical Layout (Top View)

```
Top View:
┌─────────────┐
│  Die1  Die2 │  ← 複数ロジックダイ / Multiple Logic Dies
│   │     │   │
└────┬───────┘
     │  TSV  ↓
     │───────┐
     ▼       │
Bottom: RDL + bump array
```

### ✦ 積層断面構成 / Cross-Sectional Layers

| 層 / Layer | 内容 / Description | 特徴 / Characteristics |
|------------|---------------------|--------------------------|
| **Die層**<br>Die Layer | 複数のロジック／メモリダイ<br>Logic or memory dies | μ-bumpで接続<br>Connected via μ-bumps |
| **接続層**<br>Connection Layer | TSV + RDL | 垂直配線＋再配線層<br>Vertical vias and metal routing |
| **配線層**<br>Metal Layer | Cu + PI（2–4層） | 高密度Cu配線＋PI絶縁<br>High-density Cu + PI insulation |
| **バンプ層**<br>Bump Layer | C4/Snバンプ | 基板（FC-BGA）と接続<br>Connection to substrate (e.g., FC-BGA) |

---

## 🔄 RDL構造（Fan-Out/WLP型）  
## 🔄 RDL Structure: Fan-Out and WLP Type

### ✦ Fan-Out型RDLの典型構成 / Typical Fan-Out RDL Stack

| 層 / Layer | 材料 / Material | 目的 / Purpose |
|------------|------------------|----------------|
| **上部配線層**<br>Top Metal Layer | Cu + PI | 信号ルーティング<br>Signal routing |
| **中間層**<br>Mid Layers | Cu + PI (2–6層) | 多層配線構成<br>Multilayer redistribution |
| **チップ埋込層**<br>Chip-Embed Layer | Mold樹脂<br>Mold Resin | ファンアウトスペース確保<br>Die support and fan-out area |
| **下部接続層**<br>Bottom I/O Layer | Cuバンプ<br>Cu bumps | PCB接続（LGA/BGA）<br>Board-level connectivity |

### ✦ 特徴 / Characteristics

- **コアレス構造**：基板レスのため超薄型化が可能  
  *Coreless* design enables ultra-thin packaging  
- **チップ周囲への配線拡張（Fan-Out）**  
  Signal fan-out from embedded die to wider region  
- **μ-bumpやHybrid Bondingとの相性が良好**  
  Compatible with μ-bump and hybrid bonding interfaces

---

## 🏗️ 多層化における設計ポイント  
## 🏗️ Key Considerations for Multilayer RDL and Interposers

| 観点 / Aspect | 留意点 / Design Notes |
|----------------|------------------------|
| **寸法制御**<br>Dimensional Control | 膜厚・ライン幅・配線間隔の精密管理<br>Precise control of thickness, width, spacing |
| **熱応力管理**<br>Thermal Stress | CTE差によるひずみに配慮<br>CTE mismatch between layers |
| **レジスト整合性**<br>Resist Alignment | マルチレイヤのアライメント精度が重要<br>Critical mask alignment for each layer |
| **平坦性制御**<br>Planarization | CMPによる表面平坦化が必須<br>CMP needed for step-height reduction and litho accuracy |

---

## 📌 まとめ / Summary

インターポーザとRDLは、チップ間の**電気・熱・機械インタフェース**として機能する**パッケージ基盤技術**です。  
Interposers and RDLs serve as the **mechanical, electrical, and thermal interface** between multiple chips.

➡ これらの積層構造の最適設計は、**高密度・高性能なパッケージングの鍵**となります。  
➡ Their careful design determines the **scalability and performance** of advanced packages.

---
