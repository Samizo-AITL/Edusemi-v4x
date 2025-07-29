# 📏 ESD試験モデルと評価規格  
# 📏 ESD Test Models and Evaluation Standards

---

## 📘 概要 / Overview

ESD耐性は、製品出荷前に **国際規格に基づいた試験** によって評価されます。  
設計者はこれらの**試験モデル（HBM, MM, CDM）**の意味と限界を理解し、**実際の設計耐性と対応づける**ことが重要です。

ESD robustness is evaluated based on **international qualification standards before product shipment**.  
Designers must understand the **meanings and limitations of ESD test models (HBM, MM, CDM)**, and relate them to **real-world circuit robustness**.

---

## 🌩️ 主なESD試験モデル / Major ESD Test Models

| モデル / Model | 概要 / Description | 主な模擬対象 / Simulated Scenario | 破壊メカニズム / Failure Mechanism |
|----------------|--------------------|----------------------------------|-----------------------------------|
| **HBM** (Human Body Model) | 人体が帯電してデバイスに触れる<br>Discharge from a charged human | 製造・検査中のオペレーター<br>Operator handling during manufacturing/test | ゲート酸化膜破壊など<br>Gate oxide breakdown |
| **MM** (Machine Model) | 機器や治具からの放電<br>Discharge from equipment or tools | テスター、ハンドラーなど<br>Tester, handler contact | 金属配線溶断、電源ピン短絡<br>Metal fusing, VDD short |
| **CDM** (Charged Device Model) | デバイス自体が帯電し接地時に放電<br>Device self-discharging to ground | ピック＆プレース中など<br>Pick & place handling | 高速高電流による突入破壊<br>Snapback or hard damage from high current |

> ⚡ **CDMは特に破壊力が強く、現代の微細デバイスでの主因**  
> ⚡ **CDM is particularly destructive and dominant in advanced CMOS nodes**

---

## 🧠 CDMが顕在化した背景 / Why CDM Became More Critical

- **微細化によりゲート酸化膜が極端に薄くなったことで、CDM放電による内部破壊が発生しやすくなった。**  
  → Gate oxide thinning in advanced nodes makes circuits highly vulnerable to fast CDM pulses.

- **組立工程の自動化により、帯電した装置やチャックによる放電が増加。**  
  → Automation equipment (e.g. pick-and-place handlers) lacks sufficient ESD mitigation compared to human operators.

> ✅ **HBMでは防げるが、CDMで破壊される**という製品が増えている。  
> ✅ Many modern failures pass HBM but fail CDM due to internal charging and ultra-fast discharges.

---

## 🧪 各試験モデルの条件と代表的規格 / Test Conditions and Standards

### ✅ **HBM（人体モデル / Human Body Model）**

- 📐 モデル構成：100 pF + 1.5 kΩ  
- 🌊 波形：指数減衰型、~150 ns  
- 🔋 電圧範囲：500 V〜2000 V  
- 📘 規格：JEDEC JESD22-A114

### ✅ **MM（機器モデル / Machine Model）**

- 📐 モデル構成：200 pF + 0 Ω（短絡）  
- 🌊 波形：非常に急峻  
- 🔋 電圧範囲：200 V〜400 V（現在は非推奨）  
- 📘 規格：JEDEC JESD22-A115（Obsolete / Not Recommended）

### ✅ **CDM（帯電デバイスモデル / Charged Device Model）**

- 📐 モデル構成：デバイスが自己帯電  
- 🌊 放電時間：数百 ps で完了（超高速）  
- 🔋 電圧範囲：250 V〜1000 V  
- 📘 規格：JEDEC JESD22-C101 / ANSI/ESDA/JEDEC JS-002

---

## 🧩 実務設計との接続点 / Practical Design Considerations

- ⚠️ **CDMは設計上最も厳しい試験条件とされる**  
  → CDM is the most stringent condition in modern design

  ✅ 対策例：**短距離GND経路、低インダクタンス配線、左右対称レイアウト**  
  → Short GND paths, low-inductance routing, and symmetric layout

- ✅ **HBM 250V（JEDEC Class 1）は最低条件**  
  → HBM 250V is the minimum accepted level for JEDEC Class 1

- 🔧 **高信頼性製品では HBM ≥ 2kV、CDM ≥ 500V が求められる**  
  → HBM ≥ 2kV and CDM ≥ 500V are targets for high-reliability applications

---

## ⚠️ ESD試験と実態のギャップ / Gaps Between Test and Reality

| 観点 / Factor | 試験条件 / Test Conditions | 実環境 / Real-World Scenarios |
|---------------|-----------------------------|-------------------------------|
| **試験対象**<br>Target | 単一ピン放電<br>Single pin | 多ピン同時放電ありうる<br>Multi-pin simultaneous events |
| **温度条件**<br>Temperature | 常温<br>Room temp | 実装中は高温高湿もあり<br>High temp/humidity possible |
| **再現性**<br>Reproducibility | 安定した波形<br>Controlled waveform | 放電はランダム<br>Random, uncontrolled events |

> 🔍 **“試験で合格”＝安全ではない。実装現場を意識した設計が必要。**  
> 🔍 **Passing tests ≠ guaranteed safety. Real-world awareness is critical.**

---

## 📚 教材的意義 / Educational Significance

- ✅ 試験値と**設計限界の数値の意味**を明確にする  
- ✅ **ESDモデルの構造的・物理的な違い**を理解できる  
- ✅ 信頼性試験と**設計仕様の橋渡し教材**として活用可能  
- ✅ 品質・解析・設計の**共通言語を形成**

---

## 🔗 次のセクション / Next Section

👉 [`esd_failure_case.md`](./esd_failure_case.md)：ESD破壊モードと不良解析の実例へ  
👉 [`esd_failure_case.md`](./esd_failure_case.md): Real-world ESD failure cases and analysis

---

## 🧭 章全体への導線 / Link to Chapter Overview

📂 [ESD保護設計の章トップへ](../d_chapter3_esd_protection_design/README.md)  
📂 [Back to Chapter Overview: ESD Protection Design](../d_chapter3_esd_protection_design/README.md)

---

© 2025 Shinichi Samizo / MIT License
