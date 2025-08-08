---
layout: default
title: 3.4 LLMとの接続設計（RISC-V・I/O連携）　　
---

---

# 🧠 3.4 LLMとの接続設計（RISC-V・I/O連携）  
**Section 3.4: LLM-Based Integration with FSM/PID via RISC-V**

---

## 🧠 LLM層の役割と特徴  
**Role of the LLM Layer**

LLM（Large Language Model）やソフトウェア制御層は、AITL-H構成において以下を担います：

- 🧭 **状況判断**（例：歩く or 立ち止まるかの意図選択）  
- 🗣️ **外部対話・音声認識からの命令変換**  
- ⚙️ **FSM/PIDへの指令・調整・介入**

> 🧩 **LLM = 意思決定層**、FSM/PID = リアルタイム制御層

---

## 🔄 LLM ⇔ FSM・PID の接続方式  
**Communication Methods between LLM and FSM/PID**

| 🛠 接続方式 | 🔍 内容 | 🎯 主な用途 |
|------------|---------|------------|
| **MMIO（Memory Mapped I/O）** | レジスタアクセス型通信 | `llm_action`, `llm_ref` |
| **IRQ（割り込み）** | イベントベース通信 | 緊急停止、状態変更 |
| **UART/I²C** | 外部通信インタフェース | 音声入力・クラウド接続 |

---

## 🧰 メモリマップ設計例（RISC-V ⇔ FSM/PID）  
**Memory Map Example for LLM Control via RISC-V**

| アドレス | 名称 | 説明 |
|----------|------|------|
| `0x0000_0000` | `llm_action` | FSM行動指定（例：TURN） |
| `0x0000_0004` | `llm_ref` | PID目標値の上書き |
| `0x0000_0008` | `llm_mode` | FSM/PIDモード切替（自律/LLM） |
| `0x0000_000C` | `llm_status` | PID制御の状態情報など |

> 🔗 LLMは `lw`, `sw` 命令でアクセス

---

## 🧪 LLM命令フロー（例）  
**Example: LLM-Initiated Control Flow**

> **LLM判断：旋回すべき** → 指令をRISC-VからFSM/PIDに伝達

```assembly
sw 0x0002, 0x0000_0000   # llm_action = TURN
```

```
FSM:    action_out ← llm_action  
PID:    ref ← pre-defined ref for TURN  
Actuator: ← PID(u_out)
```

---

## 🔌 インターフェース信号設計  
**Interface Signal Mapping**

| 信号名 | 方向 | 内容 | 接続先 |
|--------|------|------|--------|
| `llm_action[2:0]` | ⬅️ LLM→FSM | 行動指令 | FSMモジュール |
| `llm_ref[15:0]`   | ⬅️ LLM→PID | PID目標値 | PID制御器 |
| `llm_mode[1:0]`   | ⬅️ LLM→共通制御 | モード切替（自律/指令） | FSM / PID |
| `pid_status[15:0]` | ⬅️ PID→LLM | 応答モニタ | LLM層の判断材料 |

---

## ⚠️ 実装時の注意点  
**Design Considerations**

- ⏱ **非リアルタイム性の意識**：LLMは数ms〜数百msの反応遅れあり
- 🔄 **FSM/PIDの自律動作維持**：LLM介入不能時にも安定制御可能に
- ⏲ **レジスタ同期処理**：LLM（CPU）とFSM/PID（ハード）でドメインが異なる場合、同期FFやFIFOを用意

---

📎 Previous｜前節：  
🔙 [3.3 PID制御のASIC実装（デジタル／アナログ）](3_3_pid_design.md)

📎 Next｜次節：  
👉 [3.5 SoC統合とバス構造・通信設計](3_5_soc_integration.md)  
Integrating all control layers (FSM, PID, LLM) into a **single SoC**, and designing communication using **AXI/APB buses**.

📚 [🔙 特別編 第3章 README に戻る｜Back to Chapter 3 README](../README.md)
