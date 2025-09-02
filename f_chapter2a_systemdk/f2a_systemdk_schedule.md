---
layout: default
title: SystemDK 開発プロジェクト進行表（部門別詳細版）
---

---

# 🗓️ SystemDK 開発プロジェクト進行表（部門別詳細版）  
**SystemDK Development Schedule by Division**

---

## 📅 部門別・週単位スケジュール表  
*Weekly Schedule by Division*

| 週 / Week | 設計部 / *Design*        | 制御部 / *Control*          | CAD部 / *CAD & Layout*    | FAB部 / *Fabrication*     | 評価部 / *Evaluation*        |
|-----------|--------------------------|-----------------------------|---------------------------|---------------------------|-------------------------------|
| 1–2       | 仕様策定・全体ブロック図 <br>*Specification & Block Diagram* | FSM仕様整理 <br>*FSM Specification* | EDAフロー準備 <br>*EDA Flow Setup* |                           | 評価要求定義 <br>*Evaluation Requirements* |
| 3–4       | アーキ定義・I/F設計 <br>*Architecture & I/F Design* | PIDモデル設計 <br>*PID Model Design* | Floorplan検討 <br>*Floorplan Study* |                           | 初期評価計画 <br>*Initial Evaluation Plan* |
| 5–6       | モジュール選定（IP候補） <br>*Module/IP Candidate Selection* | LLM I/O仕様化 <br>*LLM I/O Definition* | レイアウトルール準備 <br>*Layout Rule Prep* |                           | FPGA検証計画 <br>*FPGA Validation Plan* |
| 7–8       | RTLスケルトン作成 <br>*RTL Skeleton* | FSM+PID統合設計 <br>*FSM+PID Integration* | 配置配線ルール作成 <br>*P&R Rule Setup* |                           | FPGA環境セットアップ <br>*FPGA Environment Setup* |
| 9–10      | RTL詳細化 <br>*RTL Detailing* | FPGAテストベンチ構築 <br>*FPGA Testbench* | P&Rツールフロー確認 <br>*P&R Flow Check* |                           | FPGA初期検証 <br>*Initial FPGA Validation* |
| 11–12     | RTLレビュー・修正 <br>*RTL Review & Fix* | LLM統合シナリオ <br>*LLM Integration Scenario* | Floorplan固定 <br>*Floorplan Freeze* |                           | RTL検証 <br>*RTL Verification* |
| 13–14     | RTL完成版 <br>*RTL Final Version* | 制御統合デバッグ <br>*Control Integration Debug* | Placement/Route実施 <br>*Placement & Routing* |                           | 物理設計検証（DRC/LVS支援） <br>*Physical Design Check (DRC/LVS)* |
| 15–16     |                          |                             | GDS出力 <br>*GDS Output*  | マスク工程準備 <br>*Mask Process Prep* | Tape-out前レビュー <br>*Pre-Tapeout Review* |
| 17–18     |                          |                             |                           | マスク作成 <br>*Mask Fabrication* |                           |
| 19–20     |                          |                             |                           | IC試作（1st Silicon） <br>*First Silicon Prototype* | ウエハテスト、初期評価 <br>*Wafer Test & Initial Eval* |
| 21–22     | IP再設計、改善 <br>*IP Redesign & Improvement* | 制御系修正 <br>*Control Fixes* | ECOレイアウト修正 <br>*ECO Layout Update* | IC 2nd試作準備 <br>*Second Silicon Prep* | 再評価 <br>*Re-Evaluation* |
| 23–24     | BR/IP/PKG DK化 <br>*BR/IP/PKG DKization* |                             |                           | IC 2nd試作 <br>*Second Silicon* | 再ウエハテスト <br>*Second Wafer Test* |
| 25–26     | IP/BR/PKG 統合 <br>*IP/BR/PKG Integration* |                             |                           |                           | 評価・システム統合支援 <br>*Evaluation & System Integration* |
| 27–28     | SystemDK最終統合 <br>*SystemDK Final Integration* |                             |                           |                           | 最終評価・報告 <br>*Final Evaluation & Report* |

---

## 🖼️ Mermaid ガントチャート  
*Mermaid Gantt Chart*

```mermaid
gantt
    title 部門別 SystemDK 開発スケジュール / *SystemDK Dev. Schedule by Division*
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    todayMarker stroke-width:2px,stroke:red,opacity:0.5

    section 設計部 / *Design*
    仕様策定・ブロック図 / *Specification & Block Diagram* :a1, 2025-09-01, 14d
    アーキ定義・I/F設計 / *Architecture & I/F Design*      :a2, 2025-09-15, 14d
    モジュール選定 / *Module Selection*                   :a3, 2025-09-29, 14d
    RTLスケルトン / *RTL Skeleton*                        :a4, 2025-10-13, 14d
    RTL詳細化 / *RTL Detailing*                           :a5, 2025-10-27, 14d
    RTL完成・レビュー / *RTL Final & Review*              :a6, 2025-11-10, 28d
    BR/IP/PKG DK化 / *BR/IP/PKG DKization*                :a7, 2026-02-02, 21d
    SystemDK最終統合 / *SystemDK Final Integration*       :a8, 2026-03-23, 14d

    section 制御部 / *Control*
    FSM仕様・PID設計 / *FSM & PID Design*                 :b1, 2025-09-15, 14d
    LLM I/O仕様 / *LLM I/O Definition*                    :b2, 2025-09-29, 14d
    FSM+PID統合 / *FSM+PID Integration*                   :b3, 2025-10-13, 14d
    FPGAテストベンチ / *FPGA Testbench*                   :b4, 2025-10-27, 14d
    LLM統合・デバッグ / *LLM Integration & Debug*         :b5, 2025-11-10, 14d

    section CAD部 / *CAD & Layout*
    EDAフロー準備 / *EDA Flow Setup*                      :c1, 2025-09-01, 14d
    Floorplan検討 / *Floorplan Study*                     :c2, 2025-09-15, 14d
    配置配線ルール準備 / *P&R Rule Prep*                  :c3, 2025-09-29, 14d
    Floorplan固定 / *Floorplan Freeze*                    :c4, 2025-11-10, 14d
    Placement & Route                                     :c5, 2025-11-24, 21d
    GDS出力 / *GDS Output*                                :c6, 2025-12-15, 14d

    section FAB部 / *Fabrication*
    マスク工程準備 / *Mask Process Prep*                  :d1, 2025-12-15, 14d
    マスク作成 / *Mask Fabrication*                       :d2, 2026-01-05, 14d
    1st Silicon試作 / *First Silicon*                     :d3, 2026-01-19, 14d
    2nd Silicon試作 / *Second Silicon*                    :d4, 2026-02-16, 14d

    section 評価部 / *Evaluation*
    評価要求定義 / *Evaluation Requirements*              :e1, 2025-09-01, 14d
    初期評価計画 / *Initial Evaluation Plan*              :e2, 2025-09-15, 14d
    FPGA環境構築・検証 / *FPGA Setup & Validation*        :e3, 2025-10-13, 28d
    RTL/物理設計検証 / *RTL/Physical Verification*        :e4, 2025-11-10, 28d
    1st Silicon評価 / *First Silicon Eval*                :e5, 2026-01-19, 21d
    2nd Silicon評価 / *Second Silicon Eval*               :e6, 2026-02-16, 21d
    最終評価・報告 / *Final Eval & Report*                :e7, 2026-03-23, 14d
```
