---
layout: default
title: 0.18μm FeRAM Process Flow（強誘電体メモリプロセス）
---

---

# 📘 0.18μm FeRAM Process Flow（強誘電体メモリプロセス）

[![Hybrid License](https://img.shields.io/badge/license-Hybrid-blueviolet)](https://samizo-aitl.github.io/Edusemi-v4x/#-ライセンス--license)

> ⚠️ **注意 / Notice**  
> 本プロセスフローは、三溝真一による**構想・教育目的**のプロセス設計に基づいています。実在する製品・製造フロー・企業機密とは一切関係ありません。  
> *This process flow is a conceptual and educational design proposed by **Shinichi Samizo**. It is not related to any actual product, manufacturing process, or proprietary information.*

---

## 📋 フルプロセスフロー / Full Process Table 

| 工程名 | 処理内容 | 分類 | 目的 | 処理条件 | 寸法 | 膜厚 | Mask |
|--------|----------|------|------|----------|------|------|------|
| FS-DP | SiON保護膜堆積 | 全体 | 界面保護 | 200Å @ 700℃ | - | - | - |
| FSN-DP | STI用窒化膜堆積 | Field | 酸化防止キャップ | 1500Å @ 750℃ | - | - | - |
| F-PH | フォトリソグラフィ（マスク露光） | Field | パターン定義（レジスト形成） | - | 0.28μm | - | F |
| F-ET | エッチング（RIE等） | Field | 不要層の除去（パターン転写） | - | 0.28μm | - | - |
| F-DP | STI酸化膜埋込 | Field | トレンチフィル | - | - | 4000Å | - |
| F-CMP | STI CMP | Field | 平坦化 | - | - | - | - |
| PRE-OX   | 犠牲酸化膜形成                    | 前処理 | 注入前の表面改質・汚染取り込み           | Dry OX, 約80Å                 | -              | 80Å        | -      |
| NWL-PH   | フォトリソグラフィ（マスク露光）  | Well   | パターン定義（レジスト形成）             | -                             | -              | -          | NWL    |
| NWL-ION  | イオン注入（ドーピング）          | Well   | N-Well形成                               | 800keV, 2E13                  | -              | -          | -      |
| PWL-PH   | フォトリソグラフィ（マスク露光）  | Well   | パターン定義（レジスト形成）             | -                             | -              | -          | PWL    |
| PWL-ION  | イオン注入（ドーピング）          | Well   | P-Well形成                               | 200keV, 5E12                  | -              | -          | -      |
| NCD-PH   | フォトリソグラフィ（マスク露光）    | CD     | Nchチャネル領域の定義                  | -                  | 1.8V      | -      | NCD    |
| NCD-ION  | イオン注入（チャネルドープ）        | CD     | NMOSのしきい値調整                     | Boron, 50keV, 1E13 | 1.8V      | -      | -      |
| PCD-PH   | フォトリソグラフィ（マスク露光）    | CD     | Pchチャネル領域の定義                  | -                  | 1.8V      | -      | PCD    |
| PCD-ION  | イオン注入（チャネルドープ）        | CD     | PMOSのしきい値調整                     | BF₂, 30keV, 1E13   | 1.8V      | -      | -      |
| NCD2-PH  | フォトリソグラフィ（マスク露光）    | CD     | Nchチャネル領域の定義（再調整）        | -                  | 3.3V      | -      | NCD    |
| NCD2-ION | イオン注入（チャネルドープ）        | CD     | NMOSのしきい値調整（再調整）           | Boron, 50keV, 1E13 | 3.3V      | -      | -      |
| PCD2-PH  | フォトリソグラフィ（マスク露光）    | CD     | Pchチャネル領域の定義（再調整）        | -                  | 3.3V      | -      | PCD    |
| PCD2-ION | イオン注入（チャネルドープ）        | CD     | PMOSのしきい値調整（再調整）           | BF₂, 30keV, 1E13   | 3.3V      | -      | -      |
| G1-OX    | ゲート酸化膜形成（第1段）           | Gate   | 全MOS領域に初期酸化膜を形成            | Dry OX             | 全MOS領域 | 35Å    | -      |
| G1-PH    | フォトリソグラフィ（3.3V保護）      | Gate   | 3.3Vデバイスをレジスト保護             | -                  | 3.3V      | -      | G1     |
| G1-ET    | 酸化膜除去（1.8V領域）              | Gate   | 1.8V領域のG1酸化膜を除去               | HF or SPM          | 1.8V      | 0Å     | -      |
| G2-OX    | ゲート酸化膜形成（第2段）           | Gate   | 1.8V領域に再酸化膜を形成（合計70Å）    | Dry OX             | 1.8V      | 35Å    | -      |
| PLY-DP   | ポリゲート堆積（Poly-Si）           | Gate   | ゲート電極材料形成                     | LPCVD              | -         | 1500Å  | -      |
| PLY-PH   | フォトリソグラフィ（マスク露光）    | Gate   | ポリゲートパターン定義（レジスト形成） | KrF                | 0.18μm    | -      | PLY    |
| PLY-ET   | ポリゲートパターンエッチング（RIE） | Gate   | ポリゲート構造定義                     | RIE                | 0.18μm    | -      | -      |
| NLL-PH   | フォトリソ Lithography              | NMOS   | LDDパターン形成（ロジック用）          | KrF, CD = 0.18μm   | 1.8V      | -      | NLL    |
| NLL-ION  | イオン注入 Ion Implantation         | NMOS   | 浅拡散形成（ロジック）                 | As, 30keV, 1E13    | 1.8V      | -      | -      |
| PLL-PH   | フォトリソ Lithography              | PMOS   | LDDパターン形成（ロジック用）          | KrF, CD = 0.18μm   | 1.8V      | -      | PLL    |
| PLL-ION  | イオン注入 Ion Implantation         | PMOS   | 浅拡散形成（ロジック）                 | BF₂, 30keV, 1E13   | 1.8V      | -      | -      |
| NLM-PH   | フォトリソ Lithography              | NMOS   | LDDパターン形成（メモリ用）            | KrF, CD = 0.22μm   | 3.3V      | -      | NLM    |
| NLM-ION  | イオン注入 Ion Implantation         | NMOS   | 浅拡散形成（メモリ）                   | As, 30keV, 1E13    | 3.3V      | -      | -      |
| PLM-PH   | フォトリソ Lithography              | PMOS   | LDDパターン形成（メモリ用）            | KrF, CD = 0.22μm   | 3.3V      | -      | PLM    |
| PLM-ION  | イオン注入 Ion Implantation         | PMOS   | 浅拡散形成（メモリ）                   | BF₂, 30keV, 1E13   | 3.3V      | -      | -      |
| SW-DP       | スペーサ堆積（SiN）              | Gate     | LDD保護 / S/D形成のためのスペーサ形成       | LPCVD, SiN, 800Å            | -        | 800Å   | -      |
| SW-ET       | スペーサエッチング（RIE）        | Gate     | アニソトロピックエッチングでスペーサ定義     | RIE                         | -        | -      | -      |
| NLL2-PH     | フォトリソグラフィ               | NMOS S/D | 1.8V NMOS 深拡散領域パターン定義            | KrF                         | 0.18μm   | -      | NLL2   |
| NLL2-ION    | イオン注入                       | NMOS S/D | 1.8V NMOSソース・ドレイン深拡散形成          | As, 40keV, 1E13             | -        | -      | -      |
| PLL2-PH     | フォトリソグラフィ               | PMOS S/D | 1.8V PMOS 深拡散領域パターン定義            | KrF                         | 0.18μm   | -      | PLL2   |
| PLL2-ION    | イオン注入                       | PMOS S/D | 1.8V PMOSソース・ドレイン深拡散形成          | BF₂, 40keV, 1E13            | -        | -      | -      |
| NLM2-PH     | フォトリソグラフィ               | NMOS S/D | 3.3V NMOS 深拡散領域パターン定義            | KrF                         | 0.22μm   | -      | NLM2   |
| NLM2-ION    | イオン注入                       | NMOS S/D | 3.3V NMOSソース・ドレイン深拡散形成          | As, 40keV, 1E13             | -        | -      | -      |
| PLM2-PH     | フォトリソグラフィ               | PMOS S/D | 3.3V PMOS 深拡散領域パターン定義            | KrF                         | 0.22μm   | -      | PLM2   |
| PLM2-ION    | イオン注入                       | PMOS S/D | 3.3V PMOSソース・ドレイン深拡散形成          | BF₂, 40keV, 1E13            | -        | -      | -      |      
| CO-SP | Coスパッタリング | Salicide | 前駆体形成 | - | - | 300Å | - |
| LMP-ANL | サリサイドアニール | Salicide | CoSi形成 | 550℃ 30s | - | - | - |
| CO-ET | エッチング（RIE等） | Salicide | 不要層の除去（パターン転写） | H2SO4系 | - | - | - |
| LMP2-ANL | 相転移アニール | Salicide | CoSi₂形成 | 750℃ 30s | - | - | - |
| F2-DP | ILD堆積 | ILD | 配線前絶縁 | PE-TEOS | - | 6000Å | - |
| F2-CMP | ILD CMP | CMP | 平坦化 | CMP | - | - | - |
| CNT-PH | フォトリソグラフィ（マスク露光） | Via | パターン定義（レジスト形成） | - | 0.24μm | - | CNT |
| CNT-ET | エッチング（RIE等） | Via | 不要層の除去（パターン転写） | - | 0.24μm | - | - |
| TIN-SP   | コンタクトバリアスパッタ         | Via       | バリアメタル形成（W下地）    | DC Sputter, TiN, 300W, Ar | -      | 300Å   | -      |
| CW-DP    | Wデポジション                    | Via       | Wプラグ形成（充填）          | CVD, WF₆                  | -      | 4000Å  | -      |
| CW-CMP   | W CMP                            | CMP       | Wプラグ上の平坦化            | CMP                       | -      | -      | -      |
| TI1-SP      | Tiスパッタ           | Capacitor    | 密着層（Pt下地）          | DC Sputter, 300W, Ar, RT     | -         | 300Å     | -      |
| Pt-SP      | Ptスパッタ           | Capacitor    | 下部電極                  | DC Sputter, 1kW, Ar, RT      | -         | 1500Å    | -      |
| PZT-COT    | PZTスピンコート      | Capacitor    | 強誘電体形成（前駆体）     | Sol-Gel Spin, 3000rpm        | -         | 1000Å    | -      |
| PZT-ANL    | PZTアニール          | Capacitor    | 強誘電性確保（結晶化）     | RTA, 650℃, O₂, 60s           | -         | 結晶化   | -      |
| TI2-SP      | Tiスパッタ           | Capacitor    | 上部電極（Al接続下地）     | DC Sputter, 300W, Ar, RT     | -         | 300Å     | -      |
| CAP-PH     | Capフォトリソ        | Capacitor    | キャパシタパターン定義     | KrF, 248nm, 60mJ/cm²         | 0.35μm    | -        | CAP    |
| CAP-ET     | Capエッチング        | Capacitor    | Pt/PZT/Tiパターン形成     | Ion Milling | 0.35μm | -     | -      |
| ALOX-SP    | AlOxスパッタ         | Capacitor    | PZT保護膜（一次）         | RF Sputter, 400W, Ar/O₂      | -         | 300Å     | -      |
| ALOX-DP    | AlOx ALDデポ         | Capacitor    | 高密度保護膜（最終）       | ALD, 200℃, TMA/H₂O           | -         | 300Å     | -      |
| ALOX-PH    | AlOxフォトリソ       | Capacitor    | 接続開口パターン定義       | KrF, 248nm, 60mJ/cm²         | 0.35μm    | -        | ALOX   |
| ALOX-ET    | AlOxエッチング       | Capacitor    | 接続開口形成               | RIE (BCl₃/Cl₂系)             | 0.35μm    | -        | -      |
| HLX-DP     | ILD-0堆積            | 層間絶縁膜   | Metal-0上絶縁              | PE-TEOS, 400℃                | -         | 6000Å    | -      |
| HLX-PH     | フォトリソグラフィ   | 層間絶縁膜   | Via-0開口パターン定義      | KrF, 248nm, 60mJ/cm²         | 0.24μm    | -        | HLX    |
| HLX-ET     | エッチング（RIE）     | 層間絶縁膜   | Via-0開口形成              | RIE (CHF₃/O₂)                | 0.24μm    | -        | -      |
| TINX-SP    | Ti/TiN バリアスパッタ| バリア        | Wプラグ拡散防止層          | DC/RF Sputter, 2-step        | -         | 300Å     | -      |
| HWX-DP     | Wプラグ堆積（CVD）   | Plug         | Via-0充填                 | W-CVD, WF₆, 400℃             | -         | 5000Å    | -      |
| HWX-CMP    | W CMP                | Plug         | Metal-1接続のための平坦化  | CMP (Slurry: Silica/Alumina) | -         | -        | -      |
| ALA-SP | Metal-1 Al堆積 | 配線層 | セル配線 | - | - | 6000Å | - |
| ALA-PH | フォトリソグラフィ（マスク露光） | 配線層 | パターン定義（レジスト形成） | - | 0.28μm | - | ALA |
| ALA-ET | エッチング（RIE等） | 配線層 | 不要層の除去（パターン転写） | - | 0.28μm | - | - |
| HLA-DP | ILD-1堆積 | 層間絶縁膜 | Metal-1上絶縁 | PE-TEOS | - | 6000Å | - |
| HLA-PH | フォトリソグラフィ（マスク露光） | 層間絶縁膜 | パターン定義（レジスト形成） | RIE+フォト | 0.24μm | - | HLA |
| HLA-ET | エッチング（RIE等） | 層間絶縁膜 | 不要層の除去（パターン転写） | RIE+フォト | 0.24μm | - | - |
| TINA-SP | Ti/TiN バリア | バリア | Via-1バリア | 300Å | - | 300Å | - |
| HWA-DP | Wプラグ堆積（Via-1） | Plug | Metal-2接続 | W-CVD | - | 5000Å | - |
| HWA-CMP | W CMP（Via-1） | Plug | 平坦化 | CMP | - | - | - |
| ALB-SP | Metal-2 Al堆積 | 配線層 | 中間配線 | - | - | 6000Å | - |
| ALB-PH | フォトリソグラフィ（マスク露光） | 配線層 | パターン定義（レジスト形成） | - | 0.35μm | - | ALB |
| ALB-ET | エッチング（RIE等） | 配線層 | 不要層の除去（パターン転写） | - | 0.35μm | - | - |
| HLB-DP | ILD-2堆積 | 層間絶縁膜 | Metal-2上絶縁 | PE-TEOS | - | 6000Å | - |
| HLB-PH | フォトリソグラフィ（マスク露光） | 層間絶縁膜 | パターン定義（レジスト形成） | RIE+フォト | 0.28μm | - | HLB |
| HLB-ET | エッチング（RIE等） | 層間絶縁膜 | 不要層の除去（パターン転写） | RIE+フォト | 0.28μm | - | - |
| TINB-SP | Ti/TiN バリア | バリア | Via-2バリア | 300Å | - | 300Å | - |
| HWB-DP | Wプラグ堆積（Via-2） | Plug | Metal-3接続 | W-CVD | - | 5000Å | - |
| HWB-CMP | W CMP（Via-2） | Plug | 平坦化 | CMP | - | - | - |
| ALC-SP | Metal-3 Al堆積 | 配線層 | グローバル配線 | - | - | 8000Å | - |
| ALC-PH | フォトリソグラフィ（マスク露光） | 配線層 | パターン定義（レジスト形成） | - | 0.5μm | - | ALC |
| ALC-ET | エッチング（RIE等） | 配線層 | 不要層の除去（パターン転写） | - | 0.5μm | - | - |
| HLC-DP | ILD-3堆積 | 層間絶縁膜 | Metal-3上絶縁 | PE-TEOS | - | 6000Å | - |
| HLC-PH | フォトリソグラフィ（マスク露光） | 層間絶縁膜 | パターン定義（レジスト形成） | RIE+フォト | 0.35μm | - | HLC |
| HLC-ET | エッチング（RIE等） | 層間絶縁膜 | 不要層の除去（パターン転写） | RIE+フォト | 0.35μm | - | - |
| TINC-SP | Ti/TiN バリア | バリア | Via-3バリア | 300Å | - | 300Å | - |
| HWC-DP | Wプラグ堆積（Via-3） | Plug | Pad接続 | W-CVD | - | 5000Å | - |
| HWC-CMP | W CMP（Via-3） | Plug | 平坦化 | CMP | - | - | - |
| ALD-SP | Pad用Al堆積 | Pad層 | Bond Pad形成 | - | - | 10000Å | - |
| ALD-PH | フォトリソグラフィ（マスク露光） | Pad層 | パターン定義（レジスト形成） | - | 3.0μm | - | PAD |
| ALD-ET | エッチング（RIE等） | Pad層 | 不要層の除去（パターン転写） | - | 3.0μm | - | - |
| PAD-DP | パッシベーション膜堆積 | 保護膜 | 外部環境保護 | SiN+SiO₂ | - | 8000Å | - |
| PAD-PH | フォトリソグラフィ（マスク露光） | 保護膜 | パターン定義（レジスト形成） | - | 3.0μm | - | PAD |
| PAD-ET | エッチング（RIE等） | 保護膜 | 不要層の除去（パターン転写） | - | 3.0μm | - | - |
| E-TEST | 電気特性評価 | 検査 | Vth/Ioff測定 | 自動テスター | - | - | - |

