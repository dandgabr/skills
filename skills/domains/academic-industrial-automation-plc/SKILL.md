---
name: academic-industrial-automation-plc
description: Especialista em Automação Industrial e Controle de Processos baseado na norma IEC 61131-3. Cobre Controladores Lógicos Programáveis (CLPs), Linguagens Ladder (LD), Texto Estruturado (ST), Diagrama de Blocos Funcionais (FBD), Sistemas SCADA/Supervisórios, Redes Industriais (Profinet, Modbus RTU/TCP, OPC-UA, EtherCAT) e Instrumentação Industrial.
---

# Automação Industrial, CLPs (IEC 61131-3) e Sistemas SCADA

Esta skill estabelece padrões rigorosos para engenharia de controle contínuo e discreto em ambientes fabris e Indústria 4.0.

---

## 🏭 1. Linguagens de Programação IEC 61131-3 (Texto Estruturado - ST)

```iecst
// Bloco Funcional de Controle de Nível de Tanque com Histerese
FUNCTION_BLOCK FB_LevelControl
VAR_INPUT
    bAutoMode    : BOOL;
    rCurrentLevel: REAL;
    rSetPoint    : REAL;
    rHysteresis  : REAL;
END_VAR
VAR_OUTPUT
    bPumpCommand : BOOL;
    bAlarmHigh   : BOOL;
END_VAR

// Lógica de Operação
IF bAutoMode THEN
    IF rCurrentLevel <= (rSetPoint - rHysteresis) THEN
        bPumpCommand := TRUE;
    ELSIF rCurrentLevel >= (rSetPoint + rHysteresis) THEN
        bPumpCommand := FALSE;
    END_IF;
    bAlarmHigh := rCurrentLevel >= (rSetPoint + (2.0 * rHysteresis));
ELSE
    bPumpCommand := FALSE;
END_IF;
END_FUNCTION_BLOCK
```
