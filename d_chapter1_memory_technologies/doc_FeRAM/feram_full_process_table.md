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

## 🟦 Part 1: FEOL (*Front-End of Line*)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 処理条件 / Condition | 寸法 / CD | 膜厚 / Thickness | Mask |
|---------------|--------------------|-----------------|----------------|----------------------|-----------|------------------|------|
| **FS-DP** | SiON保護膜堆積<br>*SiON protection film deposition* | 全体 / Global | 界面保護<br>*Interface protection* | 200Å @ 700℃ | - | - | - |
| **FSN-DP** | STI用窒化膜堆積<br>*STI nitride deposition* | Field | 酸化防止キャップ<br>*Oxidation cap* | 1500Å @ 750℃ | - | - | - |
| **F-PH** | フォトリソグラフィ<br>*Photolithography* | Field | パターン定義<br>*Patterning* | - | 0.28µm | - | F |
| **F-ET** | エッチング（RIE等）<br>*Etching (RIE)* | Field | パターン転写<br>*Pattern transfer* | - | 0.28µm | - | - |
| **F-DP** | STI酸化膜埋込<br>*STI oxide fill* | Field | トレンチフィル<br>*Trench fill* | - | - | 4000Å | - |
| **F-CMP** | STI CMP<br>*CMP planarization* | Field | 平坦化<br>*Planarization* | - | - | - | - |
| **PRE-OX** | 犠牲酸化膜形成<br>*Sacrificial oxidation* | 前処理 / Pre | 表面改質・汚染除去<br>*Surface treatment* | Dry OX ~80Å | - | 80Å | - |
| **NWL-PH** | フォトリソ（N-Well）<br>*Lithography (N-Well)* | Well | N-Well定義<br>*N-Well definition* | - | - | - | NWL |
| **NWL-ION** | イオン注入<br>*Ion implantation* | Well | N-Well形成<br>*N-Well formation* | 800keV, 2E13 | - | - | - |
| **PWL-PH** | フォトリソ（P-Well）<br>*Lithography (P-Well)* | Well | P-Well定義<br>*P-Well definition* | - | - | - | PWL |
| **PWL-ION** | イオン注入<br>*Ion implantation* | Well | P-Well形成<br>*P-Well formation* | 200keV, 5E12 | - | - | - |
| **NCD-PH** | フォトリソ（1.8V NMOS） | CD | Nch領域定義 | - | 1.8V | - | NCD |
| **NCD-ION** | NMOSチャネル注入<br>*NMOS channel doping* | CD | Vth調整 | B, 50keV, 1E13 | 1.8V | - | - |
| **PCD-PH** | フォトリソ（1.8V PMOS） | CD | Pch領域定義 | - | 1.8V | - | PCD |
| **PCD-ION** | PMOSチャネル注入<br>*PMOS channel doping* | CD | Vth調整 | BF₂, 30keV, 1E13 | 1.8V | - | - |
| **NCD2-PH** | フォトリソ（3.3V NMOS） | CD | Nch再調整 | - | 3.3V | - | NCD2 |
| **NCD2-ION** | NMOSチャネル再注入 | CD | Vth調整 | B, 50keV, 1E13 | 3.3V | - | - |
| **PCD2-PH** | フォトリソ（3.3V PMOS） | CD | Pch再調整 | - | 3.3V | - | PCD2 |
| **PCD2-ION** | PMOSチャネル再注入 | CD | Vth調整 | BF₂, 30keV, 1E13 | 3.3V | - | - |
| **G1-OX** | ゲート酸化 (第1段)<br>*Gate oxidation (G1)* | Gate | 初期酸化膜 | Dry OX 35Å | 全MOS | 35Å | - |
| **G1-PH** | フォトリソ（3.3V保護） | Gate | レジスト保護 | - | 3.3V | - | G1 |
| **G1-ET** | 酸化膜除去 (1.8V領域) | Gate | G1膜除去 | HF/SPM | 1.8V | 0Å | - |
| **G2-OX** | ゲート酸化 (第2段) | Gate | 再酸化 | Dry OX 35Å | 1.8V | 35Å | - |
| **PLY-DP** | ポリSi堆積 | Gate | ゲート電極 | LPCVD | - | 1500Å | - |
| **PLY-PH** | フォトリソ（ゲート） | Gate | パターン定義 | KrF | 0.18µm | - | PLY |
| **PLY-ET** | ポリゲートエッチング | Gate | ゲート形成 | RIE | 0.18µm | - | - |
| **NLL/PLL-PH, ION** | NMOS/PMOS LDD注入 | LDD | 浅拡散形成 | As/BF₂ | 1.8V | - | - |
| **NLM/PLM-PH, ION** | NMOS/PMOS LDD注入 | LDD | 浅拡散形成 | As/BF₂ | 3.3V | - | - |
| **SW-DP, SW-ET** | スペーサ堆積＋エッチ | Gate | LDD保護 | LPCVD+RIE | - | 800Å | - |
| **NLL2/PLL2, NLM2/PLM2** | NMOS/PMOS深拡散注入 | S/D | ソース・ドレイン形成 | As/BF₂, 40keV | 1.8V/3.3V | - | - |

