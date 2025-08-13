---
layout: default
title: Edusemi-v4x/index.md
---

<!-- ページ専用スタイル -->
<link rel="stylesheet" href="{{ '/assets/css/edusemi.css' | relative_url }}"/>

# 🎓 Edusemi-v4x  
**半導体プロダクト開発のための基礎教育教材**  
🇺🇸 *Foundational Educational Materials for Semiconductor Product Development*  
<a class="btn-link" href="./README_en.md">English README →</a>

---

## ✍️ はじめに | Introduction

半導体技術は **トランジスタの発明** から始まり、**MOS構造** の登場で急速に進化しました。  
**微細化と集積化** はムーアの法則に沿って進み、LSIはあらゆる分野に広がっています。

しかし、**物性・回路・プロセス・テスト** は教育では分断されがち。実務では密接につながり、  
**回路はデバイス原理に依存し、設計はプロセスと信頼性に支えられます**。  
**Edusemi-v4x** はこの「**基礎技術同士の構造的つながり**」に焦点を当て、応用を見据えた **構造的理解** を育てます。

> 💡 *Design follows physics, and productization follows verification.*  
> 物性→回路→実装→検証までの接続を可視化します。

---

## 📘 プロジェクト概要 | Project Overview

**Edusemi-v4x** は、**設計・製造・検査・品質保証** を一貫して学べる **オープン教材** です。

- 🎯 **対象**：工学系学生／若手技術者／教育者  
- 🌟 **特徴**：基礎のつながり重視、設計〜量産検査まで網羅  
- 🧪 **実習**：sky130・OpenLane・Python・GitHub・ChatGPT

---

## 🧭 基礎編 | Fundamentals

<table class="nice-table">
<thead><tr><th>章</th><th>タイトル</th><th>概要</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="chapter1_materials/README.md">半導体物性と材料基礎</a></td><td>バンド構造・PN接合・MOS電界効果</td></tr>
<tr><td>2</td><td><a href="chapter2_comb_logic/README.md">デジタル論理と回路設計</a></td><td>組み合わせ回路・順序回路・FSM・HDL</td></tr>
<tr><td>3</td><td><a href="chapter3_process_evolution/README.md">プロセス技術と微細化の制約</a></td><td>ノード変遷・配線・リソ・信頼性</td></tr>
<tr><td>4</td><td><a href="chapter4_mos_characteristics/README.md">MOSトランジスタ特性</a></td><td>寸法・特性・PDK・デザインルール</td></tr>
<tr><td>5a</td><td><a href="chapter5a_spec_module_if/README.md">仕様策定とIF設計</a></td><td>上流工程・モジュール選定・PoC接続</td></tr>
<tr><td>5</td><td><a href="chapter5_soc_design_flow/README.md">SoC設計フロー</a></td><td>RTL・P&R・DRC/LVS・タイミング</td></tr>
<tr><td>6</td><td><a href="chapter6_test_and_package/README.md">テスト・パッケージ</a></td><td>ETEST・不良解析・信頼性試験・出荷</td></tr>
<tr><td>7</td><td><a href="chapter7_design_review_and_org/README.md">デザインレビューと組織連携</a></td><td>SRAM不良事例・DR構造・合意形成</td></tr>
</tbody>
</table>

---

## 🧩 応用編 | Applications

<table class="nice-table">
<thead><tr><th>章</th><th>タイトル</th><th>概要</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="d_chapter1_memory_technologies/README.md">メモリ技術</a></td><td>SRAM・DRAM・FeRAM・MRAM</td></tr>
<tr><td>2</td><td><a href="d_chapter2_high_voltage_devices/README.md">高耐圧デバイス</a></td><td>LDMOS・電界制御・高電圧設計</td></tr>
<tr><td>3</td><td><a href="d_chapter3_esd_protection_design/README.md">ESD設計</a></td><td>保護素子・破壊事例・試験規格</td></tr>
<tr><td>4</td><td><a href="d_chapter4_layout_optimization/README.md">レイアウト最適化</a></td><td>CMPダミー・IRドロップ・ラッチアップ</td></tr>
<tr><td>5</td><td><a href="d_chapter5_analog_mixed_signal/README.md">アナログ／MIX信号</a></td><td>アナログ設計・ノイズ・混載設計</td></tr>
<tr><td>5a</td><td><a href="d_chapter5a_analog_mixed_signal/README.md">0.18μm AMS設計技法</a></td><td>ばらつき・マッチング・1/fノイズ</td></tr>
<tr><td>5b</td><td><a href="d_chapter5b_ams_block_and_pdk/README.md">製造起点のAMS差別化</a></td><td>1/fノイズ低減・製造技術応用</td></tr>
<tr><td>6</td><td><a href="d_chapter6_pdk_and_eda_environment/README.md">PDKとEDA環境</a></td><td>DRC/LVS/ERC・PDK構成</td></tr>
<tr><td>7</td><td><a href="d_chapter7_automation_and_verification/README.md">自動化と検証</a></td><td>OpenLane・CI/CD・Lint</td></tr>
<tr><td>8</td><td><a href="d_chapter8_fsm_design_basics/README.md">FSM設計</a></td><td>Moore/Mealy・状態遷移図・Verilog</td></tr>
<tr><td>9</td><td><a href="d_chapter9_pll_and_clock_design/README.md">PLLとクロック</a></td><td>PLL構造・ジッタ・STA配慮</td></tr>
</tbody>
</table>

