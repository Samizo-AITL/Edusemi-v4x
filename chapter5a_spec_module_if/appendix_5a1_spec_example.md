---
layout: default
title: 付録 5a.1｜仕様書の具体例（教育用サンプル 3種）
---

# 📎 付録 5a.1 : 仕様書の具体例（教育用サンプル 3種）  
**Appendix 5a.1 : Example Specification Documents (3 Educational Samples)**

---

## 📝 サンプル1：小型マイコンSoC  
**Sample 1: Compact MCU SoC**

| 項目 / Item | 日本語 | English |
|-------------|--------|---------|
| **プロジェクト名** | 教育用センサ連携マイコンSoC | Educational Sensor-Interface MCU SoC |
| **目的** | センサ信号の取得・処理・PC送信を統合 | Integrate sensor data acquisition, processing, and PC transmission |
| **機能要件** | - I²C外部センサ入力<br>- 16bit ALU<br>- UART通信 | - I²C external sensor input<br>- 16-bit ALU<br>- UART communication |
| **性能要件** | 50 MHz, UART 115200 bps, 消費電力200 mW以下 | 50 MHz, UART 115200 bps, ≤ 200 mW power |
| **制約条件** | FPGA (Artix-7 100T), 3.3V/1.8V, Sky130互換 | FPGA (Artix-7 100T), 3.3V/1.8V, Sky130 compatible |
| **インターフェース** | UART, I²C, AMBA-APB, SRAM 32KB | UART, I²C, AMBA-APB, SRAM 32KB |
| **評価方法** | FPGA動作確認、UARTログ取得、消費電力測定 | FPGA verification, UART log, power measurement |
| **拡張性** | SPI追加、ALU32bit化 | Add SPI, expand ALU to 32-bit |

---

## 🖼 サンプル2：画像処理向けSoC  
**Sample 2: Image Processing SoC**

| 項目 / Item | 日本語 | English |
|-------------|--------|---------|
| **プロジェクト名** | 教育用リアルタイム画像処理SoC | Educational Real-Time Image Processing SoC |
| **目的** | カメラ入力をリアルタイム処理して表示 | Real-time processing of camera input and display output |
| **機能要件** | - CMOSカメラ入力（MIPI CSI-2）<br>- RGB to Grayscale変換<br>- VGA出力 | - CMOS camera input (MIPI CSI-2)<br>- RGB to Grayscale conversion<br>- VGA output |
| **性能要件** | 100 MHz動作, フレームレート30fps | 100 MHz, 30 fps frame rate |
| **制約条件** | FPGA (Zynq-7020), DDR3 512MB | FPGA (Zynq-7020), DDR3 512MB |
| **インターフェース** | MIPI CSI-2, VGA, AXI4, DDR3 | MIPI CSI-2, VGA, AXI4, DDR3 |
| **評価方法** | 動画入力→処理→出力の一連動作を計測 | End-to-end video processing test |
| **拡張性** | OpenCV連携、エッジ検出機能追加 | OpenCV integration, edge detection |

---

## ⚡ サンプル3：高速通信SoC  
**Sample 3: High-Speed Communication SoC**

| 項目 / Item | 日本語 | English |
|-------------|--------|---------|
| **プロジェクト名** | 教育用高速通信FPGA SoC | Educational High-Speed Communication FPGA SoC |
| **目的** | 高速シリアル通信リンクを用いたデータ転送検証 | Verify high-speed serial link for data transfer |
| **機能要件** | - 10GbE対応MAC<br>- DMAエンジン<br>- CRCエラーチェック | - 10GbE MAC<br>- DMA engine<br>- CRC error check |
| **性能要件** | 156.25 MHzリファレンスクロック, 10Gbpsリンク | 156.25 MHz ref clock, 10 Gbps link |
| **制約条件** | FPGA (Kintex-7), SFP+モジュール | FPGA (Kintex-7), SFP+ module |
| **インターフェース** | 10GbE (XAUI), AXI4-Stream, DDR4 | 10GbE (XAUI), AXI4-Stream, DDR4 |
| **評価方法** | 連続データ転送速度・エラー率測定 | Measure sustained throughput & BER |
| **拡張性** | 暗号化モジュール追加 | Add encryption module |

---

## 📌 作成時の共通ポイント

1. **必須要件・性能を明確に数値で示す**  
2. **評価方法を仕様書に含める**  
3. **拡張性の記述で将来性を示す**  

---

## 🔗 関連リンク

- [第5a.1節：仕様策定のプロセス](../5a.1_spec_process.md)  
- [第5a章 README](../README.md)  

---

## 👤 著者・ライセンス｜Author & License

| 項目 / Item | 内容 / Details |
|-------------|----------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |
