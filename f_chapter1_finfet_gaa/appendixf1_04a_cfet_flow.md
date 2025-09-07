---
layout: default
title: Appendix F1-04a：CFET 製造プロセスフロー（Sequential Stacked n/p）
---

---

# 📘 CFET 製造プロセスフロー（Sequential Stacked n/p）  
# *CFET Process Flow (Sequential Stacked n/p)*

---

本ドキュメントは、提示いただいた **GAA Multi‑Nanosheet FET 製造プロセスフロー** を基礎に、**CFET（Complementary FET）= nFET と pFET を上下に積層**するための追加工程・変更点を組み込んだ **Sequential CFET** 向けのフローをまとめたものです。  
*This document adapts the provided GAA multi‑nanosheet flow to a **Sequential CFET** where nFET and pFET are vertically stacked, highlighting deltas and added steps.*

> **基本方針 / Policy**：下層（Bottom）を先に完成 → 熱予算を抑えつつ上層（Top）を形成 → **上下を垂直ビアで連結**し「断面=インバータ」を実現。  
> *Finish the bottom device first, then form the top device under tight thermal budget, and connect them with vertical vias so that the cross‑section itself is a CMOS inverter.*

---

## 🔹 前提情報 / Basic Assumptions

| 項目 / Item | 内容（日本語） | Description (English) |
|---|---|---|
| **構造 / Structure** | CFET（GAAナノシートの上下スタック、Bottom=nFET, Top=pFET の一例） | CFET with stacked GAA nanosheets (example: Bottom=nFET, Top=pFET) |
| **適用ノード / Target Node** | 3nm〜1nm世代 | 3nm–1nm nodes |
| **基板 / Substrate** | 300 mm Si (100)、SOIまたはハンドルウェハ | 300 mm Si (100), SOI or handle wafer |
| **チャネル / Channel Stack** | GAAナノシート継承（Si/SiGe多層） | GAA nanosheet (Si/SiGe multilayer) |
| **キー制約 / Key Constraints** | **上下デバイスの熱・ドーピング独立性**、垂直アライメント、コンタクト抵抗 | **Independent thermal/doping**, vertical alignment, contact resistance |

---

## 🧭 フロー全体像 / High‑Level Map

1. **共通前処理**（STI/ウェル/チャネル積層…） → *GAAと同様*  
2. **下層デバイス（例：nFET）完成**（Dummy Gateまで → S/D → HKMG 完了）  
3. **層間絶縁・支持層形成**（Bottom保護 + 上層用フラット化）  
4. **上層デバイス（例：pFET）形成**（低温プロセス徹底）  
5. **垂直ビアで上下接続**（インバータ出力/VDD/GNDの立体配線）  
6. **BEOL配線**（VDD=上層寄り、GND=下層寄り などの最適化）

---

## 🔸 Step 1–10：共通前処理（GAA共通） / Common Front‑End (same as GAA)

GAAフローの **Step 1〜10**（基板準備→Dummy Gate まで）は原則そのまま適用。  
*Apply GAA Steps 1–10 (substrate to dummy gate) as‑is.*

> 以降は **CFET固有の分岐・追加点**のみ記述します（各表の「Δ CFET」欄に差分を明記）。  
> *Below we focus on CFET‑specific deltas.*

---

## 🔸 Step 11：下層 S/D 拡張注入（Bottom）  
*Bottom Source/Drain Extension Implant*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的 / Purpose** | 下層デバイスのSCE抑制 | Suppress SCE of bottom device | 上層形成時の熱を見込んで **やや浅め**に設計 |
| **条件 / Conditions** | B⁺/As⁺、低エネ | Low‑energy implants | 角度注入でシート損傷最小化 |
| **要点 / Key** | 低損傷・浅接合 | Low damage, shallow junction | **Top工程の熱予算**を前提にドーパント拡散を最小化 |

---

## 🔸 Step 12–15：下層 S/D・HKMG 完結（Bottom）  
*Finish Bottom S/D and HKMG*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **S/D Epi** | 20–30 nm 隆起エピ | Raised epi 20–30 nm | 後工程コンタクトの **垂直位置合わせ基準**を刻む |
| **Dummy除去** | 穏和エッチ | Gentle removal | 上層影響を避けるため **表面粗さ最小化** |
| **HKMG** | HfO₂ + TiN/TiAlN | HK + Metal gate | **nFET/pFET別 Work‑Function 設計**を分離管理 |
| **アニール** | Spike RTA | Spike RTA | **Top用低温プロセスに備え**温度履歴を記録 |

> ここまでで **下層デバイスは完成**。以降、**保護＋平坦化**して上層へ。

---

## 🔸 Step 16：下層保護層 / Bottom Protection & Planarization

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | 下層を熱・プラズマから保護し、上層用に平坦化 | Protect bottom device; planarize for top | **SiN/SiO₂積層**＋CMPでフラットに |
| **条件** | SiN/SiO₂、CMP | SiN/SiO₂ with CMP | 保護膜厚は **>50 nm** 目安 |
| **要点** | マーカー維持 | Keep alignment marks | 垂直ビア位置決めの基準保持 |

---

## 🔸 Step 17：上層チャネル堆積 / Top Channel Stack Deposition

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | 上層用 Si/SiGe ナノシート堆積 | Deposit top Si/SiGe nanosheets | **低温RP‑CVD/ALD**を優先 |
| **条件** | Si 5–8 nm / SiGe 10 nm × 3 | Si/SiGe multilayers | 下層ダメージ回避の温度プロファイル |
| **要点** | 界面シャープ | Sharp interfaces | **Top/Bottom Vth 独立**の前提 |

