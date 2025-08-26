---
layout: default
title: 基礎編 第1章：半導体物性とMOS構造の基礎　
---

---

# 📘 基礎編 第1章：半導体物性とMOS構造の基礎  
**Fundamentals-Chapter 1: Fundamentals of Semiconductor Physics and MOS Structure**

---

## 🧭 概要｜Overview

本章では、MOSトランジスタやCMOS回路設計の物理的基盤となる**半導体物性**を  
段階的に学び、**バンド構造から論理回路の出発点**であるCMOSインバータまでを理解します。

> This chapter explores the **physical foundation of MOS transistors**,  
> providing a step-by-step understanding from **band structure to CMOS logic circuits**.

---

## 🎯 学習のねらい｜Learning Objectives

| 🇯🇵 日本語                                                                                          | 🇺🇸 English                                                                                       |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| バンド構造、PN接合、MOS構造など、**物性物理の本質を段階的に理解**する                              | Understand the **core physical concepts** such as band structures, PN junctions, and MOS theory. |
| MOSチャネル形成と**スイッチ動作の物理モデル**を明確に把握する                                      | Learn the **channel formation** and physical **switching model** of MOS transistors.             |
| CMOSインバータにより、**論理回路設計の出発点**を実感として理解する                                 | Gain intuitive understanding of **logic circuit fundamentals** via the CMOS inverter.            |

---

## 📚 章構成｜Chapter Structure

| 節番号 | ファイル名 / Filename                                | 内容概要 / Summary                                                                              |
|--------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| 1.1    | [`1.1_band_structure.md`](./1.1_band_structure.md)     | **バンド構造とキャリア移動**<br>🔋 *Band Structure and Carriers (Electrons & Holes)*          |
| 1.2    | [`1.2_pn_junction.md`](./1.2_pn_junction.md)           | **PN接合と整流特性**<br>🔌 *PN Junction and Rectification*                                   |
| 1.3    | [`1.3_mos_structure.md`](./1.3_mos_structure.md)       | **MOS構造・電界制御とチャネル形成**<br>⚙️ *MOS Structure and Channel Formation*              |
| 1.4    | [`1.4_mos_switch.md`](./1.4_mos_switch.md)             | **MOSのスイッチ動作と回路モデル**<br>🔁 *MOS Switching and Circuit Abstraction*               |
| 1.5    | [`1.5_cmos_inverter.md`](./1.5_cmos_inverter.md)       | **CMOSインバータの構造と波形解析**<br>🔀 *CMOS Inverter Structure and Logical Behavior*       |

---

## 🧠 学習のポイント｜Key Takeaways

- 半導体の物性基礎（**バンド構造・PN接合・MOS構造**）を**階層的に理解**
- **チャネル形成と電界制御**によるMOSのスイッチ性の原理を視覚的に把握
- CMOSインバータの構造と動作波形から、**論理設計への出発点**へ導入

---

## 📂 ディレクトリ構成｜Directory Structure

```
Edusemi-v4x/
└── chapter1_materials/
├── README.md
├── 1.1_band_structure.md
├── 1.2_pn_junction.md
├── 1.3_mos_structure.md
├── 1.4_mos_switch.md
└── 1.5_cmos_inverter.md
```

---

## 🖼️ 図版予定｜Planned Figures

各図は `/images/` に格納予定です：

- `band_diagram_intrinsic.png`：真性半導体のバンド図  
- `pn_depletion_potential.png`：PN接合と整流モデル  
- `mos_cross_section.png`：MOS断面構造  
- `mos_depletion_inversion.png`：空乏層→反転チャネル  
- `nmos_switch.png`, `pmos_switch.png`：スイッチ動作の回路記号  
- `cmos_inverter_structure.png`：インバータ構造図  
- `cmos_inverter_waveform.png`：出力波形（立ち上がり・立ち下がり）

---

## 🔄 次章への接続｜Transition to Chapter 2

| 🇯🇵 日本語                                                                                         | 🇺🇸 English                                                                                         |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| 本章の理解を踏まえ、第2章では**組み合わせ論理回路**（AND, OR, NAND, XORなど）の設計・解析に進みます。 | Building on this foundation, Chapter 2 explores **combinational logic design** and circuit analysis. |

📎 [👉 第2章：組み合わせ論理回路の設計へ進む](../chapter2_comb_logic/README.md)

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **✉️ Email** | [![Email](https://img.shields.io/badge/Email-shin3t72%40gmail.com-red?style=for-the-badge&logo=gmail)](mailto:shin3t72@gmail.com) |
| **🐦　X** | [![X](https://img.shields.io/badge/X-@shin3t72-black?style=for-the-badge&logo=x)](https://x.com/shin3t72) |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../README.md)  
[![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)
