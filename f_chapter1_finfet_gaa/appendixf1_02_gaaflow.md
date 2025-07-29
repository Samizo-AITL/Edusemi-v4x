# 📘 GAA Multi-Nanosheet FET 製造プロセスフロー  
# 📘 GAA Multi-Nanosheet FET Process Flow

本ドキュメントでは、**先端ノード（5nm〜2nm世代）で採用されるGAA（Gate-All-Around）Multi-Nanosheet FET**の製造プロセスを、**日本語・英語併記形式**で段階的に解説します。各ステップは**目的・条件・技術要点**の3点に整理され、**表形式＋太字メリハリ**で視覚的に理解しやすい構成となっています。

---

## 🔹 前提情報 / Basic Assumptions

| 項目 / Item | 内容（日本語） | Description (English) |
|-------------|----------------|------------------------|
| **構造 / Structure** | GAA Multi-Nanosheet FET（Si/SiGeスタック構造） | GAA Multi-Nanosheet FET with Si/SiGe stacking |
| **適用ノード / Target Node** | 5nm〜2nm CMOSロジック | 5nm–2nm CMOS logic |
| **基板 / Substrate** | 300 mm Si (100), p型, TTV < 1 µm | 300 mm Si (100), p-type, TTV < 1 µm |
| **チャネル / Channel Stack** | Si 5nm / SiGe 10nm × 3〜5層 | Si 5nm / SiGe 10nm × 3–5 layers |
| **主目的 / Main Goal** | ゲートによる完全包囲制御を通じたSCE抑制 | Suppression of SCE via full gate control |

---

## 🔸 Step 1：基板準備 / Substrate Preparation

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | 高品質SOIまたはエピタキシャルSi基板を準備する | Prepare high-quality SOI or epitaxial Si substrate |
| **条件 / Conditions** | 300mm Si (100), BOX厚 145nm（SOI）またはエピ厚 ~20nm | 300mm Si (100), BOX thickness ~145nm (SOI) or epi-layer ~20nm |
| **技術要点 / Key Points** | アンダーカット性と電気特性の最適バランスを取る | Optimize trade-off between undercut profile and electrical performance |

---

## 🔸 Step 2：STI形成 / Shallow Trench Isolation (STI)

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | トランジスタ間の電気絶縁を確保する | Ensure electrical isolation between devices |
| **条件 / Conditions** | ArF露光 + RIE + TEOS埋込 → CMP | ArF lithography + RIE + TEOS fill → CMP |
| **技術要点 / Key Points** | STI平坦性が後工程のチャネル構造形成に影響する | STI planarity critically affects channel stack patterning |

---

## 🔸 Step 3：ウェル注入 / Well Implantation

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | p-well / n-well を形成してチャネル領域を定義する | Define p-well/n-well regions for the channel |
| **条件 / Conditions** | B, As, P注入（~10¹³ cm⁻²）、RTA ~1000℃ | Implant B, As, P (~10¹³ cm⁻²), RTA at ~1000°C |
| **技術要点 / Key Points** | ナノシートスタックへの熱拡散を抑えることが重要 | Suppressing thermal diffusion into nanosheet stack is critical |

---

## 🔸 Step 4：チャネル積層堆積 / Channel Stack Deposition

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | Si/SiGeの多層構造を堆積し、後のナノシート構造を形成する | Deposit multilayer Si/SiGe stack to form future nanosheet |
| **条件 / Conditions** | RP-CVDまたはUHV-CVD、Si 5–8nm / SiGe 10nm ×3 | RP-CVD or UHV-CVD, Si 5–8nm / SiGe 10nm ×3 |
| **技術要点 / Key Points** | 界面のシャープネスと厚さ均一性が性能に直結 | Interface sharpness and thickness uniformity are essential |

---

## 🔸 Step 5：初期酸化とキャップ形成 / Initial Oxidation & Capping

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | チャネル表面を酸化し、後のゲート絶縁膜の品質を高める | Oxidize channel surface to improve gate dielectric quality |
| **条件 / Conditions** | ドライ酸化またはALD酸化、SiO₂ ~1–2nm + SiNキャップ ~5nm | Dry or ALD oxidation, SiO₂ ~1–2nm + SiN cap ~5nm |
| **技術要点 / Key Points** | 酸化によるチャネル界面欠陥の低減がカギ | Interface defect suppression is critical for reliability |

