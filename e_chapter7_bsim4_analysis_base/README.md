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
```

---

## 👤 **著者・ライセンス | Author & License**

| 📌 項目 / Item | 📄 内容 / Details |
|------|------|
| **著者 / Author** | **三溝 真一**（Shinichi Samizo） |
| **💻 GitHub** | [![GitHub](https://img.shields.io/badge/GitHub-Samizo--AITL-blue?style=for-the-badge&logo=github)](https://github.com/Samizo-AITL) |
| **📜 ライセンス / License** | [![Hybrid License](https://img.shields.io/badge/License-Hybrid-blueviolet?style=for-the-badge)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)<br>コード / Code: [MIT](https://opensource.org/licenses/MIT)<br>教材テキスト / Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<br>図表 / Figures: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) |

---

## 🔙 戻る｜Back to Top

🏠 [![Site](https://img.shields.io/badge/Site-Edusemi--v4x-lightgrey?style=for-the-badge&logo=githubpages&labelColor=555&color=brightgreen)](../) [![Repo](https://img.shields.io/badge/Repo-Edusemi--v4x-lightgrey?style=for-the-badge&logo=github&labelColor=555&color=blue)](https://github.com/Samizo-AITL/Edusemi-v4x)

