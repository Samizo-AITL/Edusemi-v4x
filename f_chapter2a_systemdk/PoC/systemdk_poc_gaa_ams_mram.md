# 🧪 GAA・AMS・MRAMを含むチップレット統合PoC  
**PoC: Heterogeneous Chiplet Integration with GAA, AMS, and MRAM**

---

## 📘 概要｜Overview

本教材では、最先端・異種ノードを組み合わせた**SystemDKベースのPoC事例**として、  
GAA（Gate-All-Around）、AMS（アナログ・ミックスドシグナル）、MRAM（不揮発メモリ）を  
**チップレット構成で統合する設計評価モデル**を提示します。

This case study presents a SystemDK-based **Proof of Concept** for heterogeneous chiplet integration.  
It focuses on combining GAA, AMS, and MRAM nodes into a single System-in-Package using modern physical design constraints.

---

## 🧩 構成ブロック例｜Chiplet Block Configuration

| ブロック | 技術 / Technology | ノード | 役割 / Role |
|----------|--------------------|--------|-------------|
| 高速CPU | GAA (nanosheet FET) | 2nm | 高性能演算・制御 |
| アナログIF | AMS / BCD | 22nm | センサ信号変換・ADC・PMU |
| メモリ | MRAM | 28nm | 状態保持・キャッシュ |

---

## 🔧 評価項目と設計視点｜Evaluated Constraints & Design Scope

### 1. SI/PI：信号／電源整合  
- クロスダイ接続のSパラメータ解析  
- PDN階層構成・デカップリング設計  
- インピーダンス解析と波形整合

### 2. Thermal：熱評価  
- GAA高密度部の熱拡散  
- MRAM保護の冷却戦略（レイヤー配置）  
- 熱FEMマップを用いたシミュレーション

### 3. Mechanical：応力・信頼性  
- RDL間のCTE差による応力集中領域の可視化  
- 封止材と界面処理の信頼性設計

### 4. EMI/EMC：ノイズ干渉  
- AMS/デジタル間のクロストーク評価  
- グラウンディングと遮蔽レイアウトの最適化

---

## 📈 評価ツール・解析手法｜Evaluation Tools & Methods

| 種別 | 使用手法 |
|------|----------|
| SI/PI | Sパラメータ、IBIS、インピーダンスプローブ |
| 熱解析 | 熱FEM（有限要素法）／熱伝導シミュレーション |
| 応力 | 機械FEM、材料CTE評価 |
| EMI/EMC | 近傍界スキャナ、レイアウト解析、伝導放射評価 |

---

## 📂 この教材に含まれるファイル｜Included Files

| ファイル名 | 内容 |
|------------|------|
| `systemdk_poc_gaa_ams_mram.md` | 本体ドキュメント |
| `images/block_diagram.png` | ブロック構成図（GAA/AMS/MRAM） |
| `images/pdn_map.png` | PDN・デカップ構成例 |
| `data/sparam_example.csv` | Sパラ例データ |
| `data/thermal_map.json` | 熱分布例FEM出力 |

---

## 🎯 教育的意義｜Educational Impact

- SystemDKの応用範囲（物理制約統合設計）を体感的に理解できる  
- ノードごとの特性を活かした設計構想力・統合力の養成  
- チップレット設計における「物理的に動く判断」の実践訓練  
- AI時代のSoC教育におけるPoC的アプローチの先例

---

## 🔗 関連リンク｜Related Materials

- [SystemDK全体構成](../README.md)  
- [PoCフォルダトップ](./README.md)  
- [評価手法一覧（f2a_9_evaluation_methods.md）](../f2a_9_evaluation_methods.md)  
- [Edusemi-v4x トップへ](../../README.md)

---

## 👤 著者・ライセンス｜Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| 著者 / Author | 三溝 真一（Shinichi Samizo）<br>Shinshu University / Ex-Epson |
| GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |
| Email | shin3t72@gmail.com |
| ライセンス / License | MIT License（再配布・改変自由） |

---
