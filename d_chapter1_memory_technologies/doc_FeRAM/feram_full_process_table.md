---
layout: default
title: 📘 0.18µm FeRAM Process Flow — 完全版 
---

---

# 📘 0.18µm FeRAM Process Flow — 完全版 
*0.18µm FeRAM Process Flow — Full Version*

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)

> ⚠️ **注意 / Notice**  
> 本プロセスフローは、三溝真一による **構想・教育目的** の設計に基づいています。  
> 実在する製品・製造フロー・企業機密とは一切関係ありません。  
> *This process flow is a conceptual and educational design by **Shinichi Samizo**.  
> It is not related to any actual product, manufacturing process, or proprietary information.*

---

## 🟦 Part 1: FEOL + Salicide (*Front-End of Line*)  

---

### 🔹 素子分離 / *Isolation (STI)*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **FS-DP** | SiON保護膜堆積<br>*SiON protection film deposition* | Global | 界面保護<br>*Interface protection* | 200Å @ 700℃ | - |
| **FSN-DP** | STI用窒化膜堆積<br>*STI nitride deposition* | Field | 酸化防止キャップ<br>*Oxidation cap* | 1500Å @ 750℃ | - |
| **F-PH** | フォトリソグラフィ<br>*Photolithography* | Field | STIパターン定義<br>*STI pattern definition* | CD = 0.28µm | F |
| **F-ET** | エッチング（RIE等）<br>*Etching (RIE)* | Field | STI溝形成<br>*STI trench etching* | CD = 0.28µm | - |
| **F-DP** | STI酸化膜埋込<br>*STI oxide fill* | Field | トレンチフィル<br>*Trench fill* | Oxide 4000Å | - |
| **F-CMP** | STI CMP<br>*CMP planarization* | Field | 平坦化<br>*Planarization* | - | - |
| **PRE-OX** | 犠牲酸化膜形成<br>*Sacrificial oxidation* | Pre | 表面改質・汚染除去<br>*Surface treatment* | Dry OX ~80Å | - |

📘 **解説 / Explanation**  
- STIにより素子間の電気的絶縁を確保し、リークを防止。  
- PRE-OXで表面を再酸化して不純物除去と注入ダメージ修復を実施。  
*STI ensures electrical isolation between devices. PRE-OX improves the silicon surface before implantation.*  

---

### 🔹 ウェル形成 / *Well Formation*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **NWL-PH** | フォトリソ（N-Well）<br>*Lithography (N-Well)* | Well | N-Well定義<br>*N-Well definition* | - | NWL |
| **NWL-ION** | イオン注入<br>*Ion implantation* | Well | N-Well形成<br>*N-Well formation* | 800keV, 2E13 | - |
| **PWL-PH** | フォトリソ（P-Well）<br>*Lithography (P-Well)* | Well | P-Well定義<br>*P-Well definition* | - | PWL |
| **PWL-ION** | イオン注入<br>*Ion implantation* | Well | P-Well形成<br>*P-Well formation* | 200keV, 5E12 | - |

📘 **解説 / Explanation**  
- N/Pウェルを形成し、NMOSとPMOS領域を分離。  
- デュアルウェルにより基板バイアス制御を可能にし、寄生トランジスタを抑制。  
*N- and P-wells define NMOS/PMOS regions. Dual-well design enables substrate bias control and suppresses parasitic effects.*  

---

### 🔹 チャネル調整注入 / *Channel Doping*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **NCD-PH** | フォトリソ（1.8V NMOS） | CD | Nch領域定義 | - | NCD |
| **NCD-ION** | NMOSチャネル注入<br>*NMOS channel doping* | CD | Vth調整 | B, 50keV, 1E13 | - |
| **PCD-PH** | フォトリソ（1.8V PMOS） | CD | Pch領域定義 | - | PCD |
| **PCD-ION** | PMOSチャネル注入<br>*PMOS channel doping* | CD | Vth調整 | BF₂, 30keV, 1E13 | - |
| **NCD2-PH** | フォトリソ（3.3V NMOS） | CD | Nch再調整 | - | NCD2 |
| **NCD2-ION** | NMOSチャネル再注入 | CD | Vth調整 | B, 50keV, 1E13 | - |
| **PCD2-PH** | フォトリソ（3.3V PMOS） | CD | Pch再調整 | - | PCD2 |
| **PCD2-ION** | PMOSチャネル再注入 | CD | Vth調整 | BF₂, 30keV, 1E13 | - |

