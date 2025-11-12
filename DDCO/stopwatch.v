module stopwatch (
    input clk,          // clock input (1 Hz or divided clock)
    input reset,        // reset stopwatch
    input start,        // start counting
    input stop,         // stop counting
    output reg [5:0] sec,  // seconds (0–59)
    output reg [5:0] min   // minutes (0–59)
);

    reg running; // keeps track if stopwatch is running

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            // Reset all values
            sec <= 0;
            min <= 0;
            running <= 0;
        end 
        else begin
            // Control logic
            if (start)
                running <= 1;
            else if (stop)
                running <= 0;

            // Time counting
            if (running) begin
                if (sec == 59) begin
                    sec <= 0;
                    if (min == 59)
                        min <= 0;     // reset after 59:59
                    else
                        min <= min + 1;
                end 
                else begin
                    sec <= sec + 1;
                end
            end
        end
    end
endmodule
