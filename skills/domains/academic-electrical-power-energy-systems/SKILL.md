---
name: academic-electrical-power-energy-systems
description: Especialista em Sistemas Elétricos de Potência (SEP), Geração, Transmissão e Distribuição de Energia, Máquinas Elétricas Girantes e Eletrônica de Potência baseado nas obras Power System Analysis (Grainger, Stevenson), Electric Machinery (Fitzgerald, Kingsley), Power Electronics (Rashid) e normas ABNT/IEEE/IEC. Cobre Matrizes de Admitância/Impedância (Ybus, Zbus), Fluxo de Potência (Newton-Raphson, Desacoplado Rápido), Cálculo de Curto-Circuito Simétrico e Assimétrico (Componentes Simétricas de Fortescue), Proteção Digital de Sistemas Elétricos (Funções ANSI 50/51, 21, 87 e Norma IEC 61850), Máquinas Síncronas e de Indução, Transformadores de Potência, Instalações Elétricas BT/MT (ABNT NBR 5410 e NBR 14039), Eletrônica de Potência e Inversores Trifásicos (SVPWM, Conversores SiC/GaN), Redes Elétricas Inteligentes (Smart Grids, Microrredes, Armazenamento BESS) e Simulação Multifísica/Eletromagnética (OpenDSS, FEMM).
---

# Sistemas Elétricos de Potência, Máquinas e Energia (Grainger & Stevenson)

Esta skill estabelece a engenharia de análise em regime permanente e dinâmico de redes elétricas de alta, média e baixa tensão, modelagem e controle de máquinas elétricas girantes, dimensionamento de conversores estáticos de potência e automação de subestações sob a norma IEC 61850.

---

## ⚡ 1. Análise de Redes Elétricas e Fluxo de Potência (*Power Flow*)

### 1.1 Formulação Matricial da Rede e Equações de Barra
A relação entre as correntes nodais injetadas $\mathbf{I}_{bus}$ e as tensões complexas de barra $\mathbf{V}_{bus}$ é regida pela Matriz de Admitância Nodal $\mathbf{Y}_{bus}$:

$$\mathbf{I}_{bus} = \mathbf{Y}_{bus} \mathbf{V}_{bus}$$

- **Elementos da Matriz $\mathbf{Y}_{bus}$**:
  - $Y_{ii} = \sum_{k \in \Omega_i} y_{ik} + y_{sh,i}$ (Soma de todas as admitâncias conectadas à barra $i$)
  - $Y_{ij} = -y_{ij}$ (Negativo da admitância série entre as barras $i$ e $j$)

### 1.2 Algoritmo de Newton-Raphson para Fluxo de Carga
As equações de injeção de potência ativa $P_i$ e reativa $Q_i$ na barra $i$ ($V_i = |V_i| e^{j\theta_i}$):

$$P_i = |V_i| \sum_{k=1}^N |V_k| |Y_{ik}| \cos(\theta_i - \theta_k - \gamma_{ik})$$
$$Q_i = |V_i| \sum_{k=1}^N |V_k| |Y_{ik}| \sin(\theta_i - \theta_k - \gamma_{ik})$$

- **Sistema Linearizado da Matriz Jacobiana**:
  $$\begin{bmatrix} \Delta \mathbf{P} \\ \Delta \mathbf{Q} \end{bmatrix} = \begin{bmatrix} \mathbf{J}_1 & \mathbf{J}_2 \\ \mathbf{J}_3 & \mathbf{J}_4 \end{bmatrix} \begin{bmatrix} \Delta \boldsymbol{\theta} \\ \Delta |\mathbf{V}|/|\mathbf{V}| \end{bmatrix} = \begin{bmatrix} \frac{\partial \mathbf{P}}{\partial \boldsymbol{\theta}} & \frac{\partial \mathbf{P}}{\partial |\mathbf{V}|} |\mathbf{V}| \\ \frac{\partial \mathbf{Q}}{\partial \boldsymbol{\theta}} & \frac{\partial \mathbf{Q}}{\partial |\mathbf{V}|} |\mathbf{V}| \end{bmatrix} \begin{bmatrix} \Delta \boldsymbol{\theta} \\ \Delta |\mathbf{V}|/|\mathbf{V}| \end{bmatrix}$$

---

## 🛡️ 2. Curto-Circuito, Componentes Simétricas e Proteção Digital

### 2.1 Teorema de Fortescue e Redes de Sequência
Qualquer sistema trifásico desequilibrado de fasores de tensão/corrente é decomposto em três sistemas simétricos desacoplados: Sequência Positiva ($1$), Negativa ($2$) e Zero ($0$):

$$\begin{bmatrix} \mathbf{V}_a \\ \mathbf{V}_b \\ \mathbf{V}_c \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix} \begin{bmatrix} \mathbf{V}_0 \\ \mathbf{V}_1 \\ \mathbf{V}_2 \end{bmatrix}, \quad \text{onde } a = e^{j 120^\circ} = -\frac{1}{2} + j\frac{\sqrt{3}}{2}$$

- **Interconexão de Redes de Sequência por Tipo de Falta**:
  1. **Falta Trifásica Simétrica (3F)**: Apenas a rede de sequência positiva atua: $I_{f1} = \frac{V_{th}}{Z_{1,th} + Z_f}$.
  2. **Falta Fase-Terra (1FT)**: Redes em Série ($1$, $2$, $0$): $I_{f1} = I_{f2} = I_{f0} = \frac{V_{th}}{Z_{1,th} + Z_{2,th} + Z_{0,th} + 3Z_f}$.
  3. **Falta Fase-Fase (2F)**: Redes Positiva e Negativa em Paralelo ($Z_{1,th} \parallel Z_{2,th}$).
  4. **Falta Dupla Fase-Terra (2FT)**: Redes Positiva, Negativa e Zero em Paralelo.

