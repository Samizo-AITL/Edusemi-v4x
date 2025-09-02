---
layout: default
title: SystemDK 開発プロジェクト進行表（部門別詳細版・現実スケジュール版）
---

---

# 🗓️ SystemDK 開発プロジェクト進行表（部門別詳細版・現実スケジュール版）  
**SystemDK Development Schedule by Division (Realistic Timeline)**

---

## 📘 概要｜Overview

本スケジュールは、教育用に単純化したものではなく、**実務に基づく現実的な進行表**です。  
SystemDK のように **設計・制御・CAD・製造・評価** を跨ぐ大規模プロジェクトは、  
**最低 14〜16か月** のスパンを必要とします。  

*This schedule reflects a **realistic project timeline** based on industry practice.  
Large-scale projects like SystemDK require **14–16 months** across design, control, CAD, fabrication, and evaluation.*  

---

## 📅 部門別・月単位スケジュール表  
*Monthly Schedule by Division*

| 月 / Month | 🛠️ 設計部 / *Design* | 🎛️ 制御部 / *Control* | 🖥️ CAD部 / *CAD & Layout* | 🏭 FAB部 / *Fabrication* | 🔬 評価部 / *Evaluation* | 🎯 主なトリガー / *Trigger* |
|------------|------------------|-------------------|------------------------|-----------------------|------------------------|---------------------------|
| **1–2** | **仕様策定・全体ブロック図** <br>*Specification & Block Diagram* | | | | | 🚀 プロジェクト開始 |
| **2–3** | **アーキ定義・I/F設計** <br>*Architecture & I/F Design* | FSM仕様整理 <br>*FSM Spec* | | | 評価要求定義 <br>*Eval. Requirements* | ✅ 仕様策定完了 |
| **3–4** | **モジュール選定** <br>*Module/IP Selection* | PIDモデル設計 <br>*PID Model Design* | EDAフロー準備 <br>*EDA Flow Setup* | | 初期評価計画 <br>*Initial Eval Plan* | 📐 アーキ定義完了 |
| **4–5** | **RTLスケルトン作成** <br>*RTL Skeleton* | LLM I/O仕様化 <br>*LLM I/O Definition* | Floorplan検討 <br>*Floorplan Study* | | FPGA検証計画 <br>*FPGA Validation Plan* | 🧩 モジュール選定完了 |
| **5–6** | **RTL詳細化** <br>*RTL Detailing* | FSM+PID統合設計 <br>*FSM+PID Integration* | P&Rルール準備 <br>*P&R Rule Prep* | | FPGA環境セットアップ <br>*FPGA Setup* | 📝 RTLスケルトン完成 |
| **6–7** | **RTLレビュー・修正** <br>*RTL Review & Fix* | FPGAテストベンチ構築 <br>*FPGA Testbench* | Floorplan固定 <br>*Floorplan Freeze* | | RTL検証 <br>*RTL Verification* | 🔍 RTL詳細化進捗 |
| **7–8** | **RTL完成版** <br>*RTL Final Version* | 制御統合デバッグ <br>*Control Integration Debug* | Placement & Routing 実施 <br>*P&R Execution* | | 物理設計検証（DRC/LVS） <br>*Physical Verification* | ✅ RTLレビュー完了 |
| **9–10** | | | **GDS出力** <br>*GDS Output* | **マスク工程準備** <br>*Mask Prep* | **Tape-out前レビュー** <br>*Pre-Tapeout Review* | 📦 P&R完了 |
| **11** | | | | **マスク作成** <br>*Mask Fabrication* | | 🏁 GDS出力完了 |
| **12–14** | | | | **1st Silicon試作** <br>*First Silicon (Fab run, 10週)* | **初期評価** <br>*Initial Eval* | 🧪 マスク完成 |
| **15** | **IP再設計・改善** <br>*IP Redesign & Fix* | 制御系修正 <br>*Control Fixes* | ECOレイアウト修正 <br>*ECO Layout Update* | 2nd試作準備 <br>*Second Silicon Prep* | | 🔄 1st Eval 結果 |
| **16–18** | **BR/IP/PKG DK化** <br>*BR/IP/PKG DKization* | | | **2nd Silicon試作** <br>*Second Silicon (Fab run, 10週)* | 再評価 <br>*Re-Eval* | 🛠️ 改善設計完了 |
| **19** | **IP/BR/PKG統合** <br>*IP/BR/PKG Integration* | | | | 評価・統合支援 <br>*System Integration Support* | 📊 2nd Eval 結果 |
| **20** | **SystemDK最終統合** <br>*SystemDK Final Integration* | | | | **最終評価・報告** <br>*Final Eval & Report* | 🏆 全部門統合完了 |

