# Repositório de Definição de Agentes (ADK 2.0)

Este diretório contém as definições declarativas dos agentes do projeto utilizando a estrutura compatível com a especificação de **Agent Config do Agent Development Kit (ADK 2.0)** da Google.

## 📁 Estrutura de Agentes

```text
.\
├── README.md               # Este guia explicativo
├── documenter\
│   └── agent.yaml          # Definição do Agente Documentador e Designer
├── software-architect\
│   └── agent.yaml          # Definição do Agente Arquiteto de Software
├── fullstack-developer\
│   └── agent.yaml          # Definição do Agente de Desenvolvimento Full Stack
├── devops-engineer\
│   └── agent.yaml          # Definição do Agente de DevOps
├── security-specialist\
│   └── agent.yaml          # Definição do Agente Especialista em Segurança
└── pentester-agent\
    └── agent.yaml          # Definição do Agente de Pentest Ético
```

## 🤖 Agentes Disponíveis

### 1. [documenter](documenter/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Especializado em desenhar diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe do Mermaid.js.
- **Skill Associada**: [documentation-designer](../skills/general/documentation-designer/SKILL.md)

### 2. [software-architect](software-architect/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Especializado na aplicação de DDD, SOLID, gerenciamento de JVM/plataforma interna e orquestração de Padrões de Projeto (Design Patterns).
- **Skill Associada**: [software-architect](../skills/general/software-architect/SKILL.md)

### 3. [fullstack-developer](fullstack-developer/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Projetar e implementar soluções web fim a fim (Backend e Frontend), garantindo legibilidade, integridade de código e documentação.
- **Skills Associadas**: [backend-developer](../skills/general/backend-developer/SKILL.md), [frontend-developer](../skills/general/frontend-developer/SKILL.md) e [clean-code-reusability](../skills/general/clean-code-reusability/SKILL.md)

### 4. [devops-engineer](devops-engineer/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Provisionamento de infraestrutura como código (IaC), deploy e operação confiável de pipelines e containers.
- **Skill Associada**: [devops-engineer](../skills/general/devops-engineer/SKILL.md)

### 5. [security-specialist](security-specialist/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Modelagem de ameaças, controles de código seguro baseados em OWASP ASVS, auditorias, DevSecOps e conformidade regulatória de privacidade.
- **Skills Associadas**: [appsec-owasp-asvs](../skills/security/appsec-owasp-asvs/SKILL.md), [devsecops-engineer](../skills/security/devsecops-engineer/SKILL.md), [security-grc-compliance](../skills/security/security-grc-compliance/SKILL.md), [security-privacy](../skills/security/security-privacy/SKILL.md) e [threat-modeler](../skills/security/threat-modeler/SKILL.md)

### 6. [pentester-agent](pentester-agent/agent.yaml)
- **Modelo Base**: `gemini-2.0-flash`
- **Função**: Executar análises ofensivas estruturadas baseadas em OWASP WSTG e API Security usando utilitários CLI (nmap, curl, zap-cli, tshark), delegando ao time de desenvolvimento a codificação de scripts de exploração customizados de forma limpa.
- **Skills Associadas**: [pentester-owasp-wstg](../skills/security/pentester-owasp-wstg/SKILL.md) e [pentester-owasp-api-security-2023](../skills/security/pentester-owasp-api-security-2023/SKILL.md)

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
