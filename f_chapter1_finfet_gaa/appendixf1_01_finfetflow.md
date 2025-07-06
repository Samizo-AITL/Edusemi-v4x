# 補足資料：FinFET 製造プロセスフロー（全48ステップ）

本資料は、FinFET（Fin Field-Effect Transistor）の製造における主要工程を48ステップに分解し、各ステップの目的・プロセス条件・技術的ポイントを詳細に記述したものである。

---

## 🔹 前提情報

- **対象プロセスノード**：10〜5nm世代のFinFET
- **基板仕様**：300 mm P型 Si（100）、抵抗率：10 Ω·cm前後
- **目的**：プレーナMOSFETを超える短チャネル制御とゲート制御性の実現

---

## 🔸 プロセスフロー一覧（概要）

| ステップ範囲 | 工程群                             | 主な内容                                                  |
|--------------|------------------------------------|-----------------------------------------------------------|
| Step 1–3     | 基板準備・ウェル形成               | ウェーハ処理、STI（絶縁）、n/pウェル、チャネル形成など   |
| Step 4–6     | ゲート形成                         | ゲート酸化膜成長、ポリSi堆積、パターニング               |
| Step 7–9     | S/D形成（拡散層含む）              | ソース・ドレイン拡張/本体注入、スパーサ形成、アニール   |
| Step 10–15   | コンタクト形成                     | シリサイド、ILD、コンタクトビア形成、Cuめっき、CMP       |
| Step 16–21   | 第1層メタル配線（M1）              | 配線・ビア定義、バリア/シード、Cu充填、CMP               |
| Step 22–26   | 上位メタル層（M2〜Mx）形成         | 層間膜形成、配線・ビア形成、Cu埋込、CMP                  |
| Step 27–30   | パッシベーション・UBM形成          | Cap層、最終保護膜、パッド開口、下部バンプ金属形成        |
| Step 31–35   | ビア形成・3D実装対応               | 上層ビア、TSV準備、マイクロバンプ、上層ILD形成           |
| Step 36–40   | 最終メタル層処理とCMP              | 上層配線パターニング、ダマシンエッチ、Cuめっき・CMP       |
| Step 41–43   | 設計検証・最終UBM形成              | RC抽出、再UBM露出と形成、露出面整合                     |
| Step 44–48   | ウェーハ仕上げ・テスト・実装       | ウェーハ薄化、最終パッシベーション、テスト、ダイシング、パッケージング |

---

## ① 初期工程（Step 1〜3）

### Step 1: Substrate Preparation
- **目的**：高純度Si基板を準備し、表面清浄度を確保
- **条件**：p型Si (100)、~10 Ω·cm、RCA洗浄＋150°C脱水ベーク
- **技術ポイント**：微細Fin形成に向けた表面平滑性・金属残渣除去が重要

---

### Step 2: STI (Shallow Trench Isolation)
- **目的**：デバイス間を電気的に分離する絶縁構造を形成
- **条件**：ArF浸潤リソ→フッ素系RIE→TEOS CVD→CMPで平坦化
- **技術ポイント**：トレンチ深さ200nm程度、STIストレスによるVthシフトに留意

---

### Step 3: Well and Channel Implantation
- **目的**：n/pウェル・チャネル形成、しきい値制御用のドーピング
- **条件**：B (p-well), As/P (n-well), 10¹²〜10¹³ cm⁻², 30〜80 keV、RTAによる活性化
- **技術ポイント**：ウェルばらつきはしきい値の分布を劣化させる

---

## ② ゲート前形成（Step 4〜6）

### Step 4: Gate Oxide Growth
- **目的**：ゲート絶縁膜として高品質なSiO₂を形成
- **条件**：乾式酸化（800–900°C）、厚み1.5–2 nm
- **技術ポイント**：界面準位密度低減がリーク低減・信頼性に直結

---

### Step 5: Poly-Si Deposition and Doping
- **目的**：ゲート電極となるポリシリコンの堆積とドーピング
- **条件**：LPCVD（~100 nm）、in-situ P/Asまたは後工程でイオン注入
- **技術ポイント**：粒界の導電性・ドーピング均一性が重要

---

