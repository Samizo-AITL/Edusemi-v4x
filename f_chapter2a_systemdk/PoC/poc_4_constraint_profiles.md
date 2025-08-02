# 🎛️ 4. 物理制約プロファイル定義  
**4. Constraint Profiles for SI/PI, Thermal, Stress, and EMI/EMC**

---

## 🎯 目的｜Objective

この章では、SystemDKベースPoC設計における  
**物理制約（SI/PI、熱、応力、EMI/EMC）** に関する設計項目をプロファイル形式で整理する。

> This section outlines the key constraint profiles that guide multi-physics-aware design  
> across Signal/Power Integrity, Thermal, Mechanical, and EMI/EMC domains.

---

## 🔌 Signal / Power Integrity（SI/PI）

| 項目 | 内容 |
|------|------|
| PDN構成 | Power Tree設計、電源層スタッキング、デカップリング戦略 |
| IR Drop | 各モジュールに対する最大許容 IR voltage drop（例：< 5%） |
| インピーダンス整合 | 信号ラインの整合設計（例：Z0 = 50Ω） |
| ピーク電流/過渡応答 | 高速メモリアクセスやRF制御時の突入電流設計 |

---

## 🌡️ Thermal Constraint（熱）

| 項目 | 内容 |
|------|------|
| 熱源分布 | MRAM書込、AMSセンサ発熱、GAA演算負荷等の熱源 |
| 拡散パス設計 | シリコン〜パッケージ〜基板へ向かう放熱設計 |
| 温度上限 | AMSブロック < 85°C、MRAM周辺 < 125°C（例） |
| 熱暴走防止 | 熱帰還を想定したレイアウトシミュレーション |

---

## 🪵 Mechanical Stress（応力）

| 項目 | 内容 |
|------|------|
| 応力集中部位 | バンプ、TSV、接合界面の熱膨張差起因部位 |
| 材料選定 | CTE（熱膨張係数）・ヤング率の調整による緩和 |
| 結合方法 | 接着/配線/はんだ接合のメカニカル安定性 |
| 応力緩和設計 | リリーフホール、スリット、パッド分散技術など |

---

## 📡 EMI / EMC（電磁干渉・整合性）

| 項目 | 内容 |
|------|------|
| 高速信号処理 | クロックライン、PLL出力のEMノイズ制御 |
| GND構造 | グランドプレーン分離とシールド構造 |
| ノイズ帯域 | 放射/伝導ノイズの対象帯域と制限（例：CISPR準拠） |
| フィルタリング設計 | LCフィルタ、シリアルフェライト等の導入 |

---

## 🧩 制約の重なりと相関管理｜Constraint Coupling

- **熱×応力**：温度上昇 → 熱膨張 → 応力増加  
- **SI×EMI**：インピーダンス不整合 → リフレクション → ノイズ拡散  
- **電源×熱**：IR Drop増大 → 熱発生 → 動作不安定

> These profiles often overlap and interact; SystemDK integrates them through  
> a layered and traceable design methodology.

---

## 📘 本章のまとめ｜Summary

PoC設計における物理制約は、**個別ではなく連成的に考慮すべき要素**である。  
SystemDKはこれらを**明文化・視覚化・設計反映**することにより、  
**再利用可能な制約テンプレート**として構成可能にする。

> Physical design constraints are not isolated parameters  
> — SystemDK organizes them into reusable and consistent design knowledge.
