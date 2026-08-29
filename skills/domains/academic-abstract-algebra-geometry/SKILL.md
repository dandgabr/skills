---
name: academic-abstract-algebra-geometry
description: Especialista em Álgebra Abstrata, Teoria de Corpos e Galois, Álgebra Linear Avançada e Geometria Diferencial baseado nas obras Algebra (Serge Lang), Abstract Algebra (Dummit & Foote), Algebra, Topology, Differential Calculus, and Optimization Theory for CS and ML (Jean Gallier, Jocelyn Quaintance) e Differential Geometry of Curves and Surfaces (do Carmo). Cobre Teoria de Grupos (Subgrupos Normais, Teoremas de Isomorfismo de Noether e Teoremas de Sylow), Teoria de Anéis e Ideais (DIP, DFUs, Domínios Euclidianos), Teoria de Corpos e Teoria de Galois (Extensões Algébricas, Corpos Finitos de Galois GF(p^n), Automorfismos e Solubilidade por Radicais de Abel-Ruffini), Espaços de Hilbert e Formas Quadráticas, Teorema Espectral e Decomposição de Jordan, Geometria Diferencial de Curvas e Superfícies (Triedro de Frenet-Serret, Formas Fundamentais I e II, Curvatura Gaussiana e Teorema de Gauss-Bonnet), Variedades Diferenciáveis e Teorema de Stokes Geral.
---

# Álgebra Abstrata, Teoria de Galois e Geometria Diferencial (Lang & do Carmo)

Esta skill fornece o rigor axiomático, formalismo algébrico estrutural e instrumental geométrico diferencial para matemática pura, física matemática, criptografia algébrica, computação teórica, robótica e aprendizado em variedades.

---

## 🏛️ 1. Álgebra Abstrata: Grupos, Anéis e Ideais

### 1.1 Teoria de Grupos e Teoremas Fundamentais
- **Subgrupos Normais e Grupos Quociente**: $N \triangleleft G \iff gNg^{-1} = N, \; \forall g \in G$. O conjunto das classes laterais $G/N$ forma um grupo bem definido.
- **Primeiro Teorema do Isomorfismo (Noether)**: Para qualquer homomorfismo de grupos $\phi: G \to H$, $\ker(\phi) \triangleleft G$ e:
  $$G / \ker(\phi) \cong \text{Im}(\phi)$$
- **Teorema de Lagrange**: Para grupo finito $G$ e subgrupo $H \le G$, a ordem $|H|$ divide $|G|$, sendo $[G:H] = |G|/|H|$.
- **Teoremas de Sylow**: Para um grupo finito $G$ de ordem $|G| = p^k m$ com $\gcd(p, m) = 1$:
  1. $G$ contém ao menos um subgrupo de ordem $p^k$ ($p$-Subgrupo de Sylow).
  2. Todos os $p$-subgrupos de Sylow são conjugados entre si.
  3. O número $n_p$ de $p$-subgrupos de Sylow satisfaz $n_p \equiv 1 \pmod p$ e $n_p$ divide $m$.

### 1.2 Anéis, Ideais e Domínios de Fatoração
- **Hierarquia de Anéis Comutativos**:
  $$\text{Corpos} \subset \text{Domínios Euclidianos (DE)} \subset \text{Domínios de Ideais Principais (DIP)} \subset \text{Domínios de Fatoração Única (DFU)} \subset \text{Domínios de Integridade}$$
- **Ideais Primos e Maximais**: Em um anel comutativo $R$ com unidade, um ideal $I$ é primo se e somente se $R/I$ é um domínio de integridade; $I$ é maximal se e somente se $R/I$ é um **corpo**.

---

## 🔬 2. Teoria de Corpos e Teoria de Galois

### 2.1 Extensões de Corpos e Corpos Finitos
- **Grau de Extensão $[E:F]$**: Dimensão de $E$ como espaço vetorial sobre $F$. Se $F \subseteq K \subseteq E$, então $[E:F] = [E:K] \cdot [K:F]$ (Teorema da Torre).
- **Corpos de Raízes (*Splitting Fields*)**: Menor extensão $E/F$ contendo todas as raízes de um polinômio $f(x) \in F[x]$.
- **Corpos Finitos de Galois $\mathbb{F}_{p^n} = GF(p^n)$**: Existência e unicidade a menos de isomorfismo para qualquer primo $p$ e inteiro $n \ge 1$, correspondendo ao corpo de raízes de $x^{p^n} - x$.

