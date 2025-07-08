# 3.2 FSM設計とRTLモジュール構成

## 🧠 FSM（Finite State Machine）の役割

FSMは、AITL-Hにおける「**本能的行動制御**」を担う層であり、  
環境入力に応じて状態遷移を行い、定型的かつ瞬時な行動を生成します。

---

## ⚙️ 状態遷移モデルの設計手順

1. **行動仕様の分解**
   - ロボットの立ち上がり、旋回、停止などを**状態単位で分割**
2. **状態と遷移条件の定義**
   - 各状態とその間を結ぶ**トリガ条件（入力信号）**を定義
3. **状態遷移図（State Diagram）作成**
   - `start → walking → turning → stop` などのパターンを図示
4. **状態符号（state encoding）の決定**
   - Binary, One-hotなどの方式を選定

---

## 🧩 RTLモジュール構成（例：fsm_engine.v）

```verilog
module fsm_engine (
    input wire clk,
    input wire rst,
    input wire [3:0] sensor_in,
    output reg [2:0] action_out
);

    typedef enum logic [1:0] {
        IDLE  = 2'b00,
        WALK  = 2'b01,
        TURN  = 2'b10,
        STOP  = 2'b11
    } state_t;

    state_t state, next_state;

    // 状態遷移ロジック
    always_ff @(posedge clk or posedge rst) begin
        if (rst)
            state <= IDLE;
        else
            state <= next_state;
    end

    // 遷移条件
    always_comb begin
        case (state)
            IDLE:  next_state = sensor_in[0] ? WALK : IDLE;
            WALK:  next_state = sensor_in[1] ? TURN : WALK;
            TURN:  next_state = sensor_in[2] ? STOP : TURN;
            STOP:  next_state = IDLE;
            default: next_state = IDLE;
        endcase
    end

    // 出力生成
    always_comb begin
        case (state)
            IDLE:  action_out = 3'b000;
            WALK:  action_out = 3'b001;
            TURN:  action_out = 3'b010;
            STOP:  action_out = 3'b100;
            default: action_out = 3'b000;
        endcase
    end

endmodule
```
💡 本テンプレートは verilog/fsm_engine.v に実装されます。

---

## 🔌 AITL構成との接続例（ポート設計）

FSMモジュールは、AITL-Hアーキテクチャにおいて**上下の層と信号レベルで接続**されます。以下に、典型的な接続構成を示します。

| 信号名 | ビット幅 | 説明 | 接続先 |
|--------|----------|------|--------|
| `clk` | 1bit | システムクロック | SoC共通 |
| `rst` | 1bit | 非同期リセット | SoC共通 |
| `sensor_in` | 4bit | センサ状態入力 | PID層 または センサIF |
| `action_out` | 3bit | 行動制御信号 | PID層 または アクチュエータIF |

> 備考：`action_out` は、状態に応じて PID制御器に「行動種別」を通知する制御信号（例：歩行、旋回、停止など）

---

## 📝 補足：FSM設計の設計指針

- 状態数は**4〜8程度**を基本とし、階層型FSM（HFSM）で拡張可能
- 条件分岐が複雑・非決定的な場合は**LLM側に判断を委譲**する
- `case`文で状態ごとの**明示的な遷移定義**を記述する
- 状態は `enum` を用いて**読みやすさと検証容易性を確保**

---

## 🔄 AITL-H内部の信号流れ（簡易図）
```
センサ入力
↓ sensor_in
[FSM層]── action_out ──▶[PID層]── ctrl_out ──▶ Actuator
▲
│
LLM層 ←─ command_in / feedback
```
> FSMは「反射的行動」、PIDは「連続的制御」、LLMは「状況判断と介入」

---

## 📎 次節との接続

次の「**3.3 PID制御のASIC実装**」では、本FSMから出力された `action_out` をもとに、  
**PID制御器がどのように物理挙動を安定化させるか**をRTL視点・SoC統合視点から解説します。

---

