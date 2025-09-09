---
layout: default
title: 特別編 第6章　SystemDK with AITL 論文公開（Final Chapter）
---

---

# 📕 特別編 第6章：SystemDK with AITL 論文公開 *(Final Chapter)*  
**Special Chapter 6: Research Paper on SystemDK with AITL *(Final Chapter)***

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter6_research/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter6_research) |

---

## 📄 論文概要｜*Paper Overview*
本研究は、従来の静的DTCOに対し、EDA設計フローに **PID + FSM + LLM** の三層制御ループを直接統合する新しい枠組み **SystemDK with AITL** を提案します。  

### 🧩 技術的ポイント｜*Key Technical Points*
- **RC遅延変動補償**：配線スケーリングによる遅延ばらつきを100倍以上低減  
- **熱結合の制御**：3D積層による温度上昇を $3\times 10^{-5}\%$ 以下に抑制  
- **応力・Vthシフトの補償**：機械的ストレスによるデバイス変動を実時間補正  
- **EMI/EMC耐性向上**：ジッタを2桁抑圧、信号完全性を保証  

### 🌍 意義｜*Significance*
Cross-layer runtime adaptation enables **guardband reduction** and **improved reliability** across **sub-2nm nodes**, providing a practical pathway for future DTCO.

---

## 🔗 論文ダウンロード｜*Download*
- 📑 [Main Paper (PDF)](systemdk_aitl2025.pdf)  

---

## 🖼️ 図表ハイライト｜*Figure Highlights*
- **Fig.1**: Supervisory PID+FSM+LLM Control Architecture (TikZ Block Diagram)  
- **Fig.2**: Delay suppression heatmap vs. thermal coupling and power burst  
- **Fig.3**: Time-series comparison: uncontrolled vs PID vs PID+FSM+LLM  
- **Fig.4**: EMI-induced jitter suppression under AITL control  

---

## 📌 関連リンク｜*Related Links*
- 🔎 [特別編 第2a章：SystemDK設計対応](../f_chapter2a_systemdk/)  
- ⚙️ [特別編 第3章：AITL-H統合制御SoC実装](../f_chapter3_socsystem/)  
- 🖥️ [特別編 第4章：OpenLane実装](../f_chapter4_openlane/)  
- 🧬 [特別編 第5章：PDKとDFM設計指針](../f_chapter5_dfm/)  

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜*Back to Top*

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)