---

## 🔸 Step 6：ハードマスク堆積とリソグラフィ / Hardmask Deposition & Lithography

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | パターン形成用のハードマスク層を形成し、ナノシートパターンを描画 | Form hardmask layer and define nanosheet pattern |
| **条件 / Conditions** | TiN/SiN堆積、ArFまたはEUV露光、CD ~20–30nm | TiN/SiN deposition, ArF or EUV lithography, CD ~20–30nm |
| **技術要点 / Key Points** | 高アスペクト比の忠実な転写と後工程耐性が要求される | High aspect-ratio pattern fidelity and etch resistance required |

---

## 🔸 Step 7：チャネルパターンエッチ / Stack Etch (Channel Fin Patterning)

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | チャネルスタックをFin状にエッチングし、ナノシート構造の外形を定義する | Etch the channel stack into fin shape to define nanosheet outline |
| **条件 / Conditions** | 垂直プロファイルのRIE、TiN/SiNハードマスク使用 | Vertical-profile RIE with TiN/SiN hardmask |
| **技術要点 / Key Points** | 側壁の粗さ・下部アンダーカットを最小化するエッチ条件が重要 | Critical to minimize sidewall roughness and undercut at base |

---

## 🔸 Step 8：選択的SiGe除去 / Selective SiGe Etch (Nanogap Formation)

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | SiGe犠牲層を除去し、ナノシート間の空間（GAAゲート用空洞）を形成する | Remove SiGe sacrificial layers to form gaps for GAA gate |
| **条件 / Conditions** | HClベースの選択エッチ、Si/SiGe選択比 > 100:1 | HCl-based selective etch, Si/SiGe selectivity > 100:1 |
| **技術要点 / Key Points** | Si層（ナノシート）を損傷せずにSiGeのみを確実に除去する必要がある | Must fully remove SiGe while preserving Si nanosheet integrity |

---

## 🔸 Step 9：内側スペーサ堆積 / Inner Spacer Deposition

| 項目 | 内容（日本語） | Description (English) |
|------|----------------|------------------------|
| **目的 / Purpose** | ナノシート周囲に絶縁スペーサ（SiN等）を形成して、S/D隔離とゲート包囲準備を行う | Form insulating inner spacers (e.g., SiN) around nanosheets for S/D isolation and gate encapsulation |
| **条件 / Conditions** | ALDまたはLPCVDによるSiN堆積、アニールで密着強化 | SiN deposition via ALD or LPCVD, followed by annealing |
| **技術要点 / Key Points** | ナノギャップへの均一充填と後工程でのスペーサエッチ制御性がカギ | Key to achieve uniform gap fill and precise etch control in later steps |

---

## 🔸 Step 10：ダミーゲート形成 / Dummy Gate Fill

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | High-k/Metalゲートプロセス前のポリシリコンによる仮ゲート形成 | Form a temporary gate using poly-Si before High-k/Metal gate process |
| **条件 / Conditions** | Poly-Si堆積 → CMP平坦化 | Poly-Si deposition followed by CMP planarization |
| **技術要点 / Key Points** | 厚み均一性と後工程（除去時）の処理性を両立 | Balance thickness uniformity and removability in later steps |

---

## 🔸 Step 11：S/D拡張注入 / Source/Drain Extension Implant

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 短チャネル効果（SCE）抑制のための浅い注入 | Shallow implant to suppress short channel effects (SCE) |
| **条件 / Conditions** | B⁺ / As⁺、10¹³–10¹⁴ cm⁻²、2–10 keV | B⁺ / As⁺, 10¹³–10¹⁴ cm⁻², 2–10 keV |
| **技術要点 / Key Points** | 低エネルギー制御でナノシート損傷を抑制 | Use low energy to minimize nanosheet damage |

---

## 🔸 Step 12：内側スペーサリセス / Inner Spacer Etch Back

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | S/Dエピ領域を露出させるためのスペーサ除去 | Etch back inner spacer to expose S/D epi regions |
| **条件 / Conditions** | RIEエッチ + CMP調整 | RIE etch + optional CMP tuning |
| **技術要点 / Key Points** | 精密なリセス制御と支持構造保持が必要 | Requires precise recess control and support retention |

