# 📈 appendix_f1_node_evolution.md  
## プロセス技術の進化と物理パラメータ推移  
## Evolution of Process Nodes and Key Physical Parameters

本資料では、**90nm以降のCMOSプロセス進化**を構造形式・物理パラメータ・技術課題の観点から整理します。  
This appendix summarizes the evolution of CMOS technology from 90nm to GAA/CFET, including structure types, physical parameters, and key challenges.

---

## 📊 プロセス進化表｜Process Evolution Table

| ノード / Node | 構造 / Structure | 電源電圧 / VDD | Tox [nm] | 最小L [nm] | 主な特徴 / Features | 技術課題 / Challenges |
|---------------|------------------|----------------|----------|------------|----------------------|------------------------|
| 90nm          | プレーナMOS       | 1.2V           | ~2.0     | ~65        | NiSi, strained-Si, LDD最適化 | 寄生容量、リーク電流、リソ制約 |
|               | 💬 NiSiサリサイドと応力導入によってトランジスタ性能向上が図られた初期段階。 |
| 65nm          | プレーナMOS       | 1.1V           | ~1.7     | ~50        | Low-k導入、高濃度チャネル | 配線遅延、短チャネル効果 |
|               | 💬 配線RC遅延が問題となり、Low-k材料の導入とチャネルドープ制御の最適化が重要課題に。 |
| 45nm          | プレーナMOS       | 1.0V           | ~1.3     | ~35        | HKMG準備、ULK材料 | ゲート制御性限界、Variability |
|               | 💬 High-k/Metal Gateの導入直前。リーク電流制御が限界に達しつつあった。 |
| 32nm          | HKMGプレーナ      | 0.9V           | ~1.0     | ~28        | High-k/Metal Gate開始 | Vtばらつき、Tinv制御 |
|               | 💬 Intelにより初めて本格導入。EOT低減とリーク制御を両立させた画期的技術。 |
| 22nm          | FinFET（初代）    | 0.85V          | ~0.9     | ~20        | Tri-Gate構造、3D Channel | Fin形状ばらつき、設計複雑化 |
|               | 💬 チャネルを立体化することで短チャネル効果を抑制。Fin寸法と密度の制御が鍵に。 |
| 14/10nm       | FinFET（主流）    | 0.75–0.80V     | ~0.8     | ~16        | マルチパターニング、BEOL低誘電率化 | 面積効率、SRAMスケーリング |
|               | 💬 FinFETが量産の主流となり、配線層の多層化とSRAMの微細化限界が焦点に。 |
| 7nm           | FinFET + EUV     | 0.65–0.70V     | ~0.7     | ~12        | EUV初導入、複雑LELELE配線 | 遮光膜設計、熱管理 |
|               | 💬 EUV露光の試験導入によりマルチパターニングの複雑さを緩和しつつ歩留まり維持を目指す。 |
| 5nm           | GAA試験開始       | 0.6–0.65V      | ~0.6     | ~8         | Nanosheet構造登場 | シート制御、Routability低下 |
|               | 💬 SamsungなどがNanosheet GAAの試作・開発に入り、Fin構造の限界を超える試み。 |
| 3nm           | GAA主流           | 0.55–0.60V     | ~0.5     | ~5         | Samsung/TSMCで採用、多チャンネル積層 | 高密度寄生、バラツキ制御困難 |
|               | 💬 多チャンネルのstacked構造が一般化し、チャンネル数による性能調整が設計課題に。 |
| ＜2nm         | CFET開発中         | 0.5V以下        | ~0.4     | ~4         | PMOS/NMOS stacked構造 | 熱干渉、配線・電源分離、歩留まり課題 |
|               | 💬 垂直方向の集積によりセル面積削減を狙うが、配線・放熱・製造歩留まりが大きな壁となる。 |

---

## 🔍 用語補足｜Glossary

- **HKMG**: High-k / Metal Gate（高誘電率材料とメタルゲート）
- **ULK**: Ultra Low-k（極低誘電率絶縁膜）
- **CFET**: Complementary FET（NMOS・PMOSの縦積層構造）

---

## 🧩 今後の教材との連携予定

- [`appendix_f1_02_gaaflow.md`](./appendix_f1_02_gaaflow.md)：GAAプロセス構造との整合化  
- [`appendix_f1_04_cfet.md`](./appendix_f1_04_cfet.md)：CFET構造の進展との相関補足  
- [`process_node_comparison.md`](./process_node_comparison.md)：0.18〜90nmとの比較統合表へ反映  

---

## 📄 ライセンス / License

MIT License に基づき、自由な教育・研究活用を歓迎します。

---

📎 [トップに戻る / Back to Home](../README.md)
