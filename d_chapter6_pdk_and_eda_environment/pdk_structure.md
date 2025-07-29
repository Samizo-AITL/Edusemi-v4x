# 📦 PDKの構成とデバイスモデル  
# 📦 Structure of PDK and Device Models

---

## 📘 概要｜Overview

**PDK（Process Design Kit）** は、ある半導体プロセスに対して回路設計を可能にするための、  
**設計ルール・デバイスモデル・ライブラリの統合パッケージ**です。  
本資料では、PDKの構成要素を分類し、その設計上の役割と**実務上の重要性**を解説します。

A **Process Design Kit (PDK)** is an integrated package consisting of **design rules, device models, and libraries**, enabling circuit design for a specific semiconductor process.  
This document categorizes PDK components and explains their design roles and practical importance.

---

## 🧱 PDKの主な構成要素｜Key Components of a PDK

| 🧩 **構成要素｜Component** | 📘 **内容｜Description** | 🔧 **使用フェーズ｜Design Phase** |
|--------------------------|--------------------------|-------------------------------|
| デザインルール<br>Design Rules | 配線幅、層構成、層間距離など<br>Geometry rules (width, spacing, layers) | レイアウト、DRC<br>Layout, DRC |
| スパイスモデル<br>SPICE Models | トランジスタの動作記述（BSIM等）<br>Device behavior models | シミュレーション<br>Simulation |
| レイアウトビュー<br>Layout Views | GDS、LEF等の物理情報<br>Physical cell representations | P&R、DRC/LVS |
| シンボルライブラリ<br>Schematic Symbols | 回路図入力用の記号ライブラリ<br>Symbols for schematic editors | スケマティック設計<br>Schematic design |
| シミュレーションパラメータ<br>Sim Params | 温度・OP条件など補助ファイル<br>Operating point, temperature effects | SPICE解析<br>SPICE analysis |
| DRC/LVSルール<br>DRC/LVS Rules | 検証ルール（形式：Calibre, ICV等）<br>Physical verification rules | 物理検証<br>Verification |
| テクノロジーファイル<br>Tech Files | 層構成・色分け・ビア情報など<br>Layer map, via structure, color map | ビューワ、レイアウト<br>Viewer, layout editing |

---

## 🧪 デバイスモデルの位置づけ｜Role of Device Models

### 🧩 モデルの種類｜Model Types

- **Level 1–7**：古典的MOSモデル（学習向け）  
  *Classic MOS models used in education*
- **BSIM3 / BSIM4**：実用的CMOSモデル（主に0.35μm以降）  
  *Mainstream practical models for modern CMOS*
- **PSP, HiSIM**：65nm以下の先端ノード向けモデル  
  *Advanced models for sub-65nm nodes*

### 📐 モデルに含まれる要素｜What Models Include

- 寸法依存性（L, W）<br>*Length/width scaling*
- 温度依存性、バラツキ（コーナー）<br>*Temperature and corner models*
- ノイズ、寄生、短チャネル効果<br>*Noise, parasitics, short-channel effects*

---

## 🌐 PDKの入手例｜Examples of PDKs

| 🏷️ **PDK名｜PDK Name** | 🏢 **提供元｜Provider** | 🔍 **特徴｜Features** |
|------------------|------------------------|--------------------------|
| **Sky130** | Google + Efabless | OSS対応、教育利用に適す<br>Open-source, ideal for education |
| **TSMC 65nm** | 商用｜Commercial | NDA必須、豊富なAMSマクロ<br>NDA required, full AMS support |
| **GF 22FDX** | GlobalFoundries | FDSOIプロセス、低消費電力向け<br>FDSOI-based, low-power optimized |

---

## 🧰 教材的意義｜Educational Significance

- 回路設計はPDKに強く依存するため、**PDK構造の理解が設計自由度を決定**する  
  *Understanding the PDK structure enables greater design flexibility*
- モデル／ルールファイルの中身を知ることで、**不具合の根本原因に到達しやすくなる**  
  *Interpreting models and rules helps in effective debugging*
- PDKは**プロセス技術の言語化された設計仕様**と捉えるべき  
  *A PDK is the "encoded design language" of a process*

---

## 🔗 関連資料｜Related Materials

▶️ [`eda_toolchain.md`](./eda_toolchain.md)：EDAツールとの接続構成へ  
*Connection between EDA tools and PDK*

---

### 🛠️ 応用編 第6章：PDKとEDA環境｜PDK and EDA Environment  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 **Shinichi Samizo** / MIT License
