---
layout: default
title: Edusemi-v4x/en/index.md 
--- 

# 🎓 Edusemi-v4x | Foundational Educational Materials for Semiconductor Product Development 

[![Back to Portal (EN)](https://img.shields.io/badge/Back%20to%20Portal-0B5FFF?style=for-the-badge&logo=homeassistant&logoColor=white)](https://samizo-aitl.github.io/portal/en/)

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |

---

## 📑 Table of Contents

1. [✍️ Introduction](#️-introduction)
2. [📘 Project Overview](#-project-overview)
3. [🧭 Fundamentals](#-fundamentals)
4. [🧩 Applications](#-applications)
5. [🛠 Practice](#-practice)
6. [📦 Special Topics](#-special-topics)
7. [🔗 Related Projects](#-related-projects)
8. [👤 Author](#-author)
9. [📄 License](#-license)
10. [💬 Feedback](#-feedback)

---

## ✍️ Introduction

Semiconductor technology began with the **invention of the transistor** and rapidly evolved with the advent of the **MOS structure**.  
**Miniaturization and integration** have progressed in line with Moore’s Law, and LSIs have penetrated all fields.

However, **fundamental areas such as physics, circuits, processes, and testing** are often fragmented in educational contexts.  
In practice, these are closely connected—**circuits depend on device physics, and design is supported by process technology and reliability**.

**Edusemi** focuses on the **structural connections between fundamental technologies**, fostering **structural understanding** with an eye toward applications.

> 💡 **Design follows physics, and productization follows verification.**  
> Visualizing the connection from *physics → circuits → implementation → verification*.

---

## 📘 Project Overview

**Edusemi-v4x** is an **open educational resource** covering the full range from **design to manufacturing, testing, and quality assurance**.

- 🎯 **Target Audience**: Engineering students, junior engineers, educators  
- ⭐ **Features**: Emphasis on fundamental interconnections, coverage from design to mass production testing  
- 🧪 **Practice**: sky130, OpenLane, Python, GitHub, ChatGPT integration

---

## 🧭 Fundamentals
> Covers **semiconductor physics, logic design, and process fundamentals** essential for all applications.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧭 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter1_materials/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter1_materials) | *Fundamentals of Semiconductor Physics and MOS Structure* | **Semiconductor physics underlying MOS transistors and CMOS design**, from **band structure to CMOS inverters**, explained step by step. |
| 🧭 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter2_comb_logic/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter2_comb_logic) | *Digital Logic and Logic Circuit Design* | **CMOS logic fundamentals**, covering **basic gates, complex logic, multiplexers, adders, and FSM design**. |
| 🧭 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter3_process_evolution/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter3_process_evolution) | *Process Evolution and Design Limits in CMOS* | **CMOS technology scaling from 0.5µm to 90nm** and the **impact of physical limits on circuit design**. |
| 🧭 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter4_mos_characteristics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter4_mos_characteristics) | *MOS Transistor Characteristics and Design Infrastructure* | **MOSFET physics, dimensions, design rules, and PDK structure** to understand **operation, reliability, and design limits** from a designer’s perspective. |
| 🧭 **Chapter 5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5a_spec_module_if/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5a_spec_module_if) | *Spec Definition & Interface Design* | **Upstream design, specification definition, module selection, and PoC integration**. |
| 🧭 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5_soc_design_flow/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5_soc_design_flow) | *SoC Design Flows and EDA Tools* | **End-to-end SoC development flow**, including **standard cell design, physical design interfaces, STA, and DFT basics**. |
| 🧭 **Chapter 6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter6_test_and_package/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter6_test_and_package) | *Test, Packaging, and Productization* | **Mass production processes** including **inspection, monitoring, reliability checks, and shipment decisions** to prevent defective products from reaching the market. |
| 🧭 **Chapter 7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter7_design_review_and_org/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter7_design_review_and_org) | *Design Review and Cross-Functional Collaboration* | **Design Review (DR) structure and purpose** and **cross-functional collaboration mechanisms** in semiconductor product development. |

---

## 🧩 Applications
> Delves into **applied semiconductor technologies** and specialized design fields to develop practical design skills.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧩 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) | *Memory Technologies – Structure and Selection Guidelines* | **SRAM, DRAM, FeRAM, MRAM, and NAND architectures**, compared by **speed, non-volatility, endurance, area efficiency, and power consumption**, with a focus on **SoC integration, selection, and interconnection**. |
| 🧩 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter2_high_voltage_devices/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter2_high_voltage_devices) | *High Voltage Devices* | **HV-CMOS and LDMOS structures and layout techniques**, and their **applications in power control, sensor interfaces, and high-voltage driver circuits**. |
| 🧩 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) | *ESD Protection Design* | **ESD reliability risks**, covering **protection device structures, layout strategies, test standards, and failure analysis** for semiconductor ICs. |
| 🧩 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter4_layout_optimization/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter4_layout_optimization) | *Layout Design and Optimization* | **Placement, routing, and geometric optimization techniques** to ensure **performance, reliability, and manufacturability (DFM)**. |
| 🧩 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) | *Analog / Mixed-Signal Design* | **AMS design fundamentals**, from **op-amps and comparators** to **layout techniques, noise mitigation, and ADC/DAC integration challenges**. |
| 🧩 **Chapter 5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5a_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5a_analog_mixed_signal) | *0.18µm AMS Design Techniques* | **Variability, noise, and parasitic countermeasures** for **0.18µm AMS circuits**, enabling operation across **wide supply voltages and frequency ranges**. |
| 🧩 **Chapter 5b**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5b_ams_block_and_pdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5b_ams_block_and_pdk) | *Differentiated Analog Modules via Manufacturing Technology — Realizing 50% Reduction in 1/f Noise* | **Manufacturing-aware design strategies** achieving **over 50% reduction in 1/f noise**, enabling **low-noise MOS device realization**. |
| 🧩 **Chapter 6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) | *PDK and EDA Environment* | **PDK components, EDA tool integration, DRC, process compatibility, and BSIM models**, forming the foundation of robust design environments. |
| 🧩 **Chapter 7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter7_automation_and_verification/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter7_automation_and_verification) | *Automation and Implementation Verification* | **Automation from RTL to physical verification**, including **Lint, DRC, LVS, STA, and CI/CD-based verification flows**. |
| 🧩 **Chapter 8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) | *FSM Design (Finite State Machine)* | **Moore and Mealy FSM structures**, with **state diagrams and three-stage Verilog descriptions** for control logic design. |
| 🧩 **Chapter 9**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) | *PLL and Clock Design* | **PLL fundamentals**, covering **skew/jitter mitigation and clock tree design** for **high-precision clock generation and distribution**. |

