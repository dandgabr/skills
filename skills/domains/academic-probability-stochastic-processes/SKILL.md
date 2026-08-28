---
name: academic-probability-stochastic-processes
description: Especialista em Probabilidade Axiomática (Kolmogorov, Teoria da Medida), Processos Estocásticos, Cadeias de Markov (Tempo Discreto e Contínuo), Martingales, Movimento Browniano, Filas e Teoria da Confiabilidade.
---

# Probabilidade Axiomática e Processos Estocásticos

Esta skill estabelece a modelagem matemática de incerteza, variáveis aleatórias multivariadas, convergência estocástica e sistemas dinâmicos probabilísticos.

---

## 🎲 1. Espaço de Probabilidade e Teoremas Limite

- **Espaço de Probabilidade $(\Omega, \mathcal{F}, P)$**: Espaço amostral $\Omega$, $\sigma$-álgebra $\mathcal{F}$ e medida de probabilidade $P$.
- **Lei Forte dos Grandes Números (SLLN)**: Para variáveis i.i.d. $X_1, X_2, \dots$ com $E[|X_i|] < \infty$:
  $$P\left( \lim_{n \to \infty} \frac{1}{n}\sum_{i=1}^n X_i = \mu \right) = 1$$
- **Teorema Central do Limite (TCL)**:
  $$\frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

---

## 📈 2. Cadeias de Markov e Equação de Chapman-Kolmogorov

Para uma cadeia de Markov a tempo discreto com espaço de estados $\mathcal{S}$ e matriz de transição $P$:
$$P_{ij}^{(n+m)} = \sum_{k \in \mathcal{S}} P_{ik}^{(n)} P_{kj}^{(m)}$$
A distribuição estacionária $\boldsymbol{\pi}$ satisfaz:
$$\boldsymbol{\pi} P = \boldsymbol{\pi} \quad \text{com } \sum_{i} \pi_i = 1$$
