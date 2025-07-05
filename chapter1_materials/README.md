# 第1章：半導体物性の基礎とMOS構造への導入

本章では、MOSトランジスタやLSI回路設計の物理的基盤となる**半導体物性の本質**を、以下の段階で丁寧に解説します：

1. バンド構造とキャリア
2. PN接合と整流特性
3. MOS構造における電界制御とチャネル形成
4. MOSトランジスタのスイッチ動作
5. CMOSインバータによる論理回路の出発点

これにより、**物性物理から論理回路の入り口まで**を、一貫した流れとして理解できる構成になっています。

---

## 🔍 本章の位置づけ

- MOSトランジスタは、**電界によりON/OFFが切り替わる構造**を持ちますが、その背景にはバンド構造やPN接合の原理が存在します。
- 本章では、MOSの構造と動作を、**スイッチ動作に至るまでの物理的視点で段階的に理解**することを重視します。
- 第2章以降の**論理ゲート・組み合わせ回路・順序回路設計**に必要な基盤を形成します。

---

## 📘 章構成（chapter1_materials/）

| 節番号 | ファイル名 | 内容概要 |
|--------|------------|----------|
| 1.1 | [`1.1_band_structure.md`](./1.1_band_structure.md) | バンド構造とキャリア（電子・正孔・ドーピング） |
| 1.2 | [`1.2_pn_junction.md`](./1.2_pn_junction.md) | PN接合、空乏層、整流と接合ダイオードの動作 |
| 1.3 | [`1.3_mos_structure.md`](./1.3_mos_structure.md) | MOS構造、電界制御、チャネル形成（nMOS/pMOSの基本） |
| 1.4 | [`1.4_mos_switch.md`](./1.4_mos_switch.md) | MOSトランジスタのスイッチ動作と回路的ON/OFFモデル |
| 1.5 | [`1.5_cmos_inverter.md`](./1.5_cmos_inverter.md) | CMOSインバータの構造・論理動作・波形と消費電力 |

---

## 🧠 学習のポイント

- 半導体物性の3本柱（バンド構造、PN接合、MOS構造）を段階的に理解
- MOSのチャネル形成と電圧制御によるスイッチ動作の本質を掴む
- nMOS/pMOSを組み合わせたCMOSインバータを通じて、論理回路設計の出発点へ到達する

---

## 📂 ディレクトリ構成

```
Edusemi-v4x/
└── chapter1_materials/
    ├── README.md
    ├── 1.1_band_structure.md
    ├── 1.2_pn_junction.md
    ├── 1.3_mos_structure.md
    ├── 1.4_mos_switch.md
    └── 1.5_cmos_inverter.md
```

---

## 🖼️ 図版・補足予定

- `/images/` に以下の図版を格納予定：
  - `band_diagram_intrinsic.png`（真性半導体）
  - `pn_depletion_potential.png`（空乏層・整流）
  - `mos_cross_section.png`（MOS断面）
  - `mos_depletion_inversion.png`（空乏→反転）
  - `nmos_switch.png`, `pmos_switch.png`, `mos_switch_model.png`
  - `cmos_inverter_structure.png`, `cmos_inverter_logic.png`, `cmos_inverter_waveform.png`

---

## 🔄 次章への接続

- 第2章では、本章の理解をもとに、**論理ゲートや組み合わせ回路**の設計・解析へ進みます。
- CMOSインバータを起点とした**論理演算回路の構成原理**を実践的に展開していきます。

---

## © ライセンス

この教材は MIT ライセンスの下で公開されています。詳細はプロジェクトルートの [LICENSE](../LICENSE) をご覧ください。
