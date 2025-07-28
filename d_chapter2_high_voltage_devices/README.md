# ⚡ 応用編 第2章：高耐圧デバイス

---

## 📘 概要

本章では、SoCやアナログ混載LSIなどにおいて用いられる **高耐圧デバイス（High Voltage Devices）** について学びます。  
LDMOSやHV-CMOSに代表されるこれらの素子は、通常のCMOSに比べて高電圧印加に耐える構造を持ち、**パワー制御・センサ入力・インタフェース駆動**などの用途に不可欠です。

また、設計においては電界集中・寄生素子・レイアウト最適化など、微細で実装的な配慮が求められます。

---

## 🗂️ セクション構成

| ファイル名 | 内容概要 |
|------------|----------|
| [`ldmos.md`](./ldmos.md) | LDMOS（横方向拡散型MOS）：高耐圧・高電流に対応した代表的構造 |
| [`hvcmos.md`](./hvcmos.md) | HV-CMOS：標準CMOSとの互換性を保ちつつ高耐圧を実現 |
| [`junction_isolation.md`](./junction_isolation.md) | 接合絶縁構造：寄生素子防止のためのレイヤ構造とバイアス制御 |
| [`dvdt.md`](./dvdt.md) | dv/dt耐性と電界破壊：急峻な電圧変化によるデバイス破壊と対策設計 |
| [`layout_rules.md`](./layout_rules.md) | レイアウト設計と最適化：ガードリング、CMPダミーなどの実装工夫 |

---

## 🎯 対象読者

- 高耐圧デバイスの基本構造と用途を学びたい初学者
- アナログ混載やPMIC設計に関心を持つ若手技術者
- 電源・センサ・ドライバなどを扱う回路設計担当者

---

## 🧩 本章の到達目標

- LDMOSやHV-CMOSの構造・動作原理を理解する  
- 寄生素子や絶縁構造を意識した設計・レイアウトに慣れる  
- 電圧印加時のデバイス破壊・誤動作を防ぐ設計知識を習得する  

---

## 🔗 関連リンク・参照章

- [応用編　第1章 メモリ技術](../d_chapter1_memory_technologies/README.md)：組込み用SRAMと高耐圧ドライバの連携設計
- [応用編　第5章 アナログ／ミックスドシグナル](../d_chapter5_analog_mixed_signal/README.md)：高電圧アナログブロックとの接続視点
- [基礎編 第4章：MOSトランジスタ特性](../chapter4_mos_characteristics/README.md)：MOSの基本構造と寄生素子理解

---

© 2025 Shinichi Samizo / MIT License

---

🏠 [Edusemi トップに戻る｜Back to Edusemi-v4x Top](../README.md)

---
