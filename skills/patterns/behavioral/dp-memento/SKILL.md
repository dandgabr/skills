---
name: "dp-memento"
description: "Padrão de Projeto Comportamental: Permite salvar e restaurar o estado anterior de um objeto sem revelar os detalhes de sua implementação."
---

# Design Pattern: Memento (Comportamental)

## 🎯 Intenção
Sem violar o encapsulamento, capturar e externar o estado interno de um objeto, de modo que o objeto possa ser restaurado para este estado mais tarde.

## ❓ Problema
Você quer salvar e restaurar backups do estado de um objeto (para comandos undo, histórico), mas os campos do objeto são privados e expô-los violaria gravemente o encapsulamento básico da POO.

## 💡 Solução
Delegar a criação do backup ao próprio objeto dono do estado (Originador). O Originador cria um objeto Memento contendo um instantâneo de seus campos. O Memento é imutável e seus dados são lidos apenas pelo próprio Originador.

## 🏗️ Estrutura do Padrão
- Originador (Originator): O objeto que tem o estado interno. Ele sabe como criar um Memento e como restaurar seu estado a partir dele.
- Memento: Um objeto de valor imutável que atua como instantâneo do estado do Originador.
- Cuidador (Caretaker): Gerencia a pilha de mementos (histórico) sem ler ou modificar o estado interno dos mementos.

## ⚖️ Prós e Contras

### ✅ Prós:
- Salva e restaura o estado de um objeto sem violar o encapsulamento.
- Simplifica o código do Originador delegando a guarda do histórico ao Cuidador.

### ❌ Contras:
- O consumo de memória RAM pode disparar se os clientes criarem mementos frequentemente e eles não forem descartados.
- O Cuidador deve gerenciar o ciclo de vida do histórico ativamente.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Defina a classe Memento contendo os atributos que precisam ser arquivados.
2. Adicione na classe Originator métodos para salvar o estado (retorna um Memento) e restaurar o estado (aceita um Memento).
3. Crie a classe Caretaker com um histórico de mementos coletados e controle para push/pop na pilha de undo/redo.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
