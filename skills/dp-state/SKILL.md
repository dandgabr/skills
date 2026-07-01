---
name: "dp-state"
description: "Padrão de Projeto Comportamental: Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe."
---

# Design Pattern: State (Comportamental)

## 🎯 Intenção
Permitir a um objeto alterar seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe.

## ❓ Problema
Uma classe possui condicionais gigantescos (switch-case ou if-else aninhados) que alteram completamente as operações da classe com base nos valores de seus atributos de estado atuais.

## 💡 Solução
Extrair as lógicas de comportamento associadas a cada estado em classes separadas de Estado Concreto. O objeto de contexto principal armazena uma referência para o objeto de estado atual e delega a ele toda a lógica.

## 🏗️ Estrutura do Padrão
- Contexto (Context): Mantém uma referência a um dos objetos de estado concreto e delega o trabalho.
- Estado (State Interface): Declara os métodos que todos os estados concretos devem implementar.
- Estados Concretos (Concrete States): Implementam comportamentos específicos associados a um estado do Contexto. Podem transicionar o contexto para outro estado.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio da responsabilidade única: organiza o código relacionado a estados particulares em classes separadas.
- Princípio do aberto/fechado: introduz novos estados sem alterar as classes de estado existentes ou o contexto.
- Elimina condicionais de estado monolíticos e difíceis de testar.

### ❌ Contras:
- Pode ser um exagero se a máquina de estados tiver poucas transições ou condições simples.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface State contendo métodos correspondentes a todas as ações iniciadas pelo contexto.
2. Crie classes de estados concretos para cada estado possível da aplicação.
3. Faça o Contexto expor um método setter público para alterar seu estado em tempo de execução.
4. Delegue os métodos de comportamento do Contexto para o objeto State atual.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
