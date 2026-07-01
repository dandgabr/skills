---
name: "dp-abstract-factory"
description: "Padrão de Projeto Criacional: Permite produzir famílias de objetos relacionados ou dependentes sem especificar suas classes concretas."
---

# Design Pattern: Abstract Factory (Criacional)

## 🎯 Intenção
Fornecer uma interface para criação de famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

## ❓ Problema
Quando seu código precisa funcionar com várias famílias de produtos relacionados, mas você não quer depender das classes concretas desses produtos — eles podem mudar no futuro ou o sistema precisa suportar novas famílias.

## 💡 Solução
Declarar explicitamente interfaces para cada produto individual que faz parte da família. Em seguida, criar uma interface de fábrica abstrata com métodos de criação para todos os produtos abstratos.

## 🏗️ Estrutura do Padrão
- Produtos Abstratos (Abstract Products): Interfaces para uma família de produtos distintos porém relacionados.
- Produtos Concretos (Concrete Products): Implementações dessas interfaces agrupadas por variantes.
- Fábrica Abstrata (Abstract Factory): Declara um conjunto de métodos para criação de cada um dos produtos abstratos.
- Fábricas Concretas (Concrete Factories): Implementam os métodos de criação da fábrica abstrata para produzir variantes específicas de produtos.

## ⚖️ Prós e Contras

### ✅ Prós:
- Garante a compatibilidade entre os produtos criados pela mesma fábrica.
- Evita acoplamento forte entre o cliente e os produtos concretos.
- Princípio da responsabilidade única e princípio do aberto/fechado.

### ❌ Contras:
- O código pode se tornar muito complexo devido à introdução de múltiplas novas interfaces e classes.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Mapeie uma matriz de tipos de produtos versus variantes desses produtos.
2. Declare interfaces abstratas para todos os tipos de produtos.
3. Declare a interface Abstract Factory com um conjunto de métodos de criação para todos os produtos abstratos.
4. Implemente uma classe concreta de fábrica para cada variante de produto.
5. Inicialize a fábrica correspondente na inicialização da aplicação e passe-a para as classes cliente.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
