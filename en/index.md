---
layout: default
title: Edusemi-v4x/en/README.md
---

<!-- Page-specific CSS (works from any directory) -->
<link rel="stylesheet" href="{{ '/assets/css/edusemi.css' | relative_url }}"/>

# 🎓 Edusemi-v4x  
**Foundational Educational Materials for Semiconductor Product Development**

<a class="btn-link" href="../">🇯🇵 Japanese index →</a>

---

## ✍️ Introduction

The evolution of **semiconductor technology** began with the **invention of the transistor** and accelerated with the **advent of the MOS structure**.  
Driven by **Moore’s Law**, **miniaturization and integration** have enabled the proliferation of **LSI** across all industries.

However, in practice, fields such as **materials science**, **circuit design**, **process technology**, and **testing** are often taught in isolation.  
Yet these domains are **deeply interconnected**—**circuit behavior** depends on **device physics**, and **design feasibility** hinges on **process capabilities and reliability**.

**Edusemi-v4x** emphasizes these **structural interconnections**. While keeping an eye on applications, the focus is on cultivating a **practical, integrated understanding** of how fundamentals work **together**.

> 💡 *Design follows physics; productization follows verification.*

---

## 📘 Project Overview

**Edusemi-v4x** is an **open-source curriculum** to learn **semiconductor design, fabrication, testing, and quality assurance** in a **systematic and hands-on** way.

- 🎯 **Audience**: Engineering students, junior engineers, educators  
- 🌟 **Highlights**: Interconnected fundamentals; end-to-end view from **design to mass production**  
- 🧪 **Practical Tools**: sky130 / OpenLane / Python / GitHub / ChatGPT

---

## 🧭 Foundations Track

<table class="nice-table">
  <thead><tr><th>Chapter</th><th>Title</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="../chapter1_materials/README.md">Fundamentals of Semiconductor Materials</a></td><td>Band structure, PN junctions, MOS field effect</td></tr>
    <tr><td>2</td><td><a href="../chapter2_comb_logic/README.md">Digital Logic and Circuit Design</a></td><td>Combinational & sequential logic, FSMs, HDL</td></tr>
    <tr><td>3</td><td><a href="../chapter3_process_evolution/README.md">Process Technology and Scaling Limits</a></td><td>Node evolution, interconnects, lithography, reliability</td></tr>
    <tr><td>4</td><td><a href="../chapter4_mos_characteristics/README.md">MOS Transistor Characteristics</a></td><td>Dimensions, characteristics, PDK, design rules</td></tr>
    <tr><td>5a</td><td><a href="../chapter5a_spec_module_if/README.md">Specification & Interface Design</a></td><td>Upstream process, module selection, PoC linkage</td></tr>
    <tr><td>5</td><td><a href="../chapter5_soc_design_flow/README.md">SoC Design Flow</a></td><td>RTL, synthesis, place & route, DRC/LVS, timing</td></tr>
    <tr><td>6</td><td><a href="../chapter6_test_and_package/README.md">Testing, Packaging, and Productization</a></td><td>ETEST, failure analysis, reliability qualification, shipping</td></tr>
    <tr><td>7</td><td><a href="../chapter7_design_review_and_org/README.md">Design Reviews & Organizational Collaboration</a></td><td>DR processes, SRAM failure cases, consensus building</td></tr>
  </tbody>
</table>

---

## 🧩 Advanced Track

<table class="nice-table">
  <thead><tr><th>Chapter</th><th>Title</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="../d_chapter1_memory_technologies/README.md">Memory Technologies</a></td><td>SRAM, DRAM, FeRAM, MRAM</td></tr>
    <tr><td>2</td><td><a href="../d_chapter2_high_voltage_devices/README.md">High-Voltage Devices</a></td><td>LDMOS, field-controlled structures, HV design</td></tr>
    <tr><td>3</td><td><a href="../d_chapter3_esd_protection_design/README.md">ESD Protection Design</a></td><td>Protection devices, test methods, layout guidelines</td></tr>
    <tr><td>4</td><td><a href="../d_chapter4_layout_optimization/README.md">Layout Design & Optimization</a></td><td>CMP dummy, IR drop, latch-up, tuning</td></tr>
    <tr><td>5</td><td><a href="../d_chapter5_analog_mixed_signal/README.md">Analog / Mixed-Signal</a></td><td>Analog blocks, noise, mixed-signal challenges</td></tr>
    <tr><td>5a</td><td><a href="../d_chapter5a_analog_mixed_signal/README_en.md">0.18μm AMS Design Techniques</a></td><td>Mismatch, 1/f noise, Q-factor improvements</td></tr>
    <tr><td>5b</td><td><a href="../d_chapter5b_ams_block_and_pdk/README.md">Analog Differentiation via Process</a></td><td>Low 1/f noise modules via manufacturing</td></tr>
    <tr><td>6</td><td><a href="../d_chapter6_pdk_and_eda_environment/README.md">PDK & EDA Environments</a></td><td>PDK components, DRC/LVS/ERC, workflows</td></tr>
    <tr><td>7</td><td><a href="../d_chapter7_automation_and_verification/README.md">Automation & Verification</a></td><td>Linting, OpenLane validation, CI/CD, logs</td></tr>
    <tr><td>8</td><td><a href="../d_chapter8_fsm_design_basics/README.md">FSM Design</a></td><td>Moore/Mealy models, state diagrams, Verilog</td></tr>
    <tr><td>9</td><td><a href="../d_chapter9_pll_and_clock_design/README.md">PLL & Clock Design</a></td><td>Architecture, synthesis, jitter/skew, STA</td></tr>
  </tbody>
