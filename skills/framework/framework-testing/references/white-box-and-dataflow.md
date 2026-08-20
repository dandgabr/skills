# 🔬 Guia de Teste Estrutural (Caixa-Branca), Fluxo de Controle e Fluxo de Dados

Este guia aborda os fundamentos teóricos e matemáticos do teste estrutural de software (caixa-branca), derivado dos trabalhos de **Paul C. Jorgensen**, **Ali Mili & Fairouz Tchier** e diretrizes de confiabilidade crítica (RTCA DO-178C / ISO 26262).

---

## 1. Grafo de Fluxo de Controle (Control Flow Graph - CFG) e DD-Paths

O Grafo de Fluxo de Controle $G = (V, E)$ modela todos os caminhos de execução possíveis de uma unidade de software, onde $V$ são blocos básicos de instruções e $E$ são os arcos direcionados de transferência de controle.

### 1.1. Caminhos de Decisão para Decisão (DD-Paths - Jorgensen)
Um DD-Path é uma cadeia de nós em um CFG onde:
1. Consiste em um único nó com grau de entrada $\ge 2$ (nó de junção), OU
2. Consiste em um único nó com grau de saída $\ge 2$ (nó de decisão), OU
3. É um caminho maximal de nós com grau de entrada $\le 1$ e grau de saída $\le 1$ (sequência linear sem bifurcações).

A compressão de um CFG em um grafo de DD-Paths preserva todas as propriedades de teste de fluxo de controle, simplificando a análise estrutural.

---

## 2. Complexidade Ciclomática de McCabe e Teste de Caminhos Básicos

A Complexidade Ciclomática $V(G)$ mede a quantidade de caminhos linearmente independentes na base do espaço vetorial do grafo.

### 2.1. Fórmulas de Cálculo
Para um grafo com $e$ arestas, $n$ nós e $p$ componentes conectados (geralmente $p=1$ para uma função):
$$V(G) = e - n + 2p$$

Para grafos planares onde todas as decisões são binárias (predicados simples $d$):
$$V(G) = d + 1$$
$$V(G) = \text{Número de regiões fechadas no plano} + 1$$

### 2.2. Algoritmo do Teste de Caminhos Básicos (Basis Path Testing)
1. **Desenhe o CFG** correspondente ao código.
2. **Calcule $V(G)$** para determinar o tamanho exato da base de caminhos linearmente independentes.
3. **Selecione o Caminho Base**: Escolha um caminho representativo da execução típica do sistema.
4. **Gere os Caminhos Derivados**: Altere sistematicamente o desfecho de cada predicado ao longo do caminho base para derivar $V(G)$ caminhos ortogonais.
5. **Formule os Casos de Teste**: Defina valores de entrada que forcem o fluxo do programa através de cada caminho da base.

---

## 3. Hierarquia de Cobertura de Fluxo de Controle

```
         [ Multiple Condition Coverage (MCC) ]
                         │
                         ▼
        [ Modified Condition/Decision Coverage (MC/DC) ]
                         │
                         ▼
         [ Decision / Branch Coverage (C1) ]
                         │
                         ▼
         [ Statement Coverage (C0) ]
```

### 3.1. Cobertura de Instruções (Statement Coverage - $C_0$)
- Exige que toda instrução executável seja percorrida pelo menos uma vez.
- **Fórmula**: $\text{Cobertura } C_0 = \frac{\text{Instruções Executadas}}{\text{Total de Instruções}} \times 100\%$.
- **Limitação**: Insensível a ramos vazios (`if (cond) { ... }` sem `else`), podendo deixar ramos e condições totalmente não testados.

### 3.2. Cobertura de Ramos / Decisão (Branch / Decision Coverage - $C_1$)
- Exige que cada decisão condicional seja avaliada como Verdadeira (T) e Falsa (F) em execuções distintas.
- Garante $100\%$ de cobertura $C_0$, mas não avalia condições atômicas internas em expressões compostas.

### 3.3. Modified Condition/Decision Coverage (MC/DC)
Exigida para softwares com nível de criticidade máximo (ex: aviônica DO-178C Nível A).

**Requisitos do MC/DC**:
1. Toda decisão atinge todos os resultados possíveis (T e F).
2. Toda condição atômica dentro da decisão atinge todos os resultados possíveis (T e F).
3. Cada condição atômica é demonstrada afetar de forma **independente** o resultado da decisão (variando apenas essa condição enquanto as outras permanecem fixas ou sem efeito de curto-circuito).

