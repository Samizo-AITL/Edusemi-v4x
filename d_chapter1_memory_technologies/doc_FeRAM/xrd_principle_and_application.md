# 📘 X線回折（X-ray Diffraction, XRD）

> 日本語・英語併記 / Bilingual Format  
> 配置パス：`d_chapter1_memory_technologies/doc_FeRAM/xrd_principle_and_application.md`

---

## 1. 基本原理 / Basic Principles

X線回折（XRD）は、物質にX線を照射したときに特定の角度で強く反射（回折）される現象を利用し、**結晶構造や格子情報**を調べる技術です。

X-ray diffraction (XRD) is a technique that analyzes how X-rays are diffracted by the regular arrangement of atoms in a crystal to reveal information about the **crystal structure and lattice parameters**.

---

## 2. ブラッグの法則 / Bragg’s Law

$$
n\lambda = 2d\sin\theta
$$

- $\lambda$：X線の波長 / X-ray wavelength  
- $d$：結晶面間隔 / Interplanar spacing  
- $\theta$：回折角 / Diffraction angle  
- $n$：回折次数 / Order of diffraction  

This relationship determines the condition for constructive interference from crystal planes.

---

## 3. 測定モード / Measurement Modes

| モード | 内容 / Description |
|-------|---------------------|
| $\theta$–$2\theta$ スキャン | 粉末試料の一般的な測定 / General scan for powders |
| $\omega$ スキャン（ロッキングカーブ） | 配向性・結晶性評価 / Rocking curve for crystal orientation |
| $\phi$ スキャン | 面内配向性の解析 / In-plane orientation |
| HRXRD | 高分解能評価（半導体薄膜）/ High-resolution for strained films |

---

## 4. FeRAM・PZT応用 / Application to FeRAM and PZT

FeRAM（強誘電体メモリ）で用いられるPZT（Pb(Zr,Ti)O₃）などの材料では、XRDにより以下を評価できます：

- 結晶相（ペロブスカイト相など）  
- 軸配向性（(001)/(111) preferred orientation）  
- 残留歪み・格子定数の評価  

XRD is critical for confirming the **ferroelectric phase**, preferred crystal orientation, and **strain in PZT films** used in FeRAM.

---

## 5. ピークとスペクトル例 / Peak Interpretation

- ペロブスカイト構造：明確な (100), (110), (111) ピーク  
- アモルファス材料：広いブロードピーク  

Perovskite-type PZT exhibits sharp peaks at specific angles, while amorphous films show broad humps.

---

## 6. 装置構成 / Instrumentation

- X線源（例：Cu K$\alpha$：1.5406 Å）  
- モノクロメータ / Monochromator  
- ゴニオメータ / Goniometer  
- 検出器 / Detector (1D or 2D)  

---

## 7. 他手法との比較 / Comparison with Other Techniques

| 手法 / Method | 特徴 / Features |
|---------------|------------------|
| XRD | 結晶構造、配向性、歪み |
| TEM | 局所構造、高倍率観察 |
| Raman | 分子結合と化学相 |
| AFM | 表面粗さ、形状評価 |

---

## 8. 演習問題 / Exercises (Optional)

1. ブラッグの法則に基づいて、$d = 3.14$ Å の面が Cu K$\alpha$ X線で回折する角度 $\theta$ を求めよ。  
2. FeRAMにおける配向性評価で、(111)ピークが強い場合の利点を述べよ。

---

*このドキュメントはEdusemiプロジェクトにおけるFeRAM教材の一部です。*
