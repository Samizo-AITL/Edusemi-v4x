# 補足資料：FinFET 製造プロセスフロー（全48ステップ）

本資料は、FinFET（Fin Field-Effect Transistor）の製造における主要工程を48ステップに分解し、各ステップの目的・プロセス条件・技術的ポイントを詳細に記述したものである。

---

## 🔹 前提情報

- **対象プロセスノード**：10〜5nm世代のFinFET
- **基板仕様**：300 mm P型 Si（100）、抵抗率：10 Ω·cm前後
- **目的**：プレーナMOSFETを超える短チャネル制御とゲート制御性の実現

---

## 🔸 プロセスフロー一覧（概要）

| ステップ範囲 | 工程群                     |
|--------------|----------------------------|
| Step 1–3     | 基板処理、ウェル形成       |
| Step 4–6     | ゲート酸化膜・ポリシリコン形成・パターニング |
| Step 7–9     | ソース/ドレイン形成（拡散層含む） |
| Step 10–15   | 金属コンタクト形成         |
| Step 16–26   | 配線層（M1〜Mx）形成       |
| Step 27–34   | 配線層仕上げ・ビア形成     |
| Step 35–40   | 上層メタル〜キャップ層     |
| Step 41–48   | RC抽出・パッド・テスト・パッケージング |

---

## 🔸 各ステップの詳細

以下に、各ステップごとの目的・条件・装置・注意点を順に記述する：

---

### Step 1: Substrate Preparation

- **目的**：300mm Siウェハの初期表面調整、異物・水分除去
- **代表条件**：
  - RCA洗浄 → 150°C・10分デハイドレーションベイク
  - TTV < 1 µm、Bow < 40 µm（CMP後の参照面基準）
- **注意点**：後続のSTI/ゲート形成の高さ精度に影響

---

### Step 2: Shallow Trench Isolation (STI) Formation

- **目的**：アクティブ領域の電気的分離
- **工程**：
  - 193 nm ArF液浸リソグラフィ
  - RIE（フッ素系）で200 nm深トレンチ形成
  - TEOS酸化膜埋込 → CMPで平坦化

---

### Step 3: Well and Channel Implantation

- **目的**：しきい値電圧調整のためのn/pウェル形成
- **条件例**：
  - B（p-well）、As/P（n-well）、10¹²–10¹³ cm⁻²、30–80 keV
  - RTA（1000°C）で活性化

---

（以下、Step 4 〜 Step 48 も同様に展開）

---

## 🔸 補足図（図示予定）

- `images/finfet_structure.png`：FinFET断面構造
- `images/finfet_process_flowchart.png`：簡略プロセスフローチャート
- `images/finfet_gate_region_detail.png`：ゲート・S/D近傍の断面構造

---

## 🔸 備考

- 本補足資料は、特別編 第1章「先端ノード（FinFET、GAA等）」の理解を補完するための技術解説です。
- 対応するGAA版プロセスフローは [`appendixf1_02_gaaflow.md`](./appendixf1_02_gaaflow.md) を参照してください。

---

## ライセンスと著者

MITライセンスにて公開。  
著者：三溝 真一（Shinichi Samizo）  
連絡先：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)
