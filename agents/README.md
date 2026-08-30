# 🤖 Agentes Especializados Universais (Multi-Harness Architecture)

Este repositório adota a **Arquitetura Multi-Harness**, garantindo que todos os **45 Agentes Especializados** sejam utilizáveis de forma nativa e interoperável em qualquer ambiente de desenvolvimento assistido por IA, sem dependência de plataformas proprietárias.

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

## 📋 Tabela Mestra dos 45 Agentes Especializados Universais

| # | Agente | Markdown (Universal) | YAML | JSON (APIs) | Descrição e Especialidade |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **ai-security-specialist** | [`AGENT.md`](ai-security-specialist/AGENT.md) | [`agent.yaml`](ai-security-specialist/agent.yaml) | [`agent.json`](ai-security-specialist/agent.json) | Agente Especialista em Segurança de Inteligência Artificial, LLMs, Visão Computacional e Voz, cobrindo Red Teaming de IA, Prompt Injection, envenenamento de dados e conformidade OWASP Top 10 for LLM. |
| 2 | **antigravity-agent** | [`AGENT.md`](antigravity-agent/AGENT.md) | [`agent.yaml`](antigravity-agent/agent.yaml) | [`agent.json`](antigravity-agent/agent.json) | Agente Principal de Pair Programming Autônomo e Engenharia do ecossistema Google Antigravity. Especializado em desenvolvimento fim a fim, refatoração, resolução de problemas, execução de comandos e extensibilidade via customizações (Skills, Rules, Plugins, Hooks e MCP). |
| 3 | **biomedical-engineer** | [`AGENT.md`](biomedical-engineer/AGENT.md) | [`agent.yaml`](biomedical-engineer/agent.yaml) | [`agent.json`](biomedical-engineer/agent.json) | Agente especialista sênior em Engenharia Biomédica, cobrindo processamento de biossinais (ECG, EEG, EMG), instrumentação médica com amplificadores de isolamento (INA), física de imagens médicas (CT, MRI, Ultrassom) e interoperabilidade com DICOM e HL7/FHIR. |
| 4 | **biotechnologist** | [`AGENT.md`](biotechnologist/AGENT.md) | [`agent.yaml`](biotechnologist/agent.yaml) | [`agent.json`](biotechnologist/agent.json) | Agente especialista sênior em Biotecnologia, Engenharia de Bioprocessos e Biomanufatura, cobrindo cultivo celular, biorreatores (STR, airlift, single-use), upstream e downstream processing, enzimologia, tecnologia do DNA recombinante, imunobiológicos e biossegurança. |
| 5 | **chemical-engineer** | [`AGENT.md`](chemical-engineer/AGENT.md) | [`agent.yaml`](chemical-engineer/agent.yaml) | [`agent.json`](chemical-engineer/agent.json) | Agente especialista sênior em Engenharia Química, Síntese e Processos Industriais, cobrindo balanço de massa e energia, cinética química, dimensionamento de reatores (CSTR, PFR, PBR), síntese orgânica/inorgânica, análise instrumental (HPLC/GC/RMN), termodinâmica de soluções e fenômenos de transporte. |
| 6 | **civil-engineer** | [`AGENT.md`](civil-engineer/AGENT.md) | [`agent.yaml`](civil-engineer/agent.yaml) | [`agent.json`](civil-engineer/agent.json) | Agente especialista sênior em Engenharia Civil e Estrutural, cobrindo cálculo estrutural, resistência dos materiais, mecânica dos solos e geotecnia (Terzaghi, Mohr-Coulomb), fundações e dimensionamento de elementos estruturais. |
| 7 | **cloud-infrastructure-architect** | [`AGENT.md`](cloud-infrastructure-architect/AGENT.md) | [`agent.yaml`](cloud-infrastructure-architect/agent.yaml) | [`agent.json`](cloud-infrastructure-architect/agent.json) | Agente Especialista em Arquitetura e Engenharia Multi-Cloud (AWS, Azure, GCP, OCI), Well-Architected Framework, FinOps e automação IaC segura. |
| 8 | **code-mapping-specialist** | [`AGENT.md`](code-mapping-specialist/AGENT.md) | [`agent.yaml`](code-mapping-specialist/agent.yaml) | [`agent.json`](code-mapping-specialist/agent.json) | Agente Especialista em Mapeamento de Código, Aplicações, Fluxos de Execução, Infraestrutura, Kubernetes, Nuvem e Grafos de Dependência Ponta a Ponta. |
| 9 | **code-optimizer** | [`AGENT.md`](code-optimizer/AGENT.md) | [`agent.yaml`](code-optimizer/agent.yaml) | [`agent.json`](code-optimizer/agent.json) | Agente especialista sênior em Otimização de Código e Arquitetura, cobrindo profiling e eliminação de gargalos (CPU, memória, I/O, latência, contenção), refatoração econômica Tidy First, otimização de persistência (N+1, batching, cache), concorrência e paralelismo (Java Virtual Threads, C# async/await, Python multiprocessing/asyncio/Dask/Ray) e arquitetura de sistemas data-intensive. |
| 10 | **computer-engineer** | [`AGENT.md`](computer-engineer/AGENT.md) | [`agent.yaml`](computer-engineer/agent.yaml) | [`agent.json`](computer-engineer/agent.json) | Agente especialista sênior em Engenharia de Computação, cobrindo arquitetura de microprocessadores (ARM/RISC-V), projeto de circuitos integrados VLSI/CMOS, síntese lógica em VHDL/Verilog, Linux Embarcado, RTOS e análise de circuitos eletrônicos. |
| 11 | **computer-scientist** | [`AGENT.md`](computer-scientist/AGENT.md) | [`agent.yaml`](computer-scientist/agent.yaml) | [`agent.json`](computer-scientist/agent.json) | Agente especialista sênior em Ciência da Computação Teórica e Algoritmos Avançados, cobrindo análise assintótica rigorosa (CLRS), estruturas de dados balanceadas, Teoria da Computação e Autômatos (Sipser), Engenharia de Compiladores (Dragon Book) e Computação Gráfica. |
| 12 | **data-ai-engineer** | [`AGENT.md`](data-ai-engineer/AGENT.md) | [`agent.yaml`](data-ai-engineer/agent.yaml) | [`agent.json`](data-ai-engineer/agent.json) | Agente especialista sênior em Engenharia de Dados, Big Data e Inteligência Artificial, cobrindo pipelines distribuídos (Spark, Airflow), streaming em tempo real (Kafka, Flink, Pinot), arquiteturas Data Mesh, Deep Learning, MLOps e Engenharia de LLMs/RAG. |
| 13 | **data-engineer-specialist** | [`AGENT.md`](data-engineer-specialist/AGENT.md) | [`agent.yaml`](data-engineer-specialist/agent.yaml) | [`agent.json`](data-engineer-specialist/agent.json) | Especialista em Engenharia de Dados, Data Mesh, Streaming em Tempo Real (Kafka, Pinot, Flink), Governança Federada e Pipelines de Anonimização de Dados. |
| 14 | **dba-specialist** | [`AGENT.md`](dba-specialist/AGENT.md) | [`agent.yaml`](dba-specialist/agent.yaml) | [`agent.json`](dba-specialist/agent.json) | Agente Especialista em Administração de Bancos de Dados (DBA) para SQL e NoSQL, cobrindo modelagem, tunagem de performance (EXPLAIN), alta disponibilidade, replicação e segurança em PostgreSQL, MariaDB, SQLite e MongoDB. |
| 15 | **devops-engineer** | [`AGENT.md`](devops-engineer/AGENT.md) | [`agent.yaml`](devops-engineer/agent.yaml) | [`agent.json`](devops-engineer/agent.json) | Agente de DevOps, Platform Engineering e DevSecOps focado em automação de infraestrutura como código (Terraform, Ansible, Vagrant, Backstage), orquestração de containers (Docker, Podman, CRI-O, Kubernetes), governança do GitHub e pipelines de CI/CD (GitHub Actions) com segurança integrada (Opengrep SAST, OWASP ZAP DAST e OWASP Dependency-Check SCA). |
| 16 | **documenter** | [`AGENT.md`](documenter/AGENT.md) | [`agent.yaml`](documenter/agent.yaml) | [`agent.json`](documenter/agent.json) | Agente especializado em documentação de software e desenhos visuais usando diagramas Mermaid.js. |
| 17 | **electrical-power-engineer** | [`AGENT.md`](electrical-power-engineer/AGENT.md) | [`agent.yaml`](electrical-power-engineer/agent.yaml) | [`agent.json`](electrical-power-engineer/agent.json) | Agente especialista sênior em Sistemas Elétricos de Potência (SEP), Redes Inteligentes (Smart Grids), Geração/Transmissão/Distribuição, fluxo de carga, proteção digital IEC 61850, máquinas elétricas, transformadores e eletrônica de potência (SVPWM, GaN/SiC). |
| 18 | **embedded-systems-specialist** | [`AGENT.md`](embedded-systems-specialist/AGENT.md) | [`agent.yaml`](embedded-systems-specialist/agent.yaml) | [`agent.json`](embedded-systems-specialist/agent.json) | Especialista em Sistemas Embarcados, RTOS (Zephyr), Linux Embarcado (Yocto Project), Firmware C/C++ e Descrição de Hardware (Verilog/VHDL). |
| 19 | **explore** | [`AGENT.md`](explore/AGENT.md) | [`agent.yaml`](explore/agent.yaml) | [`agent.json`](explore/agent.json) | Subagente Especialista em Exploração Rápida de Codebases, busca de padrões, análise de arquitetura, mapeamento de dependências e entendimento de estruturas de projetos existentes. |
| 20 | **fullstack-developer** | [`AGENT.md`](fullstack-developer/AGENT.md) | [`agent.yaml`](fullstack-developer/agent.yaml) | [`agent.json`](fullstack-developer/agent.json) | Agente de Desenvolvimento Full Stack especialista em criar aplicações web fim a fim, integrando lógica de backend (REST, gRPC), frontend (React, Vue), bancos de dados (DBA) e garantindo código limpo e seguro. |
| 21 | **general** | [`AGENT.md`](general/AGENT.md) | [`agent.yaml`](general/agent.yaml) | [`agent.json`](general/agent.json) | Agente Generalista Multi-Etapas, especializado em orquestração, decomposição de problemas complexos em subtarefas, coordenação de fluxos e integração dinâmica de múltiplas habilidades do repositório. |
| 22 | **geoscientist** | [`AGENT.md`](geoscientist/AGENT.md) | [`agent.yaml`](geoscientist/agent.yaml) | [`agent.json`](geoscientist/agent.json) | Agente especialista sênior em Geociências, Sensoriamento Remoto e Análise Espacial, cobrindo cartografia UTM/SIRGAS2000, espectrometria orbital (Sentinel-2, Landsat-8), índices NDVI/EVI/NDWI, geomorfologia de riscos (CPRM/IPT), SIG (QGIS/PostGIS) e CAR. |
| 23 | **hardware-security-specialist** | [`AGENT.md`](hardware-security-specialist/AGENT.md) | [`agent.yaml`](hardware-security-specialist/agent.yaml) | [`agent.json`](hardware-security-specialist/agent.json) | Especialista em Auditoria Física de Hardware, Segurança de Dispositivos IoT, Extração de Firmware, Glitching e Side-Channel Attacks. |
| 24 | **iam-specialist** | [`AGENT.md`](iam-specialist/AGENT.md) | [`agent.yaml`](iam-specialist/agent.yaml) | [`agent.json`](iam-specialist/agent.json) | Agente Especialista em Gestão de Identidades e Controle de Acessos (IAM/PAM), Governança de Identidades, Arquitetura Zero Trust, Entra ID, Power Platform, AWS, Azure, GCP e OCI IAM. |
| 25 | **information-systems-specialist** | [`AGENT.md`](information-systems-specialist/AGENT.md) | [`agent.yaml`](information-systems-specialist/agent.yaml) | [`agent.json`](information-systems-specialist/agent.json) | Agente especialista sênior em Sistemas de Informação Corporativos, cobrindo modelagem de processos BPMN 2.0, sistemas ERP/CRM, governança de serviços de TI (ITIL 4, COBIT 2019), Business Intelligence e auditoria de sistemas. |
| 26 | **malware-analyst** | [`AGENT.md`](malware-analyst/AGENT.md) | [`agent.yaml`](malware-analyst/agent.yaml) | [`agent.json`](malware-analyst/agent.json) | Especialista em Análise de Malware, Engenharia Reversa de Binários, Evasão de EDR e Análise Forense de Código Executável em Windows, Linux, Android e macOS. |
| 27 | **mathematician** | [`AGENT.md`](mathematician/AGENT.md) | [`agent.yaml`](mathematician/agent.yaml) | [`agent.json`](mathematician/agent.json) | Agente especialista sênior em Matemática Pura e Aplicada, cobrindo Cálculo Avançado (I a IV), Análise Real e Complexa, Teoria de Corpos e Galois, Álgebra Linear Avançada, EDO/EDP, Métodos Numéricos, Geometria Diferencial (do Carmo) e Probabilidade Axiomática (Kolmogorov, Itô). |
| 28 | **mechanical-engineer** | [`AGENT.md`](mechanical-engineer/AGENT.md) | [`agent.yaml`](mechanical-engineer/agent.yaml) | [`agent.json`](mechanical-engineer/agent.json) | Agente especialista sênior em Engenharia Mecânica, cobrindo mecânica dos sólidos, resistência dos materiais (Von Mises, Mohr), mecânica dos fluidos e CFD (Navier-Stokes), transferência de calor e dinâmica de sistemas mecânicos. |
| 29 | **mechatronics-engineer** | [`AGENT.md`](mechatronics-engineer/AGENT.md) | [`agent.yaml`](mechatronics-engineer/agent.yaml) | [`agent.json`](mechatronics-engineer/agent.json) | Agente especialista sênior em Engenharia Mecatrônica, Robótica Industrial/Móvel (ROS 2), Teoria de Controle Clássico e Moderno (Espaço de Estados, PID Anti-windup, LQR, Riccati, MPC, Kalman), Controladores Lógicos Programáveis (CLPs IEC 61131-3) e Sistemas SCADA. |
| 30 | **moodle-specialist** | [`AGENT.md`](moodle-specialist/AGENT.md) | [`agent.yaml`](moodle-specialist/agent.yaml) | [`agent.json`](moodle-specialist/agent.json) | Agente especialista sênior em Moodle LMS e EdTech. Atua desde a arquitetura de servidores e modelagem de banco de dados (DBA), até o design de temas (UI/UX), desenvolvimento de plugins, infraestrutura de caching (MUC), integrações (LTI, SCORM, xAPI) e aplicação de metodologias de Andragogia. |
| 31 | **pentester-agent** | [`AGENT.md`](pentester-agent/AGENT.md) | [`agent.yaml`](pentester-agent/agent.yaml) | [`agent.json`](pentester-agent/agent.json) | Agente Pentester Ético especializado em auditorias ofensivas (OWASP WSTG, DAST com OWASP ZAP, API Security, Cloud, LLMs e Red Team Scripting) usando utilitários CLI e scripts customizados. |
| 32 | **physical-engineer** | [`AGENT.md`](physical-engineer/AGENT.md) | [`agent.yaml`](physical-engineer/agent.yaml) | [`agent.json`](physical-engineer/agent.json) | Agente especialista sênior em Engenharia Física e Nanotecnologia, cobrindo física do estado sólido (Kronig-Penney, bandas, fônons de Debye), semicondutores, processos de microfabricação em sala limpa, síntese de nanomateriais de carbono e sensores quânticos. |
| 33 | **physicist** | [`AGENT.md`](physicist/AGENT.md) | [`agent.yaml`](physicist/agent.yaml) | [`agent.json`](physicist/agent.json) | Agente especialista sênior em Física Teórica e Aplicada, cobrindo Mecânica Clássica Avançada (Lagrangeana, Hamiltoniana, Poisson, Caos), Eletromagnetismo de Maxwell e Radiação de Larmor, Termodinâmica e Ensembles Estatísticos (Pathria, Sommerfeld, BEC), Relatividade Especial/Geral e Mecânica Quântica (Dirac, Pauli, Bloch). |
| 34 | **project-reviewer** | [`AGENT.md`](project-reviewer/AGENT.md) | [`agent.yaml`](project-reviewer/agent.yaml) | [`agent.json`](project-reviewer/agent.json) | Agente de Revisão de Projetos especializado na auditoria de regras de negócio, distribuição técnica (Banco, Backend, Frontend) e boas práticas de arquitetura e segurança. |
| 35 | **qa-testing-specialist** | [`AGENT.md`](qa-testing-specialist/AGENT.md) | [`agent.yaml`](qa-testing-specialist/agent.yaml) | [`agent.json`](qa-testing-specialist/agent.json) | Agente Especialista em Garantia de Qualidade (QA) e Automação de Testes Multi-Framework (Pytest, Unittest, Jest, Mocha, Criterion, Playwright). |
| 36 | **quantum-computing-specialist** | [`AGENT.md`](quantum-computing-specialist/AGENT.md) | [`agent.yaml`](quantum-computing-specialist/agent.yaml) | [`agent.json`](quantum-computing-specialist/agent.json) | Especialista em Computação Quântica, Desenvolvimento de Circuitos Quânticos (Qiskit, Cirq), Algoritmos Quânticos (Shor, Grover, VQE) e Criptografia Pós-Quântica (PQC). |
| 37 | **researcher** | [`AGENT.md`](researcher/AGENT.md) | [`agent.yaml`](researcher/agent.yaml) | [`agent.json`](researcher/agent.json) | Subagente Especialista em Pesquisa, Varredura de Codebase, Análise de Documentação e Busca Externa com ferramentas de leitura estrita. Ideal para investigações abrangentes sem sobrecarregar a janela de contexto principal. |
| 38 | **reverse-engineer-agent** | [`AGENT.md`](reverse-engineer-agent/AGENT.md) | [`agent.yaml`](reverse-engineer-agent/agent.yaml) | [`agent.json`](reverse-engineer-agent/agent.json) | Agente de Engenharia Reversa e Análise de Baixo Nível, especializado na depuração de processos, análise de binários, manipulação de memória (Cheat Engine) e segurança de código contra exploração. |
| 39 | **security-specialist** | [`AGENT.md`](security-specialist/AGENT.md) | [`agent.yaml`](security-specialist/agent.yaml) | [`agent.json`](security-specialist/agent.json) | Agente Especialista em Segurança da Informação, cobrindo práticas completas de AppSec (SAST, DAST, IAST, RASP, SCA), DevSecOps, conformidade regulatória de privacidade (LGPD/GDPR) e modelagem de ameaças. |
| 40 | **self** | [`AGENT.md`](self/AGENT.md) | [`agent.yaml`](self/agent.yaml) | [`agent.json`](self/agent.json) | Subagente de Auto-Clonagem, Delegação e Execução Concorrente / Isolamento de Contexto (Self Subagent / Fork Delegate). Herda e replica integralmente o modelo, ferramentas de workspace (leitura, edição, terminal, busca) e diretrizes do agente principal/chamador para executar subtarefas complexas em conversas ou subprocessos independentes em qualquer harness ou framework de IA. |
| 41 | **skill-creator** | [`AGENT.md`](skill-creator/AGENT.md) | [`agent.yaml`](skill-creator/agent.yaml) | [`agent.json`](skill-creator/agent.json) | Agente especialista sênior em Arquitetura, Criação, Aprimoramento e Catalogação de Skills para assistentes de IA. Domina a conversão de livros/documentos PDF em Markdown estruturado, elaboração de SKILL.md de padrão de produção, interconexão de habilidades e governança do repositório. |
| 42 | **software-architect** | [`AGENT.md`](software-architect/AGENT.md) | [`agent.yaml`](software-architect/agent.yaml) | [`agent.json`](software-architect/agent.json) | Agente de Arquitetura de Software que aplica DDD, SOLID e orquestração de Design Patterns para guiar o design de projetos. |
| 43 | **software-engineer** | [`AGENT.md`](software-engineer/AGENT.md) | [`agent.yaml`](software-engineer/agent.yaml) | [`agent.json`](software-engineer/agent.json) | Agente especialista sênior em Engenharia de Software, cobrindo engenharia de requisitos formais, arquiteturas modulares e distribuídas (Clean Architecture, Microsserviços, Hexagonal), DevSecOps, testes automatizados e métricas de qualidade. |
| 44 | **telecom-engineer** | [`AGENT.md`](telecom-engineer/AGENT.md) | [`agent.yaml`](telecom-engineer/agent.yaml) | [`agent.json`](telecom-engineer/agent.json) | Agente especialista sênior em Engenharia de Telecomunicações, cobrindo teoria da informação de Shannon, modulações digitais avançadas (QAM, OFDM), propagação em fibras ópticas (WDM/DWDM), redes celulares 5G/6G, comunicações por satélite e Radiofrequência. |
| 45 | **telecom-voice-specialist** | [`AGENT.md`](telecom-voice-specialist/AGENT.md) | [`agent.yaml`](telecom-voice-specialist/agent.yaml) | [`agent.json`](telecom-voice-specialist/agent.json) | Agente Especialista em Engenharia de Voz, Telefonia e Comunicações em Tempo Real (VoIP, SIP, SBC, PSTN, WebRTC, Codecs G.711/G.729/Opus, Kamailio/FreeSWITCH, QoS e STIR/SHAKEN). |

---

## ⚙️ Diretrizes de Contribuição e Adição de Novos Agentes

Ao criar um novo agente, garanta a paridade entre `AGENT.md`, `agent.yaml`, `agent.json` e `plugin.json`, utilizando sempre caminhos relativos e `model: inherit`.
