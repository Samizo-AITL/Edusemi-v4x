module fsm_tb;

reg clk, rst_n, start;
wire flag_done;

fsm uut (
    .clk(clk),
    .rst_n(rst_n),
    .start(start),
    .flag_done(flag_done)
);

initial begin
    clk = 0;
    forever #10 clk = ~clk; // 50MHz相当
end

initial begin
    $dumpfile("fsm.vcd");
    $dumpvars(0, fsm_tb);

    rst_n = 0; start = 0;
    #20 rst_n = 1;         // リセット解除
    #30 start = 1;         // 遷移開始
    #20 start = 0;
    #200 $finish;
end

endmodule