---

## 🖼️ Mermaid ガントチャート  
*Mermaid Gantt Chart (Realistic Schedule)*

```mermaid
gantt
    title 部門別 SystemDK 開発スケジュール（現実版） / *SystemDK Dev. Schedule (Realistic)*
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    todayMarker stroke-width:2px,stroke:red,opacity:0.5

    section 🛠️ 設計部 / *Design*
    仕様策定・ブロック図 / *Specification & Block Diagram* :a1, 2025-09-01, 60d
    アーキ定義・I/F設計 / *Architecture & I/F Design*      :a2, after a1, 30d
    モジュール選定 / *Module Selection*                   :a3, after a2, 30d
    RTLスケルトン / *RTL Skeleton*                        :a4, after a3, 30d
    RTL詳細化 / *RTL Detailing*                           :a5, after a4, 30d
    RTLレビュー・修正 / *RTL Review & Fix*                :a6, after a5, 30d
    RTL完成版 / *RTL Final Version*                       :a7, after a6, 30d
    IP再設計・改善 / *IP Redesign & Fix*                  :a8, after e8, 30d
    BR/IP/PKG DK化 / *BR/IP/PKG DKization*                :a9, after a8, 60d
    IP/BR/PKG統合 / *IP/BR/PKG Integration*               :a10, after a9, 30d
    SystemDK最終統合 / *SystemDK Final Integration*       :a11, after a10, 30d

    section 🎛️ 制御部 / *Control*
    FSM仕様 / *FSM Spec*                                  :b1, after a2, 30d
    PIDモデル設計 / *PID Model*                           :b2, after b1, 30d
    LLM I/O仕様 / *LLM I/O*                               :b3, after b2, 30d
    FSM+PID統合 / *FSM+PID Integration*                   :b4, after b3, 30d
    FPGAテストベンチ / *FPGA Testbench*                   :b5, after a4, 30d
    制御系修正 / *Control Fixes*                          :b6, after e8, 30d

    section 🖥️ CAD部 / *CAD & Layout*
    EDAフロー準備 / *EDA Flow Setup*                      :c1, after a2, 30d
    Floorplan検討 / *Floorplan Study*                     :c2, after a4, 30d
    P&Rルール準備 / *P&R Rule Prep*                       :c3, after c2, 30d
    Floorplan固定 / *Floorplan Freeze*                    :c4, after c3, 30d
    Placement & Routing                                   :c5, after a7, 60d
    GDS出力 / *GDS Output*                                :c6, after c5, 30d
    ECOレイアウト修正 / *ECO Layout Update*               :c7, after e8, 30d

    section 🏭 FAB部 / *Fabrication*
    マスク工程準備 / *Mask Prep*                          :d1, after c6, 30d
    マスク作成 / *Mask Fabrication*                       :d2, after d1, 30d
    1st Silicon試作 / *First Silicon*                     :d3, after d2, 70d
    2nd Silicon準備 / *Second Silicon Prep*               :d4, after a8, 30d
    2nd Silicon試作 / *Second Silicon*                    :d5, after d4, 70d

    section 🔬 評価部 / *Evaluation*
    評価要求定義 / *Eval. Requirements*                   :e1, after a1, 30d
    初期評価計画 / *Initial Eval Plan*                    :e2, after e1, 30d
    FPGA検証計画 / *FPGA Validation Plan*                 :e3, after b3, 30d
    FPGA環境セットアップ / *FPGA Setup*                   :e4, after a4, 30d
    RTL検証 / *RTL Verification*                          :e5, after a5, 30d
    物理設計検証 / *Physical Verification*                :e6, after c5, 30d
    Tape-out前レビュー / *Pre-Tapeout Review*             :e7, after c6, 30d
    初期評価（1st Silicon） / *Initial Eval*              :e8, after d3, 45d
    再評価（2nd Silicon） / *Re-Eval*                     :e9, after d5, 45d
    評価・統合支援 / *Integration Support*                :e10, after e9, 30d
    最終評価・報告 / *Final Eval & Report*                :e11, after e10, 30d
```
