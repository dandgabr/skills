---
name: academic-classical-mechanics-relativity
description: Especialista em Mecânica Clássica Avançada (Formalismos Newtoniano, Lagrangeano e Hamiltoniano), Dinâmica de Corpos Rígidos, Teoria do Caos e Teoria da Relatividade Especial e Geral (Métricas de Lorentz e Einstein).
---

# Mecânica Clássica Avançada e Teoria da Relatividade

Esta skill abrange a dinâmica analítica de partículas e corpos rígidos através das equações de Euler-Lagrange e equações canônicas de Hamilton, bem como a relatividade do espaço-tempo.

---

## ⚙️ 1. Formalismo Lagrangeano e Hamiltoniano

- **Lagrangeana**: $L(q, \dot{q}, t) = T - V$
- **Equações de Euler-Lagrange**:
  $$\frac{d}{dt}\left( \frac{\partial L}{\partial \dot{q}_i} \right) - \frac{\partial L}{\partial q_i} = 0$$
- **Hamiltoniana**: $H(q, p, t) = \sum_i p_i \dot{q}_i - L$ com momento conjugado $p_i = \frac{\partial L}{\partial \dot{q}_i}$:
  $$\dot{q}_i = \frac{\partial H}{\partial p_i}, \quad \dot{p}_i = -\frac{\partial H}{\partial q_i}$$

---

## 🌌 2. Relatividade Especial e Invariante Espaço-Temporal

O intervalo espaço-temporal $ds^2$ no espaço de Minkowski com métrica $\eta_{\mu\nu} = \text{diag}(-c^2, 1, 1, 1)$:
$$ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2 = \eta_{\mu\nu} dx^\mu dx^\nu$$
Transformações de Lorentz para velocidade relativa $v$ ao longo do eixo $x$:
$$x' = \gamma (x - vt), \quad t' = \gamma \left( t - \frac{vx}{c^2} \right) \quad \text{com } \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$$
