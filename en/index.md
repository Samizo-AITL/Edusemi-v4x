---
layout: default
title: Edusemi-v4x/en/README.md
---

---

# 🎓 **Edusemi-v4x: Foundational Educational Materials for Semiconductor Product Development**

🇯🇵 **[日本語版 README](../README.md)**  
　 *Japanese version with full structure and chapter descriptions*

---

✍️ **Introduction**

The evolution of **semiconductor technology** began with the **invention of the transistor** and accelerated with the **advent of the MOS structure**.  
Driven by **Moore's Law**, **miniaturization and integration** have enabled the proliferation of **LSI** across all industries.

However, in practice, fields such as **materials science**, **circuit design**, **process technology**, and **testing** are often taught in isolation.  
Yet these domains are **deeply interconnected**—**circuit behavior** depends on **device physics**, and **design feasibility** hinges on **process capabilities and reliability**.

**Edusemi** addresses this by emphasizing the **structural interconnections** between foundational technologies.  
While keeping an eye on application domains, the focus is on cultivating a **deep, practical understanding** of how these fundamentals work **together**.

---

## 📘 **Project Overview**

**Edusemi-v4x** is an **open-source curriculum project** designed to teach the **fundamentals of semiconductor design, fabrication, testing, and quality assurance** in a **systematic and hands-on way**.

- 🎯 **Target Audience**: Engineering students, junior engineers, educators  
- ⭐ **Key Features**: Emphasis on **interconnected fundamentals**, full-stack understanding from **circuit design to mass production**  
- 🧪 **Practical Tools**: Exercises using **sky130**, **OpenLane**, **Python**, **GitHub**, and **interactive ChatGPT learning**

---

## 🧭 **Foundations Track: Chapter Overview**

| Chapter | **Title** | **Description** |
|---------|-----------|-----------------|
| [1](../chapter1_materials/README.md) | **Fundamentals of Semiconductor Materials** | **Band structure**, **PN junctions**, **MOS field-effect principles** |
| [2](../chapter2_comb_logic/README.md) | **Digital Logic and Circuit Design** | **Combinational** / **sequential logic**, **FSMs**, **HDL basics** |
| [3](../chapter3_process_evolution/README.md) | **Process Technology and Scaling Limitations** | **Node evolution**, **interconnects**, **lithography**, **device variability** |
| [4](../chapter4_mos_characteristics/README.md) | **MOS Transistor Characteristics and Design Foundations** | **Dimensions**, **PDK**, **design rules**, **reliability** |
| [5a](../chapter5a_spec_module_if/README.md) | **Specification, Module Selection, and Interface Design** | Covers **upstream process, IF design, and PoC linkage** |
| [5](../chapter5_soc_design_flow/README.md) | **SoC Design Flow and EDA Tools** | **RTL**, **synthesis**, **place & route**, **DRC/LVS**, **timing analysis** |
| [6](../chapter6_test_and_package/README.md) | **Testing, Packaging, and Productization** | **ETEST**, **wafer test**, **failure analysis**, **reliability qualification** |
| [7](../chapter7_design_review_and_org/README.md) | **Design Reviews and Organizational Collaboration** | **DR processes**, **defect case studies**, **SRAM failures**, **team consensus** |

---

## 🧩 **Advanced Track: Chapter Overview**

