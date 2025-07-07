module adder_tb;

reg  [3:0] A, B;
wire [3:0] SUM;
wire       COUT;

adder4 uut (
    .A(A),
    .B(B),
    .SUM(SUM),
    .COUT(COUT)
);

initial begin
    $dumpfile("adder.vcd");
    $dumpvars(0, adder_tb);

    A = 4'b0011; B = 4'b0101; #10;  // 3 + 5 = 8
    A = 4'b1111; B = 4'b0001; #10;  // 15 + 1 = 16 (COUT=1)
    A = 4'b1001; B = 4'b1001; #10;  // 9 + 9 = 18
    $finish;
end

endmodule
