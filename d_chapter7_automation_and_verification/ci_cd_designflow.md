# 🔄 CI/CDによる設計検証自動化

---

## 📘 概要

CI/CD（Continuous Integration / Continuous Deployment）は、ソフトウェア開発において  
継続的な検証と自動デプロイを実現する仕組みです。  
これを半導体設計に応用することで、**RTLの更新やP&R変更に対して自動検証**が可能となり、  
**品質確保の高速化と作業の属人性排除**に寄与します。

---

## 🛠️ CI/CDで自動化可能なステップ

| フェーズ | 自動化項目 | 使用例 |
|---------|------------|--------|
| `フロントエンド` | `Lint`, `論理合成`, `テストベンチ実行` | `Yosys`, `Verilator` |
| `バックエンド` | `配置配線`, `DRC/LVS`, `STA` | `OpenLane`, `Magic`, `Netgen` |
| `レポート生成` | `エリア`, `タイミング`, `消費電力` 解析 | `OpenROAD`, `report parser` |
| `通知・レビュー` | `自動メール送信`, `GitHub Pull Request連携` | `Slack通知`, `GitHub Actions` |

---

## 🔧 GitHub Actions を活用したCI構成例

### ✔️ `.github/workflows/openlane-ci.yml`

```yaml
name: OpenLane CI

on:
  push:
    paths:
      - "designs/**"
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Docker
        run: |
          docker pull efabless/openlane:current
      - name: Run Synthesis
        run: |
          docker run -v ${{ github.workspace }}:/project \
            efabless/openlane:current \
            ./flow.tcl -design my_block -tag ci-run -save

      - name: Upload reports
        uses: actions/upload-artifact@v3
        with:
          name: reports
          path: designs/my_block/runs/ci-run/reports/
```

### 📈 `自動検証ループの構築と効果`

- `設計更新のたびに検証が自動実行`
- `エラーやSlack通知により即座にフィードバック`
- `設計ステータスの可視化（バッジ表示、ログ添付）`

---

### 🎓 `教材的意義`

- `設計品質の自動保証` という考え方を体験できる
- `設計・検証・レビューが一体化したモダンな設計手法` に触れられる
- `OpenソースEDA + GitHub + Python` を用いた `次世代設計プロセス` の基礎となる

---

### 🔗 `関連章`

- [`openlane_validation.md`](./openlane_validation.md)：`OpenLaneによる設計検証`
- [`drc_lvs_erc.md`](./drc_lvs_erc.md)：`レイアウトレベルの自動検証`

---

© 2025 Shinichi Samizo / MIT License

