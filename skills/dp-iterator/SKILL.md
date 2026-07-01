---
name: "dp-iterator"
description: "Padrão de Projeto Comportamental: Permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore, etc.)."
---

# Design Pattern: Iterator (Comportamental)

## 🎯 Intenção
Fornecer uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente.

## ❓ Problema
Diferentes estruturas de dados (listas ligadas, árvores, pilhas) exigem algoritmos de travessia totalmente diferentes. Misturar esses algoritmos de busca dentro da lógica de negócio polui as classes e expõe suas estruturas internas.

## 💡 Solução
Extrair o algoritmo de travessia de uma coleção para um objeto independente chamado iterador. O iterador encapsula o estado de iteração atual (como índice e ponteiros) e fornece métodos simples como next e hasMore.

## 🏗️ Estrutura do Padrão
- Iterador (Iterator): Declara as operações necessárias para percorrer uma coleção.
- Iteradores Concretos (Concrete Iterators): Implementam algoritmos específicos para percorrer uma coleção específica.
- Coleção (Iterable/Collection): Declara um método para obter iteradores compatíveis com a coleção.
- Coleções Concretas (Concrete Collections): Retornam novas instâncias de um iterador concreto associado à sua estrutura interna.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio da responsabilidade única: limpa as coleções movendo algoritmos de busca complexos para classes separadas.
- Permite percorrer a mesma coleção em paralelo usando múltiplos iteradores independentes.
- Permite adiar uma iteração e continuá-la depois.

### ❌ Contras:
- Aplicar o padrão pode ser exagero se o aplicativo funcionar apenas com listas simples.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface do iterador com métodos como next, current, e hasNext.
2. Declare a interface da coleção com o método para gerar um iterador.
3. Crie os iteradores concretos implementando a interface do iterador para varrer a coleção específica.
4. Faça a coleção implementar o método gerador retornando uma instância do iterador correto passando self/this.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
