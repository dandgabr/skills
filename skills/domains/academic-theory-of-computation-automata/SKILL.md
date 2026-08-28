---
name: academic-theory-of-computation-automata
description: Especialista em Teoria da Computação, Linguagens Formais e Teoria dos Autômatos baseado na obra Introduction to the Theory of Computation (Michael Sipser). Cobre Hierarquia de Chomsky, Autômatos Finitos (DFA/NFA), Expressões Regulares, Autômatos de Pilha (PDA), Gramáticas Livres de Contexto, Máquinas de Turing, Problema da Parada, Decidibilidade e Classes de Complexidade P, NP, NP-Completo e PSPACE.
---

# Teoria da Computação e Linguagens Formais (Sipser)

Esta skill estabelece as fronteiras matemáticas da computabilidade e complexidade, formalizando modelos abstratos de computação e decidibilidade de problemas.

---

## 🏛️ 1. A Hierarquia de Chomsky

```
┌─────────────────────────────────────────────────────────────┐
│ Tipo 0: Linguagens Recursivamente Enumeráveis (Máq. Turing) │
├─────────────────────────────────────────────────────────────┤
│ Tipo 1: Linguagens Sensíveis ao Contexto (Autômato Linear)   │
├─────────────────────────────────────────────────────────────┤
│ Tipo 2: Linguagens Livres de Contexto (Autômatos de Pilha)  │
├─────────────────────────────────────────────────────────────┤
│ Tipo 3: Linguagens Regulares (Autômatos Finitos DFA / NFA)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 2. O Problema da Parada e Reduções Polinomiais

- **Linguagem da Parada $A_{TM} = \{ \langle M, w \rangle \mid M \text{ é uma Máquina de Turing e } M \text{ aceita } w \}$**:
  - Provado indecidível por contradição e diagonalização de Cantor.
- **Teorema de Cook-Levin**: O problema SAT (Satisfatibilidade Booleana) é **NP-Completo**.
- **Redução de Karp**: Se $A \le_p B$ e $A$ é NP-difícil, então $B$ é NP-difícil.
