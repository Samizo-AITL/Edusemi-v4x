---
layout: default
title: ドライバーIC / Driver IC
---

# ⚡ ドライバーIC | Driver IC

高耐圧デバイスの応用例として、パワートランジスタや外部負荷を効率的に制御するための **ドライバーIC** が必須となる。本章では代表的なドライバーICアーキテクチャと設計課題を整理する。

---

## 📌 1. ドライバーICの役割 / Roles
- LDMOS, HV-CMOS, IGBT の **ゲート駆動**  
- **レベルシフト**（低電圧ロジック → 高電圧デバイス制御）  
- **保護機能**（UVLO, OCP, OTP, Shoot-through防止）  

---

## 🔋 2. 主なアーキテクチャ / Architectures
- **High-Side / Low-Side Driver**  
- **Half-Bridge Driver (Bootstrap方式含む)**  
- **Full-Bridge Driver (Hブリッジ駆動)**  
- **絶縁型ゲートドライバ (Photocoupler / Magnetic Isolation / Capacitive Isolation)**  

---

## 🛠 3. 実装上の課題 / Design Challenges
- 高dv/dt耐性 (数10 V/ns)  
- サブストレート電流 / ラッチアップ対策  
- レベルシフト回路の消費電力削減  
- 過電流・短絡時の高速保護  

---

## 🏭 4. 応用例 / Applications
- DC-DCコンバータ制御  
- モータードライバ (BLDC, PMSM, Stepper)  
- パワーアンプ (RF, Audio)  
- インクジェット・圧電駆動回路  

---

## 🔗 5. 参考リンク / References
- IEEE JSSC, TED: Gate Driver Circuit Design  
- 各社アプリケーションノート (TI, Infineon, Rohm, Onsemi)  
