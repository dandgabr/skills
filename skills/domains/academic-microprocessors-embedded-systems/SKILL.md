---
name: academic-microprocessors-embedded-systems
description: Especialista em Arquitetura de Microprocessadores e Sistemas Embarcados baseado na obra Computer Organization and Design (Patterson, Hennessy). Cobre microcontroladores ARM Cortex-M/A, RISC-V, Assembly, Pipelines com Forwarding e Previsão de Desvio, Hierarquia de Memória Cache (L1/L2/L3), Barramentos Industriais (UART, SPI, I2C, CAN, USB), Timers, DMA e RTOS (FreeRTOS, Zephyr).
---

# Microprocessadores, Arquitetura RISC-V e Sistemas Embarcados

Esta skill estabelece as diretrizes para desenvolvimento de firmware de baixo nível, controle de periféricos por hardware e projeto de microprocessadores com pipeline.

---

## 💻 1. Pipeline de 5 Estágios (IF, ID, EX, MEM, WB)

```
[ IF: Busca de Instrução ] ──> [ ID: Decodificação & Registradores ]
                            ──> [ EX: Execução na ULA / Branch ]
                            ──> [ MEM: Acesso à Memória de Dados ]
                            ──> [ WB: Escrita de Retorno no Registrador ]
```

- **Mitigação de Hazards**:
  - *Hazard Estrutural*: Caches separadas de Instrução e Dados (Arquitetura Harvard).
  - *Hazard de Dados*: Encaminhamento direto de dados (*Data Forwarding*) da saída da ULA/MEM para a entrada da ULA do estágio seguinte.
  - *Hazard de Controle*: Preditor dinâmico de desvios (Branch Predictor) de 2 bits.
