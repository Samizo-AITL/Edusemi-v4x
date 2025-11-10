---
layout: default
title: 実践編 第0章 環境構築とツールセットの準備
---

---

# 🛠️ 実践編 第0章：環境構築とツールセットの準備  
**Practical Chapter 0: Environment Setup and Toolchain Preparation**

---

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4/e_chapter0_environment_setup/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter0_environment_setup) |

---

## 📘 概要｜*Overview*

本章では、後続の **第1〜第6章の実践内容**（Python 自動化、Sky130 PDK 実験、SPICE 解析、OpenLane 設計）を  
確実に進めるための **完全な開発環境セットアップ手順**を提供します。

This chapter prepares the **full toolchain** necessary for all practical chapters (1–6),  
including Python automation, Sky130 experiments, SPICE simulations, and OpenLane digital design.

---

## 🎯 目的｜*Objectives*

- ✅ Python・VS Code の開発環境構築  
- ✅ Sky130 PDK（volare）と SPICE モデルの導入  
- ✅ OpenLane（Docker + WSL2）の実行環境準備  
- ✅ Magic / Netgen / KLayout の DRC・LVS・GDS ビュー環境  
- ✅ GitHub Pages（教材公開）のビルド環境  

---

## 🧰 必須ツール一覧｜*Required Tools*

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Automation, plotting |
| VS Code | Coding, Jupyter |
| Git / GitHub | Version control |
| ngspice | SPICE simulation |
| Sky130A PDK (volare) | SPICE models / Magic tech |
| Docker Desktop | OpenLane container |
| WSL2 + Ubuntu 22.04 | OpenLane runtime |
| Magic / Netgen | DRC / LVS |
| KLayout | GDS viewer |

---

## 📂 第0章フォルダ構成｜*Folder Structure*

```
e_chapter0_environment_setup/
 ├── 01_python_setup.md
 ├── 02_sky130_pdk_setup.md
 ├── 03_ngspice_setup.md
 ├── 04_vscode_setup.md
 ├── 05_wsl_docker_setup.md
 ├── 06_openlane_first_run.md
 ├── 07_magic_lvs_drc_setup.md
 ├── 08_klayout_viewer_setup.md
 └── 09_complete_environment_checklist.md
```

---

## 🔗 各節へのリンク｜*Links to Each Section*

| 節 / Section | 内容 / Description | リンク |
|-------------|-------------------|--------|
| ✅ 01 Python Setup | Python / VS Code 構築 | [📄 Open](01_python_setup.md) |
| ✅ 02 Sky130 PDK Setup | volare・PDK導入 | [📄 Open](02_sky130_pdk_setup.md) |
| ✅ 03 ngspice Setup | SPICE シミュレータ | [📄 Open](03_ngspice_setup.md) |
| ✅ 04 VS Code Setup | 統合開発環境 | [📄 Open](04_vscode_setup.md) |
| ✅ 05 WSL2 + Docker Setup | OpenLane 基盤 | [📄 Open](05_wsl_docker_setup.md) |
| ✅ 06 OpenLane First Run | Verilog→GDS | [📄 Open](06_openlane_first_run.md) |
| ✅ 07 Magic / Netgen Setup | DRC / LVS | [📄 Open](07_magic_lvs_drc_setup.md) |
| ✅ 08 KLayout Viewer Setup | GDS Viewer | [📄 Open](08_klayout_viewer_setup.md) |
| ✅ 09 Total Checklist | 総合確認 | [📄 Open](09_complete_environment_checklist.md) |

---

## 🗺️ 第0章 全体構成図｜*Overall Architecture Diagram*

```mermaid
graph TD
    A[Python Setup] --> B[Sky130 PDK Setup]
    B --> C[ngspice Setup]
    C --> D[VS Code Integrations]
    D --> E[WSL2 + Docker Setup]
    E --> F[OpenLane First Run]
    F --> G[Magic / Netgen Setup]
    G --> H[KLayout Viewer Setup]
    H --> I[Complete Checklist]

    style A fill:#e3f2fd,stroke:#1565c0
    style B fill:#e8f5e9,stroke:#2e7d32
    style C fill:#fffde7,stroke:#f9a825
    style D fill:#ffecb3,stroke:#ef6c00
    style E fill:#fce4ec,stroke:#c2185b
    style F fill:#ede7f6,stroke:#4527a0
    style G fill:#e1f5fe,stroke:#0288d1
    style H fill:#fff3e0,stroke:#ef6c00
    style I fill:#c8e6c9,stroke:#2e7d32
```

---

## 👤 Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | https://github.com/Samizo-AITL |
| **License** | MIT / CC BY 4.0 / CC BY-NC 4.0 |
