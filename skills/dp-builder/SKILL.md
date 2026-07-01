---
name: "dp-builder"
description: "Padrão de Projeto Criacional: Permite construir objetos complexos passo a passo. Permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção."
---

# Design Pattern: Builder (Criacional)

## 🎯 Intenção
Separar a construção de um objeto complexo da sua representação, de modo que o mesmo processo de construção possa criar diferentes representações.

## ❓ Problema
Classes com construtores gigantescos (telescópicos) contendo dezenas de parâmetros opcionais, ou processos de criação que envolvem várias etapas sequenciais complexas.

## 💡 Solução
Extrair o código de construção do objeto de sua própria classe e colocá-lo em objetos separados chamados builders. A construção ocorre passo a passo através de métodos encadeados.

## 🏗️ Estrutura do Padrão
- Builder Interface: Declara etapas de construção de objetos comuns a todos os tipos de construtores.
- Concrete Builders: Oferecem implementações diferentes das etapas de construção. Produzem produtos que não seguem necessariamente uma interface comum.
- Produto (Product): O objeto complexo resultante sendo construído.
- Diretor (Director): Define a ordem em que as etapas de construção devem ser chamadas, permitindo criar configurações específicas de produtos de forma reutilizável.

## ⚖️ Prós e Contras

### ✅ Prós:
- Permite construir objetos passo a passo, adiar etapas ou executá-las recursivamente.
- Reutilização de código de construção para diferentes representações.
- Princípio da responsabilidade única: isola a construção complexa da lógica de negócio do produto.

### ❌ Contras:
- A complexidade geral do código aumenta, pois o padrão exige a criação de múltiplas novas classes.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Defina claramente as etapas de construção comuns para criar todas as representações do produto.
2. Declare essas etapas na interface do construtor (Builder).
3. Crie classes de construtores concretos para cada representação e implemente suas etapas de construção.
4. Pense em criar uma classe Diretor (Director) para encapsular as configurações mais comuns do produto.
5. O cliente cria tanto o objeto builder quanto o diretor, passando o builder para o diretor para iniciar a construção.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