### 2.2 Teorema Fundamental da Teoria de Galois e Teorema de Abel-Ruffini
- Uma extensão finita $E/F$ é **Galoisiana** se for normal e separável ($\text{Gal}(E/F) = \text{Aut}(E/F)$ com $|\text{Gal}(E/F)| = [E:F]$).
- **Correspondência de Galois**: Existe uma bijeção invertendo inclusão entre subcorpos intermediários $F \subseteq K \subseteq E$ e subgrupos $H \le \text{Gal}(E/F)$ dada por $K = E^H$ e $H = \text{Gal}(E/K)$.
- **Teorema de Abel-Ruffini**: Equações polinomiais de grau $n \ge 5$ não são em geral solúveis por radicais, pois o grupo simétrico $S_n$ não é um grupo solúvel para $n \ge 5$ (o subgrupo alternado $A_n$ é simples para $n \ge 5$).

---

## 🌐 3. Álgebra Linear Avançada e Teorema Espectral

### 3.1 Espaços de Hilbert e Formas Quadráticas
- **Espaço de Hilbert**: Espaço vetorial munido de produto interno $\langle \mathbf{u}, \mathbf{v} \rangle$ que é completo sob a métrica induzida pela norma $\|\mathbf{u}\| = \sqrt{\langle \mathbf{u}, \mathbf{u} \rangle}$.
- **Teorema Espectral para Operadores Auto-Adjuntos (Hermitianos)**: Todo operador linear autoadjunto $T: V \to V$ admite uma base ortonormal de autovetores associados a autovalores puramente reais:
  $$T = \sum_{i=1}^n \lambda_i \mathbf{v}_i \mathbf{v}_i^\dagger$$
- **Forma Canônica de Jordan**: Qualquer operador linear sobre um corpo algebricamente fechado ($\mathbb{C}$) decompõe-se em blocos de Jordan $J_k(\lambda) = \lambda \mathbf{I} + \mathbf{N}$.

---

## 📐 4. Geometria Diferencial de Curvas e Superfícies (do Carmo)

### 4.1 Triedro de Frenet-Serret para Curvas no $\mathbb{R}^3$
Para uma curva $\boldsymbol{\alpha}(s)$ parametrizada por comprimento de arco ($s$):
$$\begin{bmatrix} \mathbf{T}' \\ \mathbf{N}' \\ \mathbf{B}' \end{bmatrix} = \begin{bmatrix} 0 & \kappa(s) & 0 \\ -\kappa(s) & 0 & \tau(s) \\ 0 & -\tau(s) & 0 \end{bmatrix} \begin{bmatrix} \mathbf{T} \\ \mathbf{N} \\ \mathbf{B} \end{bmatrix}$$

### 4.2 Formas Fundamentais e Curvaturas de Gauss e Média
Para uma superfície regular parametrizada $\mathbf{x}(u, v)$:
- **Primeira Forma Fundamental (Métrica)**: $I = E \, du^2 + 2F \, du \, dv + G \, dv^2$.
- **Segunda Forma Fundamental**: $II = e \, du^2 + 2f \, du \, dv + g \, dv^2$.
- **Curvatura Gaussiana Intrínseca (Theorema Egregium de Gauss)**:
  $$K = \frac{eg - f^2}{EG - F^2}$$
- **Teorema Global de Gauss-Bonnet**:
  $$\iint_M K \, dA + \int_{\partial M} \kappa_g \, ds = 2\pi \chi(M) = 2\pi (2 - 2g)$$
  onde $\chi(M)$ é a característica de Euler e $g$ é o gênero da superfície.

---

## 🌌 5. Variedades Diferenciáveis e Teorema de Stokes Geral

- **Espaço Tangente e Formas Diferenciais**: $\omega \in \Omega^k(M)$ com derivada exterior $d: \Omega^k(M) \to \Omega^{k+1}(M)$ tal que $d^2 = 0$.
- **Teorema de Stokes Geral**:
  $$\int_{\partial M} \omega = \int_M d\omega$$
  Unifica o Teorema Fundamental do Cálculo, Green, Divergência de Gauss e Stokes clássico.
