---
name: "dp-flyweight"
description: "Padrão de Projeto Estrutural: Permite ajustar mais objetos na quantidade disponível de RAM ao compartilhar partes comuns de estado entre múltiplos objetos em vez de manter todos os dados em cada objeto."
---

# Design Pattern: Flyweight (Estrutural)

## 🎯 Intenção
Usar compartilhamento para suportar grandes quantidades de objetos de grão fino de maneira eficiente.

## ❓ Problema
A aplicação cria milhares ou milhões de instâncias semelhantes, esgotando a memória RAM por carregar dados repetitivos (ex: dados visuais de árvores em um jogo florestal).

## 💡 Solução
Dividir o estado do objeto em duas partes: Estado Intrínseco (dados constantes que podem ser compartilhados e armazenados no Flyweight) e Estado Extrínseco (dados variáveis que dependem do contexto de uso e são mantidos fora do Flyweight).

## 🏗️ Estrutura do Padrão
- Flyweight: Contém a parte do estado do objeto original que pode ser compartilhada por múltiplas instâncias (ex: textura e modelo 3D).
- Contexto (Context): Contém o estado extrínseco, único para todas as situações (ex: coordenadas X, Y da árvore individual) e uma referência ao Flyweight correspondente.
- Fábrica Flyweight (Flyweight Factory): Gerencia o cache de objetos Flyweight existentes para garantir que novos só sejam criados se não existirem no cache.

## ⚖️ Prós e Contras

### ✅ Prós:
- Economiza muita memória RAM se o programa tiver muitos objetos parecidos.

### ❌ Contras:
- Pode aumentar o uso de CPU para recalcular ou buscar o estado extrínseco.
- Torna o código consideravelmente complexo devido à separação de dados.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Divida os campos da classe que consome muita RAM em: estado intrínseco (imutável, compartilhável) e estado extrínseco (mutável, dependente de contexto).
2. Mantenha os campos intrínsecos em uma classe Flyweight separada e torne seus campos imutáveis.
3. Crie uma Fábrica Flyweight para gerenciar o pool de instâncias Flyweight.
4. Os clientes usam o Flyweight chamando seus métodos e passando o estado extrínseco como argumentos.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
