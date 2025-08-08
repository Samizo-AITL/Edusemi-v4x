---
layout: default
title: Appendix 2.4 - Standard Die-to-Die Interfaces and Future Trends
---

# 📘 Appendix 2.4：UCIeなどの標準インタフェースと今後の動向  
**Appendix 2.4: Standard Die-to-Die Interfaces and Future Trends**

---

## 📌 概要 / Overview

本資料では、チップレットや2.5D/3D集積における**代表的なチップ間インタフェース（Die-to-Die I/F）**について、  
主要規格の比較と技術的な位置づけ、そして今後の潮流をまとめます。  
*This appendix covers standard Die-to-Die interfaces used in chiplet and 2.5D/3D integration, including key specifications and future directions.*

---

## 🔌 なぜ標準I/Fが必要か？  
**Why Are Standard Interfaces Needed?**

| 💡 視点 / Perspective | 🔍 解説 / Explanation |
|------------------------|-------------------------|
| **異種ベンダー対応**<br>Multi-vendor Integration | チップレット設計では異なる企業のIP/ダイを統合する必要がある<br>Chiplets may come from different vendors |
| **SoC内との違い**<br>Beyond Traditional SoC Buses | パッケージ内での高速・低消費電力通信が要求される<br>Package-level interconnects require high-speed, low-power |
| **オープン化の加速**<br>Move Toward Openness | 専用バスからオープンな標準I/Fへ<br>Shift from proprietary to open and reusable interfaces |

---

## 🔷 主要なDie-to-Dieインタフェース一覧  
**Comparison of Representative Die-to-Die I/F Standards**

| 🌐 規格 / Standard | 🚀 帯域幅 / Bandwidth | ⏱️ レイテンシ / Latency | 📘 特徴 / Features |
|--------------------|------------------------|--------------------------|----------------------|
| **UCIe** | 32Gbps/lane（v1.1） | 数ns以下 | オープン・業界標準化中（Intel, TSMC等）<br>Open industry consortium |
| **XSR** | ～112Gbps | 低 | SerDesベースの高速I/O<br>SerDes-based for high-speed links |
| **BoW**<br>(Bunch of Wires) | 2–16Gbps/lane | 低 | OIF主導の低電力オープンI/F<br>Open serial I/F by OIF |
| **AIB** | ～20Gbps | 低 | Intel独自、EMIB向け<br>Intel proprietary, used in EMIB |
| **HBI**<br>(Hybrid Bonding I/F) | >1000Gbps/mm² | 超低 | TSV + Hybrid Bondingベース<br>Requires TSV + Hybrid bonding |

---

## 🧩 UCIeの構造と特徴  
**UCIe (Universal Chiplet Interconnect Express)**

### ✦ 概要

- 2022年にIntelが提唱、現在は**業界コンソーシアム**形式で管理  
  *Proposed by Intel, now governed by an industry consortium*
- **階層化プロトコルスタック**により、他の標準（PCIe、CXL等）との互換性あり  
  *Layered protocol stack allows interoperability with PCIe/CXL*
- PHYレイヤ、Linkレイヤ、Protocolレイヤの3階層構成

```
  UCIe Stack:
+-------------------------+
| Protocol Layer         | ← PCIe, CXL, etc.
+-------------------------+
| Link Layer             |
+-------------------------+
| Die-to-Die PHY Layer   | ← 配線距離 < 2mm
```

---

## 🔄 技術動向と設計トレンド  
**Trends in Interconnect Technology and Design**

| 🧠 観点 / Focus | 📊 傾向 / Trend |
|------------------|-------------------------|
| **配線距離**<br>Wiring Distance | 数mm以下を想定、低スイング駆動が可能<br>Short-range (< 2mm) driving enables low-power links |
| **信号方式**<br>Signaling | PAM4/NRZ等の多値信号化対応<br>Use of NRZ/PAM4 for bandwidth efficiency |
| **オープン化**<br>Standardization | BoW/UCIeへの業界集約が進行<br>Convergence toward BoW and UCIe |
| **熱・EMI対策**<br>Thermal and EMI | 帯域幅増加に伴う熱集中と電磁干渉が新たな課題<br>Higher bandwidth brings thermal/EMI concerns |

---

## 📌 まとめ / Summary

標準化されたDie-to-Die I/Fは、**チップレット技術のスケーラビリティと再利用性**の鍵を握ります。  
*Standardized interfaces are essential for scalable and reusable chiplet integration.*

➡ UCIeはその中心的存在として、今後**EDAツール・IP設計の前提**にもなりうる規格です。  
➡ UCIe will likely become a default assumption for **EDA/IP design ecosystems**.

---

## 🔗 特別編 第2章 トップへ戻る  
[📎 戻る｜Back to Chapter 2 Top](./README.md)
