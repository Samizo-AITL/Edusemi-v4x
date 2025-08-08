---
layout: default
title: "3.3 PID制御のASIC実装（デジタル／アナログ）"
---

# ⚙️ 3.3 PID制御のASIC実装（デジタル／アナログ）  
**Section 3.3: PID Controller Implementation (Digital / Analog)**

---

## 🎯 目的と役割 / Purpose and Role

PID制御器は、FSMからの命令（例：歩け、止まれ）に対して、  
対象システム（アクチュエータやセンサ出力）を**安定的に制御**するための理性的制御層です。  
The PID controller is a rational control layer that stabilizes the system (e.g., actuators, sensors) in response to FSM commands such as "walk" or "stop".

AITL-H構造では、中間層として物理実体との橋渡しを行い、  
制御の「**応答速度**」「**安定性**」「**フィードバック性**」を確保します。  
It bridges digital decision logic with physical systems, ensuring **responsiveness**, **stability**, and **feedback** performance.

---

## 🧮 PID制御の基本式（離散型） / Discrete PID Equation

$$
u[k] = K_p \cdot e[k] + K_i \cdot \sum_{i=0}^{k} e[i] + K_d \cdot (e[k] - e[k-1])
$$

- $e[k] = r[k] - y[k]$: **目標値と現在値の差 / Error (target - actual)**
- $u[k]$: **出力 / Output**
- $K_p, K_i, K_d$: **比例・積分・微分ゲイン / Proportional, Integral, Derivative gains**
  
---

## 🛠️ デジタルPID制御器のRTL構成 / RTL Implementation of Digital PID

```verilog
module pid_controller (
    input wire clk,
    input wire rst,
    input wire signed [15:0] ref,     // 目標値 / reference value
    input wire signed [15:0] y,       // 現在値 / current value
    output reg signed [15:0] u_out    // 制御出力 / control output
);

    parameter signed [15:0] Kp = 16'sd2;
    parameter signed [15:0] Ki = 16'sd1;
    parameter signed [15:0] Kd = 16'sd1;

    reg signed [15:0] e, e_prev, integ, deriv;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            e <= 0;
            e_prev <= 0;
            integ <= 0;
            deriv <= 0;
            u_out <= 0;
        end else begin
            e <= ref - y;
            integ <= integ + e;
            deriv <= e - e_prev;
            u_out <= Kp*e + Ki*integ + Kd*deriv;
            e_prev <= e;
        end
    end
endmodule
```

⚠️ **注意 / Caution**：積分飽和やオーバーフロー制御は別途設計が必要です。  
**Integral windup** and **overflow protection** require additional logic.

---

## 🔄 FSMとの連携 / Connection with FSM

FSMは「行動指令」、PIDは「連続制御」。FSMの `action_out` は、  
PID制御器の目標値 `ref` に変換されて接続されます。  
FSM issues behavior commands, which are converted to reference values (`ref`) for PID control.

| FSM出力 `action_out` | 意味 / Meaning | PIDの目標値 `ref` |
|----------------------|----------------|-------------------|
| `3'b001`             | 前進 / Forward | `+1000`           |
| `3'b010`             | 旋回 / Turn    | `-500`            |
| `3'b100`             | 停止 / Stop    | `0`               |

> PIDはこの `ref` に基づいて `u_out` を生成します。  
> The PID controller generates `u_out` based on `ref`.

---

## 🔌 ポート設計と接続 / Port Design and Integration

| ポート名 | ビット幅 / Bit Width | 説明 / Description | 接続対象 / Connected To |
|----------|----------------------|--------------------|--------------------------|
| `ref`    | 16bit                | 目標値 / Reference | FSM / LLM                |
| `y`      | 16bit                | 現在値 / Measured Value | センサ / Sensor IF |
| `u_out`  | 16bit                | 出力 / Output      | PWM / Driver             |
| `clk`    | 1bit                 | クロック / Clock   | SoC内部クロック / Global Clock |
| `rst`    | 1bit                 | リセット / Reset   | システムリセット         |

---

## ⚖️ アナログPIDとの比較 / Digital vs Analog PID

| 項目 / Aspect    | デジタルPID / Digital PID     | アナログPID / Analog PID               |
|------------------|-------------------------------|----------------------------------------|
| 実装 / Realization | Verilog (HDL)                 | オペアンプ回路 / Op-amp based         |
| 精度 / Accuracy   | 離散・クロック依存 / Discrete | 温度・ノイズ影響あり / Analog noise  |
| 柔軟性 / Flexibility | ゲイン変更容易 / Reconfigurable | 設計固定 / Fixed                      |
| SoC統合 / SoC Integration | 容易 / Easy               | 難しい / Difficult                     |

> デジタルPIDから学び、アナログ実装は補足的に扱います。  
> Begin with digital; analog is for advanced cases.

---

## 📝 設計の注意点 / Design Considerations

- 🧯 **積分飽和対策 / Integral Windup**：積分値の上限・下限設計  
- 🧮 **固定小数点演算 / Fixed-point Arithmetic**：スケーリングとシフト制御  
- 🔄 **FSM→PID変換 / FSM-to-PID Mapping**：補助モジュール設計が必要  

---

## 📎 次節との接続 / To the Next Section

▶️ 次は [**3.4 LLMとの接続設計（RISC-V連携）**](3_4_llm_connection.md) に進みます。  
In the next section, we explore **LLM control integration** including **RISC-V co-design**, memory mapping, and interrupt handling.

---

🔙 [特別編第3章のREADMEに戻る](../README.md)  
