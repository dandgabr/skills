---
name: "dp-adapter"
description: "Padrão de Projeto Estrutural: Permite que objetos com interfaces incompatíveis colaborem entre si."
---

# Design Pattern: Adapter (Estrutural)

## 🎯 Intenção
Converter a interface de uma classe em outra interface esperada pelos clientes. O Adapter permite que classes com interfaces incompatíveis trabalhem juntas.

## ❓ Problema
Você quer utilizar uma classe existente, mas a interface dela não corresponde à interface que o seu código cliente espera.

## 💡 Solução
Criar um adaptador: um objeto intermediário que converte a interface de um objeto para que outro possa compreendê-la. O adaptador envolve (wraps) um dos objetos para traduzir as chamadas.

## 🏗️ Estrutura do Padrão
- Cliente (Client): Contém a lógica de negócio do programa e se comunica via Target interface.
- Interface do Cliente (Client Interface/Target): Descreve o protocolo que outras classes devem seguir para colaborar com o cliente.
- Adaptado (Adaptee): A classe de terceiros ou legado que possui a interface incompatível.
- Adaptador (Adapter): Uma classe que implementa a Interface do Cliente enquanto envolve o objeto Adaptado, traduzindo as requisições do Cliente em chamadas compreensíveis pelo Adaptado.

## ⚖️ Prós e Contras

### ✅ Prós:
- Princípio da responsabilidade única: separa a lógica de conversão de dados da lógica de negócio.
- Princípio do aberto/fechado: introduz novos adaptadores sem quebrar o código cliente existente.

### ❌ Contras:
- A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Certifique-se de ter pelo menos duas classes com interfaces incompatíveis (o serviço útil e o cliente).
2. Declare a interface do cliente que descreve como ele deseja interagir com os serviços.
3. Crie a classe Adapter e faça com que ela implemente a interface do cliente.
4. Adicione um campo de referência para o objeto do serviço adaptado (Adaptee) no Adapter (composição).
5. Implemente todos os métodos da interface do cliente no Adapter redirecionando as chamadas para o Adaptee.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
