module fsm_engine (
    input  wire        clk,
    input  wire        rst,
    input  wire [3:0]  sensor_in,
    output reg  [2:0]  action_out
);

    typedef enum logic [1:0] {
        IDLE  = 2'b00,
        WALK  = 2'b01,
        TURN  = 2'b10,
        STOP  = 2'b11
    } state_t;

    state_t state, next_state;

    always_ff @(posedge clk or posedge rst) begin
        if (rst)
            state <= IDLE;
        else
            state <= next_state;
    end

    always_comb begin
        case (state)
            IDLE:  next_state = sensor_in[0] ? WALK : IDLE;
            WALK:  next_state = sensor_in[1] ? TURN : WALK;
            TURN:  next_state = sensor_in[2] ? STOP : TURN;
            STOP:  next_state = IDLE;
            default: next_state = IDLE;
        endcase
    end

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
