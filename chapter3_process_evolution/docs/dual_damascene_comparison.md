---
layout: default
title: 付録A-7：デュアルダマシン配線プロセスの詳細と比較
---

---

# 📎 付録A-7：デュアルダマシン配線プロセスの詳細と比較  
# 📎 Appendix A-7: Dual Damascene Interconnect Process and Comparison

---

## 🧭 目的｜Objective

本付録では、**デュアルダマシン（Dual Damascene）**プロセスの詳細フローを中心に、  
従来の**Al/Wプラグ配線**との比較を通じて、配線技術の進化と物理的優位性を明確化します。

> This appendix outlines the **dual damascene process flow**, comparing it with **traditional Al/W plug schemes**,  
> highlighting improvements in resistance, capacitance, electromigration (EM) lifetime, and integration efficiency.

---

## 🛠️ デュアルダマシンプロセス詳細フロー｜Dual Damascene Process Flow

| 工程No. | 工程名 / Step                      | 内容 / Description |
|--------|-----------------------------------|---------------------|
| ①      | ULK層の堆積 / ULK Deposition      | 層間絶縁膜（Low-k）をCVDで形成<br>Low-k dielectric (e.g., SiOC) is deposited by CVD |
| ②      | ビアパターン形成 / Via Lithography | VIA用レジストパターンを描画・エッチング<br>First lithography to define via |
| ③      | トレンチ形成 / Trench Lithography | 配線トレンチを上層に形成、ビアと連結<br>Second lithography to define trench over via |
| ④      | バリア層形成 / Barrier Deposition | Cu拡散防止用のバリア層（Ta/TaNなど）<br>Sputtered Ta/TaN barrier for Cu diffusion block |
| ⑤      | シード層堆積 / Seed Layer Deposition | Cuメッキ導電層を形成（PVD）<br>Cu seed layer by PVD |
| ⑥      | Cu電解めっき / Cu Electroplating   | ビア＋トレンチをCuで充填（ECP）<br>Cu is electroplated into via and trench |
| ⑦      | CMP研磨 / CMP Planarization        | 過剰Cu/バリアをCMPで除去・平坦化<br>CMP removes excess Cu/barrier and flattens the surface |
| ⑧      | 次層工程へ / Next ILD Formation    | M1→M2など上層へ進む<br>Move to next interlayer dielectric |

> 📌 Dual patterning of **via + trench**, followed by Cu electroplating and CMP,  
> enables high-density, low-RC interconnects suitable for advanced SoCs.

---

## 🧪 配線特性比較表｜Comparison: Al/W Plug vs Cu/ULK

| 特性 / Property                  | Al配線 + Wプラグ / Al + W Plug                        | Cu配線 + ULK / Cu + ULK (Dual Damascene)                        |
|----------------------------------|--------------------------------------------------------|------------------------------------------------------------------|
| 配線抵抗率 / Line Resistivity   | 約 **2.7 μΩ·cm**（Al）                                 | 約 **1.7 μΩ·cm**（Cu）                                           |
| プラグ抵抗 / Plug Resistance    | 高い（Wは抵抗大、接続部での寄与が顕著）<br>High due to high resistivity of W | 一体形成により**低減**<br>Unified structure reduces resistance |
| 層間誘電率 / Dielectric Constant | 約 **k = 4.0〜4.2**（SiO₂系）                          | 約 **k = 2.5〜3.0**（ULK：SiOC, SiLK, CDO等）                    |
| RC遅延 / RC Delay                | **大きい（R↑, C↑）**                                  | **小さい（R↓, C↓）→ 高速化**                                   |
| EM耐性 / EM Lifetime             | 中程度（AlはCuより弱い）<br>Moderate                  | **優れる（長寿命）**<br>Excellent EM resistance                 |
| ビア構造 / Via Formation         | WプラグとAl配線は**別工程**<br>Two-step               | **一括形成**（Via+Trench同時）<br>Single-step (dual patterning) |
| 平坦化 / Planarization           | CMP不要な場合もあり<br>Sometimes etch-back only       | **CMP必須**<br>CMP is mandatory for Cu                          |
| 実装プロセス / Process Scheme   | 多段プロセス（プラグ+配線）<br>Separate plug + metal  | **デュアルダマシン**<br>Dual Damascene integration             |
| 採用ノード / Node Adoption       | 0.35µm〜0.18µm：**国内ロジック主流**<br>0.35–0.18µm mainstream in Japan | 0.13µm以降の**先端ファブ限定**<br>Advanced nodes (0.13µm–45nm+) |
| 備考 / Notes                     | **設備・コストに優れる**（CMP不要）<br>Cost-effective | **設備・CMP条件が厳しい**<br>Needs CMP, high integration cost |

> 🔍 国内ではCu/ULK導入は限定的で、多くはAl/Wプラグを継続採用。  
> → 国内設計教育では**Al/Wでも十分な理解が可能**。

---

## 🧠 技術進化の意義｜Why Dual Damascene Matters

- 📉 **RC遅延の低減** → クロック高速化（GHz世代）
- 🔋 **低消費電力化** → Cの削減により充放電損失を低減
- 🧱 **多層配線（M6, M8, M10）に対応**
- 💪 **EM信頼性の向上** → 高信頼・長寿命LSI

> Dual damascene is essential for **modern SoC performance**,  
> enabling faster, denser, and more reliable interconnect schemes.

---

## 🖼️ 図解候補（別途）｜Suggested Visuals (TBD)

| 図番号 | 内容 / Description |
|--------|--------------------|
| Fig.1  | デュアルダマシン工程断面図（Via + Trench） |
| Fig.2  | Cu配線とAl配線のRCモデル比較               |
| Fig.3  | EM破壊例とCu/Alの寿命差比較                |
| Fig.4  | CMP断面構造（Cu/ULK上の研磨例）            |

---

## 📘 関連リンク｜Related Links

- [3.3 配線・CMP・RC遅延の技術進化と設計影響](../3.3_interconnect_and_litho.md)
- [A-3：0.13µm プロセスフロー](./0.13um_Logic_ProcessFlow.md)
- [A-4：90nm プロセスフロー（NiSi, Strained-Si等）](./0.09um_Logic_ProcessFlow.md)

---

## 🧾 備考｜Notes

- 本付録は、**0.13µm以降に導入されたCu/ULK技術の理解**を支援します。  
- 教材用途としては、**Al/Wでも十分な構造理解とRC解析が可能**です。  
- CMP工程の課題（例：Dishing、Erosion）も指導補足可能です。

> While Cu/ULK and dual damascene are dominant in cutting-edge fabs,  
> **Al/W interconnects remain pedagogically valuable** and accessible.

---
