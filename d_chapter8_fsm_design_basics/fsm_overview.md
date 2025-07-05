# 🔁 FSMの基礎概念と分類

---

## 📘 FSMとは？

FSM（Finite State Machine：有限状態機械）は、入力に応じて状態を遷移しながら、出力を生成する制御回路のモデルです。  
特に、**順序回路の設計**や**プロトコル処理**、**制御信号の生成**など、あらゆるデジタル回路に応用されています。

FSMは主に以下の要素で構成されます：

- `状態`（State）：回路の内部状態（記憶）
- `入力`（Input）：外部から与えられる信号
- `出力`（Output）：状態と入力に基づく制御信号
- `状態遷移`（Transition）：入力に応じて状態が変化

---

## 🔀 Moore型と Mealy型

FSMは、**出力の定義方法**により大きく2つに分類されます。

### ✔️ Moore型 FSM

- 出力は**状態のみに依存**
- 状態ごとに出力が決まる（出力タイミングが安定）
- 実装例：`traffic light controller`, `simple sequence generator`

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

### ✔️ Mealy型 FSM

- 出力は **状態＋入力に依存**
- 状態遷移時に即座に出力が変わる（応答性が高い）
- 実装例：`serial data detector`, `protocol handshake`

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

## 🧠 状態最小化と抽象化

- 状態数が多いと回路が複雑化 → `状態の最小化` が重要
- `状態図`や`状態遷移表`により可視化
- 教育では、「状態＝意味のある動作」として意識的にラベル付けすることで理解が深まる

---

## 🎓 教材的意義

- `順序回路`の基礎として、記憶・遷移・出力の構造的理解が得られる
- `FSM分類（Moore/Mealy）`の使い分けを通して、設計上のトレードオフを学べる
- HDL設計やシミュレーション前の論理整理として有効

---

次は [`fsm_state_transition.md`](./fsm_state_transition.md)：状態遷移図と状態表 に進みます。
