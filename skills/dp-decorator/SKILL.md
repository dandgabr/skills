---
name: "dp-decorator"
description: "Padrão de Projeto Estrutural: Permite acoplar novos comportamentos a objetos ao colocá-los dentro de invólucros (wrappers) de objetos reais."
---

# Design Pattern: Decorator (Estrutural)

## 🎯 Intenção
Dinamicamente, anexar responsabilidades adicionais a um objeto. Os decorators fornecem uma alternativa flexível à herança para extensão de funcionalidade.

## ❓ Problema
Herança é estática e não permite alterar o comportamento de um objeto em tempo de execução. Além disso, estender classes com herança para todas as combinações de comportamentos leva a uma explosão de subclasses.

## 💡 Solução
Composição e Wrappers (Decorators). O Decorator implementa a mesma interface do objeto envolvido e delega as chamadas originais para ele, adicionando seu próprio comportamento antes ou depois da delegação.

## 🏗️ Estrutura do Padrão
- Componente (Component): Declara a interface comum tanto para os wrappers quanto para os objetos envolvidos.
- Componente Concreto (Concrete Component): A classe de objetos sendo envolvida que define o comportamento básico.
- Decorador Base (Base Decorator): Mantém uma referência ao objeto envolvido e delega todo o trabalho a ele.
- Decoradores Concretos (Concrete Decorators): Sobrescrevem métodos do Decorador Base para adicionar comportamentos adicionais dinamicamente.

## ⚖️ Prós e Contras

### ✅ Prós:
- Estende o comportamento de um objeto sem criar uma nova subclasse.
- Adiciona ou remove responsabilidades de um objeto em tempo de execução.
- Combina múltiplos comportamentos ao envolver um objeto em vários decoradores.

### ❌ Contras:
- É difícil remover um wrapper específico do meio da pilha de decorators.
- Dificuldade de depurar objetos com comportamento dependente da ordem dos invólucros.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Certifique-se de que seu método de negócio principal e os decorators compartilham a mesma interface.
2. Crie uma classe base Decorator com um campo de referência para o Componente original.
3. Redirecione todas as operações do Decorator base para o objeto referenciado.
4. Crie decoradores concretos herdando do Decorator base e adicione comportamento customizado nas operações.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
