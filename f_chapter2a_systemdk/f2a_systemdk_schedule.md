---
layout: default
title: SystemDK 開発プロジェクト進行表（部門別詳細版）
---

---

# 🗓️ SystemDK 開発プロジェクト進行表（部門別詳細版）  
**SystemDK Development Schedule by Division**

---

## 📅 部門別・週単位スケジュール表

| 週 / Week | 設計部 / Design         | 制御部 / Control           | CAD部 / CAD & Layout     | FAB部 / Fabrication      | 評価部 / Evaluation         |
|-----------|-------------------------|----------------------------|--------------------------|--------------------------|------------------------------|
| 1–2       | 仕様策定・全体ブロック図 | FSM仕様整理                 | EDAフロー準備             |                          | 評価要求定義                 |
| 3–4       | アーキ定義・I/F設計     | PIDモデル設計               | Floorplan検討             |                          | 初期評価計画                 |
| 5–6       | モジュール選定（IP候補）| LLM I/O仕様化               | レイアウトルール準備       |                          | FPGA検証計画                 |
| 7–8       | RTLスケルトン作成       | FSM+PID統合設計             | 配置配線ルール作成         |                          | FPGA環境セットアップ         |
| 9–10      | RTL詳細化               | FPGAテストベンチ構築         | P&Rツールフロー確認        |                          | FPGA初期検証                 |
| 11–12     | RTLレビュー・修正       | LLM統合シナリオ              | Floorplan固定              |                          | RTL検証                      |
| 13–14     | RTL完成版               | 制御統合デバッグ             | Placement/Route実施       |                          | 物理設計検証（DRC/LVS支援）  |
| 15–16     |                         |                            | GDS出力                   | マスク工程準備           | Tape-out前レビュー            |
| 17–18     |                         |                            |                          | マスク作成                |                              |
| 19–20     |                         |                            |                          | IC試作（1st Silicon）     | ウエハテスト、初期評価        |
| 21–22     | IP再設計、改善           | 制御系修正                   | ECOレイアウト修正          | IC 2nd試作準備            | 再評価                       |
| 23–24     | BR/IP/PKG DK化           |                            |                          | IC 2nd試作                | 再ウエハテスト                |
| 25–26     | IP/BR/PKG 統合           |                            |                          |                          | 評価・システム統合支援        |
| 27–28     | SystemDK最終統合         |                            |                          |                          | 最終評価・報告                |

---

## 🖼️ Mermaid ガントチャート

```mermaid
gantt
    title 部門別 SystemDK 開発スケジュール
    dateFormat  YYYY-MM-DD
    axisFormat  %m/%d
    %% 基準日を追加
    todayMarker stroke-width:2px,stroke:red,opacity:0.5

    section 設計部
    仕様策定・ブロック図     :a1, 2025-09-01, 2w
    アーキ定義・I/F設計      :a2, 2025-09-15, 2w
    モジュール選定           :a3, 2025-09-29, 2w
    RTLスケルトン            :a4, 2025-10-13, 2w
    RTL詳細化                :a5, 2025-10-27, 2w
    RTL完成・レビュー        :a6, 2025-11-10, 4w
    BR/IP/PKG DK化           :a7, 2026-02-02, 3w
    SystemDK最終統合         :a8, 2026-03-23, 2w

    section 制御部
    FSM仕様・PID設計        :b1, 2025-09-15, 2w
    LLM I/O仕様             :b2, 2025-09-29, 2w
    FSM+PID統合             :b3, 2025-10-13, 2w
    FPGAテストベンチ        :b4, 2025-10-27, 2w
    LLM統合・デバッグ       :b5, 2025-11-10, 2w

    section CAD部
    EDAフロー準備           :c1, 2025-09-01, 2w
    Floorplan検討           :c2, 2025-09-15, 2w
    配置配線ルール準備       :c3, 2025-09-29, 2w
    Floorplan固定           :c4, 2025-11-10, 2w
    Place&Route             :c5, 2025-11-24, 3w
    GDS出力                 :c6, 2025-12-15, 2w

    section FAB部
    マスク工程準備           :d1, 2025-12-15, 2w
    マスク作成              :d2, 2026-01-05, 2w
    1st Silicon試作         :d3, 2026-01-19, 2w
    2nd Silicon試作         :d4, 2026-02-16, 2w

    section 評価部
    評価要求定義            :e1, 2025-09-01, 2w
    初期評価計画            :e2, 2025-09-15, 2w
    FPGA環境構築・検証       :e3, 2025-10-13, 4w
    RTL/物理設計検証        :e4, 2025-11-10, 4w
    1st Silicon評価         :e5, 2026-01-19, 3w
    2nd Silicon評価         :e6, 2026-02-16, 3w
    最終評価・報告           :e7, 2026-03-23, 2w
```
