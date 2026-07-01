---
name: "dp-bridge"
description: "Padrão de Projeto Estrutural: Divide uma classe grande ou um conjunto de classes intimamente ligadas em duas hierarquias separadas — abstração e implementação — que podem ser desenvolvidas independentemente."
---

# Design Pattern: Bridge (Estrutural)

## 🎯 Intenção
Desacoplar uma abstração de sua implementação, de modo que as duas possam variar independentemente.

## ❓ Problema
Explosão combinatória de subclasses (p. ex., se você tem classes de formas geométricas como Círculo e Quadrado, e quer variantes de cores como CírculoVermelho, QuadradoAzul, etc., o número de subclasses cresce exponencialmente).

## 💡 Solução
Substituir a herança por composição. Extrair a dimensão independente (ex: as cores) em sua própria hierarquia de classes (Implementação), e manter uma referência para ela na classe original (Abstração).

## 🏗️ Estrutura do Padrão
- Abstração (Abstraction): Fornece lógica de controle de alto nível. Depende de um objeto de implementação.
- Abstração Refinada (Refined Abstraction): Variantes da lógica de controle.
- Implementação (Implementation): Declara a interface comum para todas as implementações concretas.
- Implementações Concretas (Concrete Implementations): Contêm código específico de plataforma ou infraestrutura.

## ⚖️ Prós e Contras

### ✅ Prós:
- Cria plataformas e aplicativos independentes.
- Código cliente interage apenas com a abstração de alto nível, escondendo detalhes da plataforma.
- Princípio do aberto/fechado e Princípio da responsabilidade única.

### ❌ Contras:
- Pode tornar o código altamente estruturado e difícil de ler para desenvolvedores juniores.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Identifique as dimensões independentes nas suas classes (ex: GUI vs. APIs de Sistema Operacional).
2. Declare as operações que o cliente precisa na classe Abstração base.
3. Declare as operações de baixo nível na interface Implementador.
4. Para todas as variantes da abstração, crie classes Abstrações Refinadas.
5. Crie classes de Implementação Concreta e aponte a referência da Abstração para um desses implementadores.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
