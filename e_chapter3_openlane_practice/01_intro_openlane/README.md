# 🚀 OpenLane導入とフローの全体像

本節では、オープンソースEDAフロー「OpenLane」の導入手順と、RTLからGDS生成までの全体像を解説します。

---

## 📦 OpenLaneとは

OpenLaneは、The-OpenROAD Projectの一部として開発されている、**デジタルLSI自動設計フロー**です。  
Sky130 PDKと組み合わせることで、Verilog RTLから物理レイアウト（GDS）まで一貫して行えます。

- ベースツール：OpenROAD（配置配線・タイミング解析）
- サポート：yosys（論理合成）、Magic（DRC/LVS）、ngspiceなど
- 実行環境：Docker / ローカル（Python + Makefile）

---

## 🔧 必要な環境構築

### 1. リポジトリのクローン

```bash
git clone https://github.com/The-OpenROAD-Project/OpenLane.git
cd OpenLane
```

### 2. OpenLaneとPDKの取得

```bash
make pull-openlane
make pull-sky130-pdk
```

> ✅ 初回は1時間以上かかる場合があります

---

## 🗂️ ディレクトリ構成（抜粋）

```text
OpenLane/
├── flow/                   # 実行用MakefileとPythonスクリプト
├── designs/                # ユーザー設計を配置（例: picorv32, gcd）
├── PDK_ROOT/               # sky130 PDKを含むディレクトリ（自動生成）
└── config.tcl              # グローバル設定
```

---

## 📈 OpenLaneの設計フロー（概要）

以下のようなステップを、PythonまたはMakefileで一括処理します。

| ステップ | 説明 | 使用ツール |
|---------|------|------------|
| 1. Synthesis | 論理合成（Verilog → gate） | `yosys` |
| 2. Floorplan | 配置計画（コア領域・ピン配置） | `init_floorplan` |
| 3. Placement | 論理セルの配置 | `OpenROAD` |
| 4. CTS | クロックツリー合成 | `OpenROAD` |
| 5. Routing | 配線処理 | `OpenROAD` |
| 6. DRC/LVS | 物理検証 | `Magic`, `Netgen` |
| 7. GDS出力 | 版下ファイル生成 | `KLayout`, `Magic` |

---

## ✅ 教育活用の意義

- 商用EDAと同様の **設計プロセスを無償で体験**
- **PDKとの連携**や制約調整、結果解析を実装を通じて学べる
- 実設計に近いログやレポート形式に触れ、**設計品質の可視化**が可能

---

## 📝 備考

- 本教材では最小構成の例（例：`gcd`, `inverter`）から始めます
- 詳細なフロー実習は [`02_rtl_to_gds_flow/`](../02_rtl_to_gds_flow/README.md) にて