---

## 🟦 Part 2: Salicide Process  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 処理条件 / Condition | 寸法 / CD | 膜厚 / Thickness | Mask |
|---------------|--------------------|-----------------|----------------|----------------------|-----------|------------------|------|
| **CO-SP** | Coスパッタリング<br>*Co sputtering* | Salicide | 前駆体形成<br>*Precursor layer* | - | - | 300Å | - |
| **LMP-ANL** | サリサイドアニール<br>*Salicide annealing* | Salicide | CoSi形成<br>*CoSi formation* | 550℃ 30s | - | - | - |
| **CO-ET** | エッチング（RIE等）<br>*Etching (RIE)* | Salicide | 不要Co層除去<br>*Remove unreacted Co* | H₂SO₄系 | - | - | - |
| **LMP2-ANL** | 相転移アニール<br>*Phase transformation annealing* | Salicide | CoSi₂形成<br>*CoSi₂ formation* | 750℃ 30s | - | - | - |

## 🔍 解説 / Explanation  

- **CoSi₂ サリサイド形成**は、ソース・ドレイン・ゲートの低抵抗化に必須。  
  *Formation of CoSi₂ salicide is essential for reducing the resistance of source, drain, and gate.*  

- 2段階アニールにより、**Co → CoSi → CoSi₂**へと相転移を制御。  
  *Two-step annealing controls the phase transition from Co → CoSi → CoSi₂.*  

- **不要な未反応Co膜は酸処理で除去**し、素子間リークを防止。  
  *Unreacted Co film is removed by acid etching to prevent device leakage.*  

---

