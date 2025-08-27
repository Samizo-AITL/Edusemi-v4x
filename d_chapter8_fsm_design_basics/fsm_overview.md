---
layout: default
title: FSMの基礎概念と分類
---

# 🔁 FSMの基礎概念と分類｜*FSM Overview and Classification*

---

## 📘 FSMとは？｜*What is FSM?*

FSM（Finite State Machine：有限状態機械）は、入力に応じて状態を遷移しながら出力を生成する  
**制御回路の抽象モデル**です。  
*FSM is an abstract model of control circuits that generates outputs while transitioning states according to inputs.*  

FSMは、**順序論理設計・プロトコル制御・インターフェース制御**において不可欠な構成要素です。  
*It is essential in sequential logic design, protocol control, and interface control.*  

FSMは以下の4要素で構成されます：  
*FSM consists of the following four elements:*

| 要素｜*Element* | 説明｜*Description* |
|--------|------------------------|
| **状態｜*State*** | 現在の回路の内部状態（記憶） <br>*Current internal memory state* |
| **入力｜*Input*** | 外部から与えられる信号 <br>*Signals from external sources* |
| **出力｜*Output*** | 状態と入力に基づいて生成される制御信号 <br>*Control signals derived from state and input* |
| **状態遷移｜*Transition*** | 条件に応じて状態が変化する規則 <br>*Rules governing how the state changes* |

---

## 🔀 Moore型とMealy型｜*Moore vs. Mealy Models*

FSMは**出力が依存する要素**により、主に以下の2種類に分類されます。  
*FSMs are mainly classified into two types depending on what the outputs depend on.*

---

### ✔️ Moore型 FSM｜*Moore FSM*

- **出力は状態にのみ依存**  
  *Outputs depend only on the state*  
- 出力タイミングが安定しやすい（1クロック遅延あり）  
  *Stable output timing (with one-cycle delay)*  

| 特徴｜*Feature* | 説明｜*Description* |
|--------------|--------------------------|
| **依存関係** | 出力 = f(状態) <br>*Output = f(state)* |
| **応答性** | 遅いが安定（1サイクル後） <br>*Stable but delayed by one cycle* |
| **用途例** | 信号機制御、状態遷移が明確なパターン生成 <br>*Traffic light control, sequence generator* |

#### ✅ 実装例（Moore）｜*Example Implementation (Moore)*

```verilog
always @(posedge clk) begin
  case (state)
    S0: begin
      output_signal <= 1'b0;
      state <= S1;
    end
    S1: begin
      output_signal <= 1'b1;
      state <= S0;
    end
  endcase
end
```

---

### ✔️ Mealy型 FSM｜*Mealy FSM*

- **出力は状態と入力の両方に依存**  
  *Outputs depend on both state and input*  
- 状態遷移時に即座に出力が変化（応答が速い）  
  *Output changes immediately upon state transition (faster response)*  

| 特徴｜*Feature* | 説明｜*Description* |
|--------------|-----------------------------|
| **依存関係** | 出力 = f(状態, 入力) <br>*Output = f(state, input)* |
| **応答性** | 高速応答だが条件分岐が複雑 <br>*Immediate response but more complex conditions* |
| **用途例** | プロトコル検出器、バス制御 <br>*Protocol detectors, bus controllers* |

#### ✅ 実装例（Mealy）｜*Example Implementation (Mealy)*

```verilog
always @(posedge clk) begin
  case (state)
    S0: begin
      if (input_bit) begin
        output_signal <= 1'b1;
        state <= S1;
      end else begin
        output_signal <= 1'b0;
        state <= S0;
      end
    end
  endcase
end
```

---

## 🧠 状態最小化と抽象化｜*State Minimization & Abstraction*

- **状態数が多すぎると設計が煩雑化するため、状態の整理が重要**  
  *Too many states complicate design; minimizing states is important.*  
- **状態遷移表や状態遷移図**を用いて可視化・整理  
  *Use state tables and state diagrams for visualization and simplification.*  
- 教育では、状態に**意味を持たせた命名・ラベル化**が理解を助ける  
  *In education, meaningful naming/labeling of states aids comprehension.*  

---

## 🎓 教材的意義｜*Educational Significance*

| 教育的ポイント｜*Learning Point* | 内容｜*Details* |
|----------------|-----------------------------|
| **構造理解** | 記憶・遷移・出力の構成を明確に学べる <br>*Clear understanding of memory, transitions, and outputs* |
| **分類理解** | Moore / Mealy の比較により応答性と安定性のトレードオフを学習 <br>*Learn trade-offs between response speed and stability* |
| **前処理設計** | HDL実装の前段として設計意図を整理可能 <br>*Organize design intent before HDL implementation* |

---

### 🔁 応用編 第8章：FSM設計（有限状態機械）｜*Applied Chapter 8: FSM Design*  
[➡️ 章の詳細へ進む｜*Go to Chapter*](./README.md)

---

### ⏭️ 次の節へ｜*Next Section*  
[`fsm_state_transition.md`](./fsm_state_transition.md)：状態遷移図と状態遷移表｜*State Diagrams and Transition Tables*