### Step 6: Gate Patterning
- **目的**：微細ゲート形状の定義（CD制御）
- **条件**：193 nm ArF immersion、HBr/Cl₂ RIEによるエッチング、CD ~30 nm
- **技術ポイント**：CD変動によるVth・ドレイン電流ばらつき抑制

---

## ③ S/D領域形成（Step 7〜9）

### Step 7: S/D Extension Implantation
- **目的**：チャネル端近傍への軽度ドーピングにより短チャネル効果を抑制
- **条件**：B or As注入、10¹³〜10¹⁴ cm⁻²、~5–20 keV、スパイクRTA
- **技術ポイント**：浅い接合でリークと抵抗のバランスを取る

---

### Step 8: Spacer Formation
- **目的**：S/D本注入範囲を定義するサイドウォールスペーサの形成
- **条件**：LPCVD Si₃N₄ or SiO₂（10–20 nm）→異方性RIEで成形
- **技術ポイント**：幅・厚みのばらつきがSDE長に影響

---

### Step 9: S/D Main Implant
- **目的**：ソース／ドレイン領域に高濃度注入し、低抵抗化
- **条件**：As or B, ~10¹⁵ cm⁻², 30–80 keV、RTAで活性化
- **技術ポイント**：深すぎると短チャネル効果増加、浅すぎるとRs増加

---

## ④ シリサイド形成（Step 10）

### Step 10: Silicide Formation
- **目的**：ゲート/S/Dに低抵抗コンタクト層を形成（NiSi or CoSi₂）
- **条件**：PVDでNiまたはCo堆積→400–600°Cアニール→未反応金属除去
- **技術ポイント**：過剰反応やラインエッジリセッションを防止

---

## ⑤ ILD・コンタクト形成（Step 11〜15）

### Step 11: Interlayer Dielectric (ILD) Deposition
- **目的**：メタル配線とトランジスタの絶縁
- **条件**：SiO₂またはSiCOH（k ~2.7–3.0）、PECVDまたはSACVD、厚さ300–500 nm
- **技術ポイント**：平坦性・低応力・欠陥ゼロが求められる

---

### Step 12: Contact Hole Etch
- **目的**：ILDをエッチングしてS/Dやゲートへの接続孔を形成
- **条件**：193nm ArF露光、CH₄/O₂またはFC系プラズマRIE、CD ~30–50 nm
- **技術ポイント**：シリサイド露出が完全であることが低抵抗に直結

---

### Step 13: Barrier and Seed Deposition (Contact)
- **目的**：Cu拡散防止と電解めっき導入層
- **条件**：TiNまたはTaN（ALD）、Cuシード（PVD）、バリア5–10 nm、シード~50 nm
- **技術ポイント**：被覆不良やボイドはオープン故障原因

---

### Step 14: Cu Electroplating (ECP) for Contact
- **目的**：コンタクトビアを銅で充填
- **条件**：酸性CuSO₄浴、10–30 mA/cm²、厚み200–400 nm（オーバーフィル）
- **技術ポイント**：添加剤制御で均一・ボイドレスを実現

---

### Step 15: CMP of Contacts
- **目的**：ECPの過剰CuをCMPで除去し表面を平坦化
- **条件**：Al₂O₃またはSiO₂系スラリー、モーター電流＋光モニタで終点検出
- **技術ポイント**：残膜<5 nm、ILDダメージ最小化

---

## ⑥ メタル配線（M1）（Step 16〜21）

### Step 16: First Metal (M1) Deposition & Patterning
- **目的**：第1層Cu配線の形成（配線＋ビア）
- **条件**：193nm ArF or EUV、Dual Damascene、CD 20–30 nm
- **技術ポイント**：配線RC・寄生容量最小化設計が必要

---

### Step 17: ILD Deposition (M1–M2)
- **目的**：メタル層間の絶縁層形成
- **条件**：Low-k SiCOH、PECVD、厚み300–500 nm
- **技術ポイント**：界面密着と誘電率制御

---

### Step 18: Lithography & Etch for M2
- **目的**：M2の配線パターンとビア形成
- **条件**：ArF immersion or EUV、FC系RIE、CD 20–30 nm
- **技術ポイント**：寸法制御とオーバーレイ精度

---

### Step 19: Barrier/Seed Deposition for M2
- **目的**：ECPのためのバリア・シード層形成
- **条件**：Ta/TaN（ALD）、Cuシード（PVD）、厚み同上
- **技術ポイント**：Via底部へのコンフォーマル性

