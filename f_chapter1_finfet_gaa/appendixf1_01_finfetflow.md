---
layout: default
title: 補足資料 / Appendix：FinFET 製造プロセスフロー（全48ステップ
---

---

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

## 🔹 Step 22：上位層間絶縁膜（ILD）堆積 / ILD Deposition (M2–Mx)

**目的 / Purpose**：  
M2以降の上層配線層を絶縁するための層間膜を形成  
Form ILD layers between upper metal layers from M2 to Mx

**条件 / Conditions**：  
- Low-k SiCOH（k ≈ 2.5–3.0）、PECVD法  
- 厚さ：300–500 nm  
- Low-k SiCOH (k ≈ 2.5–3.0), deposited via PECVD  
- Thickness: 300–500 nm

**技術ポイント / Technical Notes**：  
- **低誘電率**と**機械的強度**の両立が必須  
- Must balance **low dielectric constant** and **mechanical robustness**

---

## 🔹 Step 23：Mx配線・ビア形成 / Lithography & Etching for Mx

**目的 / Purpose**：  
Mx層の配線パターンおよびビアホールの形成  
Define metal patterns and vias for Mx layer

**条件 / Conditions**：  
- ArF immersion または EUV  
- フルオロカーボン系RIE、Dual Damascene構造  
- ArF immersion or EUV, FC-based RIE, Dual Damascene

**技術ポイント / Technical Notes**：  
- **高アスペクト比Viaの形成**およびCD均一性が重要  
- Ensure **high aspect ratio vias** and **critical dimension uniformity**

---

## 🔹 Step 24：Mxバリア・シード堆積 / Barrier & Seed Deposition (Mx)

**目的 / Purpose**：  
MxのCu埋込前にバリア層とシード層を形成  
Form barrier and seed layers prior to Cu fill for Mx

**条件 / Conditions**：  
- Ta/TaN（ALD）、Cuシード（PVD）  
- 膜厚：バリア5–10 nm、シード~50 nm  
- Ta/TaN (ALD), Cu seed (PVD), Barrier: 5–10 nm, Seed: ~50 nm

**技術ポイント / Technical Notes**：  
- Via底部や配線壁面への**コンフォーマル堆積性**が鍵  
- **Conformal coverage** on via bottom and trench walls is critical

---

## 🔹 Step 25：Mx銅電解めっき / Cu Electroplating (Mx)

**目的 / Purpose**：  
Mx層配線およびビアをCuで充填  
Fill metal lines and vias of Mx layer with Cu

**条件 / Conditions**：  
- 添加剤制御付き酸性CuSO₄浴  
- 厚さ：200–400 nm（オーバーフィル）  
- Acidic CuSO₄ bath with additives, Thickness: 200–400 nm (overfill)

**技術ポイント / Technical Notes**：  
- パターン密度に応じた**電流制御**が必要  
- Requires **current tuning** based on pattern density

---

## 🔹 Step 26：Mx層CMP / CMP of Mx Layers

**目的 / Purpose**：  
Mx層のCuオーバーフィルを除去し、平坦面を形成  
Remove Cu overfill and planarize the surface for next layers

**条件 / Conditions**：  
- アルミナ/SiO₂スラリー、ディッシング/エロージョン抑制設計  
- Alumina/SiO₂ slurry, Dishing/Erosion suppression techniques

**技術ポイント / Technical Notes**：  
- **ラインエッジ保護**および**微細構造保持**が重要  
- Critical to **protect line edges** and **preserve fine structures**

---

## 🔹 Step 27：キャップ層堆積 / Cap Layer Deposition

**目的 / Purpose**：  
Cuの拡散防止と機械的保護層（SiN、SiCNなど）を形成  
Form Cu diffusion barrier and mechanical cap layer (e.g., SiN, SiCN)

**条件 / Conditions**：  
- PECVDまたはLPCVD、厚さ：20–50 nm  
- PECVD or LPCVD, Thickness: 20–50 nm

**技術ポイント / Technical Notes**：  
- **ストレス低減**によりウェーハ反りを抑制  
- Low-stress films to suppress **wafer warpage**

---

## 🔹 Step 28：パッシベーション層形成 / Passivation Layer Deposition

**目的 / Purpose**：  
ウェーハ全体を保護する最終絶縁膜（SiN、SiO₂など）  
Form final passivation layer for chip protection (e.g., SiN, SiO₂)

