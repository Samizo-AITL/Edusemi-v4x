module mux_tb;

reg A, B, SEL;
wire Y;

mux2to1 uut (
    .A(A),
    .B(B),
    .SEL(SEL),
    .Y(Y)
);

initial begin
    $dumpfile("mux.vcd");
    $dumpvars(0, mux_tb);

    A = 0; B = 1; SEL = 0; #10;
    SEL = 1;              #10;
    A = 1; B = 0; SEL = 0; #10;
    A = 1; B = 1; SEL = 1; #10;
    $finish;
end

endmodule
