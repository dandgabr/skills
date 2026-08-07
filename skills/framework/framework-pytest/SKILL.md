---
name: "framework-pytest"
description: "Atua como Especialista em testes automatizados com Pytest em Python, cobrindo fixtures, parametrização, mocks, plugins (pytest-cov, pytest-asyncio, pytest-xdist), conftest.py e estratégias de TDD."
---

# Habilidade de IA: Especialista em Testes com Pytest (Pytest Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Automação de Testes especializado em Pytest**. O objetivo é guiar a criação de suítes de testes limpas, expressivas e performáticas para aplicações Python, cobrindo desde testes unitários a testes de integração com banco de dados e APIs assíncronas.

---

## 🧭 Princípios e Arquitetura do Pytest

Ao escrever testes com Pytest, siga os princípios fundamentais do framework:
- **Assertions Simples e Nativas**: Utilize o `assert` nativo do Python. O Pytest reescreve a AST para fornecer diffs detalhados automaticamente sem a necessidade de métodos de asserção verbosos.
- **Injeção de Dependências por Fixtures**: Substitua estruturas rígidas de `setUp`/`tearDown` por fixtures reutilizáveis via injeção de parâmetros nas funções de teste.
- **Descobrimento Automático**: Mantenha arquivos nomeados como `test_*.py` ou `*_test.py` e funções de teste prefixadas com `test_*`.
- **Modularização via `conftest.py`**: Compartilhe fixtures, hooks e configurações entre múltiplos diretórios sem necessidade de imports explícitos.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Fixtures e Gestão de Recursos (`@pytest.fixture`)
- **Escopos**: Utilize o escopo adequado (`function`, `class`, `module`, `package`, `session`) para evitar recriação desnecessária de recursos caros (como conexões de banco de dados ou contêineres).
- **Teardown com `yield`**: Forneça o recurso após o `yield` e execute o código de limpeza logo em seguida.

```python
import pytest
from my_app.db import DatabaseConnection

@pytest.fixture(scope="session")
def db_engine():
    """Fixture de sessão para inicializar o banco de dados em memória."""
    engine = DatabaseConnection.create_in_memory()
    engine.setup_tables()
    yield engine
    engine.dispose()

@pytest.fixture
def db_session(db_engine):
    """Fixture por função de teste com rollback automático para isolamento total."""
    connection = db_engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()
```

### 2. Parametrização de Testes (`@pytest.mark.parametrize`)
- Reduza duplicação de código testando múltiplos cenários de entrada e saída com uma única função de teste.

```python
import pytest
from my_app.validators import validate_email

@pytest.mark.parametrize("email, expected", [
    ("user@domain.com", True),
    ("admin.sub@domain.co.uk", True),
    ("invalid-email", False),
    ("@domain.com", False),
    ("user@.com", False),
])
def test_email_validation_cases(email: str, expected: bool):
    assert validate_email(email) is expected
```

### 3. Mocks e Substituição de Dependências (`pytest-mock` / `mocker`)
- Prefira a fixture `mocker` fornecida pelo `pytest-mock` em vez do decorador nativo `@patch`, garantindo limpeza automática do mock ao final do teste.

```python
import pytest
from my_app.services import PaymentProcessor

def test_process_payment_success(mocker):
    # Mock do serviço de gateway externo de pagamento
    mock_gateway = mocker.patch("my_app.services.ExternalPaymentGateway.charge")
    mock_gateway.return_value = {"status": "SUCCESS", "transaction_id": "tx_999"}

    processor = PaymentProcessor()
    result = processor.execute_order(order_id="123", amount=150.00)

    assert result["success"] is True
    assert result["tx_id"] == "tx_999"
    mock_gateway.assert_called_once_with(amount=150.00)
```

### 4. Testes Assíncronos (`pytest-asyncio`)
- Marque testes `async def` com o decorador `@pytest.mark.asyncio` para testar funções corrotinas nativas.

```python
import pytest
import httpx

@pytest.mark.asyncio
async def test_async_fetch_user():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        assert response.status_code == 200
```

---

## ⚙️ Configuração Recomendada (`pytest.ini` / `pyproject.toml`)

```toml
[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --cov=src --cov-report=term-missing"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
markers = [
    "slow: marca testes lentos que requerem rede ou DB",
    "integration: testes de integração de sistema",
]
```

---

## 🔗 Integração com Outras Skills

- [qa-engineer](../../general/roles/qa-engineer/SKILL.md): Guia o planejamento de casos de teste e matrizes de cobertura.
- [lang-python](../../languages/lang-python/SKILL.md): Garante conformidade com PEP 8, tipagem e estilo de código Python.
- [framework-testing](../framework-testing/SKILL.md): Fornece os conceitos teóricos de TDD, mocks e pirâmide de testes.
