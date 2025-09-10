---
layout: default
title: 特別編 第6章　SystemDK with AITL 論文公開（Final Chapter）
---

---

# 📕 特別編 第6章：SystemDK with AITL 論文公開 *(Final Chapter)*  
**Special Chapter 6: Research Paper on SystemDK with AITL *(Final Chapter)***

---

## 1. 📝 背景と課題 / *Introduction*
- 従来のDTCO（Design-Technology Co-Optimization）は **静的補償・過大ガードバンド依存** が課題。  
- サブ2nm以降では **RC遅延、熱結合、EMI/EMC変動** が深刻化。  
- これらに対して **実時間でのクロスレイヤー制御** が必要。  

*Traditional DTCO relies on static compensation and large guardbands.  
At sub-2nm nodes, RC delay, thermal coupling, and EMI/EMC variations become critical.  
Real-time cross-layer control is required.*

---

## 2. ⚙️ 提案枠組み / *Proposed Framework: SystemDK with AITL*
- **PID**：リアルタイム安定化制御 / *Real-time stabilization*  
- **FSM**：モード遷移・状態監督 / *Supervisory mode/state control*  
- **LLM**：ゲイン再設計・知識統合 / *Knowledge-driven redesign with LLM*  
- **アーキテクチャ**：三層構造でEDA設計フローに直接統合  

*SystemDK with AITL introduces a three-layer control loop (PID + FSM + LLM) directly integrated into the EDA design flow.*  

### 📊 Fig.1: Supervisory PID+FSM+LLM Control Architecture

```mermaid
flowchart LR
    A[EDA Flow Input] --> B[PID (Real-time Control)]
    B --> C[FSM (Supervisory Control)]
    C --> D[LLM (Knowledge/Redesign)]
    D --> E[Compensated Output]

    %% Feedback loop
    E -.->|Runtime Metrics (Delay/Thermal/EMI)| B
```

---

## 3. 🧩 技術的ポイント / *Key Technical Points*
- **RC遅延変動補償 / RC Delay Compensation**  
  → 配線スケーリングばらつきを100倍以上低減  
- **熱結合制御 / Thermal Coupling Control**  
  → 3D積層温度上昇を $3\times10^{-5}\%$ 以下に抑制  
- **応力・Vthシフト補償 / Stress & Vth Shift Compensation**  
  → 機械的ストレスの影響をリアルタイム補正  
- **EMI/EMC耐性向上 / EMI/EMC Robustness**  
  → ジッタを2桁抑圧し信号完全性を保証  

---

## 4. 🔬 検証結果 / *Simulation Results*
- **遅延補償**：従来 vs PID vs PID+FSM+LLM  
- **熱結合抑制**：バースト電力下での温度上昇ヒートマップ  
- **EMIジッタ抑制**：制御有無でのタイムシーケンス比較  

### 📊 Fig.2: Delay suppression heatmap vs. thermal coupling and power burst
<img src="./figures/fig2_delay_heatmap.png" alt="Fig.2: Delay suppression heatmap" width="80%">

### 📊 Fig.3: Time-series comparison (Uncontrolled vs PID vs PID+FSM+LLM)
<img src="./figures/fig3_time_series.png" alt="Fig.3: Time-series comparison" width="80%">

### 📊 Fig.4: EMI-induced jitter suppression under AITL control
<img src="./figures/fig4_emi_jitter.png" alt="Fig.4: EMI-induced jitter suppression" width="80%"> 

| Metric / 指標 | Conventional | PID only | PID+FSM+LLM |
|---------------|--------------|----------|-------------|
| RC Delay Variation | 1.0 (norm.) | 0.2 | **0.01** |
| Thermal Rise (ΔT) | +12 K | +4 K | **+0.001 K** |
| EMI Jitter | 100 ps | 20 ps | **1 ps** |

---

## 5. 🌍 意義と応用 / *Significance & Applications*
- **ガードバンド削減 / Guardband Reduction** → 消費電力・性能最適化  
- **信頼性向上 / Reliability Improvement** → 熱暴走・EMI不良の抑制  
- **産業応用 / Industrial Application** → EDAフロー統合、PoCへの展開  

*Cross-layer runtime adaptation enables guardband reduction and improved reliability across sub-2nm nodes, offering a practical pathway for future DTCO.*

---

## 6. 🚀 今後の展望 / *Future Work*
- LLMをEDAフローに組み込んだ **AI-driven DTCO**  
- 実チップ試作・産業界でのPoC検証  
- 大学・企業研修における教材利用  

---

## 7. 📄 論文・関連リンク / *Downloads & Related Links*
- 📑 [Main Paper (PDF)](systemdk_aitl2025.pdf)  

🔗 **Related Chapters**  
- [特別編 第2a章：SystemDK設計対応](../f_chapter2a_systemdk/)  
- [特別編 第3章：AITL-H統合制御SoC実装](../f_chapter3_socsystem/)  
- [特別編 第4章：OpenLane実装](../f_chapter4_openlane/)  
- [特別編 第5章：PDKとDFM設計指針](../f_chapter5_dfm/)  

---

## 8. 👤 著者・ライセンス / *Author & License*

| 📌 Item | 📄 Details |
|------|------|
| **Author** | **三溝 真一 / Shinichi Samizo** |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>Code: [MIT](https://opensource.org/licenses/MIT)<br>Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る / *Back to Top*
🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../)  
📂 [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)
