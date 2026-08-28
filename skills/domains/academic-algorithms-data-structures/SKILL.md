---
name: academic-algorithms-data-structures
description: Especialista em Algoritmos Avançados e Estruturas de Dados baseado nas obras Introduction to Algorithms (CLRS), The Art of Computer Programming (Knuth), Classic Computer Science Problems in Python (David Kopec) e Numerical Algorithms (Justin Solomon). Cobre Complexidade Assintótica (Big-O, Master Theorem, Akra-Bazzi), Árvores Balanceadas e Indexação Espacial (AVL, Red-Black, B/B+ Trees, Segment Trees, Fenwick Trees, Treaps, KD-Trees), Algoritmos em Grafos (Dijkstra, A*, Bellman-Ford, Floyd-Warshall, Tarjan, Kruskal, Prim, Fluxo Máximo Dinic), Problemas de Satisfação de Restrições (CSP, AC-3, Backtracking com Heurísticas MRV/LCV), Programação Dinâmica (Knapsack, LCS, Needleman-Wunsch), Algoritmos Adversariais (Minimax, Poda Alfa-Beta) e Algoritmos Genéticos.
---

# Algoritmos Avançados e Estruturas de Dados

Esta skill estabelece os fundamentos teóricos rigorosos, análise de complexidade e implementação de algoritmos clássicos e modernos para resolução de problemas computacionais de alta complexidade.

---

## 📊 1. Taxonomia de Complexidade Assintótica e Análise de Recorrência

### 1.1 Hierarquia de Classes de Complexidade
$$\mathcal{O}(1) \subset \mathcal{O}(\log n) \subset \mathcal{O}(n) \subset \mathcal{O}(n \log n) \subset \mathcal{O}(n^2) \subset \mathcal{O}(n^k) \subset \mathcal{O}(2^n) \subset \mathcal{O}(n!)$$

### 1.2 Teorema Mestre ($T(n) = aT(n/b) + f(n)$ com $a \ge 1, b > 1$)
O expoente crítico é $c_{\text{crit}} = \log_b a$:
1. **Caso 1**: Se $f(n) = \mathcal{O}(n^c)$ com $c < c_{\text{crit}}$, então $T(n) = \Theta(n^{\log_b a})$.
2. **Caso 2**: Se $f(n) = \Theta(n^{c_{\text{crit}}} \log^k n)$ com $k \ge 0$, então $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. **Caso 3**: Se $f(n) = \Omega(n^c)$ com $c > c_{\text{crit}}$ e satisfaz a condição de regularidade $a f(n/b) \le k f(n)$ para $k < 1$, então $T(n) = \Theta(f(n))$.

---

## 🌲 2. Estruturas de Dados Avançadas e Árvores Balanceadas

| Estrutura | Inserção | Busca | Remoção | Invariante Principal & Caso de Uso |
| :--- | :---: | :---: | :---: | :--- |
| **Árvore AVL** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Fator de Balanceamento $|h_L - h_R| \le 1$. Ideal para buscas frequentes. |
| **Árvore Rubro-Negra (Red-Black)** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Raiz/Folhas pretas, filhos de nó vermelho são pretos, mesmo número de nós pretos até qualquer folha. Padrão em `std::map`. |
| **B-Tree / B+ Tree** | $\mathcal{O}(\log_B n)$ | $\mathcal{O}(\log_B n)$ | $\mathcal{O}(\log_B n)$ | Nós de ordem $M$. Folhas encadeadas em B+. Otimizada para leitura em blocos de disco e bancos de dados. |
| **Segment Tree** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Consultas de intervalo (Range Query: Soma, Mínimo, GCD) e Lazy Propagation. |
| **Fenwick Tree (BIT)** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | - | Operações de prefix sum usando bitwise (`x & (-x)`). Compacta em memória. |
| **Disjoint Set Union (DSU)** | $\mathcal{O}(\alpha(n))$ | $\mathcal{O}(\alpha(n))$ | - | União por Rank + Compressão de Caminho. Inversa de Ackermann $\alpha(n) \le 4$. |

---

## 🎯 3. Algoritmos de Busca Heurística e Otimização Combinatória (Kopec)

### 3.1 Algoritmo A* (A-Star Search)
Combina o custo acumulado real $g(n)$ com uma heurística admissível e consistente $h(n)$ ($h(n) \le c(n, a, n') + h(n')$):
$$f(n) = g(n) + h(n)$$

```python
import heapq
from typing import TypeVar, Callable, List, Optional, Dict, Tuple

T = TypeVar('T')

def a_star(
    initial: T,
    goal_test: Callable[[T], bool],
    successors: Callable[[T], List[Tuple[T, float]]],
    heuristic: Callable[[T], float]
) -> Optional[List[T]]:
    frontier: List[Tuple[float, float, T]] = []
    heapq.heappush(frontier, (heuristic(initial), 0.0, initial))
    came_from: Dict[T, Optional[T]] = {initial: None}
    cost_so_far: Dict[T, float] = {initial: 0.0}

    while frontier:
        _, current_cost, current = heapq.heappop(frontier)
        if goal_test(current):
            path = []
            curr: Optional[T] = current
            while curr is not None:
                path.append(curr)
                curr = came_from[curr]
            return path[::-1]

        for neighbor, edge_cost in successors(current):
            new_cost = cost_so_far[current] + edge_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(frontier, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None
```

