---
name: hardware-hacking-embedded-security
description: Especialista em Auditoria e Segurança de Hardware, IoT e Sistemas Embarcados baseado nas obras The Hardware Hacking Handbook (Jasper van Woudenberg) e The IoT Hacker's Handbook (Aditya Gupta). Cobre identificação de barramentos físicos (UART, JTAG, SWD, I2C, SPI), extração e dumping de firmware (Flash chips, eMMC, NAND), ataques de injeção de falhas (Fault Injection/Clock & Voltage Glitching), ataques de canal lateral (Side-Channel DPA/CPA) e bypass de Secure Boot.
---

# Auditoria de Segurança de Hardware e IoT (Hardware Hacking)

Esta skill estabelece procedimentos para análise física, extração de firmware, testes não invasivos e avaliação de resiliência de hardware embarcado e dispositivos IoT contra ataques físicos e eletrônicos.

---

## 🔍 1. Reconhecimento Físico da Placa (PCB Reconnaissance)

- **Identificação de Chips**: Leitura de marcações de circuitos integrados (MCU, SoC, Flash SPI, RAM, PMIC).
- **Mapeamento de Pinos de Teste (Test Points & Headers)**:
  - **UART (Universal Asynchronous Receiver-Transmitter)**: Identificação de pinos `GND`, `TX`, `RX`, `VCC` usando multímetro e analisador lógico. Obtenção de console serial / root shell (`baudrate 115200`).
  - **JTAG / SWD**: Identificação de pinos `TMS`, `TCK`, `TDI`, `TDO`, `TRST` via **JTAGulator** ou multímetro. Extração de memória RAM e registradores em tempo de execução via OpenOCD.
  - **SPI / I2C Flash**: Conexão direta com clipes SOIC-8/SOIC-16 e programadores (CH341A, Bus Pirate) para dumping do firmware com `flashrom`.

---

## ⚡ 2. Ataques de Injeção de Falhas e Canal Lateral (Fault Injection & Side-Channel)

| Tipo de Ataque | Mecanismo | Objetivo |
| :--- | :--- | :--- |
| **Voltage Glitching** | Queda abrupta (brownout) na linha de alimentação `VCC` da CPU por alguns nanossegundos. | Pular instruções de validação de assinatura (`CMP` / `JNE`) no bootloader. |
| **Clock Glitching** | Inserção de pulsos de clock anômalos ultra-rápidos. | Corromper registradores e desativar restrições de memória. |
| **DPA (Differential Power Analysis)** | Medição de micro-variações no consumo de corrente elétrica durante operações criptográficas. | Reconstrução de chaves AES/RSA através da correlação matemática de traços de consumo. |
