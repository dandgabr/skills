---
name: academic-digital-systems-vlsi
description: Especialista em Sistemas Digitais, Síntese Lógica e Projeto de Circuitos Integrados VLSI baseado nas obras Digital Design (Morris Mano) e CMOS VLSI Design (Weste, Harris). Cobre FPGAs (Xilinx AMD, Intel Altera), síntese em VHDL/Verilog/SystemVerilog, Máquinas de Estados Finitas (FSM Moore/Mealy), Static Timing Analysis (STA), Layout CMOS, Regras DRC/LVS e Design for Testability (DFT - Scan Chains, BIST).
---

# Sistemas Digitais Avançados e Projeto VLSI / CMOS

Esta skill estabelece a metodologia de ponta a ponta para síntese e verificação de hardware digital síncrono para implantação em FPGAs e fabricação de chips ASIC.

---

## 📐 1. Análise Estática de Temporização (Static Timing Analysis - STA)

Para que um circuito síncrono opere sem metastabilidade em frequência $f = 1/T_{clk}$:
- **Condição de Setup Time ($t_{setup}$)**:
  $$T_{clk} \ge t_{cq} + t_{comb, max} + t_{setup} - t_{skew}$$
- **Condição de Hold Time ($t_{hold}$)**:
  $$t_{cq} + t_{comb, min} \ge t_{hold} + t_{skew}$$

---

## 🔬 2. Inversor CMOS e Modelo RC de Elmore

Tempo de atraso de propagação de um gate CMOS:
$$t_{pd} \approx 0.69 \cdot R_{eq} C_L$$
