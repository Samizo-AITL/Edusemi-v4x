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

## 🧪 各試験モデルの条件と代表的規格 / Test Conditions and Standards

### ✅ **HBM（人体モデル / Human Body Model）**

- 📐 **モデル構成**：100 pF + 1.5 kΩ  
- 🌊 **波形**：指数減衰型、~150 ns  
- 🔋 **電圧範囲**：500 V〜2000 V  
- 📘 **規格**：JEDEC JESD22-A114

### ✅ **MM（機器モデル / Machine Model）**

- 📐 **モデル構成**：200 pF + 0 Ω（ほぼ短絡）  
- 🌊 **波形**：非常に急峻で短時間  
- 🔋 **電圧範囲**：200 V〜400 V（現在は非推奨）  
- 📘 **規格**：JEDEC JESD22-A115（Obsolete / Not Recommended）

### ✅ **CDM（帯電デバイスモデル / Charged Device Model）**

- 📐 **モデル構成**：実チップが自己帯電  
- 🌊 **放電時間**：数百 ps で完了（非常に高速）  
- 🔋 **電圧範囲**：250 V〜1000 V  
- 📘 **規格**：JEDEC JESD22-C101 / ANSI/ESDA/JEDEC JS-002

---

## 🧩 実務設計との接続点 / Practical Design Considerations

- ⚠️ **設計ではCDMが最も厳しい試験条件となる**  
  → CDM is the most stringent model in actual circuit design  
  → 対策例：**短距離GND経路、低インダクタンス配線、左右対称レイアウト**  
  → Countermeasures: short GND paths, low-L layout, symmetry

- ✅ **HBM 250Vは最低限の耐性要件（JEDEC Class 1）**  
  → HBM 250V is the baseline requirement in JEDEC Class 1

- 🔧 **高信頼性製品では HBM 2kV, CDM 500V 以上が望ましい**  
  → High-reliability ICs may require HBM ≥ 2kV, CDM ≥ 500V

---

## ⚠️ ESD試験と実態のギャップ / Gaps Between Test and Reality

| 観点 / Factor | 試験条件 / Test Conditions | 実環境 / Real-World Scenarios |
|---------------|-----------------------------|-------------------------------|
| **試験対象**<br>Target | 単一ピン放電<br>Single pin discharge | 多ピン同時放電の可能性<br>Multiple-pin simultaneous |
| **温度条件**<br>Temperature | 常温で試験<br>Room temperature | 実装中は高温/高湿もあり<br>High temp/humidity in real process |
| **再現性**<br>Reproducibility | 安定した波形<br>Controlled waveform | ランダムな放電イベント<br>Random and uncontrolled events |

> 🔍 **“試験で合格”は安全の保証ではない。現場を意識した設計が重要。**  
> 🔍 **Passing tests does not guarantee robustness — real-world awareness is essential.**

---

## 📚 教材的意義 / Educational Significance

- ✅ **設計段階における数値目標の明確化**  
- ✅ 各モデルの**物理的イメージの理解**  
- ✅ 信頼性試験と**設計仕様の橋渡し教材**  
- ✅ **品質・信頼性エンジニアとの共通言語を形成**

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