## 🟦 Part 3: Capacitor Formation (Pt/PZT/Ti + AlOx)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 処理条件 / Condition | 寸法 / CD | 膜厚 / Thickness | Mask |
|---------------|--------------------|-----------------|----------------|----------------------|-----------|------------------|------|
| **TI1-SP** | Tiスパッタリング<br>*Ti sputtering* | Capacitor | Ptとの密着層<br>*Adhesion layer for Pt* | DC Sputter, 300W, Ar | - | 300Å | - |
| **Pt-SP** | Ptスパッタリング<br>*Pt sputtering* | Capacitor | 下部電極形成<br>*Bottom electrode* | DC Sputter, 1kW, Ar | - | 1500Å | - |
| **PZT-COT** | PZTスピンコート<br>*PZT spin coating* | Capacitor | 強誘電体前駆体堆積<br>*Ferroelectric precursor deposition* | Sol-Gel, 3000rpm | - | 1000Å | - |
| **PZT-ANL** | PZTアニール<br>*PZT annealing* | Capacitor | ペロブスカイト結晶化<br>*Perovskite crystallization* | RTA, 650℃, O₂, 60s | - | - | - |
| **TI2-SP** | Tiスパッタリング<br>*Ti sputtering* | Capacitor | 上部電極バッファ<br>*Top electrode buffer* | DC Sputter, 300W, Ar | - | 300Å | - |
| **CAP-PH** | フォトリソグラフィ<br>*Photolithography* | Capacitor | キャパシタパターン定義<br>*Capacitor patterning* | KrF, 248nm | 0.35µm | - | CAP |
| **CAP-ET** | イオンミリング<br>*Ion milling (IBE)* | Capacitor | Pt/PZT/Tiパターニング<br>*Patterning of Pt/PZT/Ti stack* | Ion Beam Etch | 0.35µm | - | - |
| **ALOX-SP** | AlOxスパッタ<br>*AlOx sputtering* | Capacitor | PZT一次保護膜<br>*First protection layer* | RF Sputter, 400W, Ar/O₂ | - | 300Å | - |
| **ALOX-DP** | AlOx ALD堆積<br>*AlOx ALD deposition* | Capacitor | 高密度保護膜形成<br>*High-density protective film* | ALD, 200℃, TMA/H₂O | - | 300Å | - |
| **ALOX-PH** | フォトリソグラフィ<br>*Photolithography* | Capacitor | 接続開口パターン定義<br>*Contact via opening* | KrF, 248nm | 0.35µm | ALOX |
| **ALOX-ET** | エッチング（RIE）<br>*Etching (RIE)* | Capacitor | 開口形成<br>*Via hole formation* | BCl₃/Cl₂ | 0.35µm | - | - |

## 🔍 解説 / Explanation  

- **Pt/PZT/Ti 構造**は、FeRAMセルの中心構造。  
  *Pt/PZT/Ti stack forms the core of the FeRAM capacitor cell.*  

- **PZTアニール (650℃, O₂)** によりペロブスカイト結晶化を実現。  
  *Annealing at 650℃ in O₂ crystallizes PZT into the perovskite phase.*  

- **AlOx保護膜（二重構造：スパッタ＋ALD）**により、  
  水素還元によるPZT特性劣化を防止。  
  *Dual AlOx protection (sputtering + ALD) prevents PZT degradation caused by hydrogen exposure.*  

- パターニングは **CMPではなくIBE (Ion Beam Etching)** を採用。  
  *Patterning requires IBE instead of CMP due to Pt’s resistance to chemical etching.*  

---

