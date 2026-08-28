# 🤖 Agentes Especializados Universais (Multi-Harness Architecture)

Este repositório adota a **Arquitetura Multi-Harness**, garantindo que todos os **27 Agentes Especializados** sejam utilizáveis de forma nativa e interoperável em qualquer ambiente de desenvolvimento assistido por IA, sem dependência de plataformas proprietárias.

---

## 🌐 Suporte Oficial a Múltiplos Harnesses

Os agentes deste ecossistema são compaginados para interoperar nativamente com:

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                ECOSSISTEMA DE HARNESSES SUPORTADOS                      │
├───────────────────────────────┬─────────────────────────────────┬───────────────────────┤
│ 🖥️ CLI Coding Assistants      │ 💻 IDEs & Editores              │ 🐍 Frameworks de IA   │
├───────────────────────────────┼─────────────────────────────────┼───────────────────────┤
│ • Claude Code (Anthropic)     │ • Cursor IDE (.cursorrules)     │ • LangChain           │
│ • OpenCode                    │ • Windsurf / Codeium            │ • AutoGen (Microsoft) │
│ • OpenAI Codex / GPT-4o CLI   │ • VS Code (GitHub Copilot)      │ • CrewAI              │
│ • Google Antigravity (ADK 2.0)│ • JetBrains AI Assistant        │ • Z.ai Orchestrator   │
│ • Aider / Goose CLI           │ • Zed Editor                    │ • LangGraph           │
└───────────────────────────────┴─────────────────────────────────┴───────────────────────┘
```

---

## 📁 Anatomia da Especificação de cada Agente

Cada agente sob `agents/<nome>/` possui três representações sincronizadas para máxima compatibilidade:

```text
agents/<nome-do-agente>/
├── AGENT.md        # 📄 Canônico Markdown + YAML Frontmatter (Claude Code, OpenCode, Codex, Cursor)
├── agent.yaml      # ⚙️ Declaração estruturada YAML com model: inherit (Antigravity / ADK 2.0)
├── agent.json      # 📦 Manifesto JSON estruturado (APIs REST, LangChain, AutoGen, CrewAI, Z.ai)
└── plugin.json     # 🔌 Metadados de plugin com entrypoint padronizado
```

---

## 🚀 Guia de Utilização por Harness

### 1. 🟣 Claude Code / Claude CLI
Carregue o agente passando o `AGENT.md` diretamente como o prompt de sistema ou referenciando no prompt:
```bash
# Execução direta com prompt de sistema do agente
claude --system-prompt agents/software-architect/AGENT.md

# Ou mencione diretamente durante a sessão interativa:
# "Adote as diretrizes e instruções de @agents/devops-engineer/AGENT.md para criar o pipeline."
```

### 2. 🟢 OpenCode / Goose / Aider
Passe a instrução do agente via flag de contexto ou registre no `.opencode/config.json`:
```bash
# OpenCode CLI
opencode run --system-prompt agents/pentester-agent/AGENT.md

# Aider CLI
aider --read agents/fullstack-developer/AGENT.md
```

### 3. 🔵 OpenAI Codex / GPT-4o / REST APIs
Utilize o `agent.json` ou extraia as instruções do `AGENT.md` via script/API:
```python
import json
from openai import OpenAI

client = OpenAI()
with open("agents/software-architect/agent.json") as f:
    agent_spec = json.load(f)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": agent_spec["instruction"]},
        {"role": "user", "content": "Projete a arquitetura do novo microsserviço de pagamentos."}
    ]
)
```

### 4. 🟡 Google Antigravity / ADK 2.0
O agente é detectado automaticamente pelo sistema de customização ao ler a pasta `agents/`:
- Configurado via `agent.yaml` com `model: inherit` para respeitar a preferência do usuário ou subagente.

### 5. 🟠 Cursor / Windsurf / Copilot Workspace
Adicione o conteúdo do `AGENT.md` às instruções da workspace (`.cursorrules` ou regras customizadas de contexto):
```text
# No .cursorrules ou workspace prompt:
Consulte e siga as diretrizes do agente em agents/software-architect/AGENT.md.
```

### 6. 🔴 Frameworks Multi-Agentes (LangChain, AutoGen, CrewAI, Z.ai)
Instancie o agente dinamicamente lendo o `agent.json`:
```python
from crewai import Agent
import json

