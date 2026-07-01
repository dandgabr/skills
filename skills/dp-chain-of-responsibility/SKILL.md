---
name: "dp-chain-of-responsibility"
description: "Padrão de Projeto Comportamental: Permite passar requisições por uma corrente de manipuladores. Ao receber uma requisição, cada manipulador decide se processa a requisição ou a passa para o próximo manipulador."
---

# Design Pattern: Chain Of Responsibility (Comportamental)

## 🎯 Intenção
Evitar o acoplamento do remetente de uma solicitação ao seu receptor, dando a mais de um objeto a oportunidade de tratar a solicitação. Encadear os objetos receptores e passar a solicitação ao longo da cadeia até que um objeto a trate.

## ❓ Problema
Um sistema precisa processar diferentes tipos de requisições sequencialmente (ex: autenticação, autorização, sanitização de dados, caching), e a ordem ou os componentes envolvidos podem mudar em tempo de execução.

## 💡 Solução
Transformar os comportamentos em objetos independentes chamados manipuladores (handlers). Cada manipulador possui um campo para armazenar uma referência ao próximo na corrente. A requisição viaja pela corrente até ser tratada ou interrompida.

## 🏗️ Estrutura do Padrão
- Manipulador (Handler): Declara a interface comum a todos os manipuladores da cadeia (geralmente um método handle).
- Manipulador Base (Base Handler): Classe opcional para manter a referência ao próximo manipulador e gerenciar a cadeia.
- Manipuladores Concretos (Concrete Handlers): Contêm o código real para processar a requisição. Ao receber a requisição, decidem se a tratam e/ou se a enviam adiante.
- Cliente (Client): Monta a corrente de manipuladores e dispara a requisição inicial.

## ⚖️ Prós e Contras

### ✅ Prós:
- Você pode controlar a ordem de tratamento de requisições.
- Princípio da responsabilidade única: desacopla classes que chamam operações de classes que as executam.
- Princípio do aberto/fechado: introduz novos manipuladores no aplicativo sem quebrar o código existente.

### ❌ Contras:
- Algumas requisições podem chegar ao final da cadeia sem serem tratadas se nenhum manipulador a interceptar.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface do manipulador com um método de processamento.
2. Crie uma classe abstrata base para eliminar o código padrão de encadeamento.
3. Implemente os manipuladores concretos herdando da base e definindo as condições de tratamento.
4. O cliente encadeia os manipuladores usando setters apropriados e inicia o fluxo chamando o primeiro manipulador.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