---

## 🔸 Step 13：S/Dエピタキシャル成長 / Raised Source/Drain Epitaxy

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | ソース／ドレインの隆起構造による低抵抗化 | Grow raised S/D regions for reduced resistance |
| **条件 / Conditions** | Selective Si/SiGe Epi, 高さ 20–30 nm | Selective Si/SiGe Epi, height 20–30 nm |
| **技術要点 / Key Points** | 結晶欠陥・ファセット形成の抑制が鍵 | Suppress crystal defects and facet formation |

---

## 🔸 Step 14：ダミーゲート除去 / Dummy Gate Removal

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | Polyゲート除去によるHigh-kゲートの準備 | Remove dummy gate to prepare for High-k/Metal gate |
| **条件 / Conditions** | TMAH等の選択エッチング | Selective etch using TMAH or similar |
| **技術要点 / Key Points** | ナノシート損傷を防ぐ穏やかな除去プロセス | Gentle etch to avoid nanosheet damage |

---

## 🔸 Step 15：High-k/Metalゲート形成 / High-k / Metal Gate Stack Deposition

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | ゲート全周を包囲する高誘電体＋メタル形成 | Form fully surrounding High-k dielectric and metal gate |
| **条件 / Conditions** | ALDによるHfO₂、TiN/TiAlN等 | HfO₂ via ALD, TiN/TiAlN stack |
| **技術要点 / Key Points** | 全面包囲性としきい値制御の両立 | Achieve full gate wrap and threshold tuning |

---

## 🔸 Step 16：S/D本注入 / S/D Implantation

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | ソース・ドレイン領域の本注入による低抵抗化 | Main implant to reduce S/D resistance |
| **条件 / Conditions** | B⁺ / As⁺、~10¹⁵ cm⁻²、30–80 keV | B⁺ / As⁺, ~10¹⁵ cm⁻², 30–80 keV |
| **技術要点 / Key Points** | 拡散抑制とアングル注入による損傷防止 | Use angled implantation and diffusion suppression |

---

## 🔸 Step 17：活性化アニール / Dopant Activation Anneal

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 注入不純物の活性化と結晶修復 | Activate dopants and repair crystal defects |
| **条件 / Conditions** | Spike RTA ~1050°C, 数秒 | Spike RTA at ~1050°C, several seconds |
| **技術要点 / Key Points** | 活性化とチャネル保持のトレードオフ | Balance between activation and channel preservation |

---

## 🔸 Step 18：シリサイド形成 / Silicide Formation

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | S/Dとゲートに低抵抗シリサイドを形成 | Form low-resistance silicide on S/D and gate |
| **条件 / Conditions** | Ni/Coスパッタ＋アニール | Ni or Co sputtering + annealing |
| **技術要点 / Key Points** | 過剰拡散やナノシート損傷の回避 | Prevent over-diffusion and nanosheet damage |

---

## 🔸 Step 19：層間絶縁膜形成 / ILD Deposition

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 配線層との絶縁形成 | Electrically isolate from interconnect layers |
| **条件 / Conditions** | SiO₂またはSiCOH膜、PECVD、~400 nm | SiO₂ or SiCOH by PECVD, ~400 nm thick |
| **技術要点 / Key Points** | ストレスと充填性のバランス | Balance stress and fill capability |

---

## 🔸 Step 20：CMP平坦化 / ILD CMP

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | ILD表面の平坦化処理 | Planarize the ILD surface |
| **条件 / Conditions** | CMPスラリー + SiNストップ層 | CMP slurry with SiN stop layer |
| **技術要点 / Key Points** | 過研磨と欠陥抑制 | Avoid over-polishing and defects |

---

## 🔸 Step 21：コンタクトホールリソグラフィ / Contact Hole Lithography

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | S/D・ゲートとの接続孔を定義 | Define vias for connection to S/D and gate |
| **条件 / Conditions** | ArFまたはEUV露光、CD ~30–50 nm | ArF or EUV lithography, CD ~30–50 nm |
| **技術要点 / Key Points** | 選択性とCD精度の高いプロセスが必要 | Requires high selectivity and CD precision |

---

