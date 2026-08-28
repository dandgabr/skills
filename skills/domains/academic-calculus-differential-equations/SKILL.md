---
name: academic-calculus-differential-equations
description: Especialista em Cálculo Diferencial e Integral (I a IV), Equações Diferenciais Ordinárias (EDO), Equações Diferenciais Parciais (EDP), Cálculo Vetorial e Métodos Numéricos baseado nas obras Algebra, Topology, Differential Calculus, and Optimization Theory for CS and ML (Jean Gallier, Jocelyn Quaintance), Numerical Algorithms (Justin Solomon), Stewart e Boyce-DiPrima. Cobre Cálculo Vetorial (Gradiente, Divergente, Rotacional, Teoremas de Green, Stokes e Divergência de Gauss), EDOs Lineares e Não-Lineares (Fator Integrante, Variação de Parâmetros, Transformadas de Laplace), EDPs Clássicas (Equações do Calor, da Onda e de Laplace/Poisson, Séries de Fourier, Separação de Variáveis) e Métodos Numéricos (Euler, RK4, Integradores Simpléticos Verlet/Leapfrog, Diferenças Finitas FDM e Elementos Finitos FEM).
---

# Cálculo Diferencial, Integral, EDOs, EDPs e Métodos Numéricos

Esta skill estabelece o instrumental rigoroso do cálculo multivariável, cálculo vetorial, equações diferenciais analíticas e discretização numérica para física matemática, dinâmica de sistemas, processamento de sinais e computação gráfica.

---

## 📐 1. Cálculo Vetorial e Teoremas Fundamentais de Integração

### 1.1 Operadores Diferenciais Vetoriais no $\mathbb{R}^3$
Dado um campo escalar $f(x,y,z)$ e um campo vetorial $\mathbf{F} = [F_x, F_y, F_z]^T$:
- **Gradiente**: $\nabla f = \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right]^T$ (aponta na direção de máxima taxa de variação).
- **Divergente**: $\nabla \cdot \mathbf{F} = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$ (taxa de expansão volumar por unidade de tempo).
- **Rotacional**: $\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ F_x & F_y & F_z \end{vmatrix}$ (medida da circulação infinitesimal).
- **Laplaciano**: $\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$.

### 1.2 Teoremas Integrais Clássicos
| Teorema | Formulação Integral | Significado Físico / Geométrico |
| :--- | :--- | :--- |
| **Teorema de Green no Plano** | $\oint_{\partial D} (L \, dx + M \, dy) = \iint_D \left( \frac{\partial M}{\partial x} - \frac{\partial L}{\partial y} \right) dA$ | Circulação em torno de uma curva plana fechada é igual ao rotacional integrado na área. |
| **Teorema de Stokes Clássico** | $\oint_{\partial S} \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot \mathbf{n} \, dS$ | Circulação de $\mathbf{F}$ na fronteira é igual ao fluxo do rotacional pela superfície. |
| **Teorema da Divergência (Gauss)** | $\oiint_{\partial V} \mathbf{F} \cdot \mathbf{n} \, dS = \iiint_V (\nabla \cdot \mathbf{F}) \, dV$ | Fluxo líquido total de $\mathbf{F}$ saindo de um volume fechado é igual à soma das fontes internas. |

---

## 📈 2. Equações Diferenciais Ordinárias (EDO) Analíticas

### 2.1 EDOs Lineares de Primeira Ordem (Fator Integrante)
$$y' + P(x)y = Q(x) \implies \mu(x) = e^{\int P(x) dx} \implies y(x) = \frac{1}{\mu(x)} \left( \int \mu(x) Q(x) dx + C \right)$$

### 2.2 EDOs Lineares de Segunda Ordem com Coeficientes Constantes
$$a y'' + b y' + c y = g(x)$$
- **Equação Característica**: $a r^2 + b r + c = 0 \implies \Delta = b^2 - 4ac$.
  1. $\Delta > 0$: $y_h(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x}$.
  2. $\Delta = 0$: $y_h(x) = c_1 e^{r x} + c_2 x e^{r x}$.
  3. $\Delta < 0$ ($r = \alpha \pm i \beta$): $y_h(x) = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)$.
