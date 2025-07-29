# FeRAM / 薄膜ピエゾ特性評価原理  
**FeRAM and Thin-Film Piezoelectric Characterization Principles**  
（教育資料・社外公開可）

---

## 1. FeRAMのヒステリシス特性評価  
**1. Hysteresis Characterization in FeRAM**

### ✅ 測定波形
- **三角波入力（Triangular wave input）**  
  → Pr, Pm, Vcなどの特性評価（標準的なヒステリシスループ）

- **PUND法（Positive-Up Negative-Down）**  
  → 実動作に近い矩形波で、スイッチング電流と非スイッチング電流を分離可能  
  → Pr抽出に有効

### ✅ 主なパラメータ（Key Parameters）
| 項目 | 意味 | 単位 |
|------|------|------|
| Pm | 最大分極（Maximum polarization） | μC/cm² |
| Pr | 残留分極（Remanent polarization） | μC/cm² |
| Vc | 保証電圧（Coercive voltage） | V |
| 2Pr | 記憶保持力の指標（Memory window） | μC/cm² |

---

## 2. 薄膜ピエゾ特性とバタフライカーブ  
**2. Thin-Film Piezoelectric Properties and Butterfly Curve**

### ✅ アクチュエータ用途の理想
- **高Pm → 高変位ストローク**  
- MEMSマイクロアクチュエータ、スピーカー、インクジェットなどで利用

### ✅ バタフライカーブ（Butterfly Curve）
- 横軸：印加電圧、縦軸：変位量（nmオーダー）
- 分極反転点で変位が非線形にジャンプ
- ヒステリシスを持つ蝶型ループを形成

---

## 3. 測定法：LDV / DBLI  
**3. Measurement Methods: LDV and DBLI**

### ✔ レーザードップラー変位計（LDV）
- MEMS振動板構造が必要（裏面研磨を伴う）
- nmスケール変位の測定に適す

### ✔ DBLI（Double Beam Laser Interferometer） by aixACCT（Germany）
- **裏面研磨不要**
- **非接触・高感度・フルウエハ対応**
- PZT薄膜の表面たわみをナノ精度で計測可能
- バタフライカーブや電界依存変位特性をそのまま抽出可能

```text
  Laser 1      Laser 2
     ↓            ↓
    ●────────────●   ← PZT薄膜表面（2点）
    ─────────────────
        Si基板（裏面加工不要）
```

---

## 4. 比較と使い分け  
**4. Comparison: FeRAM vs. Piezo Thin-Film Use Cases**

| 観点 | FeRAM用途 | ピエゾアクチュエータ用途 |
|------|-----------|----------------------------|
| 主目的 | 電気的記憶保持 | 機械的変位出力 |
| 評価波形 | 三角波 / PUND | 矩形波 / LDV / DBLI |
| 測定対象 | 分極電流 | 表面変位（nm） |
| 理想形状 | 縦長ヒステリシスループ | バタフライカーブ |

---

## 5. 補足・教育応用  
**5. Notes and Educational Use**

- DBLIやPUND法などの測定技術は、**材料開発段階からの迅速なスクリーニング**に有効  
- 特定の企業仕様や試験条件を含まず、**教育資料・社外共有資料として安全に活用可能**

---

© 2025 Samizo-AITL. For educational and non-confidential use.
