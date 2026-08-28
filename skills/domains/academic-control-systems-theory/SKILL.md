---
name: academic-control-systems-theory
description: Especialista em Engenharia de Controle Clássico e Moderno baseado nas obras Modern Control Engineering (Katsuhiko Ogata) e Feedback Control of Dynamic Systems (Franklin, Powell). Cobre Modelagem de Sistemas Dinâmicos, Controladores PID, Lugar das Raízes (Root Locus), Diagramas de Bode e Nyquist, Espaço de Estados (State-Space), Controlabilidade, Observabilidade, Regulador Linear Quadrático (LQR) e Filtro de Kalman.
---

# Teoria de Controle Clássico e Moderno (Ogata & Franklin)

Esta skill estabelece os métodos formais para análise de estabilidade, sintetização de controladores e observadores de estado para plantas lineares (SISO e MIMO) e não-lineares.

---

## 🎯 1. Controle Clássico: PID e Função de Transferência

Função de transferência de um controlador PID em tempo contínuo:
$$C(s) = K_p + \frac{K_i}{s} + K_d s = K_p \left( 1 + \frac{1}{T_i s} + T_d s \right)$$

Critério de Estabilidade de Routh-Hurwitz e Margem de Fase ($\text{MF}$):
$$\text{MF} = 180^\circ + \angle L(j\omega_{gc}) \quad \text{onde } |L(j\omega_{gc})| = 1$$

---

## 🔄 2. Controle Moderno em Espaço de Estados

$$\begin{aligned}
\dot{\mathbf{x}}(t) &= \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t) \\
\mathbf{y}(t) &= \mathbf{C}\mathbf{x}(t) + \mathbf{D}\mathbf{u}(t)
\end{aligned}$$

- **Matriz de Controlabilidade**: $\mathcal{C} = \begin{bmatrix} \mathbf{B} & \mathbf{AB} & \mathbf{A}^2\mathbf{B} & \dots & \mathbf{A}^{n-1}\mathbf{B} \end{bmatrix}$ (Posto pleno $= n$).
- **Matriz de Observabilidade**: $\mathcal{O} = \begin{bmatrix} \mathbf{C}^T & (\mathbf{CA})^T & (\mathbf{CA}^2)^T & \dots & (\mathbf{CA}^{n-1})^T \end{bmatrix}^T$ (Posto pleno $= n$).
- **Lei de Controle por Realimentação de Estados**: $\mathbf{u}(t) = -\mathbf{K}\mathbf{x}(t) + \mathbf{r}(t)$.
