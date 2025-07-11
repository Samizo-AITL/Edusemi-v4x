# 💾 応用編 第1章：メモリ技術

---

## 📘 概要

SoC（System-on-Chip）設計において、演算処理や制御回路だけでなく、**適切なメモリ構成の選定**は製品の性能・コスト・消費電力に直結します。

中でもSRAMは、論理プロセスに直接統合可能な「組込みメモリ」として広く使われており、**SRAMマクロの活用は設計上の基本スキル**の一つです。

本章では、SRAMを起点として、DRAM、FeRAM、MRAM、3D NANDまで、**メモリ技術の全体像を実務視点で整理**し、SoC設計との関係を意識した技術理解を深めることを目的としています。

---

## 📂 セクション構成

| ファイル名 | 内容 |
|------------|------|
| [`sram.md`](./sram.md)       | SRAM（Static RAM）：高速・揮発性、キャッシュやレジスタファイル用途 |
| [`dram.md`](./dram.md)       | DRAM（Dynamic RAM）：外部メモリ。リフレッシュ必要。LPDDR/DDRなど |
| [`feram.md`](./feram.md)     | FeRAM（強誘電体RAM）：高速・不揮発。アナログ混載LSI向け |
| [`mram.md`](./mram.md)       | MRAM（磁気RAM）：不揮発性。STT/SOT型。将来の組込み候補 |
| [`3dnand.md`](./3dnand.md)   | 3D NANDフラッシュ：大容量・不揮発。ストレージ用だが階層設計が必要 |

---

## 🎯 対象読者

- 半導体の基本構造を理解した**初学者・学生**
- SoC設計における**メモリ選定に関心のある若手技術者**
- 教育機関や教材開発に関わる**指導者・研修担当者**

---

## 🔧 今後の展開（予定）

- 次世代メモリ（ReRAM, PCMなど）の追加  
- キャッシュ設計やメモリマップ構成など**システム応用観点の補足**  
- 消費電力・速度・面積のトレードオフに基づく**メモリ選定手法の提示**

---

## 🔗 本リポジトリのメイン教材との接続

この章は応用編の1章として構成されていますが、以下の基礎章と密接に関係します：

| 章 | 内容 | 関連性 |
|----|------|--------|
| [基礎編　第4章 MOSトランジスタ特性](../chapter4_mos_characteristics/) | トランジスタの動作原理とスイッチング動作 | セル構造理解に必須 |
| [基礎編　第5章 SoC設計フローとEDAツール](../chapter5_soc_design_flow/) | 合成・配置・タイミング設計 | SRAMマクロ配置、eFlash/I/F考慮 |
| [基礎編　第6章 テスト・パッケージ](../chapter6_test_and_package/) | 信頼性評価・不良解析・試験方法 | メモリの耐久性・リテンション設計 |

---

© 2025 Shinichi Samizo / MIT License