| Chapter | **Title** | **Description** |
|---------|-----------|-----------------|
| [1](../d_chapter1_memory_technologies/README.md) | **Memory Technologies** | **SRAM**, **DRAM**, **FeRAM**, **MRAM** — structures, characteristics, SoC relevance |
| [2](../d_chapter2_high_voltage_devices/README.md) | **High-Voltage Devices** | **LDMOS**, **field-controlled structures**, **device design** for HV |
| [3](../d_chapter3_esd_protection_design/README.md) | **ESD Protection Design** | **Protection devices**, **ESD test methods**, **layout guidelines** |
| [4](../d_chapter4_layout_optimization/README.md) | **Layout Design and Optimization** | **CMP dummy fill**, **IR drop**, **latch-up**, **physical design tuning** |
| [5](../d_chapter5_analog_mixed_signal/README.md) | **Analog / Mixed-Signal Design** | **Analog blocks**, **noise**, **mixed-signal layout challenges** |
| [5a](../d_chapter5a_analog_mixed_signal/README_en.md) | **0.18μm AMS Design Techniques** | Design-level optimizations: **mismatch, flicker noise, Q-factor improvement**, etc. |
| [5b](../d_chapter5b_ams_block_and_pdk/README.md) | **Analog Differentiation via Process** | Creating **low 1/f noise AMS modules** through manufacturing innovation |
| [6](../d_chapter6_pdk_and_eda_environment/README.md) | **PDK and EDA Environments** | **PDK components**, **EDA workflows**, **DRC/LVS/ERC** integration |
| [7](../d_chapter7_automation_and_verification/README.md) | **Automation and Verification Techniques** | **Linting**, **OpenLane validation**, **CI/CD**, **log analysis** |
| [8](../d_chapter8_fsm_design_basics/README.md) | **FSM Design (Finite State Machines)** | **Moore / Mealy models**, **state diagrams**, **Verilog code** |
| [9](../d_chapter9_pll_and_clock_design/README.md) | **PLL and Clock Design** | **PLL architecture**, **frequency synthesis**, **jitter/skew**, **STA** considerations |

---

## 🛠 **Practice Track: Chapter Overview**

| Chapter | **Title** | **Description** |
|---------|-----------|-----------------|
| [1](../e_chapter1_python_automation_tools/README.md) | **Python Tools for Automation** | **SPICE simulation**, **characteristic plotting**, **OpenLane log parsing** |
| [2](../e_chapter2_sky130_experiments/README.md) | **Sky130 Experiments and SPICE Evaluation** | **Vg–Id curves**, **Vth estimation**, **BTI/TDDB reliability** |
| [3](../e_chapter3_openlane_practice/README.md) | **Digital Design Practice with OpenLane** | **RTL-to-GDSII**, **synthesis**, **P&R**, **report interpretation** |
| [4](../e_chapter4_poc_spec_and_design/README.md) | **PoC Specifications and Design Expansion** | **FSM**, **MUX**, **Adder** — PoC specs and **testbench-based Verilog design** |
| [5](../e_chapter5_evaluation_and_report/README.md) | **Evaluation and Reporting of Design Results** | **Waveform**, **area**, **timing**, **DRC/LVS** review and proposals |

---

## 📦 **Special Topics Track: Chapter Overview**

| Chapter | **Title** | **Description** |
|---------|-----------|-----------------|
| [1](../f_chapter1_finfet_gaa/README.md) | **Advanced Node Technologies (FinFET, GAA, CFET)** | **Transistor structures**, **scaling strategies**, and **design implications** |
| [2](../f_chapter2_chiplet_pkg/README.md) | **Chiplet and Advanced Packaging Technologies** | **2.5D/3D integration**, **TSV**, **interposer**, **heterogeneous systems** |
| [2a](../f_chapter2a_systemdk/README.md) | **SystemDK and Physical Constraint Management** | **Signal/power integrity**, **thermal**, **mechanical**, and **EMI/EMC-aware design integration** |
| [3](../f_chapter3_socsystem/README.md) | **SoC Implementation of FSM × PID × LLM Control** | Applying **AITL architecture** to **integrated control SoCs** |
| [4](../f_chapter4_openlane/README.md) | **RTL-to-GDSII Implementation of AITL Control Logic** | **OpenLane layout**, **DRC**, **integration verification** |
| [5](../f_chapter5_dfm/README.md) | **DFM and Physical Verification Using PDK** | **Sky130 PDK**, **LVS**, **DFM best practices**, **manufacturing readiness** |

---

## 📘 **Related Documentation**

- 📄 [Introduction (Concept and Purpose)](../introduction.md)  
- 📄 [Revision History (ChangeLog)](../revision_history.md)

