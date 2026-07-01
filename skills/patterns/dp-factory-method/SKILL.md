---
name: "dp-factory-method"
description: "Padrão de Projeto Criacional: Fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados."
---

# Design Pattern: Factory Method (Criacional)

## 🎯 Intenção
Definir uma interface para criar um objeto, mas deixar as subclasses decidirem qual classe instanciar. O Factory Method permite a uma classe adiar a instanciação para subclasses.

## ❓ Problema
Quando um sistema precisa ser independente de como seus produtos são criados, compostos e representados, e quando a classe criadora não pode antecipar a classe dos objetos que deve criar.

## 💡 Solução
Substituir chamadas diretas de construção de objetos (usando o operador new) por chamadas a um método fábrica especial. Os objetos ainda são criados via new, mas a partir do método fábrica.

## 🏗️ Estrutura do Padrão
- Produto (Product): Declara a interface comum a todos os objetos que o criador e suas subclasses podem produzir.
- Produto Concreto (Concrete Product): Implementações distintas da interface do produto.
- Criador (Creator): Declara o método fábrica que retorna novos objetos produto. Pode fornecer uma implementação padrão.
- Criadores Concretos (Concrete Creators): Sobrescrevem o método fábrica base para retornar uma instância de um Produto Concreto diferente.

## ⚖️ Prós e Contras

### ✅ Prós:
- Evita acoplamento firme entre o criador e os produtos concretos.
- Princípio de responsabilidade única: move o código de criação do produto para um único lugar.
- Princípio do aberto/fechado: introduz novos tipos de produtos sem quebrar o código cliente existente.

### ❌ Contras:
- O código pode se tornar mais complicado, pois exige a criação de novas subclasses para implementar o padrão.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Defina uma interface comum para todos os produtos (Product).
2. Crie um método abstrato ou padrão de fabricação na classe Creator (Creator).
3. Encontre todas as chamadas a construtores diretos e substitua-as por chamadas ao método fábrica.
4. Crie subclasses de Creator para cada tipo de produto concreto e sobrescreva o método fábrica correspondente.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
