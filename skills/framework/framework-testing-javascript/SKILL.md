---
name: framework-testing-javascript
description: "Atua como Especialista em Testes Automatizados e Engenharia de QA no ecossistema JavaScript e TypeScript (Node.js, React, Vue, NestJS). Cobre o framework integrado Jest e a arquitetura modular Mocha com Chai e Sinon.js, dominando Spies, Stubs, Mocks, asserções BDD/TDD, Snapshots, Fake Timers, testes assíncronos e cobertura de código com Istanbul/c8."
---

# Testes Automatizados em JavaScript & TypeScript: Jest & Mocha

Esta skill estabelece as diretrizes e padrões de engenharia para desenvolvimento e automação de testes no ecossistema JavaScript e TypeScript, abrangendo soluções completas (*battery-included*) como **Jest** e composições modulares com **Mocha + Chai + Sinon.js**.

---

## 🧭 1. Comparativo e Diretrizes de Seleção de Framework

| Característica | Jest | Mocha + Chai + Sinon.js |
| :--- | :--- | :--- |
| **Arquitetura** | Framework "tudo-em-um" (Runner + Assertions + Mocks) | Runner desacoplado com ecossistema de plugins |
| **Mocks & Spies** | Nativo (`jest.fn()`, `jest.spyOn()`, `jest.mock()`) | Via Sinon.js (`sinon.stub()`, `sinon.spy()`) |
| **Asserções** | Matchers ricos nativos (`expect(val).toBe()`) | Biblioteca Chai (`expect`, `should`, `assert`) |
| **Snapshot Testing** | Suporte nativo (`toMatchSnapshot()`) | Requer plugins adicionais |
| **Ambiente Típico** | React, Vue, NestJS, TypeScript, Next.js | Microserviços Node.js legados, Express, ESM puro |

---

## ⚡ 2. Jest: Padrões de Teste e Mocks Nativos

### 2.1 Testes Unitários e Matchers Nativos
```typescript
import { calculateOrderTotal } from './calculator';

describe('calculateOrderTotal', () => {
  it('deve calcular o total com desconto e frete corretamente', () => {
    const items = [{ price: 100, quantity: 2 }, { price: 50, quantity: 1 }];
    const discount = 20;
    const shipping = 15;

    const result = calculateOrderTotal(items, discount, shipping);
    expect(result).toBe(245); // (200 + 50) - 20 + 15
  });

  it('deve lançar erro para quantidade negativa', () => {
    const invalidItems = [{ price: 100, quantity: -1 }];
    expect(() => calculateOrderTotal(invalidItems, 0, 0)).toThrow('Quantidade inválida');
  });
});
```

### 2.2 Mocks de Módulos e Funções Assíncronas
```typescript
import { UserService } from './user.service';
import { UserRepository } from './user.repository';

jest.mock('./user.repository');

describe('UserService', () => {
  let userService: UserService;
  let mockRepo: jest.Mocked<UserRepository>;

  beforeEach(() => {
    jest.clearAllMocks();
    mockRepo = new UserRepository() as jest.Mocked<UserRepository>;
    userService = new UserService(mockRepo);
  });

  it('deve retornar usuário quando encontrado no repositório', async () => {
    mockRepo.findById.mockResolvedValue({ id: 'u1', name: 'Alice' });
    const user = await userService.getUser('u1');
    
    expect(mockRepo.findById).toHaveBeenCalledWith('u1');
    expect(user.name).toBe('Alice');
  });
});
```

---

## ☕ 3. Mocha + Chai + Sinon.js: Arquitetura Modular

### 3.1 Teste BDD com Chai e Sandbox Sinon.js
```javascript
const { expect } = require('chai');
const sinon = require('sinon');
const { PaymentService } = require('../src/payment.service');
const { PaymentGateway } = require('../src/payment.gateway');

describe('PaymentService (Mocha + Chai + Sinon)', () => {
  let sandbox;
  let paymentService;
  let gatewayMock;

  beforeEach(() => {
    sandbox = sinon.createSandbox();
    gatewayMock = new PaymentGateway();
    paymentService = new PaymentService(gatewayMock);
  });

  afterEach(() => {
    sandbox.restore(); // Restaura todos os stubs e spies
  });

  it('deve processar o pagamento e registrar transação', async () => {
    const stub = sandbox.stub(gatewayMock, 'charge').resolves({ status: 'SUCCESS', id: 'tx-999' });

    const result = await paymentService.processPayment({ amount: 100 });
    
    expect(stub.calledOnce).to.be.true;
    expect(result.status).to.equal('SUCCESS');
    expect(result.id).to.equal('tx-999');
  });
});
```

---

## 🧪 4. Fake Timers e Testes Assíncronos

### 4.1 Jest Fake Timers
```typescript
jest.useFakeTimers();

it('deve executar callback após debounce de 300ms', () => {
  const callback = jest.fn();
  const debounced = debounce(callback, 300);

  debounced();
  expect(callback).not.toHaveBeenCalled();

  jest.advanceTimersByTime(300);
  expect(callback).toHaveBeenCalledTimes(1);
});
```
