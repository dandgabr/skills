---
name: "tech-testing"
description: "Fornece diretrizes e boas práticas para testes de software robustos, cobrindo TDD, Pirâmide de Testes, Unitários, Integração e E2E, além de ferramentas como Vitest, Jest e Playwright."
---

# Habilidade de IA: Engenharia de Testes (Testing Specialist)

Esta skill orienta a inteligência artificial a agir como especialista em **Qualidade de Testes de Software**. O objetivo principal é guiar a IA e desenvolvedores a desenhar sistemas altamente testáveis, balanceando a pirâmide de testes de forma saudável, aplicando TDD (Test-Driven Development) e utilizando ferramentas modernas para garantir que nenhuma regressão atinja o ambiente de produção.

---

## 🧭 Diretrizes de Estratégia de Testes

Ao atuar nesta skill, paute suas validações técnicas e geração de testes nos seguintes princípios:

### 1. A Pirâmide de Testes
- **Distribuição Ideal**:
  - **Unitários (Base)**: Rápidos, isolados de efeitos colaterais (banco de dados, rede). Devem compor 70-80% do total de testes.
  - **Integração (Meio)**: Validam a comunicação entre múltiplos componentes (ex: regras de negócio interagindo com o ORM ou chamadas de API internas). Devem compor 15-20%.
  - **E2E / Ponta a Ponta (Topo)**: Validam o fluxo real do usuário sob o navegador real (simulando clique, escrita). Lentos e caros. Devem compor 5-10%.

```
       / \
      /   \      E2E (Playwright / Cypress)
     / E2E \
    /-------\
   / INTEGR. \   Integração (Vitest + DB Mock/Containers)
  /-----------\
 /  UNITÁRIOS  \  Unitários (Vitest / Jest)
/---------------\
```

### 2. TDD (Test-Driven Development)
- **Ciclo Red-Green-Refactor**:
  1. **Red**: Escreva um teste que falhe para uma nova funcionalidade antes do código existir.
  2. **Green**: Escreva o mínimo de código necessário para fazer o teste passar de forma simples.
  3. **Refactor**: Limpe o código, otimize a legibilidade e remova duplicações sob a proteção do teste que agora passa.

### 3. Técnicas de Isolamento (Mocks, Stubs e Spies)
- **Mocks**: Simulam objetos reais que recebem chamadas. Usados para verificar se funções colaterais foram executadas com parâmetros corretos (ex: garantir que a função `sendEmail()` foi invocada).
- **Stubs**: Fornecem respostas pré-programadas para chamadas externas para simular caminhos felizes ou de erro (ex: simular que a chamada de API retornou um erro `500` para ver se o código trata a exceção).
- **Spies**: Envelopam funções reais para rastrear quantas vezes e com quais argumentos foram chamadas, sem alterar a implementação padrão.

---

## 🛠️ Padrões de Código Recomendados (Vitest/Jest)

### Teste Unitário com Mocks de Serviço
```typescript
import { describe, it, expect, vi } from 'vitest';
import { PaymentService } from './payment.service';
import { PaymentGateway } from './payment-gateway';

describe('PaymentService', () => {
  it('deve processar o pagamento com sucesso se o gateway aprovar', async () => {
    // Criando um Stub do gateway externo
    const mockGateway: PaymentGateway = {
      charge: vi.fn().mockResolvedValue({ success: true, transactionId: 'txn_123' })
    };

    const service = new PaymentService(mockGateway);
    const result = await service.processOrder('order_001', 100);

    expect(result.success).toBe(true);
    expect(result.id).toBe('txn_123');
    // Verificando chamada (Mock check)
    expect(mockGateway.charge).toHaveBeenCalledWith(100);
  });
});
```

---

## 🔗 Integração com Outras Skills
- [qa-engineer](../../general/qa-engineer/SKILL.md): Utiliza os princípios de testes funcionais e E2E para projetar planos de teste abrangentes.
- [backend-developer](../../general/backend-developer/SKILL.md): Aplica testes de integração para validar a conexão e a robustez lógica de APIs e DBs.
- [frontend-developer](../../general/frontend-developer/SKILL.md): Constrói testes unitários de componentes UI e testes de renderização.
