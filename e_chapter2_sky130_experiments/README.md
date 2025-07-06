# 🛠 第2章：Sky130実験とSPICE特性評価

本章では、SkyWater社が提供するオープンPDK「Sky130」を活用し、MOSトランジスタの基本特性をSPICEレベルで評価・観察する方法を学びます。  
PDKに含まれるモデルファイルを用いて、nMOS・pMOS の `Vg–Id` 特性、`Vd–Id` 特性、`Vth` 抽出などを実践的に行います。

---

## 🎯 教材のねらい

- Sky130の `.spice` モデルを用いたMOSデバイス特性評価
- 実測に近い動作を模擬できる教育用スクリプトの実装
- Pythonスクリプトと連携した評価系の自動化・可視化

---

## 📁 フォルダ構成（予定）

| フォルダ名 | 内容 |
|-----------|------|
| `01_setup_sky130_model/` | Sky130 PDKのSPICEモデル準備と動作確認 |
| `02_idvg_experiment/` | `Vg–Id` 特性（nMOS / pMOS）の取得とプロット |
| `03_idvd_experiment/` | `Vd–Id` 特性（飽和・リニア領域）の取得と比較 |
| `04_vth_extraction/` | `Vth` 抽出（直線外挿法、gm最大法）の自動化 |
| `05_parameter_sweep/` | L/W変化・温度・電源依存性などの一括スイープ |

※今後の教材拡充に応じて変更の可能性あり

---

## 🔗 関連章との連携

- [実践編 第1章：Pythonによる自動化ツール群](../e_chapter1_python_automation_tools/README.md)
  - `01_spice_runner/` を活用し、SPICEスイープ実行・CSV出力
  - `02_plot_vgid/` を使って可視化まで一貫

- [応用編 第5章：アナログ・ミックスドシグナル設計](../../chapterA5_analog_mixedsignal/README.md)
  - MOS特性の深掘りからアナログ設計へ発展可能

---

## 📦 利用条件

- 教材は Sky130 PDK v0.0.2 を前提とします（`sky130_fd_pr__nfet_01v8`, `pfet_01v8` など）
- `ngspice` v35以降の使用を推奨
- Pythonによる自動化には `pandas`, `matplotlib`, `subprocess` が必要です

---

## 📝 備考

- Sky130は物理寸法ベースで `0.13µm` 相当の教育・研究用途に最適なPDKです
- 本章の評価スクリプトは、回路設計の基本理解とモデル信頼性の検証にも活用できます
