---
name: "dp-singleton"
description: "Padrão de Projeto Criacional: Garante que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância."
---

# Design Pattern: Singleton (Criacional)

## 🎯 Intenção
Garantir que uma classe tenha apenas uma instância e fornecer um ponto de acesso global para ela.

## ❓ Problema
Garantir que uma classe tenha apenas uma única instância (ex: conexões com banco de dados, sistema de logs, caches compartilhados) e fornecer um ponto de acesso global simples sem expor variáveis globais vulneráveis.

## 💡 Solução
Tornar o construtor padrão privado para impedir instanciações diretas. Criar um método estático de acesso que atua como construtor, instanciando o objeto de forma tardia (lazy initialization) se necessário, e armazenando a instância em um campo estático.

## 🏗️ Estrutura do Padrão
- Singleton: Declara o método estático (ex: getInstance) que retorna a mesma instância de sua própria classe. O construtor é privado.

## ⚖️ Prós e Contras

### ✅ Prós:
- Garantia absoluta de uma única instância ativa da classe.
- Ponto de acesso global flexível e controlado.
- Inicialização tardia (Lazy initialization): o objeto só é criado quando é solicitado pela primeira vez.

### ❌ Contras:
- Viola o Princípio de Responsabilidade Única (a classe gerencia seu ciclo de vida além de sua lógica de negócios).
- Pode mascarar um design ruim, introduzindo dependências globais difíceis de testar em testes unitários.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Adicione um campo estático privado na classe Singleton para armazenar a instância única.
2. Declare um método de criação estático público para obter a instância.
3. Implemente a inicialização tardia dentro do método estático (crie a instância se o campo for nulo).
4. Torne o construtor da classe privado.
5. Em ambientes multi-thread, implemente sincronização (p. ex., double-checked locking) para evitar condições de corrida na criação do Singleton.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
