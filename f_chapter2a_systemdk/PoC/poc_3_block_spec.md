# 🧱 poc_3_block_spec.md  
**GAA / AMS / MRAMブロックの仕様定義**  
**Block Specification for GAA / AMS / MRAM**

---

## 📘 概要｜Overview

本節では、PoCで統合対象となる3種のブロック（GAA, AMS, MRAM）について、  
その**プロセスノード・機能・インターフェース・制約感度**などを整理します。

This section defines the specifications of the three blocks—**GAA**, **AMS**, and **MRAM**—  
with focus on process node, functionality, interfaces, and sensitivity to constraints.

---

## 🧩 ブロック定義｜Block Overview

| ブロック / Block | ノード / Node | 主機能 / Function | 主な制約感度 / Constraint Sensitivities |
|------------------|----------------|--------------------|------------------------------------------|
| GAA CPU Core     | 2nm            | 高性能ロジック処理 | 熱、SI/PI、応力（熱密度による）         |
| AMS Analog IF    | 22nm BCD       | センサIF、ADC、PMU | EMI/EMC、SI/PI、アナログノイズ耐性       |
| MRAM NVM         | 28nm           | キャッシュ/状態保持 | 熱、応力、電源ノイズ                     |

---

## 🔌 インターフェース特性｜Interface Characteristics

- **GAA CPU**
  - 高速SerDes / DDR相当のI/F
  - 高密度信号バンドル
  - 電力密度：5~8 W/mm²

- **AMS Analog Block**
  - ADC/DAC, RF-IF, センサ用小信号I/O
  - アナログGNDとノイズアイソレーション必要

- **MRAM**
  - 書き込み時高電流、低電圧感度
  - 高温保持特性に制限あり（~125°C）

---

## 🧪 制約マッピング例｜Example Constraint Mapping

```text
[Constraint Map - GAA]
  - Thermal: ★★★★★（ヒートスプレッダ必要）
  - SI/PI: ★★★★☆（高速インターフェース）
  - Stress: ★★★☆☆（局所密度制約）

[Constraint Map - AMS]
  - EMI/EMC: ★★★★★（RF干渉）
  - SI/PI: ★★★☆☆（混載信号）
  - Thermal: ★★☆☆☆（動作温度範囲広い）

[Constraint Map - MRAM]
  - Thermal: ★★★★☆（保持時熱感度）
  - Stress: ★★★★☆（セル構造応力依存）
  - Power: ★★★☆☆（Vdd変動に敏感）
