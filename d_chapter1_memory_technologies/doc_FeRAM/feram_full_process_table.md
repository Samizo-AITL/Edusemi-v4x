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

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **FS-DP** | SiON保護膜堆積<br>*SiON protection film deposition* | Global | 界面保護<br>*Interface protection* | 200Å @ 700℃ |
| **FSN-DP** | STI用窒化膜堆積<br>*STI nitride deposition* | Field | 酸化防止キャップ<br>*Oxidation cap* | 1500Å @ 750℃ |
| **F-PH** | フォトリソグラフィ<br>*Photolithography* | Field | STIパターン定義<br>*STI pattern definition* | CD = 0.28µm |
| **F-ET** | エッチング（RIE）<br>*Etching (RIE)* | Field | STI溝形成<br>*STI trench etching* | CD = 0.28µm |
| **F-DP** | STI酸化膜埋込<br>*STI oxide fill* | Field | トレンチフィル<br>*Trench fill* | Oxide 4000Å |
| **F-CMP** | STI CMP<br>*CMP planarization* | Field | 平坦化<br>*Planarization* | - |
| **PRE-OX** | 犠牲酸化膜形成<br>*Sacrificial oxidation* | Pre | 表面改質・汚染除去<br>*Surface treatment* | Dry OX ~80Å |

📘 **解説**  
STIで素子間を分離し、リーク防止。PRE-OXで注入前に表面を整える。  
*STI isolates devices to prevent leakage. PRE-OX improves surface quality before implantation.*  

---

### 🔹 ウェル形成 / *Well Formation*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **NWL-PH** | フォトリソ（N-Well）<br>*Lithography (N-Well)* | Well | N-Well定義<br>*N-Well definition* | - |
| **NWL-ION** | イオン注入<br>*Ion implantation* | Well | N-Well形成<br>*N-Well formation* | 800keV, 2E13 |
| **PWL-PH** | フォトリソ（P-Well）<br>*Lithography (P-Well)* | Well | P-Well定義<br>*P-Well definition* | - |
| **PWL-ION** | イオン注入<br>*Ion implantation* | Well | P-Well形成<br>*P-Well formation* | 200keV, 5E12 |

📘 **解説**  
N/P-Wellを形成し、NMOSとPMOSの領域を分離。デュアルウェル構造により寄生素子を抑制。  
*N- and P-wells are formed to separate NMOS and PMOS regions, suppressing parasitic effects.*  

---

### 🔹 チャネル調整注入 / *Channel Doping*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **NCD/PCD-PH** | フォトリソ（1.8V NMOS/PMOS） | CD | チャネル定義 | - |
| **NCD/PCD-ION** | イオン注入<br>*Ion implantation* | CD | Vth調整 | B or BF₂, 30–50keV |
| **NCD2/PCD2-PH** | フォトリソ（3.3V NMOS/PMOS） | CD | チャネル再調整 | - |
| **NCD2/PCD2-ION** | イオン注入<br>*Ion implantation* | CD | Vth調整（3.3V用） | B or BF₂, 30–50keV |

📘 **解説**  
1.8Vと3.3Vで別マスクを使い、チャネルドーピングを分離。閾値電圧を個別に最適化。  
*Channel doping is performed separately for 1.8V and 3.3V devices, optimizing threshold voltages.*  

---

### 🔹 ゲート形成 / *Gate Formation*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **G1-OX** | ゲート酸化 (第1段)<br>*Gate oxidation (G1)* | Gate | 初期酸化膜 | Dry OX 35Å |
| **G1-PH / G1-ET** | フォト＋エッチ (1.8V除去) | Gate | 膜厚制御 | HF or SPM |
| **G2-OX** | ゲート酸化 (第2段) | Gate | 再酸化 | Dry OX 35Å |
| **PLY-DP** | ポリSi堆積 | Gate | ゲート電極 | LPCVD 1500Å |
| **PLY-PH / PLY-ET** | フォト＋エッチ | Gate | ゲート形成 | KrF, CD = 0.18µm |

📘 **解説**  
逆Tox方式で1.8V: 35Å, 3.3V: 70Åに分離。ポリSiゲートをKrF露光で形成。  
*Inverse Tox method yields 35Å for 1.8V and 70Å for 3.3V devices. Poly-Si gate patterned with KrF lithography.*  

---

### 🔹 LDD・S/D形成 / *LDD & Source/Drain*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **NLL/PLL ION** | LDD注入 (1.8V) | LDD | 浅拡散形成 | As/BF₂ |
| **NLM/PLM ION** | LDD注入 (3.3V) | LDD | 浅拡散形成 | As/BF₂ |
| **SW-DP/ET** | スペーサ堆積＋エッチ | Gate | LDD保護 | SiN, 800Å |
| **NLL2/PLL2, NLM2/PLM2** | 深拡散注入 | S/D | ソース・ドレイン形成 | As/BF₂, 40keV |

📘 **解説**  
LDD形成でホットキャリアを抑制し、スペーサで拡散制御。深拡散でソース・ドレイン完成。  
*LDD suppresses hot carriers, spacers control diffusion, and deep implants complete S/D formation.*  

---

### 🔹 サリサイド形成 / *Salicide Formation (CoSi₂)*  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **CO-SP** | Coスパッタ<br>*Co sputtering* | Salicide | 前駆体形成<br>*Precursor layer* | - |
| **LMP-ANL** | サリサイドアニール<br>*Salicide annealing* | Salicide | CoSi形成<br>*CoSi formation* | 550℃, 30s |
| **CO-ET** | 酸エッチング<br>*Acid etching* | Salicide | 未反応Co除去<br>*Remove unreacted Co* | H₂SO₄系 |
| **LMP2-ANL** | 相転移アニール<br>*Phase annealing* | Salicide | CoSi₂形成<br>*CoSi₂ formation* | 750℃, 30s |

