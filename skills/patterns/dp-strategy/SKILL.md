---
name: "dp-strategy"
description: "Padrão de Projeto Comportamental: Define uma família de algoritmos, coloca cada um deles em uma classe separada, e faz seus objetos intercambiáveis."
---

# Design Pattern: Strategy (Comportamental)

## 🎯 Intenção
Definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. O Strategy permite que o algoritmo varie independentemente dos clientes que o utilizam.

## ❓ Problema
Você tem várias alternativas para executar uma determinada lógica de negócio (ex: diferentes métodos de ordenação, rotas de navegação, métodos de pagamento) e quer alternar entre elas em tempo de execução sem encher o código cliente de condicionais complexos.

## 💡 Solução
Extrair os algoritmos em classes separadas chamadas Estratégias (Strategies). A classe original (Contexto) mantém uma referência a uma interface Estratégia e delega a execução do algoritmo a ela.

## 🏗️ Estrutura do Padrão
- Contexto (Context): Mantém uma referência para uma das estratégias e se comunica via interface genérica da estratégia.
- Estratégia (Strategy Interface): Comum a todas as variantes dos algoritmos. Declara o método de execução.
- Estratégias Concretas (Concrete Strategies): Implementações variadas do algoritmo.

## ⚖️ Prós e Contras

### ✅ Prós:
- Substitui herança por composição, dando mais flexibilidade em tempo de execução.
- Isola os detalhes de implementação do algoritmo do código que o consome.
- Princípio do aberto/fechado: novas estratégias podem ser introduzidas sem mexer no contexto.

### ❌ Contras:
- Se você tiver apenas alguns algoritmos estáveis, a introdução de novas interfaces e classes apenas complica desnecessariamente o projeto.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface Strategy com a assinatura do método do algoritmo.
2. Crie classes concretas implementando as variações do algoritmo.
3. Na classe Context, armazene uma referência à interface Strategy e implemente um método setter para injetar a estratégia desejada.
4. Chame o método da estratégia no fluxo de execução do Contexto.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
