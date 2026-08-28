---
name: academic-circuit-analysis-electronics
description: Especialista em Análise de Circuitos Elétricos e Eletrônica Analógica baseado nas obras Introductory Circuit Analysis (Boylestad) e Microelectronic Circuits (Sedra, Smith). Cobre Leis de Kirchhoff, Teoremas de Thévenin e Norton, Circuitos RLC em Regime Permanente e Transitório, Fasores, Amplificadores Operacionais, Diodos, Transistores BJT e MOSFETs, e Resposta em Frequência (Diagramas de Bode).
---

# Análise de Circuitos Elétricos e Microeletrônica (Sedra & Smith)

Esta skill estabelece os métodos matemáticos e modelos de pequenos e grandes sinais para projeto e análise de circuitos elétricos lineares e não-lineares.

---

## ⚡ 1. Teoremas de Redes e Análise Fasorial

- **Leis de Kirchhoff (LKC e LKV)**: $\sum I_{no} = 0$, $\sum V_{malha} = 0$.
- **Equivalentes de Thévenin e Norton**:
  $$V_{th} = V_{oc}, \quad I_n = I_{sc}, \quad R_{th} = \frac{V_{oc}}{I_{sc}}$$
- **Impedância Fasorial $\mathbf{Z}$**:
  $$\mathbf{Z}_R = R, \quad \mathbf{Z}_L = j\omega L, \quad \mathbf{Z}_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$$

---

## 🔬 2. Modelo de Pequenos Sinais do Transistor MOSFET

Na região de saturação ($V_{DS} \ge V_{GS} - V_{th}$):
$$I_D = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} (V_{GS} - V_{th})^2 (1 + \lambda V_{DS})$$
Transcondutância $g_m$:
$$g_m = \left. \frac{\partial I_D}{\partial V_{GS}} \right|_{V_{DS, Q}} = \sqrt{2 \mu_n C_{ox} \frac{W}{L} I_D} = \frac{2 I_D}{V_{OV}}$$
