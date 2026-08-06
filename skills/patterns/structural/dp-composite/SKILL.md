---
name: "dp-composite"
description: "Padrão de Projeto Estrutural: Permite compor objetos em estruturas de árvore e trabalhar com essas estruturas como se fossem objetos individuais."
---

# Design Pattern: Composite (Estrutural)

## 🎯 Intenção
Compor objetos em estruturas de árvore para representar hierarquias partes-todo. O Composite permite aos clientes tratarem de maneira uniforme objetos individuais e composições de objetos.

## ❓ Problema
Se o seu aplicativo pode ser representado como uma árvore de objetos (ex: caixas contendo produtos, que podem conter caixas menores com produtos), calcular o total ou processar a árvore exige varrer loops aninhados complexos e checar classes concretas a todo momento.

## 💡 Solução
Fazer com que caixas (compostos) e produtos (folhas) compartilhem uma interface comum que declare um método para executar a operação. Para um produto concreto, o método calcula o preço direto; para a caixa, varre seus itens filhos acumulando os preços.

## 🏗️ Estrutura do Padrão
- Componente (Component): Declara a interface comum para elementos simples e complexos da árvore.
- Folha (Leaf): Elemento básico de uma árvore que não tem sub-elementos. Realiza o trabalho real.
- Container/Composite: Elemento que possui sub-elementos (folhas ou outros containers). Delega o trabalho real para seus filhos.

## ⚖️ Prós e Contras

### ✅ Prós:
- Permite trabalhar com estruturas de árvore complexas mais convenientemente: polimorfismo facilita o uso de recursão.
- Princípio do aberto/fechado: novos tipos de elementos de árvore podem ser adicionados sem quebrar o código existente.

### ❌ Contras:
- Pode ser difícil fornecer uma interface comum para classes cujos comportamentos diferem muito. Pode ser necessário enfraquecer o encapsulamento ou a tipagem.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Garanta que o modelo central da sua aplicação possa ser representado como uma estrutura de árvore.
2. Declare a interface Componente com as operações que façam sentido tanto para folhas quanto para containers.
3. Crie a classe Folha para representar elementos simples.
4. Crie a classe Composite para representar containers, incluindo um array de Componentes filhos e métodos para gerenciar filhos (add/remove).
5. Implemente os métodos da interface no Composite delegando as tarefas aos sub-elementos.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
