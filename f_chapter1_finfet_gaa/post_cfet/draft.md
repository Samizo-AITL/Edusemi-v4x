# Post-CFET デバイス・アーキテクチャ 論文草稿（改訂詳細版）

## 要旨（Abstract）
CMOS スケーリングは Planar MOSFET から FinFET、ゲート・オール・アラウンド（GAA）、そして Complementary FET（CFET）へと進化してきた。CFET は電気的制御性をさらに高め、短チャネル効果や配線ボトルネックを緩和するが、シリコン基盤の材料物性や熱拡散特性は限界に近づきつつある。本稿では、**Post-CFET デバイス候補**として、**二次元材料 FET、モノリシック 3D 集積、スピントロニクス／量子デバイス、異種原子スケール集積**を整理する。それぞれの物理原理、製造課題、定量的指標、応用分野、設計フローへの影響を比較し、教育的意義を含めた展望を与える。

---

## 1. 序論
半導体産業は 1970 年代以降、微細化と新構造導入により性能向上を続けてきた。  
- **Planar MOSFET → FinFET → GAA → CFET** は、デバイス構造による「電気的制御性向上」の道のりである。  
- **限界要因**：シリコンチャネルの移動度劣化、リーク電流増加、配線遅延支配、熱拡散制約。  

CFET によりトランジスタの「空間効率」は高まったが、**材料限界**や**配線・熱課題**を克服するには、新しい材料や三次元統合、あるいは論理＋記憶＋物理の融合が不可欠となる。  
この次の時代を「Post-CFET」と定義する。  

---

## 2. CMOS から Post-CFET への進化経路
- **Planar → FinFET**：3次元化で短チャネル制御を改善。  
- **FinFET → GAA**：チャネルを完全に囲み、さらに制御性を強化。  
- **GAA → CFET**：nFET/pFET の積層により配線効率・面積効率を飛躍的に改善。  
- **Post-CFET へ**：材料限界（Si）と熱限界を突破するため、新しい物理・新しい統合が必要。  

---

## 3. Post-CFET 候補技術

### 3.1 二次元材料 FET
- **実証例**：IEDM 2023 で **MoS₂ Lg=12 nm FET** が報告され、**Ion/Ioff ≈ 10⁷、SS ≈ 65 mV/dec** を達成。  
- **物理原理**：原子1層〜数層の vdW 材料（MoS₂, WS₂, WSe₂, Black Phosphorus）をチャネルに利用。  
- **製造課題**：
  - 大面積成膜の均一性（CVD 成膜で 5–10% のばらつき残存）  
  - 金属接触抵抗 Rc ≈ 1 kΩ·µm  
  - 薄膜の層間変動性  
- **応用分野**：IoT ノード、フレキシブル電子回路、生体センサー。  
- **設計影響**：SPICE モデル未成熟、統計設計への適用が課題。  

---

### 3.2 モノリシック 3D 集積（M3D）
- **実証例**：2019 IEDM で **SRAM 上下2層積層**が報告され、**配線遅延 30% 減、面積 40% 削減**。  
- **研究進展**：*Nature Electronics 2022* にて AI ワークロードで **エネルギー効率 1.4–1.7 倍** 改善を報告。  
- **物理原理**：Sequential プロセスで層ごとにトランジスタ形成＋超微細 ILV 接続。  
- **製造課題**：
  - 低温プロセス（<450℃）必須  
  - 層間ばらつき（しきい値電圧、信頼性）  
  - ホットスポット発生（>1 W/mm²）  
- **応用分野**：AI アクセラレータ、メモリ中心コンピューティング。  
- **設計影響**：3D 配置配線設計、熱・応力解析のEDA統合が必須。  

---

### 3.3 スピントロニクス・量子デバイス
- **実証例**：IBM による **STT-MRAM endurance 10¹² cycle**。  
- **研究進展**：SOT-MRAM 書込み電流 **30–40% 削減**、トポロジカル FET で室温オン/オフ比 **10³**。  
- **物理原理**：スピン自由度（Spin-FET, Spin-logic）、トポロジカル絶縁体を利用。  
- **製造課題**：
  - 室温安定化、プロセス互換性  
  - 書込み電流の低減（数 mA → 数百 µA レベルへ）  
- **応用分野**：ニューロモーフィック計算、宇宙用耐放射線システム、In-Memory Computing。  
- **設計影響**：不揮発性＋演算融合により、新アーキテクチャ設計が必須。  

---

### 3.4 異種原子スケール集積
- **実証例**：*Nature Photonics 2020* にて **Si 導波路＋MoS₂ 光検出器**、Responsivity ≈ 200 mA/W @1.55 µm。  
- **物理原理**：Si CMOS + 2D + フォトニクス + MEMS のモノリシック統合。  
- **製造課題**：
  - 界面整合、熱膨張差、クラック対策  
  - 高温プロセス互換性  
- **応用分野**：光インターコネクト、センサー統合、医療・宇宙システム。  
- **設計影響**：異分野モデル化が課題、Cross-domain EDA 必須。  

---

## 4. 設計・教育的観点
- **SystemDK / AITL の必要性**：Post-CFET 技術は熱・応力・量子効果など多物理制約を伴うため、EDA に統合する必要がある。  
- **教育カリキュラム例**：
  1. CMOS スケーリング史  
  2. Post-CFET 候補技術レビュー  
  3. マルチフィジックス設計演習（熱解析、応力解析）  
  4. 応用事例（IoT/AI/宇宙探査）  
  5. SystemDK+AITL による設計補償演習  

---

## 5. 将来シナリオ
- **2030年代前半**：2D-CFET ハイブリッド、M3D-2D 統合実証。  
- **2030年代後半**：IoT/AI Edge 部分導入。  
- **2040年代**：HPC・宇宙用途で主流化、EDA 教育に統合。  

---

## 6. 結論
Post-CFET デバイスは、**構造スケーリングから材料・システム統合スケーリング**へのパラダイムシフトを象徴する。研究的進展に加え、**教育・設計支援・社会実装**の観点で体系化することが求められる。  

---

## 7. 図・表

### 図1：CMOS → CFET → Post-CFET 進化ツリー
➡ [evolution_tree_detailed.mmd](./figures/evolution_tree_detailed.mmd)

### 図2：Post-CFET デバイス概念ブロック図
➡ [post_cfet_block_diagrams.mmd](./figures/post_cfet_block_diagrams.mmd)

### 図3：Post-CFET 技術マインドマップ
➡ [post_cfet_mindmap.mmd](./figures/post_cfet_mindmap.mmd)

### 表1：Post-CFET 候補技術の比較マトリクス（詳細版）
➡ [comparison_full.md](./figures/comparison_full.md)

---

## 参考文献
1. IRDS, *International Roadmap for Devices and Systems*, 2024 Edition  
2. 高木聡一郎ほか, “2D材料FETのCMOS限界突破可能性,” *IEDM Tech Digest*, 2023  
3. Liu et al., “Monolithic 3D Integration for Memory-Centric Computing,” *Nature Electronics*, 2022  
4. Fert et al., “Spintronics: The Future of Logic and Memory,” *Rev. Mod. Phys.*, 2019  
5. Wong, H.-S. P., “Beyond the Limits of Silicon: Opportunities and Challenges of 2D Materials,” *Nature Reviews Materials*, 2020  
6. Batude, P. et al., “3D Sequential Integration: A Key Enabler of Monolithic 3D ICs,” *IEDM*, 2019  
