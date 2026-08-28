---
name: "framework-pytest"
description: "Atua como Especialista em testes automatizados com Pytest em Python, cobrindo fixtures, parametrização formal (BVA/Partições), Property-Based Testing (Hypothesis), Mocks (pytest-mock), Testes de Mutação (mutmut), async e cobertura com pytest-cov."
---

# Habilidade de IA: Especialista em Testes com Pytest (Pytest Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Automação de Testes especializado em Pytest**, aplicando rigor metodológico de engenharia de software baseado em **Paul C. Jorgensen** (*Software Testing: A Craftsman's Approach*), **Ali Mili** e diretrizes ISTQB.

O objetivo é guiar a criação de suítes de testes limpas, expressivas, parametrizadas formalmente e testadas contra mutantes para garantir zero regressões.

---

## 🧭 Princípios e Arquitetura do Pytest

- **Assertions Simples e Nativas**: Utilize o `assert` nativo do Python. O Pytest reescreve a AST para fornecer diffs detalhados automaticamente sem necessidade de asserts verbosos.
- **Injeção de Dependências por Fixtures**: Substitua estruturas rígidas de `setUp`/`tearDown` por fixtures modulares e reutilizáveis.
- **Descobrimento Automático**: Nomenclatura padronizada `test_*.py` / `*_test.py` e funções `test_*`.
- **Modularização via `conftest.py`**: Compartilhe fixtures e hooks por diretórios sem imports manuais cíclicos.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Parametrização Formal de BVA e Tabelas de Decisão (`@pytest.mark.parametrize`)
Aplique amostragem de valor limite canônica ($min-, min, min+, nom, max-, max, max+$) diretamente na parametrização do Pytest:

```python
import pytest
from my_app.services import validate_withdrawal

# Domínio válido de saque: [10.0, 5000.0]
@pytest.mark.parametrize("amount, balance, is_blocked, expected_status, raises_exc", [
    # BVA: Limites da variável amount
    (9.99, 1000.0, False, None, True),          # min- (Robusto inválido)
    (10.0, 1000.0, False, "APPROVED", False),    # min
    (10.01, 1000.0, False, "APPROVED", False),   # min+
    (500.0, 1000.0, False, "APPROVED", False),   # nom
    (4999.99, 6000.0, False, "APPROVED", False), # max-
    (5000.0, 6000.0, False, "APPROVED", False),  # max
    (5000.01, 6000.0, False, None, True),        # max+ (Robusto inválido)
    # Tabela de Decisão: Condições de Saldo e Bloqueio
    (100.0, 50.0, False, "INSUFFICIENT_FUNDS", False),
    (100.0, 1000.0, True, "CARD_BLOCKED", False),
])
def test_withdrawal_bva_and_decision_rules(amount, balance, is_blocked, expected_status, raises_exc):
    if raises_exc:
        with pytest.raises(ValueError):
            validate_withdrawal(amount=amount, balance=balance, is_blocked=is_blocked)
    else:
        status = validate_withdrawal(amount=amount, balance=balance, is_blocked=is_blocked)
        assert status == expected_status
```

### 2. Property-Based Testing com `hypothesis` (Oráculos Metamórficos)
Quando testar entradas exaustivas ou quando o oráculo direto for complexo, utilize propriedades invariantes:

```python
from hypothesis import given, strategies as st
from my_app.algorithms import sort_items, compress, decompress

# Invariante 1: O tamanho do array ordenado é idempotente e preserva elementos
@given(st.lists(st.integers()))
def test_sort_invariants(numbers):
    result = sort_items(numbers)
    assert len(result) == len(numbers)
    assert sorted(numbers) == result

# Invariante 2 (Metamórfica): Compressão -> Descompressão restaura o dado original
@given(st.text(min_size=1))
def test_compression_roundtrip(payload):
    compressed = compress(payload)
    decompressed = decompress(compressed)
    assert decompressed == payload
```

### 3. Fixtures e Gestão de Recursos (`@pytest.fixture`)

```python
import pytest
from my_app.db import DatabaseConnection

@pytest.fixture(scope="session")
def db_engine():
    """Fixture de sessão para inicializar banco em memória."""
    engine = DatabaseConnection.create_in_memory()
    engine.setup_tables()
    yield engine
    engine.dispose()

@pytest.fixture
def db_session(db_engine):
    """Isolamento por função com rollback automático em transação."""
    connection = db_engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()
```

### 4. Mocks e Spies com `pytest-mock` (`mocker`)

```python
def test_process_payment_success(mocker):
    mock_gateway = mocker.patch("my_app.services.ExternalGateway.charge")
    mock_gateway.return_value = {"status": "SUCCESS", "tx_id": "tx_999"}

    processor = PaymentProcessor()
    result = processor.execute(order_id="123", amount=150.00)

    assert result["success"] is True
    assert result["tx_id"] == "tx_999"
    mock_gateway.assert_called_once_with(amount=150.00)
```

---

## 🧬 Testes de Mutação em Python (`mutmut`)

Para mensurar o Escore de Mutação ($MS$) e garantir que a suíte mata mutantes de operadores aritméticos e relacionais:

```bash
# Execução da análise de mutação
mutmut run --paths-to-mutate=src/

# Verificação do relatório de mutantes sobreviventes
mutmut results
mutmut show <mutant_id>
```

---

## ⚙️ Configuração Recomendada (`pyproject.toml`)

```toml
[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra -q --cov=src --cov-report=term-missing --cov-fail-under=85"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
markers = [
    "slow: marca testes que demandam I/O ou contêineres",
    "integration: testes de integração inter-módulos",
]
```

---

## 🔗 Integração com Outras Skills
- [qa-engineer](../../roles/qa-engineer/SKILL.md): Matriz de RBT e critérios de aceite.
- [framework-testing](../framework-testing/SKILL.md): Fundamentos de caixa-preta, caixa-branca e mutação.
- [lang-python](../../languages/lang-python/SKILL.md): Tipagem com mypy e conformidade PEP 8.