📘 **解説 / Explanation**  
- 低電圧(1.8V)用と高電圧(3.3V)用でチャネル注入を分け、閾値電圧を最適化。  
- デュアルチャネルマスクにより短チャネル効果を抑制。  
*Channel doping separated for 1.8V and 3.3V devices, optimizing threshold voltage. Dual masks help control short-channel effects.*  

---

### 🔹 ゲート形成 / *Gate Formation*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **G1-OX** | ゲート酸化 (第1段)<br>*Gate oxidation (G1)* | Gate | 初期酸化膜 | Dry OX 35Å | - |
| **G1-PH** | フォトリソ（3.3V保護） | Gate | レジスト保護 | - | G1 |
| **G1-ET** | 酸化膜除去 (1.8V領域) | Gate | G1膜除去 | HF/SPM | - |
| **G2-OX** | ゲート酸化 (第2段) | Gate | 再酸化 | Dry OX 35Å | - |
| **PLY-DP** | ポリSi堆積 | Gate | ゲート電極 | LPCVD 1500Å | - |
| **PLY-PH** | フォトリソ（ゲート） | Gate | パターン定義 | KrF, CD=0.18µm | PLY |
| **PLY-ET** | ポリゲートエッチング | Gate | ゲート形成 | RIE, CD=0.18µm | - |

📘 **解説 / Explanation**  
- 逆Tox方式を導入し、1.8Vデバイスは35Å、3.3Vは70Å酸化膜を確保。  
- ゲート電極はポリSiで形成、KrF露光による0.18µmパターン。  
*Inverse Tox scheme: 35Å oxide for 1.8V, 70Å for 3.3V. Poly-Si gate patterned at 0.18µm by KrF lithography.*  

---

### 🔹 LDD・S/D形成 / *LDD & Source/Drain*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **NLL/PLL-PH** | フォトリソ（1.8V LDD） | LDD | LDD定義 | - | NLL/PLL |
| **NLL/PLL-ION** | NMOS/PMOS LDD注入 | LDD | 浅拡散形成 | As/BF₂ | - |
| **NLM/PLM-PH** | フォトリソ（3.3V LDD） | LDD | LDD定義 | - | NLM/PLM |
| **NLM/PLM-ION** | NMOS/PMOS LDD注入 | LDD | 浅拡散形成 | As/BF₂ | - |
| **SW-DP** | スペーサ堆積 | Gate | LDD保護 | SiN, 800Å | - |
| **SW-ET** | スペーサエッチング | Gate | アニソトロピック形成 | RIE | - |
| **NLL2/PLL2-PH** | フォトリソ（1.8V深拡散） | S/D | ソース・ドレイン定義 | - | NLL2/PLL2 |
| **NLL2/PLL2-ION** | NMOS/PMOS深拡散注入 | S/D | ソース・ドレイン形成 | As/BF₂, 40keV | - |
| **NLM2/PLM2-PH** | フォトリソ（3.3V深拡散） | S/D | ソース・ドレイン定義 | - | NLM2/PLM2 |
| **NLM2/PLM2-ION** | NMOS/PMOS深拡散注入 | S/D | ソース・ドレイン形成 | As/BF₂, 40keV | - |

📘 **解説 / Explanation**  
- LDDでホットキャリア劣化を抑制し、スペーサで拡散領域を制御。  
- 最終的に深拡散注入でソース・ドレインを完成。  
*LDD reduces hot-carrier degradation, spacers control diffusion, and deep implants complete S/D formation.*  

---

