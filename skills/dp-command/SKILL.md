---
name: "dp-command"
description: "Padrão de Projeto Comportamental: Transforma uma solicitação em um objeto independente que contém toda a informação sobre a solicitação, permitindo parametrizar, enfileirar ou desfazer operações."
---

# Design Pattern: Command (Comportamental)

## 🎯 Intenção
Encapsular uma solicitação como um objeto, desta forma permitindo parametrizar clientes com diferentes solicitações, enfileirar ou registrar solicitações e suportar operações que podem ser desfeitas.

## ❓ Problema
Vincular comandos de interface de usuário (como botões e atalhos de teclado) diretamente a classes de negócio acopla fortemente os componentes visuais com as regras de negócio, além de dificultar o suporte a operações de desfazer/refazer (undo/redo).

## 💡 Solução
Extrair detalhes da solicitação em classes separadas que implementam uma interface comum com um método execute. O acionador (invoker) chama execute sem saber qual comando está sendo executado.

## 🏗️ Estrutura do Padrão
- Comando (Command): Declara a interface comum com o método execute.
- Comandos Concretos (Concrete Commands): Implementam o método execute e delegam chamadas para um ou mais objetos receptores.
- Remetente/Invocador (Invoker/Sender): Classe responsável por iniciar a solicitação (ex: botão). Mantém uma referência ao Comando.
- Receptor (Receiver): A classe que contém a lógica de negócio real a ser executada pelo comando.
- Cliente (Client): Cria e configura objetos comandos concretos e os associa aos invocadores.

## ⚖️ Prós e Contras

### ✅ Prós:
- Desacopla a classe que invoca a operação da classe que realiza a operação.
- Permite implementar operações reversíveis (desfazer/refazer) salvando o histórico de comandos executados.
- Permite enfileirar ou agendar a execução de comandos.
- Permite criar comandos compostos (padrão macro).

### ❌ Contras:
- O código pode ficar mais complexo, pois introduz uma camada completamente nova de comandos.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Declare a interface do comando com o método execute (e opcionalmente undo).
2. Crie classes de comandos concretos, injetando o objeto receptor adequado no construtor.
3. Implemente execute nos comandos concretos mapeando para chamadas de métodos no receptor.
4. Configure os remetentes (invokers) para aceitar e disparar os comandos.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