## 🔸 Step 22：コンタクトエッチ / Contact Etch

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 定義されたコンタクトホールをエッチングしS/Dやゲートを露出 | Etch defined contact holes to expose S/D or gate |
| **条件 / Conditions** | フルオロカーボン系RIE、エッチストップ層活用 | Fluorocarbon-based RIE with etch-stop layer |
| **技術要点 / Key Points** | オーバーエッチによるリーク経路生成を回避 | Avoid leakage path formation due to over-etching |

---

## 🔸 Step 23：バリア・シード層形成（コンタクト）  
**Barrier and Seed Deposition (Contact)**

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | コンフォーマルなバリア/シード層を形成し銅埋込に備える | Form conformal barrier/seed layers for Cu plating |
| **条件 / Conditions** | TiN/TaN（ALD）＋ Cuシード（PVD）、膜厚 ~5–50 nm | TiN/TaN by ALD + Cu seed via PVD, thickness ~5–50 nm |
| **技術要点 / Key Points** | 高アスペクト比での被覆性と界面密着が重要 | Crucial for high aspect-ratio step coverage and adhesion |

---

## 🔸 Step 24：銅電解メッキ（ECP） / Copper Electrochemical Plating

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | コンタクトホール内を銅でボイドなく充填 | Void-free fill of contact holes with copper |
| **条件 / Conditions** | 酸性Cu硫酸浴、電流密度制御、オーバーフィル ~200–400 nm | Acidic Cu sulfate bath, controlled current density, overfill ~200–400 nm |
| **技術要点 / Key Points** | 添加剤（レベラー、サプレッサー）の選定が充填品質を左右 | Additive tuning (leveler/suppressor) critical for void control |

---

## 🔸 Step 25：CMP（コンタクト銅） / CMP of Contact Copper

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 銅オーバーフィルの除去とILDの平坦化 | Remove Cu overfill and planarize ILD |
| **条件 / Conditions** | Cu用CMPスラリー、エンドポイント制御 | Cu-selective CMP slurry, endpoint control |
| **技術要点 / Key Points** | 過研磨によるILD凹みやCu残膜を防止 | Prevent ILD erosion and residual Cu after polishing |

---

## 🔸 Step 26：ILD堆積（配線層直前） / ILD Deposition over Contact

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 第1層配線（M1）に向けた絶縁膜の形成 | Form interlayer dielectric above contacts before M1 |
| **条件 / Conditions** | SiCOHやSiOCなどの低k膜、PECVD、~300–500 nm | Low-k film (e.g., SiCOH), PECVD, thickness ~300–500 nm |
| **技術要点 / Key Points** | 低寄生容量と良好なキャッピング特性が求められる | Requires low parasitic capacitance and good capping properties |

---

## 🔸 Step 27：M1リソグラフィ・エッチ / M1 Lithography and Etch

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 第1層メタル配線の形状定義 | Define metal-1 wiring patterns |
| **条件 / Conditions** | ArFまたはEUV露光、CD ~20–30 nm、RIE加工 | ArF/EUV lithography, CD ~20–30 nm, RIE |
| **技術要点 / Key Points** | 微細ラインの形状保持とCD制御が重要 | Critical for line profile integrity and CD control |

---

## 🔸 Step 28：M1バリア／シード形成 / Barrier and Seed Deposition for M1

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | Cu電解めっきに先立つバリアとCuシード層形成 | Prepare for Cu ECP by depositing barrier and seed layers |
| **条件 / Conditions** | Ta/TaN（ALD）、Cuシード（PVD）、バリア5–10 nm、シード ~50 nm | Ta/TaN (ALD), Cu seed (PVD), barrier 5–10 nm, seed ~50 nm |
| **技術要点 / Key Points** | トレンチ／ビア内部への均一堆積が不可欠 | Uniform deposition into trenches and vias is essential |

---

## 🔸 Step 29：銅ECP（M1） / Copper ECP for M1

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | ビア・トレンチ内を銅で埋める | Fill vias/trenches with copper |
| **条件 / Conditions** | 酸性Cu浴、添加剤制御、オーバーフィル | Acidic Cu bath, additive control, overfill |
| **技術要点 / Key Points** | ボイドフリーと後工程CMPへの整合が必要 | Void-free fill and CMP compatibility are critical |

