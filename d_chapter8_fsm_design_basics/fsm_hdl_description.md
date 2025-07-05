# 💻 VerilogによるFSM記述

---

## 📘 FSMのHDL記述とは

FSM（有限状態機械）の論理構造を、HDL（Hardware Description Language）を使って表現する方法です。  
Verilogでは、状態遷移・出力制御を `always` ブロックで定義します。

---

## 🧩 FSM記述の基本構造（3段構成）

```verilog
module simple_fsm (
  input  wire clk,
  input  wire rst,
  input  wire in,
  output reg  out
);

  typedef enum reg [1:0] {S0, S1, S2} state_t;
  state_t state, next_state;

  // 1. 状態遷移（次状態の決定）
  always @(*) begin
    case (state)
      S0: next_state = in ? S1 : S0;
      S1: next_state = in ? S2 : S1;
      S2: next_state = S0;
      default: next_state = S0;
    endcase
  end

  // 2. 状態の更新（クロック・リセット）
  always @(posedge clk or posedge rst) begin
    if (rst) begin
      state <= S0;
    end else begin
      state <= next_state;
    end
  end

  // 3. 出力の生成（状態に応じて出力制御）
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

## ✅ 記述スタイルのポイント

| 要素 | 説明 |
|------|------|
| `state` / `next_state` | 現在の状態と、次の状態 |
| `always @(*)` | 組み合わせ論理の記述（次状態・出力） |
| `always @(posedge clk)` | 状態の更新（順序回路） |
| `typedef enum` | 状態を列挙型で記述すると可読性が向上 |
| `case文` | 状態ごとの動作分岐 |

---

## 🛠 Tips：記述の型を崩さないこと

- **次状態／出力／状態更新** の3ブロックに分けるのがベストプラクティス
- 状態数が増えると読みづらくなるため、**状態名を意味あるもの**にする
- `default:` を常に書く（合成ツールの警告防止）

---

## 🎓 教材的意義

- FSM設計の“型”を覚えることで、どんな制御回路も記述可能になる
- `タイミング設計`や`検証`との接続が明確になる
- 実践的には、**非同期リセット**や**メタ安定回避**との併用も重要（発展編へ）

---

以上で FSMの基本設計〜記述が完了です。  
次章では、応用事例や検証演習への展開が可能です。

