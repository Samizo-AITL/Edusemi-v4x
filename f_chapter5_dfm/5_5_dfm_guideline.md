---
layout: default
title: 5.5 DFM設計：量産対応のためのレイアウト指針
---

---

# 🏭 5.5 DFM設計：量産対応のためのレイアウト指針  
**DFM Design Guidelines for Manufacturability**

---

## 🎯 本節の目的｜Objectives

- **DFM（Design for Manufacturability）の基本概念**を理解する  
  **Understand the fundamental concept of DFM**
- **歩留まり・信頼性に配慮した設計手法**を学ぶ  
  **Learn layout strategies to enhance yield and reliability**
- **Sky130 PDK における DFM 支援要素と設定項目**を把握する  
  **Explore DFM-support features in the Sky130 environment**

---

## 🧪 DFMとは？｜What is DFM?

DFMとは、**製造ばらつきや微細構造によるリスクに備え**、  
**設計初期から量産対応を意識して設計を最適化する文化**です。

📌 製品としての **再現性・歩留まり・信頼性を高める** ことがDFMの目的です。

---

## 🧩 よくあるDFM課題と対策｜Common Issues and Solutions

| ⚠️ **課題**<br>Issue | 🛠️ **設計対策**<br>Design Strategy |
|------------------|---------------------------|
| 配線ピッチが狭い<br>Narrow metal pitch | **Metal spacing**を十分に確保<br>Apply tighter spacing rules |
| ビア信頼性不足<br>Via reliability issues | **冗長ビア配置（double via）**を使用<br>Use redundant vias |
| 熱集中による劣化<br>Heat concentration | GND/VDD配線の**幅増し・分散配置**<br>Distribute heat-generating cells |
| セル密度過多<br>High core density | `FP_CORE_UTIL`を低めに設定<br>Reduce core utilization ratio |
| チップ端部の歪み<br>Edge-related variation | **Well Tap・Filler Cellの配置徹底**<br>Place filler/tap cells at edges |

---

## 🔍 Sky130におけるDFM支援要素｜DFM-Friendly Features in Sky130

| 📦 **要素** | 🔍 **説明**<br>Description |
|-------------|---------------------------|
| `sky130_fd_sc_hd` | 高歩留まり向け標準セル群<br>High-yield optimized standard cells |
| `well_tap_placement` | 自動Well Tap配置<br>Auto-insertion of well taps in OpenLane |
| `antenna rule` | アンテナ効果による破壊防止<br>Prevent oxide damage from metal antenna effect |
| `fill cell insertion` | 配線密度均一化ダミーセル<br>Dummy fill cells for metal density balance |

---

## ⚙️ OpenLaneにおけるDFMパラメータ例｜DFM Parameters in OpenLane

| ⚙️ **パラメータ**<br>Parameter | 📝 **説明**<br>Description | ✅ **推奨例**<br>Recommended Value |
|---------------------|-----------------------------|-----------------------------|
| `FP_CORE_UTIL` | セル密度（floorplan密度）<br>Core utilization ratio | `0.35`〜`0.5` |
| `PL_TARGET_DENSITY` | 配置密度の目標値<br>Placement target density | `0.5`〜`0.6` |
| `GRT_ALLOW_CONGESTION` | 混雑ルーティングの許容<br>Allow routing congestion | `1`（許容） |

---

## ✅ 本節まとめ｜Summary

- DFMは、**再現性と歩留まりを高める設計手法の総称**です  
  **DFM ensures manufacturable and reliable layout designs**
- Sky130はDFMに配慮したセルやルールが多数含まれている  
  **Sky130 includes various features to support DFM design**
- OpenLane設定や配置ルールもDFM観点で適切に調整が必要  
  **Careful tuning of OpenLane parameters improves DFM compliance**

---

## 🔗 前後のリンク｜Navigation

- ⬅️ [5.4 LVSの仕組みと等価性判定の論理](5_4_lvs_check.md)  
- ▶️ [5.6 チップ完成に向けた最終検証ステップ](5_6_final_verification.md)  
- 🏠 [特別編 第5章 README に戻る](README.md)
