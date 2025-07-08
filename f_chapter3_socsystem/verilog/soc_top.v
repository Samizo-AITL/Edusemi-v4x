module soc_top (
    input  wire        clk,
    input  wire        rst,
    input  wire [3:0]  sensor_in,
    input  wire [15:0] y_feedback,
    output wire [15:0] actuator_out
);

    wire [2:0] action_out;
    wire [15:0] ref;

    // FSM Instance
    fsm_engine fsm_inst (
        .clk(clk),
        .rst(rst),
        .sensor_in(sensor_in),
        .action_out(action_out)
    );

    // Action decoder: convert FSM action to PID ref
    assign ref = (action_out == 3'b001) ? 16'd1000 :   // WALK
                 (action_out == 3'b010) ? -16'd500 :   // TURN
                 16'd0;                                // STOP or IDLE

    // PID Instance
    pid_controller pid_inst (
        .clk(clk),
        .rst(rst),
        .ref(ref),
        .y(y_feedback),
        .u_out(actuator_out)
    );

endmodule
