---
name: academic-probability-stochastic-processes
description: "Especialista em Probabilidade Axiomática, Teoria da Medida e Processos Estocásticos baseado nas obras Probability and Random Processes (Grimmett, Stirzaker), Probability: Theory and Examples (Rick Durrett) e Stochastic Differential Equations (Bernt Øksendal). Cobre Espaços de Probabilidade (Kolmogorov, σ-álgebras, Medida de Lebesgue-Stieltjes, Esperança Condicional como Projeção em L2), Modos de Convergência (Quase Certa, em Probabilidade, em Lp, em Distribuição, Lemas de Borel-Cantelli e Teorema de Slutsky), Cadeias de Markov a Tempo Discreto e Contínuo (Equações Diferenciais de Chapman-Kolmogorov, Matriz Geradora Q, Distribuições Estacionárias), Teoria dos Martingales (Teorema da Parada Opcional de Doob), Processo de Poisson e Teoria de Filas (M/M/1, Lei de Little) e Movimento Browniano / Cálculo Estocástico de Itô (Lema de Itô e SDEs)."
---

# Probabilidade Axiomática e Processos Estocásticos (Grimmett & Durrett)

Esta skill estabelece a fundamentação mecanicista e probabilística formal sob Teoria da Medida, convergência de variáveis aleatórias multivariadas, cadeias de Markov, teoria dos martingales, processos pontuais e equações diferenciais estocásticas.

---

## 🎲 1. Fundamentação Axiomática de Kolmogorov e Teoria da Medida

### 1.1 Espaço de Probabilidade $(\Omega, \mathcal{F}, P)$
- $\Omega$: Espaço amostral de eventos elementares.
- $\mathcal{F}$: $\sigma$-álgebra de subconjuntos de $\Omega$ fechada sob complementação e uniões enumeráveis.
- $P: \mathcal{F} \to [0, 1]$: Medida de probabilidade finitamente aditiva e $\sigma$-aditiva com $P(\Omega) = 1$.
- **Esperança Condicional como Projeção em $L^2$**: Dado sub-$\sigma$-álgebra $\mathcal{G} \subseteq \mathcal{F}$, $E[X|\mathcal{G}]$ é a única variável aleatória $\mathcal{G}$-mensurável tal que:
  $$\int_A E[X|\mathcal{G}] \, dP = \int_A X \, dP, \quad \forall A \in \mathcal{G}$$

### 1.2 Modos de Convergência Estocástica e Lemas de Borel-Cantelli
```
Hierarquia de Modos de Convergência:
  Convergência em Lp (p ≥ 1) ──┐
                               ▼
  Convergência Quase Certa (q.c. / a.s.) ──> Convergência em Probabilidade (P) ──> Convergência em Distribuição (d)
```

- **Primeiro Lema de Borel-Cantelli**: Se $\sum_{n=1}^\infty P(A_n) < \infty$, então $P(\limsup_{n \to \infty} A_n) = 0$.
- **Segundo Lema de Borel-Cantelli**: Se os eventos $A_n$ são independentes e $\sum_{n=1}^\infty P(A_n) = \infty$, então $P(\limsup_{n \to \infty} A_n) = 1$.
- **Teorema de Slutsky**: Se $X_n \xrightarrow{d} X$ e $Y_n \xrightarrow{P} c$ (constante), então $X_n + Y_n \xrightarrow{d} X + c$ e $X_n Y_n \xrightarrow{d} cX$.

---

## 📈 2. Cadeias de Markov a Tempo Discreto e Contínuo

### 2.1 Tempo Discreto (DTMC) e Equação de Chapman-Kolmogorov
Para uma sequência $\{X_n\}_{n=0}^\infty$ satisfazendo a propriedade de Markov $P(X_{n+1}=j \mid X_n=i, \dots, X_0=i_0) = P_{ij}$:
$$P_{ij}^{(n+m)} = \sum_{k \in \mathcal{S}} P_{ik}^{(n)} P_{kj}^{(m)} \iff \mathbf{P}^{(n+m)} = \mathbf{P}^{(n)} \mathbf{P}^{(m)}$$
- **Distribuição Estacionária $\boldsymbol{\pi}$**: Para cadeias irredutíveis e aperiódicas:
  $$\boldsymbol{\pi} \mathbf{P} = \boldsymbol{\pi} \quad \text{com } \sum_{i \in \mathcal{S}} \pi_i = 1$$

