`timescale 1ns/1ps

module stopwatch_tb;
    reg clk, reset, start, stop;
    wire [5:0] sec, min;

    // Instantiate the stopwatch
    stopwatch uut (
        .clk(clk),
        .reset(reset),
        .start(start),
        .stop(stop),
        .sec(sec),
        .min(min)
    );

    // Clock generation: toggle every 5 ns -> 100 MHz
    initial begin
        clk = 0;
        forever #5 clk = ~clk;
    end

    initial begin
        // For GTKWave dump
        $dumpfile("stopwatch.vcd");
        $dumpvars(0, stopwatch_tb);

        // Initialize signals
        reset = 1; start = 0; stop = 0;
        #20 reset = 0;    // Release reset after 20 ns

        #20 start = 1;    // Start counting
        #10 start = 0;    // Pulse style start button

        // Let it run for a while
        #600 stop = 1;    // Stop after ~600 ns
        #10 stop = 0;

        #100 start = 1;   // Start again
        #10 start = 0;

        #300 reset = 1;   // Reset stopwatch
        #20 reset = 0;

        #200 $finish;     // End simulation
    end

    // Display output on console
    initial begin
        $monitor("T=%0t | running=%b | min=%0d | sec=%0d", 
                 $time, uut.running, min, sec);
    end
endmodule
