# 🤖 Agentes Especializados Universais (Multi-Harness Architecture)

Este repositório adota a **Arquitetura Multi-Harness**, garantindo que todos os **54 Agentes Especializados** sejam organizados em **7 categorias funcionais** e utilizáveis de forma nativa e interoperável em qualquer ambiente de desenvolvimento assistido por IA, sem dependência de plataformas proprietárias.

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

Cada agente sob `agents/<categoria>/<nome>/` possui representações sincronizadas para máxima compatibilidade:

```text
agents/<categoria>/<nome-do-agente>/
├── AGENT.md        # 📄 Canônico Markdown + YAML Frontmatter, sem linha model por padrão (Claude Code, OpenCode, Codex, Cursor)
├── agent.yaml      # ⚙️ Declaração estruturada YAML (Antigravity / ADK 2.0) — pode usar model: inherit
├── agent.json      # 📦 Manifesto JSON estruturado, sem campo model por padrão (APIs REST, LangChain, AutoGen, CrewAI, Z.ai)
└── plugin.json     # 🔌 Metadados de plugin com entrypoint padronizado
```

---

## 🚀 Guia de Utilização por Harness

### 1. 🟣 Claude Code / Claude CLI
Carregue o agente passando o `AGENT.md` diretamente como o prompt de sistema ou referenciando no prompt:
```bash
# Execução direta com prompt de sistema do agente
claude --system-prompt agents/software-engineering/software-architect/AGENT.md

# Ou mencione diretamente durante a sessão interativa:
# "Adote as diretrizes e instruções de @agents/data-cloud-devops/devops-engineer/AGENT.md para criar o pipeline."
```

### 2. 🟢 OpenCode / Goose / Aider
Passe a instrução do agente via flag de contexto ou registre no `.opencode/config.json`:
```bash
# OpenCode CLI
opencode run --system-prompt agents/cybersecurity/pentester-agent/AGENT.md

# Aider CLI
aider --read agents/software-engineering/fullstack-developer/AGENT.md
```

### 3. 🔵 OpenAI Codex / GPT-4o / REST APIs
Utilize o `agent.json` ou extraia as instruções do `AGENT.md` via script/API:
```python
import json
from openai import OpenAI

client = OpenAI()
with open("agents/software-engineering/software-architect/agent.json") as f:
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
O agente é detectado automaticamente pelo sistema de customização ao ler as categorias em `.agents/plugins.json`:
- Configurado via `agent.yaml` com `model: inherit` para respeitar a preferência do usuário ou subagente (suportado apenas neste harness).
- Em `AGENT.md` e `agent.json`, a linha/campo `model` deve ser omitida — ver [AGENTS.md](../AGENTS.md) para as regras de `model` por harness.

### 5. 🟠 Cursor / Windsurf / Copilot Workspace
Adicione o conteúdo do `AGENT.md` às instruções da workspace (`.cursorrules` ou regras customizadas de contexto):
```text
# No .cursorrules ou workspace prompt:
Consulte e siga as diretrizes do agente em agents/software-engineering/software-architect/AGENT.md.
```

### 6. 🔴 Frameworks Multi-Agentes (LangChain, AutoGen, CrewAI, Z.ai)
Instancie o agente dinamicamente lendo o `agent.json`:
```python
from crewai import Agent
import json

with open("agents/software-engineering/qa-testing-specialist/agent.json") as f:
    spec = json.load(f)

