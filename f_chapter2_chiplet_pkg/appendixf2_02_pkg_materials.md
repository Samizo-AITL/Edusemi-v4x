# 📘 Appendix 2.2：先端パッケージを支える材料技術  
# 📘 Appendix 2.2: Materials Supporting Advanced Packaging

---

本補足資料では、2.5D/3Dパッケージに使用される**主要材料とその役割**を解説します。  
Material choices directly affect **thermal behavior, signal integrity, and reliability** in 2.5D/3D packages.

---

## 🧱 基板・インターポーザ材料  
## 🧱 Substrate and Interposer Materials

| 材料 / Material | 用途 / Application | 特徴 / Characteristics |
|------------------|---------------------|--------------------------|
| **Siインターポーザ**<br>Silicon Interposer | 高密度配線層<br>High-density routing | CTE小、微細配線、コスト高<br>Low CTE, fine pitch, costly |
| **有機基板（ABF）**<br>Organic Substrate (ABF) | パッケージ基板<br>Package base | 樹脂系、低コスト、大面積対応<br>Resin-based, cost-effective, large area |
| **ガラス基板**<br>Glass Substrate | 次世代パッケージ基板<br>Next-gen substrate | 高平坦性、高周波特性、脆性あり<br>Flat, RF-friendly, brittle |

---

## ⚙️ 配線・導体材料  
## ⚙️ Conductor and Metallization Materials

| 材料 / Material | 用途 / Application | 特徴 / Characteristics |
|------------------|---------------------|--------------------------|
| **銅（Cu）**<br>Copper | 配線、TSV、バンプ<br>Wiring, TSV, bump | 高導電率、酸化防止にキャップ必要<br>Excellent conductivity, needs capping |
| **金（Au）**<br>Gold | ワイヤ、バンプ<br>Wire, bump | 化学安定、非常に高価<br>Chemically stable, very expensive |
| **アルミ（Al）**<br>Aluminum | パッド、旧世代配線<br>Pad, legacy wiring | 酸化しやすい、主に旧技術向け<br>Oxidizes easily, older processes |
| **ニッケル（Ni）**<br>Nickel | UBM、バリア層<br>UBM, barrier layer | 拡散防止、硬度高、濡れ性良好<br>Hard, diffusion barrier, solderable |
| **SnAgはんだ**<br>SnAg Solder | バンプ、接続部<br>Bump, joints | Pbフリー、熱疲労に注意<br>Lead-free, thermal fatigue sensitive |

---

## 🧪 絶縁・封止材料  
## 🧪 Insulating and Encapsulation Materials

| 材料 / Material | 用途 / Application | 特徴 / Characteristics |
|------------------|---------------------|--------------------------|
| **SiO₂** | 配線・TSV絶縁<br>Dielectric for wires/TSV | 高絶縁性、熱伝導中程度<br>Good insulation, moderate thermal |
| **SiN / SiCN** | 拡散バリア、キャップ層<br>Barrier and cap | 密着性・バリア性良、応力注意<br>Adhesive, stress-prone |
| **ポリイミド（PI）**<br>Polyimide | RDL絶縁膜<br>RDL dielectric | 低誘電率、柔軟、吸湿あり<br>Low-k, flexible, moisture-sensitive |
| **エポキシ樹脂**<br>Epoxy Resin | 封止材（モールド）<br>Encapsulation mold | 安価・成形性良、熱伝導低め<br>Cheap, moldable, low thermal conduction |

---

## ❄️ 熱対策材料  
## ❄️ Thermal Management Materials

| 材料 / Material | 用途 / Application | 特徴 / Characteristics |
|------------------|---------------------|--------------------------|
| **サーマルビア（Cu-TSV）**<br>Thermal Vias | 熱拡散用TSV<br>Heat spreading | 高熱伝導、構造設計重要<br>High thermal conductivity, layout-sensitive |
| **TIM（Thermal Interface Material）** | チップ～ヒートシンク間<br>Die-to-heatsink | グリース・ゲル・硬化タイプ等あり<br>Grease, gel, curing types available |
| **ヒートスプレッダ**<br>Heat Spreader | パッケージ外部上面<br>Package surface | Al/Cu製、放熱＋物理保護<br>Metal (Al, Cu), spreads heat, protects die |

---

## 📌 まとめ / Summary

材料選定はパッケージングにおける**性能・信頼性・コストの三位一体要素**であり、特に**異種材料の界面・CTE差**への対応が重要です。  
Material selection is a key balance of **performance, reliability, and cost** — especially critical in managing **material interfaces and CTE mismatch** in heterogeneous integration.

---
