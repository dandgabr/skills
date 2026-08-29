---
name: academic-classical-mechanics-relativity
description: Especialista em Mecânica Clássica Avançada, Dinâmica Analítica, Teoria do Caos e Teoria da Relatividade Especial e Geral baseado nas obras Classical Mechanics (Herbert Goldstein), Mechanics (Landau & Lifshitz), Gravitation (Misner, Thorne, Wheeler) e Spacetime and Geometry (Sean Carroll). Cobre Formalismos Lagrangeano e Hamiltoniano (Euler-Lagrange, Transformada de Legendre, Parênteses de Poisson, Transformações Canônicas, Hamilton-Jacobi e Teorema de Noether), Dinâmica do Corpo Rígido Tridimensional (Tensor de Inércia, Ângulos de Euler, Equações de Euler do Movimento), Teoria de Pequenas Oscilações e Modos Normais, Teoria do Caos Determinístico (Expoentes de Lyapunov, Seções de Poincaré, Atratores Estranhos), Relatividade Especial Covariante (Quadrivetores de Minkowski, Tensor Eletromagnético Fμν) e Relatividade Geral (Geodésicas, Tensor de Curvatura de Riemann, Equações de Campo de Einstein e Métrica de Schwarzschild).
---

# Mecânica Clássica Avançada e Teoria da Relatividade (Goldstein & Landau)

Esta skill estabelece os fundamentos matemáticos e físicos da mecânica analítica variacional, dinâmica de sistemas de muitos corpos e corpos rígidos, teoria do caos e a geometria relativística do espaço-tempo de Lorentz e Einstein.

---

## ⚙️ 1. Formalismo Lagrangeano e Hamiltoniano

### 1.1 Princípio de Hamilton e Equações de Euler-Lagrange
O princípio da mínima ação de Hamilton $\delta S = \delta \int_{t_1}^{t_2} L(q_i, \dot{q}_i, t) \, dt = 0$ governa o movimento em coordenadas generalizadas $q_i$:

$$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = Q_i^{nc}$$

onde $L = T - V$ é a função Lagrangeana e $Q_i^{nc}$ são forças generalizadas não-conservativas.

- **Teorema de Noether**: Para cada simetria contínua da ação (invariância sob um grupo a 1 parâmetro), existe uma quantidade conservada:
  - Invariância por translação temporal $\implies$ Conservação da Energia Total $H$.
  - Invariância por translação espacial $\implies$ Conservação do Momento Linear Total $\mathbf{P}$.
  - Invariância por rotação espacial $\implies$ Conservação do Momento Angular Total $\mathbf{L}$.
  - Coordenada cíclica ($\frac{\partial L}{\partial q_k} = 0$) $\implies$ Momento conjugado constante $p_k = \frac{\partial L}{\partial \dot{q}_k} = \text{const}$.

### 1.2 Mecânica Hamiltoniana e Parênteses de Poisson
A função Hamiltoniana $H(q, p, t)$ obtida via Transformada de Legendre $H = \sum_i p_i \dot{q}_i - L$:

$$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}$$

- **Parênteses de Poisson**: $\{f, g\} = \sum_i \left( \frac{\partial f}{\partial q_i} \frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i} \frac{\partial g}{\partial q_i} \right)$.
- **Evolução Temporal de um Observável**: $\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}$.
- **Equação de Hamilton-Jacobi**: $H\left( q_i, \frac{\partial S}{\partial q_i}, t \right) + \frac{\partial S}{\partial t} = 0$, onde $S(q_i, \alpha_i, t)$ é a função principal de Hamilton.

---

## 🔄 2. Dinâmica de Corpos Rígidos e Pequenas Oscilações

### 2.1 Tensor de Inércia e Equações de Euler
O tensor de inércia simétrico de 2ª ordem $\mathbf{I}$:

$$I_{jk} = \int_V \rho(\mathbf{r}) \left( r^2 \delta_{jk} - x_j x_k \right) dV$$