---

### Step 20: Cu Electroplating for M2
- **目的**：M2ビア・配線層へのCu充填
- **条件**：添加剤付きCuSO₄浴、厚み200–400 nm
- **技術ポイント**：スロットル電流制御で埋込均一性確保

---

### Step 21: CMP of M2 Cu Layer
- **目的**：M2上部の平坦化、次層への準備
- **条件**：同様のCMP条件、表面粗さ<0.5 nm RMS
- **技術ポイント**：次リソグラフィとの連携精度に影響

---

## ⑦ 上位メタル層形成（Step 22〜26）

### Step 22: ILD Deposition (M2–Mx)
- **目的**：上層メタルの絶縁形成
- **条件**：Low-k材料（k=2.5–3.0）、厚み300–500 nm
- **技術ポイント**：低誘電率と強度のバランス

---

### Step 23: Lithography & Etching for Mx
- **目的**：上位メタルのパターン・ビア形成
- **条件**：EUVまたはArF immersion、CD 20–30 nm、Dual Damascene
- **技術ポイント**：高アスペクト比Via形成と寸法均一性

---

### Step 24: Barrier & Seed Deposition (Mx)
- **目的**：ECP前の準備（拡散防止＋導電種）
- **条件**：Ta/TaN（ALD）、Cu（PVD）、同様の厚み
- **技術ポイント**：Via底部の膜厚均一性

---

### Step 25: Cu Electroplating (Mx)
- **目的**：上層メタルのCu埋込
- **条件**：先述と同等、過剰堆積→CMP対象
- **技術ポイント**：ライン長・ビアサイズに応じた電流制御

---

### Step 26: CMP of Mx Layers
- **目的**：上位層の平坦化
- **条件**：Alumina/SiO₂スラリー、ディッシング／エロージョン対策
- **技術ポイント**：ラインエッジ保持と微細構造の保護

---

## ⑧ パッシベーションとUBM形成（Step 27〜30）

### Step 27: Cap Layer Deposition
- **目的**：Cu配線の拡散防止・機械保護（SiN, SiCNなど）
- **条件**：PECVDまたはLPCVD、厚さ20–50 nm、低ストレス
- **技術ポイント**：ストレス低減によるウェーハ反り防止

---

### Step 28: Passivation Layer Deposition
- **目的**：全体保護用パッシベーション層（SiN, SiO₂など）
- **条件**：PECVD、厚さ0.5–1.0 µm、ピンホールなし
- **技術ポイント**：密着性・水分バリア性が要求される

---

### Step 29: Pad Opening Lithography and Etch
- **目的**：バンプ形成に向けたパッド部露出
- **条件**：193nm ArF露光、F系RIE、UBM露出面を精密制御
- **技術ポイント**：エッチング過剰でUBM損傷リスク

---

### Step 30: Under Bump Metallization (UBM)
- **目的**：バンプ接続用金属（NiV/Cu/Auなど）を形成
- **条件**：PVD + 電解Ni/Cu/Au、厚さ合計~10 µm
- **技術ポイント**：機械強度＋拡散防止＋濡れ性確保

---

## ⑨ TSV・3D実装対応（Step 31〜35）

### Step 31: Via Formation for Upper Metal
- **目的**：メタル層間（Mx-Mx+1）のビア形成
- **条件**：FC/ArプラズマによるRIE、CD ~20–30 nm
- **技術ポイント**：エッチストップ層への制御精度

---

### Step 32: Barrier & Seed Deposition (Via)
- **目的**：Via内部へのTaN/Cu堆積
- **条件**：バリア（ALD）、シード（PVD）、厚み5–10 nm/50 nm
- **技術ポイント**：高アスペクト比Viaへの被覆性

---

### Step 33: Cu Electroplating (Via)
- **目的**：Via銅埋込
- **条件**：酸性CuSO₄浴、ボイドレス充填
- **技術ポイント**：柱状結晶抑制と完全埋込

---

### Step 34: CMP of Cu Via/Wiring
- **目的**：Via・配線部の平坦化
- **条件**：Cu選択CMP、残膜<5 nm
- **技術ポイント**：Dishing・トップビュー均一性

---

