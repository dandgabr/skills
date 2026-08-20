# Repositório de Definição de Agentes (ADK 2.0)

Este diretório contém as definições declarativas dos agentes do projeto utilizando a estrutura compatível com a especificação de **Agent Config do Agent Development Kit (ADK 2.0)** da Google.

## 📁 Estrutura de Agentes

```text
.\
├── README.md                           # Este guia explicativo
├── documenter\
│   └── agent.yaml                      # Agente Documentador e Designer (Mermaid)
├── software-architect\
│   └── agent.yaml                      # Agente Arquiteto de Software
├── fullstack-developer\
│   └── agent.yaml                      # Agente Desenvolvedor Full Stack
├── moodle-specialist\
│   └── agent.yaml                      # Agente Especialista em Moodle LMS e EdTech
├── devops-engineer\
│   └── agent.yaml                      # Agente Engenheiro de DevOps e DevSecOps
├── dba-specialist\
│   └── agent.yaml                      # Agente Administrador de Banco de Dados (DBA)
├── telecom-voice-specialist\
│   └── agent.yaml                      # Agente Engenheiro de Voz e Telefonia (VoIP/SBC/PSTN)
├── cloud-infrastructure-architect\
│   └── agent.yaml                      # Agente Arquiteto de Infraestrutura Multi-Cloud & FinOps
├── qa-testing-specialist\
│   └── agent.yaml                      # Agente Especialista em QA e Automação de Testes
├── ai-security-specialist\
│   └── agent.yaml                      # Agente Especialista em Segurança de IA (LLM/CV/Voice)
├── security-specialist\
│   └── agent.yaml                      # Agente Especialista em Segurança e DevSecOps
├── pentester-agent\
│   └── agent.yaml                      # Agente de Pentest Ético e Red Teaming
├── iam-specialist\
│   └── agent.yaml                      # Agente Especialista em IAM, Entra ID, Power Platform e Cloud Access
├── project-reviewer\
│   └── agent.yaml                      # Agente Revisor de Projetos Especialista
├── reverse-engineer-agent\
│   └── agent.yaml                      # Agente de Engenharia Reversa e Baixo Nível
├── skill-creator\
│   └── agent.yaml                      # Agente Especialista em Criação e Governança de Skills
├── antigravity-agent\
│   └── agent.yaml                      # Agente Principal Antigravity (Pair Programmer & Autônomo)
├── researcher\
│   └── agent.yaml                      # Subagente Especialista em Pesquisa e Varredura de Codebase
├── self\
│   └── agent.yaml                      # Subagente de Clonagem e Isolamento de Contexto (Self Subagent)
├── explore\
│   └── agent.yaml                      # Subagente Especialista em Exploração Rápida de Codebases
└── general\
    └── agent.yaml                      # Agente Generalista Multi-Etapas e Orquestrador
```

## 🤖 Agentes Disponíveis

### 1. [documenter](documenter/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Especializado em desenhar diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe do Mermaid.js.
- **Skill Associada**: [documentation-designer](../skills/general/engineering-practices/documentation-designer/SKILL.md)

### 2. [software-architect](software-architect/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Especializado na aplicação de DDD, SOLID, gerenciamento de JVM/plataforma interna e orquestração de Padrões de Projeto (Design Patterns).
- **Skill Associada**: [software-architect](../skills/general/roles/software-architect/SKILL.md)

