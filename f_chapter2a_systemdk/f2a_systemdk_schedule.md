---
layout: default
title: SystemDK 開発プロジェクト進行表（部門別詳細版・トリガー明示版）
---

---

# 🗓️ SystemDK 開発プロジェクト進行表（部門別詳細版・トリガー明示版）  
**SystemDK Development Schedule by Division (with Explicit Triggers)**

---

## 📘 概要｜Overview

SystemDK は、**設計・制御・CAD・製造・評価** といった複数部門を跨ぐ統合開発であり、  
単独の技術理解だけでなく、**依存関係（トリガー）を意識した進行管理** が必須となります。  

*SystemDK is an integrated development across **design, control, CAD, fabrication, and evaluation**,  
where project management must explicitly account for **dependencies and triggers**.*  

---

## 📅 部門別・週単位スケジュール表  
*Weekly Schedule by Division*

| 週 / Week | 🛠️ 設計部 / *Design* | 🎛️ 制御部 / *Control* | 🖥️ CAD部 / *CAD & Layout* | 🏭 FAB部 / *Fabrication* | 🔬 評価部 / *Evaluation* | 🎯 主なトリガー / *Trigger* |
|-----------|------------------|-------------------|------------------------|-----------------------|------------------------|---------------------------|
| **1–2** | **仕様策定・全体ブロック図** <br>*Specification & Block Diagram* | | | | | 🚀 プロジェクト開始 |
| **3–4** | **アーキ定義・I/F設計** <br>*Architecture & I/F Design* | FSM仕様整理 <br>*FSM Spec* | | | 評価要求定義 <br>*Eval. Requirements* | ✅ 仕様策定完了 |
| **5–6** | **モジュール選定（IP候補）** <br>*Module/IP Selection* | PIDモデル設計 <br>*PID Model Design* | EDAフロー準備 <br>*EDA Flow Setup* | | 初期評価計画 <br>*Initial Eval Plan* | 📐 アーキ定義完了 |
| **7–8** | **RTLスケルトン作成** <br>*RTL Skeleton* | LLM I/O仕様化 <br>*LLM I/O Definition* | Floorplan検討 <br>*Floorplan Study* | | FPGA検証計画 <br>*FPGA Validation Plan* | 🧩 モジュール選定完了 |
| **9–10** | **RTL詳細化** <br>*RTL Detailing* | FSM+PID統合設計 <br>*FSM+PID Integration* | P&Rルール準備 <br>*P&R Rule Prep* | | FPGA環境セットアップ <br>*FPGA Setup* | 📝 RTLスケルトン完成 |
| **11–12** | **RTLレビュー・修正** <br>*RTL Review & Fix* | FPGAテストベンチ構築 <br>*FPGA Testbench* | Floorplan固定 <br>*Floorplan Freeze* | | RTL検証 <br>*RTL Verification* | 🔍 RTL詳細化進捗 |
| **13–14** | **RTL完成版** <br>*RTL Final Version* | 制御統合デバッグ <br>*Control Integration Debug* | Placement & Routing 実施 <br>*P&R Execution* | | 物理設計検証（DRC/LVS） <br>*Physical Verification* | ✅ RTLレビュー完了 |
| **15–16** | | | **GDS出力** <br>*GDS Output* | **マスク工程準備** <br>*Mask Prep* | **Tape-out前レビュー** <br>*Pre-Tapeout Review* | 📦 P&R完了 |
| **17–18** | | | | **マスク作成** <br>*Mask Fabrication* | | 🏁 GDS出力完了 |
| **19–20** | | | | **IC試作（1st Silicon）** <br>*First Silicon* | **ウエハテスト・初期評価** <br>*Wafer Test & Initial Eval* | 🧪 マスク完成 |
| **21–22** | **IP再設計・改善** <br>*IP Redesign & Fix* | 制御系修正 <br>*Control Fixes* | ECOレイアウト修正 <br>*ECO Layout Update* | 2nd試作準備 <br>*Second Silicon Prep* | 再評価 <br>*Re-Evaluation* | 🔄 1st Silicon評価結果 |
| **23–24** | **BR/IP/PKG DK化** <br>*BR/IP/PKG DKization* | | | **2nd試作** <br>*Second Silicon* | 再ウエハテスト <br>*Second Wafer Test* | 🛠️ 改善設計完了 |
| **25–26** | **IP/BR/PKG統合** <br>*IP/BR/PKG Integration* | | | | 評価・システム統合支援 <br>*System Integration Support* | 📊 2nd Silicon結果 |
| **27–28** | **SystemDK最終統合** <br>*SystemDK Final Integration* | | | | **最終評価・報告** <br>*Final Eval & Report* | 🏆 全部門統合完了 |

