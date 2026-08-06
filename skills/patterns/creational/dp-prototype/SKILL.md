---
name: "dp-prototype"
description: "Padrão de Projeto Criacional: Permite copiar objetos existentes sem tornar seu código dependente de suas classes."
---

# Design Pattern: Prototype (Criacional)

## 🎯 Intenção
Especificar os tipos de objetos a serem criados usando uma instância-protótipo e criar novos objetos copiando este protótipo.

## ❓ Problema
Você precisa copiar um objeto, mas não pode depender das classes concretas dele (p. ex. quando o código lida com objetos através de interfaces) ou deseja evitar o custo de instanciar e inicializar do zero se um estado similar já existe.

## 💡 Solução
Delegar o processo de clonagem aos próprios objetos que estão sendo clonados. O padrão declara uma interface comum com um método de clonagem (clone) para todos os objetos que suportam clonagem.

## 🏗️ Estrutura do Padrão
- Protótipo (Prototype): Declara os métodos de clonagem. Normalmente, é apenas um método clone.
- Protótipo Concreto (Concrete Prototype): Implementa o método de cópia. Copia os dados do objeto original para o novo objeto, inclusive lidando com clonagem rasa (shallow copy) ou profunda (deep copy).
- Cliente (Client): Cria um novo objeto solicitando ao protótipo que se clone.

## ⚖️ Prós e Contras

### ✅ Prós:
- Você pode clonar objetos sem acoplamento com suas classes concretas.
- Evita código de inicialização repetitivo clonando protótipos pré-configurados.
- Gera objetos complexos de forma mais conveniente.

### ❌ Contras:
- Clonar objetos complexos que têm referências circulares pode ser muito difícil.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Crie a interface Prototype e declare o método clone nela.
2. Uma classe de protótipo concreta deve definir o construtor que aceita um objeto daquela mesma classe como argumento para copiar todos os campos privados.
3. O método clone geralmente executa um return new ConcretePrototype(*this) (ou equivalente da linguagem).
4. Opcionalmente, crie um registro centralizado de protótipos (Prototype Registry) para catalogar instâncias prontas para cópia.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
