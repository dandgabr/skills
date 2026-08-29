---
name: academic-control-systems-theory
description: "Especialista em Teoria de Controle Clássico, Moderno, Robótica Industrial e Automação baseada em Katsuhiko Ogata (Modern Control Engineering), John J. Craig (Introduction to Robotics Mechanics and Control) e norma IEC 61131-3. Cobre Lugar das Raízes, Diagramas de Bode/Nyquist, PID Anti-windup, Espaço de Estados, Controlabilidade e Observabilidade de Kalman, Regulador Linear Quadrático (LQR com equação de Riccati ARE), Observadores de Luenberger, Discretização ZOH no Plano Z, Controle Deadbeat, Controle Preditivo Baseado em Modelo (MPC), Filtro de Kalman, Cinemática Direta/Inversa (Denavit-Hartenberg), Jacobiano Robótico, Dinâmica de Lagrange-Euler, ROS 2, SLAM, e Automação com CLPs (Texto Estruturado ST, Ladder LD, SCADA, Modbus, Profinet, OPC-UA)."
---

# Teoria de Controle, Robótica Industrial e Automação (IEC 61131-3)

Esta skill estabelece a fundamentação teórica, formulações matemáticas rigorosas e aplicações práticas de engenharia de controle, modelagem de sistemas dinâmicos, robótica manipuladora e móvel, e automação industrial de processos.

---

## 🎛️ 1. Controle Clássico no Domínio da Frequência

### 1.1 PID com Anti-Windup (Clamping e Back-Calculation)
A lei contínua do controlador PID em forma paralela:
$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) \, d\tau + K_d \frac{de(t)}{dt}$$

```
        ┌─────────────────────────────────────────────────────────────┐
        │                 Saturação do Atuador u_sat                  │
        └──────────────────────────────┬──────────────────────────────┘
                                       │ u_sat - u (Erro de Saturação)
                                       ▼
    e(t) ───[ Ki ]───(+)───[ 1/s ]───(+)───[ u(t) ]───[ Saturação ]───> u_sat(t)
                      ▲               │
                      └───[ 1/Tt ]────┘ (Realimentação Anti-Windup)
```

### 1.2 Critério de Estabilidade de Nyquist
O número de polos de malha fechada no semiplano direito ($Z$) é dado por $Z = N + P$, onde $P$ é o número de polos de malha aberta no semiplano direito e $N$ é o número de voltas no sentido horário que o diagrama de Nyquist $G(s)H(s)$ dá em torno do ponto crítico $(-1 + j0)$.

---

## 🚀 2. Controle Moderno em Espaço de Estados e Controle Ótimo

### 2.1 Modelo Contínuo e Matrizes de Controlabilidade e Observabilidade
$$\dot{\mathbf{x}}(t) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t), \quad \mathbf{y}(t) = \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)$$
- **Controlabilidade**: $\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{AB} & \mathbf{A}^2\mathbf{B} & \cdots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}, \quad \text{posto}(\mathcal{C}) = n$.
- **Observabilidade**: $\mathcal{O} = \begin{bmatrix} \mathbf{C}^T & (\mathbf{CA})^T & (\mathbf{CA}^2)^T & \cdots & (\mathbf{CA}^{n-1})^T \end{bmatrix}^T, \quad \text{posto}(\mathcal{O}) = n$.

### 2.2 Regulador Linear Quadrático (LQR)
Minimiza o funcional quadrático de custo:
$$J = \int_0^\infty \left( \mathbf{x}^T \mathbf{Q} \mathbf{x} + \mathbf{u}^T \mathbf{R} \mathbf{u} \right) dt \implies \mathbf{u}(t) = -\mathbf{K}\mathbf{x}(t), \quad \mathbf{K} = \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P}$$
onde $\mathbf{P} = \mathbf{P}^T > 0$ é a solução única da **Equação Algébrica de Riccati (ARE)**:
$$\mathbf{A}^T \mathbf{P} + \mathbf{P} \mathbf{A} - \mathbf{P} \mathbf{B} \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} + \mathbf{Q} = \mathbf{0}$$

### 2.3 Observador de Estados de Luenberger & Filtro de Kalman
- **Observador de Luenberger**: $\dot{\hat{\mathbf{x}}} = \mathbf{A}\hat{\mathbf{x}} + \mathbf{B}\mathbf{u} + \mathbf{L}(\mathbf{y} - \mathbf{C}\hat{\mathbf{x}})$.
- **Filtro de Kalman Estacionário**: Ganho $\mathbf{L} = \mathbf{P}_e \mathbf{C}^T \mathbf{R}_v^{-1}$, onde $\mathbf{P}_e$ resolve a Riccati de erro com ruídos de processo $\mathbf{Q}_w$ e medição $\mathbf{R}_v$.

---

## 🦾 3. Robótica Industrial, Manipuladores e ROS 2

### 3.1 Transformações Homogêneas de Denavit-Hartenberg (DH)
A matriz de transformação entre elos consecutivos $^{i-1}\mathbf{T}_i$:
$$^{i-1}\mathbf{T}_i = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\
\sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

### 3.2 Dinâmica de Lagrange-Euler e Jacobiano Robótico
- **Equação Dinâmica da Junta**:
  $$\mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau}$$
- **Velocidade Cartesiana do Efetuador**: $\mathbf{v} = \mathbf{J}(\mathbf{q})\dot{\mathbf{q}}$. Singularidades cinemáticas ocorrem quando $\det(\mathbf{J}(\mathbf{q})) = 0$.

---

## 🏭 4. Automação Industrial, CLPs (IEC 61131-3) e Sistemas SCADA

### 4.1 Bloco Funcional em Texto Estruturado (ST - IEC 61131-3)
```iecst
// Bloco Funcional de Controle de Processo com Intertravamento de Segurança
FUNCTION_BLOCK FB_ProcessControl
VAR_INPUT
    bAutoMode     : BOOL;
    rProcessVar   : REAL;
    rSetPoint     : REAL;
    rTolerance    : REAL;
    bEmergencyStop: BOOL;
END_VAR
VAR_OUTPUT
    bActuatorOn   : BOOL;
    bHighAlarm    : BOOL;
    bLowAlarm     : BOOL;
END_VAR

IF bEmergencyStop THEN
    bActuatorOn := FALSE;
    bHighAlarm  := TRUE;
ELSIF bAutoMode THEN
    IF rProcessVar < (rSetPoint - rTolerance) THEN
        bActuatorOn := TRUE;
    ELSIF rProcessVar > (rSetPoint + rTolerance) THEN
        bActuatorOn := FALSE;
    END_IF;
    bHighAlarm := rProcessVar > (rSetPoint + (2.0 * rTolerance));
    bLowAlarm  := rProcessVar < (rSetPoint - (2.0 * rTolerance));
ELSE
    bActuatorOn := FALSE;
END_IF;
END_FUNCTION_BLOCK
```

### 4.2 Protocolos e Redes Industriais
- **Modbus RTU/TCP**: Mapeamento de Coils (`0xxxx`), Discrete Inputs (`1xxxx`), Input Registers (`3xxxx`) e Holding Registers (`4xxxx`).
- **OPC-UA (Open Platform Communications Unified Architecture)**: Comunicação cliente-servidor orientada a objetos com criptografia TLS e certificados X.509 para telemetria em tempo real com sistemas SCADA e MES.
- **Profinet / EtherCAT**: Barramentos Ethernet industriais determinísticos com ciclo de varredura (*jitter*) na escala de microssegundos.