📘 **解説**  
サリサイドによりS/Dとゲートの抵抗を低減。2段階アニールでCo → CoSi → CoSi₂に変換。未反応Coは酸処理で除去。  
*Salicide lowers resistance of S/D and gate. Two-step anneal transforms Co → CoSi → CoSi₂. Unreacted Co is removed by acid etching.*  

---

## 🟩 Part 2: Capacitor + BEOL (*Back-End of Line*)  

---

### 🔹 ILD & Contact Formation (*F2-DP〜Via*)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **F2-DP** | ILD堆積<br>*ILD deposition* | ILD | 配線前絶縁膜 | PE-TEOS, 6000Å |
| **F2-CMP** | CMP平坦化<br>*CMP planarization* | CMP | 表面平坦化 | CMP |
| **CNT-PH/ET** | フォト＋エッチ<br>*Lithography + Etching* | Contact | コンタクト開口形成 | CD = 0.24µm |
| **TIN-SP** | TiNスパッタ<br>*TiN sputtering* | Barrier | バリアメタル形成 | DC sputter, 300Å |
| **CW-DP** | Wデポジション<br>*W deposition* | Plug | Wプラグ充填 | CVD, WF₆, 4000Å |
| **CW-CMP** | W CMP<br>*W CMP planarization* | CMP | 平坦化 | CMP |

📘 **解説**  
ILDで絶縁し、Wプラグで下層デバイスとのコンタクトを確立。TiNバリアがW拡散を防ぐ。  
*ILD provides insulation; W plug establishes contact. TiN barrier prevents W diffusion.*  

---

### 🔹 Capacitor Formation (*Pt/PZT/Ti + AlOx*)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **TI1-SP** | Tiスパッタ | Capacitor | Pt下地密着層 | 300Å |
| **Pt-SP** | Ptスパッタ | Capacitor | 下部電極形成 | 1500Å |
| **PZT-COT** | PZTスピンコート | Capacitor | 強誘電体前駆体 | Sol-Gel, 1000Å |
| **PZT-ANL** | PZTアニール | Capacitor | ペロブスカイト結晶化 | RTA, 650℃ O₂ |
| **TI2-SP** | Tiスパッタ | Capacitor | 上部電極バッファ | 300Å |
| **CAP-PH/ET** | フォト＋イオンミリング | Capacitor | キャパシタパターニング | KrF, CD=0.35µm |
| **ALOX-SP/DP** | AlOxスパッタ＋ALD | Capacitor | 保護膜（二重構造） | 各300Å |
| **ALOX-PH/ET** | フォト＋エッチ | Capacitor | 接続開口形成 | KrF, 0.35µm |

📘 **解説**  
Pt/PZT/Ti構造でFeRAMセル形成。AlOx保護膜（二重構造）で水素還元劣化を防ぐ。PtはCMP不可のためIBEを採用。  
*Pt/PZT/Ti capacitor is core of FeRAM. Dual AlOx layers prevent H₂ degradation. IBE used for Pt patterning.*  

---

### 🔹 BEOL Interconnects (M1〜M3)  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **HLX-DP〜HWX-CMP** | ILD-0, Via-0, Wプラグ形成 | Interconnect | Capacitor-M1接続 | CD=0.24µm |
| **ALA-SP/PH/ET** | Metal-1 Al配線形成 | Metal-1 | セル配線 | 0.28µm, 6000Å |
| **HLA-DP〜HWA-CMP** | ILD-1, Via-1, Wプラグ形成 | Interconnect | M1-M2接続 | CD=0.24µm |
| **ALB-SP/PH/ET** | Metal-2 Al配線形成 | Metal-2 | 中間配線 | 0.35µm, 6000Å |
| **HLB-DP〜HWB-CMP** | ILD-2, Via-2, Wプラグ形成 | Interconnect | M2-M3接続 | CD=0.28µm |
| **ALC-SP/PH/ET** | Metal-3 Al配線形成 | Metal-3 | グローバル配線 | 0.50µm, 8000Å |

📘 **解説**  
M1〜M3のAl配線で多層配線を構成。各層はWプラグとILDで接続。M3はグローバル配線用途。  
*Three Al layers form interconnects. W plugs + ILD connect layers. M3 serves as global wiring.*  

---

### 🔹 Pad & Passivation  

| 工程名 / Step | 処理内容 / Process | 分類 / Category | 目的 / Purpose | 条件 / Condition |
|---------------|--------------------|-----------------|----------------|------------------|
| **ALD-SP/PH/ET** | Al厚膜パッド形成 | Pad | Bond Pad作製 | 3.0µm, 10000Å |
| **PAD-DP** | パッシベーション膜堆積 | Passivation | 環境保護 | SiN+SiO₂, 8000Å |
| **PAD-PH/ET** | フォト＋エッチ | Passivation | I/O開口形成 | 3.0µm |

📘 **解説**  
厚膜Alパッドでワイヤボンディング対応。パッシベーションで湿気・Na拡散を防ぎ信頼性確保。  
*Thick Al pads enable wire bonding. SiN+SiO₂ passivation protects against humidity/Na diffusion.*  

---

### 🔹 E-Test  

| 工程名 / Step | 内容 / Details |
|---------------|----------------|
| **E-TEST** | Vth, Ioff, FeRAM保持特性などを最終ウェハで測定<br>*Measure Vth, Ioff, FeRAM retention at wafer level* |

📘 **解説**  
最終テストでCMOS特性とFeRAM特性を同時に評価。  
*Final wafer test verifies both CMOS and FeRAM characteristics.*  
