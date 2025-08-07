---
layout: default
title: CI/CDによる設計検証自動化
---

---

# 🔄 CI/CDによる設計検証自動化  
**🔄 CI/CD-Based Automated Design Verification**

---

## 📘 概要｜Overview

CI/CD（Continuous Integration / Continuous Deployment）は、ソフトウェア開発における  
継続的な統合とデプロイメントの仕組みであり、これを**半導体設計に応用**することで、  
**RTLの更新やP&Rの変更に対する自動検証**が可能となります。

CI/CD enables **automated verification** of RTL updates and P&R changes in semiconductor design,  
**accelerating quality assurance** and **eliminating manual dependencies**.

---

## 🛠️ CI/CDで自動化可能なステップ｜Automatable Steps via CI/CD

| フェーズ｜Phase | 自動化項目｜Automation Tasks | 使用例｜Examples |
|-------------|------------------------|---------------------------|
| フロントエンド | Lint, 論理合成, テストベンチ実行<br>Lint, Synthesis, Testbench | Yosys, Verilator |
| バックエンド | 配置配線, DRC/LVS, STA<br>P&R, DRC/LVS, STA | OpenLane, Magic, Netgen |
| レポート生成 | 面積, タイミング, 消費電力<br>Area, Timing, Power Reports | OpenROAD, Report Parser |
| 通知・レビュー | 自動メール送信, PR連携<br>Auto-notification, PR Checks | GitHub Actions, Slack通知 |

---

## 🔧 GitHub Actions を活用した CI 構成例  
## 🔧 Example: CI Flow using GitHub Actions

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

---

## 📈 自動検証ループの構築と効果  
## 📈 Benefits of Continuous Verification Loops

- **設計更新のたびに検証が自動実行**  
  *Verifications are triggered on every commit or pull request*
- **エラー通知・Slack連携で即座にフィードバック**  
  *Immediate feedback via logs or Slack alerts*
- **バッジ表示やレポートによる状態可視化**  
  *Status visualization through badges and reports*

---

## 🎓 教材的意義｜Educational Significance

- 設計品質を**自動で保証する方法論**を体験できる  
  *Hands-on with quality assurance automation*
- 設計・検証・レビューが**一体化した現代的手法**を学べる  
  *Learn modern integrated design-review-verification flows*
- **Open Source EDA + GitHub + Python** を活用した  
  **再現性ある設計フロー構築の基礎**を理解できる  
  *Foundation for reproducible, automated design pipelines*

---

## 🔗 関連章｜Related Sections

- [`openlane_validation.md`](./openlane_validation.md)：OpenLaneによる設計検証  
  *Post-P&R verification with OpenLane*
- [`drc_lvs_erc.md`](./drc_lvs_erc.md)：レイアウトレベルの検証基礎  
  *Fundamentals of layout-level checks*

---

### 🤖 応用編 第7章：自動化と実装検証技術｜Applied Chapter 7: Automation and Implementation Verification  
[➡️ 章の詳細へ進む｜Go to Chapter](./README.md)

---

© 2025 Shinichi Samizo / MIT License
