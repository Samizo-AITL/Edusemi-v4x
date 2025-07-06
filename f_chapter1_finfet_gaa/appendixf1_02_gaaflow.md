# 補足資料：GAA Multi-Nanosheet FET 製造プロセスフロー（全48ステップ）

本資料では、先端ノードにおける GAA（Gate-All-Around）Multi-Nanosheet FET の製造プロセスを全48ステップで分解し、各工程の目的・プロセス条件・技術的な要点を体系的に記述します。

---

## 🔹 前提情報

- **対象構造**：GAA Multi-Nanosheet FET（5nm～2nm世代）
- **基板仕様**：300 mm Si（⟨100⟩）、p型、TTV < 1 µm、Bow < 40 µm
- **チャネル構成**：Si/SiGe積層（例：Si 5 nm / SiGe 8 nm ×3）
- **目的**：短チャネル制御を最大化するフルサラウンドゲート構造の実現

---

## 🔸 プロセスフロー一覧（概要）

| ステップ範囲 | 工程群                             | 主な内容                                                  |
|--------------|------------------------------------|-----------------------------------------------------------|
| Step 1–3     | 基板準備・ウェル形成               | SOIまたはエピ基板、STI、ウェル形成                       |
| Step 4–6     | チャネルスタック形成               | Si/SiGe多層堆積、初期酸化膜整形                          |
| Step 7–9     | ナノシート形成・チャネル露出        | パターン形成、選択エッチによるSiGe除去                   |
| Step 10–15   | ゲート堆積と定義                    | High-k/メタルゲート形成、GAA構造包囲                     |
| Step 16–26   | S/D形成とコンタクト                 | Epitaxy, Anneal, Silicide, ILD, CMP                       |
| Step 27–48   | 配線形成、UBM、テスト・パッケージング | FinFETとほぼ同一のフロー構成（適宜差異を記述）          |

---

## ① 基板準備・チャネル多層形成（Step 1〜6）

### Step 1: Substrate Preparation (SOI or Bulk)
- **目的**：GAA用高品質SOI基板または薄エピ層Si基板の準備
- **条件**：300 mm、(100) Si、BOX厚 ~145 nm（SOI）、または薄エピ ~20 nm（bulk）
- **技術ポイント**：ボディ効果抑制とアンダーカット性を両立させる選択が必要

---

### Step 2: Shallow Trench Isolation (STI)
- **目的**：デバイス間絶縁の形成
- **条件**：通常と同様、ArF露光 + RIE、TEOS埋込 + CMP
- **技術ポイント**：ナノシート整形後に形状崩れしないSTI平坦性が求められる

---

### Step 3: Well and Channel Implantation
- **目的**：チャネル領域のn-well/p-well形成
- **条件**：B, As, P注入、~10¹³ cm⁻²、RTA ~1000°C
- **技術ポイント**：ナノシート層へ不要な拡散を避ける低温プロファイルが望ましい

---

### Step 4: Channel Stack Deposition (Si/SiGe Multi-Layer)
- **目的**：交互のSi/SiGe層スタック（3~5層）で後のナノシート構造を形成
- **条件**：超高真空CVD（UHVCVD）またはRP-CVD、Si ~5–8 nm、SiGe ~10 nm
- **技術ポイント**：厚さ均一性と界面鮮明性がナノワイヤ品質に直結

---

### Step 5: Channel Stack Oxidation and Capping
- **目的**：初期酸化膜（インターフェース品質確保）、保護膜形成
- **条件**：ドライ酸化またはALD酸化、SiO₂ ~1–2 nm、Si₃N₄キャップ ~5 nm
- **技術ポイント**：ナノシート界面の欠陥密度を極小化

---

### Step 6: Hardmask Deposition & Lithography
- **目的**：チャネルスタックパターン形成のためのハードマスク堆積と露光
- **条件**：SiNまたはTiNハードマスク、ArFまたはEUVリソ、CD ~20–30 nm
- **技術ポイント**：エッチング耐性とCD均一性の両立

---

## ② ナノシート構造形成・ゲート形成（Step 7〜15）

### Step 7: Stack Etch (Channel Fin Patterning)
- **目的**：チャネルスタックをFin状にパターニング
- **条件**：垂直プロファイルのRIE、SiN/TiNハードマスク使用
- **技術ポイント**：側壁荒れを抑えるエッチ制御が重要