---

## 🛠 実践編 | Practice

<table class="nice-table">
<thead><tr><th>章</th><th>タイトル</th><th>概要</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="e_chapter1_python_automation_tools/README.md">Python自動化ツール</a></td><td>SPICE解析・OpenLaneログ処理</td></tr>
<tr><td>2</td><td><a href="e_chapter2_sky130_experiments/README.md">Sky130実験</a></td><td>Vg–Id・Vth推定・BTI/TDDB評価</td></tr>
<tr><td>3</td><td><a href="e_chapter3_openlane_practice/README.md">OpenLane実習</a></td><td>合成〜配置配線〜GDS出力</td></tr>
<tr><td>4</td><td><a href="e_chapter4_poc_spec_and_design/README.md">PoC設計展開</a></td><td>FSM・MUX・Adder・テスト</td></tr>
<tr><td>5</td><td><a href="e_chapter5_evaluation_and_report/README.md">評価とレポート</a></td><td>面積・波形・タイミング・DRC/LVS</td></tr>
</tbody>
</table>

---

## 📦 特別編 | Special Topics

<table class="nice-table">
<thead><tr><th>章</th><th>タイトル</th><th>概要</th></tr></thead>
<tbody>
<tr><td>1</td><td><a href="f_chapter1_finfet_gaa/README.md">先端ノード</a></td><td>FinFET・GAA・CFETと設計影響</td></tr>
<tr><td>2</td><td><a href="f_chapter2_chiplet_pkg/README.md">チップレットと先端パッケージ</a></td><td>2.5D/3D・TSV・異種集積</td></tr>
<tr><td>2a</td><td><a href="f_chapter2a_systemdk/README.md">SystemDK実装制約設計</a></td><td>SI/PI・熱・応力・EMI/EMC</td></tr>
<tr><td>3</td><td><a href="f_chapter3_socsystem/README.md">統合制御SoC実装</a></td><td>FSM×PID×LLM（AITL）</td></tr>
<tr><td>4</td><td><a href="f_chapter4_openlane/README.md">OpenLane実装</a></td><td>統合制御RTLの配置配線</td></tr>
<tr><td>5</td><td><a href="f_chapter5_dfm/README.md">DFM設計</a></td><td>DRC・LVS・DFM指針・Sky130</td></tr>
</tbody>
</table>

---

## 🤖 ChatGPT連携 | AI Integration

学習者は ChatGPT を **学習パートナー** として、コード添削・エラー解析・ツール操作・レポート補助に活用できます。  
現代の設計現場に即した **対話型・実務直結型学習** を支援します。

---

## 🔗 関連プロジェクト | Related Projects

<ul class="icon-list">
  <li>🎛️ <a href="https://samizo-aitl.github.io/EduController/">EduController</a> – 制御理論〜AI制御、OpenLane連携</li>
  <li>🤖 <a href="https://samizo-aitl.github.io/AITL-H/">AITL-H</a> – FSM＋PID＋LLMの三層制御アーキテクチャ</li>
  <li>🌐 <a href="https://samizo-aitl.github.io/Edusemi-Plus/">Edusemi-Plus</a> – 地政学・戦略・AI・量子・投資の応用教材</li>
</ul>

---

## 👤 執筆者 | Author

**三溝 真一（Shinichi Samizo）**  
信州大学大学院 電気電子工学 修了  
元 セイコーエプソン株式会社 技術者（1997〜）

📌 経験領域：半導体デバイス・インクジェット薄膜アクチュエータ・製品化・ISO教育  
✉️ <a href="mailto:shin3t72@gmail.com">shin3t72@gmail.com</a> | 🐦 <a href="https://x.com/shin3t72">@shin3t72</a> | 💻 <a href="https://samizo-aitl.github.io/">Website</a>

---

## 📄 ライセンス | License

MITライセンスに基づき、自由に使用・改変・再配布が可能。教育・研究・社内研修への活用も歓迎します。  
<a class="btn-link" href="revision_history.md">改訂履歴（ChangeLog）</a>　
<a class="btn-secondary" href="https://github.com/Samizo-AITL/Edusemi-v4x/discussions">Discussions →</a>
