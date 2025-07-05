# ⚠️ 応用編 第3章：ESD設計（Electrostatic Discharge Protection）

---

## 📘 概要

ESD（Electrostatic Discharge：静電気放電）は、**半導体ICに最も頻繁に影響を与える信頼性リスクの一つ**です。  
特にI/Oセルや電源ラインでは、外部からの高電圧スパイクによりデバイスが破壊される恐れがあります。

本章では、ESD保護設計における基本原理、代表的な保護素子、回路設計とレイアウトでの注意点、さらには**実際の破壊モードと解析**までを実務視点で解説します。

---

## 🗂️ セクション構成

| ファイル名 | 内容概要 |
|------------|----------|
| [`esd_overview.md`](./esd_overview.md) | ESD現象の基本と保護設計の必要性（人体モデルなど） |
| [`esd_devices.md`](./esd_devices.md) | GGNMOS, ダイオード, SCRなど各種保護素子の動作原理 |
| [`esd_layout.md`](./esd_layout.md) | レイアウトでのESDパス設計・ガードリング配置・DPP距離など |
| [`esd_spec.md`](./esd_spec.md) | HBM/MM/CDMなどの試験規格とそれぞれの試験条件 |
| [`esd_failure_case.md`](./esd_failure_case.md) | 実際のESD破壊と物理解析（FA）との接続、設計フィードバックの視点 |

---

## 🎯 対象読者

- ESD破壊やI/Oトラブルに直面したことのある若手エンジニア  
- 保護回路の原理とレイアウト制約を理解したい設計者  
- 製品品質や不良解析に関心のある品質技術・FA担当者

---

## 🧩 本章の到達目標

- ESDの発生原理・破壊モード・保護設計の要点を体系的に理解する  
- GGNMOSやダイオードなどのESD保護素子の構造を把握する  
- 保護素子の配置・接続パスを含むレイアウト上の工夫を実装できる  
- ESD破壊と不良解析（FA）の連携的な位置づけを理解する

---

## 🔗 関連リンク・参照章

- [第2章 高耐圧デバイス](../d_chapter2_high_voltage_devices/README.md)：dv/dt破壊や電界集中の対策と連携  
- [第6章 テストとパッケージ](../../chapter6_test_and_package/README.md)：信頼性試験やESDスクリーニングとの関連  
- [第5章 アナログ／ミックスドシグナル](../d_chapter5_analog_mixed_signal/README.md)：ESD感受性の高いアナログ端子の設計注意点

---

© 2025 Shinichi Samizo / MIT License
