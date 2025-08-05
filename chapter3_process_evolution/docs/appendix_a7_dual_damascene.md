# 📎 付録A-7：デュアルダマシン配線プロセスの詳細と比較  
# 📎 Appendix A-7: Dual Damascene Interconnect Process and Comparison

---

## 🧭 目的｜Objective

本付録では、**デュアルダマシン（Dual Damascene）**プロセスの詳細フローを中心に、  
従来の**Al/Wプラグ配線**との比較を通じて、配線技術の進化と物理的優位性を明確化します。

> This appendix outlines the **dual damascene process flow**, comparing it with **traditional Al/W plug schemes**,  
> highlighting improvements in resistance, capacitance, EM lifetime, and integration efficiency.

---

## 🛠️ デュアルダマシンプロセス詳細フロー｜Dual Damascene Process Flow

| 工程No. | 工程名 / Step                  | 内容 / Description |
|--------|-------------------------------|---------------------|
| ①      | ULK層の堆積（SiOCなど）         | 層間絶縁膜（Low-k）をCVDで形成 |
| ②      | ビアパターン形成（1次リソグラフィ） | VIA用レジストパターンを描画し、エッチング |
| ③      | トレンチパターン形成（2次リソ）     | 上層の配線トレンチを描画し、ビアと連結 |
| ④      | バリア層形成（Ta/TaNなど）         | Cu拡散防止用のバリア金属をスパッタ等で形成 |
| ⑤      | Cuシード層の成膜                  | Cuめっき用の導電層をPVDで形成（スパッタ） |
| ⑥      | Cu電解めっき（ECP）                | トレンチ＋ビアにCuを充填（全体に堆積） |
| ⑦      | CMPによるCu除去と平坦化            | 上面のCu/バリアをCMPで除去し、層を整形 |
| ⑧      | 次層ILD形成へ（M1→M2など）         | 多層化に向けて次の絶縁膜形成へ進む |

> 📌 Dual patterning of **via + trench**, followed by Cu electroplating and CMP,  
> enables high-density, low-RC interconnects suitable for advanced SoCs.

---

## 🧪 配線特性比較表｜Comparison: Al/W Plug vs Cu/ULK

| 特性 / Property                  | Al配線 + Wプラグ / Al + W Plug                              | Cu配線 + ULK / Cu + ULK (Dual Damascene)                        |
|----------------------------------|--------------------------------------------------------------|------------------------------------------------------------------|
| 配線抵抗率 / Resistivity        | 約 2.7 μΩ·cm（Al）                                           | 約 1.7 μΩ·cm（Cu）                                               |
| プラグ抵抗 / Plug Resistance    | 高め（Wは抵抗が高く、ビア部分での抵抗寄与大）               | ビア・配線一体化により**低抵抗**                                |
| 層間誘電率 / Interlayer Dielectric Constant | 約 **k = 4.0〜4.2**（SiO₂系）                              | 約 **k = 2.5〜3.0**（SiOC, SiLK, CDO など ULK系）              |
| RC遅延 / RC Delay                | 高め（R↑, C↑）                                               | **低減（R↓, C↓）→ 高速動作向き**                               |
| EM耐性 / Electromigration       | 中程度（AlはCuより劣る）                                    | **高耐性**（CuはEM寿命に優れる）                               |
| ビア構造 / Via Structure        | WプラグとAl配線を**別工程で形成**                            | Cu viaと配線を**一括形成（デュアルダマシン）**                  |
| 平坦化工程 / Planarization      | CMP不要な場合もあり（Alエッチバックなど）                    | **CMP必須**（Cu選択性のないエッチング不可）                     |
| 実装プロセス / Process Scheme   | Al配線 + Wプラグ + 多工程                                     | **デュアルダマシン：ビア＋トレンチ同時形成 + CMP仕上げ**        |
| 採用ノード / Applied Nodes      | 0.35µm〜0.18µm（主に国内ロジックプロセス）                   | 0.13µm〜45nm以降（先端ファブ中心）                              |
| 備考 / Notes                     | **国内ファブで長期採用**（設備・コスト面の優位）              | **先端SoC・高密度LSI向け**。設備投資・CMP工程が複雑             |

---

## 🧠 技術進化の意義｜Why Dual Damascene Matters

- 📉 **RC遅延の低減** → クロック周波数のボトルネック解消
- 🔋 **低消費電力化** → 配線容量（C）削減による充放電ロス低減
- 🧱 **多層配線対応性** → 高集積回路（M6, M8, M10）への展開可能
- 💪 **EM信頼性向上** → 長寿命・高信頼性LSIの実現

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

- [3.3 配線・CMP・RC遅延の技術進化と設計影響](./docs/3.3_interconnect_and_litho.md)
- [A-3：0.13µm プロセスフロー](./0.13um_Logic_ProcessFlow.md)
- [A-4：90nm プロセスフロー（NiSi, Strained-Si等）](./0.09um_Logic_ProcessFlow.md)

---

## 🧾 備考｜Notes

- **本付録は、0.13µm以降に導入された配線革新の理解を支援**することを目的とします。  
- 教育・試作ではAl/Wが依然有効であり、Cu/ULKは評価対象・先端設計の理解に活用します。

> This appendix is designed to help **understand the wiring transition from Al to Cu**,  
> with emphasis on dual damascene's **technical value and integration complexity**.

---
