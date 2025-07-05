# 🧪 OpenLaneによる実装検証とログ解析

---

## 📘 概要

本節では、オープンソースの物理設計ツールフロー `OpenLane` を活用して、  
配置配線後の検証（`DRC` / `LVS` / `STA`）とログファイルの読み解き方を解説します。

OpenLaneはSky130PDKに対応しており、教育・研究用途でも広く使われています。

---

## 🔧 OpenLane 構成と自動検証フロー

OpenLaneは各ステージで自動的に検証処理を挟みます。

```text
[RTL] → synthesis → floorplan → placement → CTS → routing → DRC / LVS / STA → [GDS]
```

### ✔️ 各段階での自動チェック

| `ステージ` | `自動検証` | `内容例` |
|------------|------------|----------|
| `synthesis` | `lint` | `論理記述の静的検証` |
| `placement` | `overlap check` | `セルの重なり確認` |
| `routing` | `DRC`, `antenna check` | `配線ルール・アンテナ効果` |
| `final` | `LVS`, `STA` | `回路一致確認・タイミング検証` |

---

### 📂 `ログファイルの構造と分析ポイント`

OpenLaneでは各ステップごとに `logs/` 以下にログが生成されます。

```text
designs/your_block/runs/your_run/logs/
├── synthesis/
│   └── yosys.log
├── placement/
│   └── tapcell.log
├── routing/
│   └── tritonRoute.log
├── lvs/
│   └── netgen.lvs.log
├── sta/
│   └── openroad.log
```

#### ✔️ `よく見るべきログ項目`

- `DRC`：`# violations`、`違反箇所座標`
- `LVS`：`Netlists match: YES/NO`、`不一致のセルやポート`
- `STA`：`slack`、`critical path`、`setup/hold 違反`

---

### 📈 `Pythonによるログ解析の実装例`

OpenLaneログはテキストベースで構造が明確なため、  
`Python`でパースして自動的に以下を抽出できます：

```python
# openlane_log_parser.py の一部例
def extract_drc_violations(log_file):
    with open(log_file) as f:
        lines = f.readlines()
    return [l for l in lines if "violation" in l.lower()]
```

- `面積` や `セル数`、`消費電力` も `reports/` フォルダから `自動抽出可能`

---

### 🎯 `教材的意義`

- 商用EDAと同様の `検証フロー全体を一貫して体験` できる
- `ログ読解力` の訓練により、`設計状態の診断力` が養われる
- `自動パースやグラフ化` により、`検証 → 改善のループ` が理解しやすい

---

### 🔗 `関連章`

- [`drc_lvs_erc.md`](./drc_lvs_erc.md)：`基本的なレイアウト検証の原理`  
- [`ci_cd_designflow.md`](./ci_cd_designflow.md)：`検証プロセスの継続的自動化`
  


