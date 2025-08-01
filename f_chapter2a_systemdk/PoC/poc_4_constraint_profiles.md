# 📏 poc_4_constraint_profiles.md  
**物理制約プロファイルの定義（SI/PI・熱・応力・EMI/EMC）**  
**Definition of Physical Constraint Profiles (SI/PI, Thermal, Stress, EMI/EMC)**

---

## 📘 概要｜Overview

本節では、SystemDKにおける主要な物理制約カテゴリ（SI/PI、熱、応力、EMI/EMC）に関して、  
設計上の考慮点・制約モデル・評価指標を整理します。

This section outlines the key physical constraint categories in SystemDK—**Signal/Power Integrity (SI/PI)**,  
**Thermal**, **Mechanical Stress**, and **EMI/EMC**—along with their design considerations and evaluation models.

---

## 🔌 SI/PI：Signal & Power Integrity

### 📐 設計項目｜Design Items
- Transmission line matching / impedance
- Power Delivery Network (PDN) hierarchy
- Decoupling capacitor layout

### 📊 評価手法｜Evaluation Methods
- Sパラメータ解析（TDR, VNA）
- PDNインピーダンス解析
- IBIS/SPIモデルによる波形検証

### 📌 SystemDKでの実装例｜SystemDK Implementation
```
- 各ブロックのI/F仕様からインピーダンス要求を定義
- PKG層でPDNテンプレートを適用
- Lチップ⇔Hチップでのクロストーク分離解析
```

---

## 🌡️ Thermal（熱）

### 📐 設計項目｜Design Items
- Power map / 熱密度分布
- ヒートスプレッダ/ヒートシンク構造
- Hotspot回避配置（floorplan）

### 📊 評価手法｜Evaluation Methods
- FEMによる熱拡散解析（steady/transient）
- Junction温度シミュレーション（Tj）
- Rth測定（熱抵抗モデル）

### 📌 SystemDKでの実装例
```
- 各ダイのPmapをfloorplanにマッピング
- 樹脂/配線層の材料スタックを熱モデルに変換
- 熱境界条件（固定温度/自然放熱）指定
```

---

## 🧱 Mechanical Stress（応力）

### 📐 設計項目｜Design Items
- 材料のCTE差（熱膨張係数）
- TSV / RDL配置によるストレス集中
- チップ・パッケージ界面剥離リスク

### 📊 評価手法｜Evaluation Methods
- FEMによる応力場解析（Von Mises, Creep）
- 変位・ひずみ量評価（Displacement/Strain）
- 寿命モデル（疲労/剥離）

### 📌 SystemDKでの実装例
```
- 材料DBにCTE/E-modulusを登録
- 層構造テンプレートから応力マップ生成
- GAAとMRAM間の界面応力を計算
```

---

## 📡 EMI / EMC（電磁妨害）

### 📐 設計項目｜Design Items
- クロック/高速信号の放射・ノイズ源
- シールド・GND設計
- RF-AMSブロックとの距離設計

### 📊 評価手法｜Evaluation Methods
- EM Field Solver（3D FEM / FDTD）
- Sパラ/RFノイズ解析
- EMCテストモデル（CISPR/Bode plot）

### 📌 SystemDKでの実装例
```
- RFブロック周辺にGNDシールド配置
- EMIホットスポット抽出しシールド再配置
- BCD-AMS用のEMノイズプロファイル共有
```

---

## 🎯 教育的ポイント｜Educational Highlights

- SI/PI・熱・応力・EMCの**分類・設計・評価**を体系的に整理
- FEMやSパラ等の**評価手法と設計への反映方法**を学習
- 制約プロファイルを**形式知としてモデル化し共有する意義**を実感

---

## 🔗 関連リンク｜Related Links

- [poc_3_block_spec.md](./poc_3_block_spec.md)
- [poc_5_integration.md](./poc_5_integration.md)
- [f2a_2_sipi.md](../../f_chapter2a_systemdk/f2a_2_sipi.md)
- [f2a_3_thermal.md](../../f_chapter2a_systemdk/f2a_3_thermal.md)
- [f2a_4_stress.md](../../f_chapter2a_systemdk/f2a_4_stress.md)
- [f2a_5_emi.md](../../f_chapter2a_systemdk/f2a_5_emi.md)
