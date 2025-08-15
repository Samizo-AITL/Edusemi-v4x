---
layout: default
title: Edusemi-v4x/en/index.md 
--- 

---

# 🎓 **Edusemi-v4x | Foundational Educational Materials for Semiconductor Product Development**  

[![Back to Samizo-AITL Portal](https://img.shields.io/badge/Back%20to%20Samizo--AITL%20Portal-brightgreen)](https://samizo-aitl.github.io/en) 

> 🆕 **Check the latest updates in the [ChangeLog](../revision_history.md).**  
> *Review all recent modifications in the [ChangeLog](../revision_history.md).*

<p align="right">
  <img src="https://img.shields.io/badge/Last%20Update-2025--08--15-orange" alt="Last Update">
  <a href="../revision_history.md">
    <img src="https://img.shields.io/badge/View-ChangeLog-blue?logo=markdown" alt="View ChangeLog">
  </a>
</p>

---

## 🔗 Official Links

| Language | GitHub Pages 🌐 | GitHub 💻 |
|----------|----------------|-----------|
| 🇺🇸 English | [![GitHub Pages EN](https://img.shields.io/badge/GitHub%20Pages-English-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/en/) | [![GitHub Repo EN](https://img.shields.io/badge/GitHub-English-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |
| 🇯🇵 Japanese | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |

---

## 📑 **Table of Contents**

- [✍️ Introduction](#️-introduction)
- [📘 Project Overview](#-project-overview)
- [🧭 Fundamentals](#-fundamentals)
- [🧩 Applications](#-applications)
- [🛠 Practice](#-practice)
- [📦 Special Topics](#-special-topics)
- [🔗 Related Projects](#-related-projects)
- [👤 Author](#-author)
- [📄 License](#-license)
- [💬 Feedback](#-feedback)

---

## ✍️ **Introduction**

Semiconductor technology began with the **invention of the transistor** and rapidly evolved with the advent of the **MOS structure**.  
**Miniaturization and integration** have progressed in line with Moore’s Law, and LSIs have penetrated all fields.

However, **fundamental areas such as physics, circuits, processes, and testing** are often fragmented in educational contexts.  
In practice, these are closely connected—**circuits depend on device physics, and design is supported by process technology and reliability**.

**Edusemi** focuses on the **structural connections between fundamental technologies**, fostering **structural understanding** with an eye toward applications.

> 💡 **Design follows physics, and productization follows verification.**  
> Visualizing the connection from *physics → circuits → implementation → verification*.

---

## 📘 **Project Overview**

**Edusemi-v4x** is an **open educational resource** covering the full range from **design to manufacturing, testing, and quality assurance**.

- 🎯 **Target Audience**: Engineering students, junior engineers, educators  
- ⭐ **Features**: Emphasis on fundamental interconnections, coverage from design to mass production testing  
- 🧪 **Practice**: sky130, OpenLane, Python, GitHub, ChatGPT integration

---

## 🧭 **Fundamentals**  
> Covers **semiconductor physics, logic design, and process fundamentals** essential for all applications.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧭 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter1_materials/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter1_materials) | *Fundamentals of Semiconductor Physics and MOS Structure* | Learn the semiconductor physics underlying MOS transistors and CMOS circuit design, from band structure to CMOS inverters, step by step. |
| 🧭 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter2_comb_logic/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter2_comb_logic) | *Digital Logic and Logic Circuit Design* | Covers the fundamentals of CMOS logic circuit design, from basic logic gates to complex logic, multiplexers, adders, and FSM design. |
| 🧭 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter3_process_evolution/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter3_process_evolution) | *Process Evolution and Design Limits in CMOS* | Learn the evolution of CMOS technology from 0.5µm to 90nm and the impact of physical limits on circuit design. |
| 🧭 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter4_mos_characteristics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter4_mos_characteristics) | *MOS Transistor Characteristics and Design Infrastructure* | Organize the physics, dimensions, design rules, and PDK structure of MOSFETs to understand their operation, reliability, and limits from a designer’s perspective. |
| 🧭 **Chapter 5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5a_spec_module_if/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5a_spec_module_if) | *Spec Definition & Interface Design* | Covers upstream design, module selection, and PoC integration. |
| 🧭 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter5_soc_design_flow/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter5_soc_design_flow) | *SoC Design Flows and EDA Tools* | Learn the full SoC development flow, the connection points between standard cell and physical design, and the basics of STA and DFT verification. |
| 🧭 **Chapter 6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter6_test_and_package/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter6_test_and_package) | *Test, Packaging, and Productization* | Understand mass production processes (inspection, monitoring, reliability checks, shipment decisions) to prevent defective products from reaching the market. |
| 🧭 **Chapter 7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/chapter7_design_review_and_org/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/chapter7_design_review_and_org) | *Design Review and Cross-Functional Collaboration* | Gain a systematic understanding of the purpose, structure, and cross-functional collaboration mechanisms of Design Reviews in semiconductor product development. |

---

## 🧩 **Applications**  
> Delves into **applied semiconductor technologies** and specialized design fields to develop practical design skills.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧩 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter1_memory_technologies/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter1_memory_technologies) | *Memory Technologies – Structure and Selection Guidelines* | Understand the structure and operation of SRAM, DRAM, FeRAM, MRAM, and NAND; learn to compare them based on speed, non-volatility, endurance, area efficiency, and power consumption; and master integration, selection, and connection methods in SoC design. |
| 🧩 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter2_high_voltage_devices/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter2_high_voltage_devices) | *High Voltage Devices* | Learn the structure and layout design techniques of HV-CMOS and LDMOS devices, and understand their applications in power control, sensor interfaces, and high-voltage driver circuits. |
| 🧩 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter3_esd_protection_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter3_esd_protection_design) | *ESD Protection Design* | Understand ESD reliability risks in semiconductor ICs, and systematically learn protection device structures, layout strategies, test standards, and failure analysis. |
| 🧩 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter4_layout_optimization/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter4_layout_optimization) | *Layout Design and Optimization* | Learn methods for optimizing placement, routing, and geometric structures in IC layouts to ensure performance, reliability, and manufacturability. |
| 🧩 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5_analog_mixed_signal) | *Analog / Mixed-Signal Design* | Understand the overall scope of AMS design, from basic circuits such as op-amps and comparators to layout design, noise countermeasures, and integration challenges with ADC/DAC. |
| 🧩 **Chapter 5a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5a_analog_mixed_signal/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5a_analog_mixed_signal) | *0.18µm AMS Design Techniques* | Learn countermeasures for variability, noise, and parasitics in 0.18µm AMS circuit design, and acquire techniques adaptable to a wide range of supply voltages and frequency bands. |
| 🧩 **Chapter 5b**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter5b_ams_block_and_pdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter5b_ams_block_and_pdk) | *Differentiated Analog Modules via Manufacturing Technology — Realizing 50% Reduction in 1/f Noise* | Learn design and manufacturing strategies to leverage fabrication processes for reducing 1/f noise by over 50% and achieving low-noise MOS devices. |
| 🧩 **Chapter 6**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter6_pdk_and_eda_environment/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter6_pdk_and_eda_environment) | *PDK and EDA Environment* | Understand the components of a PDK, its integration with EDA tools, design rule checking, process compatibility, and the relationship with BSIM models. |
| 🧩 **Chapter 7**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter7_automation_and_verification/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter7_automation_and_verification) | *Automation and Implementation Verification* | Learn automation techniques from RTL design to physical layout verification, and master CI/CD verification flows alongside Lint, DRC, LVS, and STA. |
| 🧩 **Chapter 8**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter8_fsm_design_basics/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter8_fsm_design_basics) | *FSM Design (Finite State Machine)* | Understand the structure and operation of Moore and Mealy FSMs, and learn three-stage description methods in Verilog with state diagrams. |
| 🧩 **Chapter 9**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/d_chapter9_pll_and_clock_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/d_chapter9_pll_and_clock_design) | *PLL and Clock Design* | Learn PLL principles, skew/jitter countermeasures, and clock tree design to acquire high-precision clock generation and distribution techniques. |