---

## 🔸 Step 30：CMP（M1銅） / CMP of M1 Copper

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 銅のオーバーフィル除去と平坦化 | Remove Cu overfill and planarize the surface |
| **条件 / Conditions** | CMPスラリー、Cu選択性高、エンドポイント制御 | CMP slurry with Cu selectivity, endpoint detection |
| **技術要点 / Key Points** | 面内均一性とディッシュ/エロージョン抑制 | Intra-wafer uniformity, suppression of dishing/erosion |

---

## 🔸 Step 31：層間絶縁膜堆積（M1–M2）  
**ILD Deposition Between M1 and M2**

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | M1とM2間の絶縁層形成（低k） | Form low-k ILD between M1 and M2 |
| **条件 / Conditions** | PECVDによりSiCOH系低k膜、厚さ ~400 nm | SiCOH low-k film by PECVD, ~400 nm |
| **技術要点 / Key Points** | RC遅延低減のためのk値最適化 | Optimize dielectric constant to reduce RC delay |

---

## 🔸 Step 32：上位メタルリソ・エッチ（M2〜Mx）  
**Higher Metal Lithography and Etch (M2–Mx)**

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | M2〜最上層メタルのビア／ラインパターン定義 | Define vias/lines for M2 to top metal layers |
| **条件 / Conditions** | EUV/ArF露光、RIEエッチ、CD ~20–30 nm | EUV/ArF lithography, RIE etch, CD ~20–30 nm |
| **技術要点 / Key Points** | 多層配線でのアライメント誤差最小化 | Minimize alignment error across multiple layers |

---

## 🔸 Step 33：バリア・シード／銅ECP（M2〜Mx）  
**Barrier, Seed & Cu Plating for M2–Mx**

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 各配線層の銅埋込準備と充填 | Prepare and fill each metal layer with Cu |
| **条件 / Conditions** | TaNバリア（ALD）、Cuシード（PVD）、ECP | TaN (ALD), Cu seed (PVD), electroplating |
| **技術要点 / Key Points** | 多層積層による残留応力とボイド制御 | Stress and void control in multilayer stacks |

---

## 🔸 Step 34：上位配線CMP / CMP of Higher Metal Layers

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 各メタル層の表面平坦化と構造確立 | Planarize and define each upper metal layer |
| **条件 / Conditions** | CMPスラリー、ターゲットエンドポイント制御 | CMP slurry with endpoint monitoring |
| **技術要点 / Key Points** | RC特性・リソ精度維持のためのCMPプロセス最適化 | Optimize CMP to maintain RC integrity and litho accuracy |

---

## 🔸 Step 35：キャップ層堆積 / Cap Layer Deposition

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | Cu配線の酸化・拡散防止 | Prevent oxidation and diffusion of Cu |
| **条件 / Conditions** | SiN/SiCN、PECVD、20–50 nm | SiN/SiCN by PECVD, 20–50 nm thick |
| **技術要点 / Key Points** | バリア性能と機械応力の両立 | Balance between barrier and stress characteristics |

---

## 🔸 Step 36：パッシベーション層形成 / Passivation Layer Deposition

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 外部環境からの保護層形成 | Protect device from external contamination |
| **条件 / Conditions** | SiN or SiO₂、PECVD、0.5–1.0 µm | SiN/SiO₂ by PECVD, 0.5–1.0 µm thick |
| **技術要点 / Key Points** | クラック防止と密着性確保 | Crack prevention and adhesion reliability |

---

## 🔸 Step 37：パッド開口 / Pad Opening Lithography & Etch

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | UBMメタル接続部の開口形成 | Form openings to access UBM pads |
| **条件 / Conditions** | ArF露光、RIEでパッシベーション開口 | ArF lithography + RIE |
| **技術要点 / Key Points** | Cuダメージ最小化 | Minimize Cu damage during etch |

---

## 🔸 Step 38：UBM形成 / Under Bump Metallization (UBM)

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | バンプ形成のための多層金属形成 | Form multilayer metals for bump attachment |
| **条件 / Conditions** | NiV/Cu/Au等、PVD＋電解メッキ、~10 µm | NiV/Cu/Au via PVD + electroplating, ~10 µm |
| **技術要点 / Key Points** | はんだ濡れ性・密着性の最適化 | Optimize solder wettability and adhesion |

---

## 🔸 Step 39：ウエハ薄化 / Wafer Thinning

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | チップの薄型化・3D実装対応 | Enable thin package and 3D integration |
| **条件 / Conditions** | バックグラインド + CMP、厚さ ~100 µm以下 | Back grinding + CMP to ~100 µm or less |
| **技術要点 / Key Points** | チップ割れ・歪み防止 | Prevent cracking and warping |

---

## 🔸 Step 40：TSV & マイクロバンプ形成 / TSV and Microbump Formation

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 3D IC接続のための垂直配線形成 | Create vertical interconnects for 3D IC |
| **条件 / Conditions** | DRIE + Cu埋込、SnAgバンプ形成 | DRIE, Cu fill, SnAg bump plating |
| **技術要点 / Key Points** | TSV内のボイド・亀裂防止 | Prevent voids and cracks in TSVs |

---

## 🔸 Step 41：最終パッシベーション / Final Passivation

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | パッケージ信頼性の最終保護 | Final environmental protection |
| **条件 / Conditions** | SiN/SiO₂、PECVD、~1.0 µm | SiN/SiO₂ by PECVD, ~1.0 µm thick |
| **技術要点 / Key Points** | 応力緩和とチップ保護の両立 | Balance between stress relief and protection |

---

## 🔸 Step 42：ウエハテスト（最終）/ Final Wafer Test

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | チップ電気特性の最終検査 | Final electrical test of chips |
| **条件 / Conditions** | ATE、Iₗₑₐₖ, Vₜₕ, 遅延など評価 | ATE, leakage, threshold, delay test |
| **技術要点 / Key Points** | GAA構造のばらつき把握が重要 | Must monitor Vt variation due to GAA |

---

## 🔸 Step 43：ダイシング / Wafer Dicing

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 個別チップへ分割 | Separate dies for packaging |
| **条件 / Conditions** | レーザーまたはソーイング | Laser scribing or mechanical saw |
| **技術要点 / Key Points** | ウエハ破損・バリ最小化 | Minimize cracks and chipping |

---

## 🔸 Step 44：ダイアタッチ / Die Attach

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | チップをパッケージ基板へ実装 | Attach chip to substrate |
| **条件 / Conditions** | 接着剤、熱圧着など | Adhesive or thermal compression |
| **技術要点 / Key Points** | 熱伝導と平坦性の確保 | Ensure good thermal path and flatness |

---

## 🔸 Step 45：フリップチップ or ワイヤボンディング  
**Flip-Chip Bonding or Wire Bonding**

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 基板とチップを電気的に接続 | Electrically connect chip and substrate |
| **条件 / Conditions** | SnAgリフロー or Au/Cuワイヤ | SnAg reflow or Au/Cu wire |
| **技術要点 / Key Points** | 接合信頼性と熱歪み制御 | Joint reliability and stress control |

---

## 🔸 Step 46：アンダーフィル / Underfill Application

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 接合部の機械的保護 | Protect joints against mechanical stress |
| **条件 / Conditions** | エポキシ系材料、加熱硬化 | Epoxy material, thermal cure |
| **技術要点 / Key Points** | ボイドレス充填、C.T.E整合 | Void-free fill, CTE matching |

---

## 🔸 Step 47：最終試験とマーキング / Final Test and Marking

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 最終品質検査と製品マーキング | Final quality check and device marking |
| **条件 / Conditions** | 自動試験機（ATE）、レーザー印字 | ATE testing and laser marking |
| **技術要点 / Key Points** | トレーサビリティと統計管理 | Maintain traceability and statistical control |

---

## 🔸 Step 48：パッケージング / Final Packaging

| 項目 | 日本語 / Japanese | 英語 / English |
|------|------------------|----------------|
| **目的 / Purpose** | 顧客向け最終パッケージ封止 | Final sealing and delivery-ready package |
| **条件 / Conditions** | WLP / FC-CSP / FOWLP / SiPなど | WLP, FC-CSP, FOWLP, SiP, etc. |
| **技術要点 / Key Points** | 熱設計・歩留まり・コストの最適化 | Balance between thermal design, yield, and cost |

---

