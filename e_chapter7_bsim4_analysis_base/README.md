---
title: "🛠 第7章: BSIM4 MOS特性解析基盤 "
layout: default
---

---

# 🛠 第7章：BSIM4 MOS特性解析基盤  
BSIM4モデルを対象に、MOSFET の Vg–Id、Vth、gm/Id、SS、DIBL を Python 自動解析するための教材です。

---

## 🔗 公式リンク | *Official Links*

| 言語 / Language | GitHub Pages 🌐 | GitHub 💻 |
|-----------------|----------------|-----------|
| 🇯🇵 日本語 / *Japanese* | [![GitHub Pages JP](https://img.shields.io/badge/GitHub%20Pages-日本語版-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/e_chapter7_bsim4_analysis_base/) | [![GitHub Repo JP](https://img.shields.io/badge/GitHub-日本語版-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x/tree/main/e_chapter7_bsim4_analysis_base) |

---


## 📂 フォルダ構成
- `spice/` — ngspice 用ネットリスト
- `src/` — Python スクリプト（dibl_extract.py、ss_extract.py、plot_vgid.py など）
- `data/`  
  - `raw/` — ngspice 出力ログ
- `figs/` — 解析によって自動生成される PNG 図

## ▶️ 使用手順
### 1. SPICE シミュレーションを実行
```bash
cd spice/netlists
ngspice vgid_nmos_vd05.cir
ngspice vgid_nmos.cir
ngspice vgid_pmos_vd05.cir
ngspice vgid_pmos.cir