---

## 🖼️ Mermaid ガントチャート  
*Mermaid Gantt Chart (with Explicit Triggers)*

```mermaid
gantt
    title 部門別 SystemDK 開発スケジュール（トリガー明示版） / *SystemDK Dev. Schedule by Division (Triggers)*
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    todayMarker stroke-width:2px,stroke:red,opacity:0.5

    section 🛠️ 設計部 / *Design*
    **仕様策定・ブロック図** / *Specification & Block Diagram* :a1, 2025-09-01, 14d
    **アーキ定義・I/F設計** / *Architecture & I/F Design*      :a2, after a1, 14d
    **モジュール選定** / *Module Selection*                   :a3, after a2, 14d
    **RTLスケルトン** / *RTL Skeleton*                        :a4, after a3, 14d
    **RTL詳細化** / *RTL Detailing*                           :a5, after a4, 14d
    **RTLレビュー・修正** / *RTL Review & Fix*                :a6, after a5, 14d
    **RTL完成版** / *RTL Final Version*                       :a7, after a6, 14d
    **IP再設計・改善** / *IP Redesign & Fix*                  :a8, after e8, 14d   %% 1st Eval 結果
    **BR/IP/PKG DK化** / *BR/IP/PKG DKization*                :a9, after a8, 14d
    **IP/BR/PKG統合** / *IP/BR/PKG Integration*               :a10, after a9, 14d
    **SystemDK最終統合** / *SystemDK Final Integration*       :a11, after a10, 14d

    section 🎛️ 制御部 / *Control*
    FSM仕様 / *FSM Spec*                                  :b1, after a2, 14d
    PIDモデル設計 / *PID Model*                           :b2, after b1, 14d
    LLM I/O仕様 / *LLM I/O*                               :b3, after b2, 14d
    FSM+PID統合 / *FSM+PID Integration*                   :b4, after b3, 14d
    FPGAテストベンチ / *FPGA Testbench*                   :b5, after a4, 14d
    制御系修正 / *Control Fixes*                          :b6, after e8, 14d   %% 1st Eval 結果

    section 🖥️ CAD部 / *CAD & Layout*
    EDAフロー準備 / *EDA Flow Setup*                      :c1, after a2, 14d
    Floorplan検討 / *Floorplan Study*                     :c2, after a4, 14d
    P&Rルール準備 / *P&R Rule Prep*                       :c3, after c2, 14d
    Floorplan固定 / *Floorplan Freeze*                    :c4, after c3, 14d
    Placement & Routing                                   :c5, after a7, 14d
    **GDS出力** / *GDS Output*                            :c6, after c5, 14d
    ECOレイアウト修正 / *ECO Layout Update*               :c7, after e8, 14d   %% 1st Eval 結果

    section 🏭 FAB部 / *Fabrication*
    マスク工程準備 / *Mask Prep*                          :d1, after c6, 14d
    マスク作成 / *Mask Fabrication*                       :d2, after d1, 14d
    1st Silicon試作 / *First Silicon*                     :d3, after d2, 14d
    2nd Silicon準備 / *Second Silicon Prep*               :d4, after a8, 14d   %% 修正版設計
    2nd Silicon試作 / *Second Silicon*                    :d5, after d4, 14d

    section 🔬 評価部 / *Evaluation*
    評価要求定義 / *Eval. Requirements*                   :e1, after a1, 14d
    初期評価計画 / *Initial Eval Plan*                    :e2, after e1, 14d
    FPGA検証計画 / *FPGA Validation Plan*                 :e3, after b3, 14d
    FPGA環境セットアップ / *FPGA Setup*                   :e4, after a4, 14d
    RTL検証 / *RTL Verification*                          :e5, after a5, 14d
    物理設計検証 / *Physical Verification*                :e6, after c5, 14d
    Tape-out前レビュー / *Pre-Tapeout Review*             :e7, after c6, 14d
    **初期評価（1st Silicon）** / *Initial Eval*           :e8, after d3, 14d
    **再評価（2nd Silicon）** / *Re-Eval*                  :e9, after d5, 14d
    評価・統合支援 / *Integration Support*                :e10, after e9, 14d
    **最終評価・報告** / *Final Eval & Report*            :e11, after e10, 14d
```
