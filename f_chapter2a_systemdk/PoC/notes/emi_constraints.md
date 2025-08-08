# EMI制約とアイソレーション戦略（**EMI Constraints and Isolation Strategy**）

## 1. 概要 / **Overview**
- **EMI（電磁妨害）**は**PoC設計**において重要な設計課題である。  
  *Electromagnetic Interference (EMI) is a critical design concern in Proof-of-Concept (PoC) development.*
- 特に**AMS / RF回路 / MRAM / FPGA間の干渉**が性能劣化の原因となる。  
  *Interference between AMS, RF circuits, MRAM, and FPGA can degrade system performance.*

## 2. EMI発生源 / **EMI Sources in PoC Board**
- **PLL**や**高周波クロック**、**高dV/dtのI/O**に起因するノイズ  
  *Noise originating from PLLs, high-frequency clocks, and high dV/dt I/Os.*
- **MRAMの書き込みパルス**による急峻な信号遷移  
  *Sharp transients from MRAM write pulses.*
- **FPGAのDDRアクセス**や**SPI通信波形**もEMI要因となる  
  *DDR access and SPI signals from the FPGA also contribute to EMI.*

## 3. 解析手法 / **Simulation and Analysis Methods**
- **近傍界 / 遠方界EMIモデリング**（Near-field / Far-field）を使った評価  
  *Evaluation using near-field and far-field EMI modeling.*
- **PCBスタック構造と放射パターン**の相関を3D EMCツールで解析  
  *Analyze correlation between PCB stack design and radiation pattern using 3D EMC tools.*
- **EMI-熱連成解析**（例：EM波→局所発熱）も有効  
  *EMI-thermal coupled simulation (e.g., EM wave-induced local heating) is also effective.*

## 4. 緩和設計案 / **EMI Mitigation Strategy**
- **GNDシールド**の挿入や**スタック層順序の最適化**  
  *Insert GND shielding and optimize stack-up layer order.*
- **Power Island分割**により**AMSとMRAMの電源隔離**を実施  
  *Split power islands to isolate AMS and MRAM power domains.*
- **EMI-aware floorplanning**を導入（**SystemDK対応**）  
  *Apply EMI-aware floorplanning techniques (supported in SystemDK).*

## 5. SystemDKへの制約統合 / **Integration into SystemDK**
- **PKGDK**での**伝導ノイズ・放射ノイズ制御フラグ**の設計  
  *Design control flags for conducted and radiated noise in PKGDK.*
- **EMIクリティカル領域の自動検出スクリプト**と連携  
  *Integrate with auto-detection scripts for EMI-critical regions.*

## 6. 図解 / **Figures**
- **EMI干渉の概念図**（例：AMSとMRAM間の影響）  
  *Conceptual diagram of EMI interference (e.g., between AMS and MRAM).*
- **層構造別の放射パターン例**  
  *Example radiation patterns based on different PCB stack-ups.*

## 7. 参考文献 / **References**
- [1] *EMI Design Guidelines for Mixed-Signal SoC*, 2024.  
- [2] **自作PoC構造モデル**および**EMIツール出力ログ**  
  *In-house PoC model and EMI simulation output logs.*

---

<p align="center">
  <img src="https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/PoC/images/emi_interference_mram_ams.png" alt="EMI Interference Diagram" width="70%">
</p>

<p align="center"><b>図2 / Figure 2：</b>PoC評価ボード上の<strong>FPGA、MRAM、AMSブロック間のEMI干渉経路の概念図</strong>。書き込みパルスやPLLノイズなどが<strong>AMS回路へ影響</strong>を与える経路を示す。<br>
<em>A conceptual EMI interference diagram between FPGA, MRAM, and AMS blocks on a PoC board. It shows how write pulses and PLL noise affect AMS circuits.</em></p>
