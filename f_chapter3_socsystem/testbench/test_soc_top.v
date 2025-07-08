`timescale 1ns / 1ps

module test_soc_top;

    // クロック・リセット
    reg clk;
    reg rst;

    // 入出力信号
    reg  [3:0]  sensor_in;
    reg  [15:0] y_feedback;
    wire [15:0] actuator_out;

    // DUT instance
    soc_top uut (
        .clk(clk),
        .rst(rst),
        .sensor_in(sensor_in),
        .y_feedback(y_feedback),
        .actuator_out(actuator_out)
    );

    // クロック生成（10ns周期）
    always #5 clk = ~clk;

    initial begin
        $display("Starting testbench...");
        $dumpfile("waveform.vcd");
        $dumpvars(0, test_soc_top);

        // 初期化
        clk = 0;
        rst = 1;
        sensor_in = 4'b0000;
        y_feedback = 16'd0;

        // リセット解除
        #20;
        rst = 0;

        // FSM状態遷移シミュレーション
        #20 sensor_in = 4'b0001; // → WALK状態へ
        #50 sensor_in = 4'b0010; // → TURN状態へ
        #50 sensor_in = 4'b0100; // → STOP状態へ
        #50 sensor_in = 4'b0000; // → IDLEに戻る

        // y_feedback を変化させて PID動作確認
        #20 y_feedback = 16'd900;
        #20 y_feedback = 16'd950;
        #20 y_feedback = 16'd990;

        // シミュレーション終了
        #100;
        $finish;
    end

endmodule