### 🔹 サリサイド形成 / *Salicide Formation (CoSi₂)*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **CO-SP** | Coスパッタ<br>*Co sputtering* | Salicide | 前駆体形成<br>*Precursor layer* | - | - |
| **LMP-ANL** | サリサイドアニール<br>*Salicide annealing* | Salicide | CoSi形成<br>*CoSi formation* | 550℃, 30s | - |
| **CO-ET** | 酸エッチング<br>*Acid etching* | Salicide | 未反応Co除去<br>*Remove unreacted Co* | H₂SO₄系 | - |
| **LMP2-ANL** | 相転移アニール<br>*Phase annealing* | Salicide | CoSi₂形成<br>*CoSi₂ formation* | 750℃, 30s | - |

📘 **解説 / Explanation**  
- サリサイドでソース・ドレイン・ゲートの抵抗を低減。  
- 2段階アニールでCo → CoSi → CoSi₂へ相転移制御。  
- 未反応Coは酸処理で除去し、リークを防止。  
*Salicide reduces S/D and gate resistance. Two-step annealing controls Co → CoSi → CoSi₂ transition. Acid etching removes unreacted Co.*  

---

## 🟩 Part 2: Capacitor + BEOL (*Back-End of Line*)  

---

### 🔹 ILD & Contact Formation (*F2-DP〜Via*)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **F2-DP** | ILD堆積<br>*ILD deposition* | ILD | 配線前絶縁膜<br>*Pre-interconnect insulation* | PE-TEOS, 6000Å | - |
| **F2-CMP** | CMP平坦化<br>*CMP planarization* | CMP | 表面平坦化<br>*Surface planarization* | CMP | - |
| **CNT-PH/ET** | フォト＋エッチ<br>*Lithography + Etching* | Contact | コンタクト開口形成<br>*Contact hole formation* | CD = 0.24µm | CNT |
| **TIN-SP** | TiNスパッタ<br>*TiN sputtering* | Barrier | バリアメタル形成<br>*Barrier metal* | DC sputter, 300Å | - |
| **CW-DP** | Wデポジション<br>*W deposition* | Plug | Wプラグ充填<br>*W plug filling* | CVD, WF₆, 4000Å | - |
| **CW-CMP** | W CMP<br>*W CMP planarization* | CMP | 平坦化<br>*Planarization* | CMP | - |

📘 **解説 / Explanation**  
ILDで絶縁を確保し、Wプラグで下層デバイスとの電気的接続を確立。TiNバリアでW拡散を防止。  
*ILD provides insulation; W plugs connect devices to interconnects. TiN barrier prevents tungsten diffusion.*  

---

### 🔹 Capacitor Formation (*Pt/PZT/Ti + AlOx*)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **TI1-SP** | Tiスパッタ | Capacitor | Pt下地密着層<br>*Adhesion for Pt* | 300Å | - |
| **Pt-SP** | Ptスパッタ | Capacitor | 下部電極形成<br>*Bottom electrode* | 1500Å | - |
| **PZT-COT** | PZTスピンコート | Capacitor | 強誘電体前駆体<br>*Ferroelectric precursor* | Sol-Gel, 1000Å | - |
| **PZT-ANL** | PZTアニール | Capacitor | ペロブスカイト結晶化<br>*Perovskite crystallization* | RTA, 650℃ O₂ | - |
| **TI2-SP** | Tiスパッタ | Capacitor | 上部電極バッファ<br>*Top electrode buffer* | 300Å | - |
| **CAP-PH/ET** | フォト＋イオンミリング | Capacitor | キャパシタパターニング<br>*Capacitor patterning* | KrF, CD=0.35µm | CAP |
| **ALOX-SP/DP** | AlOxスパッタ＋ALD | Capacitor | 保護膜（二重構造）<br>*Protective film (dual)* | 各300Å | - |
| **ALOX-PH/ET** | フォト＋エッチ | Capacitor | 接続開口形成<br>*Opening formation* | KrF, 0.35µm | ALOX |

