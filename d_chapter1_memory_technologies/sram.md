# 🧠 SRAM（Static Random Access Memory）

---

## 📘 概要

SRAM（Static RAM）は、**高速で揮発性のメモリ**として、SoC内部に組み込まれる主要なメモリ構成です。  
DRAMのようにリフレッシュを必要とせず、6T構成セルで安定した保持が可能です。

主な用途には、**キャッシュメモリ、レジスタファイル、ルックアップテーブル（LUT）**などがあり、論理プロセス内に直接レイアウト可能な「**組込みメモリ（embedded memory）**」として広く使われています。

---

## 🔧 セル構造：6T SRAMセル

### 📐 構成図（初心者向け）

```
               VDD
                |
              +---+
              | P1|───┐
              +---+   |
                |     |
                |    Q (保存ノード)
                |     |
  BL───AX1──────┘     └──────AX2───BL_bar
       |                        |
      WL -----------------------
                |     |
              +---+  +---+
              | N1|  | N2|     ← インバータの下側
              +---+  +---+
                |     |
               GND   GND
```

### 🔍 各部の説明

| 名称 | 役割 |
|------|------|
| P1/N1、P2/N2 | 2つのインバータを交差接続し、**ラッチ回路**を構成（QとQ_barに反転値が保持） |
| AX1 / AX2（アクセスFET） | **スイッチ**：WLがHighになるとONになり、ビット線BL/BL_barとQ/Q_barが接続される |
| Q / Q_bar | 1ビットのデータ保持ノード（Q: データ, Q_bar: 反転） |
| WL（Word Line） | セルの選択線。Highにすると読み書きが有効になる |
| BL / BL_bar（Bit Line） | 読み書きのデータ線。差動で信号伝達（信頼性向上） |

---

## 📊 特性と設計観点

| 項目 | 内容 |
|------|------|
| 保持性 | 電源ON中はデータ保持（リフレッシュ不要） |
| 面積 | DRAMより大きい（6T構成＋アイソレーション） |
| 消費電力 | 書き込み時は比較的大きい、待機時は低消費 |
| レイアウト | シンメトリ、対称性重視（ばらつき対策） |
| スピード | 非常に高速（キャッシュレベル） |
| 安定性 | **SNM（Static Noise Margin）**設計が重要（読み出し破壊や書き込み失敗対策） |

---

## 🏭 組込みメモリとしての使い方

- SRAMマクロをPDKベースで呼び出し（例：sky130 → `sky130_sram_1kbyte_1rw1r_8x8`）
- OpenLaneなどで `black-box` の形で接続
- キャッシュ構成やアーキテクチャに応じて**階層的に配置**

---

## 🔁 他メモリとの比較（簡易）

| メモリ種別 | 高速性 | 容量 | 面積効率 | 不揮発性 | 組込み性 |
|------------|--------|------|----------|----------|-----------|
| SRAM       | ◎      | △    | △        | ×        | ◎         |
| DRAM       | ○      | ◎    | ◎        | ×        | △（外部） |
| Flash      | ×      | ◎    | ○        | ◎        | △         |

---

## 📚 補足情報・関連知識

- **6T以外の構成**：8T, 10T, Dual-Port SRAM なども存在（用途・性能に応じて選択）
- **ノード面積**：数μm² → 先端では0.04μm²以下に縮小（FinFET/GAAでは微細化が難題に）
- **設計課題**：読み出し破壊（read disturb）、書き込み失敗、SNMなど
- **先端設計**ではレイアウトばらつき・低電圧時の動作保証が鍵

---

## 🔗 関連章（教材リンク）

- [基礎編 第2章](../chapter2_comb_logic/)：レジスタや記憶素子の論理構造  
- [基礎編 第4章](../chapter4_mos_characteristics/)：トランジスタ特性とばらつき  
- [応用編 第4章](../d_chapter4_layout_optimization/)：SRAMマクロ配置とDFM対応  

---

## 📦 技術アーカイブ参照（Edusemi-Plusリポジトリ）  
*Technical archive references from Edusemi-Plus repository*

以下の資料は、半導体メモリ技術の現場記録として教材を補完するものです。  
These documents complement this curriculum with real-world memory development records.

---

### 📘 DRAM立ち上げ記録（1998年）  
- 📄 [`DRAM_Startup_64M_1998.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in1998/DRAM_Startup_64M_1998.md)  
　→ 0.25μm世代の64M DRAMプロセス立ち上げ経験記録  
　→ Record of 0.25μm 64M DRAM ramp-up and yield improvement

### 📘 モバイル用VSRAM技術（2001年）  
- 📄 [`VSRAM_2001.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/VSRAM_2001.md)  
　→ DRAMプロセスを利用した擬似SRAMの開発と課題対応  
　→ Development and issue resolution of pseudo-SRAM using DRAM process

### 📘 Mosys 1T-SRAM技術参考リンク  
- 📄 [`MoSys_1T_SRAM_Links.md`](https://github.com/Samizo-AITL/Edusemi-Plus/blob/main/archive/in2001/MoSys_1T_SRAM_Links.md)  
　→ SRAM代替技術として検討されたMosys社 1T-SRAM の外部リンク集  
　→ External reference links on MoSys 1T-SRAM as alternative SRAM macro

---

© 2025 Shinichi Samizo / MIT License
