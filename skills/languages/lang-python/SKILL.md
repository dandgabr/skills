---
name: "lang-python"
description: "Fornece padrões de engenharia de software em Python 3 baseados na documentação oficial (docs.python.org/pt-br/3), cobrindo o Zen do Python (PEP 20), guia de estilo (PEP 8), Data Model (__dunder__), Pattern Matching (PEP 634), Tipagem Avançada (PEP 484/695), Asyncio, Biblioteca Padrão e frameworks modernos."
---

# Habilidade de IA: Engenharia de Python (Python 3 Specialist)

Esta skill orienta a inteligência artificial a atuar como especialista na linguagem **Python 3**, alinhada rigorosamente às diretrizes da documentação oficial da linguagem ([docs.python.org/pt-br/3](https://docs.python.org/pt-br/3/)), a Referência da Linguagem (*Language Reference*), a Referência da Biblioteca Padrão (*Standard Library*) e as Propostas de Aprimoramento do Python (PEPs). O objetivo é construir código idiomático, expressivo, manutenível, seguro e de alta performance.

---

## 🧭 Diretrizes Gerais e Fundamentos da Linguagem (docs.python.org)

Ao atuar nesta skill, aplique rigorosamente os princípios oficiais da Python Software Foundation:

### 1. Filosofia e Estilo Idiomático (PEP 20, PEP 8 & PEP 257)
- **The Zen of Python (PEP 20)**:
  - *Belo é melhor que feio. Explícito é melhor que implícito. Simples é melhor que complexo.*
  - Evite truques ilegíveis de código ("code golf") em favor da clareza e manutenibilidade.
- **Guia de Estilo PEP 8**:
  - Nomenclatura: `snake_case` para variáveis, funções e métodos; `PascalCase` para classes; `ALL_CAPS` para constantes.
  - Indentação estrita com 4 espaços (nunca misturar tabs e espaços).
  - Organização de imports no topo do arquivo divididos em 3 blocos: (1) Biblioteca Padrão, (2) Bibliotecas de Terceiros e (3) Módulos Locais.
- **Convenções de Docstrings (PEP 257)**:
  - Escreva docstrings explicativas para módulos, classes e funções públicas usando a convenção de aspas triplas `"""Texto explicativo."""`.

### 2. Modelo de Dados da Linguagem (Data Model & Dunder Methods)
- **Métodos Especiais (__dunder__)**: Implemente o comportamento Pythonic das suas classes customizadas utilizando o Data Model oficial:
  - Representação: `__str__` (para exibição amigável ao usuário) e `__repr__` (para depuração inequívoca).
  - Context Managers: `__enter__` e `__exit__` (síncrono) ou `__aenter__` e `__aexit__` (assíncrono com `async with`).
  - Coleções e Iteração: `__len__`, `__getitem__`, `__setitem__`, `__iter__`, `__next__`.
  - Comparação e Hashing: `__eq__` e `__hash__` para objetos utilizáveis como chaves em dicionários e conjuntos.

### 3. Casamento de Padrões Estruturais (Structural Pattern Matching - PEP 634/635/636)
- Utilize a instrução `match / case` (Python 3.10+) para desestruturar sequências, dicionários e instâncias de classes de forma limpa:

```python
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: float
    y: float

def process_event(event: tuple | Point) -> str:
    match event:
        case Point(x=0, y=0):
            return "Origem central"
        case Point(x=x, y=y) if x == y:
            return f"Ponto na diagonal principal: {x}"
        case ("click", x, y):
            return f"Clique no ponteiro: ({x}, {y})"
        case ("key", str(k)) if len(k) == 1:
            return f"Tecla pressionada: {k}"
        case _:
            return "Evento desconhecido"
```

### 4. Sistema de Tipagem Estática e Genéricos (PEP 484, PEP 526 & PEP 695)
- **Anotações de Tipo (`typing`)**: Aplique type hints em assinaturas de funções e atributos centrais do domínio.
- **Sintaxe Moderna de Genéricos (Python 3.12+ - PEP 695)**:
  - Declare genéricos diretamente com a palavra-chave `type` e parâmetros entre colchetes:

```python
# Sintaxe PEP 695 (Python 3.12+)
type Result[T] = dict[str, T]

class Repository[T]:
    def __init__(self, initial_data: list[T]) -> None:
        self._items: list[T] = initial_data

    def get_first(self) -> T | None:
        return self._items[0] if self._items else None
```

---

## 🛠️ Destaques da Biblioteca Padrão (Python Standard Library)

Ao implementar soluções, priorize os módulos embutidos maduros da linguagem antes de adicionar dependências externas:

- **Orientação a Objetos e Dados**:
  - `dataclasses`: Criação de classes de dados com `dataclass(slots=True, frozen=True)`.
  - `enum`: Definição de enums fortemente tipados (`Enum`, `IntEnum`, `StrEnum`).
  - `collections`: `defaultdict`, `Counter`, `deque`, `namedtuple`.
- **E/S e Sistema de Arquivos**:
  - `pathlib`: Manipulação de caminhos de arquivos orientada a objetos (`Path(__file__).parent`).
  - `contextlib`: Criação simplificada de gerenciadores de contexto com `@contextmanager`.
  - `json`: Serialização e parsing seguro de JSON.
- **Execução Assíncrona e Concorrência**:
  - `asyncio`: Event loop nativo, corrotinas (`async def`), tarefas (`asyncio.create_task`) e semáforos (`asyncio.Semaphore`).
  - `concurrent.futures`: Processamento paralelo baseado em threads (`ThreadPoolExecutor`) ou processos (`ProcessPoolExecutor`).
- **Operação e Depuração**:
  - `logging`: Logging estruturado configurado por módulos (`logging.getLogger(__name__)`).
  - `unittest`: Suíte de testes unitários nativa (para compatibilidade sem pacotes externos).

---

## 🧰 Padrões de Código Recomendados

### 1. Gerenciador de Contexto Personalizado (`contextlib`)
```python
from contextlib import contextmanager
from typing import Generator
import time
import logging

logger = logging.getLogger(__name__)

@contextmanager
def execution_timer(task_name: str) -> Generator[None, None, None]:
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start_time
        logger.info(f"Tarefa '{task_name}' concluída em {elapsed:.4f}s")
```

### 2. Aplicação Asyncio Nativa com Tratamento de Sinais
```python
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("worker")

async def worker_task(task_id: int, semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        logger.info(f"Iniciando task {task_id}")
        await asyncio.sleep(0.5)
        logger.info(f"Concluída task {task_id}")

async fn main() -> None:
    semaphore = asyncio.Semaphore(3)
    tasks = [asyncio.create_task(worker_task(i, semaphore)) for i in range(10)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## ⚙️ Gerenciamento de Ambientes e Empacotamento Moderno (PEP 621)

- **`pyproject.toml`**: Centralize metadados do projeto, dependências e configurações de ferramentas (`pytest`, `black`, `mypy`, `ruff`) em um único arquivo conforme a norma PEP 621.
- **Ambientes Virtuais (`venv`)**: Isolar dependências utilizando o módulo nativo `python -m venv .venv` ou gerenciadores modernos de alta performance como `uv` ou `poetry`.

---

## 🔒 Questões de Segurança e Práticas Seguras

- **Deserialização Insegura (CWE-502)**: Nunca desserialize dados não confiáveis usando `pickle`, `marshal` ou `shelve`. Ao usar PyYAML, force sempre a chamada por `yaml.safe_load()`.
- **Injeção de Comandos e Código**: Evite o uso de `eval()`, `exec()` e `subprocess.Popen(..., shell=True)` com dados vindos do usuário. Utilize a API orientada a objetos de listas de argumentos.
- **Argumentos Mutáveis Padrão**: Evite definir listas ou dicionários como argumentos padrão em funções (ex: `def func(val=[])`), pois eles persistem entre as execuções e podem causar bugs lógicos e vazamento de dados.
- **Path Traversal (CWE-22)**: Use `pathlib.Path` e valide a segurança de caminhos resolvidos com `Path.resolve()` contra caminhos base (ex: impedindo navegação para pastas superiores via `../`).

## 🔗 Integração com Outras Skills

- Para criar suítes de testes unitários e de integração parametrizadas em Python, consulte [framework-pytest](../../framework/framework-testing-python/SKILL.md) e [framework-unittest](../../framework/framework-testing-python/SKILL.md).
- Para integrar e otimizar acessos a bancos de dados relacionais e NoSQL em Python (SQLAlchemy, psycopg, PyMongo, Tortoise ORM), consulte [dba-database-administrator](../../roles/dba-database-administrator/SKILL.md), [db-postgresql](../../databases/db-postgresql/SKILL.md), [db-sqlite](../../databases/db-sqlite/SKILL.md), [db-mariadb](../../databases/db-mariadb/SKILL.md) e [db-mongodb](../../databases/db-mongodb/SKILL.md).
- Para desenvolver ferramentas ofensivas, scripts de rede e utilitários de segurança em Python, consulte [pentest-scripter-python-bash-go](../../security/appsec/pentest-scripter-python-bash-go/SKILL.md).
- Para auditar código Python contra falhas de segurança (SAST) e aplicar correções de código limpo, consulte [sast-code-review](../../security/appsec/sast-code-review/SKILL.md) e [clean-code-reusability](../../engineering-practices/clean-code-reusability/SKILL.md).
