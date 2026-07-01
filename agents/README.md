# Repositório de Definição de Agentes (ADK 2.0)

Este diretório contém as definições declarativas dos agentes do projeto utilizando a estrutura compatível com a especificação de **Agent Config do Agent Development Kit (ADK 2.0)** da Google.

## 📁 Estrutura de Agentes

```text
.\
├── README.md               # Este guia explicativo
├── documenter\
│   └── agent.yaml          # Definição do Agente Documentador e Designer
└── software-architect\
    └── agent.yaml          # Definição do Agente Arquiteto de Software
```

## 🤖 Agentes Disponíveis

### 1. [documenter](documenter/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Especializado em desenhar fluxogramas, diagramas de classe e sequências de APIs utilizando a sintaxe correta do Mermaid.js.
- **Skill Associada**: [documentation-designer](../skills/documentation-designer/SKILL.md)

### 2. [software-architect](software-architect/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Especializado na aplicação de DDD, SOLID, gerenciamento de JVM/plataforma interna e orquestração de Padrões de Projeto (Design Patterns).
- **Skill Associada**: [software-architect](../skills/software-architect/SKILL.md)

## 🚀 Como Invocá-los via ADK 2.0

Para instanciar e rodar esses agentes em seus scripts ou fluxos colaborativos baseados em grafo do ADK 2.0, você pode carregá-los declarativamente usando o runtime do ADK:

```python
import asyncio
from google.adk.agents import config_agent_utils
from google.adk.runners import Runner

async def main():
    # Carregar os agentes declarativamente do YAML usando utilitário do ADK 2.0
    architect_agent = config_agent_utils.from_config("software-architect/agent.yaml")
    documenter_agent = config_agent_utils.from_config("documenter/agent.yaml")

    # Executar o agente de arquitetura em runtime usando o Runner do ADK 2.0
    runner = Runner()
    response = await runner.run(
        agent=architect_agent,
        prompt="Projete a modelagem tática da camada de domínio para um e-commerce"
    )
    print(response.output)

if __name__ == "__main__":
    asyncio.run(main())
```