**条件 / Conditions**：  
- PECVD、厚さ：0.5–1.0 µm、ピンホール無し  
- PECVD, Thickness: 0.5–1.0 µm, Pinhole-free

**技術ポイント / Technical Notes**：  
- **密着性と防湿性**が最重要パラメータ  
- Key parameters: **adhesion** and **moisture barrier**

---

## 🔹 Step 29：パッド開口リソグラフィ＆エッチ / Pad Opening Lithography and Etch

**目的 / Purpose**：  
UBM形成のためパッド部分を露出  
Open passivation above pad for UBM (Under Bump Metallization)

**条件 / Conditions**：  
- ArF露光 + F系RIE、UBM上層への影響最小化  
- ArF lithography + F-based RIE, Minimize damage to UBM

**技術ポイント / Technical Notes**：  
- **エッチング過剰でUBM損傷**しないよう制御  
- **Etch depth control** to prevent UBM damage

---

## 🔹 Step 30：UBM形成（バンプ下金属） / Under Bump Metallization (UBM)

**目的 / Purpose**：  
フリップチップ用のNiV/Cu/Au多層UBMを形成  
Form NiV/Cu/Au multilayer UBM for flip-chip bonding

**条件 / Conditions**：  
- PVD + 電解Ni/Cu/Au、合計厚さ：約5〜10 µm  
- PVD + Electroplating of Ni/Cu/Au, Total thickness: ~5–10 µm

**技術ポイント / Technical Notes**：  
- **濡れ性・信頼性・耐酸化性**のバランス設計が必須  
- Must balance **wetting**, **reliability**, and **oxidation resistance**

---

## 🔹 Step 31：上層ビア形成 / Via Formation for Upper Metal

**目的 / Purpose**：  
最上層配線層間の垂直ビアを形成（TSVや上位配線との接続）  
Form vertical vias for top-level metal interconnection or TSV

**条件 / Conditions**：  
- フルオロカーボン系RIE、CD：20〜30 nm、アスペクト比 > 2  
- Fluorocarbon-based RIE, CD: 20–30 nm, Aspect ratio > 2

**技術ポイント / Technical Notes**：  
- **高アスペクト比**かつ**エッチストップ層への正確な制御**が必要  
- Requires **high aspect ratio** and **precise etch-stop targeting**

---

## 🔹 Step 32：バリア・シード堆積（Via） / Barrier & Seed Deposition (Via)

**目的 / Purpose**：  
ビア内面を金属でコーティングし、電解めっきの導入準備  
Deposit barrier and seed layers inside vias for ECP

**条件 / Conditions**：  
- バリア：Ta/TaN（ALD）、シード：Cu（PVD）  
- Barrier: Ta/TaN (ALD), Seed: Cu (PVD)  
- 膜厚：バリア5–10 nm、シード約50 nm  
- Thickness: 5–10 nm (barrier), ~50 nm (seed)

**技術ポイント / Technical Notes**：  
- **コンフォーマル性**（特にVia底部への被覆性）が信頼性に直結  
- **Conformal coverage** at via bottom is essential for reliability

---

## 🔹 Step 33：ビア銅埋込 / Cu Electroplating (Via)

**目的 / Purpose**：  
Via空間をCuで充填し、低抵抗な縦方向接続を構築  
Fill via structures with Cu to enable low-resistance vertical connection

**条件 / Conditions**：  
- 酸性CuSO₄浴、電流密度制御付きECP  
- Acidic CuSO₄ bath, ECP with current control  
- 厚さ：200〜400 nm程度のオーバーフィル  
- Overfill: 200–400 nm

**技術ポイント / Technical Notes**：  
- **空隙（ボイド）防止**と**結晶制御**（柱状結晶抑制）が重要  
- Prevent **voiding** and control **grain structure** (avoid columnar crystals)

---

## 🔹 Step 34：ビア部CMP / CMP of Cu Via/Wiring

**目的 / Purpose**：  
ビア上部および配線部のCu過剰堆積を除去し平坦化  
Planarize Cu overfill in via and wiring regions for next steps

**条件 / Conditions**：  
- 銅選択CMP、スラリー：SiO₂またはAl₂O₃系、残膜<5 nm  
- Selective CMP for Cu, slurry: SiO₂ or Al₂O₃ based, Residue < 5 nm

**技術ポイント / Technical Notes**：  
- **ディッシング・エロージョン**の抑制と**上面均一性**が重要  
- Suppress **dishing/erosion** and ensure **uniform topography**

---

