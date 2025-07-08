# 🌟 特別編 第4章：FSM×PID×LLM制御系のOpenLaneによるRTL-to-GDSII実装

## 📘 概要

本章では、Edusemi特別編 第3章で構築した FSM×PID×LLM のRTL実装をもとに、  
**OpenLane v2.0 + Sky130 PDK** を用いて物理設計（配置配線→GDSII生成）を行います。

各モジュール（FSM / PID / SoC統合）について、以下のフローを段階的に体験できます：

- 論理合成
- 配置・配線
- DRC/LVS検証
- タイミング解析
- GDSレイアウト生成
- KLayoutやMagicによる可視化

---

## 📖 学習の流れ（章ナビゲーション）

### 🔹 各節リンク

- [4.1 OpenLane導入と構成](docs/4_1_openlane_intro.md)
- [4.2 FSM配置配線](docs/4_2_fsm_layout.md)
- [4.3 PID配置配線](docs/4_3_pid_layout.md)
- [4.4 SoC統合配置配線](docs/4_4_soc_layout.md)
- [4.5 設計評価と比較](docs/4_5_evaluation.md)
- [4.6 GDS可視化と考察](docs/4_6_gds_view.md)

---

## 📂 構成ディレクトリ

```
f_chapter4_openlane/
├── README.md
├── index.md
├── _sidebar.md
├── toc_f_chapter4_openlane.md
├── docs/
└── openlane/
```

---

## 🚀 実行環境について

- **OpenLane v2.0 以上**
- **Sky130A PDK**（Open_PDK準拠）
- Docker版または手動インストール環境
- Magic / KLayout によるGDS可視化も対応

---

## 📎 前提教材

- 特別編 第3章：[FSM×PID×LLMによる統合制御システムのSoC実装手法](../f_chapter3_soc/README.md)
