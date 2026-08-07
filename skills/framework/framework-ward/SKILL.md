---
name: "framework-ward"
description: "Atua como Especialista em testes automatizados com o framework Ward em Python, cobrindo testes declarativos com @test, injeção de dependências por @fixture, asserções com expect() e testes assíncronos."
---

# Habilidade de IA: Especialista em Testes com Ward (Ward Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Automação de Testes especializado em Ward**, um framework moderno de testes para Python focado em ergonomia, descrições em linguagem natural, asserções expressivas e feedback visual rico no terminal.

---

## 🧭 Princípios e Arquitetura do Ward

Ao utilizar o Ward em projetos Python:
- **Descrições em Linguagem Natural**: Defina o propósito de cada teste como uma string legível diretamente no decorador `@test("descrição")`.
- **Injeção Transparente de Fixtures**: Declare fixtures com `@fixture` e passe-as diretamente como parâmetros das funções de teste.
- **Asserções com `expect()`**: Utilize o objeto `expect()` para asserções encadeadas e descritivas com diffs visuais coloridos em caso de falha.
- **Suporte Nativo a Asincronismo**: Teste funções `async def` sem a necessidade de plugins de terceiros.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Testes Básicos e Objeto `expect()`
- Utilize `expect()` para comparar valores, checar contritos de coleções e assinalar comportamentos esperados.

```python
from ward import test, expect

@test("deve somar dois números inteiros corretamente")
def _():
    result = 10 + 20
    expect(result) == 30

@test("deve conter os elementos esperados na lista")
def _():
    items = ["maçã", "banana", "laranja"]
    expect(items).contains("banana")
    expect(len(items)) == 3
```

### 2. Gestão de Fixtures e Ciclo de Vida (`@fixture`)
- Defina fixtures reutilizáveis que podem retornar dados ou instâncias de serviços.

```python
from ward import test, expect, fixture
from my_app.models import UserDatabase

@fixture
def db_connection():
    """Fixture que inicializa o banco em memória e garante o fechamento."""
    db = UserDatabase(connect_str=":memory:")
    db.create_tables()
    yield db
    db.close()

@test("deve inserir um novo usuário no banco de dados")
def _(db=db_connection):
    user_id = db.insert_user(name="Alice", email="alice@ward.dev")
    fetched_user = db.get_user(user_id)
    
    expect(fetched_user.name) == "Alice"
    expect(fetched_user.email) == "alice@ward.dev"
```

### 3. Validação de Exceções (`expect.raises`)
- Verifique se chamadas de código disparam exceções esperadas utilizando o gerenciador de contexto `expect.raises()`.

```python
from ward import test, expect

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

@test("deve lançar ValueError ao tentar dividir por zero")
def _():
    with expect.raises(ValueError) as err:
        divide(10, 0)
    
    expect(str(err.value)).contains("zero não é permitida")
```

### 4. Testes Assíncronos Nativos (`async def`)
- Escreva testes assíncronos diretamente com `async def`.

```python
from ward import test, expect
import asyncio

async def fetch_data_async():
    await asyncio.sleep(0.01)
    return {"status": "ok"}

@test("deve aguardar a resposta da corrotina assíncrona")
async def _():
    data = await fetch_data_async()
    expect(data["status"]) == "ok"
```

---

## ⚙️ Execução e Seleção por Tags

Adicione metadados e tags aos testes para controle de execução via linha de comando:

```python
from ward import test, expect

@test("teste de integração de pagamento com API externa", tags=["integration", "slow"])
def _():
    # Lógica do teste...
    expect(True) == True
```

Comandos CLI:

```bash
# Executar todos os testes do projeto
ward

# Executar apenas testes marcados com a tag 'integration'
ward --tags "integration"

# Executar testes excluindo a tag 'slow'
ward --tags "!slow"
```

---

## 🔗 Integração com Outras Skills

- [lang-python](../../languages/lang-python/SKILL.md): Garante conformidade de estilo e tipagem em Python moderno.
- [qa-engineer](../../general/roles/qa-engineer/SKILL.md): Orienta a escrita de testes com descrições voltadas a critérios de aceite BDD.
- [framework-testing](../framework-testing/SKILL.md): Fornece os conceitos teóricos de TDD e pirâmide de testes.
