---
layout: default
title: VerilogによるFSM記述
---

---

# 💻 VerilogによるFSM記述｜*FSM Description in Verilog*

---

## 📘 FSMのHDL記述とは｜*What is FSM HDL Description?*

FSM（有限状態機械）の構造をHDL（Hardware Description Language）で表現する方法です。  
*FSM (Finite State Machine) can be described in HDL such as Verilog for synthesizable hardware logic.*  

Verilogでは、**状態遷移・状態更新・出力制御**をそれぞれ `always` ブロックで記述します。  
*In Verilog, FSMs are typically written in three blocks: **next state logic**, **state update**, and **output logic.***

---

## 🧩 FSM記述の基本構造（3段構成）｜*Three-Part FSM Template in Verilog*

```verilog
module simple_fsm (
  input  wire clk,
  input  wire rst,
  input  wire in,
  output reg  out
);

  typedef enum reg [1:0] {S0, S1, S2} state_t;
  state_t state, next_state;

  // 1. 状態遷移（次状態の決定）｜Next State Logic
  always @(*) begin
    case (state)
      S0: next_state = in ? S1 : S0;
      S1: next_state = in ? S2 : S1;
      S2: next_state = S0;
      default: next_state = S0;
    endcase
  end

  // 2. 状態の更新（クロック・リセット）｜State Update
  always @(posedge clk or posedge rst) begin
    if (rst) begin
      state <= S0;
    end else begin
      state <= next_state;
    end
  end

  // 3. 出力の生成（状態に応じて出力）｜Output Logic
  always @(*) begin
    case (state)
      S0: out = 1'b0;
      S1: out = 1'b1;
      S2: out = 1'b0;
      default: out = 1'b0;
    endcase
  end

endmodule
```

---

## ✅ 記述スタイルのポイント｜*Styling Guidelines*

| **要素｜*Element*** | **説明｜*Description*** |
|------------------|------------------------|
| `state / next_state` | 現在の状態と次状態を明確に区別 <br>*Separate current and next states clearly* |
| `always @(*)` | 組み合わせロジックに必須 <br>*Used for combinational logic* |
| `always @(posedge clk)` | クロック駆動の順序ロジック <br>*Sequential logic triggered by clock* |
| `typedef enum` | 状態名に意味を持たせやすい <br>*Improves readability and maintainability* |
| `case文` | 明確な状態分岐を実現 <br>*Encodes state-dependent behavior clearly* |

---

## 🛠 Tips：記述の型を崩さないこと｜*Tips: Maintain the Template*

- `状態遷移・状態更新・出力制御` を**3つのブロックに分離**  
  *Separate next-state, state-update, and output-control blocks clearly.*  
- 状態名には意味のあるラベルを使う（例：`WAIT`, `DONE`）  
  *Use meaningful labels for states (e.g., `WAIT`, `DONE`).*  
- `default:` 文を常に書く（合成ツールの警告回避）  
  *Always include a `default:` clause to avoid synthesis tool warnings.*  

---

## 🎓 教材的意義｜*Educational Importance*

| 観点｜*Aspect* | 内容｜*Details* |
|---------|----------------------------|
| **型の習得** | FSM構文の型を守ることでどの設計にも応用可能 <br>*Template-based coding applies to any control logic* |
| **タイミング接続性** | STAやCDC設計との接続がしやすくなる <br>*Integrates well with STA and CDC design* |
| **将来の拡張** | メタ安定回避や非同期リセット設計の基礎に <br>*Provides foundation for metastability avoidance and async reset design* |

---

以上で FSMの設計とVerilog記述が完了です。  
*This completes FSM design and its implementation in Verilog.*  

You are now ready to apply FSMs to **control logic, protocols, and sequencers.**  
*FSM concepts can now be applied in practical digital systems.*

---

### 🔁 応用編 第8章：FSM設計（有限状態機械）｜*Applied Chapter 8: FSM Design*  
[➡️ 章の詳細へ進む｜*Go to Chapter*](./README.md)
