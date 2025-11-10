---
layout: default
title: 実践編 第0章 環境構築とツールセットの準備
---

# 🛠️ 実践編 第0章：環境構築とツールセットの準備  
**Practical Chapter 0: Environment Setup and Toolchain Preparation**

## 🔗 公式リンク / *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | https://samizo-aitl.github.io/Edusemi-v4x/e_chapter0_environment_setup/ | https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter0_environment_setup |

## 📘 概要｜Overview

本章では、後続の **第1〜第6章のすべての実践内容**  
（Python 自動化、Sky130 PDK 実験、SPICE 解析、OpenLane 設計、PoC 実装）を確実に進めるための  
**完全な開発環境セットアップ手順**を提供します。

This chapter prepares the **full toolchain** necessary for all practical chapters (1–6),  
including Python automation, Sky130 experiments, SPICE simulations, and OpenLane digital design.

## 🎯 目的｜Objectives

- ✅ Python・VS Code の開発環境構築  
- ✅ Sky130 PDK（volare）と SPICE モデルの導入  
- ✅ OpenLane（Docker + WSL2）の実行環境準備  
- ✅ Magic / Netgen / KLayout の DRC・LVS・GDS ビュー環境  
- ✅ GitHub Pages（教材公開）のビルド環境  

## 🧰 必須ツール一覧｜Required Tools

- Python 3.10+
- VS Code + Python Extension
- Git / GitHub
- ngspice
- Sky130A PDK (volare)
- Docker Desktop
- WSL2 + Ubuntu 22.04
- Magic / Netgen
- KLayout

## 📂 フォルダ構成例｜Folder Structure

e_chapter0_environment_setup/  
 ├── 01_python_setup/  
 ├── 02_sky130_pdk_setup/  
 ├── 03_ngspice_setup/  
 ├── 04_openlane_setup/  
 ├── 05_magic_netgen_setup/  
 ├── 06_klayout_setup/  
 └── 07_github_pages_setup/

## 👤 Author & License

Author: 三溝 真一 (Shinichi Samizo)  
GitHub: https://github.com/Samizo-AITL  
License: MIT / CC BY 4.0 / CC BY-NC 4.0
