# Repositório de Habilidades e Agentes

Este repositório serve como uma central modular e extensível para carregamento de **Habilidades (Skills)**, **Agentes Especializados Universais (Multi-Harness Architecture)** e regras de engenharia de software para assistentes de programação de inteligência artificial em CLI e IDEs (Claude Code, OpenCode, OpenAI Codex, Google Antigravity, Cursor, Windsurf, Z.ai e frameworks multi-agente).

---

## 🧭 Navegação Rápida

> 📚 **[Acesse o Catálogo Completo de Habilidades e Agentes (CATALOGO.md)](CATALOGO.md)**  
> Consulte a lista detalhada das **187 Skills** e **51 Agentes Especializados**, com métricas por categoria, subcategorias e descrições técnicas completas.

- 🤖 **[Guia de Agentes Especializados Universais (agents/README.md)](agents/README.md)**: Personas, manifestos (`AGENT.md`, `agent.yaml`, `agent.json`) e instruções de execução para qualquer harness.
- 📜 **[Regras Globais do Projeto (AGENTS.md)](AGENTS.md)**: Diretrizes de comportamento, Clean Code, padrões de skills e criação de agentes.
- ⚙️ **[Manifesto de Skills (skills.json)](skills.json)**: Configuração e importação modular de habilidades.

---

## 📁 Estrutura de Pastas

```text
├── CATALOGO.md             # Catálogo mestre com inventário de todas as 187 skills e 51 agentes
├── README.md               # Visão geral e documentação do repositório
├── AGENTS.md               # Regras gerais de comportamento, clean code e workflows
├── skills.json             # Manifesto de carregamento e herança de skills
├── skills/
│   ├── cloud-infra/        # AWS, Azure, GCP, OCI, Linux Kernel, HPC, Zero Trust (7 skills)
│   ├── databases/          # PostgreSQL, MariaDB, MongoDB, SQLite, Data Mesh, Streaming (6 skills)
│   ├── domains/            # Matemática, Física, Computação Teórica, Circuitos, Robótica/Controle, Telecom, Química/CFD, SEP, Biotecnologia, WebAssembly (34 skills)
│   ├── engineering-practices/ # Clean Code, C4 Model, System Design, Conventional Commits (6 skills)
│   ├── framework/          # Spring Boot, Quarkus, MicroProfile, React, Vue, APIs REST, GraphQL, gRPC, SOAP, Testes de Mutação (15 skills)
│   ├── languages/          # Java Moderno, Python, TypeScript, Go, Rust, C, C++, Assembly, Typst, LaTeX, Bash, etc. (15 skills)
│   ├── mapping/            # Código AST, Call Graphs, Rede, eBPF, CMDB, Engenharia Reversa (13 skills)
│   ├── patterns/           # Design Patterns GoF e Boundary-Control-Entity BCE (4 skills)
│   ├── programs/           # Containers, GitHub Actions, Antigravity Guide, Markmap, Moodle, WinDbg, DAST, IAST, SAST (15 skills)
│   ├── roles/              # Architect, Orchestrator, Career Hunter, Web/Code Researcher, DevOps, DBA, QA, PO, UX (21 skills)
└── agents/                 # 51 Agentes Especializados Universais em 7 Categorias
    ├── core-orchestration/     # Orquestração, supervisão, general e autodelegação (4 agentes)
    ├── research-discovery/     # Pesquisa de código, web, literatura científica e mapeamento (5 agentes)
    ├── software-engineering/   # Engenharia de software, arquitetura, QA/mutação, Java e otimização (9 agentes)
    ├── data-cloud-devops/      # Multi-Cloud, DevOps/CI-CD, DBA, Data Mesh e IA/Big Data (5 agentes)
    ├── cybersecurity/          # Pentest, AppSec, IAM, IA Red Teaming, Malware e Hardware (7 agentes)
    ├── academic-sciences/      # Ciências exatas, engenharias de base e computação avançada (16 agentes)
    └── specialized-domains/    # Carreira/ATS, Moodle LMS, Sistemas Corporativos e Criador de Skills (5 agentes)
```

---

## 🛠️ Como Utilizar

### 1. Regras do Projeto (`AGENTS.md`)
O arquivo [AGENTS.md](AGENTS.md) define as regras gerais que todos os agentes e modelos devem seguir ao interagir com o código deste repositório (ex: comentários em inglês, respostas em português, padrões de clean code e reuso).

### 2. O Ecossistema Modular de Habilidades
As habilidades estão organizadas de forma coesa para permitir que os agentes invoquem apenas os conhecimentos necessários para cada tarefa:
- **Arquitetura & Engenharia**: A skill [software-architect](skills/roles/software-architect/SKILL.md) coordena decisões estruturais, orientando a invocação de [c4-model-architecture](skills/engineering-practices/c4-model-architecture/SKILL.md), [system-design-scalability](skills/engineering-practices/system-design-scalability/SKILL.md) e das master skills de [Design Patterns](CATALOGO.md#-padrões-de-projeto--design-patterns-gof-3).
- **Clean Code & Reuso**: A skill [clean-code-reusability](skills/engineering-practices/clean-code-reusability/SKILL.md) é transversal e garante a não duplicação e alta legibilidade do código.
- **Segurança da Informação**: Abrange do ciclo de desenvolvimento seguro ([appsec-owasp-asvs](skills/security/appsec/appsec-owasp-asvs/SKILL.md), [threat-modeler](skills/security/ops-architecture/threat-modeler/SKILL.md)) até conformidade normativa ([iso-27000-series](skills/security/grc-compliance/iso-27000-series/SKILL.md), [isc2-cissp-csslp-standards](skills/security/grc-compliance/isc2-cissp-csslp-standards/SKILL.md)).

### 3. Criando uma Nova Habilidade (Skill)
Para criar uma nova skill, adicione uma pasta sob a categoria correspondente em `skills/` seguindo a estrutura do [template-skill](skills/engineering-practices/template-skill/SKILL.md).
O arquivo principal é o `SKILL.md`, contendo o cabeçalho frontmatter em YAML:

```yaml
---
name: "nome-da-skill"
description: "Descrição técnica clara indicando quando a IA deve ativar esta skill"
---
# Instruções da Skill
Diretrizes técnicas, padrões, formulários e exemplos de código.
```

### 4. Gerenciando Dependências e Heranças (`skills.json`)
O arquivo [skills.json](skills.json) permite registrar fontes externas de skills ou configurar escopos de carregamento.

---

Para consultar o inventário detalhado de todas as 187 skills e 51 agentes, acesse o **[Catálogo Completo (CATALOGO.md)](CATALOGO.md)**.