### 2.2 Tempo Contínuo (CTMC) e Matriz Geradora Infinitesimal $\mathbf{Q}$
Transições governadas por taxas $\lambda_{ij} \ge 0$ ($i \ne j$) com $q_{ii} = -\sum_{j \ne i} q_{ij}$:
- **Equações Diferenciais de Kolmogorov**:
  - *Backward*: $\frac{d \mathbf{P}(t)}{dt} = \mathbf{Q} \mathbf{P}(t)$
  - *Forward*: $\frac{d \mathbf{P}(t)}{dt} = \mathbf{P}(t) \mathbf{Q} \implies \mathbf{P}(t) = e^{\mathbf{Q} t}$
- **Equilíbrio Estacionário**: $\boldsymbol{\pi} \mathbf{Q} = \mathbf{0}$.

---

## 🛑 3. Teoria de Martingales e Tempos de Parada (Doob)

Um processo estocástico integrado $\{M_n\}_{n=0}^\infty$ adaptado a uma filtração $\{\mathcal{F}_n\}_{n=0}^\infty$ é um **Martingale** se $E[|M_n|] < \infty$ e:
$$E[M_{n+1} \mid \mathcal{F}_n] = M_n, \quad \forall n \ge 0$$
- **Tempo de Parada (*Stopping Time*) $\tau$**: Variável aleatória com valores em $\{0, 1, 2, \dots\} \cup \{\infty\}$ tal que $\{\tau = n\} \in \mathcal{F}_n$.
- **Teorema da Parada Opcional de Doob**: Se $M_n$ é um martingale e $\tau$ é um tempo de parada limitado ($\tau \le K$ q.c.), então:
  $$E[M_\tau] = E[M_0]$$

---

## 📉 4. Movimento Browniano e Cálculo Estocástico de Itô

### 4.1 Processo de Wiener $W(t)$
1. $W(0) = 0$ quase certamente.
2. Incrementos independentes: Para $0 \le t_1 < t_2 < \dots < t_k$, $W(t_{i+1}) - W(t_i)$ são mutuamente independentes.
3. Incrementos Gaussianos estacionários: $W(t) - W(s) \sim \mathcal{N}(0, t - s)$.
4. Trajetórias contínuas, porém não-diferenciáveis em quase todos os pontos com variação quadrática finita $[W, W]_t = t$.

### 4.2 Lema de Itô para Equações Diferenciais Estocásticas (SDEs)
Para um processo de difusão de Itô $dX_t = \mu(t, X_t) dt + \sigma(t, X_t) dW_t$ e função duas vezes diferenciável $f(t, x)$:

$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \mu \frac{\partial f}{\partial x} + \frac{1}{2} \sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \sigma \frac{\partial f}{\partial x} dW_t$$

---

## 🚶 5. Teoria de Filas e Processos de Nascimento e Morte

- **Lei de Little**: Em qualquer sistema em regime permanente, o número médio de entidades no sistema ($L$) correlaciona-se com a taxa média de chegada ($\lambda$) e o tempo médio no sistema ($W$):
  $$L = \lambda W \quad \text{e} \quad L_q = \lambda W_q$$
- **Fila $M/M/1$ com taxa de chegada $\lambda$ e taxa de serviço $\mu$ ($\rho = \lambda/\mu < 1$)**:
  - Probabilidade de $n$ clientes: $p_n = (1 - \rho) \rho^n$.
  - Número médio no sistema: $L = \frac{\rho}{1 - \rho}$.
  - Tempo médio no sistema: $W = \frac{1}{\mu - \lambda}$.
