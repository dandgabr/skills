---
name: academic-digital-systems-vlsi
description: "Especialista em Sistemas Digitais, Síntese Lógica, Descrição de Hardware (Verilog, SystemVerilog, VHDL) e Projeto de Circuitos Integrados VLSI/CMOS baseado em Morris Mano (Digital Design), Weste & Harris (CMOS VLSI Design), Blaine Readler e Douglas Perry. Cobre síntese RTL, máquinas de estados finitas (FSM Moore/Mealy), testbenches para simulação, Static Timing Analysis (STA - Setup/Hold times, Clock Skew, Jitter), modelo RC de Elmore, layout CMOS, regras DRC/LVS, mapeamento para FPGAs (AMD Xilinx Vivado, Intel Altera Quartus) e Design for Testability (DFT - Scan Chains, BIST)."
---

# Sistemas Digitais, Síntese Lógica, HDL (Verilog/VHDL) e Projeto VLSI

Esta skill estabelece a metodologia unificada de engenharia para modelagem, descrição em hardware (RTL), simulação funcional, análise estática de temporização e síntese de circuitos integrados ASIC e FPGAs baseada nas obras de **Morris Mano** (*Digital Design*) e **Neil Weste & David Harris** (*CMOS VLSI Design*).

---

## 💻 1. Descrição de Hardware RTL: Verilog, SystemVerilog & VHDL

### 1.1 Contador Síncrono com Reset Assíncrono em Verilog / SystemVerilog
```verilog
// SystemVerilog IEEE 1800-2017
module counter_8bit (
    input  logic       clk,
    input  logic       rst_n,   // Reset assíncrono ativo em nível baixo (low-active)
    input  logic       enable,
    output logic [7:0] count
);

    always_ff @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            count <= 8'h00;
        end else if (enable) begin
            count <= count + 1'b1;
        end
    end

endmodule
```

### 1.2 Máquina de Estados Finitos (FSM Moore) em VHDL
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fsm_moore is
    Port (
        clk    : in  STD_LOGIC;
        rst_n  : in  STD_LOGIC;
        din    : in  STD_LOGIC;
        dout   : out STD_LOGIC
    );
end entity fsm_moore;

architecture Behavioral of fsm_moore is
    type state_type is (STATE_IDLE, STATE_ACTIVE, STATE_DONE);
    signal current_state, next_state : state_type;
begin

    -- Processo Sequencial de Transição de Estado
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            current_state <= STATE_IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;

    -- Lógica Combinacional de Próximo Estado e Saída
    process(current_state, din)
    begin
        case current_state is
            when STATE_IDLE =>
                dout <= '0';
                if din = '1' then next_state <= STATE_ACTIVE; else next_state <= STATE_IDLE; end if;
            when STATE_ACTIVE =>
                dout <= '1';
                next_state <= STATE_DONE;
            when STATE_DONE =>
                dout <= '0';
                next_state <= STATE_IDLE;
        end case;
    end process;

end architecture Behavioral;
```

---

## 📐 2. Análise Estática de Temporização (Static Timing Analysis - STA)

Para evitar condições de corrida (*race conditions*) e metastabilidade em registradores alimentados por clock com período $T_{clk} = 1/f_{clk}$:

```
Flip-Flop 1 (Lauch) ──[t_cq]──> [ Lógica Combinacional t_comb ] ──> [t_setup/t_hold]──> Flip-Flop 2 (Capture)
      │                                                                                        │
      └──────────────────────────[ Clock Skew t_skew ]─────────────────────────────────────────┘
```

1. **Condição de Setup Time (Tempo de Estabelecimento)**:
   $$T_{clk} \ge t_{cq} + t_{comb, max} + t_{setup} - t_{skew} + t_{jitter}$$
   - *Violação de Setup*: Ocorre quando o caminho combinacional é excessivamente longo. Solução: Inserção de registradores intermediários (*Pipelining*).
2. **Condição de Hold Time (Tempo de Retenção)**:
   $$t_{cq} + t_{comb, min} \ge t_{hold} + t_{skew}$$
   - *Violação de Hold*: Depende exclusivamente dos atrasos mínimos e não pode ser corrigida reduzindo a frequência de clock. Solução: Inserção de buffers de atraso na rota de dados.

---

## 🔬 3. Projeto Físico CMOS, Layout e Regras DRC/LVS

- **Modelo de Atraso RC de Elmore**:
  $$t_{pd} \approx \sum_{i} R_i \cdot C_i \approx 0.69 \cdot R_{eq} C_L$$
- **Regras Geométricas de Fabricação (DRC - Design Rule Checking)**: Espaçamento mínimo entre difusões, sobreposição de polissilício e largura mínima de trilhas de metal ($M1-Mn$).
- **LVS (Layout Versus Schematic)**: Extração de netlist parasítica ($R, C$) a partir do layout físico e verificação 1:1 de equivalência lógica contra o esquemático SPICE.
- **Design for Testability (DFT)**: Inserção automática de *Scan Chains* e geradores/analisadores de padrões de teste embutidos (*BIST - Built-In Self-Test*) para atingir cobertura de falhas por *Stuck-at Faults* $> 99\%$.