- **Método da Variação dos Parâmetros**: Para encontrar a solução particular $y_p(x)$:
  $$y_p(x) = -y_1(x) \int \frac{y_2(x) g(x)}{W(y_1, y_2)(x)} dx + y_2(x) \int \frac{y_1(x) g(x)}{W(y_1, y_2)(x)} dx$$
  onde $W(y_1, y_2)(x) = y_1 y_2' - y_2 y_1'$ é o determinante Wronskiano.

### 2.3 Transformada de Laplace para Resolução de PVIs
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t) e^{-st} dt$$
- $\mathcal{L}\{y'(t)\} = s Y(s) - y(0)$
- $\mathcal{L}\{y''(t)\} = s^2 Y(s) - s y(0) - y'(0)$
- **Teorema da Convolução**: $\mathcal{L}^{-1}\{F(s)G(s)\} = (f * g)(t) = \int_0^t f(\tau) g(t - \tau) d\tau$.

---

## 🌊 3. Equações Diferenciais Parciais (EDP) Fundamentais

### 3.1 Classificação de EDPs de 2ª Ordem ($A u_{xx} + B u_{xy} + C u_{yy} + \dots = 0$)
- **Hiperbólica ($B^2 - 4AC > 0$)**: Equação da Onda $\frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u$ (propagação e ondas acústicas/eletromagnéticas).
- **Parabólica ($B^2 - 4AC = 0$)**: Equação do Calor / Difusão $\frac{\partial u}{\partial t} = \alpha \nabla^2 u$ (condução térmica e dissipação).
- **Elíptica ($B^2 - 4AC < 0$)**: Equação de Laplace $\nabla^2 u = 0$ / Poisson $\nabla^2 u = f$ (potencial eletrostático e fluidos incompressíveis).

### 3.2 Método de Separação de Variáveis e Séries de Fourier
Para a equação da barra de calor $u_t = \alpha u_{xx}$ com condições de contorno de Dirichlet $u(0,t) = u(L,t) = 0$:
$$u(x, t) = \sum_{n=1}^\infty B_n \sin\left(\frac{n\pi x}{L}\right) e^{-\alpha \left(\frac{n\pi}{L}\right)^2 t}, \quad B_n = \frac{2}{L} \int_0^L f(x) \sin\left(\frac{n\pi x}{L}\right) dx$$

---

## 🧮 4. Métodos Numéricos para EDOs e EDPs (Solomon)

### 4.1 Método de Runge-Kutta Clássico de 4ª Ordem (RK4)
Para o PVI $\frac{dy}{dt} = f(t, y), \; y(t_0) = y_0$:
$$y_{n+1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$$
- $k_1 = f(t_n, y_n)$
- $k_2 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1)$
- $k_3 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2)$
- $k_4 = f(t_n + h, y_n + h k_3)$
Erro de truncamento local: $\mathcal{O}(h^5)$; Erro global: $\mathcal{O}(h^4)$.

### 4.2 Integradores Simpléticos (Verlet e Leapfrog) para Mecânica e Gráficos
Para sistemas Hamiltonianos $\ddot{\mathbf{x}} = \mathbf{a}(\mathbf{x})$, integradores simpléticos conservam a energia mecânica e o volume do espaço de fase sem amortecimento espúrio:
- **Velocity Verlet**:
  $$\mathbf{x}_{n+1} = \mathbf{x}_n + \mathbf{v}_n h + \frac{1}{2} \mathbf{a}_n h^2$$
  $$\mathbf{v}_{n+1} = \mathbf{v}_n + \frac{1}{2} (\mathbf{a}_n + \mathbf{a}_{n+1}) h$$

### 4.3 Método das Diferenças Finitas (FDM) para EDPs
Aproximação de derivadas por estêncil central:
$$u_{xx}(x_i, y_j) \approx \frac{u_{i+1, j} - 2u_{i,j} + u_{i-1, j}}{\Delta x^2}$$
$$u_{yy}(x_i, y_j) \approx \frac{u_{i, j+1} - 2u_{i,j} + u_{i, j-1}}{\Delta y^2}$$
- **Condição CFL (Courant-Friedrichs-Lewy) para estabilidade explícita de ondas**: $C = \frac{c \Delta t}{\Delta x} \le 1$.
