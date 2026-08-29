---
name: academic-quantum-mechanics-matter
description: Especialista em Mecânica Quântica Avançada, Física Atômica, Teoria de Perturbações e Física da Matéria Condensada baseado nas obras Modern Quantum Mechanics (J. J. Sakurai, Napolitano), Quantum Mechanics (Claude Cohen-Tannoudji) e Introduction to Solid State Physics (Charles Kittel). Cobre Formalismo de Dirac no Espaço de Hilbert, Oscilador Harmônico Quântico via Operadores Escada (Criação e Aniquilação), Teoria do Momento Angular e Spin 1/2 (Matrizes de Pauli e Coeficientes de Clebsch-Gordan), Métodos de Aproximação (Perturbação Independente do Tempo Não-Degenerada/Degenerada, Efeito Stark e Zeeman, Método Variacional, Aproximação WKB e Regra de Ouro de Fermi), Teoria de Espalhamento Quântico (Aproximação de Born e Ondas Parciais), Teorema de Bloch e Estrutura de Bandas em Sólidos e Física Nuclear.
---

# Mecânica Quântica Avançada e Matéria Condensada (Sakurai & Cohen-Tannoudji)

Esta skill estabelece o formalismo quântico canônico em espaços de Hilbert, álgebra de operadores, métodos analíticos de aproximação, dinâmica quântica temporal, teoria de espalhamento e modelos de bandas eletrônicas na física da matéria condensada.

---

## ⚛️ 1. Formalismo de Dirac e Postulados Fundamentais

### 1.1 Vetores de Estado e Observáveis no Espaço de Hilbert $\mathcal{H}$
- **Equação de Schrödinger Dependente do Tempo**:
  $$i\hbar \frac{d}{dt} |\psi(t)\rangle = \hat{H} |\psi(t)\rangle \implies |\psi(t)\rangle = e^{-i\hat{H}t/\hbar} |\psi(0)\rangle$$
- **Medição Quântica e Colapso (Postulado de Born)**: A probabilidade de obter o autovalor $a_n$ com autovetor não-degenerado $|a_n\rangle$:
  $$P(a_n) = |\langle a_n | \psi \rangle|^2$$
- **Relação de Incerteza Generalizada de Robertson-Schrödinger**:
  $$\sigma_A^2 \sigma_B^2 \ge \left( \frac{1}{2i} \langle [\hat{A}, \hat{B}] \rangle \right)^2 + \left( \frac{1}{2} \langle \{ \hat{A} - \langle A \rangle, \hat{B} - \langle B \rangle \} \rangle \right)^2$$
  Para $[\hat{x}, \hat{p}_x] = i\hbar \hat{I} \implies \sigma_x \sigma_p \ge \frac{\hbar}{2}$.

### 1.2 Oscilador Harmônico Simples por Operadores Escada
Hamiltoniano $\hat{H} = \frac{\hat{p}^2}{2m} + \frac{1}{2}m\omega^2 \hat{x}^2 = \hbar\omega \left( \hat{a}^\dagger \hat{a} + \frac{1}{2} \right)$:
- Operadores de aniquilação $\hat{a}$ e criação $\hat{a}^\dagger$ com $[\hat{a}, \hat{a}^\dagger] = 1$:
  $$\hat{a} |n\rangle = \sqrt{n} |n-1\rangle, \quad \hat{a}^\dagger |n\rangle = \sqrt{n+1} |n+1\rangle, \quad E_n = \left(n + \frac{1}{2}\right)\hbar\omega$$

---

## 🌀 2. Momento Angular Quântico, Spin e Composição de Spins

### 2.1 Álgebra do Momento Angular $\hat{\mathbf{J}}$
$$[\hat{J}_i, \hat{J}_j] = i\hbar \varepsilon_{ijk} \hat{J}_k, \quad \hat{\mathbf{J}}^2 |j, m\rangle = \hbar^2 j(j+1) |j, m\rangle, \quad \hat{J}_z |j, m\rangle = \hbar m |j, m\rangle$$
- **Spin 1/2 e Matrizes de Pauli $\boldsymbol{\sigma}$**:
  $$\hat{\mathbf{S}} = \frac{\hbar}{2}\boldsymbol{\sigma}, \quad \sigma_x = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \quad \sigma_y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}, \quad \sigma_z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
  com relação fundamental $\sigma_i \sigma_j = \delta_{ij} I + i\varepsilon_{ijk} \sigma_k$.

### 2.2 Coeficientes de Clebsch-Gordan e Acoplamento $\hat{\mathbf{J}} = \hat{\mathbf{J}}_1 + \hat{\mathbf{J}}_2$
$$|J, M\rangle = \sum_{m_1=-j_1}^{j_1} \sum_{m_2=-j_2}^{j_2} \langle j_1, j_2; m_1, m_2 | J, M \rangle |j_1, m_1\rangle |j_2, m_2\rangle$$
com restrições $|j_1 - j_2| \le J \le j_1 + j_2$ e $M = m_1 + m_2$.

---

## 📐 3. Métodos de Aproximação em Mecânica Quântica

### 3.1 Teoria de Perturbações Independente do Tempo (Rayleigh-Schrödinger)
Para $\hat{H} = \hat{H}_0 + \lambda \hat{V}$:
- **Correção de 1ª Ordem na Energia**: $E_n^{(1)} = \langle n^{(0)} | \hat{V} | n^{(0)} \rangle$.
- **Correção de 2ª Ordem na Energia**:
  $$E_n^{(2)} = \sum_{k \ne n} \frac{|\langle k^{(0)} | \hat{V} | n^{(0)} \rangle|^2}{E_n^{(0)} - E_k^{(0)}}$$
- **Perturbação Degenerada**: Diagonalização da submatriz de perturbação $V_{ij} = \langle \psi_i^{(0)} | \hat{V} | \psi_j^{(0)} \rangle$ no subespaço degenerado (ex.: Efeito Zeeman e Estrutura Fina do Hidrogênio).

### 3.2 Teoria de Perturbações Dependente do Tempo e Regra de Ouro de Fermi
A taxa de transição por unidade de tempo $W_{i \to f}$ induzida por uma perturbação harmônica para um contínuo de estados com densidade $\rho(E_f)$:

$$W_{i \to f} = \frac{2\pi}{\hbar} |\langle f | \hat{V} | i \rangle|^2 \rho(E_f)$$

---

## 🧊 4. Teorema de Bloch e Física da Matéria Condensada

- **Teorema de Bloch**: Elétrons em um potencial cristalino periódico $V(\mathbf{r} + \mathbf{R}) = V(\mathbf{r})$ possuem autofunções na forma de ondas planas moduladas pela periodicidade da rede:
  $$\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k} \cdot \mathbf{r}} u_{\mathbf{k}}(\mathbf{r}), \quad u_{\mathbf{k}}(\mathbf{r} + \mathbf{R}) = u_{\mathbf{k}}(\mathbf{r})$$
- **Modelo de Kronig-Penney e Abertura de Band Gaps**: A reflexão de Bragg nas bordas da Primeira Zona de Brillouin ($k = \pm \pi/a$) produz ondas estacionárias com energias distintas, gerando a banda proibida (*Band Gap* $E_g$).
- **Massa Efetiva do Elétron/Buraco no Cristal**:
  $$m^* = \hbar^2 \left( \frac{d^2 E}{dk^2} \right)^{-1}$$
