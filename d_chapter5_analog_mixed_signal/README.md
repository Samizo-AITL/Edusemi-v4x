# 🎛️ 応用編 第5章：アナログ／ミックスドシグナル設計

---

## 📘 概要

デジタルSoC設計の中でも、**アナログ／ミックスドシグナル（AMS）**回路は依然として重要な役割を担っています。電圧検出、電流制御、センサIF、PLL、ADC/DACなど、**現実世界との橋渡し**にはアナログの知識が不可欠です。

この章では、アナログ回路設計の基本ブロック、レイアウト上の注意点、ノイズや電源変動に対する設計手法、混載時の制約など、**デジタル設計者にも必要なAMS設計の実践知識**を扱います。

---

## 🧩 セクション構成

| ファイル名 | セクション内容 |
|------------|----------------|
| [`ams_overview.md`](./ams_overview.md) | アナログ・ミックスド信号設計の概要と応用領域 |
| [`basic_blocks.md`](./basic_blocks.md) | オペアンプ、バッファ、コンパレータなどの基本回路構成 |
| [`layout_considerations.md`](./layout_considerations.md) | アナログレイアウトの注意点（対称性、マッチング、ウェル共有など） |
| [`noise_and_psrr.md`](./noise_and_psrr.md) | ノイズ設計とPSRR（電源変動耐性）に関する基礎と実践 |
| [`mixed_signal_interface.md`](./mixed_signal_interface.md) | ADC/DAC等のデジアナ境界における設計注意点 |

---

## 🎯 対象読者

- デジタル回路設計を学んでいるが、アナログ要素への理解を深めたい初学者
- AMS混載SoCを扱う若手設計エンジニア
- アナログレイアウトやノイズ対策を実装観点から理解したい技術者

---

## 🔗 関連章リンク

- [応用編　第4章：レイアウト設計と最適化](../d_chapter4_layout_optimization/)
- [応用編　第6章：PDKとEDA環境](../d_chapter6_pdk_and_eda_environment/)
- [応用編　第8章：FSM設計（有限状態機械）](../d_chapter8_fsm_design_basics/)

---

© 2025 Shinichi Samizo / MIT License