---

### Step 8: Selective SiGe Etch (Nanogap Formation)
- **目的**：SiGe層の除去によるナノシート間隙形成（GAA空間）
- **条件**：HClベースの選択エッチ、Si保持率 > 100:1
- **技術ポイント**：Siゲート支持構造の崩壊防止が最重要

---

### Step 9: Inner Spacer Deposition
- **目的**：ナノシート下部・側部の空隙に絶縁膜（SiN）形成
- **条件**：ALDまたはLPCVDによるSiN、アニールによる膜均一化
- **技術ポイント**：後のゲート包囲の形状を決める重要工程

---

### Step 10: Dummy Gate Fill
- **目的**：プレゲート形成（後のHigh-k/Metal Gateプロセスを分離）
- **条件**：Poly-Si堆積、CMP平坦化、パターン露出
- **技術ポイント**：ゲートリプレースに向けた厚み管理

---

### Step 11: Source/Drain Extension Implant
- **目的**：軽いS/D拡張注入で短チャネル効果抑制
- **条件**：BまたはAs低エネルギー注入、~10¹³–10¹⁴ cm⁻²
- **技術ポイント**：チャネル近傍での拡がり抑制が重要

---

### Step 12: Inner Spacer Etch Back
- **目的**：内側スペーサのリセス（部分除去）
- **条件**：RIE + CMP制御
- **技術ポイント**：S/Dエピ成長領域の確保

---

### Step 13: Raised Source/Drain Epitaxy
- **目的**：シリコン or SiGeによるS/D隆起層成長（抵抗低減）
- **条件**：Selective Epi、B/Asドープ、高さ ~20–30 nm
- **技術ポイント**：段差／ファセット形成抑制

---

### Step 14: Dummy Gate Removal
- **目的**：Poly-Siゲート除去によりHigh-kゲート形成準備
- **条件**：選択的エッチ（TMAH等）、シート保持
- **技術ポイント**：ナノシート破壊防止のプロセス管理

---

### Step 15: High-k / Metal Gate Stack Deposition
- **目的**：GAA構造を包囲するHigh-k絶縁膜＋メタルゲート堆積
- **条件**：ALDによるHfO₂、TiN/TiAlNなどのメタルゲート、CMP整形
- **技術ポイント**：全面包囲性と界面準備、しきい値調整膜選定

---

## ③ S/D仕上げとコンタクト形成（Step 16〜26）

### Step 16: S/D Implantation
- **目的**：ソース・ドレインの本注入で低抵抗化
- **条件**：As（nMOS）、B（pMOS）、~10¹⁵ cm⁻²、30–80 keV
- **技術ポイント**：ナノシート側壁への不要拡散を防ぐアングル注入が有効

---

### Step 17: Dopant Activation Anneal
- **目的**：注入不純物の活性化と欠陥修復
- **条件**：Spike RTA ~1050°C、短時間で結晶性維持
- **技術ポイント**：チャネルダメージ回避と活性化率バランスが課題

---

### Step 18: Silicide Formation
- **目的**：S/Dおよびゲート部への低抵抗シリサイド形成
- **条件**：NiまたはCoスパッタ + アニール（400–600°C）、未反応金属除去
- **技術ポイント**：ナノシート上部の金属拡散防止が重要

---

### Step 19: Interlayer Dielectric (ILD) Deposition
- **目的**：金属層とチャネル構造の絶縁
- **条件**：SiO₂または低k（SiCOH）膜、PECVD、~400 nm
- **技術ポイント**：シート包囲構造を埋めるための流動性とストレス制御

---

### Step 20: Chemical Mechanical Planarization (CMP)
- **目的**：ILD表面の平坦化と後工程の露出
- **条件**：CMPスラリー制御、SiNストップ層を利用
- **技術ポイント**：過研磨による構造崩壊を防止

---

### Step 21: Contact Hole Lithography
- **目的**：S/D・ゲートに接続するコンタクトホール定義
- **条件**：ArFまたはEUV露光、CD ~30–50 nm
- **技術ポイント**：選択性の高いエッチとCD精度

---

### Step 22: Contact Etch
- **目的**：コンタクトホールのエッチング
- **条件**：フルオロカーボン系RIE、エッチストップ層検出
- **技術ポイント**：ナノシートゲート下部のリーク防止構造の保護