### 3. [fullstack-developer](fullstack-developer/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Projetar e implementar soluções web fim a fim (Backend, Frontend e Banco de Dados), garantindo legibilidade, integridade de código e segurança.
- **Skills Associadas**: [backend-developer](../skills/general/roles/backend-developer/SKILL.md), [frontend-developer](../skills/general/roles/frontend-developer/SKILL.md), [dba-database-administrator](../skills/general/roles/dba-database-administrator/SKILL.md), [appsec-owasp-asvs](../skills/security/appsec/appsec-owasp-asvs/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

### 4. [devops-engineer](devops-engineer/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Provisionamento de infraestrutura como código (IaC), plataformas internas (Backstage), orquestração de containers (Docker, Podman, CRI-O, K8s), governança GitHub e pipelines CI/CD (GitHub Actions) com segurança integrada (DevSecOps).
- **Skills Associadas**: [devops-engineer](../skills/general/roles/devops-engineer/SKILL.md), [program-github](../skills/programs/github/SKILL.md), [github-actions](../skills/programs/github-actions/SKILL.md), [containers](../skills/programs/containers/SKILL.md), [devsecops-engineer](../skills/security/ops-architecture/devsecops-engineer/SKILL.md) e [cis-controls](../skills/security/grc-compliance/cis-controls/SKILL.md)

### 5. [dba-specialist](dba-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Administração de bancos de dados SQL e NoSQL, modelagem de esquemas, tunagem de planos de execução (EXPLAIN), replicação, backups (PITR) e segurança.
- **Skills Associadas**: [dba-database-administrator](../skills/general/roles/dba-database-administrator/SKILL.md), [db-postgresql](../skills/general/databases/db-postgresql/SKILL.md), [db-mariadb](../skills/general/databases/db-mariadb/SKILL.md), [db-sqlite](../skills/general/databases/db-sqlite/SKILL.md) e [db-mongodb](../skills/general/databases/db-mongodb/SKILL.md)

### 6. [telecom-voice-specialist](telecom-voice-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Engenharia de voz, telefonia IP (VoIP), interconexão PSTN, Session Border Controllers (SBC), WebRTC, QoS (DSCP EF), STIR/SHAKEN e combate a fraudes.
- **Skills Associadas**: [telecom-voice-engineering](../skills/general/domains/telecom-voice-engineering/SKILL.md), [ai-voice-stt-tts-security](../skills/security/ai-security/ai-voice-stt-tts-security/SKILL.md) e [auth-protocols-mfa](../skills/security/ops-architecture/auth-protocols-mfa/SKILL.md)

### 7. [cloud-infrastructure-architect](cloud-infrastructure-architect/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Arquitetura e operação Multi-Cloud (AWS, Azure, GCP, OCI), Well-Architected Framework, governança de custos (FinOps) e auditorias de segurança em nuvem.
- **Skills Associadas**: [cloud-aws](../skills/general/cloud-infra/cloud-aws/SKILL.md), [cloud-azure](../skills/general/cloud-infra/cloud-azure/SKILL.md), [cloud-gcp](../skills/general/cloud-infra/cloud-gcp/SKILL.md), [cloud-oci](../skills/general/cloud-infra/cloud-oci/SKILL.md), [csa-cloud-security](../skills/security/cloud-iam/csa-cloud-security/SKILL.md) e [iam-access-management](../skills/security/cloud-iam/iam-access-management/SKILL.md)

### 8. [qa-testing-specialist](qa-testing-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Automação de testes de software multi-framework (Pytest, Unittest, Jest, Mocha, Criterion), estratégias de cobertura e relatórios de defeitos.
- **Skills Associadas**: [qa-engineer](../skills/general/roles/qa-engineer/SKILL.md), [framework-testing](../skills/framework/framework-testing/SKILL.md), [framework-pytest](../skills/framework/framework-pytest/SKILL.md), [framework-unittest](../skills/framework/framework-unittest/SKILL.md), [framework-jest](../skills/framework/framework-jest/SKILL.md), [framework-mocha](../skills/framework/framework-mocha/SKILL.md) e [framework-criterion](../skills/framework/framework-criterion/SKILL.md)

### 9. [ai-security-specialist](ai-security-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Segurança e Red Teaming de Inteligência Artificial Generativa (LLM/SLM), Visão Computacional e Voz, mitigando Prompt Injection e envenenamento de dados.
- **Skills Associadas**: [ai-llm-slm-security](../skills/security/ai-security/ai-llm-slm-security/SKILL.md), [ai-computer-vision-security](../skills/security/ai-security/ai-computer-vision-security/SKILL.md), [ai-voice-stt-tts-security](../skills/security/ai-security/ai-voice-stt-tts-security/SKILL.md) e [pentest-ai-generative-llm](../skills/security/appsec/pentest-ai-generative-llm/SKILL.md)

### 10. [security-specialist](security-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Modelagem de ameaças, controles de código seguro baseados em OWASP ASVS, auditorias, DevSecOps e conformidade regulatória de privacidade.
- **Skills Associadas**: [appsec-owasp-asvs](../skills/security/appsec/appsec-owasp-asvs/SKILL.md), [devsecops-engineer](../skills/security/ops-architecture/devsecops-engineer/SKILL.md), [security-grc-compliance](../skills/security/grc-compliance/security-grc-compliance/SKILL.md), [security-privacy](../skills/security/grc-compliance/security-privacy/SKILL.md) e [threat-modeler](../skills/security/ops-architecture/threat-modeler/SKILL.md)

### 11. [iam-specialist](iam-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Projetar, auditar e gerenciar arquiteturas de controle de acesso (RBAC/ABAC/PBAC), governança de identidades (PIM/PAM), federação SSO (SAML/OIDC), provisionamento SCIM e politicas de acesso em nuvem e plataformas corporativas (Power Platform, Dataverse, Entra ID, AWS, Azure, GCP, OCI).
- **Skills Associadas**: [iam-access-management](../skills/security/cloud-iam/iam-access-management/SKILL.md), [iam-access-power-platform](../skills/security/cloud-iam/iam-access-power-platform/SKILL.md), [iam-access-azure](../skills/security/cloud-iam/iam-access-azure/SKILL.md), [iam-access-aws](../skills/security/cloud-iam/iam-access-aws/SKILL.md), [iam-access-gcp](../skills/security/cloud-iam/iam-access-gcp/SKILL.md), [iam-access-oci](../skills/security/cloud-iam/iam-access-oci/SKILL.md) e [csa-cloud-security](../skills/security/cloud-iam/csa-cloud-security/SKILL.md)

### 12. [pentester-agent](pentester-agent/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Executar análises ofensivas estruturadas baseadas em OWASP WSTG, API Security, Cloud e Red Team Scripting usando utilitários CLI (nmap, curl, zap-cli, tshark).
- **Skills Associadas**: [pentester-owasp-wstg](../skills/security/appsec/pentester-owasp-wstg/SKILL.md), [pentester-owasp-api-security-2023](../skills/security/appsec/pentester-owasp-api-security-2023/SKILL.md), [pentest-cloud-aws-azure-gcp](../skills/security/appsec/pentest-cloud-aws-azure-gcp/SKILL.md), [pentest-web-application-modern](../skills/security/appsec/pentest-web-application-modern/SKILL.md) e [pentest-scripter-python-bash-go](../skills/security/appsec/pentest-scripter-python-bash-go/SKILL.md)

### 13. [project-reviewer](project-reviewer/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Revisar, padronizar e distribuir requisitos de negócio entre Banco de Dados, Backend e Frontend, garantindo a aplicação de boas práticas de arquitetura e segurança.
- **Skills Associadas**: [project-reviewer](../skills/general/roles/project-reviewer/SKILL.md), [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md), [appsec-owasp-asvs](../skills/security/appsec/appsec-owasp-asvs/SKILL.md) e [security-privacy](../skills/security/grc-compliance/security-privacy/SKILL.md)

### 14. [reverse-engineer-agent](reverse-engineer-agent/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Depuração, análise dinâmica de binários, manipulação direta de RAM (Cheat Engine) e validação de segurança de código de baixo nível.
- **Skills Associadas**: [program-cheat-engine](../skills/programs/program-cheat-engine/SKILL.md), [memory-manipulation](../skills/security/appsec/memory-manipulation/SKILL.md), [sast-code-review](../skills/security/appsec/sast-code-review/SKILL.md) e [appsec-owasp-asvs](../skills/security/appsec/appsec-owasp-asvs/SKILL.md)

### 15. [moodle-specialist](moodle-specialist/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Especialista em ciclo completo de desenvolvimento, infraestrutura física, banco de dados (DBA), temas de design/UX e metodologias de Andragogia e EdTech para o Moodle LMS.
- **Skills Associadas**: [program-moodle](../skills/programs/moodle/SKILL.md), [program-moodle-dba](../skills/programs/moodle-dba/SKILL.md), [program-moodle-design](../skills/programs/moodle-design/SKILL.md), [program-moodle-infra](../skills/programs/moodle-infra/SKILL.md), [program-moodle-plugins](../skills/programs/moodle-plugins/SKILL.md) e [edtech-andragogy](../skills/general/domains/edtech-andragogy/SKILL.md)

### 16. [skill-creator](skill-creator/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Especialista em arquitetura, criação, aprimoramento e catalogação de Skills do projeto, dominando a conversão de livros/documentos PDF em Markdown estruturado, elaboração de SKILL.md de padrão de produção, interconexão de habilidades e governança do repositório.
- **Skills Associadas**: [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md) e [documentation-designer](../skills/general/engineering-practices/documentation-designer/SKILL.md)

### 17. [antigravity-agent](antigravity-agent/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Agente Principal de Pair Programming Autônomo e Engenharia do ecossistema Google Antigravity. Especializado em desenvolvimento fim a fim, refatoração, resolução de problemas, execução de comandos e extensibilidade via customizações (Skills, Rules, Plugins, Hooks e MCP).
- **Skills Associadas**: [antigravity-guide](../skills/programs/antigravity-guide/SKILL.md), [agy-customizations](../skills/programs/agy-customizations/SKILL.md), [program-github](../skills/programs/github/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

### 18. [researcher](researcher/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Subagente Especialista em Pesquisa, Varredura de Codebase, Análise de Documentação e Busca Externa com ferramentas de leitura estrita, preservando a janela de contexto principal do desenvolvedor/agente coordenador.
- **Skills Associadas**: [antigravity-guide](../skills/programs/antigravity-guide/SKILL.md), [explore](../skills/general/roles/explore/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

### 19. [self](self/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Subagente de Clonagem e Continuidade de Contexto (Self Subagent). Herda integralmente as configurações, ferramentas e modelo do agente principal para isolar subtarefas complexas e permitir execução paralela sem poluir a sessão primária.
- **Skills Associadas**: [antigravity-guide](../skills/programs/antigravity-guide/SKILL.md), [agy-customizations](../skills/programs/agy-customizations/SKILL.md), [general](../skills/general/roles/general/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

### 20. [explore](explore/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Subagente Especialista em Exploração Rápida de Codebases, busca de padrões, mapeamento de arquitetura de diretórios, identificação de contratos e diagnóstico de débitos técnicos.
- **Skills Associadas**: [explore](../skills/general/roles/explore/SKILL.md), [software-architect](../skills/general/roles/software-architect/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

### 21. [general](general/agent.yaml)
- **Modelo Base**: `google/gemini-2.5-pro`
- **Função**: Agente Generalista Multi-Etapas, especializado em planejamento e orquestração de tarefas complexas, decomposição em etapas atômicas e coordenação dinâmica de múltiplas habilidades.
- **Skills Associadas**: [general](../skills/general/roles/general/SKILL.md), [software-architect](../skills/general/roles/software-architect/SKILL.md), [agy-customizations](../skills/programs/agy-customizations/SKILL.md) e [clean-code-reusability](../skills/general/engineering-practices/clean-code-reusability/SKILL.md)

## 🚀 Como Invocá-los via ADK 2.0

Para instanciar e rodar esses agentes em seus scripts ou fluxos colaborativos baseados em grafo do ADK 2.0, você pode carregá-los declarativamente usando o runtime do ADK:

```python
import asyncio
from google.adk.agents import config_agent_utils
from google.adk.runners import Runner

async def main():
    # Carregar os agentes declarativamente do YAML usando utilitário do ADK 2.0
    architect_agent = config_agent_utils.from_config("software-architect/agent.yaml")
    dba_agent = config_agent_utils.from_config("dba-specialist/agent.yaml")

    # Executar o agente de banco de dados em runtime usando o Runner do ADK 2.0
    runner = Runner()
    response = await runner.run(
        agent=dba_agent,
        prompt="Analise o plano de execução EXPLAIN ANALYZE da consulta e proponha um índice GIN ou B-Tree"
    )
    print(response.output)

if __name__ == "__main__":
    asyncio.run(main())
```
