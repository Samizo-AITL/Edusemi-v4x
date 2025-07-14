# 🎓 Edusemi-v4x: Foundational Educational Materials for Semiconductor Product Development

✍️ **Introduction**

The evolution of semiconductor technology began with the invention of the transistor and rapidly accelerated with the advent of the MOS structure.  
Driven by Moore's Law, miniaturization and integration have enabled the proliferation of LSI across all industries.

However, in the real world of engineering, disciplines such as **materials science, circuit design, process technology, and testing** are often taught in isolation.  
In practice, these fields are **closely interconnected**—circuit behavior relies on device physics, and design feasibility depends on process capabilities and reliability.

**Edusemi** addresses this gap by focusing on the **structural interconnections between foundational technologies**.  
While maintaining awareness of advanced applications, the emphasis remains on cultivating a **deep, structural understanding** of core semiconductor technologies—making the knowledge immediately useful in real-world development.

---

## 📘 Project Overview

**Edusemi-v4x** is an open-source educational project designed to teach the **fundamentals of semiconductor design, fabrication, testing, and quality assurance** in an integrated and practical manner.

- **Target Audience**: Engineering students, junior engineers, and educators  
- **Key Features**: Emphasis on interconnection of basics, full-stack understanding from circuit design to mass production  
- **Hands-On Support**: Modern learning approach using **sky130, OpenLane, Python, GitHub**, and **interactive learning with ChatGPT**

---

## 🧭 Foundations Track: Chapter Overview

| Chapter | Title | Description |
|---------|-------|-------------|
| [1](chapter1_materials/README.md) | Fundamentals of Semiconductor Materials | Band structure, PN junctions, MOS field-effect principles |
| [2](chapter2_comb_logic/README.md) | Digital Logic and Circuit Design | Combinational and sequential logic, FSMs, HDL basics |
| [3](chapter3_process_evolution/README.md) | Process Technology and Scaling Limitations | Node evolution, interconnects, lithography, reliability |
| [4](chapter4_mos_characteristics/README.md) | MOS Transistor Characteristics and Design Foundations | Device dimensions, PDKs, design rules, performance metrics |
| [5](chapter5_soc_design_flow/README.md) | SoC Design Flow and EDA Tools | RTL design, synthesis, place & route, DRC/LVS, timing analysis |
| [6](chapter6_test_and_package/README.md) | Testing, Packaging, and Productization | ETEST, wafer probing, failure analysis, reliability testing |
| [7](chapter7_design_review_and_org/README.md) | Design Reviews and Organizational Collaboration | DR structure, case studies, defect examples, consensus building |

---

## 🧩 Advanced Track: Chapter Overview

| Chapter | Title | Description |
|---------|-------|-------------|
| [1](d_chapter1_memory_technologies/README.md) | Memory Technologies | SRAM, DRAM, FeRAM, MRAM—structures, features, and SoC relevance |
| [2](d_chapter2_high_voltage_devices/README.md) | High-Voltage Devices | LDMOS and field control structures for high-voltage operation |
| [3](d_chapter3_esd_protection_design/README.md) | ESD Protection Design | Basics of ESD, protection devices, layout considerations |
| [4](d_chapter4_layout_optimization/README.md) | Layout Design and Optimization | CMP dummy fill, IR drop, latch-up prevention, physical strategies |
| [5](d_chapter5_analog_mixed_signal/README.md) | Analog / Mixed-Signal Design | Analog block design, noise, layout challenges in mixed-signal systems |
| [6](d_chapter6_pdk_and_eda_environment/README.md) | PDK and EDA Environments | Structure of PDKs, EDA integration, DRC/LVS/ERC workflows |
| [7](d_chapter7_automation_and_verification/README.md) | Automation and Verification Techniques | Linting, OpenLane verification, log analysis, CI/CD practices |
| [8](d_chapter8_fsm_design_basics/README.md) | FSM Design (Finite State Machines) | Moore/Mealy models, state diagrams, Verilog implementation |
| [9](d_chapter9_pll_and_clock_design/README.md) | PLL and Clock Design | PLL architecture, frequency synthesis, jitter/skew, STA considerations |

---

## 🛠 Practice Track: Chapter Overview

