---
layout: default
title: Edusemi-v4x/en/README.md
---

---

# 🎓 **Edusemi-v4x | Foundational Educational Materials for Semiconductor Product Development**  
🇯🇵 *半導体プロダクト開発のための基礎教育教材*

---

## 🔗 **Official Links**


| 言語 | 種別 | リンク |
|------|------|--------|
| 🇺🇸 English Version | 🌐 GitHub Pages | [https://samizo-aitl.github.io/Edusemi-v4x/en/](https://samizo-aitl.github.io/Edusemi-v4x/en/) |
| 🇺🇸 English Version | 💻 GitHub | [https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/en) |
| 🇯🇵 Japanese Version | 🌐 GitHub Pages | [https://samizo-aitl.github.io/Edusemi-v4x/](https://samizo-aitl.github.io/Edusemi-v4x/) |
| 🇯🇵 Japanese Version | 💻 GitHub | [https://github.com/Samizo-AITL/Edusemi-v4x](https://github.com/Samizo-AITL/Edusemi-v4x) |

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
> Systematically covers **semiconductor physics, logic design, and process technology**—the foundation of all applications.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧭 **[1](../chapter1_materials/README.md)** | **Semiconductor Physics & Materials** | Band structure, PN junction, MOS field effect |
| 🧭 **[2](../chapter2_comb_logic/README.md)** | **Digital Logic & Circuit Design** | Combinational/sequential circuits, FSM, HDL |
| 🧭 **[3](../chapter3_process_evolution/README.md)** | **Process Technology & Scaling** | Node evolution, interconnect, lithography, reliability |
| 🧭 **[4](../chapter4_mos_characteristics/README.md)** | **MOS Characteristics** | Dimensions, characteristics, PDK, design rules |
| 🧭 **[5a](../chapter5a_spec_module_if/README.md)** | **Spec Definition & Interface Design** | Upstream process, module selection, PoC connectivity |
| 🧭 **[5](../chapter5_soc_design_flow/README.md)** | **SoC Design Flow** | RTL, P&R, DRC/LVS, timing |
| 🧭 **[6](../chapter6_test_and_package/README.md)** | **Test & Packaging** | ETEST, failure analysis, reliability testing, shipment |
| 🧭 **[7](../chapter7_design_review_and_org/README.md)** | **Design Review & Collaboration** | SRAM failure cases, DR structure, consensus building |

---

## 🧩 **Applications**
> Builds on fundamentals to cover **memory, high-voltage, ESD, and analog/mixed-signal design**.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🧩 **[1](../d_chapter1_memory_technologies/README.md)** | **Memory Technologies** | SRAM, DRAM, FeRAM, MRAM |
| 🧩 **[2](../d_chapter2_high_voltage_devices/README.md)** | **High-Voltage Devices** | LDMOS, field control, high-voltage design |
| 🧩 **[3](../d_chapter3_esd_protection_design/README.md)** | **ESD Protection Design** | Protection devices, failure cases, test standards |
| 🧩 **[4](../d_chapter4_layout_optimization/README.md)** | **Layout Optimization** | CMP dummy, IR drop, latch-up |
| 🧩 **[5](../d_chapter5_analog_mixed_signal/README.md)** | **Analog / Mixed-Signal** | Analog design, noise, mixed integration |
| 🧩 **[5a](../d_chapter5a_analog_mixed_signal/README.md)** | **0.18μm AMS Design** | Variability, matching, 1/f noise |
| 🧩 **[5b](../d_chapter5b_ams_block_and_pdk/README.md)** | **AMS Differentiation from Manufacturing** | 1/f noise reduction, leveraging manufacturing |
| 🧩 **[6](../d_chapter6_pdk_and_eda_environment/README.md)** | **PDK & EDA Environment** | DRC/LVS/ERC, PDK structure |
| 🧩 **[7](../d_chapter7_automation_and_verification/README.md)** | **Automation & Verification** | OpenLane, CI/CD, lint |
| 🧩 **[8](../d_chapter8_fsm_design_basics/README.md)** | **FSM Design** | Moore/Mealy, state diagrams, Verilog |
| 🧩 **[9](../d_chapter9_pll_and_clock_design/README.md)** | **PLL & Clock Design** | PLL structure, jitter, STA considerations |

---

## 🛠 **Practice**
> Hands-on training through **Python automation, Sky130 experiments, and OpenLane implementation**.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 🛠 **[1](../e_chapter1_python_automation_tools/README.md)** | **Python Automation Tools** | SPICE analysis, OpenLane log processing |
| 🛠 **[2](../e_chapter2_sky130_experiments/README.md)** | **Sky130 Experiments** | Vg–Id, Vth estimation, BTI/TDDB evaluation |
| 🛠 **[3](../e_chapter3_openlane_practice/README.md)** | **OpenLane Practice** | Synthesis → P&R → GDS output |
| 🛠 **[4](../e_chapter4_poc_spec_and_design/README.md)** | **PoC Design Development** | FSM, MUX, adder, testing |
| 🛠 **[5](../e_chapter5_evaluation_and_report/README.md)** | **Evaluation & Reporting** | Area, waveform, timing, DRC/LVS |

---

## 📦 **Special Topics**
> Focuses on **advanced nodes, chiplets, integrated control SoCs**, and other frontier topics.

| 📖 Chapter | 📚 Title | 📝 Summary |
|----|--------|---------|
| 📦 **[1](../f_chapter1_finfet_gaa/README.md)** | **Advanced Nodes** | FinFET, GAA, CFET and their design impacts |
| 📦 **[2](../f_chapter2_chiplet_pkg/README.md)** | **Chiplets & Advanced Packaging** | 2.5D/3D, TSV, heterogeneous integration |
| 📦 **[2a](../f_chapter2a_systemdk/README.md)** | **SystemDK Design Constraints** | SI/PI, thermal, stress, EMI/EMC |
| 📦 **[3](../f_chapter3_socsystem/README.md)** | **Integrated Control SoC** | FSM × PID × LLM (AITL) |
| 📦 **[4](../f_chapter4_openlane/README.md)** | **OpenLane Implementation** | P&R of integrated control RTL |
| 📦 **[5](../f_chapter5_dfm/README.md)** | **Design for Manufacturability** | DRC, LVS, DFM guidelines, Sky130 |

---

| 🌐 Project | Overview | Key Features |
|------------|----------|--------------|
| 📚 [**Edusemi-Plus**](https://samizo-aitl.github.io/Edusemi-Plus/) <br>💻 [GitHub](https://github.com/Samizo-AITL/Edusemi-Plus) | Applied learning materials analyzing geopolitics, product strategy, AI, quantum, and investment. | - Case studies on Apple Silicon, CHIPS Act, and Cryo-CMOS<br>- Explores not only technology but also its social context and background |
| 🎛️ [**EduController**](https://samizo-aitl.github.io/EduController/) <br>💻 [GitHub](https://github.com/Samizo-AITL/EduController) | Covers control theory (PID, state-space) to AI control (NN, RL, LLM). | - PoC design linked with OpenLane control implementation<br>- Design exercises, RTL verification, and FSM generation support in Python |
| 🤖 [**AITL-H**](https://samizo-aitl.github.io/AITL-H/) <br>💻 [GitHub](https://github.com/Samizo-AITL/AITL-H) | Three-layer control architecture: FSM (instinct) + PID (reason) + LLM (intelligence). | - PoC implementation for humanoid robots and integrated control<br>- Structurally linked with Edusemi special editions 3 & 4 |

---

## 👤 **Author**

| 📌 Item | Details |
|--------|---------|
| **Name** | Shinichi Samizo |
| **Education** | M.Eng., Electrical & Electronic Engineering, Shinshu University |
| **Career** | Former engineer at Seiko Epson Corporation (1997–) |
| **Expertise** | Semiconductor devices (logic, memory, HV mixed integration)<br>Inkjet thin-film piezo actuators<br>PrecisionCore printhead productization, BOM management, ISO training |
| **Contact** | ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)<br>🐦 [https://x.com/shin3t72](https://x.com/shin3t72)<br>💻 [https://samizo-aitl.github.io/](https://samizo-aitl.github.io/) |

---

## 📄 **License**

| 📌 Item | Details |
|--------|---------|
| **Type** | MIT License |
| **Usage** | Free to use, modify, and redistribute |
| **Recommended Uses** | Education, research, corporate training |

---

## 💬 **Feedback & ChangeLog**

💬 **[Discuss Edusemi materials → Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)**  
📄 **[Revision History / ChangeLog](../revision_history.md)**