---

### Step 23: Barrier and Seed Deposition (Contact)
- **目的**：コンタクト内壁にバリア・銅シードを形成
- **条件**：ALDでTiN/TaN、PVDでCuシード、バリア5–10 nm、シード ~50 nm
- **技術ポイント**：高アスペクト比への均一性が要求される

---

### Step 24: Copper Electrochemical Plating (ECP)
- **目的**：コンタクトホール内部の銅埋込
- **条件**：酸性Cu硫酸浴、添加剤制御、厚さ ~200–400 nm（オーバーフィル）
- **技術ポイント**：ボイドレス充填と後CMPとの整合性

---

### Step 25: CMP of Contact Copper
- **目的**：銅オーバーフィルの除去と平坦化
- **条件**：Cu選択CMPスラリー、エンドポイント制御
- **技術ポイント**：ILD露出後の残膜管理（<5 nm）

---

### Step 26: ILD Deposition over Contact
- **目的**：第1層配線（M1）への絶縁層形成
- **条件**：低k膜（SiCOHなど）、PECVD、厚さ ~300–500 nm
- **技術ポイント**：キャッピング機能と低ストレス両立

---

## ④ 配線層（M1〜Mx）、上層構造形成（Step 27〜34）

※以下の工程（Step 27〜34）は FinFETと同様のプロセスだが、**構造的な要求精度**がGAAでより厳しくなる。

---

### Step 27: M1 Lithography and Etch
- **目的**：第1層メタル配線定義（デュアルダマシン）
- **条件**：ArFまたはEUV露光、CD ~20–30 nm、RIE加工
- **技術ポイント**：配線歪みによるRC遅延への影響を最小化

---

### Step 28: Barrier/Seed Deposition for M1
- **目的**：ビア＋配線の銅めっき前処理
- **条件**：Ta/TaNバリア（ALD）、Cuシード（PVD）、バリア ~5–10 nm、シード ~50 nm
- **技術ポイント**：ナノスケール溝への均一膜形成

---

### Step 29: Copper ECP for M1
- **目的**：M1ビア・トレンチのCu充填
- **条件**：通常の酸性浴、電流密度制御、オーバーフィルあり
- **技術ポイント**：ビアボイド／クラック抑制とスムーズなCMP対応

---

### Step 30: CMP of M1 Copper
- **目的**：M1配線の平坦化
- **条件**：Cu選択CMPスラリー、エンドポイント光学検出
- **技術ポイント**：面内均一性とラインエッジ整合性

---

### Step 31: ILD Deposition (M1–M2)
- **目的**：M1とM2間の絶縁層
- **条件**：SiCOH系低k膜、厚さ ~400 nm、PECVD
- **技術ポイント**：層間寄生容量を最小化

---

### Step 32: Lithography and Etch for Higher Metal (M2〜Mx)
- **目的**：上位メタル配線・ビア形成
- **条件**：EUV/ArF露光、RIE、CD ~20–30 nm
- **技術ポイント**：深いスタックでのアライメント精度

---

### Step 33: Barrier/Seed & Cu Plating (M2〜Mx)
- **目的**：バリア・シード堆積 → Cu充填（M2〜Mx）
- **条件**：TaN + Cu（ALD + PVD）、ECPによりオーバーフィル
- **技術ポイント**：多層堆積におけるストレス／ボイド制御

---

### Step 34: CMP of Higher Metal
- **目的**：配線層表面の平坦化
- **条件**：同様のCMPスラリーとプロセス
- **技術ポイント**：ビアリングエッジのエロージョン防止

---

## ⑤ 上層メタル・キャップ層・パッド・パッケージ工程（Step 35〜48）

### Step 35: Cap Layer Deposition
- **目的**：Cu配線を保護するキャッピング層（SiN/SiCN）形成
- **条件**：PECVD、膜厚 ~20–50 nm
- **技術ポイント**：応力とMoistureバリア性能の両立

---

### Step 36: Passivation Layer Deposition
- **目的**：最終保護層（SiN/SiO₂）を形成し外部環境から保護
- **条件**：PECVD、膜厚 ~0.5–1.0 µm、密着性と無欠陥性重視
- **技術ポイント**：はんだバンプとの密着不良防止