📘 **解説 / Explanation**  
- **Pt/PZT/Ti** 構造でFeRAMセルを形成。  
- **PZTアニール (650℃ O₂)** によりペロブスカイト結晶化を達成。  
- **AlOx保護膜（二重：スパッタ＋ALD）**で水素還元劣化を防止。  
- **PtはCMP困難のためIBE**でパターニング。  
*Pt/PZT/Ti capacitor is core of FeRAM. PZT crystallized via O₂ anneal. Dual AlOx prevents H₂ degradation. Pt patterned using IBE instead of CMP.*  

---

### 🔹 BEOL Interconnects (M1〜M3)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **HLX-DP〜HWX-CMP** | ILD-0, Via-0, Wプラグ形成 | Interconnect | Capacitor-M1接続 | CD=0.24µm | HLX |
| **ALA-SP/PH/ET** | Metal-1 Al配線形成 | Metal-1 | セル配線<br>*Cell wiring* | 0.28µm, 6000Å | ALA |
| **HLA-DP〜HWA-CMP** | ILD-1, Via-1, Wプラグ形成 | Interconnect | M1-M2接続 | CD=0.24µm | HLA |
| **ALB-SP/PH/ET** | Metal-2 Al配線形成 | Metal-2 | 中間配線<br>*Intermediate wiring* | 0.35µm, 6000Å | ALB |
| **HLB-DP〜HWB-CMP** | ILD-2, Via-2, Wプラグ形成 | Interconnect | M2-M3接続 | CD=0.28µm | HLB |
| **ALC-SP/PH/ET** | Metal-3 Al配線形成 | Metal-3 | グローバル配線<br>*Global wiring* | 0.50µm, 8000Å | ALC |

📘 **解説 / Explanation**  
- BEOLは **M1〜M3の3層Al配線**で構成。  
- 各層は **Wプラグ＋ILD**で接続される。  
- **M1: セル配線, M2: 中間配線, M3: グローバル配線**。  
- **CMP**により段差を抑制。  
*BEOL uses 3 layers of Al interconnects. W plugs + ILD ensure reliable connections. M1 for cells, M2 for intermediate, M3 for global wiring. CMP controls planarity.*  

---

### 🔹 Pad & Passivation  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition | Mask |
|---------------|--------------------|-----------------|----------------|------------------|------|
| **ALD-SP/PH/ET** | Al厚膜パッド形成<br>*Thick Al pad formation* | Pad | Bond Pad作製<br>*Bond pad formation* | 3.0µm, 10000Å | PAD |
| **PAD-DP** | パッシベーション膜堆積<br>*Passivation deposition* | Passivation | 環境保護<br>*Environmental protection* | SiN+SiO₂, 8000Å | - |
| **PAD-PH/ET** | フォト＋エッチ<br>*Lithography + Etching* | Passivation | I/O開口形成<br>*Opening formation* | CD=3.0µm | PAD |

📘 **解説 / Explanation**  
- **厚膜Alパッド**でワイヤボンディング・フリップチップ接続に対応。  
- **パッシベーション膜 (SiN+SiO₂)** で湿気・Na拡散を防ぎ、長期信頼性を確保。  
- **通常プロセスでは最終工程に水素シンターを含めるが、本フローではPZT水素還元劣化を防ぐため削除。**  
*Thick Al pads support bonding. SiN+SiO₂ passivation ensures long-term reliability.  
Normally a final hydrogen sintering step is included, but here it is omitted to avoid hydrogen-induced degradation of PZT.*  

---

### 🔹 E-Test  

| 工程名 / Step | 内容 / Details |
|---------------|----------------|
| **E-TEST** | Vth, Ioff, FeRAM保持・書込特性を最終ウェハで測定<br>*Wafer-level measurement of Vth, Ioff, FeRAM retention & write characteristics* |

📘 **解説 / Explanation**  
最終テストでCMOS特性とFeRAM特性を同時に評価。  
*Final wafer test verifies both CMOS and FeRAM characteristics.*  
