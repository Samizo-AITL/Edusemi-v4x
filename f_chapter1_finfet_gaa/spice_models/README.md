# SPICE Models for FinFET / GAA Transistors  
FinFET / GAA トランジスタ用 SPICE モデル

このディレクトリには、15nm世代のFinFETおよび5nm世代のGAA（Gate-All-Around）構造に対応した、BSIM-CMG準拠のSPICEモデルを収録しています。

## 📁 File List / ファイル一覧

| File | Description |
|------|-------------|
| `finfet_15nm_model.spice` | 15nm FinFETモデル（BSIM-CMG） |
| `gaa_5nm_model.spice`     | 5nm GAAモデル（Multi-Nanosheet） |
| `nmos_iv_test.spice`      | I-Vカーブ確認用の共通テストベンチ |

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

## 📌 Future Work / 今後の予定

- ✅ PMOSモデルの追加（`pfinfet`, `pgaa`）
- ✅ CFET仮想モデルの定義（`cfet_stack_model.spice`）
- 📊 PythonによるI-Vプロット例の追加
- 📚 教材との統合（Edusemi 第1章と連携）

---

## 🧪 参考仕様（抜粋）

| Parameter | FinFET | GAA |
|-----------|--------|-----|
| Node      | 15nm   | 5nm |
| W_eff     | 3 fins × 30nm | 3 sheets × 5nm |
| T_ox      | 1.2nm | 0.8nm |
| V_th      | 0.42V | 0.38V |

---

**Author**: Samizo-AITL / Edusemi Project  
**License**: MIT (or educational use only, if specified)
