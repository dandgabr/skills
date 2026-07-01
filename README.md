# Repositório de Habilidades (Skills) e Customizações

Este repositório serve como uma pasta genérica centralizada para carregar habilidades (skills), instruções de agentes e definições de projetos para assistentes de programação de IA em CLI e IDEs.

A estrutura foi projetada para ser modular, extensível e compatível com as especificações de customização baseadas em agentes.

## 📁 Estrutura de Pastas

```text
├── README.md             # Este guia explicativo
├── AGENTS.md             # Regras gerais do projeto, estilo e restrições
├── skills.json           # Registro de caminhos de skills externas e heranças
├── skills/               # Diretório contendo as skills (regras de contexto)
│   ├── software-architect/ # Skill principal de Arquiteto de Software
│   ├── documentation-designer/ # Skill auxiliar de desenhos e diagramas (Mermaid)
│   ├── backend-developer/ # Papéis de Desenvolvimento (Backend, Frontend, QA, etc.)
│   ├── appsec-owasp-asvs/ # Segurança da Informação, Modelagem e Conformidade
│   ├── tech-typescript/  # Stacks de tecnologia específicas (Vue, TS, Testes)
│   ├── dp-*/             # 22 Habilidades de Padrões de Projeto (Design Patterns do GoF)
│   └── template-skill/   # Exemplo/Template de skill
└── agents/               # Diretório contendo os agentes configurados (ADK 2.0)
    ├── documenter/       # Agente Documentador e Designer
    └── software-architect/ # Agente Arquiteto de Software
```

## 🛠️ Como Utilizar

### 1. Regras do Projeto (`AGENTS.md`)
Escreva no arquivo [AGENTS.md](AGENTS.md) as regras de comportamento gerais que todos os agentes que carregam essa pasta devem seguir (p. ex., guias de estilo de código, convenções de arquitetura, padrões de commit).

### 2. O Ecossistema de Engenharia, Segurança, Design Patterns e Documentação
Neste repositório, as decisões de engenharia, segurança e práticas de desenvolvimento estão modularizadas e integradas:
- **[software-architect](skills/software-architect/SKILL.md)**: Atua como a skill coordenadora. Quando o agente precisa propor decisões de arquitetura de alto nível, aplicar DDD ou realizar modelagem lógica, ele carrega essa skill.
- **Segurança da Informação e DevSecOps**: Skills como **[appsec-owasp-asvs](skills/appsec-owasp-asvs/SKILL.md)** e **[devsecops-engineer](skills/devsecops-engineer/SKILL.md)** são empregadas para garantir a conformidade regulatória (LGPD/GDPR), design seguro de sistemas e automações de segurança em pipelines.
- **Desenvolvimento por Papéis**: Skills especializadas por domínio (**[backend-developer](skills/backend-developer/SKILL.md)**, **[frontend-developer](skills/frontend-developer/SKILL.md)**, **[qa-engineer](skills/qa-engineer/SKILL.md)**, **[ui-ux-designer](skills/ui-ux-designer/SKILL.md)**) definem os padrões esperados para cada disciplina da equipe.
- **[Design Patterns (dp-*)](skills/dp-factory-method/SKILL.md)**: Habilidades de apoio específicas para cada um dos 22 padrões clássicos de projeto (Gang of Four). A skill de arquiteto direciona a invocação dessas de forma condicional dependendo do cenário.
- **[documentation-designer](skills/documentation-designer/SKILL.md)**: Skill auxiliar especializada em documentar sistemas e desenhar diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe moderna do Mermaid.js.

### 3. Criando uma Nova Habilidade (Skill)
Para criar uma nova skill, adicione uma pasta sob `skills/` seguindo a estrutura do [template-skill](skills/template-skill/).
O arquivo principal é o `SKILL.md`, que precisa iniciar com um cabeçalho frontmatter em YAML:

```yaml
---
name: "Nome da Skill"
description: "Descrição de quando a IA deve ativar e usar esta skill"
---
# Instruções da Skill
Escreva aqui as diretrizes detalhadas de execução para esta skill específica.
```

