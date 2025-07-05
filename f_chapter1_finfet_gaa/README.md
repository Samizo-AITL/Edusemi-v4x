# 特別編 第1章：先端ノード（FinFET、GAA等）

## 概要

本章では、微細化の限界を超えてトランジスタ性能を維持・向上させるために導入された新構造デバイス──**FinFET**および**GAA（Gate-All-Around）Multi-Nanosheet FET**──について解説します。

従来のプレーナ型MOSFETでは、チャネル長の微細化に伴って短チャネル効果（SCE）やDIBL、リーク電流の増加が問題となってきました。FinFETは立体的なFin構造によりゲート制御性を高め、GAAはナノシートをゲートで完全包囲する構造により、さらなる短チャネル制御を実現します。

本章では、それぞれの構造に対応した**詳細な製造プロセスフロー（48ステップ）**も補足資料として提供し、**物理構造・電気特性・設計制約**の三面から理解を深めることを目的とします。

---

## 節構成とファイル一覧

| 節番号 | ファイル名                   | 内容概要 |
|--------|------------------------------|----------|
| 1.1    | `f1_1_planar_limitations.md` | プレーナMOSの限界と微細化の壁 |
| 1.2    | `f1_2_finfet.md`             | FinFET構造の原理とプロセス概要 |
| 1.3    | `f1_3_gaa.md`                | GAA構造とMulti-Nanosheet技術 |
| 1.4    | `f1_4_comparison.md`         | プレーナ vs FinFET vs GAAの特性比較 |
| 1.5    | `f1_5_design_constraints.md` | 設計上の制約とPDKの変化 |
| 1.6    | `f1_6_future_trends.md`      | CFET・3D統合など次世代トレンド |

---

## 補足資料（Appendix）

| ファイル名                      | 内容概要 |
|--------------------------------|----------|
| `appendixf1_01_finfetflow.md`  | FinFETの製造プロセス（全48ステップ） |
| `appendixf1_02_gaaflow.md`     | GAA Multi-Nanosheet FETの製造プロセス（全48ステップ） |
| `appendixf1_03_finfet_vs_gaa.md` | FinFETとGAAの構造・特性・設計影響の比較まとめ |

---

## 教材のねらい

- FinFETとGAAの**構造理解**と**設計制約**の関係を体系的に学ぶ
- 実プロセスベースでの**先端ノード技術の実感**を得る
- 次世代ノード（CFET・3D統合等）への技術連続性を捉える

---

## 図版（予定）

- FinFET構造断面図（images/finfet_structure.png）
- GAA構造断面と犠牲層除去ステップ（images/gaa_layers.png）
- 特性比較表（images/finfet_vs_gaa_table.png）
- CFET/3D構造の概念図（images/cfet_3d_diagram.png）

---

## 著者とライセンス

本教材は MIT ライセンスに基づいて公開されています。

- **著者**：三溝 真一（Shinichi Samizo）  
- **GitHub**：[Samizo-AITL](https://github.com/Samizo-AITL)  
- **連絡先**：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)