qa_agent = Agent(
    role=spec["name"],
    goal=spec["description"],
    backstory=spec["instruction"],
    verbose=True
)
```

---

## 📋 Tabela Mestra dos 53 Agentes Especializados Universais

| # | Categoria | Agente | Markdown (Universal) | YAML | JSON (APIs) | Descrição e Especialidade |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `core-orchestration` | **antigravity-agent** | [`AGENT.md`](core-orchestration/antigravity-agent/AGENT.md) | [`agent.yaml`](core-orchestration/antigravity-agent/agent.yaml) | [`agent.json`](core-orchestration/antigravity-agent/agent.json) | Agente Principal de Pair Programming Autônomo e Engenharia do ecossistema Google Antigravity. Especializado em desenvolvimento fim a fim, refatoração, resolução de problemas, execução de comandos e extensibilidade via customizações (Skills, Rules, Plugins, Hooks e MCP). |
| 2 | `core-orchestration` | **general** | [`AGENT.md`](core-orchestration/general/AGENT.md) | [`agent.yaml`](core-orchestration/general/agent.yaml) | [`agent.json`](core-orchestration/general/agent.json) | Agente Generalista Multi-Etapas, especializado em orquestração, decomposição de problemas complexos em subtarefas, coordenação de fluxos e integração dinâmica de múltiplas habilidades do repositório. |
| 3 | `core-orchestration` | **multi-agent-orchestrator** | [`AGENT.md`](core-orchestration/multi-agent-orchestrator/AGENT.md) | [`agent.yaml`](core-orchestration/multi-agent-orchestrator/agent.yaml) | [`agent.json`](core-orchestration/multi-agent-orchestrator/agent.json) | Agente Orquestrador e Supervisor de Sistemas Multi-Agente. Especializado em decomposição de problemas, ancoragem de objetivos iniciais, monitoramento contínuo de subagentes, detecção de desvio de escopo (Agent Drift / Role Drift), correção proativa em tempo real e aplicação de kill-switch/terminação segura. |
| 4 | `core-orchestration` | **self** | [`AGENT.md`](core-orchestration/self/AGENT.md) | [`agent.yaml`](core-orchestration/self/agent.yaml) | [`agent.json`](core-orchestration/self/agent.json) | Subagente de Auto-Clonagem, Delegação e Execução Concorrente / Isolamento de Contexto (Self Subagent / Fork Delegate). Herda e replica integralmente o modelo, ferramentas de workspace (leitura, edição, terminal, busca) e diretrizes do agente principal/chamador para executar subtarefas complexas em conversas ou subprocessos independentes em qualquer harness ou framework de IA. |
| 5 | `research-discovery` | **code-mapping-specialist** | [`AGENT.md`](research-discovery/code-mapping-specialist/AGENT.md) | [`agent.yaml`](research-discovery/code-mapping-specialist/agent.yaml) | [`agent.json`](research-discovery/code-mapping-specialist/agent.json) | Agente Especialista em Mapeamento de Código, Aplicações, Fluxos de Execução, Infraestrutura, Kubernetes, Nuvem e Grafos de Dependência Ponta a Ponta. |
| 6 | `research-discovery` | **code-researcher** | [`AGENT.md`](research-discovery/code-researcher/AGENT.md) | [`agent.yaml`](research-discovery/code-researcher/agent.yaml) | [`agent.json`](research-discovery/code-researcher/agent.json) | Subagente Especialista em Pesquisa em Base de Código, Varredura de Repositórios, Análise de Árvore Sintática Abstrata (AST), Símbolos, Dependências e Arquitetura de Software com ferramentas de leitura estrita. |
| 7 | `research-discovery` | **explore** | [`AGENT.md`](research-discovery/explore/AGENT.md) | [`agent.yaml`](research-discovery/explore/agent.yaml) | [`agent.json`](research-discovery/explore/agent.json) | Subagente Especialista em Exploração Rápida de Codebases, busca de padrões, análise de arquitetura, mapeamento de dependências e entendimento de estruturas de projetos existentes. |
| 8 | `research-discovery` | **scientific-researcher** | [`AGENT.md`](research-discovery/scientific-researcher/AGENT.md) | [`agent.yaml`](research-discovery/scientific-researcher/agent.yaml) | [`agent.json`](research-discovery/scientific-researcher/agent.json) | Agente Especialista em Pesquisa Científica e Revisão Sistemática de Literatura. Domina os protocolos PRISMA 2020, framework PICO/PECO, diretrizes PRESS, busca em bases indexadas (PubMed, arXiv, IEEE Xplore, Semantic Scholar, Scopus, SciELO) e análise de redes de citação. |
| 9 | `research-discovery` | **web-researcher** | [`AGENT.md`](research-discovery/web-researcher/AGENT.md) | [`agent.yaml`](research-discovery/web-researcher/agent.yaml) | [`agent.json`](research-discovery/web-researcher/agent.json) | Agente Especialista em Pesquisa na Web e Motores de Busca (Google, DuckDuckGo, Bing, SearXNG, Yahoo). Domina operadores booleanos avançados, Google Dorks, filtros de domínio, tipos de arquivos, OSINT defensivo, triangulação de dados e verificação factual de fontes. |
| 10 | `software-engineering` | **code-optimizer** | [`AGENT.md`](software-engineering/code-optimizer/AGENT.md) | [`agent.yaml`](software-engineering/code-optimizer/agent.yaml) | [`agent.json`](software-engineering/code-optimizer/agent.json) | Agente especialista sênior em Otimização de Código e Arquitetura, cobrindo profiling e eliminação de gargalos (CPU, memória, I/O, latência, contenção), refatoração econômica Tidy First, otimização de persistência (N+1, batching, cache), concorrência e paralelismo (Java Virtual Threads, C# async/await, Python multiprocessing/asyncio/Dask/Ray) e arquitetura de sistemas data-intensive. |
| 11 | `software-engineering` | **documenter** | [`AGENT.md`](software-engineering/documenter/AGENT.md) | [`agent.yaml`](software-engineering/documenter/agent.yaml) | [`agent.json`](software-engineering/documenter/agent.json) | Agente especialista sênior em Engenharia de Documentação Técnica, Prosa Humana Anti-IA (Anti-AI Writing Manifesto), Arquitetura Diátaxis e Modelagem Visual de Diagramas com Mermaid.js. |
| 12 | `software-engineering` | **frontend-developer** | [`AGENT.md`](software-engineering/frontend-developer/AGENT.md) | [`agent.yaml`](software-engineering/frontend-developer/agent.yaml) | [`agent.json`](software-engineering/frontend-developer/agent.json) | Agente especialista sênior em Engenharia de Frontend e Design Engineering, dominando des-templatização de Tailwind e shadcn/ui, texturas táteis (SVG noise), física de molas naturais (Framer Motion), otimização de Core Web Vitals e acessibilidade estrita WCAG 2.2. |
| 13 | `software-engineering` | **fullstack-developer** | [`AGENT.md`](software-engineering/fullstack-developer/AGENT.md) | [`agent.yaml`](software-engineering/fullstack-developer/agent.yaml) | [`agent.json`](software-engineering/fullstack-developer/agent.json) | Agente de Desenvolvimento Full Stack especialista em criar aplicações web fim a fim, integrando lógica de backend (REST, gRPC), frontend (React, Vue), bancos de dados (DBA) e garantindo código limpo e seguro. |
| 14 | `software-engineering` | **java-enterprise-architect** | [`AGENT.md`](software-engineering/java-enterprise-architect/AGENT.md) | [`agent.yaml`](software-engineering/java-enterprise-architect/agent.yaml) | [`agent.json`](software-engineering/java-enterprise-architect/agent.json) | Agente Especialista em Arquitetura e Engenharia Java Corporativa (Java 21/25 LTS, Spring Boot 3.x, Quarkus Cloud-Native, MicroProfile/Jakarta EE, Virtual Threads Project Loom, JPA/Hibernate e Arquitetura BCE). |
| 15 | `software-engineering` | **project-reviewer** | [`AGENT.md`](software-engineering/project-reviewer/AGENT.md) | [`agent.yaml`](software-engineering/project-reviewer/agent.yaml) | [`agent.json`](software-engineering/project-reviewer/agent.json) | Agente de Revisão de Projetos especializado na auditoria de regras de negócio, distribuição técnica (Banco, Backend, Frontend) e boas práticas de arquitetura e segurança. |
| 16 | `software-engineering` | **qa-testing-specialist** | [`AGENT.md`](software-engineering/qa-testing-specialist/AGENT.md) | [`agent.yaml`](software-engineering/qa-testing-specialist/agent.yaml) | [`agent.json`](software-engineering/qa-testing-specialist/agent.json) | Agente Especialista em Garantia de Qualidade (QA), Automação de Testes Multi-Framework, Testes de Mutação (Mutation Testing), Fuzzing e Auditoria de Conformidade de Requisitos. Domina a injeção sistemática de falhas, eliminação de test gaps e validação rigorosa de critérios de aceitação. |
| 17 | `software-engineering` | **software-architect** | [`AGENT.md`](software-engineering/software-architect/AGENT.md) | [`agent.yaml`](software-engineering/software-architect/agent.yaml) | [`agent.json`](software-engineering/software-architect/agent.json) | Agente de Arquitetura de Software que aplica DDD, SOLID e orquestração de Design Patterns para guiar o design de projetos. |
| 18 | `software-engineering` | **software-engineer** | [`AGENT.md`](software-engineering/software-engineer/AGENT.md) | [`agent.yaml`](software-engineering/software-engineer/agent.yaml) | [`agent.json`](software-engineering/software-engineer/agent.json) | Agente especialista sênior em Engenharia de Software, cobrindo engenharia de requisitos formais, arquiteturas modulares e distribuídas (Clean Architecture, Microsserviços, Hexagonal), DevSecOps, testes automatizados e métricas de qualidade. |
| 19 | `software-engineering` | **ui-ux-designer** | [`AGENT.md`](software-engineering/ui-ux-designer/AGENT.md) | [`agent.yaml`](software-engineering/ui-ux-designer/agent.yaml) | [`agent.json`](software-engineering/ui-ux-designer/agent.json) | Agente especialista sênior em Design de Interface (UI), Experiência do Usuário (UX) e Direção de Arte, dominando 24 estilos de design de páginas, o Anti-AI Slop Manifesto, tipografia de alto contraste, arquitetura de Design Systems e acessibilidade WCAG 2.2. |
| 20 | `software-engineering` | **vcs-repository-specialist** | [`AGENT.md`](software-engineering/vcs-repository-specialist/AGENT.md) | [`agent.yaml`](software-engineering/vcs-repository-specialist/agent.yaml) | [`agent.json`](software-engineering/vcs-repository-specialist/agent.json) | Agente especialista sênior em Sistemas de Controle de Versão (VCS) e Gestão Avançada de Repositórios, cobrindo Git de baixo nível (DAG, reflog, worktrees, sparse-checkout, LFS, filter-repo), Subversion/SVN (FSFS, trunk/branches/tags, mergeinfo, svnadmin, hooks), Mercurial (Hg), migrações completas de VCS legados e governança de branching. |
| 21 | `data-cloud-devops` | **cloud-infrastructure-architect** | [`AGENT.md`](data-cloud-devops/cloud-infrastructure-architect/AGENT.md) | [`agent.yaml`](data-cloud-devops/cloud-infrastructure-architect/agent.yaml) | [`agent.json`](data-cloud-devops/cloud-infrastructure-architect/agent.json) | Agente Especialista em Arquitetura e Engenharia Multi-Cloud (AWS, Azure, GCP, OCI), Well-Architected Framework, FinOps e automação IaC segura. |
| 22 | `data-cloud-devops` | **data-ai-engineer** | [`AGENT.md`](data-cloud-devops/data-ai-engineer/AGENT.md) | [`agent.yaml`](data-cloud-devops/data-ai-engineer/agent.yaml) | [`agent.json`](data-cloud-devops/data-ai-engineer/agent.json) | Agente especialista sênior em Engenharia de Dados, Big Data e Inteligência Artificial, cobrindo pipelines distribuídos (Spark, Airflow), streaming em tempo real (Kafka, Flink, Pinot), arquiteturas Data Mesh, Deep Learning, MLOps e Engenharia de LLMs/RAG. |
| 23 | `data-cloud-devops` | **data-engineer-specialist** | [`AGENT.md`](data-cloud-devops/data-engineer-specialist/AGENT.md) | [`agent.yaml`](data-cloud-devops/data-engineer-specialist/agent.yaml) | [`agent.json`](data-cloud-devops/data-engineer-specialist/agent.json) | Especialista em Engenharia de Dados, Data Mesh, Streaming em Tempo Real (Kafka, Pinot, Flink), Governança Federada e Pipelines de Anonimização de Dados. |
| 24 | `data-cloud-devops` | **dba-specialist** | [`AGENT.md`](data-cloud-devops/dba-specialist/AGENT.md) | [`agent.yaml`](data-cloud-devops/dba-specialist/agent.yaml) | [`agent.json`](data-cloud-devops/dba-specialist/agent.json) | Agente Especialista em Administração de Bancos de Dados (DBA) para SQL e NoSQL, cobrindo modelagem, tunagem de performance (EXPLAIN), alta disponibilidade, replicação e segurança em PostgreSQL, MariaDB, SQLite e MongoDB. |
| 25 | `data-cloud-devops` | **devops-engineer** | [`AGENT.md`](data-cloud-devops/devops-engineer/AGENT.md) | [`agent.yaml`](data-cloud-devops/devops-engineer/agent.yaml) | [`agent.json`](data-cloud-devops/devops-engineer/agent.json) | Agente de DevOps, Platform Engineering e DevSecOps focado em automação de infraestrutura como código (Terraform, Ansible, Vagrant, Backstage), orquestração de containers (Docker, Podman, CRI-O, Kubernetes), governança do GitHub e pipelines de CI/CD (GitHub Actions) com segurança integrada (Opengrep SAST, OWASP ZAP DAST e OWASP Dependency-Check SCA). |
| 26 | `cybersecurity` | **ai-security-specialist** | [`AGENT.md`](cybersecurity/ai-security-specialist/AGENT.md) | [`agent.yaml`](cybersecurity/ai-security-specialist/agent.yaml) | [`agent.json`](cybersecurity/ai-security-specialist/agent.json) | Agente Especialista em Segurança de Inteligência Artificial, LLMs, Visão Computacional e Voz, cobrindo Red Teaming de IA, Prompt Injection, envenenamento de dados e conformidade OWASP Top 10 for LLM. |
| 27 | `cybersecurity` | **hardware-security-specialist** | [`AGENT.md`](cybersecurity/hardware-security-specialist/AGENT.md) | [`agent.yaml`](cybersecurity/hardware-security-specialist/agent.yaml) | [`agent.json`](cybersecurity/hardware-security-specialist/agent.json) | Especialista em Auditoria Física de Hardware, Segurança de Dispositivos IoT, Extração de Firmware, Glitching e Side-Channel Attacks. |
| 28 | `cybersecurity` | **iam-specialist** | [`AGENT.md`](cybersecurity/iam-specialist/AGENT.md) | [`agent.yaml`](cybersecurity/iam-specialist/agent.yaml) | [`agent.json`](cybersecurity/iam-specialist/agent.json) | Agente Especialista em Gestão de Identidades e Controle de Acessos (IAM/PAM), Governança de Identidades, Arquitetura Zero Trust, Entra ID, Power Platform, AWS, Azure, GCP e OCI IAM. |
| 29 | `cybersecurity` | **malware-analyst** | [`AGENT.md`](cybersecurity/malware-analyst/AGENT.md) | [`agent.yaml`](cybersecurity/malware-analyst/agent.yaml) | [`agent.json`](cybersecurity/malware-analyst/agent.json) | Especialista em Análise de Malware, Engenharia Reversa de Binários, Evasão de EDR e Análise Forense de Código Executável em Windows, Linux, Android e macOS. |
| 30 | `cybersecurity` | **pentester-agent** | [`AGENT.md`](cybersecurity/pentester-agent/AGENT.md) | [`agent.yaml`](cybersecurity/pentester-agent/agent.yaml) | [`agent.json`](cybersecurity/pentester-agent/agent.json) | Agente Pentester Ético especializado em auditorias ofensivas (OWASP WSTG, DAST com OWASP ZAP, API Security, Cloud, LLMs e Red Team Scripting) usando utilitários CLI e scripts customizados. |
| 31 | `cybersecurity` | **reverse-engineer-agent** | [`AGENT.md`](cybersecurity/reverse-engineer-agent/AGENT.md) | [`agent.yaml`](cybersecurity/reverse-engineer-agent/agent.yaml) | [`agent.json`](cybersecurity/reverse-engineer-agent/agent.json) | Agente de Engenharia Reversa e Análise de Baixo Nível, especializado na depuração de processos, análise de binários, manipulação de memória (Cheat Engine) e segurança de código contra exploração. |
| 32 | `cybersecurity` | **security-specialist** | [`AGENT.md`](cybersecurity/security-specialist/AGENT.md) | [`agent.yaml`](cybersecurity/security-specialist/agent.yaml) | [`agent.json`](cybersecurity/security-specialist/agent.json) | Agente Especialista em Segurança da Informação, cobrindo práticas completas de AppSec (SAST, DAST, IAST, RASP, SCA), DevSecOps, conformidade regulatória de privacidade (LGPD/GDPR) e modelagem de ameaças. |
| 33 | `academic-sciences` | **biomedical-engineer** | [`AGENT.md`](academic-sciences/biomedical-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/biomedical-engineer/agent.yaml) | [`agent.json`](academic-sciences/biomedical-engineer/agent.json) | Agente especialista sênior em Engenharia Biomédica, cobrindo processamento de biossinais (ECG, EEG, EMG), instrumentação médica com amplificadores de isolamento (INA), física de imagens médicas (CT, MRI, Ultrassom) e interoperabilidade com DICOM e HL7/FHIR. |
| 34 | `academic-sciences` | **biotechnologist** | [`AGENT.md`](academic-sciences/biotechnologist/AGENT.md) | [`agent.yaml`](academic-sciences/biotechnologist/agent.yaml) | [`agent.json`](academic-sciences/biotechnologist/agent.json) | Agente especialista sênior em Biotecnologia, Engenharia de Bioprocessos e Biomanufatura, cobrindo cultivo celular, biorreatores (STR, airlift, single-use), upstream e downstream processing, enzimologia, tecnologia do DNA recombinante, imunobiológicos, biossegurança (CTNBio/ANVISA) e conformidade BPL. |
| 35 | `academic-sciences` | **chemical-engineer** | [`AGENT.md`](academic-sciences/chemical-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/chemical-engineer/agent.yaml) | [`agent.json`](academic-sciences/chemical-engineer/agent.json) | Agente especialista sênior em Engenharia Química, Síntese e Processos Industriais, cobrindo balanço de massa e energia, cinética química, dimensionamento de reatores (CSTR, PFR, PBR), síntese orgânica/inorgânica, análise instrumental (HPLC/GC/RMN), termodinâmica de soluções e fenômenos de transporte. |
| 36 | `academic-sciences` | **civil-engineer** | [`AGENT.md`](academic-sciences/civil-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/civil-engineer/agent.yaml) | [`agent.json`](academic-sciences/civil-engineer/agent.json) | Agente especialista sênior em Engenharia Civil e Estrutural, cobrindo cálculo estrutural, resistência dos materiais, mecânica dos solos e geotecnia (Terzaghi, Mohr-Coulomb), fundações e dimensionamento de elementos estruturais. |
| 37 | `academic-sciences` | **computer-engineer** | [`AGENT.md`](academic-sciences/computer-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/computer-engineer/agent.yaml) | [`agent.json`](academic-sciences/computer-engineer/agent.json) | Agente especialista sênior em Engenharia de Computação, cobrindo arquitetura de microprocessadores (ARM/RISC-V), projeto de circuitos integrados VLSI/CMOS, síntese lógica em VHDL/Verilog, Linux Embarcado, RTOS e análise de circuitos eletrônicos. |
| 38 | `academic-sciences` | **computer-scientist** | [`AGENT.md`](academic-sciences/computer-scientist/AGENT.md) | [`agent.yaml`](academic-sciences/computer-scientist/agent.yaml) | [`agent.json`](academic-sciences/computer-scientist/agent.json) | Agente especialista sênior em Ciência da Computação Teórica e Algoritmos Avançados, cobrindo análise assintótica rigorosa (CLRS), estruturas de dados balanceadas, Teoria da Computação e Autômatos (Sipser), Engenharia de Compiladores (Dragon Book) e Computação Gráfica. |
| 39 | `academic-sciences` | **electrical-power-engineer** | [`AGENT.md`](academic-sciences/electrical-power-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/electrical-power-engineer/agent.yaml) | [`agent.json`](academic-sciences/electrical-power-engineer/agent.json) | Agente especialista sênior em Sistemas Elétricos de Potência (SEP), Redes Elétricas Inteligentes (Smart Grids), Geração, Transmissão e Distribuição, cobrindo fluxo de carga, curto-circuito, proteção digital IEC 61850, máquinas elétricas, transformadores, eletrônica de potência (SVPWM, inversores SiC/GaN) e conformidade NBR 5410/14039. |
| 40 | `academic-sciences` | **geoscientist** | [`AGENT.md`](academic-sciences/geoscientist/AGENT.md) | [`agent.yaml`](academic-sciences/geoscientist/agent.yaml) | [`agent.json`](academic-sciences/geoscientist/agent.json) | Agente especialista sênior em Geociências e Sensoriamento Remoto, cobrindo geologia estrutural, geofísica, cartografia digital, geoprocessamento com GIS/QGIS e espectrometria de imagens de satélite multiespectral. |
| 41 | `academic-sciences` | **mathematician** | [`AGENT.md`](academic-sciences/mathematician/AGENT.md) | [`agent.yaml`](academic-sciences/mathematician/agent.yaml) | [`agent.json`](academic-sciences/mathematician/agent.json) | Agente especialista sênior em Matemática Pura e Aplicada, cobrindo Cálculo Avançado (I a IV), Análise Real e Complexa, Álgebra Abstrata, Álgebra Linear Avançada, Equações Diferenciais Ordinárias e Parciais (EDO/EDP), Métodos Numéricos, Geometria Diferencial e Probabilidade Axiomática. |
| 42 | `academic-sciences` | **mechanical-engineer** | [`AGENT.md`](academic-sciences/mechanical-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/mechanical-engineer/agent.yaml) | [`agent.json`](academic-sciences/mechanical-engineer/agent.json) | Agente especialista sênior em Engenharia Mecânica, cobrindo mecânica dos sólidos, resistência dos materiais (Von Mises, Mohr), mecânica dos fluidos e CFD (Navier-Stokes), transferência de calor e dinâmica de sistemas mecânicos. |
| 43 | `academic-sciences` | **mechatronics-engineer** | [`AGENT.md`](academic-sciences/mechatronics-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/mechatronics-engineer/agent.yaml) | [`agent.json`](academic-sciences/mechatronics-engineer/agent.json) | Agente especialista sênior em Engenharia Mecatrônica, Robótica Industrial/Móvel (ROS 2), Teoria de Controle Clássico e Moderno (Espaço de Estados, PID, LQR, Kalman), Controladores Lógicos Programáveis (CLPs IEC 61131-3) e Sistemas SCADA. |
| 44 | `academic-sciences` | **physical-engineer** | [`AGENT.md`](academic-sciences/physical-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/physical-engineer/agent.yaml) | [`agent.json`](academic-sciences/physical-engineer/agent.json) | Agente especialista sênior em Engenharia Física e Nanotecnologia, cobrindo física do estado sólido, semicondutores, processos de microfabricação em sala limpa, síntese de nanomateriais de carbono (grafeno, nanotubos), pontos quânticos e sensores quânticos. |
| 45 | `academic-sciences` | **physicist** | [`AGENT.md`](academic-sciences/physicist/AGENT.md) | [`agent.yaml`](academic-sciences/physicist/agent.yaml) | [`agent.json`](academic-sciences/physicist/agent.json) | Agente especialista sênior em Física Teórica e Aplicada, cobrindo Mecânica Clássica Avançada (Lagrangeana e Hamiltoniana), Eletromagnetismo de Maxwell, Termodinâmica e Mecânica Estatística, Relatividade Especial e Geral, e Mecânica Quântica da Matéria Condensada. |
| 46 | `academic-sciences` | **quantum-computing-specialist** | [`AGENT.md`](academic-sciences/quantum-computing-specialist/AGENT.md) | [`agent.yaml`](academic-sciences/quantum-computing-specialist/agent.yaml) | [`agent.json`](academic-sciences/quantum-computing-specialist/agent.json) | Especialista em Computação Quântica, Desenvolvimento de Circuitos Quânticos (Qiskit, Cirq), Algoritmos Quânticos (Shor, Grover, VQE) e Criptografia Pós-Quântica (PQC). |
| 47 | `academic-sciences` | **telecom-engineer** | [`AGENT.md`](academic-sciences/telecom-engineer/AGENT.md) | [`agent.yaml`](academic-sciences/telecom-engineer/agent.yaml) | [`agent.json`](academic-sciences/telecom-engineer/agent.json) | Agente especialista sênior em Engenharia de Telecomunicações, cobrindo teoria da informação de Shannon, modulações digitais avançadas (QAM, OFDM), propagação em fibras ópticas (WDM/DWDM), redes celulares 5G/6G, comunicações por satélite e Radiofrequência. |
| 48 | `academic-sciences` | **telecom-voice-specialist** | [`AGENT.md`](academic-sciences/telecom-voice-specialist/AGENT.md) | [`agent.yaml`](academic-sciences/telecom-voice-specialist/agent.yaml) | [`agent.json`](academic-sciences/telecom-voice-specialist/agent.json) | Agente Especialista em Engenharia de Voz, Telefonia e Comunicações em Tempo Real (VoIP, SIP, SBC, PSTN, WebRTC, Codecs G.711/G.729/Opus, Kamailio/FreeSWITCH, QoS e STIR/SHAKEN). |
| 49 | `specialized-domains` | **career-coach-job-hunter** | [`AGENT.md`](specialized-domains/career-coach-job-hunter/AGENT.md) | [`agent.yaml`](specialized-domains/career-coach-job-hunter/agent.yaml) | [`agent.json`](specialized-domains/career-coach-job-hunter/agent.json) | Agente Especialista em Carreira, Mineração de Vagas, Revisão e Otimização de Currículos para ATS e Aprimoramento de Perfis Profissionais (LinkedIn, Upwork, GitHub). Domina algoritmos de parsing de ATS, fórmulas de impacto XYZ, Google Dorks para busca de empregos e estratégias de propostas para freelancers. |
| 50 | `specialized-domains` | **embedded-systems-specialist** | [`AGENT.md`](specialized-domains/embedded-systems-specialist/AGENT.md) | [`agent.yaml`](specialized-domains/embedded-systems-specialist/agent.yaml) | [`agent.json`](specialized-domains/embedded-systems-specialist/agent.json) | Especialista em Sistemas Embarcados, RTOS (Zephyr), Linux Embarcado (Yocto Project), Firmware C/C++ e Descrição de Hardware (Verilog/VHDL). |
| 51 | `specialized-domains` | **information-systems-specialist** | [`AGENT.md`](specialized-domains/information-systems-specialist/AGENT.md) | [`agent.yaml`](specialized-domains/information-systems-specialist/agent.yaml) | [`agent.json`](specialized-domains/information-systems-specialist/agent.json) | Agente especialista sênior em Sistemas de Informação Corporativos, cobrindo modelagem de processos BPMN 2.0, sistemas ERP/CRM, governança de serviços de TI (ITIL 4, COBIT 2019), Business Intelligence e auditoria de sistemas. |
| 52 | `specialized-domains` | **linguistic-specialist** | [`AGENT.md`](specialized-domains/linguistic-specialist/AGENT.md) | [`agent.yaml`](specialized-domains/linguistic-specialist/agent.yaml) | [`agent.json`](specialized-domains/linguistic-specialist/agent.json) | Agente especialista em Revisão Linguística, Precisão Semântica e Qualidade Editorial Multilíngue (PT-BR, EN-US, ES-LATAM). Atua eliminando ambiguidades sintáticas, expurgando vícios de inteligência artificial (Anti-AI Prosa) e assegurando comunicação clara, humana e tecnicamente rigorosa. |
| 53 | `specialized-domains` | **moodle-specialist** | [`AGENT.md`](specialized-domains/moodle-specialist/AGENT.md) | [`agent.yaml`](specialized-domains/moodle-specialist/agent.yaml) | [`agent.json`](specialized-domains/moodle-specialist/agent.json) | Agente especialista sênior em Moodle LMS e EdTech. Atua desde a arquitetura de servidores e modelagem de banco de dados (DBA), até o design de temas (UI/UX), desenvolvimento de plugins, infraestrutura de caching (MUC), integrações (LTI, SCORM, xAPI) e aplicação de metodologias de Andragogia. |
| 54 | `specialized-domains` | **skill-creator** | [`AGENT.md`](specialized-domains/skill-creator/AGENT.md) | [`agent.yaml`](specialized-domains/skill-creator/agent.yaml) | [`agent.json`](specialized-domains/skill-creator/agent.json) | Agente especialista sênior em Arquitetura, Criação, Aprimoramento e Catalogação de Skills para assistentes de IA. Domina a conversão de livros/documentos PDF em Markdown estruturado, elaboração de SKILL.md de padrão de produção, interconexão de habilidades e governança do repositório. |

---

## ⚙️ Diretrizes de Contribuição e Adição de Novos Agentes

Ao criar um novo agente:
1. Posicione a pasta do agente na categoria adequada sob `agents/<categoria>/<nome-do-agente>/`.
2. Garanta a paridade entre `AGENT.md`, `agent.yaml`, `agent.json` e `plugin.json`, utilizando sempre caminhos relativos para skills (`../../../skills/...`).
3. Por padrão, **omite o campo `model`** no `AGENT.md` e `agent.json` (o agente herda o modelo da sessão/config do harness). Siga as regras detalhadas de `model` por harness definidas na seção [🧠 Regras de Modelo](../AGENTS.md#-regras-de-modelo-model-por-harness) do [AGENTS.md](../AGENTS.md).
4. Registre o novo agente em `CATALOGO.md` e `agents/README.md`.
