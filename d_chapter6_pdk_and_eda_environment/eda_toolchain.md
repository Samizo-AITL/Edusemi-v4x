# 🧰 EDAツールチェーン：商用・OSSツールとの接続

---

## 📘 概要

PDKを用いたSoC設計には、**EDAツールとの連携が不可欠**です。  
本資料では、商用ツールとオープンソース（OSS）ツールの役割分担と、PDKとのインタフェースを中心に、設計フロー全体にわたる接続関係を整理します。

---

## 🔧 商用EDAツールの例

| ツール名 | 提供企業 | 主な用途 |
|----------|-----------|----------|
| Virtuoso | Cadence | 回路図・レイアウト・アナログシミュレーション |
| Spectre / HSPICE | Cadence / Synopsys | 回路シミュレーション（SPICE） |
| ICC2 / Innovus | Synopsys / Cadence | 配置配線・タイミング検証 |
| Calibre | Siemens EDA | DRC / LVS / PEX（物理検証） |

- PDKに付属するルールファイル（DRC/LVS用、モデルファイル）はこれらに最適化されている。
- 商用PDKは**ツール依存性が高く、ツールとPDKが一体で提供される**ことが多い。

---

## 🧪 オープンソースEDAツールの例

| ツール名 | 主な機能 | 備考 |
|----------|----------|------|
| Magic | レイアウトエディタ | Sky130等と接続可能 |
| Xschem | 回路図エディタ | Verilog/Spice混載設計対応 |
| ngspice | 回路シミュレータ | Sky130モデルと連携可能 |
| KLayout | GDSビューア、DRC | Pythonスクリプトで柔軟に拡張可能 |
| OpenROAD | 配置配線・物理検証 | Sky130向けに最適化（OpenLaneと併用） |

- Sky130のような**OSS PDKに特化したツールチェーン**が整備されつつある。
- Python等の自動化スクリプトと親和性が高く、教育・研究用途に向く。

---

## 🔁 ツール間のPDK接続構成（例：Sky130）
```
回路図 (Xschem)
↓
シミュレーション (ngspice) ← スパイスモデル
↓
レイアウト (Magic)
↓
DRC / LVS / PEX (Magic, Netgen)
↓
配置配線 (OpenROAD)
↓
最終検証 (KLayout, custom scripts)
```
- `sky130A` PDKには、各ツール向けの設定フォルダが分離されており、**柔軟なツール連携が可能**。
- 各ツールは共通のPDK内ファイル（ルール・モデル）を参照して動作する。

---

## 🏫 教材的意義

- 商用ツールは**高機能だがブラックボックス化しやすい**ため、基礎教育ではOSSツールの活用が推奨される
- EDAのフローを構造的に理解することで、**PDKとの依存関係や検証観点が明確になる**
- Sky130やOpenLaneは、教育用PDK＋OSSツールのベストプラクティスとして活用可能

---

## 🔗 関連資料

- [`pdk_structure.md`](./pdk_structure.md)：PDKの構成とモデルの詳細
- [`rule_check_flow.md`](./rule_check_flow.md)：DRC/LVS等の検証フローへ

---

© 2025 Shinichi Samizo / MIT License
