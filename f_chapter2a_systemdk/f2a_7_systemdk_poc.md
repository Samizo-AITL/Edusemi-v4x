# 🎓 f2a_7_systemdk_poc.md  
**SystemDKベースの統合PoC演習課題**  
**SystemDK-Based PoC Exercise**

---

## 📘 目的｜Objective

本演習では、SystemDKの観点から物理制約（SI/PI、熱、応力、EMI/EMC）を考慮した  
**チップレット統合設計PoC** を構築・検証するプロジェクトを提案します。  
This exercise proposes a PoC project that incorporates physical constraints into chiplet-based system design using SystemDK principles.

---

## 📐 課題テーマ｜Exercise Theme

> 「2.5D構造を用いたマルチチップ統合設計を行い、物理制約項目に基づく評価・改善提案を行え。」

### ✅ 条件例｜Example Requirements

- 複数のチップレット（ロジック、メモリ、I/O）を2.5Dインターポーザ上に配置
- PDN構造を設計し、IR Dropとインピーダンス整合を確認（SI/PI）
- 熱源分布と冷却経路をモデリング（Thermal）
- バンプ構造と接合界面における応力を評価（Mechanical Stress）
- EMIフィルタリングやグラウンド設計を含むノイズ設計（EMI/EMC）

---

## 🧰 提案ツールと構成｜Suggested Tools & Setup

| カテゴリ | 推奨ツール／内容 |
|----------|----------------|
| 回路モデル | SPICE, Verilog-A, IBIS |
| 配置設計 | Excel/CSVで抽象配置 → SVG可視化 or KiCAD |
| SI/PI解析 | PowerDC, Ansys SIwave, openEMS（オプション） |
| 熱解析 | Icepak, COMSOL Multiphysics |
| 機械応力 | COMSOL, SolidWorks Simulation |
| EMI/EMC検証 | HFSS, Simplorer（例示） |

※教材では簡易モデルと可視化ツールによる**物理直感重視**の演習を推奨。

---

## 📝 レポート構成例｜Suggested Report Structure

1. 設計目的と構成概要（チップ構成・PKG構造）
2. 各物理制約に関する考察とモデル設定
3. 問題点とトレードオフ評価（IR Drop vs EMIなど）
4. 構造・材料・配線変更による改善提案
5. SystemDKとしての設計判断まとめ

---

## 📎 関連リンク｜Related Links

- [SystemDK README](./README.md)
- [f2a_2_sipi.md](./f2a_2_sipi.md)
- [f2a_3_thermal.md](./f2a_3_thermal.md)
- [f2a_4_mechanical.md](./f2a_4_mechanical.md)
- [f2a_5_emi_emc.md](./f2a_5_emi_emc.md)
- [f_chapter2_chiplet_pkg/](../f_chapter2_chiplet_pkg/)

---

## 🧭 今後の展開｜Future Extensions

- PoCからのSystemDKテンプレート化と再利用設計  
- Sky130/CaravelなどのRTL設計との接続を視野に入れた**PoC-to-Product展開**  
- 教材内演習として複数制約を**数式モデル化＋可視化＋検証**する統合演習展開

---

## 🧑‍🏫 教育目的の注記｜Educational Note

この演習は、理論のみでなく**設計判断に伴う物理的感覚と衝突関係**を体験的に学ぶための構成です。  
実際のEDAツールがなくとも、**関係性と対立構造を整理することが主目的**です。
