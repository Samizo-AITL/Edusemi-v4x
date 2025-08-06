---
layout: default
title: 補足資料 / Appendix：FinFETとGAAの構造・特性・設計影響の比較まとめ
---

---

# 🧩 補足資料 / Appendix：FinFETとGAAの構造・特性・設計影響の比較まとめ  
**Comparison Summary of FinFET and GAA (Gate-All-Around) Devices**

本資料では、先端ノードCMOS技術における2大トランジスタ構造 ――  
**FinFET（Fin型トランジスタ）** と **GAA（Multi-Nanosheet型トランジスタ）** について、以下の観点から体系的に比較します。  
This appendix compares two advanced CMOS transistor structures — FinFET and GAA Multi-Nanosheet FET — from the following perspectives:

- **構造と製造プロセス / Physical structure & manufacturing**
- **電気特性 / Electrical characteristics**
- **設計影響 / Design impacts**

---

## 🔸 比較1：物理構造 / Physical Structure

| 🧱 項目 / Item | 🌀 FinFET | 🌐 GAA Multi-Nanosheet FET |
|----------------|-----------|-----------------------------|
| **チャネル形状 / Channel geometry** | 垂直Fin構造 / Vertical fin | 水平ナノシート構造 / Horizontal nanosheet |
| **ゲート包囲率 / Gate coverage** | 3面（上面＋側面）/ 3 sides | 4面（全面）/ 4 sides (all-around) |
| **チャネル数制御 / Drive width control** | Fin本数による / By # of fins | シート数による / By # of sheets |
| **対応ノード / Applicable nodes** | 22nm〜5nm | 5nm〜2nm |

---

## 🔸 比較2：製造プロセスの特徴 / Process Characteristics

| 🏭 項目 / Item | 🌀 FinFET | 🌐 GAA |
|----------------|-----------|--------|
| **チャネル形成 / Channel formation** | Finエッチ＋STI埋込 / Etch + STI | Si/SiGeエピ＋犠牲層除去 / Si/SiGe Epi + sacrificial layer |
| **難所工程 / Critical steps** | Fin寸法制御 / Fin CD control | シート選択エッチ / Sheet-selective etch |
| **メタルゲート形成 / Gate stack** | リセス＋成膜 / Recess + deposition | 空洞包囲 / Cavity conformal deposition |
| **CMP工程 / CMP process** | STI/Poly複数CMP / Multiple CMPs | 多層CMP（Dummy含む）/ Multilayer CMP incl. dummy gate |

---

## 🔸 比較3：電気特性（代表値） / Electrical Characteristics (Typical)

| ⚡ 特性項目 / Parameter | 🌀 FinFET | 🌐 GAA | 📝 備考 / Notes |
|------------------------|-----------|--------|------------------|
| **SS（Subthreshold Slope）** | ~70 mV/dec | ~65 mV/dec | GAAがより良好 / GAA superior |
| **DIBL** | 60–80 mV/V | <50 mV/V | 短チャネル耐性 / Better short-channel |
| **オン電流 / Ion** | 高 / High | 同等〜高 / Comparable or better | Depends on W, Nsheet |
| **オフ電流 / Ioff** | 数nA/µm / Few nA/µm | 数百pA/µm / Sub-nA | Excellent gate control |

---

## 🔸 比較4：設計影響 / Design Implications

| 🧩 項目 / Item | 🌀 FinFET | 🌐 GAA |
|----------------|-----------|--------|
| **PDK設計単位 / PDK unit** | Fin数 / # of fins | シート数 / # of sheets |
| **ライブラリ構成 / Library types** | 2〜4 Finセル / 2–4 fin cells | 3–5シート構成 / 3–5 sheet configs |
| **レイアウト自由度 / Layout flexibility** | 高 / Matured | 制限あり / More constrained |
| **RC抽出 / RC extraction** | Fin寸法支配 / Fin CD dominated | 3D寄生顕著 / More 3D parasitics |

---

## 🔸 今後の展望と位置づけ / Future Outlook

| 🚀 観点 / Viewpoint | 🌀 FinFET | 🌐 GAA |
|---------------------|-----------|--------|
| **技術成熟度 / Maturity** | 量産済（Intel 22nm〜）/ Mass-production | 量産中（2nm〜）/ In progress |
| **今後の限界 / Scaling limit** | ≧5nm程度 / ~5nm | 2nm以下可 / <2nm capable |
| **次構造との接続 / Path to next** | GAA導入前段階 / Pre-GAA | CFETや3D-ICへ / Path to CFET, 3D-IC |

---

## 📷 図版リンク / Diagram References (予定)

- `images/finfet_vs_gaa_structure.png`：構造断面図 / Structural Cross-section  
- `images/finfet_vs_gaa_table.png`：比較表まとめ図 / Summary Table  
- `images/rc_model_finfet_gaa.png`：RCモデル差異 / RC Extraction Models

---

## 📝 備考 / Notes

本資料は [`f1_4_comparison.md`](./f1_4_comparison.md) の補強資料として設計され、FinFETとGAAの技術理解と設計比較を支援します。  
詳細プロセス差は以下参照：

- [`appendixf1_01_finfetflow.md`](./appendixf1_01_finfetflow.md)  
- [`appendixf1_02_gaaflow.md`](./appendixf1_02_gaaflow.md)

---

## ©️ 著者・ライセンス / Author & License

- **著者 / Author**：三溝 真一（Shinichi Samizo）  
- **Email**：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- **ライセンス / License**：MIT License  
- **GitHub**：[Samizo-AITL](https://github.com/Samizo-AITL)

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)