---

## 🛠 **Practice**  
> Hands-on exercises with Python automation, Sky130 experiments, and OpenLane design to solidify skills.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🛠 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter1_python_automation_tools/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter1_python_automation_tools) | *Python-Based Automation Tools for Semiconductor Design* | Develop Python scripts to automate SPICE simulations, reliability model evaluations, and report analysis in conjunction with the Sky130 PDK and OpenLane flow. |
| 🛠 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter2_sky130_experiments/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter2_sky130_experiments) | *Sky130 Experiments and SPICE-Based Characterization* | Use the SkyWater Sky130 PDK to evaluate MOS characteristics (Vg–Id curves, Vth extraction) and predict BTI/TDBB, performing SPICE-based design verification. |
| 🛠 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter3_openlane_practice/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter3_openlane_practice) | *Digital Design Practice Using OpenLane* | Experience the LSI design flow from Verilog RTL to GDS generation, understanding the objectives and tools for synthesis, placement, routing, and DRC. |
| 🛠 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter4_poc_spec_and_design/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter4_poc_spec_and_design) | *PoC Specifications and Design Implementation* | Using minimal PoC circuits (FSM/MUX/Adder) with the Sky130 PDK, experience the process from specification creation to RTL design and physical implementation. |
| 🛠 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter5_evaluation_and_report/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter5_evaluation_and_report) | *Evaluation and Reporting of Design Results* | Evaluate implemented PoC circuits by analyzing simulation results, area/timing metrics, DRC/LVS checks, and propose improvements as part of the design feedback cycle. |