---

### Step 37: Pad Opening Lithography and Etch
- **目的**：最終パッド（UBM）接続用の開口形成
- **条件**：ArF露光、RIEによるSiN/SiO₂開口
- **技術ポイント**：UBMパッドのダメージ防止が必須

---

### Step 38: Under Bump Metallization (UBM)
- **目的**：NiV/Cu/Au等で構成されるメタル積層でバンプ接続を確保
- **条件**：PVD + 電解メッキ、総厚 ~10 µm
- **技術ポイント**：接着・拡散・はんだ濡れ性の最適化

---

### Step 39: Wafer Thinning (Back Grinding)
- **目的**：パッケージ厚制御や3D統合のためのウエハ薄化
- **条件**：バックグラインド + CMP、最終厚 ~100 µm以下
- **技術ポイント**：チップ曲がり／応力緩和と破損防止

---

### Step 40: Through-Silicon Via (TSV) & Microbump Formation
- **目的**：3D実装に向けた縦配線構造とマイクロバンプ形成
- **条件**：
  - TSV：DRIEエッチ + Cu埋込 + バリア層形成
  - Bump：SnAg/Pb-Free ~20–30 µm
- **技術ポイント**：TSVボイドレス形成とCuクラック防止

---

### Step 41: Final Passivation
- **目的**：最終保護膜としてのパッシベーション
- **条件**：SiNまたはSiO₂、PECVD、厚さ0.5–1.0 µm
- **技術ポイント**：密着性・熱ストレス・パッケージとの整合

---

### Step 42: Final Wafer Test
- **目的**：ダイシング前の機能・電気特性試験
- **条件**：ATEにてリーク電流、しきい値、遅延、歩留まり確認
- **技術ポイント**：GAA構造由来のしきい値分布制御

---

### Step 43: Wafer Dicing
- **目的**：個別チップへ分離（シンギュレーション）
- **条件**：レーザースクライビングまたはソーイング、低ダメージ処理
- **技術ポイント**：薄型ウエハの割れ抑制と高精度

---

### Step 44: Die Attach
- **目的**：基板へのダイ実装
- **条件**：銀ペースト接着または接着剤、熱圧着
- **技術ポイント**：接着厚・熱伝導と平坦性制御

---

### Step 45: Flip-Chip Bonding or Wire Bonding
- **目的**：パッケージ基板との電気接続
- **条件**：
  - Flip Chip：バンプ + リフロー接合
  - ワイヤ：金・銅線による超音波接合
- **技術ポイント**：信号整合と熱ストレス分散

---

### Step 46: Underfill Application
- **目的**：バンプ接合部を封止し信頼性確保
- **条件**：エポキシ系材料、ディスペンス + キュア（硬化）
- **技術ポイント**：ボイドフリー塗布とC.T.E.整合

---

### Step 47: Final Test and Marking
- **目的**：完成品の最終品質保証試験とロットマーキング
- **条件**：電気特性、機能、速度試験；レーザー刻印
- **技術ポイント**：3σ管理とトレーサビリティ

---

### Step 48: Packaging (FC-CSP, WLP, FOWLPなど)
- **目的**：量産パッケージへの封止
- **条件**：FC-CSP, WLP, FOWLP, SiPなどアプリケーションに応じた選択
- **技術ポイント**：熱設計、実装性、コストのバランス最適化

---

## 📘 補足

- 📷 図版（構造断面や工程模式図）は `/images/gaa_*.png` に格納予定
- 📚 参考文献は別途 appendixf1_ref.md に整理
- 🏷️ 著者：Shinichi Samizo / MIT License（再利用可）

---

## 🔸 図版（予定）

- `images/gaa_stack_structure.png`：Si/SiGeナノシート構造
- `images/gaa_process_flowchart.png`：GAAプロセスフロー図
- `images/gaa_release_step.png`：犠牲層除去によるナノシート形成断面

---

## 🔸 補足

- 本資料は FinFET版の [`appendixf1_01_finfetflow.md`](./appendixf1_01_finfetflow.md) と対応します。
- 各ステップの工程時間・装置・統計制御指標（例：AFM Rq, OES signal）も随時追記予定。

---

## ライセンスと著者

MITライセンスにて公開。  
著者：三溝 真一（Shinichi Samizo）  
連絡先：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)