### Step 35: Upper ILD Deposition
- **目的**：上層絶縁膜（SiCOH等）形成
- **条件**：PECVD、厚み300–500 nm
- **技術ポイント**：誘電率低減と吸湿抑制

---

## ⑩ テスト・出荷前工程（Step 36〜48）

### Step 36: Lithography for Upper Metal
- **目的**：上層配線パターン形成
- **条件**：ArF immersion or EUV、CD ~20–30 nm
- **技術ポイント**：Overlay精度とLWR制御が課題

---

### Step 37: Dual Damascene Etch
- **目的**：ビア＋配線溝の同時エッチ
- **条件**：FC系RIE、垂直プロファイル制御
- **技術ポイント**：過エッチ抑制と寸法均一性

---

### Step 38: Barrier & Seed Deposition (Upper Metal)
- **目的**：Cu ECP前のTa/TaN + Cu堆積
- **条件**：ALD + PVD、膜厚：バリア5–10 nm、シード50 nm
- **技術ポイント**：パターン密度による埋込均一性管理

---

### Step 39: Cu Electroplating (Upper Metal)
- **目的**：上層Cu埋込
- **条件**：従来通り、ボイドレス充填・過剰堆積
- **技術ポイント**：マクロ欠陥・樹状成長の回避

---

### Step 40: CMP of Upper Metal
- **目的**：最終層のCu CMP
- **条件**：選択CMP、平坦度 < 0.5 nm RMS
- **技術ポイント**：次工程（パッシベーション）への表面品質保証

---

### Step 41: RC Extraction and Parasitics
- **目的**：配線の抵抗・容量抽出による回路遅延評価
- **条件**：EDAツールによるポストレイアウト抽出
- **技術ポイント**：RC delay < 60 ps/mm を目標

---

### Step 42: Pad Opening for UBM
- **目的**：最終UBM露出（パッケージ接続用）
- **条件**：ArFスキャナ＋RIE、UBM損傷なしが必須
- **技術ポイント**：微細PAD位置制御精度

---

### Step 43: UBM再形成（NiV/Cu/Au）
- **目的**：最終パッドへのUBM追加形成（バンプ接続強化）
- **条件**：PVD + ECP、厚み ~10 µm
- **技術ポイント**：フリップチップ対応の信頼性担保

---

### Step 44: Wafer Thinning
- **目的**：ウェーハ厚を~100 µm以下に薄化し、熱・3D集積性向上
- **条件**：バックグラインディング + CMP
- **技術ポイント**：反り・割れ防止と均一性維持

---

### Step 45: TSV/Micro Bump Formation
- **目的**：3D IC対応の垂直接続（TSV）とマイクロバンプ形成
- **条件**：DRIEによるTSV形成、Cu ECP、SnAgまたはPbフリーバンプ
- **技術ポイント**：高信頼・高密度・低Voidingが要求される

---

### Step 46: Final Passivation
- **目的**：最終保護膜（SiNまたはSiO₂）でデバイスを保護
- **条件**：PECVD、厚さ0.5–1.0 µm、低ストレス・高密着
- **技術ポイント**：水分・異物遮断性能

---

### Step 47: Wafer Test and Dicing
- **目的**：電気的良否判定とダイシング
- **条件**：ATEによる速度・リーク・機能検査 → レーザー or ソーイング
- **技術ポイント**：マーキング・トレーサビリティと切断ダメージ抑制

---

### Step 48: Packaging
- **目的**：最終製品としての実装（FC-CSP、FOWLP等）
- **条件**：ダイアタッチ、ワイヤ／バンプ接続、モールド、アンダーフィル
- **技術ポイント**：機械強度、放熱、量産性のバランス設計

---

## 🔸 補足図（図示予定）

- `images/finfet_process_overview.png`
- `images/finfet_metallization_stack.png`
- `images/finfet_final_test_packaging.png`

---

## 🔸 備考

- 本補足資料は、特別編 第1章「先端ノード（FinFET、GAA等）」の理解を補完するための技術解説です。
- 対応するGAA版プロセスフローは [`appendixf1_02_gaaflow.md`](./appendixf1_02_gaaflow.md) を参照してください。

---

## ライセンスと著者

MITライセンスにて公開。  
著者：三溝 真一（Shinichi Samizo）  
連絡先：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)
