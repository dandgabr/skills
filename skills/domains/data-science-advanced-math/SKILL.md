---
name: data-science-advanced-math
description: Especialista em Matemática Avançada e Fundamentos Estatísticos para Ciência de Dados e Machine Learning baseado nas obras Essential Math for Data Science (Thomas Nield) e Data Science The Hard Parts (Daniel Vaughan). Cobre Álgebra Linear (Autovalores, SVD, PCA), Cálculo Multivariado (Gradiente Descendente, Jacobiano), Probabilidade e Teorema de Bayes, Inferência Estatística e Testes de Hipótese (p-value, A/B Testing).
---

# Matemática Avançada para Ciência de Dados e Machine Learning

Esta skill estabelece os fundamentos matemáticos e estatísticos rigorosos necessários para modelagem preditiva, otimização de algoritmos de Machine Learning e tomada de decisão orientada a dados.

---

## 📊 1. Álgebra Linear Aplicada a Dados

### Decomposição em Valores Singulares (SVD) e PCA
- **SVD**: Fatora qualquer matriz $A_{m 	imes n}$ em $U_{m 	imes m} \Sigma_{m 	imes n} V^T_{n 	imes n}$.
- **PCA (Principal Component Analysis)**: Projeta dados de alta dimensionalidade nos autovetores correspondentes aos maiores autovalores da matriz de covariância, maximizando a variância explicada com menor custo computacional.

---

## 📈 2. Cálculo e Otimização Numérica

### Gradiente Descendente e Otimizadores Modernos
- **Vetor Gradiente**: $
abla f(x) = \left[ rac{\partial f}{\partial x_1}, rac{\partial f}{\partial x_2}, \dots, rac{\partial f}{\partial x_n} ight]^T$
- **Regra de Atualização**:
  $$x_{t+1} = x_t - \eta 
abla f(x_t)$$
  onde $\eta$ é a taxa de aprendizado (*learning rate*).
- **Otimizadores Avançados**: Momentum, RMSprop e Adam (Adaptive Moment Estimation).
