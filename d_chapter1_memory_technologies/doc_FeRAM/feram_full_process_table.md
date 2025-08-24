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

---

## 🔍 解説 / Explanation  

- **CoSi₂ サリサイド形成**は、ソース・ドレイン・ゲートの低抵抗化に必須。  
  *Formation of CoSi₂ salicide is essential for reducing the resistance of source, drain, and gate.*  

- 2段階アニールにより、**Co → CoSi → CoSi₂**へと相転移を制御。  
  *Two-step annealing controls the phase transition from Co → CoSi → CoSi₂.*  

- **不要な未反応Co膜は酸処理で除去**し、素子間リークを防止。  
  *Unreacted Co film is removed by acid etching to prevent device leakage.*  

---

