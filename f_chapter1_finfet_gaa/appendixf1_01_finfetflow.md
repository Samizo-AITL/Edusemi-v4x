# 🧬 補足資料 / Appendix：FinFET 製造プロセスフロー（全48ステップ）  
**FinFET Full Process Flow – 48-Step Breakdown for Advanced Nodes**

本資料では、FinFET（Fin型トランジスタ）の製造プロセスを48ステップに分解し、各ステップの**目的・条件・技術ポイント**を詳細に解説します。  
This document describes the full FinFET manufacturing flow, broken into **48 steps** with detailed **purpose, conditions, and key technical notes** for each.

---

## 📘 基本情報 / Basic Information

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **対象ノード / Target Node** | 10–5nm 世代 / 10–5nm generation |
| **基板仕様 / Substrate** | 300mm P-type Si (100), ~10 Ω·cm |
| **目的 / Objective** | プレーナMOSを超える短チャネル制御とゲート制御性の実現<br>Enhanced short-channel control beyond planar CMOS |

---

## 🧩 プロセスセグメント構成 / Process Segment Structure

| セグメント / Segment | ステップ範囲 / Step Range | 内容 / Description |
|-----------------------|----------------------------|---------------------|
| ① **初期工程 / Initial Process** | Step 1–3 | ウェル・STI形成 / Well & STI |
| ② **ゲート前形成 / Pre-Gate Formation** | Step 4–6 | ゲート酸化膜、ポリSi、パターニング |
| ③ **S/D構造 / Source/Drain Region** | Step 7–9 | 注入とスパーサ形成 / Implant & Spacer |
| ④ **シリサイド / Silicide** | Step 10 | Ni/Co系低抵抗コンタクト |
| ⑤ **ILD・コンタクト / Contact** | Step 11–15 | 絶縁膜、ビア、Cu配線形成 |
| ⑥ **M1層 / Metal-1** | Step 16–21 | 第1層配線プロセス |
| ⑦ **上位メタル / Upper Metals** | Step 22–26 | M2〜Mx多層形成 |
| ⑧ **パッシベーション / Passivation** | Step 27–30 | Cap層・UBM形成 |
| ⑨ **3D実装対応 / 3D Integration** | Step 31–35 | TSV、バンプ、上層ILD等 |
| ⑩ **テスト・実装 / Final Steps** | Step 36–48 | RC抽出、UBM再形成、パッケージング等 |

---

## 🎯 ドキュメントの目的 / Document Objective

- **教育目的**でFinFETのプロセス全体像を把握する  
  To provide **educational insight** into the full FinFET process.
- 各工程の**装置・材料・プロセス設計上の論点**を整理  
  Summarize **equipment, materials, and key process issues** at each step.
- GAAプロセスとの比較・教材リンクに連携  
  Link with GAA flow comparison and teaching materials.

---

## 📎 関連資料 / Related Files

- [`appendixf1_02_gaaflow.md`](./appendixf1_02_gaaflow.md)：GAA版プロセスフロー  
- [`f1_2_finfet.md`](./f1_2_finfet.md)：FinFET構造と動作解説  
- [`appendixf1_03_finfet_vs_gaa.md`](./appendixf1_03_finfet_vs_gaa.md)：FinFETとGAAの比較

---

## 🖼️ 図版予定 / Planned Figures

- `images/finfet_process_overview.png`：全体フロー図  
- `images/finfet_metallization_stack.png`：配線層構成断面図  
- `images/finfet_final_test_packaging.png`：後工程とパッケージ構造

---

## 👤 著者・ライセンス / Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

⬇️ 以下、各ステップの詳細解説へ続きます。  
⬇️ Proceed to detailed descriptions of each step below.

---

## 🔹 Step 1：基板準備 / Substrate Preparation

**目的 / Purpose**：  
高純度シリコン基板を準備し、微細加工に備えた表面清浄度を確保  
Prepare high-purity Si wafers and ensure surface cleanliness for fine processing

**条件 / Conditions**：  
- P型 Si (100)、抵抗率 ~10 Ω·cm  
- RCA洗浄 → 150°C 脱水ベーク  
- P-type Si (100), ~10 Ω·cm  
- RCA clean → 150°C dehydration bake

**技術ポイント / Technical Notes**：  
- 微細Fin形成に向けた**表面平坦性と金属残渣除去**が極めて重要  
- Critical to ensure **surface smoothness** and **removal of metal contaminants** for Fin formation

---

## 🔹 Step 2：STI（浅溝絶縁）形成 / Shallow Trench Isolation (STI)

**目的 / Purpose**：  
隣接トランジスタ間を電気的に分離する絶縁溝を形成  
Form isolation trenches to electrically separate adjacent devices

**条件 / Conditions**：  
- ArF浸潤リソグラフィ → フッ素系RIE → TEOS CVD → CMP  
- ArF immersion lithography → Fluorine-based RIE → TEOS CVD → CMP

**技術ポイント / Technical Notes**：  
- トレンチ深さ ≒ 200 nm  
- STIストレスによる**しきい値シフト（Vth Shift）**への影響に注意  
- STI depth ≈ 200 nm  
- Attention to **Vth shift due to STI-induced stress**

---

## 🔹 Step 3：ウェル・チャネル形成 / Well and Channel Implantation

