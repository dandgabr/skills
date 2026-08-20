# 📚 Guia de Técnicas de Teste de Caixa-Preta (Black-Box Testing)

Este guia consolida as técnicas formais de projeto de casos de teste funcionais (caixa-preta), baseadas nas obras de **Paul C. Jorgensen** (*Software Testing: A Craftsman's Approach*), **Brian Hambling et al.** (*Software Testing: ISTQB Guide*) e **Ali Mili & Fairouz Tchier** (*Software Testing: Concepts and Operations*).

---

## 1. Análise de Valor Limite (Boundary Value Analysis - BVA)

A Análise de Valor Limite baseia-se na constatação empírica de que a maior densidade de defeitos ocorre nos extremos dos domínios de entrada.

### 1.1. Valores Canônicos de Teste por Variável
Para uma variável $x$ definida no intervalo $[a, b]$, definimos os pontos de amostragem:
- **$a$**: Mínimo exato ($min$)
- **$a^+$**: Imediatamente acima do mínimo ($min+$)
- **$nom$**: Valor nominal (típico / médio)
- **$b^-$**: Imediatamente abaixo do máximo ($max-$)
- **$b$**: Máximo exato ($max$)
- **$a^-$**: Abaixo do mínimo ($min-$) [Inválido / Robusto]
- **$b^+$**: Acima do máximo ($max+$) [Inválido / Robusto]

### 1.2. Taxonomia de Técnicas de BVA (Jorgensen)

| Técnica | Hipótese de Falha | Pontos por Variável | Total de Testes ($n$ variáveis) | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| **BVA Tradicional** | Falha Simples (Single Fault Assumption) | $min, min+, nom, max-, max$ | $4n + 1$ | Varia 1 variável nos 4 limites mantendo as outras em $nom$, mais 1 caso nominal completo. |
| **Teste de Robustez** | Falha Simples (com valores inválidos) | $min-, min, min+, nom, max-, max, max+$ | $6n + 1$ | Inclui valores fora do domínio válido para testar tratamento de exceções. |
| **Teste de Pior Caso (Worst-Case)** | Falha Múltipla (Multiple Fault Assumption) | $min, min+, nom, max-, max$ | $5^n$ | Produto cartesiano de todos os 5 pontos de todas as variáveis. |
| **Pior Caso Robusto (Robust Worst-Case)** | Falha Múltipla (com valores inválidos) | $min-, min, min+, nom, max-, max, max+$ | $7^n$ | Produto cartesiano completo dos 7 pontos por variável. |

---

## 2. Teste de Partição de Equivalência (Equivalence Partitioning - EP)

A partição de equivalência divide o domínio de entrada em classes onde o comportamento do programa é assumido como uniforme.

### 2.1. Classificação Formal das Partições (Jorgensen)
- **Classes Válidas ($V_i$)**: Subconjuntos de dados esperados e aceitos pela especificação.
- **Classes Inválidas ($I_j$)**: Subconjuntos de dados não aceitos (valores fora do intervalo, formatos incorretos, tipos inválidos).

### 2.2. Níveis de Rigor em Partições de Equivalência

1. **Normal Fraca (Weak Normal)**:
   - Baseia-se na hipótese de falha simples.
   - Seleciona 1 valor de cada partição válida $V_i$.
   - Número de testes: $\max(|Classes(V_1)|, |Classes(V_2)|, \dots, |Classes(V_n)|)$.
2. **Normal Forte (Strong Normal)**:
   - Baseia-se na hipótese de falhas múltiplas (interações).
   - Cobre o produto cartesiano de todas as classes válidas: $V_1 \times V_2 \times \dots \times V_n$.
3. **Robusta Fraca (Weak Robust)**:
   - Cobre 1 valor de cada classe válida e 1 valor de cada classe inválida, testando classes inválidas isoladamente (uma por teste).
4. **Robusta Forte (Strong Robust)**:
   - Cobre o produto cartesiano de todas as classes válidas e inválidas.

---

## 3. Teste Baseado em Tabela de Decisão (Decision Table-Based Testing)

Ideal para regras de negócio complexas, relacionamentos lógicos intrincados e combinações condicionais.

### 3.1. Estrutura Canônica da Tabela de Decisão

```
+------------------------------------+-------+-------+-------+-------+
| Condições / Entradas               | Regra 1| Regra 2| Regra 3| Regra 4|
+------------------------------------+-------+-------+-------+-------+
| C1: Saldo suficiente               |   T   |   T   |   F   |   F   |
| C2: Cartão ativo e desbloqueado    |   T   |   F   |   T   |   F   |
| C3: Limite diário não excedido     |   T   |   -   |   -   |   -   |
+------------------------------------+-------+-------+-------+-------+
| Ações / Saídas Esperadas           |       |       |       |       |
+------------------------------------+-------+-------+-------+-------+
| A1: Aprovar transação              |   X   |       |       |       |
| A2: Recusar por cartão bloqueado   |       |   X   |       |       |
| A3: Recusar por saldo insuficiente |       |       |   X   |   X   |
+------------------------------------+-------+-------+-------+-------+
```

### 3.2. Regras de Engenharia para Tabelas de Decisão
1. **Completude (Completeness)**: Para $k$ condições binárias, a tabela completa deve representar $2^k$ regras elementares.
2. **Consistência (Consistency)**: Nenhuma coluna idêntica nas condições pode levar a ações divergentes ou contraditórias.
3. **Simplificação e Don't Care ($-$)**: Se o valor de uma condição não altera a ação resultante, combine as colunas usando a regra de absorção booleana. Uma regra com $m$ entradas "don't care" representa $2^m$ regras elementares.

---

## 4. Teste de Transição de Estados (State Transition Testing)

Aplicado a sistemas reativos cujo comportamento depende do histórico de eventos e do estado atual (Finite State Machines - FSM).

### 4.1. Elementos da FSM
- **Estados ($S$)**: Conjunto finito de estados possíveis.
- **Eventos / Entradas ($E$)**: Estímulos que provocam transições.
- **Ações / Saídas ($A$)**: Respostas produzidas pelo sistema.
- **Transições ($T: S \times E \rightarrow S \times A$)**: Relação de mudança de estado.

### 4.2. Critérios de Cobertura de Estados (ISTQB & Jorgensen)
- **Cobertura de Estados (All States)**: Todo estado válido $s \in S$ é visitado pelo menos uma vez.
- **Cobertura de Transições (0-switch / All Transitions)**: Toda transição válida $t \in T$ é executada pelo menos uma vez.
- **Cobertura de Pares de Transições (1-switch / Transition Pairs)**: Toda sequência de duas transições consecutivas ($S_1 \xrightarrow{E_1} S_2 \xrightarrow{E_2} S_3$) é exercitada.
- **Testes de Transições Inválidas**: Enviar eventos proibidos para o estado atual e verificar se o sistema rejeita a transição sem corromper o estado.

---

## 5. Testes Combinatoriais e All-Pairs (Pairwise Testing)

Quando o número de parâmetros e valores gera explosão combinatória inviável para produto cartesiano completo, a técnica All-Pairs garante que todo par de valores entre quaisquer dois parâmetros seja testado em pelo menos um caso de teste.

### 5.1. Fundamentação Matemática
- Baseado em **Matrizes Ortogonais (Orthogonal Arrays)** $OA(N, k, v, t)$, onde:
  - $N$: Número de execuções de teste
  - $k$: Número de parâmetros
  - $v$: Número de níveis/valores por parâmetro
  - $t$: Força de interação (geralmente $t=2$ para pairwise)
- **Eficácia Prática**: Estudos empíricos (NIST) comprovam que mais de 70-85% dos defeitos de software são disparados pela interação de no máximo 2 variáveis, e mais de 95% por até 3 variáveis.

---

## 6. Testes Baseados em Casos de Uso (Use Case Testing)

Mapeamento de cenários derivados dos fluxos de negócios:
- **Fluxo Básico (Happy Path)**: Sequência típica de sucesso sem desvios.
- **Fluxos Alternativos**: Variações válidas para atingir o objetivo de negócio.
- **Fluxos de Exceção**: Tratamento de erros, interrupções e falhas de pré-condição.
- **Matriz de Rastreabilidade**: Garantir cobertura 1:1 entre passos do caso de uso e casos de teste executáveis.
