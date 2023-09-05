`timescale 1ns / 1ps


module simulacija;

reg clk=0;

source UUT(
.sysclk(clk)
);
always #5 clk=~clk;
endmodule
