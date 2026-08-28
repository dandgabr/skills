---
name: lang-hdl-verilog-vhdl
description: Fornece padrões de engenharia e descrição de hardware digital utilizando Verilog, SystemVerilog e VHDL baseado nas obras Verilog by Example (Blaine Readler) e VHDL Programming by Example (Douglas Perry). Cobre síntese lógica, máquinas de estado finitas (FSM), testbenches para simulação, registradores, lógica combinacional vs sequencial, e mapeamento para FPGAs (Xilinx/AMD, Intel/Altera, Lattice).
---

# Descrição de Hardware Digital em Verilog e VHDL

Esta skill estabelece diretrizes e boas práticas para projeto e simulação de circuitos digitais síncronos e assíncronos implementados em FPGA e ASIC.

---

## 💻 1. Exemplo: Contador Síncrono de 8 bits com Reset Ativo em Verilog

```verilog
module counter_8bit (
    input  wire       clk,
    input  wire       rst_n,   // Reset assíncrono ativo em nível baixo
    input  wire       enable,
    output reg  [7:0] count
);

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= 8'h00;
        end else if (enable) begin
            count <= count + 1'b1;
        end
    end

endmodule
```

---

## 💻 2. Exemplo: Contador Síncrono em VHDL

```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity counter_8bit is
    Port (
        clk    : in  STD_LOGIC;
        rst_n  : in  STD_LOGIC;
        enable : in  STD_LOGIC;
        count  : out STD_LOGIC_VECTOR (7 downto 0)
    );
end counter_8bit;

architecture Behavioral of counter_8bit is
    signal count_reg : unsigned(7 downto 0) := (others => '0');
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            count_reg <= (others => '0');
        elsif rising_edge(clk) then
            if enable = '1' then
                count_reg <= count_reg + 1;
            end if;
        end if;
    end process;

    count <= std_logic_vector(count_reg);
end Behavioral;
```
