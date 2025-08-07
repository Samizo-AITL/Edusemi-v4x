# 📉 5a.4 1/fノイズの低減技術  
# 📉 5a.4 Flicker Noise Reduction Techniques

---

## 📘 概要｜Overview

低周波動作のアナログ回路では、**1/fノイズ（フリッカーノイズ）**が信号忠実度に深刻な影響を与えます。  
MOSトランジスタでは、主にチャネル界面のトラップ状態に起因するこのノイズは、特に差動入力・センサ・ADCフロントエンドで設計上の制約となります。

In low-frequency analog circuits, **1/f noise (flicker noise)** critically affects signal integrity.  
In MOSFETs, this noise mainly originates from trap states at the channel interface and imposes design challenges in differential inputs, sensors, and ADC front-ends.

---

## ⚠️ 原因と影響｜Cause and Impact

### 🔍 発生メカニズム｜Mechanism

1/fノイズは、チャネル界面に存在するトラップによってキャリアが**捕獲・再放出**されることで生じる電流ゆらぎに起因します。

- トラップ密度が高い → ノイズ増大
- チャネル面積が小さい → ノイズ増大
- 周波数が低い → ノイズ増大（$\propto 1/f$）

---

## 📈 スペクトルの例｜Example Spectrum
```
S(f)
↑
│      ／￣￣￣￣￣
│     /
│    /    ← 1/f ノイズ領域
│   /
│  /             ／→ 白色熱雑音（Johnson-Nyquist）
│_/＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
→ f（周波数）
```
---

## 📏 ノイズ電圧密度の近似式｜Approximate Noise Density

MOSFETにおける1/fノイズ電圧密度は以下で近似されます：

$$
S_{V}(f) = \frac{K}{C_{\mathrm{ox}}^2 W L f}
$$

- $K$：プロセス依存定数（トラップ密度に比例）
- $C_{\mathrm{ox}}$：ゲート酸化膜容量（$=\varepsilon_{\mathrm{ox}}/t_{\mathrm{ox}}$）
- $W$, $L$：トランジスタの幅と長さ
- $f$：周波数

---

## 🔧 ノイズ低減の設計技術｜Noise Reduction Techniques

| 対策｜Technique | 内容｜Description |
|--------|--------|
| **PMOSを優先的に使用** | nMOSより1/fノイズが小さい（ホール vs 電子のトラップ感度） |
| **W・Lを大きく設計** | チャネル面積を増やしてノイズ源の平均化 |
| **酸化膜品質の向上** | RTO, H₂アニールで界面トラップ密度を低減 |
| **チョッピング回路（Chopper Amp）** | 低周波ノイズを変調して高周波で除去 |
| **Auto-Zero Amp** | ノイズをサンプリングでキャンセル（ゼロ点補正） |

---

## 🧪 実務的な影響｜Practical Impact Examples

- センサ回路のオフセット揺らぎが測定精度を制限  
  *Offset fluctuation limits sensor accuracy*
- ADC入力段でノイズフロアが上昇  
  *Flicker noise increases ADC noise floor*
- 差動アンプの出力ドリフトが時間経過で増加  
  *Output drift over time due to 1/f noise in diff amp*

---

## 🧭 関連項目｜Related Topics

- [`3_rsce_and_ldd.md`](./3_rsce_and_ldd.md)：短チャネル高ドーピングとの関連性  
- [`chapter4_mos_characteristics/`](../chapter4_mos_characteristics/)：酸化膜品質と界面準位の解説  
- [`ams_overview.md`](../d_chapter5_analog_mixed_signal/ams_overview.md)：ノイズとPSRR全体像

---

## 🧠 用語解説｜Glossary

| 用語｜Term | 意味｜Meaning |
|--------|------------------|
| 1/f Noise | フリッカーノイズ。低周波に強く現れる非理想雑音 |
| $S_{V}(f)$ | ノイズ電圧密度（[V²/Hz]） |
| Chopper Amp | 入力信号を変調・復調して低周波ノイズを除去する回路 |
| $C_{\mathrm{ox}}$ | ゲート酸化膜容量（F/cm²） |

---

## ✅ まとめ｜Summary

1/fノイズは、低周波アナログ回路の性能を制限する根本的な要因です。  
AMS設計においては、**デバイス選択・構造寸法・酸化膜制御・回路手法の多層的対応**が必要となります。

Flicker noise is a fundamental limitation in low-frequency analog circuits.  
Effective AMS design requires a **multilayered strategy of device choice, geometry tuning, oxide quality, and circuit-level techniques**.

---

[🎛️ 応用編　第5章a：0.18um AMS設計技法　トップに戻る](./README.md)




