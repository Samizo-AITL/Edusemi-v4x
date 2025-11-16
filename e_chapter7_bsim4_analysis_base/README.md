---
title: "🛠 第7章: BSIM4 MOS特性解析基盤 "
layout: default
---



# 🛠 第7章：BSIM4 MOS特性解析基盤  
BSIM4モデルを対象に、MOSFET の Vg–Id、Vth、gm/Id、SS、DIBL を Python 自動解析するための教材です。

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
