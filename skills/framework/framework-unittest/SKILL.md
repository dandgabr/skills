---
name: "framework-unittest"
description: "Atua como Especialista em testes automatizados com a biblioteca nativa unittest do Python, cobrindo TestCase, asserções, métodos de ciclo de vida (setUp/tearDown), subtests, unittest.mock (@patch, MagicMock) e test discovery."
---

# Habilidade de IA: Especialista em Testes com Unittest (Python Unittest Specialist)

Esta skill orienta a inteligência artificial a agir como **Engenheiro de QA e Desenvolvimento especializado no framework nativo `unittest` do Python**. O objetivo é guiar a construção de suítes de testes sem dependências externas, utilizando as convenções orientadas a objetos do `unittest.TestCase` e os recursos avançados de substituição com `unittest.mock`.

---

## 🧭 Princípios e Arquitetura do Unittest

Ao utilizar o `unittest`, aplique as diretrizes estruturais nativas da biblioteca padrão:
- **Classes de Teste Derivadas de `unittest.TestCase`**: Agrupe testes relacionados em classes que estendem `TestCase`.
- **Ciclo de Vida Determinístico**:
  - `setUp()` / `tearDown()`: Executados imediatamente antes e depois de cada método de teste individual.
  - `setUpClass()` / `tearDownClass()`: Executados uma única vez para toda a classe de teste (devem ser decorados com `@classmethod`).
- **Métodos de Asserção Explícitos**: Utilize os métodos da classe `TestCase` (`assertEqual`, `assertRaises`, `assertIn`, etc.) para garantir mensagens de erro descritivas em caso de falha.
- **Isolamento sem Dependências**: Projete suítes de testes leves capazes de rodar em qualquer ambiente Python nativo usando `python -m unittest discover`.

---

## 🛠️ Diretrizes Práticas de Engenharia e Padrões de Código

### 1. Estrutura de TestCase e Ciclo de Vida
- Organize a inicialização de recursos e garanta a limpeza adequada no `tearDown`.

```python
import unittest
from my_app.services import UserRegistry

class TestUserRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes da classe."""
        cls.shared_resource = {"environment": "test"}

    def setUp(self):
        """Executado antes de cada teste individual."""
        self.registry = UserRegistry()
        self.registry.clear()

    def tearDown(self):
        """Executado após cada teste individual para garantia de limpeza."""
        self.registry.clear()

    def test_register_user_success(self):
        user = self.registry.register("alice@example.com", "Alice")
        self.assertEqual(user.email, "alice@example.com")
        self.assertTrue(self.registry.exists("alice@example.com"))

    def test_register_duplicate_user_raises_exception(self):
        self.registry.register("bob@example.com", "Bob")
        with self.assertRaises(ValueError):
            self.registry.register("bob@example.com", "Bob Repetido")
```

### 2. Uso de Subtests para Parametrização (`self.subTest`)
- Utilize o gerenciador de contexto `self.subTest()` para iterar sobre múltiplos cenários sem interromper a execução dos demais em caso de falha.

```python
import unittest
from my_app.utils import is_even

class TestUtilityFunctions(unittest.TestCase):
    def test_is_even_with_multiple_inputs(self):
        cases = [
            (2, True),
            (3, False),
            (0, True),
            (-4, True),
            (-5, False),
        ]
        for number, expected in cases:
            with self.subTest(number=number, expected=expected):
                self.assertEqual(is_even(number), expected)
```

### 3. Mocks Avançados com `unittest.mock` (`@patch`, `MagicMock`)
- Substitua chamadas externas, bancos de dados ou rotas de rede utilizando os decoradores e objetos de `unittest.mock`.

```python
import unittest
from unittest.mock import patch, MagicMock
from my_app.services import WeatherService

class TestWeatherService(unittest.TestCase):
    @patch("my_app.services.requests.get")
    def test_get_temperature_success(self, mock_get):
        # Configurando a resposta mock do objeto requests
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"main": {"temp": 25.5}}
        mock_get.return_value = mock_response

        service = WeatherService(api_key="fake_key")
        temp = service.get_temperature("Sao Paulo")

        self.assertEqual(temp, 25.5)
        mock_get.assert_called_once_with(
            "https://api.weather.org/data",
            params={"q": "Sao Paulo", "appid": "fake_key"}
        )
```

---

## ⚙️ Execução e Descoberta de Testes

Execute os testes via linha de comando sem necessidade de instalação de pacotes externos:

```bash
# Descobrir e rodar todos os testes na pasta 'tests'
python -m unittest discover -s tests -p "test_*.py" -v

# Rodar um teste específico de uma classe
python -m unittest tests.test_user.TestUserRegistry.test_register_user_success
```

---

## 🔗 Integração com Outras Skills

- [lang-python](../../languages/lang-python/SKILL.md): Garante conformidade com estilo de código estrito e tipagem.
- [qa-engineer](../../general/roles/qa-engineer/SKILL.md): Orienta a estruturação de planos de teste unitários em projetos sem dependências de terceiros.
- [framework-testing](../framework-testing/SKILL.md): Apresenta os conceitos de isolamento, stubs e mocks.