**目的 / Purpose**：  
n/pウェルの定義としきい値調整チャネルドーピングの導入  
Define n/p wells and implant channel dopants for Vth adjustment

**条件 / Conditions**：  
- B (p-well), As/P (n-well)：10¹²〜10¹³ cm⁻²、30〜80 keV  
- Rapid Thermal Annealing (RTA) による活性化  
- B (p-well), As/P (n-well): 10¹²–10¹³ cm⁻², 30–80 keV  
- Activation by RTA

**技術ポイント / Technical Notes**：  
- ウェル分布のばらつきが**Vth均一性**に影響  
- Variation in well doping affects **Vth uniformity**

---

## 🔹 Step 4：ゲート酸化膜形成 / Gate Oxide Growth

**目的 / Purpose**：  
ゲート絶縁膜として高品質な酸化膜を形成  
Form high-quality oxide as gate insulator

**条件 / Conditions**：  
- 乾式酸化：800–900°C、厚さ 1.5–2.0 nm  
- Dry oxidation at 800–900°C, thickness 1.5–2.0 nm

**技術ポイント / Technical Notes**：  
- **界面準位密度（Dit）**を抑えることがリーク・信頼性に重要  
- Reducing **interface trap density (Dit)** is crucial for leakage and reliability

---

## 🔹 Step 5：ポリSi堆積・ドーピング / Poly-Si Deposition and Doping

**目的 / Purpose**：  
ゲート電極となるポリシリコンを形成し、導電性を確保  
Deposit doped polysilicon for gate electrode to ensure conductivity

**条件 / Conditions**：  
- LPCVD（~100 nm）  
- In-situ P/Asドープ または イオン注入後アニール  
- LPCVD (~100 nm), In-situ P/As doping or post-implant annealing

**技術ポイント / Technical Notes**：  
- ポリSiの**粒界伝導**とドーピング均一性がスイッチング性能に影響  
- **Grain boundary conduction** and doping uniformity are key for switching behavior

---

## 🔹 Step 6：ゲートパターニング / Gate Patterning

**目的 / Purpose**：  
微細ゲート寸法（CD）を定義  
Define critical gate dimensions (CD) via lithography and etch

**条件 / Conditions**：  
- 193nm ArF immersion、HBr/Cl₂ベースのRIE  
- CD ≒ 30 nm（ノードに依存）  
- 193nm ArF immersion lithography, HBr/Cl₂-based RIE, CD ~30 nm

**技術ポイント / Technical Notes**：  
- CDのばらつきが**Vth・ドレイン電流**のばらつき要因となる  
- CD variation causes fluctuation in **Vth and drain current**

---

## 🔹 Step 7：S/D拡張注入 / S/D Extension Implantation

**目的 / Purpose**：  
短チャネル効果抑制のためのチャネル端軽度ドーピング  
Light doping at channel edge to suppress short-channel effects

**条件 / Conditions**：  
- BまたはAs、10¹³–10¹⁴ cm⁻²、5–20 keV  
- スパイクRTAで活性化  
- B or As: 10¹³–10¹⁴ cm⁻², 5–20 keV, activated by spike RTA

**技術ポイント / Technical Notes**：  
- 浅い接合で**リーク電流と抵抗のトレードオフ**を最適化  
- Optimize **leakage vs resistance** via shallow junction depth

---

## 🔹 Step 8：スペーサ形成 / Spacer Formation

**目的 / Purpose**：  
S/D本注入範囲を定義するスペーサ（サイドウォール）の形成  
Form sidewall spacers to define main S/D implant region

**条件 / Conditions**：  
- LPCVD Si₃N₄またはSiO₂（10–20 nm）  
- 異方性RIEによるエッチバック  
- LPCVD Si₃N₄ or SiO₂ (10–20 nm), anisotropic RIE etchback

**技術ポイント / Technical Notes**：  
- スペーサ幅のばらつきが**SDE長とR_on**に影響  
- Spacer width variation affects **SDE length and R_on**

---

## 🔹 Step 9：S/D本注入 / S/D Main Implant

**目的 / Purpose**：  
ソース・ドレイン領域に高濃度ドーピングを施し、低抵抗化  
Heavily dope S/D regions to reduce series resistance

**条件 / Conditions**：  
- AsまたはB：~10¹⁵ cm⁻²、30–80 keV  
- RTAで活性化  
- As or B: ~10¹⁵ cm⁻², 30–80 keV, activated by RTA

**技術ポイント / Technical Notes**：  
- 深すぎると**短チャネル効果増加**、浅すぎると**抵抗上昇**  
- Too deep increases **SCE**, too shallow increases **series resistance**

---

## 🔹 Step 10：シリサイド形成 / Silicide Formation

**目的 / Purpose**：  
ゲート・S/D領域に低抵抗金属シリサイドを形成  
Form low-resistance silicide at gate and S/D

**条件 / Conditions**：  
- PVD NiまたはCo → Rapid Anneal（400–600°C）→ 未反応金属除去  
- PVD Ni or Co → RTA (400–600°C) → remove unreacted metal

**技術ポイント / Technical Notes**：  
- **オーバーシリサイド（リーセッション）**や**短絡**を防止  
- Prevent **excess silicide recession** and **shorts**

---