</table>

---

## 🛠 Practice Track

<table class="nice-table">
  <thead><tr><th>Chapter</th><th>Title</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="../e_chapter1_python_automation_tools/README.md">Python Tools for Automation</a></td><td>SPICE analysis, OpenLane log parsing</td></tr>
    <tr><td>2</td><td><a href="../e_chapter2_sky130_experiments/README.md">Sky130 Experiments & SPICE Evaluation</a></td><td>Vg–Id curves, Vth estimation, BTI/TDDB</td></tr>
    <tr><td>3</td><td><a href="../e_chapter3_openlane_practice/README.md">Digital Design with OpenLane</a></td><td>RTL→GDSII, synthesis, P&R, reports</td></tr>
    <tr><td>4</td><td><a href="../e_chapter4_poc_spec_and_design/README.md">PoC Specifications & Design</a></td><td>FSM, MUX, Adder, testbenches</td></tr>
    <tr><td>5</td><td><a href="../e_chapter5_evaluation_and_report/README.md">Evaluation & Reporting</a></td><td>Area, waveform, timing, DRC/LVS</td></tr>
  </tbody>
</table>

---

## 📦 Special Topics

<table class="nice-table">
  <thead><tr><th>Chapter</th><th>Title</th><th>Description</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="../f_chapter1_finfet_gaa/README.md">Advanced Nodes (FinFET, GAA, CFET)</a></td><td>Structures, scaling, design implications</td></tr>
    <tr><td>2</td><td><a href="../f_chapter2_chiplet_pkg/README.md">Chiplet & Advanced Packaging</a></td><td>2.5D/3D, TSV, interposer, heterogeneous</td></tr>
    <tr><td>2a</td><td><a href="../f_chapter2a_systemdk/README.md">SystemDK: Physical Constraint Design</a></td><td>SI/PI, thermal, mechanical, EMI/EMC</td></tr>
    <tr><td>3</td><td><a href="../f_chapter3_socsystem/README.md">SoC Implementation of FSM × PID × LLM</a></td><td>AITL control applied to SoCs</td></tr>
    <tr><td>4</td><td><a href="../f_chapter4_openlane/README.md">OpenLane Implementation</a></td><td>Layout of integrated control RTL</td></tr>
    <tr><td>5</td><td><a href="../f_chapter5_dfm/README.md">DFM & Physical Verification</a></td><td>DRC/LVS/DFM guidance with Sky130</td></tr>
  </tbody>
</table>

---

## 🤖 Integration with ChatGPT

Use ChatGPT as a **learning partner** for code reviews, error diagnostics, tool guidance, and report support—enabling **interactive, real-world-aligned learning**.

---

## 🔗 Related Projects

<ul class="icon-list">
  <li>🎛️ <a href="https://github.com/Samizo-AITL/EduController">EduController</a> – Control theory to AI control; OpenLane integration</li>
  <li>🤖 <a href="https://github.com/Samizo-AITL/AITL-H">AITL-H</a> – Three-layer control (FSM + PID + LLM)</li>
  <li>🌐 <a href="https://github.com/Samizo-AITL/edusemi-plus">Edusemi-Plus</a> – Geopolitics, strategy, AI, quantum, investment</li>
</ul>

---

## 👤 Author

**Shinichi Samizo**  
M.S. in Electrical and Electronic Engineering, Shinshu University  
Former Seiko Epson Corporation Engineer (since 1997)

📌 Areas of Expertise: Semiconductor devices, thin-film piezo actuators, productization, ISO education  
✉️ <a href="mailto:shin3t72@gmail.com">shin3t72@gmail.com</a> | 🐦 <a href="https://x.com/shin3t72">@shin3t72</a> | 💻 <a href="https://samizo-aitl.github.io/">Website</a>

---

## 📄 License

Licensed under the **MIT License**. Free to use, modify, and redistribute for **education**, **research**, and **corporate training**.

<a class="btn-secondary" href="../revision_history.md">Revision History</a>　
<a class="btn-link" href="https://github.com/Samizo-AITL/Edusemi-v4x/discussions">Discussions →</a>