## 🔹 Step 35：上層ILD堆積 / Upper ILD Deposition

**目的 / Purpose**：  
3D構造の上部保護・絶縁膜を形成  
Deposit upper ILD for protection and insulation in 3D structure

**条件 / Conditions**：  
- SiCOHまたはSiO₂、PECVD、厚さ：300–500 nm  
- SiCOH or SiO₂, PECVD, Thickness: 300–500 nm

**技術ポイント / Technical Notes**：  
- **低誘電率**と**吸湿抑制**の両立設計  
- Balance **low-k property** and **moisture resistance**

---

## 🔹 Step 36：上層配線リソグラフィ / Lithography for Upper Metal

**目的 / Purpose**：  
上層配線（Mx+1）形成のためのパターン定義  
Define pattern for top-level interconnect (e.g., Mx+1)

**条件 / Conditions**：  
- ArF immersionまたはEUV露光、CD：~20–30 nm  
- ArF immersion or EUV lithography, CD: ~20–30 nm

**技術ポイント / Technical Notes**：  
- **LWR（Line Width Roughness）とOverlay誤差**の最小化が必須  
- Minimize **LWR and overlay errors** for high-density routing

---

## 🔹 Step 37：デュアルダマシンエッチ / Dual Damascene Etch

**目的 / Purpose**：  
上層ビアと配線溝を同時に形成  
Etch vias and trenches simultaneously (dual damascene)

**条件 / Conditions**：  
- フッ素系RIE、プロファイル：垂直、選択比制御  
- Fluorocarbon-based RIE, vertical profile, controlled selectivity

**技術ポイント / Technical Notes**：  
- **アスペクト比制御**と**過エッチ抑制**が重要  
- Control **aspect ratio** and avoid **over-etching**

---

## 🔹 Step 38：バリア・シード堆積（上層） / Barrier & Seed Deposition (Upper Metal)

**目的 / Purpose**：  
Cu ECP用の導電・拡散防止層形成  
Form conductive and barrier layers prior to Cu electroplating

**条件 / Conditions**：  
- Ta/TaN（ALD）、Cuシード（PVD）  
- Ta/TaN (ALD), Cu seed (PVD)  
- バリア膜厚：5–10 nm、シード：~50 nm  
- Barrier: 5–10 nm, Seed: ~50 nm

**技術ポイント / Technical Notes**：  
- **高密度パターン**に対しても**被覆均一性**を確保  
- Ensure **uniform coverage** even for **dense patterns**

---

## 🔹 Step 39：銅電解めっき（上層） / Cu Electroplating (Upper Metal)

**目的 / Purpose**：  
上層配線とビアを銅で埋込（低抵抗配線）  
Fill trenches and vias with Cu for low-resistance interconnect

**条件 / Conditions**：  
- 酸性CuSO₄浴、添加剤制御付きECP  
- Acidic CuSO₄ bath with additive-controlled ECP  
- オーバーフィル：~300–400 nm  
- Overfill: ~300–400 nm

**技術ポイント / Technical Notes**：  
- **空隙防止（ボイドレス）**と**柱状結晶の抑制**  
- Prevent **voids** and suppress **columnar crystal growth**

---

## 🔹 Step 40：上層Cu CMP / CMP of Upper Metal

**目的 / Purpose**：  
過剰堆積Cuの除去と表面平坦化  
Remove overfill Cu and planarize the top layer

**条件 / Conditions**：  
- CMP：アルミナまたはシリカ系スラリー、選択CMP  
- CMP: Alumina or silica slurry, selective CMP  
- 平坦度：< 0.5 nm RMS  
- Planarity: < 0.5 nm RMS

**技術ポイント / Technical Notes**：  
- **トップビュー均一性**と**次工程への影響最小化**  
- Ensure **uniform topography** and minimize impact on next steps

---

## 🔹 Step 41：RC抽出と寄生評価 / RC Extraction and Parasitic Evaluation

**目的 / Purpose**：  
配線の**抵抗（R）**・**容量（C）**を抽出し、回路性能（遅延・ノイズ）を評価  
Extract **resistance (R)** and **capacitance (C)** to evaluate delay and noise

**条件 / Conditions**：  
- レイアウト後EDAツールによるポストレイアウト解析  
- Post-layout extraction using EDA tools

**技術ポイント / Technical Notes**：  
- **RC delay < 60 ps/mm** を目標  
- Accurate extraction is critical for **timing sign-off**

---

