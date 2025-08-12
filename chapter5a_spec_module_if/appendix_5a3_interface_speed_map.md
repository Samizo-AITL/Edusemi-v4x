---
layout: default
title: 基礎編 第5a.3a付録｜インターフェース性能比較マップ
---

---

# 📎 基礎編 第5a.3a付録 : インターフェース性能比較マップ  
**Fundamentals Appendix 5a.3a : Interface Performance Comparison Map**

---

## 🎯 付録の目的｜Purpose of This Appendix

| 🇯🇵 日本語 | 🇺🇸 English |
|-----------|-----------|
| 各種インターフェースの**速度・レイテンシ・距離・用途**を一目で比較できるようにする | Provide a side-by-side comparison of various interfaces in terms of **speed, latency, distance, and applications** |
| PoC段階と量産段階での**最適IF選定の判断材料**とする | Serve as a decision-making reference for selecting the optimal interface at PoC and mass production stages |

---

## 📊 インターフェース性能比較表｜Interface Performance Table

| **インターフェース / Interface** | **最大速度（理論値） / Max Speed** | **レイテンシ / Latency** | **典型距離 / Typical Distance** | **主用途 / Main Applications** |
|----------------------------------|-----------------------------------|--------------------------|----------------------------------|----------------------------------|
| **I²C (Std/Fast)**               | 100 / 400 kbps                    | 高 / High                | ～1 m                            | センサ制御 / Sensor control |
| **SPI**                          | ～50 Mbps                         | 低 / Low                 | 数十 cm                          | LCD制御、外部ADC/DAC / LCD control, external ADC/DAC |
| **UART**                         | ～1 Mbps                          | 中 / Medium              | 数 m                             | デバッグ、設定 / Debug, configuration |
| **USB 2.0**                      | 480 Mbps                          | 低 / Low                 | 数 m                             | 外部I/O、データ転送 / External I/O, data transfer |
| **USB 3.x**                      | 5 Gbps                            | 低 / Low                 | 数 m                             | 高速外部I/O / High-speed external I/O |
| **Ethernet (100M/1G)**            | 100 Mbps / 1 Gbps                  | 中 / Medium              | ～100 m                          | ネットワーク接続 / Networking |
| **PCI Express Gen3**              | 8 Gbps/lane                       | 低 / Low                 | 数十 cm                          | 高速内部接続 / High-speed internal connection |
| **DDR4-3200**                     | 3.2 Gbps/pin                      | 非常に低 / Very low      | 数 cm                            | メインメモリ / Main memory |
| **LPDDR4**                        | 4.2 Gbps/pin                      | 非常に低 / Very low      | 数 cm                            | モバイル用メモリ / Mobile memory |
| **MIPI CSI-2**                    | ～6 Gbps/lane                     | 低 / Low                 | 数十 cm                          | カメラ入力 / Camera input |
| **MIPI DSI**                      | ～6 Gbps/lane                     | 低 / Low                 | 数十 cm                          | ディスプレイ出力 / Display output |

---

## 🗺 性能マップ（帯域幅 vs 距離）｜Performance Map (Bandwidth vs Distance)

> 💡 Mermaid図をGitHubで見る  
> [🔗 View on GitHub (appendix_5a3_interface_speed_map.md)](https://github.com/Samizo-AITL/Edusemi-v4x/blob/main/chapter5a_spec_module_if/appendix_5a3_interface_speed_map.md)

```mermaid
%% Bandwidth vs Distance chart (categorized)
graph LR
    subgraph Short_Distance[短距離 / Short Distance]
        SPI[SPI<br/>~50 Mbps]
        MIPI_CSI[MIPI CSI-2<br/>~6 Gbps]
        MIPI_DSI[MIPI DSI<br/>~6 Gbps]
        DDR4[DDR4-3200<br/>3.2 Gbps/pin]
        LPDDR4[LPDDR4<br/>4.2 Gbps/pin]
        PCIe[PCIe Gen3<br/>8 Gbps/lane]
    end

    subgraph Medium_Distance[中距離 / Medium Distance]
        UART[UART<br/>~1 Mbps]
        USB2[USB 2.0<br/>480 Mbps]
        USB3[USB 3.x<br/>5 Gbps]
        Ethernet1G[Ethernet 1G<br/>1 Gbps]
    end

    subgraph Long_Distance[長距離 / Long Distance]
        I2C[I²C<br/>100/400 kbps]
        Ethernet100M[Ethernet 100M<br/>100 Mbps]
    end
```

---

## 🛠 設計での使い方｜How to Use in Design

| **設計段階 / Design Stage** | **優先事項 / Priority Points** |
|-----------------------------|--------------------------------|
| **PoC段階 / PoC Stage** | 実装容易性とFPGA互換性を優先<br>Prioritize ease of implementation and FPGA compatibility |
| **量産段階 / Mass Production Stage** | 信号品質・規格適合・EMC対策を重視<br>Focus on signal integrity, standard compliance, and EMC countermeasures |
| **共通注意点 / Common Notes** | 高速IFは配線長・レイアウト制約が大きくなるため、基板・パッケージ設計と早期連携<br>High-speed IFs require early co-design with PCB and package designers due to length/layout constraints |

---

## 🔗 関連ページ｜Related Pages

- [📘 第5a.3節：インターフェース設計と種類](5a.3_interface_design.md)  
- [📘 第5a章 README](README.md)  

---

## 👤 著者・ライセンス｜Author & License

| **項目 / Item** | **内容 / Details** |
|-----------------|--------------------|
| **著者 / Author** | 三溝 真一（Shinichi Samizo） |
| **GitHub** | [Samizo-AITL](https://github.com/Samizo-AITL) |
| **Email** | [shin3t72@gmail.com](mailto:shin3t72@gmail.com) |
| **ライセンス / License** | MIT License（再配布・改変自由）<br>Redistribution and modification allowed |

---

## 🔙 戻る｜Back

**⬅ [第5a.3節：インターフェース設計と種類](5a.3_interface_design.md)**  
**🏠 [第5a章トップ](README.md)**
