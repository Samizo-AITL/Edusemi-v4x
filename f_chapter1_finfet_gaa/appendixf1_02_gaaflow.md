# 補足資料：GAA Multi-Nanosheet FET 製造プロセスフロー（全48ステップ）

本資料では、先端ノードにおける GAA（Gate-All-Around）Multi-Nanosheet FET の製造プロセスを全48ステップで分解し、各工程の目的・プロセス条件・技術的な要点を体系的に記述します。

---

## 🔹 前提情報

- **対象構造**：GAA Multi-Nanosheet FET（5nm～2nm世代）
- **基板仕様**：300 mm Si（⟨100⟩）、p型、TTV < 1 µm、Bow < 40 µm
- **チャネル構成**：Si/SiGe積層（例：Si 5 nm / SiGe 8 nm ×3）
- **目的**：短チャネル制御を最大化するフルサラウンドゲート構造の実現

---

## 🔸 プロセスフロー分類（概要）

| 範囲       | 工程グループ                      |
|------------|-----------------------------------|
| Step 1–3   | 基板準備とSi/SiGeスーパーラティス形成 |
| Step 4–6   | ハードマスク形成とFinエッチング     |
| Step 7–12  | STI埋込・平坦化・ダミーゲート形成   |
| Step 13–18 | ダミーゲートパターニングとGAA形成   |
| Step 19–24 | メタルゲート構築・アニール・ストレス導入 |
| Step 25–34 | コンタクト形成と配線下地形成       |
| Step 35–40 | 配線層（M0, M1）形成とCMP           |
| Step 41–48 | パッド開口・UBM・テスト・パッケージ |

---

## 🔸 各ステップの詳細（抜粋例）

---

### Step 1: Substrate Preparation

- **目的**：高精度エピ成長に適した基板準備
- **仕様**：
  - 300 mm p型 Si（⟨100⟩）、TTV < 1 µm、粒子 < 0.12 µm（10以下）
  - Option：SiGeバッファ層（20–50 nm、Ge 20–30%）

---

### Step 2: Superlattice Epitaxial Growth

- **目的**：Si/SiGe交互積層によるナノシートチャネル構築
- **工程**：
  - RPCVD at 650–700°C（Ge memory < 0.1%）
  - 層構成例：Si 5 nm / SiGe 8 nm ×3

---

### Step 3: CMP (Epi Planarization)

- **目的**：上部SiGe層を露出し、高さ±2 nmで平坦化
- **条件**：
  - シリカ系スラリー、Si vs SiGeの除去率比考慮
  - Spectro-reflectometryでエンドポイント制御

---

（以下、Step 4〜48も同形式で展開予定）

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
