---
name: "dp-observer"
description: "Padrão de Projeto Comportamental: Permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando."
---

# Design Pattern: Observer (Comportamental)

## 🎯 Intenção
Definir uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

## ❓ Problema
Quando um objeto muda seu estado, outros objetos precisam executar ações decorrentes dessa mudança, mas você quer evitar acoplamento direto ou pesquisas em loops infinitos (polling).

## 💡 Solução
Criar um mecanismo de assinatura. O objeto que possui o estado interessante (Sujeito/Publisher) mantém uma lista de referências de objetos interessados (Observadores/Subscribers) e chama seus métodos de notificação quando ocorrem mudanças.

## 🏗️ Estrutura do Padrão
- Publicador (Publisher/Subject): Mantém a lista de assinantes e fornece métodos para adicionar e remover assinantes. Dispara eventos.
- Assinante (Subscriber/Observer Interface): Declara a interface de notificação (normalmente contendo um método update).
- Assinantes Concretos (Concrete Subscribers): Implementam as ações em resposta às notificações do publicador.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio do aberto/fechado: você pode introduzir novos assinantes sem alterar o código do publicador.
- Estabelece relações dinâmicas em tempo de execução entre objetos.

### ❌ Contras:
- Os assinantes são notificados em ordem aleatória, e se não forem removidos (unsubscribe) podem gerar vazamento de memória (lapsed listener problem).

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Identifique o publicador (Publisher) que dispara os eventos de alteração de estado.
2. Declare a interface Observer com um método update.
3. Na classe Publisher, adicione uma lista/array de Observers e métodos de gerência (subscribe/unsubscribe).
4. Ao disparar uma mudança, percorra a lista de assinantes chamando update de cada um.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
