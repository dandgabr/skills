---
name: "framework-jest"
description: "Atua como Especialista em testes automatizados com Jest no ecossistema JavaScript e TypeScript, cobrindo Mocks, Spies, Snapshots, testes assíncronos, fake timers e suporte ao Node.js e React."
---

# Habilidade de IA: Especialista em Testes com Jest (Jest Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Desenvolvimento especializado em Jest**. O objetivo é guiar a construção de suítes de testes unitários, de integração e de componentes no ecossistema JavaScript e TypeScript (Node.js, React, Vue, Express, NestJS), aplicando boas práticas de isolamento, geração de mocks e testes de snapshot.

---

## 🧭 Princípios e Arquitetura do Jest

Ao utilizar o Jest em aplicações JS/TS:
- **Zero Configuração Inicial**: O Jest oferece um ambiente completo fora da caixa (*battery-included*), incluindo asserções, runner, mocks e relatórios de cobertura.
- **Isolamento de Testes**: Cada arquivo de teste é executado em um ambiente de sandbox isolado para evitar contaminação de estado global.
- **Mocks Nativos e Poderosos**: Utilize `jest.fn()`, `jest.spyOn()` e `jest.mock()` para substituir dependências de módulos, chamadas de rede ou funções assíncronas.
- **Snapshot Testing**: Capture estados de renderização de UI ou estruturas de dados complexas para prevenir alterações regressivas não intencionais.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Testes Unitários e Matchers Nativos
- Utilize os matchers adequados (`toBe` para igualdade estrita primitiva; `toEqual` para comparação profunda de objetos e arrays).

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

  it('deve lançar um erro se a quantidade for negativa', () => {
    const invalidItems = [{ price: 100, quantity: -1 }];
    expect(() => calculateOrderTotal(invalidItems, 0, 0)).toThrow('Quantidade inválida');
  });
});
```

### 2. Mocks de Funções e Módulos (`jest.fn`, `jest.mock`, `jest.spyOn`)
- Isole chamadas de rede ou bancos de dados substituindo módulos por implementações simuladas.

```typescript
import { UserService } from './user.service';
import { UserRepository } from './user.repository';

// Mock do módulo de repositório
jest.mock('./user.repository');

describe('UserService', () => {
  let userService: UserService;
  let mockRepo: jest.Mocked<UserRepository>;

  beforeEach(() => {
    jest.clearAllMocks(); // Limpa histórico de chamadas entre testes
    mockRepo = new UserRepository() as jest.Mocked<UserRepository>;
    userService = new UserService(mockRepo);
  });

  it('deve buscar e retornar o perfil de um usuário existente', async () => {
    const fakeUser = { id: 'usr_123', name: 'Alice', email: 'alice@jest.io' };
    mockRepo.findById.mockResolvedValue(fakeUser);

    const user = await userService.getUserProfile('usr_123');

    expect(user).toEqual(fakeUser);
    expect(mockRepo.findById).toHaveBeenCalledWith('usr_123');
    expect(mockRepo.findById).toHaveBeenCalledTimes(1);
  });
});
```

### 3. Manipulation de Tempo com Fake Timers (`jest.useFakeTimers`)
- Simule o avanço do tempo sem aguardar delays reais em chamadas com `setTimeout` ou `setInterval`.

```typescript
function debounce(fn: Function, delay: number) {
  let timer: NodeJS.Timeout;
  return (...args: any[]) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}

describe('debounce utility', () => {
  beforeEach(() => {
    jest.useFakeTimers();
  });

  afterEach(() => {
    jest.useRealTimers();
  });

  it('deve disparar a função apenas após o tempo estipulado', () => {
    const callback = jest.fn();
    const debouncedFn = debounce(callback, 1000);

    debouncedFn();
    expect(callback).not.toHaveBeenCalled();

    // Avança o tempo simulado no Jest
    jest.advanceTimersByTime(1000);

    expect(callback).toHaveBeenCalledTimes(1);
  });
});
```

---

## ⚙️ Configuração Recomendada (`jest.config.ts`)

```typescript
import type { Config } from 'jest';

const config: Config = {
  preset: 'ts-jest',
  testEnvironment: 'node', // Use 'jsdom' para aplicações React/Frontend
  roots: ['<rootDir>/src', '<rootDir>/tests'],
  testMatch: ['**/*.spec.ts', '**/*.test.ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/main.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};

export default config;
```

---

## 🔗 Integração com Outras Skills

- [lang-typescript](../../languages/lang-typescript/SKILL.md): Garante tipagem estrita e conformidade TS em testes.
- [frontend-developer](../../roles/frontend-developer/SKILL.md): Orienta a criação de testes de componentes UI em React/Vue.
- [backend-developer](../../roles/backend-developer/SKILL.md): Guia a criação de testes unitários e de integração de serviços backend em Node.js.
- [framework-testing](../framework-testing/SKILL.md): Apresenta a pirâmide de testes e padrões TDD.
