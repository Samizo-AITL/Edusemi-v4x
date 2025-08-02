
# 🔗 5. Chiplet統合における制約整合とレイアウト設計  
**5. Constraint Alignment and Layout Design in Chiplet Integration**

---

## 🎯 目的｜Objective

本章では、GAA / AMS / MRAM 各ブロックを2.5Dインターポーザ上に統合する際の  
**レイアウト設計、制約整合、パッケージ配置**について記述する。

> This section outlines layout strategies and constraint alignment  
> for chiplet integration over a 2.5D interposer platform.

---

## 🗺️ 統合構造と構成レイヤー｜Integration Structure

- **GAA Logic**：中央配置（主制御・高密度ロジック）
- **AMS Block**：エッジ側配置（ノイズ源から距離を確保）
- **MRAM Block**：熱設計上、GAAとの間隔を持たせて配置
- **Power/GND層**：上位層に分離構造、バイパス・デカップリング配置
- **クロック/通信線**：隣接干渉を避けて物理ルートを調整

---

## 🧮 配置と配線設計｜Floorplan and Routing

| 項目 | 設計方針 |
|------|----------|
| クロック供給 | 中央から各ブロックへ等長配線設計 |
| シリアル通信線 | AMS干渉を避けるルート設計 |
| 電源供給 | AMS用は専用PDN or LDOを通すことを推奨 |
| GND配置 | EMI制御のためAMS/GAAで分割構造採用可 |

---

## 📡 EMI / 熱 / 応力の配置考慮｜Constraint-Aware Placement

- **EMI**：高周波クロック源（PLL）はAMSから物理的に隔離
- **Thermal**：MRAM書込みによる発熱をAMSに伝播させない
- **Mechanical**：ブロック間の熱膨張差による応力集中回避

> Placement and routing must consider physical proximity, thermal boundaries,  
> and signal integrity simultaneously.

---

## 🔄 制約整合と競合回避｜Constraint Reconciliation

| 制約カテゴリ | 競合例 | 対応設計方針 |
|---------------|--------|----------------|
| SI vs EMI | クロック信号をGAAとAMSが共有 | バス分離・GND強化 |
| 熱 vs 応力 | 発熱ブロックが応力集中点と重なる | 中間層で放熱 or 分散配置 |
| 電源 vs EMI | 高電流路がノイズ源と交差 | 層分割とフィルタ挿入 |

---

## 📘 本章のまとめ｜Summary

- **GAA / AMS / MRAM の物理的配置と接続方針**を明確化  
- 各種制約（熱・応力・EMI・電源）を**相互に衝突しないよう調整**
- 次章ではこの統合レイアウトに対して**FEM解析による定量評価**を行う

> Clear alignment of layout with physical constraints sets the stage  
> for precise simulation and optimization in the following FEM analysis.
