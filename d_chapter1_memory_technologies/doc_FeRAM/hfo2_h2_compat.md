# ✅ HfZrO₂系強誘電体の水素工程適合性  
# ✅ Hydrogen Compatibility of HfZrO₂-based Ferroelectrics

---

## 1. 背景 / Background

従来の強誘電体FeRAM（特にPZT系）は、CMOSプロセス後工程で使用される水素アニール処理により、特性劣化（インプリント、疲労、分極低下）を引き起こすことが知られている。  
Traditional ferroelectric FeRAMs, especially PZT-based ones, are known to suffer from degradation such as imprint, fatigue, and polarization loss when exposed to hydrogen annealing during backend CMOS processing.

---

## 2. PZTにおける課題と対策 / Issues with PZT and Mitigations

- **劣化要因 / Degradation Factors**
  - 酸素空孔生成とドメインピンニング  
    Formation of oxygen vacancies and domain pinning  
  - 還元反応によるTi⁴⁺ → Ti³⁺変化  
    Reductive conversion of Ti⁴⁺ to Ti³⁺

- **対策例 / Known Mitigations**
  - AlOxバリア（スパッタ＋ALD）  
    AlOx dual-layer barrier (sputtering + ALD)
  - 水素シンター除外（工程制限）  
    Exclusion of hydrogen sintering from the process

---

## 3. HfZrO₂の水素耐性 / Hydrogen Resistance of HfZrO₂

| 特性 / Property        | 内容 / Description |
|------------------------|---------------------|
| 結晶安定性             | orthorhombic相が水素下でも保持されやすい  
                          Orthorhombic phase remains stable under H₂ |
| 成膜技術               | ALD等により緻密かつ低欠陥な膜形成が可能  
                          Dense, low-defect films via ALD |
| キャップ層             | TiNなどで水素バリア効果を確保可能  
                          Hydrogen barrier enabled by TiN |
| 実証事例               | CMOS混載FeFETで420 °C H₂アニール動作実績あり  
                          Validated operation under 420 °C H₂ anneal |

HfZrO₂ exhibits robust hydrogen resistance due to its stable orthorhombic phase and compatibility with standard CMOS backend processes, including hydrogen sintering at 420 °C.

---

## 4. 実用工程例 / Practical Process Integration

```
BEOL工程例 / Example BEOL Flow:
  1. HfZrO₂薄膜形成（ALD） / ALD deposition of HfZrO₂
  2. TiNキャップ堆積 / TiN cap deposition
  3. ポストアニール（RTA） / Post-deposition annealing (RTA)
  4. 標準水素シンター（420 °C, H₂/N₂） / Standard H₂ sintering (420 °C)
```

実用プロセス内で特別な保護膜や制限工程を必要とせず、量産適合性に優れる。  
No special barrier or process deviation is required, enabling manufacturable CMOS integration.

---

## 5. 比較表 / Comparison Table

| 項目 / Item             | PZT                    | HfZrO₂                      |
|--------------------------|-------------------------|-----------------------------|
| 水素還元耐性 / H₂ Tolerance | ×（劣化あり / Degrades） | ◎（高耐性 / Highly tolerant） |
| CMOS整合性 / CMOS Compatibility | △（高温＋Pb問題 / High temp, Pb） | ◎（低温・ALD適合 / Low-temp, ALD-compatible） |
| 工程制約 / Process Constraint | 要バリア＆アニール制限 / Needs barrier, avoid anneal | 不要 / None required |

---

## 6. 最新トレンド：FeRAM vs FeFET / Latest Trend: FeRAM vs FeFET

| 項目 / Item           | FeRAM（1T1C）                           | FeFET（1T）                                   |
|------------------------|------------------------------------------|-----------------------------------------------|
| 構造 / Structure       | 1T1C（FET + 強誘電キャパシタ）          | 1T（FET単体、キャパシタレス）                  |
| 記録原理 / Principle   | 分極によるキャパシタ電荷記憶             | 分極によるFETのしきい値（Vth）シフト           |
| 読み出し方式 / Readout | **破壊読み出し**（リフレッシュ必要）     | **非破壊読み出し**（通常のFET読み出し）        |
| 面積効率 / Density     | 中程度（キャパシタ分必要）               | 高（SRAM並、1T構成）                          |
| CMOS整合性 / CMOS Compatibility | 高（特にHfZrO₂使用時）          | **非常に高い**（HfZrO₂ゲート絶縁膜として使用）   |
| 主な用途 / Applications | 組込みNVM、RTC、MCUなど                 | AI推論、キャッシュ、SoC NVM、インメモリ計算等   |
| 実用化状況 / Status    | 富士通、Lapisなどで組込み量産実績あり    | GLOBALFOUNDRIES, imec などが開発中（初期量産） |

FeFET is emerging as a next-generation ferroelectric memory with better scalability, simpler structure, and superior CMOS compatibility compared to conventional FeRAM.

---

## 7. 関連資料 / References

- Fraunhofer IPMS, FeFET Technology Reports (2021–2024)
- imec, IEDM Proceedings (2022)
- GLOBALFOUNDRIES, eMRAM/eFeRAM Datasheets
- T. Mikolajick et al., "The FeFET—A Promising Non-Volatile Memory," IEEE TED (2020)
- L. Grigoriev et al., "HfO₂-Based Ferroelectric FETs for Scalable NVM," IEDM (2022)