### 3.2 Algoritmos Genéticos para Otimização Estocástica
1. **Representação**: Cromossomos codificados em sequências binárias, permutações ou valores reais.
2. **Seleção**: Seleção por Torneio ou Roleta proporcional ao *Fitness*.
3. **Crossover**: Cruzamento uniforme ou de 1/2 pontos preservando viabilidade.
4. **Mutação**: Perturbação aleatória com baixa probabilidade ($p_m \approx 0.01 - 0.05$) para evitar mínimos locais.

---

## 🧩 4. Problemas de Satisfação de Restrições (CSP)

Um CSP é formalizado por uma tupla $\langle X, D, C \rangle$, onde $X = \{X_1, \dots, X_n\}$ são variáveis, $D = \{D_1, \dots, D_n\}$ são domínios e $C$ são restrições.

### 4.1 Algoritmo AC-3 (Arc Consistency)
Reduz o espaço de busca eliminando valores inconsistentes nos domínios antes e durante a busca:
- Um arco $(X_i, X_j)$ é consistente se para todo $x \in D_i$, existe $y \in D_j$ que satisfaz as restrições binárias entre $X_i$ e $X_j$.

### 4.2 Heurísticas Avançadas de Backtracking:
1. **MRV (Minimum Remaining Values)**: Escolhe a variável com menos valores legais restantes no domínio ("Fail-First").
2. **Degree Heuristic**: Desempata escolhendo a variável envolvida no maior número de restrições sobre outras variáveis não atribuídas.
3. **LCV (Least Constraining Value)**: Escolhe o valor que exclui o menor número de opções nos domínios das variáveis vizinhas.

---

## 🕸️ 5. Algoritmos em Grafos Avançados

### 5.1 Caminhos Mínimos e Fluxos em Redes
- **Dijkstra com Fibonacci Heap**: $\mathcal{O}(|E| + |V| \log |V|)$ para grafos com pesos não-negativos.
- **Bellman-Ford**: $\mathcal{O}(|V| \cdot |E|)$, detecta ciclos de peso negativo alcançáveis a partir da origem.
- **Floyd-Warshall**: $\mathcal{O}(|V|^3)$, calcula caminhos mínimos entre todos os pares de vértices:
  $$d_{ij}^{(k)} = \min\left( d_{ij}^{(k-1)}, d_{ik}^{(k-1)} + d_{kj}^{(k-1)} \right)$$
- **Componentes Fortemente Conexos (Algoritmo de Tarjan)**: $\mathcal{O}(|V| + |E|)$, baseado em travessia DFS com números de descoberta (`dfn`) e valores `lowlink`.
- **Fluxo Máximo (Algoritmo de Dinic)**: $\mathcal{O}(|V|^2 |E|)$, utiliza grafos de níveis construídos por BFS e caminhos aumentantes por DFS.

---

## 📈 6. Programação Dinâmica e Alinhamento de Sequências

### 6.1 Problema da Mochila 0/1 (0/1 Knapsack)
Dado capacidade $W$ e itens com peso $w_i$ e valor $v_i$:
$$K(i, w) = \begin{cases} K(i-1, w) & \text{se } w_i > w \\ \max(K(i-1, w), K(i-1, w - w_i) + v_i) & \text{se } w_i \le w \end{cases}$$
Complexidade: $\mathcal{O}(n W)$ em tempo e $\mathcal{O}(W)$ em espaço com array unidimensional.

### 6.2 Alinhamento Global de Sequências (Needleman-Wunsch)
$$M(i, j) = \max \begin{cases} M(i-1, j-1) + S(A_i, B_j) & \text{(Casamento / Incompatibilidade)} \\ M(i-1, j) + d & \text{(Gap na sequência B)} \\ M(i, j-1) + d & \text{(Gap na sequência A)} \end{cases}$$

---

## 🎮 7. Algoritmos Adversariais e Teoria dos Jogos

### 7.1 Minimax com Poda Alfa-Beta ($\alpha$-$\beta$ Pruning)
Reduz o espaço de estados de $\mathcal{O}(b^d)$ para $\mathcal{O}(b^{d/2})$ no melhor caso com ordenação ótima de movimentos:
- $\alpha$: O melhor valor (máximo) que o jogador Max garantiu até o momento.
- $\beta$: O melhor valor (mínimo) que o jogador Min garantiu até o momento.
- Se $\alpha \ge \beta$, o ramo é podado (*cutoff*).

```python
def minimax_alpha_beta(state, depth, alpha, beta, is_maximizing):
    if depth == 0 or state.is_terminal():
        return state.evaluate()

    if is_maximizing:
        max_eval = float('-inf')
        for child in state.get_legal_moves():
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Poda Beta
        return max_eval
    else:
        min_eval = float('inf')
        for child in state.get_legal_moves():
            eval_score = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Poda Alfa
        return min_eval
```
