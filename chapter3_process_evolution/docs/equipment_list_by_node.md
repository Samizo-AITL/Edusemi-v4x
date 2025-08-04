# 📘 A-6：180nm〜90nm プロセス装置一覧 / Process Equipment List by Node

本資料は、180nm、130nm、90nm 各世代のCMOSロジックプロセスにおける主要な製造装置を工程ごとに整理したものです。  
This document lists typical equipment used in CMOS logic processes across 180nm to 90nm nodes, categorized by processing step.

⚠️ **注意 / Note**  
本装置一覧は筆者の実務経験と技術記録に基づくものであり、ファウンドリ各社の実装とは異なる可能性があります。  
This list is based on practical experience and may differ from actual foundry implementations.

---

## 🧪 装置一覧 / Equipment Table

| 工程カテゴリ / Process Category | 工程例 / Step Examples | 180nm | 130nm | 90nm |
|----------------|----------------------|--------|--------|--------|
| **露光 / Lithography** | STI, Poly, Contact | **Nikon NSR-2205i14E** (5x i-line)<br>**Canon FPA-3000i5+** (2x i-line) | **NSR-S204B** (KrF) | **NSR-S307E** (KrF, 248nm) |
| **酸化 / Oxidation** | G-OX, LOCOS, PRE-OX | TEL AL-1 | TEL AL-2 | TEL AL-3 |
| **成膜 / Deposition** | SiN, SiO₂, Poly | AMAT P5000<br>Tokyo Electron Trias | AMAT Centura | Lam Research Vector |
| **エッチング / Etching** | Poly Etch, Spacer Etch | TEL Unity M | LAM TCP 9400 | TEL Telius |
| **CMP / 平坦化** | STI CMP, ILD CMP | Ebara Frex200 | Ebara Frex300 | Applied Reflexion LK |
| **イオン注入 / Implantation** | Vth, LDD, S/D | Varian 350D | Axcelis GSD-HE | Axcelis Optima HDx |
| **アニール / Anneal** | LDD後、Salicide | TEL Alpha-8 | TEL Alpha-8S | TEL ALPHA-303i |
| **サリサイド / Salicide** | CoSi₂, NiSi | AMAT Endura Co | Endura Ni | Endura Ni / RTA |
| **配線 / Metallization** | Metal-1〜3 | AMAT Endura Al | AMAT Endura Cu | Novellus ALTUS Cu |
| **絶縁膜 / ILD** | TEOS, Low-k | Novellus Sequel | Novellus Black Diamond | ULK: Coral, SiCOH |
| **Wプラグ / Tungsten Plug** | Contact, Via | AMAT Centura WCVD | TEL Unity W | TEL Telius WCVD |
| **バリア / Barrier** | Ti/TiN | Novellus iPVD | AMAT IMP TiN | PVD + ALD併用 |
| **パッド / Pad処理** | Al Pad, Passivation | Canon FPA-2000i5+ | Nikon NSR-2205i14E | Canon FPA-3000i5+ |
| **プローバ / Electrical Test** | E-Test, Param.測定 | TEL P8 | Cascade Summit | TEL P12 |

---

## 🔍 用語補足 / Notes

- **NSR**: Nikon Step-and-Repeat露光装置（縮小倍率5:1）  
- **FPA**: Canon投影露光機（2倍縮小など）  
- **AMAT**: Applied Materials社装置（PVD/CVD等）  
- **TEL**: 東京エレクトロン（酸化、CVD、アニール等）  
- **Axcelis/Varian**: 注入装置メーカー  
- **Novellus**: Low-k膜やPVDで有名（現在はLam傘下）

---

## 📚 関連資料 / Related Docs

- [A-1：0.18μm Process Flow](./0.18um_Logic_ProcessFlow.md)
- [A-3：0.13μm Process Flow](./0.13um_Logic_ProcessFlow.md)
- [A-4：0.09μm Process Flow](./0.09um_Logic_ProcessFlow.md)
- [A-5：ノード比較表 / Node Comparison](./process_node_comparison.md)

---

📎 **[目次に戻る / Back to Appendix](./)**  
