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

## 🔹 Step 11：層間絶縁膜（ILD）形成 / Interlayer Dielectric (ILD) Deposition

**目的 / Purpose**：  
配線層とトランジスタを絶縁する層間膜を形成  
Form interlayer dielectric to insulate interconnects from the transistor layer

**条件 / Conditions**：  
- SiO₂ または SiCOH（k ≈ 2.7–3.0）、PECVDまたはSACVD  
- 膜厚：300–500 nm  
- SiO₂ or SiCOH (k ≈ 2.7–3.0), deposited via PECVD or SACVD  
- Thickness: 300–500 nm

**技術ポイント / Technical Notes**：  
- 平坦性・低応力・欠陥フリーが必要  
- **Planarity**, **low mechanical stress**, and **zero defects** are critical

---

## 🔹 Step 12：コンタクトホールエッチング / Contact Hole Etch

**目的 / Purpose**：  
S/Dまたはゲート電極への接続のためにコンタクト孔を形成  
Form contact holes to connect S/D or gate to upper metal layers

**条件 / Conditions**：  
- 193nm ArF露光、CH₄/O₂ またはフルオロカーボン系RIE  
- CD（線幅）：30–50 nm  
- 193nm ArF lithography, CH₄/O₂ or FC-based plasma RIE  
- CD: 30–50 nm

**技術ポイント / Technical Notes**：  
- **シリサイド露出の完全性**が接続抵抗に直結  
- Full **silicide exposure** is crucial for low contact resistance

---

## 🔹 Step 13：バリア/シード層堆積（コンタクト） / Barrier & Seed Deposition (Contact)

**目的 / Purpose**：  
Cu電解めっきに備えてバリア層と導電シード層を形成  
Form barrier and conductive seed layers for Cu electroplating

**条件 / Conditions**：  
- TaN または TiN（ALD）、Cuシード（PVD）  
- バリア厚：5–10 nm、シード厚：~50 nm  
- TaN or TiN (ALD), Cu seed (PVD)  
- Barrier: 5–10 nm, Seed: ~50 nm

**技術ポイント / Technical Notes**：  
- 被覆不良やボイドは**オープン不良の主要因**  
- Poor coverage or voids lead to **open failures**

---

## 🔹 Step 14：銅電解めっき（コンタクト） / Cu Electroplating for Contact

**目的 / Purpose**：  
コンタクト孔を銅で充填（Cu Fill）  
Fill contact vias with copper by electroplating

**条件 / Conditions**：  
- 酸性CuSO₄浴、電流密度：10–30 mA/cm²  
- 充填厚：200–400 nm（オーバーフィル）  
- Acidic CuSO₄ bath, 10–30 mA/cm²  
- Thickness: 200–400 nm (overfill)

**技術ポイント / Technical Notes**：  
- **添加剤制御**により均一・ボイドレス埋込が可能  
- Use of additives enables **uniform, void-free fill**

---

## 🔹 Step 15：コンタクトCMP / CMP of Contacts

**目的 / Purpose**：  
過剰銅を研磨除去し、平坦な接続面を形成  
Remove excess Cu and planarize the surface for interconnect

**条件 / Conditions**：  
- Al₂O₃ または SiO₂ スラリー  
- モーター電流 or 光学モニタによるエンドポイント制御  
- Alumina or SiO₂ slurry, endpoint detected by motor current or optical methods

**技術ポイント / Technical Notes**：  
- **ILDダメージの最小化**と**残膜制御（<5 nm）**が重要  
- Minimize **ILD damage** and control **residual film <5 nm**

---

## 🔹 Step 16：第1層配線堆積・パターニング（M1） / First Metal (M1) Deposition & Patterning

**目的 / Purpose**：  
M1配線とビア構造を形成（配線インフラの基礎）  
Form first metal layer (M1) interconnects and vias

**条件 / Conditions**：  
- ArF immersionまたはEUVリソグラフィ  
- Dual Damascene構造、CD：20–30 nm  
- ArF immersion or EUV lithography  
- Dual Damascene, CD: 20–30 nm

**技術ポイント / Technical Notes**：  
- **RC最小化設計**と寄生抑制が必須  
- Requires **RC minimization** and **parasitic suppression**

---

## 🔹 Step 17：M1–M2層間絶縁膜堆積 / ILD Deposition (M1–M2)

**目的 / Purpose**：  
M1とM2間の絶縁層を形成  
Form ILD between M1 and M2 layers

**条件 / Conditions**：  
- Low-k SiCOH（k ≈ 2.5–3.0）、PECVD  
- 膜厚：300–500 nm  
- Low-k SiCOH (k ≈ 2.5–3.0), PECVD, Thickness: 300–500 nm

**技術ポイント / Technical Notes**：  
- **低誘電率**と**機械的強度**のバランスが重要  
- Balance between **low-k** and **mechanical robustness**

---

## 🔹 Step 18：M2配線/ビアパターニング / Lithography & Etch for M2

**目的 / Purpose**：  
M2の配線パターンとビアを形成  
Define M2 wiring and via structures

**条件 / Conditions**：  
- ArF immersionまたはEUV  
- フルオロカーボン系RIE、CD ≈ 20–30 nm  
- ArF immersion or EUV, FC-based RIE, CD: 20–30 nm

**技術ポイント / Technical Notes**：  
- **オーバーレイ精度**と寸法均一性の確保が重要  
- Ensure **overlay accuracy** and **CD uniformity**

---

## 🔹 Step 19：M2 バリア・シード堆積 / Barrier & Seed Deposition for M2

**目的 / Purpose**：  
電解めっき用のバリア層＋シード層形成  
Form barrier and seed layers for Cu ECP

**条件 / Conditions**：  
- Ta/TaN（ALD）、Cuシード（PVD）  
- 膜厚：同上（バリア 5–10 nm、シード ~50 nm）  
- Ta/TaN (ALD), Cu seed (PVD), same thickness as previous steps

**技術ポイント / Technical Notes**：  
- ビア底部への**コンフォーマル堆積性**が鍵  
- Critical to achieve **conformal deposition** at via bottom

---

## 🔹 Step 20：M2銅電解めっき / Cu Electroplating for M2

**目的 / Purpose**：  
M2配線層への銅充填  
Fill M2 wiring and vias with copper

**条件 / Conditions**：  
- CuSO₄浴、添加剤制御  
- 厚さ：200–400 nm（オーバーフィル）  
- CuSO₄ bath with additive control  
- Thickness: 200–400 nm (overfill)

**技術ポイント / Technical Notes**：  
- パターン密度による**局所電流制御**が重要  
- Requires **localized current control** based on pattern density

---

## 🔹 Step 21：M2 CMP（平坦化） / CMP of M2 Cu Layer

**目的 / Purpose**：  
M2の表面を平坦化し、次工程のリソ精度を確保  
Planarize M2 top surface for next lithography

**条件 / Conditions**：  
- 同様のCMP条件（スラリー、圧力、速度）  
- 表面粗さ < 0.5 nm RMS  
- Similar CMP process, surface roughness < 0.5 nm RMS

**技術ポイント / Technical Notes**：  
- 次工程との**整合性（overlay）**確保に直結  
- Direct impact on **overlay precision** for next litho steps

---
