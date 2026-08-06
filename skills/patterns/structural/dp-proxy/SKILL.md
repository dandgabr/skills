---
name: "dp-proxy"
description: "Padrão de Projeto Estrutural: Fornece um substituto ou um espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo fazer algo antes ou depois que a requisição chegue a ele."
---

# Design Pattern: Proxy (Estrutural)

## 🎯 Intenção
Fornecer um substituto ou marcador de localização para outro objeto para controlar o acesso a esse objeto.

## ❓ Problema
Você tem um objeto pesado que consome muitos recursos (ex: banco de dados, leitor de arquivos grandes) e quer controlar seu acesso, fazer carregamento sob demanda (lazy loading), registrar logs de acesso (logging), ou caching, sem alterar a classe do objeto original.

## 💡 Solução
Criar uma classe Proxy com a mesma interface do objeto original. O Proxy intercepta todas as chamadas do cliente, realiza a operação secundária (verificação, log, cache) e, se apropriado, delega o trabalho real ao objeto de serviço real.

## 🏗️ Estrutura do Padrão
- Interface do Serviço (Service Interface): Declara a interface comum ao Serviço Real e ao Proxy.
- Serviço Real (Real Service): Classe de serviço que contém a lógica de negócio real.
- Proxy: Contém uma referência ao objeto de serviço. Gerencia o ciclo de vida do serviço real e delega chamadas a ele.

## ⚖️ Prós e Contras

### ✅ Prós:
- Permite controlar o objeto de serviço sem que o cliente saiba disso.
- Gerencia o ciclo de vida do objeto de serviço quando o cliente não se importa com isso.
- O Proxy funciona mesmo se o serviço real não estiver pronto ou disponível.

### ❌ Contras:
- O código pode se tornar mais complicado devido à introdução de novas classes.
- A resposta do serviço pode sofrer pequenos atrasos pela passagem pelo proxy.

## 🛠️ Diretrizes de Implementação para IA

Ao ser solicitada a implementar este padrão de projeto:

1. Crie uma interface comum para o serviço real e o proxy (caso não exista).
2. Crie a classe Proxy e armazene uma referência ao objeto de serviço nela.
3. Implemente os métodos da interface no Proxy e intercale a lógica de controle necessária antes/depois de delegar para o serviço real.

---
> **Referência:** Conteúdo consolidado com base nas especificações do [Refactoring.Guru](https://refactoring.guru/design-patterns) e boas práticas de arquitetura de software.
