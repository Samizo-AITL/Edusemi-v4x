# 🧬 appendixf1_06_node_params_structural.md
## FinFET / GAA / CFET 各ノードの構造パラメータ比較  
**Node Structural Parameters: $n$, $H$, $W$ for FinFET, GAA, and CFET**

---

## 📘 概要 / Overview

この資料は、各ノードにおけるFinFET / GAA / CFET構造の**物理的寸法パラメータ（$n$, $H$, $W$）**を整理したものです。  
This appendix provides structural parameters across nodes including number of channels ($n$), height ($H$), and width ($W$).

---

## 📊 ノード別構造パラメータ表 / Node-wise Structural Table

| ノード<br>Node | 構造<br>Structure | タイプ<br>Type | $n$ | $H$ (nm) | $W$ (nm) | 備考 / Note |
|----------------|------------------|----------------|----|----------|----------|----------------------------|
| 22nm           | FinFET           | NMOS/PMOS      | 2  | 40       | 10       | 初期FinFET構造               |
| 14nm           | FinFET           | NMOS/PMOS      | 3  | 45       | 8        |                            |
| 10nm           | FinFET           | NMOS/PMOS      | 3  | 50       | 10       |                            |
| 7nm            | FinFET           | NMOS/PMOS      | 4  | 55       | 10       |                            |
| 5nm            | FinFET           | NMOS/PMOS      | 5  | 55       | 8        |                            |
| 3nm            | GAA              | NMOS/PMOS      | 4  | 30       | 15       | Multi-nanosheet構造         |
| 2nm            | GAA              | NMOS/PMOS      | 4  | 28       | 14       | IMEC/TSMC想定               |
| 1.4nm          | GAA              | NMOS/PMOS      | 5  | 28       | 16       |                            |
| 1.0nm          | CFET             | NMOS+PMOS      | 2×2| ~25/25   | ~12      | GAA上下積層構造（推定値）   |
| 0.7nm          | CFET (Forksheet) | NMOS+PMOS      | 2×2| ~20/20   | ~10      | Gate-Fin分離構想（推定値）  |

---

## 📝 備考 / Notes

- $n$はFin数またはナノシート数（1トランジスタあたり）
- CFETではNMOSとPMOSの**垂直積層**のため、$n$はそれぞれのレイヤで2個と想定
- GAA構造ではFinではなく**ナノシート幅**が有効チャネルとなる

---

## 🔗 関連資料 / Related

- [appendixf1_05_node_params.md](./appendixf1_05_node_params.md)  
- [appendixf1_05a_cfet_params.md](./appendixf1_05a_cfet_params.md)  
