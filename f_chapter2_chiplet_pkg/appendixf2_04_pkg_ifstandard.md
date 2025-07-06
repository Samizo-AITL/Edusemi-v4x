# 📘 Appendix 2.4：UCIeなどの標準インタフェースと今後の動向

本資料では、チップレットや2.5D/3D集積で用いられる**標準的なチップ間インタフェース（Die-to-Die I/F）**について、代表例とその比較、今後の技術潮流を解説します。

---

## 🔌 なぜ標準I/Fが必要か？

- チップレット時代では**異なるベンダーのダイを組み合わせる**可能性が高まる
- SoC内のバスと異なり、**パッケージ内での高速かつ低電力な接続**が必要
- 各社が独自規格で閉じた設計をする時代から、**オープンで再利用可能なI/F**へ

---

## 🔷 主要なDie-to-Die I/F一覧

| 規格 | 帯域幅 | レイテンシ | 特徴 |
|------|--------|------------|------|
| **UCIe** | 32Gbps/lane（v1.1） | 数ns以下 | オープン規格、業界標準化中（Intel, TSMC等） |
| **XSR** | ～112Gbps | 低 | SerDesベース、高速信号向け |
| **Bunch of Wires (BoW)** | 2–16Gbps/lane | 低 | オープンなシリアルI/F（OIF主導） |
| **AIB** | ～20Gbps | 低 | Intel独自規格、EMIBで採用 |
| **HBI (Hybrid Bonding I/F)** | >1000Gbps/mm² | 超低 | TSV+Hybrid Bonding前提、先端プロセス向け |

---

## 🧩 UCIe（Universal Chiplet Interconnect Express）の概要

- 2022年、Intel主導で発表、現在は**業界コンソーシアム**で管理
- **Protocol Stack構造**により、PCIeやCXLとも親和性あり
- PHY/Die-to-Die層、Link層、Protocol層の3階層
```
  UCIe Stack:
+———————+
| Protocol Layer      | ← PCIe, CXL, etc.
+———————+
| Link Layer          |
+———————+
| Die-to-Die PHY      | ← 配線距離 < 2mm
```

---

## 🔄 技術動向と今後の焦点

| 観点 | 傾向 |
|------|------|
| 配線距離 | 数mm以下（パッケージ内）を前提とした設計 |
| 信号方式 | NRZ/ PAM4による高速低電力I/O設計 |
| オープン化 | UCIeやBoWを中心に業界が集約傾向 |
| 熱と実装制約 | 高帯域時の熱集中とEMI対策が課題 |

---

## 📌 まとめ

標準化されたDie-to-Die I/Fは、**チップレット設計の普及と再利用性の鍵**です。今後のIPベンダーやEDAツールも、UCIe対応を前提とした設計支援が進むと考えられます。

---
