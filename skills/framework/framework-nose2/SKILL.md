---
name: "framework-nose2"
description: "Atua como Especialista em testes automatizados com Nose2 em Python, cobrindo configuração via unittest.cfg, plugins de cobertura e multiprocessamento, parametrização com @params e suítes dinâmicas."
---

# Habilidade de IA: Especialista em Testes com Nose2 (Nose2 Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Automação de Testes especializado no Nose2**, o sucessor oficial do `nose` para ecossistemas Python baseados em `unittest`. O objetivo é otimizar o descobrimento de testes, parametrizar suítes dinâmicas e utilizar o sistema extensível de plugins do Nose2 para medir cobertura e executar testes em paralelo.

---

## 🧭 Princípios e Arquitetura do Nose2

Ao utilizar o Nose2 em projetos Python:
- **Compatibilidade Nativa com `unittest`**: Todos os testes escritos com `unittest.TestCase` são executados pelo Nose2 sem modificações.
- **Suporte a Testes em Funções Standalone**: O Nose2 descobre e executa funções de teste simples sem a obrigatoriedade de instanciar classes `TestCase`.
- **Arquitetura Baseada em Plugins**: Estenda o comportamento do test runner ativando plugins via arquivo de configuração `unittest.cfg`.
- **Parametrização Flexível**: Utilize geradores de teste e o decorador `@params` de `nose2.tools`.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Parametrização com `@params` (`nose2.tools`)
- Utilize o decorador `@params` para injetar múltiplos conjuntos de argumentos em funções ou métodos de teste.

```python
from nose2.tools import params
import unittest

@params(
    ("admin@company.com", True),
    ("user@domain.org", True),
    ("invalid-email", False),
)
def test_email_validation(email_str, expected_result):
    from my_app.validators import is_valid_email
    assert is_valid_email(email_str) == expected_result
```

### 2. Generadores de Teste (Yield-based Tests)
- Escreva funções de teste que geram chamadas com asserções dinâmicas usando o operador `yield`.

```python
def check_square(number, expected_square):
    assert number * number == expected_square

def test_squares_generator():
    cases = [(2, 4), (3, 9), (4, 16), (5, 25)]
    for num, expected in cases:
        yield check_square, num, expected
```

### 3. Filtragem de Testes por Atributos (Plugin `attrib`)
- Atribua metadados aos métodos de teste usando o decorador `@attr` para permitir execuções seletivas (ex: apenas testes rápidos em CI/CD).

```python
import unittest
from nose2.tools import params

class TestPaymentGateway(unittest.TestCase):
    # Atribuindo tag de velocidade e tipo
    tags = ['unit', 'fast']

    def test_local_calculation(self):
        self.assertEqual(10 + 5, 15)

    def test_external_api_call(self):
        # Marcando método como lento
        setattr(self.test_external_api_call, 'speed', 'slow')
        # Lógica de teste...
```

---

## ⚙️ Arquivo de Configuração (`unittest.cfg`)

Exemplo de configuração corporativa ativando cobertura de código e multiprocessamento:

```ini
[unittest]
plugins = nose2.plugins.coverage
          nose2.plugins.attrib
          nose2.plugins.mp

[coverage]
always-on = True
coverage = src
coverage-report = term-missing
coverage-report = html

[multiprocess]
always-on = False
processes = 4
```

---

## 💻 Comandos Úteis de Linha de Comando

```bash
# Execução padrão com saída verbosa
nose2 -v

# Filtrar e executar apenas testes marcados com atributo speed=fast
nose2 -A "speed=fast"

# Executar suíte utilizando 4 processos em paralelo (Multiprocess)
nose2 --multiprocess 4

# Gerar relatório de cobertura HTML
nose2 --with-coverage
```

---

## 🔗 Integração com Outras Skills

- [framework-unittest](../framework-unittest/SKILL.md): Fornece a base estrutural de `unittest.TestCase` estendida pelo Nose2.
- [lang-python](../../languages/lang-python/SKILL.md): Garante conformidade de sintaxe e padrões Python.
- [qa-engineer](../../general/roles/qa-engineer/SKILL.md): Auxilia na categorização de testes rápidos vs lentos.
