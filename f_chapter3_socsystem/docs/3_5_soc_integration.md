# 3.5 SoC統合とバス構造・通信設計

## 🧩 統合設計の目的

FSM・PID・LLMの三層制御モジュールを、1つのSoCとして統合する際に必要な設計は：

- 各モジュールの**明確な役割分離とインターフェース定義**
- **通信バス**を用いたモジュール間接続（AXI, APB等）
- トップモジュールでの**接続スケーラビリティの確保**

---

## 🏗 SoC全体構成ブロック図（概念）
```
    +-----------------------------+
    |           SoC Top          |
    |                             |
    |   +---------+   +--------+  |
    |   |   FSM   |←→|  PID    |  |
    |   +----+----+   +--------+  |
    |        ↑                ↑   |
    |        | action_out     | u_out
    |        ↓                ↓
    |     +-----------------------+
    |     |      LLM Interface    | ←→ RISC-V CPU
    |     +-----------------------+
    |            ↑   ↑
    |         MMIO  IRQ
    +-----------------------------+

    ---
```

---

## 📡 バス接続方式の選択肢

| バス種別 | 用途 | メリット | 備考 |
|----------|------|----------|------|
| AXI4 | 高速SoC設計全般 | 高帯域・複数マスター対応 | LLM/RISC-V ↔ MMIO |
| APB | 周辺デバイス制御 | 簡易構成・低電力 | FSM, PID 接続に適 |

> 教材設計では、「RISC-Vマスター + AXI + APBブリッジ + FSM/PIDスレーブ」の構成を推奨

---

## 🔄 接続モジュールと信号整理

| モジュール | 主なポート | 接続先 |
|------------|------------|--------|
| FSM | `clk`, `rst`, `sensor_in`, `action_out` | Top, Sensor, PID |
| PID | `clk`, `rst`, `ref`, `y`, `u_out` | FSM, Actuator |
| LLM I/F | `llm_action`, `llm_ref`, `mode` | RISC-V ↔ FSM/PID |
| RISC-V SoC | AXI Master | LLM I/F経由で制御 |

---

## ⚙️ トップモジュールの設計例（抜粋）

```verilog
module soc_top (
    input wire clk,
    input wire rst,
    input wire [3:0] sensor_data,
    input wire [15:0] y_feedback,
    output wire [15:0] actuator_out
);
    // FSMインスタンス
    wire [2:0] action_out;
    fsm_engine fsm_inst (
        .clk(clk),
        .rst(rst),
        .sensor_in(sensor_data),
        .action_out(action_out)
    );

    // PIDインスタンス
    wire [15:0] ref;
    pid_controller pid_inst (
        .clk(clk),
        .rst(rst),
        .ref(ref),
        .y(y_feedback),
        .u_out(actuator_out)
    );

    // LLM I/F（MMIO接続想定）
    llm_interface llm_if (
        .llm_action_in(mmio_action),
        .llm_ref_in(mmio_ref),
        .fsm_action_out(action_out),
        .pid_ref_out(ref)
    );

endmodule
```

---

## 📝 統合設計の注意点
	•	バスクロックと制御クロックのドメイン整合
	•	MMIO制御はレイテンシ許容設計
	•	モジュール間は中間バッファリングやFIFO設計も検討

---

## 📎 次節との接続

次は「3.6 ケーススタディ：三層制御によるPoC実装例」です。
実際にこのSoC構成をもとに、FSM×PID×LLMによる倒立振子やロボット制御のPoC実装事例を紹介します。

---