### 2.2 Filosofia de Proteção e Norma IEC 61850
```
Principais Funções ANSI de Proteção:
├── ANSI 50/51: Sobrecorrente Instantânea e Temporizada (Curvas IEC/IEEE)
├── ANSI 50N/51N: Sobrecorrente de Neutro / Residual de Terra
├── ANSI 21: Proteção de Distância Mho / Quadrilateral (Zonas Z1: 80-85%, Z2: 120%, Z3 reversa)
├── ANSI 87: Proteção Diferencial Percentual (87T Transformadores com restrição harmônica 2ª/5ª, 87B Barramentos)
└── ANSI 27/59: Subtensão e Sobretensão

Arquitetura de Subestações Digitais (IEC 61850):
├── Process Bus: Tráfego de Sampled Values (SV - IEC 61850-9-2LE a 4800/4000 Hz) e GOOSE (mensagens de trip < 3 ms)
└── Station Bus: Tráfego MMS para Sistemas SCADA e sincronização temporal IEEE 1588 PTP (Precision Time Protocol)
```

---

## 🔄 3. Máquinas Elétricas e Transformadores de Potência

### 3.1 Transformadores de Potência Trifásicos
- **Circuito Equivalente Referido ao Primário**:
  - Parâmetros do Ensaio a Vazio: Resistência de perdas no ferro $R_c = \frac{V_{1}^2}{P_0}$ e Reatância de magnetização $X_m = \frac{V_{1}^2}{Q_0}$.
  - Parâmetros do Ensaio de Curto-Circuito: Resistência equivalente $R_{eq} = \frac{P_{cc}}{I_{cc}^2}$ e Reatância de dispersão $X_{eq} = \sqrt{Z_{cc}^2 - R_{eq}^2}$.
- **Grupos de Ligação**: Dyn11 (Delta primário, Estrela com neutro secundário defasado em $+30^\circ$), YNd1, YNy0.

### 3.2 Máquinas Síncronas e de Indução
- **Gerador Síncrono de Polos Salientes (Teoria de Duas Reações de Blondel)**:
  $$P = \frac{E_f V}{X_d} \sin\delta + \frac{V^2 (X_d - X_q)}{2 X_d X_q} \sin(2\delta)$$
  onde o segundo termo representa o torque de relutância.
- **Motor de Indução Trifásico (MIT)**:
  - Escorregamento: $s = \frac{n_s - n_r}{n_s}$
  - Equação de Torque Eletromagnético (Kloss):
    $$T = \frac{3 R_2' / s}{\omega_s \left[ (R_1 + R_2'/s)^2 + (X_1 + X_2')^2 \right]} V_{1,th}^2$$

---

## 🔌 4. Eletrônica de Potência e Inversores Trifásicos (SVPWM)

### 4.1 Modulação por Vetor Espacial (Space Vector PWM - SVPWM)
Em inversores de fonte de tensão (VSI) trifásicos com 6 chaves semicondutoras IGBT/SiC, o vetor de tensão de referência $\mathbf{V}_{ref} = V_\alpha + j V_\beta$ é sintetizado combinando os dois vetores ativos adjacentes ($\mathbf{V}_1 \dots \mathbf{V}_6$) e os vetores nulos ($\mathbf{V}_0, \mathbf{V}_7$):

$$T_1 = \frac{\sqrt{3} T_s |\mathbf{V}_{ref}|}{V_{dc}} \sin\left( \frac{\pi}{3} - \theta \right), \quad T_2 = \frac{\sqrt{3} T_s |\mathbf{V}_{ref}|}{V_{dc}} \sin(\theta), \quad T_0 = T_s - T_1 - T_2$$

- **Vantagem sobre SPWM senoidal**: Eleva a utilização do barramento CC em $+15,5\%$ sem entrar em sobremodulação ($V_{max,linear} = \frac{V_{dc}}{\sqrt{3}}$ contra $\frac{V_{dc}}{2}$).

---

## 📋 5. Instalações Elétricas e Conformidade Normativa (BT e MT)

| Norma Regulamentadora / Técnica | Âmbito de Aplicação | Requisitos Críticos de Engenharia |
| :--- | :--- | :--- |
| **ABNT NBR 5410** | Instalações de Baixa Tensão ($\le 1000\text{V CA}$) | Dimensionamento por 6 critérios: Seção Mínima, Capacidade de Condução, Queda de Tensão ($\le 4\%$), Sobrecarga, Curto-circuito e Proteção contra Choques (DR $\le 30\text{mA}$, Equipotencialização BEP). |
| **ABNT NBR 14039** | Instalações de Média Tensão ($1.0\text{kV}$ a $36.2\text{kV}$) | Subestações abrigadas e de alvenaria, coordenação de proteção relé-fusível, transformadores a seco vs a óleo, isolamento e distâncias dielétricas no ar. |
| **NR-10** | Segurança em Instalações e Serviços em Eletricidade | Prontuário das Instalações Elétricas (PIE), Análise Preliminar de Risco (APR), Vestimentas ATPV para proteção contra Arco Elétrico, Zonas de Risco e Controlada. |
| **PRODIST Módulos 3 e 8 (ANEEL)** | Acesso à Rede e Qualidade da Energia Elétrica (QEE) | Limites de distorção harmônica total ($THD_V \le 10\%$, $THD_I$), flutuação de tensão (*Flicker* $P_{st}, P_{lt}$), desequilíbrio de tensão e fator de potência ($\ge 0.92$). |
