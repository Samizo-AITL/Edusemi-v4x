module fsm (
    input clk,
    input rst_n,
    input start,
    output reg flag_done
);

reg [1:0] state, next_state;

localparam IDLE = 2'b00,
           LOAD = 2'b01,
           EXEC = 2'b10,
           DONE = 2'b11;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n)
        state <= IDLE;
    else
        state <= next_state;
end

always @(*) begin
    next_state = state;
    flag_done = 0;
    case (state)
        IDLE: if (start) next_state = LOAD;
        LOAD: next_state = EXEC;
        EXEC: begin
            next_state = DONE;
            flag_done = 1;
        end
        DONE: next_state = IDLE;
    endcase
end

endmodule
