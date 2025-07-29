# 🧪 CMP対応のダミーパターンと均一化設計  
# 🧪 CMP-Compatible Dummy Pattern and Density Equalization Design

---

## 📘 概要 | Overview

CMP（Chemical Mechanical Polishing）は、**金属層や絶縁層の平坦化（planarization）**を目的とした工程で、  
レイアウト設計における**パターン密度の均一性**が品質に直結します。  
CMP (Chemical Mechanical Polishing) is a **planarization process** for metal and dielectric layers,  
where **layout density uniformity** directly affects manufacturing quality.

本セクションでは、CMP非均一性による不具合と、**Metal Fill（ダミーパターン）**による対応技術を学びます。  
This section covers CMP-related issues and the use of **metal fill (dummy patterns)** to address them.

---

## 🧩 CMPとは | What is CMP?

| 項目 / Item | 内容 / Description |
|-------------|--------------------|
| **目的<br>Purpose** | 層間の段差をなくし、表面を平坦に保つ<br>Eliminates step differences between layers for planar surfaces |
| **工法<br>Method** | スラリー＋パッドでの機械的・化学的研磨<br>Mechanical + chemical polishing using slurry and pad |
| **適用層<br>Target Layers** | メタル層間、STI、ILD など<br>Metal layers, STI, interlayer dielectrics |
| **問題点<br>Issues** | パターン密度に依存して研磨量に差 → **オーバー研磨／アンダー研磨**<br>Polishing rate varies with pattern density → **Over- or under-polishing** |

---

## ⚠️ CMP非均一性の問題 | Issues from CMP Non-Uniformity

- ⚡ **配線密度が高い部分は研磨不足、低密度部分は過研磨**  
  High-density areas are under-polished, while low-density areas are over-polished
- 🧨 その結果：
  - **Via露出不足 / Via Contact Failure**
  - **Metal断線・短絡 / Open or Short in Metal Lines**
  - **誘電膜厚の不均一 → クロストーク上昇 / Non-uniform dielectric thickness → Crosstalk increase**

---

## 🧱 Metal Fill（ダミーパターン）の種類 | Types of Dummy Patterns

| 種類 / Type | 用途 / Purpose | 配慮点 / Considerations |
|-------------|----------------|--------------------------|
| **Dummy Metal** | 空白領域を金属で埋めて密度均一化<br>Fills empty areas to equalize density | 信号とのカップリング抑制距離を確保<br>Maintain spacing to minimize coupling |
| **Dummy Via** | Via密度均一化、構造対称性向上<br>Equalize via density, improve symmetry | 層間接続への影響を最小化<br>Minimize impact on routing layers |
| **Dummy Poly** | ポリシリコン領域の密度均一化（特にゲート間）<br>Equalize poly density, especially between gates | デバイス特性への影響を避けるため配置に制約あり<br>Requires careful placement to avoid affecting device behavior |

---

## 📐 Density Rule（密度ルール） | Density Rule in PDK

- 📏 **局所密度制約：40〜60%**（例：100μm × 100μm ウィンドウ）  
  **Local density range**: typically 40–60% within a defined window (e.g., 100μm × 100μm)
- 📊 **層ごとの平均密度チェック（global & local）**  
  Density constraints apply to each metal layer both globally and locally
- 🔁 一定以上の空白領域では**自動Metal Fillが挿入される**  
  Automated metal fill insertion is applied where gaps exceed defined thresholds

> ✅ 多くのEDAツール（Innovus, ICC2など）で**Auto Fill機能**が利用可能  
> Most EDA tools provide **Auto Fill** functionality before tapeout

---

## 🛠️ 実務上の工夫 | Practical Considerations

- 🧩 **Dummy Metalに擬似Net（Dummy Net）を割り当てる**ことで浮遊容量の影響を軽減  
  Assigning dummy nets to dummy metal can reduce parasitic coupling
- 🛑 **クロック・高速信号配線の周囲はFill除外**（除外リージョン）  
  Exclude fill around high-speed/clock nets to prevent noise
- 🔄 **Guard Ring（ガードリング）との兼ね合いにも注意**  
  Be mindful of interactions with guard rings used for latch-up prevention

---

## 🎯 教材的意義 | Educational Perspective

- 🎓 「なぜ空白を埋めるのか？」を**CMP物理から理解する**  
  Understand "why we fill empty spaces" from a CMP physics perspective
- 🤖 **自動設計ツールの内部原理を学ぶ入り口に**  
  A gateway to understanding the internal logic of automated design tools
- 🛡️ **設計によって製造信頼性が大きく変わることを実感**  
  Realize how design choices impact **manufacturing reliability**

---

## 🔗 次のセクション | Next Section

➡ [`ir_drop_and_em.md`](./ir_drop_and_em.md)：IRドロップとエレクトロマイグレーション対策へ  
➡ *IR Drop and Electromigration Countermeasures*

---

🧱 応用編 第4章：レイアウト設計と最適化 /  
🧱 *Applied Chapter 4: Layout Design and Optimization*  
[📘 セクション一覧 / Section Index](../d_chapter4_layout_optimization/README.md)

---

© 2025 Shinichi Samizo / MIT License
