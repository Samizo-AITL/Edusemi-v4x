# 🧩 応用編 第5a章：0.18μm AMS設計技法  
# 🧩 Applied Chapter 5a: 0.18μm AMS Design Techniques

---

## 📘 概要｜Overview

**0.18μm世代におけるアナログ／ミックスドシグナル（AMS）設計**では、ばらつき、ノイズ、精度、寄生効果などの非理想要因に対して高い信頼性と性能を確保することが求められます。  
特に0.18μmノードは、**素子バリエーションが豊富で、電源電圧や周波数帯も広く、AMS設計に最適なスケール**です。FinFETやGAAを前提とする先端ノードと比べて、**設計の自由度・直感性・教育的価値が高いことから、本章では0.18μm AMS設計に特化**したトピックを扱います。

In 0.18μm analog/mixed-signal (AMS) design, ensuring high reliability and performance requires addressing key non-idealities such as mismatch, noise, accuracy, and parasitics.  
The 0.18μm node is especially suitable for AMS circuits due to **its wide device variety, voltage range, and intuitive layout structure**. Compared to advanced nodes like FinFET/GAA, it offers **greater flexibility and clarity**, making it highly effective for **practical design and educational use**. This chapter focuses on critical AMS techniques tailored to 0.18μm.

---

## 📂 セクション構成｜Section Structure

| 📄 **ファイル名｜Filename** | 📚 **内容｜Description** |
|----------------------------|--------------------------|
| [`1_poly_resistor_mismatch.md`](./1_poly_resistor_mismatch.md) | ポリ抵抗のばらつきと精度制御<br>Poly resistor mismatch and precision control |
| [`2_transistor_matching.md`](./2_transistor_matching.md) | 隣接トランジスタのマッチングとレイアウト設計<br>Matching of adjacent transistors and layout techniques |
| [`3_rsce_and_ldd.md`](./3_rsce_and_ldd.md) | RSCE（逆ショートチャネル効果）とLDD工程の最適化<br>RSCE effects and optimization of LDD engineering |
| [`4_flicker_noise.md`](./4_flicker_noise.md) | 1/f（フリッカー）ノイズの低減技術<br>1/f (flicker) noise reduction techniques |
| [`5_inductor_q_factor.md`](./5_inductor_q_factor.md) | インダクタのQ値改善と配線・基板設計<br>Improving inductor Q-factor via wiring and substrate design |

---

## 🎯 対象読者｜Target Audience

- 実用的なAMS設計課題を構造的に理解したいアナログ技術者  
  *Analog engineers aiming to systematize practical AMS design challenges*
- PDK仕様やプロセス特性と素子性能の関連を掴みたい設計者  
  *Designers interested in the relationship between PDK/process and device behavior*
- レイアウト・プロセス・動作特性を統合的に扱いたい開発者  
  *Developers integrating layout, process, and performance perspectives*

---

## 🔗 関連章｜Related Chapters

| 章｜Chapter | 内容｜Details |
|-------------|----------------|
| [`d_chapter5_analog_mixed_signal/`](../d_chapter5_analog_mixed_signal/) | AMS設計全体：回路構成・インタフェース設計・ノード選定<br>General AMS design: circuit blocks, interface, node selection |
| [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/) | MOSトランジスタ特性と信頼性評価<br>MOS characteristics and reliability assessment |
| [`d_chapter6_pdk_and_eda_environment/`](../d_chapter6_pdk_and_eda_environment/) | PDKを活用したSPICE評価とAMSシミュレーション環境<br>SPICE evaluation and simulation environment using PDKs |

---

## 👤 著者・ライセンス｜Author & License

| 🏷️ 項目｜Item | 📝 内容｜Details |
|----------------|----------------------------------------------|
| **著者｜Author** | 三溝 真一（Shinichi Samizo）<br>信州大学大学院 修了／元 セイコーエプソン |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス｜License** | MIT License（再配布・改変自由）<br>*Redistribution and modification allowed* |

---

### 🏠 [Edusemi-v4x トップへ戻る｜Back to Edusemi-v4x Top](../README.md)