## 🔹 Step 42：UBMパッド開口 / Pad Opening for UBM

**目的 / Purpose**：  
パッケージ接続用に**UBM（Under Bump Metallization）層**を露出  
Expose **UBM layer** for external packaging (flip-chip, etc.)

**条件 / Conditions**：  
- ArFスキャナー + RIEによる開口、精密アライメント制御  
- ArF scanner lithography + RIE, precise alignment control

**技術ポイント / Technical Notes**：  
- **UBM損傷を回避**するため、エッチング深さ制御が必須  
- Avoid **over-etching** to prevent UBM damage

---

## 🔹 Step 43：UBM再形成（NiV / Cu / Au） / Final UBM Formation (NiV / Cu / Au)

**目的 / Purpose**：  
パッケージング強度・接続信頼性向上のため**UBM金属層を追加形成**  
Enhance bump adhesion and reliability by adding UBM stack

**条件 / Conditions**：  
- PVD（NiV）＋電解Cu/Auめっき、合計厚み：~10 µm  
- NiV by PVD + Cu/Au electroplating, total thickness ~10 µm

**技術ポイント / Technical Notes**：  
- **Snバンプとの濡れ性**や**界面拡散**への耐性を確保  
- Ensure good **wetting with solder bump** and **diffusion barrier**

---

## 🔹 Step 44：ウェーハ薄化 / Wafer Thinning

**目的 / Purpose**：  
3D実装や放熱性向上のため、**ウェーハを薄化（~100 µm以下）**  
Thin the wafer to **~100 µm or less** for better 3D stacking and thermal performance

**条件 / Conditions**：  
- バックグラインディング（BG）→ CMP  
- Back grinding followed by CMP

**技術ポイント / Technical Notes**：  
- **反り・割れ防止**と厚み均一性が重要  
- Maintain **uniformity** and avoid **warping/cracking**

---

## 🔹 Step 45：TSV / マイクロバンプ形成 / TSV & Micro-Bump Formation

**目的 / Purpose**：  
3D IC実装のため、**垂直TSV（Through-Silicon Via）と微細バンプ**を形成  
Form **TSVs and micro-bumps** for 3D chip stacking and packaging

**条件 / Conditions**：  
- TSV：DRIEエッチ → 絶縁膜 → バリア/シード → Cu ECP  
- Bump：SnAgまたはPbフリー電解めっき  
- TSV: DRIE etch → dielectric → barrier/seed → Cu ECP  
- Bump: SnAg or lead-free electroplating

**技術ポイント / Technical Notes**：  
- **ボイド・割れ**のない完全埋込と**接続信頼性**が鍵  
- Ensure **void-free filling** and **reliable bump formation**

---

## 🔹 Step 46：最終パッシベーション / Final Passivation

**目的 / Purpose**：  
完成チップを**湿気・機械ダメージ**から保護  
Protect die from **moisture and mechanical damage**

**条件 / Conditions**：  
- SiNまたはSiO₂を**PECVD**で成膜、厚さ0.5–1.0 µm  
- Deposit SiN or SiO₂ by PECVD, thickness: 0.5–1.0 µm

**技術ポイント / Technical Notes**：  
- **ピンホールなし**・低ストレスが必須条件  
- Must ensure **no pinholes** and **low film stress**

---

## 🔹 Step 47：ウェーハテスト・ダイシング / Wafer Test & Dicing

**目的 / Purpose**：  
チップ単位で**電気テスト**と**切断**を実施  
Perform **electrical testing** and **dicing** per die

**条件 / Conditions**：  
- ATEによるリーク・速度・論理検査 → レーザーダイシングまたはソーイング  
- ATE for leakage, speed, logic → laser or saw dicing

**技術ポイント / Technical Notes**：  
- **歩留まり分析**と**トレーサビリティ**保持が重要  
- Ensure **yield analysis** and **traceability**

---

## 🔹 Step 48：パッケージング / Final Packaging

**目的 / Purpose**：  
**実装形態（FC-CSP, FOWLPなど）**で製品化  
Package into product form: **FC-CSP, FOWLP, etc.**

**条件 / Conditions**：  
- ダイアタッチ → ワイヤボンディングまたはバンプ → モールド → アンダーフィル  
- Die attach → wire bond or flip-chip bump → mold → underfill

**技術ポイント / Technical Notes**：  
- **熱管理・信頼性・量産性**の設計バランスが鍵  
- Balance **thermal design**, **reliability**, and **manufacturability**

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)
