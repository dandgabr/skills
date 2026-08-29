# 🧠 ZAI CLI - Manual de Operação e Diretrizes do Repositório

Este arquivo é lido automaticamente pelo **ZAI CLI** (`.zai/ZAI.md`) e estabelece as diretrizes de engenharia, o protocolo de ativação dinâmica de personas e o roteamento para as **196 Habilidades (Skills)** e **42 Agentes Especializados Universais** mantidos no repositório.

---

## 📌 Diretrizes Globais do Projeto (Alinhamento Canônico)

1. **Idiomas**:
   - Os comentários no código e mensagens de commit devem ser preferencialmente em **Inglês** (ou conforme o padrão definido pelo time).
   - As interações no chat com o desenvolvedor devem ser em **Português**, a menos que solicitado de outra forma.

2. **Qualidade e Estilo de Código**:
   - Sempre siga as convenções da linguagem do projeto atual (p. ex., PEP 8 para Python, ESLint/Prettier para JavaScript/TypeScript, Google Java Style, etc.).
   - Priorize legibilidade e simplicidade sobre otimizações prematuras.
   - Mantenha funções pequenas e com responsabilidade única (SRP).

3. **Arquitetura e Clean Code**:
   - Siga os princípios SOLID e Domain-Driven Design (DDD) quando aplicável.
   - Mantenha a separação de responsabilidades (camadas de negócio, dados e apresentação).
   - Garanta a não duplicação e reutilização ativa de código utilizando a skill canônica [**clean-code-reusability**](skills/engineering-practices/clean-code-reusability/SKILL.md).

4. **Gerenciamento de Erros e Logs**:
   - Evite blocos catch/except vazios.
   - Utilize logging apropriado e estruturado em vez de prints genéricos no console.

---

## ⚡ Protocolo de Operação e Ativação Dinâmica no ZAI CLI

O ZAI CLI opera com modelos avançados da família GLM (GLM-4.6 / GLM-4.5) e ferramentas de sistema (`view_file`, `str_replace_editor`, `create_file`, `bash`, `search`, `batch_edit`).

### 🎯 Fluxo de Execução sob Demanda:
1. **Identificação e Descoberta**: Ao receber uma tarefa técnica especializada, consulte o catálogo unificado em [**CATALOGO.md**](CATALOGO.md) ou o catálogo de agentes em [**agents/README.md**](agents/README.md) para identificar as habilidades e personas relevantes.
2. **Carregamento sob Demanda (Just-in-Time)**: Utilize a ferramenta `view_file` para carregar o arquivo canônico de instruções antes de iniciar o trabalho:
   - **Para Agentes**: `view_file` no caminho `agents/<nome-do-agente>/AGENT.md`
   - **Para Skills**: `view_file` no caminho `skills/<categoria>/.../<nome-da-skill>/SKILL.md`
3. **Execução Especializada**: Assuma o papel, aplique os padrões técnicos, checklists, formulários e convenções especificados no documento carregado.
4. **Clean Code Pre-Check**: Antes de criar ou modificar código, faça buscas no codebase para reutilizar estruturas e funções existentes conforme [**clean-code-reusability**](skills/engineering-practices/clean-code-reusability/SKILL.md).

---

## 📚 Catálogos e Índices Mestres

Para evitar duplicações e manter a consistência, todos os metadados, tabelas descritivas completas e caminhos estão centralizados nos seguintes documentos canônicos:

- 📖 [**CATALOGO.md**](CATALOGO.md): Índice completo e detalhado de todas as **196 Habilidades (Skills)** divididas em 11 categorias e de todos os **42 Agentes Especializados**.
- 🤖 [**agents/README.md**](agents/README.md): Guia da Arquitetura Multi-Harness (Markdown, YAML e JSON) e catálogo com os 42 agentes prontos para execução universal.
- 📜 [**AGENTS.md**](AGENTS.md): Regras, convenções e definições gerais de governança do repositório.

---

## 🗂️ Mapa Sintético de Categorias de Habilidades (Skills)

