---
name: "dp-template-method"
description: "Padrão de Projeto Comportamental: Define o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura."
---

# Design Pattern: Template Method (Comportamental)

## 🎯 Intenção
Definir o esqueleto de um algoritmo em uma operação, adiando a definição de alguns passos para subclasses. O Template Method permite que as subclasses redefinam certas etapas de um algoritmo sem mudar a sua estrutura.

## ❓ Problema
Várias classes executam algoritmos que seguem passos muito semelhantes, com pequenas diferenças em etapas específicas (ex: leitores de relatórios PDF, CSV e JSON que abrem, leem e fecham arquivos da mesma forma, diferindo apenas na análise do conteúdo).

## 💡 Solução
Criar uma classe base abstrata e declarar o método modelo (Template Method) que define a sequência de chamadas de etapas. Algumas etapas podem ser implementadas diretamente na base (etapas padrão) e outras declaradas como abstratas (ganchos/hooks) para serem implementadas pelas subclasses.

## 🏗️ Estrutura do Padrão
- Classe Abstrata (Abstract Class): Declara o método modelo e as etapas abstratas/concretas do algoritmo.
- Classe Concreta (Concrete Class): Sobrescreve as etapas abstratas para personalizar o comportamento sem mexer na estrutura do algoritmo principal.

## ⚖️ Prós e Contras

### ✅ Prós:
- Evita duplicação de código ao puxar as etapas repetitivas para a superclasse.
- Permite controle rigoroso sobre a estrutura e extensão permitida do algoritmo por meio de ganchos (hooks).

### ❌ Contras:
- Alguns clientes podem se sentir limitados pelo esqueleto rígido do algoritmo fornecido pela superclasse.
- Pode violar o Princípio de Substituição de Liskov se as subclasses mudarem as premissas de execução das etapas herdadas.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Analise o algoritmo alvo para ver se você pode dividi-lo em etapas sequenciais.
2. Declare a classe base abstrata e crie o método modelo contendo o fluxo das etapas.
3. Declare as etapas que diferem entre as variações como métodos abstratos (devem ser implementadas) ou métodos virtuais com comportamento básico (hooks).
4. Crie subclasses concretas e implemente os métodos de etapas correspondentes.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