## 🟩 Part 4: BEOL (W Plug + Al Interconnects)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 処理条件 / Condition | 寸法 / CD | 膜厚 / Thickness | Mask |
|---------------|--------------------|-----------------|----------------|----------------------|-----------|------------------|------|
| **HLX-DP** | ILD-0堆積<br>*ILD-0 deposition* | ILD | Capacitor上絶縁 | PE-TEOS, 400℃ | - | 6000Å | - |
| **HLX-PH** | フォトリソグラフィ<br>*Photolithography* | ILD | Via-0パターン定義 | KrF, 248nm | 0.24µm | - | HLX |
| **HLX-ET** | エッチング（RIE）<br>*Etching (RIE)* | ILD | Via-0開口形成 | CHF₃/O₂ RIE | 0.24µm | - | - |
| **TINX-SP** | Ti/TiNスパッタ<br>*Ti/TiN sputter* | Barrier | バリア層形成 | DC/RF Sputter | - | 300Å | - |
| **HWX-DP** | Wプラグ堆積<br>*W plug deposition* | Plug | Via-0充填 | W-CVD, WF₆, 400℃ | - | 5000Å | - |
| **HWX-CMP** | CMP研磨<br>*CMP planarization* | CMP | M1接続用平坦化 | CMP | - | - | - |
| **ALA-SP** | Metal-1 Al堆積<br>*Metal-1 Al deposition* | Metal-1 | セル配線形成 | PVD | - | 6000Å | - |
| **ALA-PH** | フォトリソグラフィ<br>*Photolithography* | Metal-1 | パターン定義 | KrF | 0.28µm | - | ALA |
| **ALA-ET** | エッチング（RIE）<br>*Etching (RIE)* | Metal-1 | 配線形成 | Cl₂/BCl₃ RIE | 0.28µm | - | - |
| **HLA-DP** | ILD-1堆積<br>*ILD-1 deposition* | ILD | M1上絶縁 | PE-TEOS | - | 6000Å | - |
| **HLA-PH** | フォトリソグラフィ<br>*Photolithography* | ILD | Via-1開口 | KrF | 0.24µm | - | HLA |
| **HLA-ET** | エッチング（RIE）<br>*Etching (RIE)* | ILD | Via-1形成 | CHF₃/O₂ RIE | 0.24µm | - | - |
| **HWA-DP** | Wプラグ堆積<br>*W plug deposition* | Plug | M2接続 | W-CVD | - | 5000Å | - |
| **HWA-CMP** | CMP研磨<br>*CMP planarization* | CMP | 平坦化 | CMP | - | - | - |
| **ALB-SP** | Metal-2 Al堆積<br>*Metal-2 Al deposition* | Metal-2 | 中間配線 | PVD | - | 6000Å | - |
| **ALB-PH** | フォトリソグラフィ<br>*Photolithography* | Metal-2 | パターン定義 | KrF | 0.35µm | - | ALB |
| **ALB-ET** | エッチング（RIE）<br>*Etching (RIE)* | Metal-2 | 配線形成 | Cl₂/BCl₃ RIE | 0.35µm | - | - |
| **HLB-DP** | ILD-2堆積<br>*ILD-2 deposition* | ILD | M2上絶縁 | PE-TEOS | - | 6000Å | - |
| **HLB-PH** | フォトリソグラフィ<br>*Photolithography* | ILD | Via-2開口 | KrF | 0.28µm | - | HLB |
| **HLB-ET** | エッチング（RIE）<br>*Etching (RIE)* | ILD | Via-2形成 | CHF₃/O₂ RIE | 0.28µm | - | - |
| **HWB-DP** | Wプラグ堆積<br>*W plug deposition* | Plug | M3接続 | W-CVD | - | 5000Å | - |
| **HWB-CMP** | CMP研磨<br>*CMP planarization* | CMP | 平坦化 | CMP | - | - | - |
| **ALC-SP** | Metal-3 Al堆積<br>*Metal-3 Al deposition* | Metal-3 | グローバル配線 | PVD | - | 8000Å | - |
| **ALC-PH** | フォトリソグラフィ<br>*Photolithography* | Metal-3 | パターン定義 | KrF | 0.50µm | - | ALC |
| **ALC-ET** | エッチング（RIE）<br>*Etching (RIE)* | Metal-3 | 配線形成 | Cl₂/BCl₃ RIE | 0.50µm | - | - |

## 🔍 解説 / Explanation  

- **BEOLは3層Al配線 (M1〜M3)** を基本とし、各層は **Wプラグ + ILD絶縁膜**で接続。  
  *The BEOL consists of three Al interconnect layers (M1–M3), each connected by W plugs and isolated with ILD.*  

- **CMPによる平坦化**を随所に導入し、多層化時の段差を抑制。  
  *CMP is applied after each W plug formation to ensure planarity for multilayer integration.*  

- **寸法スケーリング**：M1〜M2は0.28–0.35µm、M3はグローバル配線として0.5µm。  
  *Line widths scale from 0.28–0.35µm for M1–M2 to 0.5µm for M3 global wiring.*  

- **バリア層 (Ti/TiN)** によりW拡散を防止し、接続信頼性を確保。  
  *Ti/TiN barrier prevents W diffusion and ensures reliable connections.*  

---