| Categoria | Diretório | Descrição / Escopo | Total |
| :--- | :--- | :--- | :---: |
| ☁️ **Infraestrutura & Nuvem** | [`skills/cloud-infra/`](skills/cloud-infra/) | AWS, Azure, GCP, OCI, Linux Kernel, HPC Clusters, Zero Trust | **7** |
| 🗄️ **Bancos de Dados & Streaming** | [`skills/databases/`](skills/databases/) | PostgreSQL, MariaDB, SQLite, MongoDB, Data Mesh, Real-Time Streaming | **6** |
| 🔬 **Domínios & Engenharias** | [`skills/domains/`](skills/domains/) | Exatas, Física, Química, Civil, Elétrica, Telecom, Robótica, IA/RAG, Hardware Hacking | **39** |
| 📐 **Práticas de Engenharia** | [`skills/engineering-practices/`](skills/engineering-practices/) | Clean Code, C4 Model, System Design & Scalability, Documentação Técnica | **5** |
| 🧪 **Frameworks, Web & Testes** | [`skills/framework/`](skills/framework/) | Testes (Pytest, Jest, Mocha, Criterion), APIs REST/gRPC/GraphQL, React, Vue | **14** |
| 💻 **Linguagens de Programação** | [`skills/languages/`](skills/languages/) | Python, TypeScript, Go, Rust, C, C++, Assembly x64, Bash, PowerShell, etc. | **15** |
| 🗺️ **Mapeamento & Topologia** | [`skills/mapping/`](skills/mapping/) | AST, Call Graphs, Topologia de Rede, eBPF, CMDB, Schemas de BD e Binários | **13** |
| 🧩 **Padrões de Projeto (GoF)** | [`skills/patterns/`](skills/patterns/) | Padrões Criacionais, Estruturais e Comportamentais do Gang of Four | **22** |
| 🛠️ **Softwares & Ferramentas** | [`skills/programs/`](skills/programs/) | Containers, GitHub Actions, Moodle LMS, WinDbg, Power BI, Power Automate | **12** |
| 🎭 **Papéis de Engenharia (Roles)** | [`skills/roles/`](skills/roles/) | Arquiteto de Software, Backend, Frontend, DevOps, DBA, QA Engineer, PO, UX | **15** |
| 🛡️ **Segurança & DevSecOps** | [`skills/security/`](skills/security/) | AppSec (ASVS, MASVS), AI Security, Cloud IAM, Criptografia/PKI, GRC, SecOps | **48** |

> ℹ️ *Consulte [**CATALOGO.md**](CATALOGO.md) para a lista detalhada de todas as 196 skills.*

---

## 🤖 Núcleo de Agentes Principais para Invocação Rápida

| Agente | Arquivo de Persona | Especialidade Principal |
| :--- | :--- | :--- |
| **general** | [`agents/general/AGENT.md`](agents/general/AGENT.md) | Orquestração de tarefas complexas multi-etapas e integração dinâmica de skills. |
| **self** | [`agents/self/AGENT.md`](agents/self/AGENT.md) | Subagente para clonagem, delegação concorrente e isolamento de contexto. |
| **researcher** | [`agents/researcher/AGENT.md`](agents/researcher/AGENT.md) | Pesquisa aprofundada, análise de documentação e varredura de código em leitura estrita. |
| **software-architect** | [`agents/software-architect/AGENT.md`](agents/software-architect/AGENT.md) | Arquitetura de software de alto e baixo nível, Domain-Driven Design e Design Patterns. |
| **software-engineer** | [`agents/software-engineer/AGENT.md`](agents/software-engineer/AGENT.md) | Engenharia de software integral, desenvolvimento, refatoração e testes. |
| **fullstack-developer** | [`agents/fullstack-developer/AGENT.md`](agents/fullstack-developer/AGENT.md) | Desenvolvimento web de ponta a ponta (Frontend, Backend e Integração). |
| **devops-engineer** | [`agents/devops-engineer/AGENT.md`](agents/devops-engineer/AGENT.md) | Infraestrutura como Código (IaC), CI/CD, Containers e Platform Engineering. |
| **dba-specialist** | [`agents/dba-specialist/AGENT.md`](agents/dba-specialist/AGENT.md) | Administração, modelagem e otimização de bancos de dados SQL e NoSQL. |
| **qa-testing-specialist** | [`agents/qa-testing-specialist/AGENT.md`](agents/qa-testing-specialist/AGENT.md) | Automação e estratégias formais de teste (TDD, BDD, Mutação, Cobertura). |
| **security-specialist** | [`agents/security-specialist/AGENT.md`](agents/security-specialist/AGENT.md) | Segurança da informação, AppSec (SAST/DAST/SCA), DevSecOps e Modelagem de Ameaças. |

> ℹ️ *Para acessar a lista completa dos 42 agentes especializados com manifestos YAML e JSON, consulte [**agents/README.md**](agents/README.md).*