Para uma decisão com $n$ condições atômicas:
- **Número de testes exigidos**: $n + 1$ testes (em contraste com $2^n$ do MCC completo).

#### Exemplo de Tabela de Independência MC/DC para $(A \lor B) \land C$:

| Teste | A | B | C | Resultado Decisão | Par de Teste para A | Par de Teste para B | Par de Teste para C |
| :---: | :-: | :-: | :-: | :---: | :---: | :---: | :---: |
| 1 | **T** | F | **T** | **T** | (1, 2) | | (1, 4) |
| 2 | **F** | F | **T** | **F** | (1, 2) | (3, 2) | |
| 3 | F | **T** | **T** | **T** | | (3, 2) | (3, 5) |
| 4 | T | F | **F** | **F** | | | (1, 4) |
| 5 | F | T | **F** | **F** | | | (3, 5) |

---

## 4. Teste de Fluxo de Dados (Data Flow Testing - Jorgensen & Mili)

Focaliza o ciclo de vida das variáveis dentro do programa: criação, modificação e uso.

### 4.1. Definições Fundamentais
- **$\text{def}(v, n)$**: O valor da variável $v$ é definido ou modificado no nó $n$ (ex: atribuição `v = expr;`, leitura de entrada).
- **$\text{use}(v, n)$**: O valor da variável $v$ é referenciado no nó $n$.
  - **c-use (computational use)**: Uso em cálculo aritmético ou atribuição direta.
  - **p-use (predicate use)**: Uso em expressão condicional que decide o fluxo de controle.
- **Caminho Livre de Definição (Def-Clear Path)**: Um caminho subjacente entre o nó $i$ e o nó $j$ para a variável $v$ onde nenhuma nova definição de $v$ ocorre nos nós intermediários.
- **du-path (Definition-Use Path)**: Caminho simples do nó de definição $\text{def}(v, i)$ ao nó de uso $\text{use}(v, j)$ que é livre de definição para $v$.

### 4.2. Critérios de Cobertura de Fluxo de Dados

| Critério | Exigência |
| :--- | :--- |
| **All-Defs** | Para cada definição de $v$ em $n$, o conjunto de testes deve conter pelo menos um def-clear path até algum uso ($\text{c-use}$ ou $\text{p-use}$). |
| **All-P-Uses** | Para cada definição de $v$ e cada $\text{p-use}$ alcançável, deve haver um def-clear path executado. |
| **All-C-Uses** | Para cada definição de $v$ e cada $\text{c-use}$ alcançável, deve haver um def-clear path executado. |
| **All-Uses** | Cobre pelo menos um def-clear path de cada definição para todo uso possível ($\text{c-use}$ e $\text{p-use}$). |
| **All-DU-Paths** | Cobre **todos** os du-paths simples e livres de definição entre todas as definições e todos os seus usos. (Critério mais rigoroso de fluxo de dados). |

---

## 5. Fatiamento de Programa (Program Slicing - Mili)

O fatiamento de programas decompõe um programa em partes relevantes para o valor de uma variável específica em um ponto de interesse.

### 5.1. Critério de Fatiamento
Um critério de fatia é formalmente definido por:
$$C = (s, V)$$
onde $s$ é uma instrução/linha do programa e $V$ é um subconjunto de variáveis observadas em $s$.

### 5.2. Modalidades de Fatiamento
- **Fatia Estática (Static Slice)**: Contém todas as instruções do programa que podem influenciar os valores de $V$ em $s$ para qualquer entrada possível (computada via grafos de dependência de controle e dados).
- **Fatia Dinâmica (Dynamic Slice)**: Contém apenas as instruções que efetivamente influenciaram os valores de $V$ em $s$ durante uma execução com entrada específica.
- **Aplicações em Teste**:
  - **Isolamento de Regressão**: Se uma modificação no código não pertence à fatia das variáveis de saída de um teste, o teste não sofrerá impacto (redução de suíte de regressão).
  - **Localização de Falhas**: A interseção de fatias de testes que falham com o complemento de fatias de testes que passam aponta com alta probabilidade a localização exata do defeito (Fault Localization).
