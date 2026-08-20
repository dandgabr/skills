# 🧬 Guia de Teste de Mutação, Semeadura de Defeitos e Testes Metamórficos

Este guia sintetiza a teoria avançada de avaliação de suítes de testes, confiabilidade de software e tratamento do problema do oráculo, fundamentado na obra de **Ali Mili & Fairouz Tchier** (*Software Testing: Concepts and Operations*) e nas metodologias modernas de engenharia de software.

---

## 1. Fundamentos do Teste de Mutação (Mutation Testing)

O teste de mutação avalia a eficácia real de uma suíte de testes injetando alterações sintáticas deliberadas (mutações) no código fonte para verificar se os testes existentes conseguem detectar (matar) essas anomalias.

### 1.1. Premissas Teóricas Fundamentais
1. **Hipótese do Programador Competente (Competent Programmer Hypothesis)**:
   Programadores desenvolvem programas próximos da correção. Defeitos reais são predominantemente pequenos desvios sintáticos e semânticos (erros de operadores, condições de contorno invertidas, variáveis trocadas).
2. **Efeito do Acoplamento (Coupling Effect)**:
   Casos de teste capazes de detectar pequenos defeitos atômicos simples (mutantes de 1ª ordem) são estatisticamente acoplados à capacidade de detectar falhas complexas e de ordens superiores compostas.

---

## 2. Operadores de Mutação e Taxonomia de Mutantes

Um operador de mutação é uma regra gramatical de transformação de código.

### 2.1. Principais Classes de Operadores de Mutação

| Operador | Nome | Descrição | Exemplo Original | Código Mutado |
| :--- | :--- | :--- | :--- | :--- |
| **AOR** | Arithmetic Operator Replacement | Substitui operadores aritméticos | `x = a + b;` | `x = a - b;` ou `x = a * b;` |
| **ROR** | Relational Operator Replacement | Substitui operadores relacionais | `if (x >= limit)` | `if (x > limit)` ou `if (x == limit)` |
| **COR** | Conditional Operator Replacement | Altera operadores booleanos | `if (a && b)` | `if (a || b)` |
| **LCR** | Logical Connector Replacement | Inverte valores booleanos / bits | `flag = !ready;` | `flag = ready;` |
| **SDL** | Statement Deletion | Deleta uma instrução executável | `calculate_discount();` | `/* removido */` |
| **UOI** | Unary Operator Insertion | Insere operadores unários | `return value;` | `return -value;` ou `return ++value;` |

### 2.2. Classificação de Mutantes
- **Mutante Morto (Killed Mutant)**: Um caso de teste da suíte $T$ falhou ao executar o mutante (comportamento divergiu do programa original).
- **Mutante Sobrevivente (Live/Surviving Mutant)**: Toda a suíte de testes passou com sucesso no mutante (indica lacuna ou fraqueza na asserção dos testes).
- **Mutante Equivalente (Equivalent Mutant)**: O mutante alterou a sintaxe, mas preserva exatamente a mesma semântica funcional do original (ex: `i++` vs `++i` em laço isolado). É indecidível determinar mutantes equivalentes automaticamente (problema da parada de Turing).

### 2.3. Cálculo do Escore de Mutação (Mutation Score)
O Escore de Mutação $MS(T, P)$ mede a suficiência dos testes:

$$MS(T, P) = \frac{K}{M - E} \times 100\%$$

Onde:
- $K$ = Quantidade de mutantes mortos.
- $M$ = Quantidade total de mutantes gerados.
- $E$ = Quantidade de mutantes equivalentes identificados.

---

## 3. Semeadura de Defeitos (Fault Seeding) e Modelo de Mills

A semeadura de falhas introduz deliberadamente um número conhecido de defeitos artificiais no software para estimar a quantidade total de defeitos reais ainda ocultos.

### 3.1. Abordagem de Captura-Recaptura (Modelo de Mills)
Seja:
- $S$: Número de defeitos artificiais semeados no código.
- $s$: Número de defeitos semeados que foram descobertos durante a execução dos testes.
- $n$: Número de defeitos reais (naturais) encontrados pelos mesmos testes.
- $N$: Número total estimado de defeitos reais existentes no código.

Assumindo que os testes têm a mesma probabilidade de encontrar defeitos reais e semeados:
$$\frac{s}{S} \approx \frac{n}{N} \implies \hat{N} = \frac{n \times S}{s}$$

### 3.2. Estimativa de Defeitos Residuais
A quantidade estimada de defeitos reais ainda não descobertos ($N_{residual}$) é:
$$N_{residual} = \hat{N} - n = n \left( \frac{S}{s} - 1 \right)$$

---

## 4. Testes Metamórficos e o Problema do Oráculo (The Oracle Problem)

O **Problema do Oráculo** surge quando é computacionalmente proibitivo ou teoricamente impossível conhecer de antemão o resultado exato esperado de uma entrada (ex: algoritmos estocásticos, renderização gráfica, processamento de linguagem natural, aprendizado de máquina).

### 4.1. Relações Metamórficas (Metamorphic Relations - MR)
O teste metamórfico contorna o oráculo ao verificar **propriedades relacionais necessárias** entre múltiplas execuções do programa com entradas relacionadas.

Se $f(x)$ calcula uma função sob entrada $x$, derivamos uma entrada transformada $x'$ de modo que uma relação matemática entre $f(x)$ e $f(x')$ deva obrigatoriamente se manter.

#### Exemplos de Relações Metamórficas em Domínios Reais:

1. **Algoritmo de Busca de Menor Caminho ($ShortestPath(G, A, B)$)**:
   - *Entrada base*: Grafo $G$, nós $A$ e $B$. Distância calculada $= d$.
   - *Entrada metamórfica*: Grafo $G$ onde todas as arestas são multiplicadas pelo fator constante $k > 0$.
   - *Relação*: $ShortestPath(k \cdot G, A, B) = k \cdot d$.
2. **Motor de Busca / Recuperação de Informação**:
   - *Entrada base*: Query $Q_1 = \text{"Software Testing"}$. Retorna conjunto de documentos $D_1$.
   - *Entrada metamórfica*: Query $Q_2 = \text{"Software Testing AND Books"}$. Retorna $D_2$.
   - *Relação*: $D_2 \subseteq D_1$.
3. **Funções Criptográficas / Hashes**:
   - *Entrada base*: Mensagem $M_1$.
   - *Entrada metamórfica*: Mensagem $M_2 = M_1 \text{ com 1 bit alterado}$.
   - *Relação (Efeito Avalanche)*: $\text{HammingDistance}(Hash(M_1), Hash(M_2)) \approx \frac{\text{Tamanho do Hash}}{2}$.
