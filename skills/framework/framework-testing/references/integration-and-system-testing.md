# 🏗️ Guia de Teste de Integração, Sistemas e Orientação a Objetos

Este guia consolida as arquiteturas de integração e testes em nível de sistema baseadas na metodologia de **Paul C. Jorgensen** (*Software Testing: A Craftsman's Approach*) e nas diretrizes do ISTQB.

---

## 1. Estratégias de Integração Baseadas em Decomposição

A integração tradicional mapeia a hierarquia de decomposição funcional (árvore de módulos).

```
         [ Módulo Raiz ]
          /           \
     [ Módulo A ]   [ Módulo B ]
      /        \          \
  [ Mod A1 ]  [ Mod A2 ] [ Mod B1 ]
```

### 1.1. Comparativo de Abordagens de Integração

| Estratégia | Direção | Artefatos Necessários | Vantagens | Desvantagens |
| :--- | :--- | :--- | :--- | :--- |
| **Top-Down** | Raiz $\rightarrow$ Folhas | **Stubs** (substitutos de módulos filhos não implementados) | Demonstra fluxos de alto nível cedo; isola erros no topo. | Criação excessiva de stubs; lógica crítica nas folhas é testada tardiamente. |
| **Bottom-Up** | Folhas $\rightarrow$ Raiz | **Drivers** (harnesses que invocam os módulos filhos) | Valida subsistemas críticos e utilitários primeiro; sem stubs. | Raiz integrada apenas no final; interface com usuário postergada. |
| **Sanduíche (Híbrida)** | Ambos os sentidos convergindo no centro | Stubs e Drivers | Balanceia validação do topo e da base simultaneamente. | Complexidade na coordenação das frentes de desenvolvimento. |
| **Big Bang** | Todos os módulos juntos de uma só vez | Nenhum | Rápido para projetos minúsculos. | **Péssima isolabilidade**: Impossível localizar a causa raiz de falhas em tempo hábil. |

---

## 2. Integração Baseada em Grafo de Chamadas (Call Graph)

Supera as restrições da decomposição estática ao focar nas dependências reais de invocação de rotinas em tempo de execução.

### 2.1. Métodos de Integração por Grafo de Chamadas
- **Integração Pairwise (Par a Par)**: Para cada aresta $(A, B)$ no grafo de chamadas, testa-se a invocação direta do módulo $A$ chamando $B$. Elimina a necessidade de integrar a árvore completa de uma só vez.
- **Integração por Vizinhança (Neighborhood Integration)**: O subgrafo contendo um nó central $N$, todos os seus predecessores imediatos e sucessores imediatos é testado como um cluster isolado.

---

## 3. MM-Paths e Testes no Nível de Sistema (Jorgensen)

Um **MM-Path (Method-to-Method Path)** modela a execução intercalada de segmentos de código em módulos distintos disparados por uma cadeia de chamadas.

### 3.1. Definição Formal de MM-Path
Um MM-Path é uma sequência de caminhos de decisão (DD-Paths) que cruzam fronteiras de métodos/módulos através de invocações de funções e retornos.

```
Módulo A                   Módulo B                   Módulo C
┌──────────┐              ┌──────────┐              ┌──────────┐
│ DD-Path 1│──(chama B)──►│ DD-Path 1│──(chama C)──►│ DD-Path 1│
│          │              │          │              │          │
│ DD-Path 2│◄─(retorna)───│ DD-Path 2│◄─(retorna)───│ DD-Path 2│
└──────────┘              └──────────┘              └──────────┘
```

### 3.2. Testes Atômicos de Sistema (Atomic System Tests - AST)
- Mapeiam a resposta ponta a ponta do sistema disparada por um evento externo de entrada (porta, interface, fila) até a geração da saída observável correspondente.
- Um AST é composto pela concatenação de múltiplos MM-Paths coordenados.

---

## 4. Teste em Sistemas Orientados a Objetos (OO Testing)

A Orientação a Objetos introduz características que desafiam os testes tradicionais procedurais:

### 4.1. Desafios OO e Mitigações

1. **Encapsulamento**:
   - O estado interno do objeto não é diretamente observável sem métodos de inspeção (`getters` ou inspeção por reflexão).
   - *Mitigação*: Testar transições de estado através dos métodos públicos que compõem o contrato da classe.
2. **Herança**:
   - Métodos herdados sem alteração sintática podem falhar no contexto do novo estado da subclasse (problema do contexto sutil).
   - *Mitigação*: Reaplicar a suíte de testes da classe-mãe na subclasse (Regra de Achatamento / Flattening).
3. **Polimorfismo e Ligação Dinâmica (Dynamic Binding)**:
   - A chamada `shape.draw()` pode invocar dezenas de implementações distintas em runtime.
   - *Mitigação*: Testar o polimorfismo instanciando o chamador com cada subclasse concreta registrada (Matriz de Vinculação Dinâmica).

### 4.2. Níveis de Teste na Hierarquia OO
- **Intra-Método**: Teste estrutural tradicional aplicado a um único método isolado.
- **Inter-Método (Intra-Classe)**: Testa a interação entre os métodos de uma mesma classe conforme operam sobre o estado compartilhado (`self` / `this`).
- **Inter-Classe (Cluster Testing)**: Testa a colaboração de classes acopladas (padrões Mediator, Observer, Factory).