---

## 📦 **Special Topics**  
> Focuses on cutting-edge topics such as advanced nodes, chiplets, and integrated control SoCs.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 📦 **Chapter 1**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter1_finfet_gaa/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter1_finfet_gaa) | *Advanced Node Technologies – FinFET, GAA & CFET* | Comprehensively explains the physical and electrical characteristics and design impacts of FinFET, GAA, and CFET structures, introducing advanced CMOS technologies beyond planar MOS limits. |
| 📦 **Chapter 2**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2_chiplet_pkg/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2_chiplet_pkg) | *Chiplets and Advanced Packaging* | Covers 2.5D/3D integration, TSV, and heterogeneous integration for chiplet architecture design, implementation, and reliability, enabling flexible design and scalability. |
| 📦 **Chapter 2a**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter2a_systemdk/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter2a_systemdk) | *Design Handling of Thermal, Stress, and Noise Constraints in SystemDK* | Explains the concept of SystemDK and methods for addressing physical constraints such as SI/PI, thermal, stress, and EMI/EMC in design. |
| 📦 **Chapter 3**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter3_socsystem/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter3_socsystem) | *SoC Implementation of Integrated Control System with FSM × PID × LLM* | Based on the AITL-H three-layer control architecture, learn methods for functional separation, hierarchical collaboration, and SoC integration. |
| 📦 **Chapter 4**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter4_openlane/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter4_openlane) | *RTL-to-GDSII Implementation of FSM×PID×LLM Control System with OpenLane* | Using the Sky130 PDK, implement placement and routing (RTL-to-GDSII) for FSM, PID, and integrated SoC modules. |
| 📦 **Chapter 5**<br>[![View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/f_chapter5_dfm/)<br>[![View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/f_chapter5_dfm) | *Physical Verification and DFM Design Guidelines with PDK* | Perform layout verification with the Sky130 PDK and acquire DFM design guidelines considering manufacturability. |

---

## 🔗 **Related Projects**
> Sister projects linked with Edusemi, covering control theory, socio-industrial structures, and advanced technologies.

| 🌐 Project | Overview | Key Features |
|---|---|---|
| ➕ **Edusemi-Plus**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-Plus/en/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-Plus) | Applied learning materials analyzing geopolitics, product strategy, AI, quantum, and investment. | - In-depth analysis of Apple Silicon, CHIPS Act, and Cryo-CMOS<br>- Explores not only technology but also its societal context and background |
| 🎛️ **EduController**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/en/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/EduController) | Covers control theory (PID, state-space) to AI control (NN, RL, LLM). | - Linked with PoC design and OpenLane control implementation<br>- Design exercises in Python, RTL verification, FSM generation support |
| 🤖 **AITL-H**<br>[![🌐 View Site](https://img.shields.io/badge/View-Site-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/en/) [![💻 View Repo](https://img.shields.io/badge/View-Repo-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) | Three-layer control architecture: FSM (instinct) + PID (reason) + LLM (intelligence). | - PoC implementation for humanoid robot integrated control<br>- Structurally linked with Edusemi Special Edition Chapters 3 & 4 |

---

## 👤 **Author**
> Author with professional background in semiconductors and inkjet actuators, creating materials integrating theory and practice.

| 📌 Item | Details |
|------|------|
| **Name** | Shinichi Samizo |
| **Education** | M.Eng., Electrical and Electronic Engineering, Shinshu University |
| **Career** | Former engineer at Seiko Epson Corporation (1997–) |
| **Expertise** | Semiconductor devices (logic, memory, high-voltage mixed)<br>Thin-film piezoelectric actuators for inkjet<br>PrecisionCore printhead productization, BOM management, ISO training |
| **Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---


## 📄 **License**
> Adopts a hybrid licensing model according to the nature of the materials, code, and diagrams.  
> *Hybrid licensing based on the nature of the materials, code, and diagrams.*

| 📌 Item | License | Description |
|------|------|------|
| **Code** | [**MIT License**](https://opensource.org/licenses/MIT) | Free to use, modify, and redistribute |
| **Text materials** | [**CC BY 4.0**](https://creativecommons.org/licenses/by/4.0/) or [**CC BY-SA 4.0**](https://creativecommons.org/licenses/by-sa/4.0/) | Attribution required, share-alike for BY-SA |
| **Figures & diagrams** | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) | Non-commercial use only |
| **External references** | Follow the original license | Cite the original source |

---

## 💬 **Feedback**
> Propose improvements or start discussions via GitHub Discussions.

[![💬 GitHub Discussions](https://img.shields.io/badge/💬%20GitHub-Discussions-brightgreen?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
