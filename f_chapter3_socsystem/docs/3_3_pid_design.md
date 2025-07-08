# 3.3 PID制御のASIC実装（デジタル／アナログ）

## 🎯 目的と役割

PID制御器は、FSMからの命令（例：歩け、止まれ）に対して、  
対象システム（アクチュエータやセンサ出力）を**安定的に制御**するための理性的制御層です。

AITL-H構造では、中間層として物理実体との橋渡しを行い、  
制御の「応答速度」や「安定性」「フィードバック性」を確保します。

---

## 🧮 PID制御の基本式（離散型）
```
u[k] = Kp * e[k] + Ki * Σ e[k] + Kd * (e[k] - e[k-1])
```
- `e[k] = r[k] - y[k]`: 目標値と現在値の差
- `u[k]`: 出力（アクチュエータ制御量）
- `Kp, Ki, Kd`: 比例・積分・微分ゲイン

---

## ⚙️ デジタルPID制御器のRTL構成

```verilog
module pid_controller (
    input wire clk,
    input wire rst,
    input wire signed [15:0] ref,     // 目標値
    input wire signed [15:0] y,       // 現在値
    output reg signed [15:0] u_out    // 制御出力
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
⚠️ 積分飽和、オーバーフロー制御は別途設計が必要

---

## 🧪 FSMとの連携方式

FSMはシステムの「行動方針」を決定し、PID制御器はそれに従って「物理量」を調整します。  
FSMの `action_out` 信号は、PID制御器の目標値 `ref` に変換されることで接続されます。

| FSM出力（action_out） | 意味 | PIDの目標値 ref |
|------------------------|------|-----------------|
| `3'b001`               | 前進 | `ref = +1000`   |
| `3'b010`               | 旋回 | `ref = -500`    |
| `3'b100`               | 停止 | `ref = 0`       |

> FSMの各状態に応じて、PIDが制御対象へ適切な出力 `u_out` を生成

---

## 🔌 ポート設計と接続

| ポート名 | ビット幅 | 役割 | 接続元・先 |
|----------|----------|------|-------------|
| `ref`    | 16bit    | 目標値（FSM出力に対応） | FSM or LLM |
| `y`      | 16bit    | センサからの現在値 | ADC/センサIF |
| `u_out`  | 16bit    | アクチュエータ制御出力 | PWM / Driver |
| `clk`    | 1bit     | クロック | SoC統合クロック |
| `rst`    | 1bit     | リセット | SoC共通リセット |

---

## 🧪 アナログPIDとの比較（参考）

| 項目       | デジタルPID          | アナログPID               |
|------------|----------------------|----------------------------|
| 実装形式   | HDL（Verilog）      | オペアンプ回路（抵抗・コンデンサ） |
| 精度       | クロック依存（離散） | ノイズや温度に敏感（連続） |
| 柔軟性     | パラメータ変更容易   | 実装後の変更困難           |
| SoC統合性 | 高                    | 低（混載設計や別チップ必要） |

> 教材ではまずデジタルPIDを中心に学習し、アナログPIDは補足的に扱います。

---

## 📝 設計の注意点

- **積分飽和の回避**：`integ`レジスタのビット幅や制限設計
- **固定小数点によるゲイン設計**：スケーリングと右シフト処理を活用
- **FSM→PIDの変換ロジック**：FSMの状態を `ref` に変換する補助モジュールを用意

---

## 📎 次節との接続

次は「**3.4 LLMとの接続設計（RISC-V連携）**」です。  
FSM・PIDに加えて、LLM層がどのように意図決定や外部通信を行うか、  
**メモリマップ方式**や**割り込み制御**を含めて解説します。

---
