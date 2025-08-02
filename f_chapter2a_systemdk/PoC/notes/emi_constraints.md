# EMI Constraints and Isolation Strategy（EMI制約とアイソレーション戦略）

## 1. Overview / 概要
- EMI（電磁妨害）のPoC設計における重要性
- AMS / RF回路 / MRAM / FPGA間の干渉

## 2. EMI Sources in PoC Board / EMI発生源
- PLL・クロック・高dV/dt I/O
- 書き込みパルス（MRAM）
- FPGAのDDRアクセス・SPI通信波形

## 3. Simulation and Analysis Methods / 解析手法
- Near-field / Far-field EMIモデリング
- PCBスタックとEM放射の相関（3D EMCツール想定）
- EMI-thermal連成（例：電磁波→局所発熱）

## 4. EMI Mitigation Strategy / 緩和設計案
- GNDシールド／スタック層制御
- Power Island分割（AMS/MRAM隔離）
- EMI-aware floorplanning（SystemDK対応）

## 5. SystemDKへの制約統合
- PKGDKでの伝導・放射ノイズ制御フラグ
- EMI-critical regionの自動検出スクリプト連携

## 6. Figures / 図解
- EMI干渉イメージ（AMS-MRAM間）
- 層構造別放射パターン例

## 7. References
- [1] EMI Design Guidelines for Mixed-Signal SoC, 2024.
- [2] 自作PoC解析ログ・EMIツール出力例

---

（例図挿入）

![emi_interference](figures/emi_interference_mram_ams.png)