with open("agents/qa-testing-specialist/agent.json") as f:
    spec = json.load(f)

qa_agent = Agent(
    role=spec["name"],
    goal=spec["description"],
    backstory=spec["instruction"],
    verbose=True
)
```

---

## 📋 Catálogo Completo dos 27 Agentes Disponíveis


| # | Agente | Markdown (Universal) | YAML (ADK 2.0) | JSON (APIs) | Descrição e Especialidade |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **ai-security-specialist** | [`AGENT.md`](ai-security-specialist/AGENT.md) | [`agent.yaml`](ai-security-specialist/agent.yaml) | [`agent.json`](ai-security-specialist/agent.json) | Agente Especialista em Segurança de Inteligência Artificial, LLMs, Visão Computacional e Voz, cobrindo Red Teaming de IA, Prompt Injection, envenenamento de dados e conformidade OWASP Top 10 for LLM. |
| 2 | **antigravity-agent** | [`AGENT.md`](antigravity-agent/AGENT.md) | [`agent.yaml`](antigravity-agent/agent.yaml) | [`agent.json`](antigravity-agent/agent.json) | Agente Principal de Pair Programming Autônomo e Engenharia do ecossistema Google Antigravity. Especializado em desenvolvimento fim a fim, refatoração, resolução de problemas, execução de comandos e extensibilidade via customizações (Skills, Rules, Plugins, Hooks e MCP). |
| 3 | **cloud-infrastructure-architect** | [`AGENT.md`](cloud-infrastructure-architect/AGENT.md) | [`agent.yaml`](cloud-infrastructure-architect/agent.yaml) | [`agent.json`](cloud-infrastructure-architect/agent.json) | Agente Especialista em Arquitetura e Engenharia Multi-Cloud (AWS, Azure, GCP, OCI), Well-Architected Framework, FinOps e automação IaC segura. |
| 4 | **code-mapping-specialist** | [`AGENT.md`](code-mapping-specialist/AGENT.md) | [`agent.yaml`](code-mapping-specialist/agent.yaml) | [`agent.json`](code-mapping-specialist/agent.json) | Agente Especialista em Mapeamento de Código, Aplicações, Fluxos de Execução, Infraestrutura, Kubernetes, Nuvem e Grafos de Dependência Ponta a Ponta. |
| 5 | **data-engineer-specialist** | [`AGENT.md`](data-engineer-specialist/AGENT.md) | [`agent.yaml`](data-engineer-specialist/agent.yaml) | [`agent.json`](data-engineer-specialist/agent.json) | Especialista em Engenharia de Dados, Data Mesh, Streaming em Tempo Real (Kafka, Pinot, Flink), Governança Federada e Pipelines de Anonimização de Dados. |
| 6 | **dba-specialist** | [`AGENT.md`](dba-specialist/AGENT.md) | [`agent.yaml`](dba-specialist/agent.yaml) | [`agent.json`](dba-specialist/agent.json) | Agente Especialista em Administração de Bancos de Dados (DBA) para SQL e NoSQL, cobrindo modelagem, tunagem de performance (EXPLAIN), alta disponibilidade, replicação e segurança em PostgreSQL, MariaDB, SQLite e MongoDB. |
| 7 | **devops-engineer** | [`AGENT.md`](devops-engineer/AGENT.md) | [`agent.yaml`](devops-engineer/agent.yaml) | [`agent.json`](devops-engineer/agent.json) | Agente de DevOps, Platform Engineering e DevSecOps focado em automação de infraestrutura como código (Terraform, Ansible, Vagrant, Backstage), orquestração de containers (Docker, Podman, CRI-O, Kubernetes), governança do GitHub e pipelines de CI/CD (GitHub Actions) com segurança integrada. |
| 8 | **documenter** | [`AGENT.md`](documenter/AGENT.md) | [`agent.yaml`](documenter/agent.yaml) | [`agent.json`](documenter/agent.json) | Agente especializado em documentação de software e desenhos visuais usando diagramas Mermaid.js. |
| 9 | **embedded-systems-specialist** | [`AGENT.md`](embedded-systems-specialist/AGENT.md) | [`agent.yaml`](embedded-systems-specialist/agent.yaml) | [`agent.json`](embedded-systems-specialist/agent.json) | Especialista em Sistemas Embarcados, RTOS (Zephyr), Linux Embarcado (Yocto Project), Firmware C/C++ e Descrição de Hardware (Verilog/VHDL). |
| 10 | **explore** | [`AGENT.md`](explore/AGENT.md) | [`agent.yaml`](explore/agent.yaml) | [`agent.json`](explore/agent.json) | Subagente Especialista em Exploração Rápida de Codebases, busca de padrões, análise de arquitetura, mapeamento de dependências e entendimento de estruturas de projetos existentes. |
| 11 | **fullstack-developer** | [`AGENT.md`](fullstack-developer/AGENT.md) | [`agent.yaml`](fullstack-developer/agent.yaml) | [`agent.json`](fullstack-developer/agent.json) | Agente de Desenvolvimento Full Stack especialista em criar aplicações web fim a fim, integrando lógica de backend (REST, gRPC), frontend (React, Vue), bancos de dados (DBA) e garantindo código limpo e seguro. |
| 12 | **general** | [`AGENT.md`](general/AGENT.md) | [`agent.yaml`](general/agent.yaml) | [`agent.json`](general/agent.json) | Agente Generalista Multi-Etapas, especializado em orquestração, decomposição de problemas complexos em subtarefas, coordenação de fluxos e integração dinâmica de múltiplas habilidades do repositório. |
| 13 | **hardware-security-specialist** | [`AGENT.md`](hardware-security-specialist/AGENT.md) | [`agent.yaml`](hardware-security-specialist/agent.yaml) | [`agent.json`](hardware-security-specialist/agent.json) | Especialista em Auditoria Física de Hardware, Segurança de Dispositivos IoT, Extração de Firmware, Glitching e Side-Channel Attacks. |
| 14 | **iam-specialist** | [`AGENT.md`](iam-specialist/AGENT.md) | [`agent.yaml`](iam-specialist/agent.yaml) | [`agent.json`](iam-specialist/agent.json) | Agente Especialista em Gestão de Identidades e Controle de Acessos (IAM/PAM), Governança de Identidades, Arquitetura Zero Trust, Entra ID, Power Platform, AWS, Azure, GCP e OCI IAM. |
| 15 | **malware-analyst** | [`AGENT.md`](malware-analyst/AGENT.md) | [`agent.yaml`](malware-analyst/agent.yaml) | [`agent.json`](malware-analyst/agent.json) | Especialista em Análise de Malware, Engenharia Reversa de Binários, Evasão de EDR e Análise Forense de Código Executável em Windows, Linux, Android e macOS. |
| 16 | **moodle-specialist** | [`AGENT.md`](moodle-specialist/AGENT.md) | [`agent.yaml`](moodle-specialist/agent.yaml) | [`agent.json`](moodle-specialist/agent.json) | Agente especialista sênior em Moodle LMS e EdTech. Atua desde a arquitetura de servidores e modelagem de banco de dados (DBA), até o design de temas (UI/UX), desenvolvimento de plugins, integrações (LTI, SCORM, xAPI) e aplicação de metodologias de Andragogia. |
| 17 | **pentester-agent** | [`AGENT.md`](pentester-agent/AGENT.md) | [`agent.yaml`](pentester-agent/agent.yaml) | [`agent.json`](pentester-agent/agent.json) | Agente Pentester Ético especializado em auditorias ofensivas (OWASP WSTG, API Security, Cloud e Red Team Scripting) usando utilitários CLI e scripts customizados. |
| 18 | **project-reviewer** | [`AGENT.md`](project-reviewer/AGENT.md) | [`agent.yaml`](project-reviewer/agent.yaml) | [`agent.json`](project-reviewer/agent.json) | Agente de Revisão de Projetos especializado na auditoria de regras de negócio, distribuição técnica (Banco, Backend, Frontend) e boas práticas de arquitetura e segurança. |
| 19 | **qa-testing-specialist** | [`AGENT.md`](qa-testing-specialist/AGENT.md) | [`agent.yaml`](qa-testing-specialist/agent.yaml) | [`agent.json`](qa-testing-specialist/agent.json) | Agente Especialista em Garantia de Qualidade (QA) e Automação de Testes Multi-Framework (Pytest, Unittest, Nose2, Ward, Jest, Mocha, Criterion, Playwright). |
| 20 | **quantum-computing-specialist** | [`AGENT.md`](quantum-computing-specialist/AGENT.md) | [`agent.yaml`](quantum-computing-specialist/agent.yaml) | [`agent.json`](quantum-computing-specialist/agent.json) | Especialista em Computação Quântica, Desenvolvimento de Circuitos Quânticos (Qiskit, Cirq), Algoritmos Quânticos (Shor, Grover, VQE) e Criptografia Pós-Quântica (PQC). |
| 21 | **researcher** | [`AGENT.md`](researcher/AGENT.md) | [`agent.yaml`](researcher/agent.yaml) | [`agent.json`](researcher/agent.json) | Subagente Especialista em Pesquisa, Varredura de Codebase, Análise de Documentação e Busca Externa com ferramentas de leitura estrita. Ideal para investigações abrangentes sem sobrecarregar a janela de contexto principal. |
| 22 | **reverse-engineer-agent** | [`AGENT.md`](reverse-engineer-agent/AGENT.md) | [`agent.yaml`](reverse-engineer-agent/agent.yaml) | [`agent.json`](reverse-engineer-agent/agent.json) | Agente de Engenharia Reversa e Análise de Baixo Nível, especializado na depuração de processos, análise de binários, manipulação de memória (Cheat Engine) e segurança de código contra exploração. |
| 23 | **security-specialist** | [`AGENT.md`](security-specialist/AGENT.md) | [`agent.yaml`](security-specialist/agent.yaml) | [`agent.json`](security-specialist/agent.json) | Agente Especialista em Segurança da Informação, cobrindo práticas de AppSec (SAST), DevSecOps (SCA com Snyk CLI e Snyk MCP), conformidade regulatória de privacidade (LGPD/GDPR) e modelagem de ameaças. |
| 24 | **self** | [`AGENT.md`](self/AGENT.md) | [`agent.yaml`](self/agent.yaml) | [`agent.json`](self/agent.json) | Subagente de Clonagem e Execução Paralela / Isolamento de Contexto (Self Subagent). Herda integralmente a configuração, ferramentas (leitura, escrita, execução de comandos e orquestração) e modelo do agente principal para executar subtarefas complexas em conversas independentes. |
| 25 | **skill-creator** | [`AGENT.md`](skill-creator/AGENT.md) | [`agent.yaml`](skill-creator/agent.yaml) | [`agent.json`](skill-creator/agent.json) | Agente especialista sênior em Arquitetura, Criação, Aprimoramento e Catalogação de Skills para assistentes de IA. Domina a conversão de livros/documentos PDF em Markdown estruturado, elaboração de SKILL.md de padrão de produção, interconexão de habilidades e governança do repositório. |
| 26 | **software-architect** | [`AGENT.md`](software-architect/AGENT.md) | [`agent.yaml`](software-architect/agent.yaml) | [`agent.json`](software-architect/agent.json) | Agente de Arquitetura de Software que aplica DDD, SOLID e orquestração de Design Patterns para guiar o design de projetos. |
| 27 | **telecom-voice-specialist** | [`AGENT.md`](telecom-voice-specialist/AGENT.md) | [`agent.yaml`](telecom-voice-specialist/agent.yaml) | [`agent.json`](telecom-voice-specialist/agent.json) | Agente Especialista em Engenharia de Voz, Telefonia e Comunicações em Tempo Real (VoIP, SIP, SBC, PSTN, WebRTC, Codecs G.711/G.729/Opus, Kamailio/FreeSWITCH, QoS e STIR/SHAKEN). |
