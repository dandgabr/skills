---
name: "tech-python"
description: "Fornece padrões de engenharia de software em Python, cobrindo estilo de código, tipagem, estruturas de projeto, frameworks populares como Django, Flask e FastAPI, além de boas práticas para testes, packaging e operacao."
---

# Habilidade de IA: Engenharia de Python (Python Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista em **Python** com foco em código legível, manutenível, testável e compatível com o ecossistema moderno da linguagem. O objetivo é combinar fundamentos da linguagem com práticas pragmáticas para aplicações web, APIs, automações, bibliotecas e serviços.

---

## 🧭 Diretrizes de Desenvolvimento em Python

Ao atuar nesta skill, aplique rigorosamente os seguintes padrões:

### 1. Estilo e Legibilidade
- **PEP 8**: Preserve nomenclatura clara, indentação consistente, linhas razoavelmente curtas e organização previsível de imports.
- **PEP 20**: Prefira simplicidade, explicitamente legível e comportamento claro a truques de implementação.
- **PEP 257**: Documente módulos, classes, funções e métodos públicos com docstrings objetivas quando isso agregar contexto real.
- **Funções Pequenas**: Mantenha funções com responsabilidade única e extraia lógica repetida para helpers bem nomeados.

### 2. Tipagem e Robustez
- **Type Hints**: Use anotações de tipo de forma consistente em APIs públicas, contratos entre camadas e objetos centrais do domínio.
- **Protocolos e Tipos Estruturais**: Prefira `Protocol`, `TypedDict`, `dataclass` e `Enum` quando isso tornar o contrato mais explícito.
- **Validação em Tempo de Execução**: Não confie apenas em anotações; valide entradas externas com bibliotecas como **Pydantic**, **attrs**, **marshmallow** ou validadores do próprio framework usado.

### 3. Estrutura de Projeto
- **Pacotes e Camadas**: Organize o código por domínio ou responsabilidade, evitando módulos gigantes e acoplamento excessivo.
- **Configuração por Ambiente**: Centralize configuração em variáveis de ambiente e arquivos de configuração por ambiente, sem segredos no repositório.
- **Dependências Reprodutíveis**: Use `poetry`, `uv`, `pip-tools` ou `requirements.txt` travado quando a reprodutibilidade for importante.

### 4. Testabilidade
- **Pytest como Padrão**: Use `pytest` para testes unitários e de integração sempre que possível.
- **Fixtures e Parametrização**: Prefira fixtures bem nomeadas e testes parametrizados para cobrir variações sem duplicação.
- **Isolamento**: Mantenha testes rápidos, determinísticos e independentes de rede, sistema de arquivos ou relógio sempre que o cenário permitir.

---

## 🛠️ Frameworks e Ecossistema Python

### 1. Django
- Use **Django** quando o problema exigir um framework completo com ORM, admin, autenticação, formulários e convenções fortes.
- Estruture apps por responsabilidade e mantenha views finas, movendo regras de negócio para services, use cases ou domain modules.
- Use **Django REST Framework** quando for necessário construir APIs REST consistentes, com serializers, permissions e viewsets bem definidos.

### 2. Flask
- Use **Flask** quando for necessária uma aplicação mais enxuta, modular e com alto grau de composição manual.
- Organize rotas, blueprints, serviços e adapters para evitar crescimento caótico do código.
- Aplique validação explícita de entrada e tratamento centralizado de erros, já que o framework é deliberadamente mínimo.

### 3. FastAPI e APIs Modernas
- Use **FastAPI** quando o foco for APIs tipadas, documentação automática e validação forte de requisições/respostas.
- Combine `Pydantic`, `Depends`, routers e injeção de dependências para manter as camadas separadas.
- Prefira corrotinas assíncronas apenas quando houver ganho real em I/O ou concorrência.

### 4. Dados, Jobs e Automação
- Use **SQLAlchemy** ou o ORM do framework com cuidado para evitar consultas caras e abuso de abstrações.
- Use **Alembic** para migrações versionadas quando houver banco relacional.
- Use **Celery**, **RQ**, **Arq** ou fila equivalente para tarefas em background quando o processamento não precisar ser síncrono.
- Use bibliotecas maduras para scraping, integrações e automações, mas preserve retries, timeout e logs estruturados.

---

## 🧰 Padrões de Código Recomendados

### Estrutura de serviço em FastAPI
```python
from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class UserIn(BaseModel):
    name: str

class UserOut(BaseModel):
    id: int
    name: str

@router.post("/users", response_model=UserOut)
def create_user(payload: UserIn) -> UserOut:
    user_id = 1
    return UserOut(id=user_id, name=payload.name)
```

### Service layer em Django
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class CreateInvoiceCommand:
    customer_id: int
    amount: float

class InvoiceService:
    def create(self, command: CreateInvoiceCommand) -> int:
        # regras de negocio aqui
        return 123
```

### Teste com pytest
```python
import pytest

@pytest.mark.parametrize("value, expected", [(1, 2), (2, 3)])
def test_increment(value, expected):
    assert value + 1 == expected
```

---

## 🔗 Integração com Outras Skills
- [backend-developer](../../general/backend-developer/SKILL.md): use quando o projeto Python precisar de desenho de APIs, persistência e arquitetura de backend.
- [tech-testing](../tech-testing/SKILL.md): use para aprofundar a estratégia de testes, pirâmide de testes e ferramentas de automação.
- [devsecops-engineer](../../security/devsecops-engineer/SKILL.md): use quando o fluxo Python envolver packaging, containers, CI/CD, secrets ou hardening.
- [security-champions](../../security/security-champions/SKILL.md): use para triagem de riscos de segurança e delegação para skills especialistas quando necessário.
- [clean-code-reusability](../../general/clean-code-reusability/SKILL.md): orienta a detecção de redundâncias e aplicação de padrões de clean code e docstrings no desenvolvimento em Python.

---

## ⚙️ Regras de Decisão

- Prefira a solução mais idiomática da comunidade Python antes de inventar abstrações próprias.
- Não misture lógica de domínio com detalhes de framework sem necessidade clara.
- Quando houver dúvida entre escrever mais código ou reforçar contratos e testes, priorize contratos explícitos e cobertura de teste.