| Chapter | Title | Description |
|---------|-------|-------------|
| [1](e_chapter1_python_automation_tools/README.md) | Python Tools for Automation | SPICE simulation, characteristic plotting, OpenLane log analysis |
| [2](e_chapter2_sky130_experiments/README.md) | Sky130 Experiments and SPICE Evaluation | Vg–Id curves, threshold voltage (Vth) estimation, BTI/TDDB analysis |
| [3](e_chapter3_openlane_practice/README.md) | Digital Design Practice with OpenLane | RTL-to-GDS flow with synthesis, place & route, and report analysis |
| [4](e_chapter4_poc_spec_and_design/README.md) | PoC Specifications and Design Expansion | FSM, MUX, Adder—PoC specs and Verilog implementation with testbenches |
| [5](e_chapter5_evaluation_and_report/README.md) | Evaluation and Reporting of Design Results | Waveform, area/timing/DRC evaluation and improvement proposals |

---

## 📦 Special Topics Track: Chapter Overview

| Chapter | Title | Description |
|---------|-------|-------------|
| [1](f_chapter1_finfet_gaa/README.md) | Advanced Nodes (FinFET, GAA, etc.) | Physics and design impacts of next-gen transistors |
| [2](f_chapter2_chiplet_pkg/README.md) | Chiplet and Advanced Packaging Technologies | 2.5D/3D integration, TSVs, interposers in heterogeneous systems |
| [3](f_chapter3_socsystem/README.md) | SoC Implementation of FSM × PID × LLM Control System | Application of AITL architecture in integrated control SoCs |
| [4](f_chapter4_openlane/README.md) | OpenLane-Based RTL-to-GDSII Implementation of Control Systems | Layout and DRC of integrated control logic |
| [5](f_chapter5_dfm/README.md) | Physical Verification and DFM Strategies | DRC/LVS/DFM techniques using Sky130 PDK |
| [6](f_chapter6_actuator_system/README.md) | Piezo Actuator Control System Design | Polarization, hysteresis compensation, FSM control, COF implementation |
| [7](f_chapter7_product_docs/README.md) | Product Documentation and Workflow in Final Products | BOM management, prototyping, evaluation, DR & mass production gates |

---

## 🤖 Integration with ChatGPT

Edusemi is designed with **ChatGPT integration** as a learning partner.  
Learners can get support in code reviews, error diagnostics, tool usage, conceptual explanations, experiment reporting, and more.

This **interactive and industry-aligned approach** bridges theory and practice—preparing learners for modern semiconductor development.

---

## 🔗 Related Projects

### 🎛️ [EduController](https://github.com/Samizo-AITL/EduController)

A comprehensive control education platform covering classic PID, modern state-space, H∞, and AI control (NN, RL, LLM integration).  
- Python-based design and verification practice  
- Integrated with Edusemi’s PoC specs and SoC implementation topics  
- End-to-end support from design to RTL-to-GDSII flows

### 🤖 [AITL-H](https://github.com/Samizo-AITL/AITL-H)

A hybrid intelligent control framework combining FSM (instinct), PID (reason), and LLM (intelligence).  
- Designed for adaptive robots and intelligent systems  
- Aligned with Edusemi Special Topics chapters on SoC and OpenLane design  
- Supports cross-domain control and SoC development learning

### 🌐 [Edusemi-Plus](https://github.com/Samizo-AITL/edusemi-plus)

An applied extension of Edusemi focused on **geopolitics, market trends, corporate strategies, and emerging technologies**.  
- Includes topics like US-China tensions, TSMC strategy, AI/quantum chips, Apple Silicon  
- Emphasizes the societal and strategic context of semiconductor technology  
- Designed for engineers, educators, and decision-makers

---

## 📘 Related Documentation

- [Introduction (Concept and Purpose)](introduction.md)  
- [Revision History (ChangeLog)](revision_history.md)

---

## 🧑‍🔬 Author Profile

- **Name**: Shinichi Samizo  
- **Education**: M.E. in Electrical and Electronic Engineering, Shinshu University Graduate School  
- **Career**:
  - Joined Seiko Epson Corporation in 1997  
  - Worked on:
    - Semiconductor device technologies (0.35μm–0.18μm nodes)  
    - Logic/memory devices, high-voltage integration  
    - Inkjet thin-film piezo actuators  
    - Productization of PrecisionCore printhead technology  
- **Contact**:  
  - GitHub: [Samizo-AITL](https://github.com/Samizo-AITL)  
  - Email: [shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---

## 📄 License

This project is released under the **MIT License**.  
Free to use, modify, and redistribute. Educational and corporate training use is welcome.

---

💬 [Join the Discussion on Edusemi → GitHub Discussions](https://github.com/Samizo-AITL/Edusemi-v4x/discussions)