---

## 🔸 Step 18–20：上層パターニング〜SiGe選択除去（Top）  
*Top Patterning & Selective SiGe Etch*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **ハードマスク** | TiN/SiN | TiN/SiN | Bottom保護のエッチ耐性を再確認 |
| **スタックエッチ** | 垂直RIE | Vertical RIE | 下層ダメージ回避の **低バイアス**条件 |
| **SiGe除去** | HCl選択エッチ | HCl selective etch | **Top側ナノギャップ形成**（GAA包囲用） |

---

## 🔸 Step 21：Top 内側スペーサ / Top Inner Spacer

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **堆積** | SiN（ALD/LPCVD） | SiN by ALD/LPCVD | 低温でギャップ均一充填 |
| **要点** | 後工程の精密エッチ | Precise etch control | **上下電極の電気的分離**に直結 |

---

## 🔸 Step 22：Top ダミーゲート / Top Dummy Gate Fill

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | HKMG前の仮ゲート形成 | Temporary gate before HKMG | 低温Poly‑Si + CMP、Bottom熱影響ゼロ化 |

---

## 🔸 Step 23–24：Top S/D 形成（拡張→Epi）  
*Top S/D Extension → Raised Epi*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **拡張注入** | 浅接合 | Shallow junction | **熱拡散を最小化** |
| **Epi** | SiGe/Si 選択エピ | Selective epi | 上層は **より低温**のエピ条件 |

---

## 🔸 Step 25：Top ダミー除去 → HKMG（Top）

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **Dummy除去** | 穏和エッチ | Gentle removal | 下層保護膜の健全性を再確認 |
| **HK** | HfO₂（ALD低温） | HfO₂ by low‑T ALD | **低温高品質誘電体**が鍵 |
| **Metal Gate** | pFET用WFメタル | WF metal for pFET | **n/p でWF分離管理** |

---

## 🔸 Step 26：層間絶縁（Top/Bottom 間） / Inter‑Device Dielectric

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | 上下デバイスの電気・熱分離 | Electrical/thermal separation | SiO₂/SiN積層で **熱クロストーク緩和** |
| **条件** | 低温PECVD | Low‑T PECVD | 後続のビアエッチ選択比を確保 |

---

## 🔸 Step 27：垂直ビア開口（Output/VDD/GND）  
*Vertical Via Definition (Output, VDD, GND)*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | **n/p の上下直結**（インバータ出力）および電源ビア形成 | Form vias for vertical n/p connection (inverter output) and supplies | **断面=インバータ** を成立させる最重要工程 |
| **条件** | 高選択RIE + エッチストップ | High‑selectivity RIE with stop layer | **ミスアライメント許容**を小さく設計 |
| **要点** | 抵抗・寄生の最小化 | Minimize R and parasitics | ビア形状最適化（アスペクト比/ライナー） |

---

## 🔸 Step 28：ビアバリア・シード → Cu埋込 → CMP  
*Via Barrier/Seed → Cu Fill → CMP*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **バリア/シード** | TaN/TiN + Cu | TaN/TiN + Cu seed | 高アスペクト比充填の成否が **遅延**に直結 |
| **ECP** | ボイドレス充填 | Void‑free ECP | 出力ビアは **最短・最太**で抵抗最小 |
| **CMP** | エンドポイント厳密 | Tight endpoint | ビアの開口上面をフラットに |

---

## 🔸 Step 29：コンタクト & M1（局所配線）  
*Contacts & M1 (Local Interconnect)*

| 項目 | 日本語 / Japanese | 英語 / English | Δ CFET |
|---|---|---|---|
| **目的** | 出力ノード/VDD/GND の局所配線 | Local routing of OUT/VDD/GND | **VDD=上層寄り、GND=下層寄り**配置が有利 |
| **条件** | ArF/EUV + RIE | ArF/EUV + RIE | インバータ出力は **最短経路**でM1へ |
| **要点** | RC最小 | Minimize RC | セル境界条件（標準セル設計）に適合 |

---

## 🔸 Step 30〜：上位配線（M2〜Mx）/ BEOL（GAA準拠）

以降は **GAAフロー（Step 31〜48）** に準拠して多層配線・パッシベーション・パッケージングへ。  
*Proceed with standard BEOL per GAA Steps 31–48.*

---

## 🧪 品質・信頼性チェック / Quality & Reliability

- **上下Vtの独立性**（WFメタル・ドーピング・応力の相互影響をモニタ）  
  *Independence of top/bottom Vt*  
- **熱クロストーク評価**（パルス通電時の温度上昇分布）  
  *Thermal crosstalk under pulsed bias*  
- **垂直ビア抵抗/ばらつき**（RC遅延・セル速度のボトルネック）  
  *Vertical via resistance/variation*  
- **信頼性**：BTI/HCI/EM の上下差分評価  
  *Reliability: BTI, HCI, EM per layer*

---

## 📝 付記 / Notes

- 本フローは **教育・設計検討用**の概念手順です。装置条件・材料・温度は実ラインに合わせて適宜最適化してください。  
- **Forksheet‑CFET**（直交配置）や **混載（Top/Bottomの極性入替）** などの派生フローは別紙で扱えます。

---

[← 戻る / Back to Special Chapter 1 Top](../f_chapter1_finfet_gaa/README.md)