---

## 🛠 Practice
> Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design to solidify skills.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🛠 **Chapter 0**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter0_environment_setup/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter0_environment_setup) | *Environment Setup and Toolchain Preparation* | **Complete toolchain setup** for Chapters 1–3, including **Python, VS Code, Git, ngspice, Sky130 PDK (volare), Magic, Netgen, KLayout, Docker, and WSL2**, ensuring a **fully functional environment** for **SPICE experiments, OpenLane design, and Python automation workflows**. |
| 🛠 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) | *Python-Based Automation Tools for Semiconductor Design* | **Python automation scripts** for **SPICE simulations, reliability model evaluation, and report analysis**, integrated with the **Sky130 PDK and OpenLane flow**. |
| 🛠 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter2_sky130_experiments/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter2_sky130_experiments) | *Sky130 Experiments and SPICE-Based Characterization* | **MOS characterization (Vg–Id curves, Vth extraction)** and **BTI/TDBB prediction** using the **SkyWater Sky130 PDK**, enabling **SPICE-based design verification**. |
| 🛠 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter3_openlane_practice/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter3_openlane_practice) | *Digital Design Practice Using OpenLane* | **End-to-end LSI design flow**, from **Verilog RTL to GDS generation**, covering **synthesis, placement, routing, and DRC** with OpenLane. |

---

## 📦 Special Topics
> Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 📦 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter1_finfet_gaa/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa) | *Advanced Node Technologies – FinFET, GAA & CFET* | **Physical and electrical characteristics** and **design impacts** of **FinFET, GAA, and CFET**, introducing **advanced CMOS technologies beyond planar MOS limits**. |
| 📦 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2_chiplet_pkg/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg) | *Chiplets and Advanced Packaging* | **2.5D/3D integration, TSV, and heterogeneous integration** for **chiplet architecture design, implementation, and reliability**, enabling **flexible design and scalability**. |
| 📦 **Chapter 2a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk) | *Design Handling of Thermal, Stress, and Noise Constraints in SystemDK* | **SystemDK concepts** and **design methodologies** for handling **SI/PI, thermal, stress, and EMI/EMC constraints** at the **SoC–system integration level**. |

---

## 🔗 Related Projects
> Sister projects linked with Edusemi, covering **control theory, socio-industrial structures, and advanced technologies**.

| 🌐 Project | Overview | Key Features |
|---|---|---|
| ➕ **Edusemi-Plus**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-Plus/en/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-Plus) | **Applied learning materials** analyzing **geopolitics, product strategy, AI, quantum technologies, and investment**. | - **In-depth analysis of Apple Silicon, the CHIPS Act, and Cryo-CMOS**<br>- **Explores technology within its societal, policy, and industrial context** |
| 🎛️ **EduController**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/en/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) | **Comprehensive coverage from control theory (PID, state-space) to AI control (NN, RL, LLM)**. | - **Linked with PoC design and OpenLane-based control implementation**<br>- **Design exercises in Python, RTL verification, and FSM generation support** |

---

## 👤 Author
> Author with professional background in semiconductors and inkjet actuators, creating **materials that integrate theory and practice**.

| 📌 Item | Details |
|------|------|
| **Name** | **Shinichi Samizo** |
| **Expertise** | **Semiconductor devices** (logic, memory, high-voltage mixed integration)<br>**Thin-film piezoelectric actuators for inkjet applications**<br>**printhead productization, BOM management, and ISO training** |
| **💻 GitHub** | **Samizo-AITL**<br>[![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-black?logo=github)](https://github.com/Samizo-AITL) |

---

## 📄 License
[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)
> Adopts a hybrid licensing model according to the nature of the materials, code, and diagrams.  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 Item | License | Description |
|------|------|------|
| **Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required, share-alike for BY-SA |
| **Figures & diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External references** | Follow the original license | Cite the original source |

---

## 💬 Feedback
> Propose improvements or start discussions via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
