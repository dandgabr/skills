---
name: academic-robotics-kinematics-dynamics
description: Especialista em Robótica e Manipuladores baseada na obra Introduction to Robotics Mechanics and Control (John J. Craig). Cobre Parâmetros de Denavit-Hartenberg (DH), Cinemática Direta e Inversa, Jacobiano Robótico e Singularidades, Dinâmica de Lagrange-Euler e Newton-Euler, Planejamento de Trajetórias, Robótica Móvel, Cinemática Diferencial, Robot Operating System (ROS 2) e SLAM.
---

# Robótica Industrial e Móvel (Craig)

Esta skill estabelece as equações cinemáticas, dinâmicas e de controle para braços manipuladores e robôs móveis autônomos.

---

## 🦾 1. Cinemática de Manipuladores (Convenção Denavit-Hartenberg)

A matriz de transformação homogênea entre juntas consecutivas $^{i-1}\mathbf{T}_i$:
$$^{i-1}\mathbf{T}_i = \begin{bmatrix}
\cos\theta_i & -\sin\theta_i\cos\alpha_i & \sin\theta_i\sin\alpha_i & a_i\cos\theta_i \\
\sin\theta_i & \cos\theta_i\cos\alpha_i & -\cos\theta_i\sin\alpha_i & a_i\sin\theta_i \\
0 & \sin\alpha_i & \cos\alpha_i & d_i \\
0 & 0 & 0 & 1
\end{bmatrix}$$

---

## ⚡ 2. Dinâmica de Lagrange-Euler do Robô

$$\mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau}$$
onde $\mathbf{M}(\mathbf{q})$ é a matriz de inércia simétrica e positiva definida, $\mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})$ representa as forças de Coriolis e centrífugas, $\mathbf{g}(\mathbf{q})$ é o vetor de gravidade e $\boldsymbol{\tau}$ são os torques atuadores nas juntas.