### 4. Gerenciando Dependências e Heranças (`skills.json`)
O arquivo [skills.json](skills.json) permite registrar caminhos para outras pastas de skills (p. ex., de repositórios compartilhados do time) ou excluir skills específicas que você não deseja que sejam carregadas.

---

## 🧠 Catálogo Geral de Habilidades (Skills)

Abaixo está a listagem detalhada de todas as skills disponíveis no ecossistema deste repositório, agrupadas por área de especialidade:

### 🛠️ Engenharia, Papéis e Desenvolvimento de Software
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **backend-developer** | [`skills/backend-developer`](skills/backend-developer/SKILL.md) | Atua como Desenvolvedor Backend sênior, projetando APIs robustas, integrando bancos de dados eficientes, aplicando concorrência segura, otimizando performance e criando testes de integração robustos. |
| **frontend-developer** | [`skills/frontend-developer`](skills/frontend-developer/SKILL.md) | Atua como Desenvolvedor Frontend sênior, criando interfaces ricas, componentização avançada, gerenciamento de estado global eficiente, otimização de Core Web Vitals e conformidade com acessibilidade (WCAG). |
| **product-owner** | [`skills/product-owner`](skills/product-owner/SKILL.md) | Atua como Product Owner (PO), refinando histórias de usuários com critérios de aceitação BDD (Cucumber), gerenciando o Product Backlog e priorizando entregas com foco em valor de negócio (ROI). |
| **qa-engineer** | [`skills/qa-engineer`](skills/qa-engineer/SKILL.md) | Atua como Engenheiro de QA (Quality Assurance), elaborando estratégias de testes de software, automatizando testes E2E e de APIs, validando regressões e gerando relatórios de defeitos. |
| **scrum-master** | [`skills/scrum-master`](skills/scrum-master/SKILL.md) | Atua como Scrum Master e Agile Coach, facilitando cerimônias ágeis (Planning, Review, Retrospective, Dailies), eliminando impedimentos, gerenciando conflitos e monitorando métricas de produtividade (Velocity, Burndown). |
| **software-architect** | [`skills/software-architect`](skills/software-architect/SKILL.md) | Atua como Arquiteto de Software aplicando engenharia de baixo nível, princípios SOLID, DDD, decisões de topologia de sistemas, testabilidade e orquestração de Padrões de Projeto. |
| **ui-ux-designer** | [`skills/ui-ux-designer`](skills/ui-ux-designer/SKILL.md) | Atua como Designer UI/UX, executando pesquisas com usuários, fluxos lógicos, wireframes, protótipos de alta fidelidade baseados em Design Systems e processos consistentes de Design Handover. |

