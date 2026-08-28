---
name: academic-algorithms-data-structures
description: Especialista em Algoritmos Avançados e Estruturas de Dados baseado nas obras Introduction to Algorithms (CLRS) e The Art of Computer Programming (Knuth). Cobre complexidade assintótica (Big-O, Omega, Theta), árvores balanceadas (AVL, Red-Black, B-Trees, Treaps), algoritmos em grafos (Dijkstra, Bellman-Ford, Floyd-Warshall, Tarjan, Kruskal, Prim, Fluxo Máximo Ford-Fulkerson), programação dinâmica e algoritmos gulosos.
---

# Algoritmos Avançados e Estruturas de Dados (CLRS)

Esta skill estabelece os fundamentos teóricos de análise assintótica, projeto algorítmico e estruturas de dados de alta eficiência para computação em larga escala.

---

## 📊 1. Taxonomia de Complexidade Assintótica

$$\mathcal{O}(1) \subset \mathcal{O}(\log n) \subset \mathcal{O}(n) \subset \mathcal{O}(n \log n) \subset \mathcal{O}(n^2) \subset \mathcal{O}(2^n) \subset \mathcal{O}(n!)$$

- **Teorema Mestre para Relações de Recorrência** $T(n) = aT(n/b) + f(n)$:
  1. Se $f(n) = \mathcal{O}(n^{\log_b a - \epsilon})$, então $T(n) = \Theta(n^{\log_b a})$.
  2. Se $f(n) = \Theta(n^{\log_b a})$, então $T(n) = \Theta(n^{\log_b a} \log n)$.
  3. Se $f(n) = \Omega(n^{\log_b a + \epsilon})$, então $T(n) = \Theta(f(n))$.

---

## 🌲 2. Estruturas de Dados Avançadas e Árvores Balanceadas

| Estrutura | Inserção (Pior Caso) | Busca (Pior Caso) | Remoção (Pior Caso) | Caso de Uso Primário |
| :--- | :---: | :---: | :---: | :--- |
| **Árvore AVL** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Bases estáticas com leituras intensivas. |
| **Árvore Rubro-Negra (Red-Black)** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | `std::map` (C++), `TreeMap` (Java), schedulers de SO. |
| **B-Tree / B+ Tree** | $\mathcal{O}(\log_B n)$ | $\mathcal{O}(\log_B n)$ | $\mathcal{O}(\log_B n)$ | Motores de banco de dados (InnoDB, Postgres) e File Systems. |
