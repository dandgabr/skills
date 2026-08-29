---
name: academic-electromagnetism-electrodynamics
description: Especialista em Eletromagnetismo Clássico e Eletrodinâmica Avançada baseado nas obras Introduction to Electrodynamics (David J. Griffiths) e Classical Electrodynamics (John David Jackson). Cobre as Equações de Maxwell Diferenciais e Integrais, Calibres de Lorenz e Coulomb, Potenciais Retardados e de Liénard-Wiechert, Teoria da Radiação Eletromagnética e Fórmula de Larmor, Propagação de Ondas em Meios Materiais e Condutores (Efeito Pelicular/Skin Depth e Relações de Kramers-Kronig), Teoria de Guias de Onda (Modos TE, TM e TEM) e Formulação Covariante Quadridimensional do Eletromagnetismo.
---

# Eletromagnetismo Clássico e Eletrodinâmica de Maxwell (Griffiths & Jackson)

Esta skill estabelece a teoria unificada de campos elétricos e magnéticos estáticos e dependentes do tempo em meios materiais, propagação de ondas eletromagnéticas, guias de onda, radiação por cargas aceleradas e a formulação relativística covariante.

---

## ⚡ 1. As Equações de Maxwell Fundamentais

### 1.1 Forma Diferencial e Integral em Meios Materiais Lineares
$$\begin{aligned}
\nabla \cdot \mathbf{D} &= \rho_f &\iff \oiint_{\partial V} \mathbf{D} \cdot d\mathbf{a} &= Q_{f,enc} \quad &\text{(Lei de Gauss)} \\
\nabla \cdot \mathbf{B} &= 0 &\iff \oiint_{\partial V} \mathbf{B} \cdot d\mathbf{a} &= 0 \quad &\text{(Ausência de Monopolos)} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} &\iff \oint_{\partial S} \mathbf{E} \cdot d\mathbf{l} &= -\frac{d\Phi_B}{dt} \quad &\text{(Lei de Faraday)} \\
\nabla \times \mathbf{H} &= \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t} &\iff \oint_{\partial S} \mathbf{H} \cdot d\mathbf{l} &= I_{f,enc} + \iint_S \frac{\partial \mathbf{D}}{\partial t} \cdot d\mathbf{a} \quad &\text{(Lei de Ampère-Maxwell)}
\end{aligned}$$

- **Relações Constitutivas**: $\mathbf{D} = \varepsilon \mathbf{E} = \varepsilon_0 \mathbf{E} + \mathbf{P}$ e $\mathbf{H} = \frac{1}{\mu} \mathbf{B} = \frac{1}{\mu_0}\mathbf{B} - \mathbf{M}$, com Lei de Ohm local $\mathbf{J}_f = \sigma \mathbf{E}$.

### 1.2 Teorema e Vetor de Poynting (Conservação de Energia)
$$\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad [\text{W/m}^2], \quad -\frac{\partial u_{em}}{\partial t} = \nabla \cdot \mathbf{S} + \mathbf{J}_f \cdot \mathbf{E}$$
onde $u_{em} = \frac{1}{2} (\varepsilon |\mathbf{E}|^2 + \mu |\mathbf{H}|^2)$ é a densidade de energia volumétrica.

---

## 🔮 2. Teoria de Potenciais, Calibres e Potenciais Retardados

### 2.1 Calibres de Lorenz e Coulomb
Definindo $\mathbf{B} = \nabla \times \mathbf{A}$ e $\mathbf{E} = -\nabla V - \frac{\partial \mathbf{A}}{\partial t}$:
- **Calibre de Lorenz**: $\nabla \cdot \mathbf{A} + \mu\varepsilon \frac{\partial V}{\partial t} = 0 \implies$ Desacopla as equações de onda não-homogêneas:
  $$\nabla^2 V - \frac{1}{c^2}\frac{\partial^2 V}{\partial t^2} = -\frac{\rho}{\varepsilon_0}, \quad \nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = -\mu_0 \mathbf{J}$$
- **Potenciais Retardados ($t_r = t - \frac{|\mathbf{r} - \mathbf{r}'|}{c}$)**:
  $$V(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0} \int \frac{\rho(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} d^3\mathbf{r}', \quad \mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} d^3\mathbf{r}'$$

### 2.2 Potenciais de Liénard-Wiechert para Cargas Pontuais
Para uma carga $q$ com trajetória $\mathbf{w}(t)$ e velocidade $\boldsymbol{\beta} = \frac{\mathbf{v}}{c}$:
$$V(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0} \frac{q}{(r - \mathbf{r} \cdot \boldsymbol{\beta})}, \quad \mathbf{A}(\mathbf{r}, t) = \frac{\mathbf{v}(t_r)}{c^2} V(\mathbf{r}, t)$$

---

## 📡 3. Radiação Eletromagnética e Guias de Onda

### 3.1 Radiação de Cargas Aceleradas e Fórmula de Larmor
A potência total irradiada por uma partícula carregada acelerada não-relativística no vácuo:

$$P = \frac{\mu_0 q^2 a^2}{6\pi c} = \frac{q^2 a^2}{6\pi \varepsilon_0 c^3}$$

- **Generalização Relativística de Liénard**:
  $$P = \frac{\mu_0 q^2 \gamma^6}{6\pi c} \left( a^2 - \left|\frac{\mathbf{v} \times \mathbf{a}}{c}\right|^2 \right)$$

### 3.2 Propagação em Condutores e Efeito Pelicular (*Skin Effect*)
Em meios com alta condutividade $\sigma \gg \omega\varepsilon$, o vetor de onda torna-se complexo $k = \beta + i/\delta$:
$$\delta = \sqrt{\frac{2}{\omega \mu \sigma}} \quad \text{(Profundidade Pelicular / Skin Depth)}$$

### 3.3 Guias de Onda Retangulares (Dimensões $a \times b$)
- **Frequência de Corte para Modos $TE_{mn}$ e $TM_{mn}$**:
  $$\omega_{mn} = c \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$
- **Modo Fundamental $TE_{10}$ ($a > b$)**: Menor frequência de corte $\omega_{10} = \frac{\pi c}{a}$, com velocidade de fase $v_p = \frac{c}{\sqrt{1 - (\omega_{10}/\omega)^2}} > c$ e velocidade de grupo $v_g = c \sqrt{1 - (\omega_{10}/\omega)^2} < c$ ($v_p \cdot v_g = c^2$).
