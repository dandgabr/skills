---
name: "framework-mocha"
description: "Atua como Especialista em testes automatizados com Mocha em JavaScript e Node.js, cobrindo interfaces BDD/TDD, integração com Chai (expect/assert) e Sinon.js (Spies, Stubs, Mocks) e testes assíncronos."
---

# Habilidade de IA: Especialista em Testes com Mocha (Mocha Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Automação de Testes especializado em Mocha**. O objetivo é orientar o desenvolvimento de suítes de testes flexíveis no ecossistema Node.js e navegador, integrando o Mocha com bibliotecas de asserção consolidadas (Chai) e ferramentas de dublês de teste (Sinon.js).

---

## 🧭 Princípios e Arquitetura do Mocha

Ao utilizar o Mocha em projetos JS/Node.js:
- **Flexibilidade Desacoplada**: O Mocha é estritamente um *test runner*. Ele permite escolher a biblioteca de asserções (Chai, Assert nativo) e a biblioteca de Mocks (Sinon.js) ideal para o projeto.
- **Interfaces de Teste Modulares**:
  - **BDD (Behavior-Driven Development)** (Padrão): `describe()`, `context()`, `it()`, `before()`, `after()`, `beforeEach()`, `afterEach()`.
  - **TDD (Test-Driven Development)**: `suite()`, `test()`, `setup()`, `teardown()`.
- **Suporte Flexível a Asincronismo**: Aceita retorno de Promises (`async/await`) ou o callback tradicional `done()`.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Teste BDD com Mocha + Chai (`expect` style)
- Combine o ciclo BDD do Mocha com o estilo fluente de asserções da biblioteca Chai.

```javascript
const { expect } = require('chai');
const { ShoppingCart } = require('../src/cart');

describe('ShoppingCart (BDD)', () => {
  let cart;

  beforeEach(() => {
    cart = new ShoppingCart();
  });

  context('quando o carrinho está vazio', () => {
    it('deve retornar total zerado e contagem de itens em zero', () => {
      expect(cart.getTotal()).to.equal(0);
      expect(cart.getItemsCount()).to.equal(0);
    });
  });

  context('quando itens são adicionados', () => {
    it('deve calcular o total acumulado dos produtos', () => {
      cart.addItem({ name: 'Livro de Node.js', price: 40.0 });
      cart.addItem({ name: 'Café Expresso', price: 10.0 });

      expect(cart.getTotal()).to.equal(50.0);
      expect(cart.getItemsCount()).to.equal(2);
    });
  });
});
```

### 2. Mocks, Stubs e Spies com Sinon.js (`sinon.createSandbox`)
- Utilize um sandbox do Sinon.js no `beforeEach`/`afterEach` para criar e restaurar automaticamente Stubs e Spies entre os testes.

```javascript
const { expect } = require('chai');
const sinon = require('sinon');
const { AuthService } = require('../src/auth-service');
const { EmailClient } = require('../src/email-client');

describe('AuthService com Sinon.js', () => {
  let sandbox;
  let authService;

  beforeEach(() => {
    sandbox = sinon.createSandbox();
    authService = new AuthService();
  });

  afterEach(() => {
    sandbox.restore(); // Limpa todos os stubs/spies criados
  });

  it('deve enviar e-mail de boas-vindas ao registrar um novo usuário', async () => {
    // Criando um Stub para o método de envio de e-mail do cliente
    const sendEmailStub = sandbox.stub(EmailClient, 'send').resolves({ sent: true });

    const result = await authService.registerUser('carol@domain.com', 'pass123');

    expect(result.success).to.be.true;
    expect(sendEmailStub.calledOnce).to.be.true;
    expect(sendEmailStub.firstCall.args[0]).to.deep.equal({
      to: 'carol@domain.com',
      subject: 'Bem-vindo ao Sistema'
    });
  });
});
```

### 3. Testes Assíncronos (Promises vs. Callback `done`)
- Prefira a sintaxe `async/await` nativa, reservando o callback `done` apenas para chamadas legadas baseadas em eventos/callbacks.

```javascript
const { expect } = require('chai');

describe('Testes Assíncronos no Mocha', () => {
  // Padrão 1: Async / Await (Recomendado)
  it('deve resolver a promise com sucesso', async () => {
    const data = await Promise.resolve('resposta_valida');
    expect(data).to.equal('resposta_valida');
  });

  // Padrão 2: Callback done (Legado/Eventos)
  it('deve disparar o evento de emissão com callback done', (done) => {
    setTimeout(() => {
      try {
        expect(10).to.equal(10);
        done(); // Sinaliza ao Mocha que o teste concluiu
      } catch (err) {
        done(err); // Sinaliza falha capturada no try/catch
      }
    }, 50);
  });
});
```

---

## ⚙️ Arquivo de Configuração (`.mocharc.json`)

```json
{
  "diff": true,
  "extension": ["js", "ts"],
  "package": "./package.json",
  "reporter": "spec",
  "slow": "75",
  "timeout": "2000",
  "ui": "bdd",
  "recursive": true,
  "spec": "tests/**/*.spec.js"
}
```

---

## 🔗 Integração com Outras Skills

- [lang-typescript](../../languages/lang-typescript/SKILL.md): Guia o uso do `ts-node/register` com Mocha.
- [backend-developer](../../roles/backend-developer/SKILL.md): Orienta a criação de suítes de testes de APIs REST em Node.js com Mocha e Supertest.
- [framework-testing](../framework-testing/SKILL.md): Apresenta a teoria de testes BDD, TDD e isolamento.
