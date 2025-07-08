module pid_controller (
    input  wire             clk,
    input  wire             rst,
    input  wire signed [15:0] ref,
    input  wire signed [15:0] y,
    output reg  signed [15:0] u_out
);

    parameter signed [15:0] Kp = 16'sd2;
    parameter signed [15:0] Ki = 16'sd1;
    parameter signed [15:0] Kd = 16'sd1;

    reg signed [15:0] e, e_prev, integ, deriv;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            e      <= 0;
            e_prev <= 0;
            integ  <= 0;
            deriv  <= 0;
            u_out  <= 0;
        end else begin
            e      <= ref - y;
            integ  <= integ + e;
            deriv  <= e - e_prev;
            u_out  <= Kp*e + Ki*integ + Kd*deriv;
            e_prev <= e;
        end
    end

endmodule
