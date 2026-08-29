---
name: academic-structural-analysis-solid-mechanics
description: "Especialista em Mecânica dos Sólidos, Análise Estrutural Matricial, Elementos Finitos (FEA), Mecânica dos Solos e Geotecnia baseado em James M. Gere & Barry J. Goodno (Mechanics of Materials), Aslam Kassimali (Matrix Analysis of Structures) e Braja M. Das (Principles of Geotechnical Engineering). Cobre Estado Plano de Tensões e Deformações (Círculo de Mohr, Critérios de Escoamento de Von Mises e Tresca), Flexão, Cisalhamento e Torção em Vigas, Flambagem de Colunas de Euler, Método da Rigidez Direta, Formulação de Elementos Finitos, Princípio das Tensões Efetivas de Terzaghi, Classificação de Solos (SUCS, HRB), Permeabilidade e Lei de Darcy, Teoria do Adensamento Unidimensional de Terzaghi, Critério de Ruptura de Mohr-Coulomb, Empuxo de Terra (Rankine/Coulomb) e Capacidade de Carga de Fundações Superficiais e Profundas (Meyerhof, Terzaghi, Hansen)."
---

# Mecânica dos Sólidos, Análise Estrutural e Engenharia Geotécnica

Esta skill estabelece os fundamentos matemáticos e métodos numéricos para análise estrutural de elementos de concreto, aço e compósitos, combinados aos modelos constitutivos da mecânica dos solos e geotecnia para fundações e contenções, fundamentada em **Gere & Goodno**, **Kassimali** e **Braja M. Das**.

---

## 🏗️ 1. Mecânica dos Sólidos e Estado de Tensão

### 1.1 Círculo de Mohr e Critérios de Escoamento
- **Tensões Principais ($\sigma_1, \sigma_2, \sigma_3$)**:
  $$\sigma_{1,2} = \frac{\sigma_x + \sigma_y}{2} \pm \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}, \quad \tau_{max} = \frac{\sigma_1 - \sigma_2}{2}$$
- **Critério de Escoamento de Von Mises (Energia de Distorção)**:
  $$\sigma_{vm} = \sqrt{\frac{1}{2} \left[ (\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2 \right]} \le \frac{f_y}{\gamma_m}$$
- **Critério de Máxima Tensão de Cisalhamento (Tresca)**:
  $$\tau_{max} = \frac{\sigma_1 - \sigma_3}{2} \le \frac{f_y}{2 \gamma_m}$$

### 1.2 Flambagem de Colunas de Euler
Carga Crítica de Flambagem elástica para coluna com comprimento efetivo $K L$:
$$P_{cr} = \frac{\pi^2 E I}{(K L)^2}, \quad \sigma_{cr} = \frac{\pi^2 E}{\lambda^2} \quad \left(\text{onde } \lambda = \frac{K L}{r} \text{ é o índice de esbeltez}\right)$$

---

## 📐 2. Análise Estrutural Matricial e Elementos Finitos (FEA)

### 2.1 Método da Rigidez Direta
Para uma estrutura reticulada com $n$ graus de liberdade:
$$\mathbf{K} \mathbf{u} = \mathbf{F}$$
- **Matriz de Rigidez Local do Elemento de Viga 2D**:
  $$\mathbf{k}_e = \begin{bmatrix}
  \frac{EA}{L} & 0 & 0 & -\frac{EA}{L} & 0 & 0 \\
  0 & \frac{12EI}{L^3} & \frac{6EI}{L^2} & 0 & -\frac{12EI}{L^3} & \frac{6EI}{L^2} \\
  0 & \frac{6EI}{L^2} & \frac{4EI}{L} & 0 & -\frac{6EI}{L^2} & \frac{2EI}{L} \\
  -\frac{EA}{L} & 0 & 0 & \frac{EA}{L} & 0 & 0 \\
  0 & -\frac{12EI}{L^3} & -\frac{6EI}{L^2} & 0 & \frac{12EI}{L^3} & -\frac{6EI}{L^2} \\
  0 & \frac{6EI}{L^2} & \frac{2EI}{L} & 0 & -\frac{6EI}{L^2} & \frac{4EI}{L}
  \end{bmatrix}$$

---

## 🌍 3. Mecânica dos Solos e Princípio de Terzaghi

### 3.1 Princípio das Tensões Efetivas
$$\sigma' = \sigma - u$$
onde $\sigma$ é a tensão total vertical devido ao peso próprio do solo e sobrecargas, $u$ é a poro-pressão da água intersticial e $\sigma'$ é a tensão efetiva que governa a resistência ao cisalhamento e o adensamento.

### 3.2 Resistência ao Cisalhamento (Critério de Mohr-Coulomb)
$$\tau_f = c' + \sigma' \tan \phi'$$
onde $c'$ é a coesão efetiva e $\phi'$ é o ângulo de atrito interno efetivo do solo.

### 3.3 Teoria do Adensamento Unidimensional de Terzaghi
Equação diferencial governante do excesso de poro-pressão $\bar{u}(z,t)$:
$$\frac{\partial \bar{u}}{\partial t} = c_v \frac{\partial^2 \bar{u}}{\partial z^2}, \quad c_v = \frac{k}{\gamma_w m_v}$$
O recalque primário total por adensamento $S_c$ para solo normalmente adensado de espessura $H_0$:
$$S_c = \frac{C_c H_0}{1 + e_0} \log_{10}\left( \frac{\sigma'_0 + \Delta\sigma'}{\sigma'_0} \right)$$

---

## 🏛️ 4. Geotecnia de Fundações e Empuxo de Terra

1. **Empuxo de Terra (Rankine)**:
   - Coeficiente de Empuxo Ativo: $K_a = \tan^2\left(45^\circ - \frac{\phi'}{2}\right) = \frac{1 - \sin\phi'}{1 + \sin\phi'}$
   - Coeficiente de Empuxo Passivo: $K_p = \tan^2\left(45^\circ + \frac{\phi'}{2}\right) = \frac{1 + \sin\phi'}{1 - \sin\phi'}$
2. **Capacidade de Carga de Fundações Superficiais (Equação Geral de Terzaghi/Meyerhof)**:
   $$q_{ult} = c' N_c s_c d_c + q N_q s_q d_q + \frac{1}{2} \gamma B N_\gamma s_\gamma d_\gamma$$
   onde $N_c, N_q, N_\gamma$ são os fatores adimensionais de capacidade de carga dependentes exclusivamente de $\phi'$.
