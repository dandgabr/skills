---
name: "dp-visitor"
description: "Padrão de Projeto Comportamental: Permite separar algoritmos dos objetos nos quais eles operam."
---

# Design Pattern: Visitor (Comportamental)

## 🎯 Intenção
Representar uma operação a ser realizada sobre os elementos de uma estrutura de objetos. O Visitor permite definir uma nova operação sem mudar as classes dos elementos sobre os quais opera.

## ❓ Problema
Você precisa aplicar uma operação em toda uma estrutura complexa de objetos (ex: árvore de nós do compilador, grafo de nós XML) sem poluir o código das classes desses nós com lógicas não-relacionadas a eles, e novas operações são adicionadas constantemente.

## 💡 Solução
Colocar o novo comportamento em uma classe separada chamada Visitante (Visitor) em vez de integrá-lo diretamente nas classes de nós. O objeto que executa o método é passado como argumento para o método visit do visitante (técnica de Double Dispatch).

## 🏗️ Estrutura do Padrão
- Visitante (Visitor Interface): Declara um conjunto de métodos de visita correspondendo às classes de elementos concretos.
- Visitantes Concretos (Concrete Visitors): Implementam operações de negócio diferentes para serem executadas sobre a estrutura.
- Elemento (Element Interface): Declara o método accept para aceitar o visitante.
- Elementos Concretos (Concrete Elements): Implementam o método accept chamando o método visit correspondente no visitante passado.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio do aberto/fechado: introduz operações que funcionam com várias classes sem alterá-las.
- Princípio da responsabilidade única: move comportamentos não relacionados para a classe do visitante.
- Pode acumular estados úteis enquanto visita os vários nós da estrutura.

### ❌ Contras:
- Adicionar ou remover uma classe de elemento exige atualizar a interface do visitante e todas as suas implementações.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface Visitor com métodos visit correspondendo a cada elemento concreto.
2. Declare o método abstrato accept(visitor) na interface Element.
3. Implemente accept nas classes concretas para chamarem visitor.visit(this).
4. Crie classes de visitantes concretos implementando as operações que deseja realizar sobre os elementos.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
