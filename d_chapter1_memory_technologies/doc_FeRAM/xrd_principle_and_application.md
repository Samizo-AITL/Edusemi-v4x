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
| $\theta$ –2 $\theta$ スキャン | 粉末試料の一般的な測定 / General scan for powders |
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

- X線源（例：Cu K $\alpha$：1.5406 Å）  
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

1. ブラッグの法則に基づいて、 $d = 3.14$ Å の面が Cu K $\alpha$ X線で回折する角度 $\theta$ を求めよ。  
2. FeRAMにおける配向性評価で、(111)ピークが強い場合の利点を述べよ。

---

## 9. 配向率と半値幅 / Orientation Ratio and FWHM

### 📐 配向率（Preferred Orientation）

XRDにおける「配向率」とは、特定の結晶面（例：(111)）がどれだけ優先的に成長しているかを示す指標です。FeRAM用途のPZT薄膜では、(111)面の配向率が高いと、良好な強誘電特性が得られる傾向があります。

Preferred orientation represents how strongly a specific crystal plane (e.g., (111)) is aligned. In FeRAM PZT films, strong (111) orientation often correlates with better ferroelectric performance.

**例 / Example**:

$$
\text{配向率} = \frac{I_{(111)}}{I_{(100)} + I_{(110)} + I_{(111)}}
$$

ここで $I_{(hkl)}$ は各ピークの強度を示します。  
$\text{This ratio}$ compares the intensity of (111) to the total sum of characteristic peaks.

---

### 🎯 半値幅（FWHM: Full Width at Half Maximum）

XRDピークの幅（ $2\theta$ 方向）を半値幅（FWHM）と呼び、結晶の粒径や結晶性を示します。FWHMが小さいほど、結晶性が高いことを示します。

FWHM (in $2\theta$ ) reflects crystallinity and grain size. Narrower peaks indicate higher crystallinity.

**シュラーの式 / Scherrer Equation**:

$$
D = \frac{K \lambda}{\beta \cos \theta}
$$

- $D$：結晶粒サイズ (nm)  
- $K$：形状因子（0.9 が一般的）  
- $\lambda$：X線波長（例：1.5406 Å）  
- $\beta$：半値幅（radian）  
- $\theta$：ブラッグ角  

This equation estimates crystallite size based on peak broadening.

---

*このドキュメントはEdusemiプロジェクトにおけるFeRAM教材の一部です。*
