# 2a.4 実装応力と界面信頼性  
**2a.4 Mechanical Stress and Interface Reliability**

---

## 📘 概要｜Overview

本節では、SystemDKにおいて重要な物理制約である  
**実装応力（Mechanical Stress）**と  
**界面信頼性（Interface Reliability）**の設計観点を扱います。

This section addresses the key physical constraints of  
**mechanical stress** and **interface reliability** in SystemDK-level design.

パッケージ材料、接合構造、温度変化による膨張差などが、  
長期信頼性や実装故障の主要因となります。

---

## 🧱 応力・変形に関する基礎｜Basic Stress & Deformation Concepts

| 用語 / Term | 説明 / Description |
|-------------|--------------------|
| 応力（Stress, σ） | 単位面積あたりの力（N/m²） |
| 歪み（Strain, ε） | 単位長さあたりの変形量（無次元） |
| ヤング率（Young’s Modulus, E） | 応力/歪みの直線関係係数（剛性指標） |
| CTE（線膨張係数） | 温度1℃あたりの伸び率（ppm/°C） |
| 熱応力（Thermal Stress） | 異なるCTE間での温度差による応力発生 |

---

## 🔍 主な応力起因の不具合例｜Common Stress-Induced Failures

| 不具合 | 原因 | 対策例 |
|--------|------|--------|
| バンプクラック | チップ–サブ基板間のCTE不整合 | アンダーフィル材、CTEマッチング |
| TSV剥離 | TSV–Si界面の熱サイクル応力 | バッファ層設計、低応力構造 |
| RDL割れ | カッパー配線層の屈曲・熱応力 | 線幅最適化、緩衝層挿入 |
| TIMポンピング | 熱サイクルでの厚み変動 | TIM選定・表面整合性の改善 |

---

## 🧰 応力設計の実務ポイント｜Practical Stress-Aware Design Tips

- 材料選定：CTE, E値, 弾性率、界面強度を考慮  
- アンダーフィル／バッファ材の導入による緩衝  
- FEM応力解析：パッケージ3Dモデルによる熱応力分布評価  
- 応力拡散経路と構造的対称性の設計（BGA配置、ヒートスプレッダ）  
- Reliability Simulation：Thermal Cycling, Drop Test, Moisture Resistance

---

## 🧪 応力と信頼性評価手法｜Stress and Reliability Evaluation

| 評価法 | 内容 / Description |
|--------|--------------------|
| TCT（Thermal Cycling Test） | 熱サイクル環境下での界面・接合強度評価 |
| Warpage測定 | チップ・基板の反り評価（干渉干渉計等） |
| X線CTスキャン | 接合部のクラック・剥離の可視化 |
| パッケージリフロー評価 | SMT時の瞬間加熱に対する耐性確認 |

---

## 🎓 教育的メッセージ｜Educational Message

> 「熱を流せば応力が生じる」  
> パッケージ設計は“力と熱の結びつき”を意識した設計図に進化する。

> “Heat always brings stress.”  
> Packaging design must evolve to reflect the coupled relationship of **thermal and mechanical** domains.

---

## 🔗 関連節｜Linked Sections

- [`f2a_3_thermal.md`](f2a_3_thermal.md)：熱応力との連携設計
- [`f2a_5_emi_emc.md`](f2a_5_emi_emc.md)：接地構造と振動によるノイズ影響
- [`f2a_6_constraint_tradeoff.md`](f2a_6_constraint_tradeoff.md)：構造強度と放熱の設計トレードオフ

---

## 📎 参考資料｜References

- “JEDEC JESD22-A104C: Temperature Cycling Test”  
- “Thermo-Mechanical Reliability in 3D ICs,” IEEE CPMT  
- Jisso Reliability Handbook, Japan Electronics Packaging Institute  
- ANSYS Mechanical / ABAQUS FEM User Guides

---
