# Verilogファイル自動シミュレーション用Makefile
# 使い方: make SIM=fsm   または SIM=adder4

SIM ?= fsm
TOP = $(SIM)_tb
SRC = src_rtl/$(SIM).v src_tb/$(TOP).v
VCD = $(SIM).vcd

all:
	@echo "▶ Running simulation for: $(SIM)"
	iverilog -o sim.out $(SRC)
	vvp sim.out
	gtkwave $(VCD) &

clean:
	rm -f sim.out *.vcd