- **Equações de Euler para o Corpo Rígido nos Eixos Principais ($1, 2, 3$)**:
  $$I_1 \dot{\omega}_1 - (I_2 - I_3) \omega_2 \omega_3 = N_1$$
  $$I_2 \dot{\omega}_2 - (I_3 - I_1) \omega_3 \omega_1 = N_2$$
  $$I_3 \dot{\omega}_3 - (I_1 - I_2) \omega_1 \omega_2 = N_3$$
  onde $\mathbf{N}$ é o torque externo aplicado.

### 2.2 Teoria de Pequenas Oscilações e Modos Normais
Para pequenas perturbações $\boldsymbol{\eta} = \mathbf{q} - \mathbf{q}_0$ em torno do equilíbrio estável ($\nabla V(\mathbf{q}_0) = 0$):
$$L \approx \frac{1}{2} \dot{\boldsymbol{\eta}}^T \mathbf{M} \dot{\boldsymbol{\eta}} - \frac{1}{2} \boldsymbol{\eta}^T \mathbf{K} \boldsymbol{\eta}$$
- **Frequências Próprias ($\omega$)**: Soluções da equação secular $\det(\mathbf{K} - \omega^2 \mathbf{M}) = 0$.

---

## 🌀 3. Teoria do Caos Determinístico e Sistemas Não-Lineares

- **Sensibilidade às Condições Iniciais (Efeito Borboleta)**: Divergência exponencial de trajetórias vizinhas no espaço de fase $\delta \mathbf{x}(t) \approx \delta \mathbf{x}(0) e^{\lambda t}$.
- **Expoente Máximo de Lyapunov ($\lambda_{max}$)**:
  $$\lambda_{max} = \lim_{t \to \infty} \frac{1}{t} \ln \frac{\|\delta \mathbf{x}(t)\|}{\|\delta \mathbf{x}(0)\|}$$
  Se $\lambda_{max} > 0$, o sistema exibe dinâmica caótica determinística.
- **Seção de Poincaré**: Mapeamento discreto estroboscópico que reduz a dimensionalidade contínua do atrator estranho fractal.

---

## 🌌 4. Teoria da Relatividade Especial e Geral

### 4.1 Relatividade Especial em Notação Covariante de 4-Vetores
Métrica de Minkowski $\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$ com $x^\mu = (ct, x, y, z)$:

- **Intervalo Invariante**: $ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu = -c^2 d\tau^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$.
- **Quadrimomento**: $P^\mu = m \frac{dx^\mu}{d\tau} = (\gamma m c, \gamma m \mathbf{v}) = (E/c, \mathbf{p}) \implies P_\mu P^\mu = -\frac{E^2}{c^2} + p^2 = -m^2 c^2$.
- **Tensor Eletromagnético de Maxwell**:
  $$F^{\mu\nu} = \begin{bmatrix} 0 & E_x/c & E_y/c & E_z/c \\ -E_x/c & 0 & B_z & -B_y \\ -E_y/c & -B_z & 0 & B_x \\ -E_z/c & B_y & -B_x & 0 \end{bmatrix}, \quad \partial_\mu F^{\mu\nu} = \mu_0 J^\nu$$

### 4.2 Relatividade Geral e Equações de Campo de Einstein
A gravitação descrita como a curvatura do espaço-tempo pseudo-riemanniano com métrica $g_{\mu\nu}$:

- **Equação das Geodésicas (Queda Livre)**:
  $$\frac{d^2 x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{d\tau} \frac{dx^\beta}{d\tau} = 0, \quad \Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\sigma} \left( \partial_\alpha g_{\beta\sigma} + \partial_\beta g_{\alpha\sigma} - \partial_\sigma g_{\alpha\beta} \right)$$
- **Equações de Campo de Einstein com Constante Cosmológica $\Lambda$**:
  $$G_{\mu\nu} + \Lambda g_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$
- **Métrica de Schwarzschild no Vácuo Estático e Esfericamente Simétrico**:
  $$ds^2 = -\left(1 - \frac{2GM}{c^2 r}\right) c^2 dt^2 + \left(1 - \frac{2GM}{c^2 r}\right)^{-1} dr^2 + r^2 (d\theta^2 + \sin^2\theta \, d\phi^2)$$
  onde $r_s = \frac{2GM}{c^2}$ é o raio do horizonte de eventos do buraco negro de Schwarzschild.
