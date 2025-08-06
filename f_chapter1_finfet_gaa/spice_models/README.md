# SPICE Models for FinFET / GAA Transistors  
FinFET / GAA トランジスタ用 SPICE モデル

このディレクトリには、15nm世代のFinFETおよび5nm世代のGAA（Gate-All-Around）構造に対応した、BSIM-CMG準拠のSPICEモデルを収録しています。

## 📁 File List / ファイル一覧

| File | Description |
|------|-------------|
| `finfet_15nm_model.spice` | 15nm FinFETモデル（BSIM-CMG） |
| `gaa_5nm_model.spice`     | 5nm GAAモデル（Multi-Nanosheet） |
| `pfinfet_15nm_model.spice` | 15nm FinFET PMOSモデル |
| `pgaa_5nm_model.spice`     | 5nm GAA PMOSモデル |
| `nmos_iv_test.spice`      | I-Vカーブ確認用の共通テストベンチ |
| `cmos_inverter_finfet.spice` | FinFET CMOSインバータ回路 |
| `cmos_inverter_gaa.spice` | GAA CMOSインバータ回路 |

---

## ✅ How to Use / 使い方

1. 使用したいモデルを`.include`で読み込む：

```
.include finfet_15nm_model.spice
* または
.include gaa_5nm_model.spice
```

2. `nmos_iv_test.spice` を使って I-V 特性を確認可能：

```
.dc Vgs 0 1.0 0.05
.print dc V(drain) I(Vds)
```

> **Note:** この回路は簡易ベンチであり、LTspiceやngspiceで動作確認可能です。

---

## 📈 I-V Test Sample

```spice
.dc Vgs 0 1.0 0.05
.print dc V(drain) I(Vds)
```

---

## ⚙️ CMOS Inverter Examples / CMOSインバータ回路例

以下は、FinFETおよびGAA構造を用いたCMOSインバータのSPICE回路例です。  
V<sub>in</sub>をスイープし、V<sub>out</sub>の反転特性（VTCカーブ）を観察できます。

| File | Description |
|------|-------------|
| `cmos_inverter_finfet.spice` | FinFET (15nm) CMOS インバータ回路 |
| `cmos_inverter_gaa.spice`    | GAA (5nm) CMOS インバータ回路     |

---

### 🧪 Example: cmos_inverter_finfet.spice

```spice
.include finfet_15nm_model.spice
.include pfinfet_15nm_model.spice

Vdd vdd 0 DC 0.8
Vin in 0 DC 0.0
M1 out in 0 0 nfinfet L=15n W=120n
M2 out in vdd vdd pfinfet L=15n W=120n

.dc Vin 0 0.8 0.05
.print dc V(in) V(out)
.end
```

---

### 🧪 Example: cmos_inverter_gaa.spice

```spice
.include gaa_5nm_model.spice
.include pgaa_5nm_model.spice

Vdd vdd 0 DC 0.8
Vin in 0 DC 0.0
M1 out in 0 0 ngaa L=10n W=120n
M2 out in vdd vdd pgaa L=10n W=120n

.dc Vin 0 0.8 0.05
.print dc V(in) V(out)
.end
```

---

📌 `.dc`解析を行うことで、CMOSインバータの **伝達特性（VTCカーブ）** をプロットできます。  
LTspice / ngspice / XYプロッターなどで確認してください。

---

## 📌 Future Work / 今後の予定

- ✅ PMOSモデルの追加（`pfinfet`, `pgaa`）
- ✅ CMOSインバータの追加（FinFET / GAA）
- 🔜 CFET仮想モデルの定義（`cfet_stack_model.spice`）
- 📊 PythonによるI-V / VTCプロット例の追加
- 📚 教材との統合（Edusemi 第1章と連携）

---

## 🧪 参考仕様（抜粋）

| Parameter | FinFET | GAA |
|-----------|--------|-----|
| Node      | 15nm   | 5nm |
| W_eff     | 3 fins × 30nm | 3 sheets × 5nm |
| T_ox      | 1.2nm | 0.8nm |
| V_th      | 0.42V / –0.45V | 0.38V / –0.40V |

---

**Author**: Samizo-AITL / Edusemi Project  
**License**: MIT (or educational use only, if specified)