### 🛡️ Segurança, DevSecOps e Conformidade
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **appsec-owasp-asvs** | [`skills/appsec-owasp-asvs`](skills/appsec-owasp-asvs/SKILL.md) | Atua como Especialista em Application Security (AppSec) baseado no OWASP ASVS v5.0.0 integrado ao NIST SSDF, CWE e CERT Secure Coding, aplicando controles de código seguro em design e implementação. |
| **devsecops-engineer** | [`skills/devsecops-engineer`](skills/devsecops-engineer/SKILL.md) | Atua como Engenheiro de DevSecOps, automatizando verificações de segurança no pipeline de CI/CD (SAST, DAST, SCA), gerenciando secrets de forma segura e garantindo a segurança em Cloud e Containers. |
| **pentester-owasp-wstg** | [`skills/pentester-owasp-wstg`](skills/pentester-owasp-wstg/SKILL.md) | Atua como Pentester Ético e Especialista em Testes de Invasão sênior estruturando auditorias sob o framework OWASP WSTG v4.2, correlacionando-as com técnicas MITRE ATT&CK. |
| **secops-incident-responder** | [`skills/secops-incident-responder`](skills/secops-incident-responder/SKILL.md) | Atua como Analista de SecOps e Resposta a Incidentes, estruturando playbooks de resposta a ataques (NIST SP 800-61), monitoramento operacional (SIEM), hardening de ambientes de produção e planos de Disaster Recovery. |
| **security-architect-sabsa** | [`skills/security-architect-sabsa`](skills/security-architect-sabsa/SKILL.md) | Atua como Arquiteto de Segurança de Sistemas usando o framework SABSA alinhado ao TOGAF e NIST CSF, traduzindo objetivos de negócios em controles de segurança e modelando zonas de confiança Zero Trust. |
| **security-grc-compliance** | [`skills/security-grc-compliance`](skills/security-grc-compliance/SKILL.md) | Atua como Analista de Governança, Riscos e Conformidade (GRC), estruturando políticas de segurança, alinhando frameworks (ISO 27001, PCI-DSS, LGPD/GDPR) e medindo a eficácia de segurança com métricas organizacionais. |
| **security-manager-samm** | [`skills/security-manager-samm`](skills/security-manager-samm/SKILL.md) | Atua como Gestor de Segurança usando o framework OWASP SAMM alinhado ao BSIMM e CIS Controls para governar, avaliar e elevar a maturidade de segurança do SDLC, gerindo regras e criando novas skills. |
| **threat-modeler** | [`skills/threat-modeler`](skills/threat-modeler/SKILL.md) | Atua como Especialista em Modelagem de Ameaças (Threat Modeling), utilizando frameworks como STRIDE, PASTA e LINDDUN para antecipar ataques, identificar riscos e especificar requisitos de segurança. |

### 💻 Tecnologias e Linguagens
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **tech-testing** | [`skills/tech-testing`](skills/tech-testing/SKILL.md) | Fornece diretrizes e boas práticas para testes de software robustos, cobrindo TDD, Pirâmide de Testes, Unitários, Integração e E2E, além de ferramentas como Vitest, Jest e Playwright. |
| **tech-typescript** | [`skills/tech-typescript`](skills/tech-typescript/SKILL.md) | Fornece padrões de engenharia de software seguro e robusto usando TypeScript, cobrindo generics, tipos avançados, segurança estrita de compilador e mapeamento defensivo de dados. |
| **tech-vue** | [`skills/tech-vue`](skills/tech-vue/SKILL.md) | Fornece padrões de desenvolvimento modular e de alta performance usando o ecossistema Vue 3, cobrindo Composition API, TypeScript, Pinia, Vue Router e otimizações de reatividade. |

