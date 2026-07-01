---
name: "dp-mediator"
description: "Padrão de Projeto Comportamental: Reduz as dependências caóticas entre objetos. Restringe comunicações diretas entre objetos e os força a colaborar apenas através de um objeto mediador."
---

# Design Pattern: Mediator (Comportamental)

## 🎯 Intenção
Definir um objeto que encapsula como um conjunto de objetos interage. O Mediator promove o acoplamento fraco ao impedir que os objetos se refiram uns aos outros explicitamente, e permite variar sua interação independentemente.

## ❓ Problema
Conexões e comunicações excessivas entre dezenas de classes diferentes (como componentes de tela de um formulário complexo) tornam qualquer alteração em um componente propensa a quebrar os demais (código espaguete).

## 💡 Solução
Cessar comunicações diretas entre os componentes e criar uma classe central (Mediador). Todos os componentes reportam eventos para o Mediador, e este decide como redirecionar ou tratar a ação entre os outros componentes.

## 🏗️ Estrutura do Padrão
- Mediador (Mediator): Declara a interface de comunicação com os componentes (geralmente um método notify).
- Mediador Concreto (Concrete Mediator): Encapsula a relação entre vários componentes e coordena suas ações.
- Componentes (Colleagues): Classes que realizam lógica de negócio individual. Elas não se conhecem mutuamente e referenciam apenas o Mediador.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio da responsabilidade única: extrai redes de comunicação complexas para um único local centralizado.
- Princípio do aberto/fechado: introduz novos mediadores sem alterar os componentes individuais.
- Reduz o acoplamento entre os vários componentes do sistema.

### ❌ Contras:
- Com o tempo, o mediador pode evoluir para um Objeto Deus (God Object).

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Identifique um grupo de classes fortemente acopladas que se beneficiariam de maior independência.
2. Declare a interface Mediator com o método genérico de notificação.
3. Implemente a classe ConcreteMediator mantendo referências a todos os componentes envolvidos.
4. Modifique as classes de componentes para aceitar a referência do Mediador e disparar notificações para ele ao invés de chamarem outros componentes diretamente.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