### 🧩 Padrões de Projeto (Design Patterns - GoF)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **dp-abstract-factory** | [`skills/dp-abstract-factory`](skills/dp-abstract-factory/SKILL.md) | Padrão de Projeto Criacional: Permite produzir famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. |
| **dp-adapter** | [`skills/dp-adapter`](skills/dp-adapter/SKILL.md) | Padrão de Projeto Estrutural: Permite que objetos com interfaces incompatíveis colaborem entre si. |
| **dp-bridge** | [`skills/dp-bridge`](skills/dp-bridge/SKILL.md) | Padrão de Projeto Estrutural: Divide uma classe grande ou um conjunto de classes intimamente ligadas em duas hierarquias separadas — abstração e implementação — que podem ser desenvolvidas independentemente. |
| **dp-builder** | [`skills/dp-builder`](skills/dp-builder/SKILL.md) | Padrão de Projeto Criacional: Permite construir objetos complexos passo a passo. Permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção. |
| **dp-chain-of-responsibility** | [`skills/dp-chain-of-responsibility`](skills/dp-chain-of-responsibility/SKILL.md) | Padrão de Projeto Comportamental: Permite passar requisições por uma corrente de manipuladores. Ao receber uma requisição, cada manipulador decide se processa a requisição ou a passa para o próximo manipulador. |
| **dp-command** | [`skills/dp-command`](skills/dp-command/SKILL.md) | Padrão de Projeto Comportamental: Transforma uma solicitação em um objeto independente que contém toda a informação sobre a solicitação, permitindo parametrizar, enfileirar ou desfazer operações. |
| **dp-composite** | [`skills/dp-composite`](skills/dp-composite/SKILL.md) | Padrão de Projeto Estrutural: Permite compor objetos em estruturas de árvore e trabalhar com essas estruturas como se fossem objetos individuais. |
| **dp-decorator** | [`skills/dp-decorator`](skills/dp-decorator/SKILL.md) | Padrão de Projeto Estrutural: Permite acoplar novos comportamentos a objetos ao colocá-los dentro de invólucros (wrappers) de objetos reais. |
| **dp-facade** | [`skills/dp-facade`](skills/dp-facade/SKILL.md) | Padrão de Projeto Estrutural: Fornece uma interface simplificada para uma biblioteca, um framework, ou qualquer outro conjunto complexo de classes. |
| **dp-factory-method** | [`skills/dp-factory-method`](skills/dp-factory-method/SKILL.md) | Padrão de Projeto Criacional: Fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. |
| **dp-flyweight** | [`skills/dp-flyweight`](skills/dp-flyweight/SKILL.md) | Padrão de Projeto Estrutural: Permite ajustar mais objetos na quantidade disponível de RAM ao compartilhar partes comuns de estado entre múltiplos objetos em vez de manter todos os dados em cada objeto. |
| **dp-iterator** | [`skills/dp-iterator`](skills/dp-iterator/SKILL.md) | Padrão de Projeto Comportamental: Permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore, etc.). |
| **dp-mediator** | [`skills/dp-mediator`](skills/dp-mediator/SKILL.md) | Padrão de Projeto Comportamental: Reduz as dependências caóticas entre objetos. Restringe comunicações diretas entre objetos e os força a colaborar apenas através de um objeto mediador. |
| **dp-memento** | [`skills/dp-memento`](skills/dp-memento/SKILL.md) | Padrão de Projeto Comportamental: Permite salvar e restaurar o estado anterior de um objeto sem revelar os detalhes de sua implementação. |
| **dp-observer** | [`skills/dp-observer`](skills/dp-observer/SKILL.md) | Padrão de Projeto Comportamental: Permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando. |
| **dp-prototype** | [`skills/dp-prototype`](skills/dp-prototype/SKILL.md) | Padrão de Projeto Criacional: Permite copiar objetos existentes sem tornar seu código dependente de suas classes. |
| **dp-proxy** | [`skills/dp-proxy`](skills/dp-proxy/SKILL.md) | Padrão de Projeto Estrutural: Fornece um substituto ou um espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo fazer algo antes ou depois que a requisição chegue a ele. |
| **dp-singleton** | [`skills/dp-singleton`](skills/dp-singleton/SKILL.md) | Padrão de Projeto Criacional: Garante que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância. |
| **dp-state** | [`skills/dp-state`](skills/dp-state/SKILL.md) | Padrão de Projeto Comportamental: Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe. |
| **dp-strategy** | [`skills/dp-strategy`](skills/dp-strategy/SKILL.md) | Padrão de Projeto Comportamental: Define uma família de algoritmos, coloca cada um deles em uma classe separada, e faz seus objetos intercambiáveis. |
| **dp-template-method** | [`skills/dp-template-method`](skills/dp-template-method/SKILL.md) | Padrão de Projeto Comportamental: Define o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura. |
| **dp-visitor** | [`skills/dp-visitor`](skills/dp-visitor/SKILL.md) | Padrão de Projeto Comportamental: Permite separar algoritmos dos objetos nos quais eles operam. |

### ⚙️ Auxiliares e Templates
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **documentation-designer** | [`skills/documentation-designer`](skills/documentation-designer/SKILL.md) | Auxilia na elaboração de documentação técnica rica e no desenho de diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe do Mermaid.js. |
| **template-skill** | [`skills/template-skill`](skills/template-skill/SKILL.md) | Um template básico que demonstra como estruturar uma habilidade (skill) personalizada para agentes de IA. |
