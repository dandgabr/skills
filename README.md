# Repositório de Habilidades (Skills) e Customizações

Este repositório serve como uma pasta genérica centralizada para carregar habilidades (skills), instruções de agentes e definições de projetos para assistentes de programação de IA em CLI e IDEs.

A estrutura foi projetada para ser modular, extensível e compatível com as especificações de customização baseadas em agentes.

## 📁 Estrutura de Pastas

```text
├── README.md
├── AGENTS.md
├── skills.json
├── skills/
│   ├── general/
│   │   ├── cloud-infra/            # AWS, Azure, GCP, OCI
│   │   ├── domains/                # Blockchain, Financial Processing
│   │   ├── engineering-practices/  # Clean Code, Documentation, Templates
│   │   └── roles/                  # Architect, Backend, Frontend, DevOps, QA, PO, UX, Scrum
│   ├── security/
│   │   ├── ai-security/            # LLM/SLM, Vision, Voice Security
│   │   ├── appsec/                 # OWASP ASVS, MASVS, WSTG, API, SAST, SCA
│   │   ├── cloud-iam/              # AWS, Azure, GCP, OCI IAM, CSA Cloud
│   │   ├── crypto-pki/             # Cryptography PQC, PKI Digital Signatures
│   │   ├── grc-compliance/         # ISO 27000, NIST CSF, PCI-DSS, Privacy, SAMM, GRC
│   │   └── ops-architecture/       # DevSecOps, Threat Modeler, SABSA, MFA, SecOps
│   ├── languages/                  # Bash, C, C++, Go, Rust, Python, TypeScript, Lua, LaTeX, etc.
│   ├── databases/                  # MariaDB, MongoDB, PostgreSQL, SQLite
│   ├── framework/                  # Pytest, Unittest, Nose2, Ward, Jest, Mocha, Criterion, Vue, etc.
│   ├── programs/                   # Gemini Enterprise, Power BI, Power Automate, etc.
│   └── patterns/
│       ├── behavioral/             # Chain of Resp., Strategy, Observer, State, etc.
│       ├── creational/             # Factory Method, Singleton, Builder, etc.
│       └── structural/             # Adapter, Facade, Decorator, Proxy, etc.
└── agents/
    ├── documenter/
    ├── software-architect/
    ├── fullstack-developer/
    ├── devops-engineer/
    ├── dba-specialist/
    ├── telecom-voice-specialist/
    ├── cloud-infrastructure-architect/
    ├── qa-testing-specialist/
    ├── ai-security-specialist/
    ├── security-specialist/
    ├── iam-specialist/
    ├── pentester-agent/
    ├── project-reviewer/
    ├── reverse-engineer-agent/
    ├── moodle-specialist/
    ├── skill-creator/
    ├── antigravity-agent/
    ├── researcher/
    ├── self/
    ├── explore/
    └── general/
```

## 🛠️ Como Utilizar

### 1. Regras do Projeto (`AGENTS.md`)
Escreva no arquivo [AGENTS.md](AGENTS.md) as regras de comportamento gerais que todos os agentes que carregam essa pasta devem seguir (p. ex., guias de estilo de código, convenções de arquitetura, padrões de commit).

### 2. O Ecossistema de Engenharia, Segurança, Design Patterns e Documentação
Neste repositório, as decisões de engenharia, segurança e práticas de desenvolvimento estão modularizadas e integradas:
- **[software-architect](skills/general/roles/software-architect/SKILL.md)**: Atua como a skill coordenadora. Quando o agente precisa propor decisões de arquitetura de alto nível, aplicar DDD ou realizar modelagem lógica, ele carrega essa skill.
- **[clean-code-reusability](skills/general/engineering-practices/clean-code-reusability/SKILL.md)**: Garante a escrita de código limpo, manutenível, sem redundâncias e estruturado segundo boas práticas de documentação em qualquer stack.
- **Segurança da Informação, DevSecOps e Privacidade**: Skills como **[appsec-owasp-asvs](skills/security/appsec/appsec-owasp-asvs/SKILL.md)**, **[devsecops-engineer](skills/security/ops-architecture/devsecops-engineer/SKILL.md)**, **[security-champions](skills/security/ops-architecture/security-champions/SKILL.md)** e **[security-privacy](skills/security/grc-compliance/security-privacy/SKILL.md)** são empregadas para garantir o design seguro, conformidade regulatória (LGPD/GDPR/ISO 27701) e proteção à privacidade por design e por padrão.
- **Pentest de APIs**: A skill **[pentester-owasp-api-security-2023](skills/security/appsec/pentester-owasp-api-security-2023/SKILL.md)** complementa o ecossistema para auditorias seguras em APIs REST, GraphQL, SOAP e microsserviços com base no OWASP API Security Top 10 2023.
- **Desenvolvimento por Papéis**: Skills especializadas por domínio (**[backend-developer](skills/general/roles/backend-developer/SKILL.md)**, **[frontend-developer](skills/general/roles/frontend-developer/SKILL.md)**, **[dba-database-administrator](skills/general/roles/dba-database-administrator/SKILL.md)**, **[qa-engineer](skills/general/roles/qa-engineer/SKILL.md)**, **[ui-ux-designer](skills/general/roles/ui-ux-designer/SKILL.md)**) definem os padrões esperados para cada disciplina da equipe.
- **[Design Patterns (dp-*)](skills/patterns/creational/dp-factory-method/SKILL.md)**: Habilidades de apoio específicas para cada um dos 22 padrões clássicos de projeto (Gang of Four). A skill de arquiteto direciona a invocação dessas de forma condicional dependendo do cenário.
- **[documentation-designer](skills/general/engineering-practices/documentation-designer/SKILL.md)**: Skill auxiliar especializada em documentar sistemas e desenhar diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe moderna do Mermaid.js.

### 3. Criando uma Nova Habilidade (Skill)
Para criar uma nova skill, adicione uma pasta sob `skills/` seguindo a estrutura do [template-skill](skills/general/engineering-practices/template-skill/SKILL.md).
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
| **backend-developer** | [`skills/general/backend-developer`](skills/general/roles/backend-developer/SKILL.md) | Atua como Desenvolvedor Backend sênior, projetando APIs robustas, integrando bancos de dados eficientes, aplicando concorrência segura, otimizando performance e criando testes de integração robustos. |
| **blockchain-cryptocurrency** | [`skills/general/blockchain-cryptocurrency`](skills/general/domains/blockchain-cryptocurrency/SKILL.md) | Atua como especialista em Blockchain, Criptomoedas, Smart Contracts (Solidity, Rust, EVM, Solana), DeFi, Tokenização (ERC-20, ERC-721, ERC-1155), Arquitetura UTXO/Account, Layer 2 (ZK/Optimistic Rollups) e Segurança/Auditoria Web3. |
| **clean-code-reusability** | [`skills/general/clean-code-reusability`](skills/general/engineering-practices/clean-code-reusability/SKILL.md) | Garante a escrita de código limpo, legível, livre de redundâncias através da reutilização ativa de componentes existentes, e documentado de acordo com as melhores práticas da tecnologia. |
| **cloud-aws** | [`skills/general/cloud-aws`](skills/general/cloud-infra/cloud-aws/SKILL.md) | Atua como especialista em arquitetura, engenharia e operação na nuvem Amazon Web Services (AWS), cobrindo Well-Architected Framework, Compute (EC2, EKS, Lambda), Storage (S3, EBS, EFS), Databases (Aurora, DynamoDB), Networking (VPC, Transit Gateway, CloudFront), IaC (Terraform, CDK) e FinOps. |
| **cloud-azure** | [`skills/general/cloud-azure`](skills/general/cloud-infra/cloud-azure/SKILL.md) | Atua como especialista em arquitetura, engenharia e operação na nuvem Microsoft Azure, cobrindo Cloud Adoption Framework, Well-Architected Framework, Compute (VMs, AKS, App Services, Azure Functions), Storage (Blob, Files, Disks), Databases (Azure SQL, Cosmos DB), Networking (VNet, ExpressRoute, Front Door), IaC (Terraform, Bicep) e FinOps. |
| **cloud-gcp** | [`skills/general/cloud-gcp`](skills/general/cloud-infra/cloud-gcp/SKILL.md) | Atua como especialista em arquitetura, engenharia e operação na nuvem Google Cloud Platform (GCP), cobrindo Google Cloud Architecture Framework, Compute (Compute Engine, GKE, Cloud Run), Storage (GCS, Persistent Disk), Databases (Cloud SQL, Spanner, BigQuery), Networking (Global VPC, Cloud Armor), IaC (Terraform) e FinOps. |
| **cloud-oci** | [`skills/general/cloud-oci`](skills/general/cloud-infra/cloud-oci/SKILL.md) | Atua como especialista em arquitetura, engenharia e operação na nuvem Oracle Cloud Infrastructure (OCI), cobrindo OCI Architecture Center, Compute (Bare Metal, VMs, OKE), Storage (Block Volumes, Object Storage), Databases (Autonomous Database, Exadata, MySQL HeatWave), Networking (VCN, DRG, FastConnect), IaC (Terraform, Resource Manager) e FinOps. |
| **dba-database-administrator** | [`skills/general/dba-database-administrator`](skills/general/roles/dba-database-administrator/SKILL.md) | Atua como Administrador de Banco de Dados (DBA) sênior para sistemas SQL e NoSQL, cobrindo modelagem de dados, estratégias de indexação, otimização de consultas (EXPLAIN), concorrência (ACID/BASE), alta disponibilidade, backups (PITR) e segurança. |
| **devops-engineer** | [`skills/general/devops-engineer`](skills/general/roles/devops-engineer/SKILL.md) | Atua como Engenheiro de DevOps e Platform Engineering sênior, cobrindo Terraform (IaC), Ansible, Vagrant, Kubernetes (GitOps/ArgoCD), containers (Docker/Podman), Backstage (IDP), CI/CD, Packer (Golden Images), observabilidade (Prometheus/Grafana/OpenTelemetry) e estratégias de deploy (Blue-Green, Canary). |
| **edtech-andragogy** | [`skills/general/domains/edtech-andragogy`](skills/general/domains/edtech-andragogy/SKILL.md) | Atua como especialista em Tecnologia Educacional (EdTech) e metodologias de ensino para adultos (Andragogia), dominando design instrucional, gamificação e padrões de interoperabilidade (SCORM, LTI, xAPI). |
| **explore** | [`skills/general/explore`](skills/general/roles/explore/SKILL.md) | Atua como agente especializado em exploração rápida de codebases, busca de padrões, entendimento de estrutura e resposta a perguntas sobre código existente. |
| **financial-transaction-processing** | [`skills/general/financial-transaction-processing`](skills/general/domains/financial-transaction-processing/SKILL.md) | Atua como especialista em processamento de transações financeiras e sistemas de pagamentos no Brasil (Pix, SPI, DICT, SPB, Boleto, CIP/Núclea) e no exterior (ISO 20022, SWIFT, FedNow, SEPA, Adquirencia, Gateways, Antifraude, Conciliacao e Idempotencia). |
| **frontend-developer** | [`skills/general/frontend-developer`](skills/general/roles/frontend-developer/SKILL.md) | Atua como Desenvolvedor Frontend sênior, criando interfaces ricas, componentização avançada, gerenciamento de estado global eficiente, otimização de Core Web Vitals e conformidade com acessibilidade (WCAG). |
| **fullstack-developer** | [`skills/general/fullstack-developer`](skills/general/roles/fullstack-developer/SKILL.md) | Atua como Desenvolvedor Full Stack especialista em criar aplicações web fim a fim, integrando lógica de backend (REST, gRPC), frontend (React, Vue), bancos de dados (DBA) e garantindo código limpo e seguro. |
| **general** | [`skills/general/general`](skills/general/roles/general/SKILL.md) | Atua como agente de propósito geral para pesquisa complexa e execução de tarefas multi-etapas, integrando múltiplas skills conforme necessário. |
| **product-owner** | [`skills/general/product-owner`](skills/general/roles/product-owner/SKILL.md) | Atua como Product Owner (PO), refinando histórias de usuários com critérios de aceitação BDD (Cucumber), gerenciando o Product Backlog e priorizando entregas com foco em valor de negócio (ROI). |
| **project-reviewer** | [`skills/general/project-reviewer`](skills/general/roles/project-reviewer/SKILL.md) | Atua como Revisor de Projetos especialista, auditando e padronizando regras de negócio, definindo a distribuição de responsabilidades entre Banco, Backend e Frontend, e garantindo boas práticas de arquitetura e segurança. |
| **qa-engineer** | [`skills/general/qa-engineer`](skills/general/roles/qa-engineer/SKILL.md) | Atua como Engenheiro de QA (Quality Assurance) e Automação de Testes Multi-Framework, elaborando estratégias de testes (unitários, integração, E2E), validando regressões e gerando relatórios de defeitos. |
| **scrum-master** | [`skills/general/scrum-master`](skills/general/roles/scrum-master/SKILL.md) | Atua como Scrum Master e Agile Coach, facilitando cerimônias ágeis (Planning, Review, Retrospective, Dailies), eliminando impedimentos, gerenciando conflitos e monitorando métricas de produtividade (Velocity, Burndown). |
| **software-architect** | [`skills/general/software-architect`](skills/general/roles/software-architect/SKILL.md) | Atua como Arquiteto de Software aplicando engenharia de baixo nível, princípios SOLID, DDD, decisões de topologia de sistemas, testabilidade e orquestração de Padrões de Projeto. |
| **telecom-voice-engineering** | [`skills/general/telecom-voice-engineering`](skills/general/domains/telecom-voice-engineering/SKILL.md) | Atua como Especialista em Engenharia de Voz, Telefonia e Comunicações em Tempo Real (VoIP, SIP, SBC, PSTN, WebRTC, Codecs G.711/G.729/Opus, Kamailio/FreeSWITCH, QoS e STIR/SHAKEN). |
| **ui-ux-designer** | [`skills/general/ui-ux-designer`](skills/general/roles/ui-ux-designer/SKILL.md) | Atua como Designer UI/UX, executando pesquisas com usuários, fluxos lógicos, wireframes, protótipos de alta fidelidade baseados em Design Systems e processos consistentes de Design Handover. |

### 🛡️ Segurança, DevSecOps e Conformidade
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **ai-computer-vision-security** | [`skills/security/ai-computer-vision-security`](skills/security/ai-security/ai-computer-vision-security/SKILL.md) | Atua como Especialista em Segurança de Visão Computacional (CV), cobrindo mitigação de ataques adversariais (FGSM, PGD, Patch Attacks), envenenamento de dados de imagem, backdoors visuais, invasão de sensores, detecção de deepfakes e alinhamento com OWASP ML Top 10 e OWASP MLSVS. |
| **ai-llm-slm-security** | [`skills/security/ai-llm-slm-security`](skills/security/ai-security/ai-llm-slm-security/SKILL.md) | Atua como Especialista em Segurança, Governança e Red Teaming de Modelos de Linguagem (LLMs e SLMs), cobrindo mitigação de Prompt Injection, Jailbreaking, envenenamento de dados, segurança de RAG e conformidade total com o OWASP Top 10 for LLM e OWASP AI Exchange. |
| **ai-model-security-analysis** | [`skills/security/ai-model-security-analysis`](skills/security/ai-security/ai-model-security-analysis/SKILL.md) | Auditoria e análise de segurança de artefatos de IA/ML, cobrindo verificação de formatos (.safetensors vs .pkl), scanning de exploits (picklescan), inspeção de código remoto e avaliação comportamental/alinhamento. |
| **ai-voice-stt-tts-security** | [`skills/security/ai-voice-stt-tts-security`](skills/security/ai-security/ai-voice-stt-tts-security/SKILL.md) | Atua como Especialista em Segurança de Processamento de Voz, Fala (STT/ASR) e Síntese Vocal (TTS), cobrindo o modelo HAVOC para dispositivos controlados por voz, ataques ultrassônicos inaudíveis, deepfake de voz, defesa em biometria vocal e alinhamento com OWASP ML Top 10 e OWASP API Security. |
| **appsec-owasp-asvs** | [`skills/security/appsec-owasp-asvs`](skills/security/appsec/appsec-owasp-asvs/SKILL.md) | Atua como Especialista em Application Security (AppSec) baseado no OWASP ASVS v5.0.0 integrado ao NIST SSDF, CWE e CERT Secure Coding, aplicando controles de código seguro em design e implementação. |
| **appsec-owasp-masvs** | [`skills/security/appsec-owasp-masvs`](skills/security/appsec/appsec-owasp-masvs/SKILL.md) | Atua como Especialista em Segurança de Aplicações Móveis (Mobile AppSec) baseado no OWASP MASVS v2.0.0 e MASTG (Android e iOS), cobrindo armazenamento seguro, criptografia móvel, proteção de rede, segurança de plataforma/WebViews, engenharia reversa e resiliência. |
| **auth-protocols-mfa** | [`skills/security/auth-protocols-mfa`](skills/security/ops-architecture/auth-protocols-mfa/SKILL.md) | Atua como especialista em protocolos de autenticação e autorização (RADIUS, TACACS+, Kerberos, OAuth 2.0, OpenID Connect, SAML 2.0, SCIM 2.0, WebAuthn/FIDO2, LDAP, EAP, JWT) e arquitetura de Autenticação Multifator (MFA, Passkeys, TOTP, MFA Resistente a Phishing e Acesso Adaptativo). |
| **cis-controls** | [`skills/security/cis-controls`](skills/security/grc-compliance/cis-controls/SKILL.md) | Atua como especialista nos CIS Critical Security Controls v8/v8.1, CIS Safeguards (IG1, IG2, IG3), CIS Benchmarks de hardening e metodologia de análise de risco CIS RAM. |
| **cryptography-pqc-standards** | [`skills/security/cryptography-pqc-standards`](skills/security/crypto-pki/cryptography-pqc-standards/SKILL.md) | Atua como especialista em engenharia de criptografia, descriptografia, gestão de chaves, criptografia pós-quântica (PQC) e protocolos de criptografia de transporte (TLS 1.3, ECH, mTLS, QUIC, DTLS 1.3, WireGuard, IPsec, SSH e PKI). |
| **csa-cloud-security** | [`skills/security/csa-cloud-security`](skills/security/cloud-iam/csa-cloud-security/SKILL.md) | Atua como especialista em arquitetura e auditoria de nuvem baseada na Cloud Security Alliance (CSA), incluindo a Cloud Controls Matrix (CCM v4), CAIQ v4, STAR Framework (Níveis 1, 2 e 3), CSA Security Guidance v4 e Zero Trust em nuvem. |
| **devsecops-engineer** | [`skills/security/devsecops-engineer`](skills/security/ops-architecture/devsecops-engineer/SKILL.md) | Atua como Engenheiro de DevSecOps, automatizando verificações de segurança no pipeline de CI/CD (SAST, DAST, SCA), gerenciando secrets de forma segura e garantindo a segurança em Cloud e Containers. |
| **game-security-godot** | [`skills/security/game-security-godot`](skills/security/appsec/game-security-godot/SKILL.md) | Atua como especialista em segurança para o motor de jogo Godot Engine, cobrindo proteção de arquivos .pck, criptografia AES, descompilação de GDScript (GDRETools), templates de exportação customizados e segurança de rede. |
| **game-security-unity** | [`skills/security/game-security-unity`](skills/security/appsec/game-security-unity/SKILL.md) | Atua como especialista em segurança para o motor de jogo Unity, cobrindo análise de código C# (Mono vs IL2CPP), engenharia reversa (dnSpy, Il2CppDumper, Ghidra), criptografia de dados, proteção de memória e segurança em rede. |
| **game-security-unreal** | [`skills/security/game-security-unreal`](skills/security/appsec/game-security-unreal/SKILL.md) | Atua como especialista em segurança para o motor de jogo Unreal Engine, cobrindo segurança em replicação de rede (RPCs), proteção de arquivos .pak, desativação de comandos de console, hardening C++ e anti-cheats. |
| **healthtech-standards-security** | [`skills/security/healthtech-standards-security`](skills/security/grc-compliance/healthtech-standards-security/SKILL.md) | Atua como especialista em tecnologias, padrões de interoperabilidade e segurança em saúde (Health Tech), cobrindo HL7 (v2, v3, CDA), FHIR (R4/R5, SMART on FHIR), DICOM & DICOMweb, OMOP CDM, terminologias médicas (SNOMED CT, LOINC, RxNorm, ICD-10/11) e conformidade HIPAA/LGPD/GDPR. |
| **iam-access-aws** | [`skills/security/iam-access-aws`](skills/security/cloud-iam/iam-access-aws/SKILL.md) | Atua como especialista em AWS IAM e controle de acesso, cobrindo IAM Policies (JSON), Permission Boundaries, SCPs (AWS Organizations), AWS IAM Identity Center, STS, ABAC, KMS Key Policies e Access Analyzer. |
| **iam-access-azure** | [`skills/security/iam-access-azure`](skills/security/cloud-iam/iam-access-azure/SKILL.md) | Atua como especialista em Microsoft Entra ID (Azure AD) e Azure IAM, cobrindo Azure RBAC, Custom Roles, PIM (Privileged Identity Management), Conditional Access, Managed Identities, ABAC e Entra ID Governance. |
| **iam-access-gcp** | [`skills/security/iam-access-gcp`](skills/security/cloud-iam/iam-access-gcp/SKILL.md) | Atua como especialista em GCP IAM (Google Cloud Access Management), cobrindo Hierarquia de Recursos, Predefined/Custom Roles, Service Account Impersonation, Workload Identity Federation, VPC Service Controls e IAM Recommender. |
| **iam-access-management** | [`skills/security/iam-access-management`](skills/security/cloud-iam/iam-access-management/SKILL.md) | Atua como especialista em IAM (Identity and Access Management) e gestão de acessos, cobrindo Active Directory, Windows, Linux, AWS, Azure, GCP, OCI e adaptável a ERPs e SaaS como SAP, Salesforce, Okta e ServiceNow. |
| **iam-access-oci** | [`skills/security/iam-access-oci`](skills/security/cloud-iam/iam-access-oci/SKILL.md) | Atua como especialista em OCI IAM (Oracle Cloud Infrastructure Access Management), cobrindo Sintaxe de Políticas OCI, Compartimentos, Domínios de Identidade, Dynamic Groups, Instance Principals e Políticas de Sign-on. |
| **iam-access-power-platform** | [`skills/security/iam-access-power-platform`](skills/security/cloud-iam/iam-access-power-platform/SKILL.md) | Atua como especialista em IAM (Identity and Access Management) do Microsoft Power Platform, Power Apps e Dataverse, cobrindo Security Roles, Privileges, Business Units, Teams (Owner/Access/Group), Column-Level Security, Hierarchy Security, DLP Policies, Environment Roles, Managed Environments e ALM Security. |
| **iso-27000-series** | [`skills/security/iso-27000-series`](skills/security/grc-compliance/iso-27000-series/SKILL.md) | Atua como auditor especialista e arquiteto de SGSI/PIMS especialista em toda a família ISO/IEC 27000, incluindo ISO/IEC 27001:2022, 27002:2022, 27005, 27017, 27018, 27032, 27035, 27036 e ISO/IEC 27701. |
| **memory-manipulation** | [`skills/security/memory-manipulation`](skills/security/appsec/memory-manipulation/SKILL.md) | Atua como especialista em manipulação de memória e segurança de baixo nível, cobrindo alocação dinâmica, gerenciamento de ponteiros, vulnerabilidades (buffer overflows, UAF, double free), técnicas ofensivas (heap grooming, ROP) e mitigações modernas (MTE, CFI, ASan). |
| **network-security-onprem-cloud** | [`skills/security/network-security-onprem-cloud`](skills/security/grc-compliance/network-security-onprem-cloud/SKILL.md) | Atua como especialista em arquitetura, engenharia e operação de segurança de redes (Network Security) abrangendo ambientes On-Premise, Híbridos e Multicloud (AWS, Azure, GCP, OCI), cobrindo NGFW, microsegmentação, SASE/SSE, ZTNA, IDS/IPS, SD-WAN, WAF e mitigação de DDoS. |
| **nist-frameworks-csf** | [`skills/security/nist-frameworks-csf`](skills/security/grc-compliance/nist-frameworks-csf/SKILL.md) | Atua como especialista nos frameworks e publicações especiais do NIST (National Institute of Standards and Technology), incluindo NIST CSF v2.0, SP 800-53 Rev. 5, SP 800-63-3/4, SP 800-30/37 (RMF), SP 800-207 (Zero Trust) e SP 800-171/172. |
| **pci-dss-compliance** | [`skills/security/pci-dss-compliance`](skills/security/grc-compliance/pci-dss-compliance/SKILL.md) | Atua como especialista em conformidade PCI DSS v4.0 (Payment Card Industry Data Security Standard), cobrindo proteção de CHD/SAD, Tokenização, Escopo CDE, Segmentação de Rede, Criptografia, HSMs de Pagamento, QSA, SAQ e Controles de Segurança. |
| **pentest-ai-generative-llm** | [`skills/security/pentest-ai-generative-llm`](skills/security/appsec/pentest-ai-generative-llm/SKILL.md) | Atua como Pentester e Auditor de Segurança especializado em Sistemas de Inteligência Artificial Generativa e LLMs, cobrindo engenharia de prompt adversária, envenenamento de dados de treino (Data Poisoning), vazamento de modelo/dados de treinamento (Model Inversion), extração de sistema e testes de robustez empírica. |
| **pentest-cloud-aws-azure-gcp** | [`skills/security/pentest-cloud-aws-azure-gcp`](skills/security/appsec/pentest-cloud-aws-azure-gcp/SKILL.md) | Atua como Pentester e Red Teamer especializado em Ambientes de Nuvem (AWS, Azure e GCP), cobrindo reconhecimento de ativos expostos, movimentação lateral em contêineres/K8s, exploração de IAM/políticas, ataques a serviços gerenciados (S3, Blob, Key Vault, Metadata Service v1/v2) e simulação de adversários. |
| **pentest-scripter-python-bash-go** | [`skills/security/pentest-scripter-python-bash-go`](skills/security/appsec/pentest-scripter-python-bash-go/SKILL.md) | Atua como Desenvolvedor e Scripter Ofensivo (Red Team Scripter) em Python, Bash e Go (Golang), construindo exploits customizados, shells reversas, ferramentas de evasão de antivírus (AV/EDR), scanners concorrentes, parsers de resultados e scripts de persistência. |
| **pentest-web-application-modern** | [`skills/security/pentest-web-application-modern`](skills/security/appsec/pentest-web-application-modern/SKILL.md) | Atua como Pentester Ético especializado em Aplicações Web Modernas (REST/GraphQL APIs, SPAs, WebSockets, HTTP/2 e Serverless), cobrindo exploração de Host Header Injection, HTTP Response Splitting, Deserialização Insegura, bypass de WAF, Web Shells e escalação de privilégios. |
| **pentester-owasp-api-security-2023** | [`skills/security/pentester-owasp-api-security-2023`](skills/security/appsec/pentester-owasp-api-security-2023/SKILL.md) | Atua como Pentester Ético especializado no OWASP API Security Top 10 2023, auditando APIs REST, GraphQL, SOAP e microsserviços contra falhas de autorização, autenticação, consumo e configuração. |
| **pentester-owasp-wstg** | [`skills/security/pentester-owasp-wstg`](skills/security/appsec/pentester-owasp-wstg/SKILL.md) | Atua como Pentester Ético e Especialista em Testes de Invasão sênior estruturando auditorias sob o framework OWASP WSTG v4.2, correlacionando-as com técnicas MITRE ATT&CK. |
| **pki-digital-signatures** | [`skills/security/pki-digital-signatures`](skills/security/crypto-pki/pki-digital-signatures/SKILL.md) | Subskill especializada em Infraestrutura de Chaves Públicas (PKI), Certificados Digitais X.509v3, Padrões de Assinatura Digital (CAdES, XAdES, PAdES, JAdES, eIDAS, ICP-Brasil) e Ferramentas Práticas (OpenSSL, Smallstep step-cli, HashiCorp Vault PKI, Cert-Manager, Cosign/Sigstore, YubiKey/PKCS#11). |
| **sast-code-review** | [`skills/security/sast-code-review`](skills/security/appsec/sast-code-review/SKILL.md) | Atua como especialista em Análise Estática de Segurança de Aplicações (SAST) e Revisão de Código de Segurança (Security Code Review), identificando vulnerabilidades no código-fonte, aplicando regras de verificação estática, remediando falhas (Injection, XSS, CSRF, Insecure Deserialization, Broken Access Control) e estabelecendo padrões de revisão automatizada e manual. |
| **sca-dependency-analysis** | [`skills/security/sca-dependency-analysis`](skills/security/appsec/sca-dependency-analysis/SKILL.md) | Atua como especialista em Análise de Composição de Software (SCA) e Gestão de Dependências de Terceiros, identificando vulnerabilidades conhecidas (CVEs), gerando e analisando Software Bill of Materials (SBOM - CycloneDX/SPDX), auditando licenças de código aberto e gerenciando riscos na cadeia de suprimentos de software (Supply Chain Security). |
| **secops-incident-responder** | [`skills/security/secops-incident-responder`](skills/security/ops-architecture/secops-incident-responder/SKILL.md) | Atua como Analista de SecOps e Resposta a Incidentes, estruturando playbooks de resposta a ataques (NIST SP 800-61), monitoramento operacional (SIEM), hardening de ambientes de produção e planos de Disaster Recovery. |
| **security-architect-sabsa** | [`skills/security/security-architect-sabsa`](skills/security/ops-architecture/security-architect-sabsa/SKILL.md) | Atua como Arquiteto de Segurança de Sistemas usando o framework SABSA alinhado ao TOGAF, NIST CSF, ISO 27001 e Zero Trust, executando a Matriz SABSA 6x6, Perfis de Atributos de Negócio (BAP), Domínios de Confiança e o Ciclo de Vida SABSA (Strategy, Design, Implement, Manage & Measure). |
| **security-champions** | [`skills/security/security-champions`](skills/security/ops-architecture/security-champions/SKILL.md) | Atua como Security Champion da equipe de engenharia, disseminando práticas seguras, triando riscos e delegando demandas para as skills especializadas de segurança quando necessário. |
| **security-grc-compliance** | [`skills/security/security-grc-compliance`](skills/security/grc-compliance/security-grc-compliance/SKILL.md) | Atua como Analista de Governança, Riscos e Conformidade (GRC), estruturando políticas de segurança, alinhando frameworks (ISO 27001, PCI-DSS, LGPD/GDPR) e medindo a eficácia de segurança com métricas organizacionais. |
| **security-manager-samm** | [`skills/security/security-manager-samm`](skills/security/grc-compliance/security-manager-samm/SKILL.md) | Atua como Gestor de Segurança usando o framework OWASP SAMM alinhado ao BSIMM e CIS Controls para governar, avaliar e elevar a maturidade de segurança do SDLC, gerindo regras e criando novas skills. |
| **security-privacy** | [`skills/security/security-privacy`](skills/security/grc-compliance/security-privacy/SKILL.md) | Atua como Especialista em Privacidade de Dados, orientando o design, a implementação e a auditoria de sistemas em conformidade com leis (LGPD, GDPR), frameworks (NIST Privacy Framework, Privacy by Design) e padrões internacionais (ISO/IEC 27701). |
| **threat-modeler** | [`skills/security/threat-modeler`](skills/security/ops-architecture/threat-modeler/SKILL.md) | Atua como Especialista em Modelagem de Ameaças (Threat Modeling), utilizando frameworks como STRIDE, PASTA e LINDDUN para antecipar ataques, identificar riscos e especificar requisitos de segurança. |

### 🔤 Linguagens de Programação e Marcação (Languages)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **lang-bash** | [`skills/languages/lang-bash`](skills/languages/lang-bash/SKILL.md) | Fornece padrões de engenharia de software em Bash/Shell Scripting. Cobre execução estrita e segura (set -euo pipefail), manipulação defensiva de variáveis e aspas, funções modulares, verificação de dependências, manipulação de arquivos/redirecionamento, além de integração com ShellCheck e boas práticas de portabilidade. |
| **lang-c** | [`skills/languages/lang-c`](skills/languages/lang-c/SKILL.md) | Fornece padrões de engenharia de software em C moderno baseados na norma internacional ISO/IEC 9899 (com foco em C23 - ISO/IEC 9899:2024, C17, C11 e C99) e nas referências de en.cppreference.com/w/c, cobrindo novas palavras-chave (nullptr, bool, constexpr), atributos ([[nodiscard]], [[deprecated]]), matemática segura (<stdckdint.h>), operações de bits (<stdbit.h>), depuração de memória e CMake. |
| **lang-cpp** | [`skills/languages/lang-cpp`](skills/languages/lang-cpp/SKILL.md) | Fornece padrões de engenharia de software em C++ moderno baseados na norma internacional ISO/IEC 14882 (com foco em C++23 - ISO/IEC 14882:2024, C++20, C++17 e C++14) e na documentação do en.cppreference.com, cobrindo RAII, Smart Pointers, Concepts, Modules, Coroutines, std::expected, std::print, Ranges, CMake e C++ Core Guidelines. |
| **lang-go** | [`skills/languages/lang-go`](skills/languages/lang-go/SKILL.md) | Fornece padrões de engenharia de software em Go (Golang) baseados na documentação oficial (go.dev/doc), Effective Go, Go Memory Model e boas práticas de concorrência (goroutines, channels, context), tratamento de erros, genéricos, módulos e testes. |
| **lang-latex** | [`skills/languages/lang-latex`](skills/languages/lang-latex/SKILL.md) | Fornece padrões de engenharia e tipografia acadêmica/científica em LaTeX (LaTeX2e e LuaLaTeX/XeLaTeX). Cobre estruturação modular de documentos multinível, gestão de bibliografia com BibLaTeX/Biber, ilustrações com TikZ, formatação matemática rigorosa (amsmath/mathtools), comandos customizados (newcommand/ProvideDocumentCommand) e prevenção de erros comuns de compilação. |
| **lang-lua** | [`skills/languages/lang-lua`](skills/languages/lang-lua/SKILL.md) | Fornece padrões de engenharia de software em Lua. Cobre o uso de local variables, manipulação eficiente de tabelas, metamétodos/metatables, closures, concorrência cooperativa com coroutines, otimização de performance e integração com C/C++ usando a API nativa ou LuaJIT FFI. |
| **lang-markdown** | [`skills/languages/lang-markdown`](skills/languages/lang-markdown/SKILL.md) | Fornece diretrizes completas de autorização, engenharia e formatação em Markdown (CommonMark, GitHub Flavored Markdown - GFM e MDX). Cobre estruturação hierárquica de documentos, formatação avançada de código e tabelas, elementos visuais (alertas GFM, diagramas Mermaid), equações matemáticas em LaTeX, padrões de linting (MarkdownLint), documentação técnica (READMEs, ADRs, Changelogs) e integração com JSX/MDX. |
| **lang-perl** | [`skills/languages/lang-perl`](skills/languages/lang-perl/SKILL.md) | Fornece padrões de engenharia de software em Perl moderno (Perl 5.30+). Cobre uso estrito de pragmas (use strict; use warnings; use utf8;), subrotinas com assinaturas (signatures), Orientação a Objetos moderna (Moo/MooX ou Perl 5.38+ builtin class), expressões regulares defensivas, manipulação segura de arquivos com lexically scoped filehandles e boas práticas CPAN. |
| **lang-powershell** | [`skills/languages/lang-powershell`](skills/languages/lang-powershell/SKILL.md) | Fornece padrões de engenharia de software em PowerShell (Windows PowerShell 5.1 e PowerShell 7+ Core). Cobre automação, gestão de pipeline de objetos, modularização (módulos de script/manifestos), tratamento de erros defensivo (Try/Catch/Finally, ErrorActionPreference), tipagem forte, PSCustomObject e boas práticas de segurança (ExecutionPolicy, remoting e credenciais). |
| **lang-python** | [`skills/languages/lang-python`](skills/languages/lang-python/SKILL.md) | Fornece padrões de engenharia de software em Python, cobrindo estilo de código, tipagem, estruturas de projeto, frameworks populares como Django, Flask e FastAPI, além de boas práticas para testes, packaging e operação. |
| **lang-rust** | [`skills/languages/lang-rust`](skills/languages/lang-rust/SKILL.md) | Fornece padrões de engenharia de software em Rust baseados na documentação oficial (doc.rust-lang.org), cobrindo Ownership, Borrowing, Lifetimes, Traits, Concorrência, Async (Tokio), tratamento de erros (Result/Option), Unsafe Rust e ecossistema Cargo. |
| **lang-typescript** | [`skills/languages/lang-typescript`](skills/languages/lang-typescript/SKILL.md) | Fornece padrões de engenharia de software seguro e robusto usando TypeScript, cobrindo generics, tipos avançados, segurança estrita de compilador e mapeamento defensivo de dados. |
| **lang-typst** | [`skills/languages/lang-typst`](skills/languages/lang-typst/SKILL.md) | Fornece padrões de engenharia e tipografia digital moderna usando Typst. Cobre sintaxe de marcação, funções customizadas, criação de templates reutilizáveis, regras de exibição (show/set rules), matemática avançada, tabelas, layout de páginas e bibliografia via Hayagriva/BibTeX. |

### 🗄️ Bancos de Dados e Persistência (Databases)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **db-mariadb** | [`skills/general/databases/db-mariadb`](skills/general/databases/db-mariadb/SKILL.md) | Fornece padrões de administração e engenharia para MariaDB baseados na documentação oficial (mariadb.com/docs). Cobre motores de armazenamento (InnoDB, Aria, ColumnStore, MyRocks), tunagem do InnoDB Buffer Pool, Galera Cluster, MariaDB MaxScale, Mariabackup e otimização EXPLAIN FORMAT=JSON. |
| **db-mongodb** | [`skills/general/databases/db-mongodb`](skills/general/databases/db-mongodb/SKILL.md) | Fornece padrões de administração e engenharia para MongoDB baseados na documentação oficial em português (mongodb.com/pt-br/docs). Cobre modelagem de documentos (Embedding vs Referencing), motor WiredTiger, Read/Write Concern, índices (Compound, Multikey, Text, TTL, 2dsphere), Aggregation Framework e Sharded Clusters. |
| **db-postgresql** | [`skills/general/databases/db-postgresql`](skills/general/databases/db-postgresql/SKILL.md) | Fornece padrões de administração e engenharia para PostgreSQL baseados na documentação oficial (postgresql.org/docs). Cobre arquitetura MVCC, tunagem de Autovacuum, tipos avançados (JSONB, PostGIS), estratégia de índices (B-Tree, GIN, GiST, BRIN), análise EXPLAIN ANALYZE BUFFERS, replicação e PgBouncer. |
| **db-sqlite** | [`skills/general/databases/db-sqlite`](skills/general/databases/db-sqlite/SKILL.md) | Fornece padrões de engenharia e otimização para SQLite baseados na documentação oficial (sqlite.org/docs.html). Cobre arquitetura Serverless, modo WAL (Write-Ahead Logging), pragmas de desempenho, índices cobridores e parciais, FTS5, JSON1 e extensão WITHOUT ROWID. |

### 🧱 Frameworks e Ferramentas (Framework)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **framework-criterion** | [`skills/framework/framework-criterion`](skills/framework/framework-criterion/SKILL.md) | Atua como Especialista em testes unitários para a linguagem C utilizando Criterion, cobrindo macros Test, cr_assert/cr_expect, ciclos de vida (.init/.fini), teste de sinais/crashes, captura de stdout/stderr e integração com CMake. |
| **framework-graphql** | [`skills/framework/framework-graphql`](skills/framework/framework-graphql/SKILL.md) | Fornece padrões de engenharia e design de APIs baseados na especificação oficial GraphQL (GraphQL Foundation), cobrindo SDL, Queries, Mutations, Subscriptions, resolvedores, DataLoader, paginação Relay, formato de resposta e erros, e segurança de queries. |
| **framework-grpc** | [`skills/framework/framework-grpc`](skills/framework/framework-grpc/SKILL.md) | Fornece padrões de engenharia para gRPC e Protocol Buffers (proto3), cobrindo RPCs unários e de streaming (Server, Client, Bidirectional), definição de arquivos .proto, transporte HTTP/2, interceptores e tratamento de erros. |
| **framework-jest** | [`skills/framework/framework-jest`](skills/framework/framework-jest/SKILL.md) | Atua como Especialista em testes automatizados com Jest no ecossistema JavaScript e TypeScript, cobrindo Mocks, Spies, Snapshots, testes assíncronos, fake timers e suporte ao Node.js e React. |
| **framework-mocha** | [`skills/framework/framework-mocha`](skills/framework/framework-mocha/SKILL.md) | Atua como Especialista em testes automatizados com Mocha em JavaScript e Node.js, cobrindo interfaces BDD/TDD, integração com Chai (expect/assert) e Sinon.js (Spies, Stubs, Mocks) e testes assíncronos. |
| **framework-nose2** | [`skills/framework/framework-nose2`](skills/framework/framework-nose2/SKILL.md) | Atua como Especialista em testes automatizados com Nose2 em Python, cobrindo configuração via unittest.cfg, plugins de cobertura e multiprocessamento, parametrização com @params e suítes dinâmicas. |
| **framework-pytest** | [`skills/framework/framework-pytest`](skills/framework/framework-pytest/SKILL.md) | Atua como Especialista em testes automatizados com o framework pytest em Python, cobrindo fixturas dinâmicas, parametrização (@pytest.mark.parametrize), plugins (pytest-asyncio, pytest-cov, pytest-mock, pytest-xdist), asserções e estrutura de testes. |
| **framework-react** | [`skills/framework/framework-react`](skills/framework/framework-react/SKILL.md) | Fornece padrões de engenharia e arquitetura para React (React 18/19), cobrindo componentes funcionais, Hooks avançados, Server Components (RSC), gerenciamento de estado (Context, Zustand, TanStack Query), roteamento e performance. |
| **framework-rest-api** | [`skills/framework/framework-rest-api`](skills/framework/framework-rest-api/SKILL.md) | Fornece padrões de engenharia e design para APIs RESTful baseados na especificação OpenAPI 3.1 e RFCs. Cobre semântica HTTP, status codes, padronização de erros RFC 7807, paginação, HATEOAS, rate limiting e OAuth2/JWT. |
| **framework-soap** | [`skills/framework/framework-soap`](skills/framework/framework-soap/SKILL.md) | Fornece padrões de engenharia e integração de serviços web baseados nos padrões W3C SOAP 1.1/1.2 e WSDL 1.1/2.0, cobrindo Envelope XML, segurança de mensagens WS-Security (WSS), assinatura XML-Signature e XSD. |
| **framework-testing** | [`skills/framework/framework-testing`](skills/framework/framework-testing/SKILL.md) | Fornece padrões de arquitetura de testes de software, cobrindo Pirâmide de Testes, TDD, BDD, testes unitários, de integração, E2E, estresse/carga, mocks/stubs e métricas de cobertura de código. |
| **framework-unittest** | [`skills/framework/framework-unittest`](skills/framework/framework-unittest/SKILL.md) | Atua como Especialista em testes automatizados com a biblioteca nativa unittest do Python, cobrindo TestCase, asserções, métodos de ciclo de vida (setUp/tearDown), subtests, unittest.mock (@patch, MagicMock) e test discovery. |
| **framework-vue** | [`skills/framework/framework-vue`](skills/framework/framework-vue/SKILL.md) | Fornece padrões de desenvolvimento modular e de alta performance usando o ecossistema Vue 3, cobrindo Composition API, TypeScript, Pinia, Vue Router e otimizações de reatividade. |
| **framework-ward** | [`skills/framework/framework-ward`](skills/framework/framework-ward/SKILL.md) | Atua como Especialista em testes automatizados com o framework Ward em Python, cobrindo testes declarativos com @test, injeção de dependências por @fixture, asserções com expect() e testes assíncronos. |
| **protocol-http** | [`skills/framework/protocol-http`](skills/framework/protocol-http/SKILL.md) | Fornece padrões de arquitetura e engenharia do protocolo HTTP (HTTP/1.1, HTTP/2, HTTP/3 e RFC 10008). Cobre semântica completa de verbos incluindo QUERY, status codes, negociação de conteúdo, cabeçalhos de segurança, CORS e estratégias de caching. |

### 🖥️ Programas e Softwares (Programs)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **agy-customizations** | [`skills/programs/agy-customizations`](skills/programs/agy-customizations/SKILL.md) | Guia completo e referência oficial do Sistema de Customização do Antigravity, cobrindo Skills, Rules, Plugins, Hooks, servidores MCP, precedência de carregamento e governança. |
| **antigravity-guide** | [`skills/programs/antigravity-guide`](skills/programs/antigravity-guide/SKILL.md) | Guia abrangente, referência rápida e mapa do ecossistema Google Antigravity (AGY CLI, IDE, Antigravity 2.0, Python SDK, slash commands, atalhos de teclado e customizações). |
| **gemini-enterprise** | [`skills/programs/gemini-enterprise`](skills/programs/gemini-enterprise/SKILL.md) | Atua como especialista em Google Gemini Enterprise, cobrindo integração com Google Workspace, Gemini Code Assist Enterprise, Vertex AI Search & Agents, governança de dados, privacidade corporativa, extensões e customização. |
| **power-automate** | [`skills/programs/power-automate`](skills/programs/power-automate/SKILL.md) | Atua como especialista em Microsoft Power Automate, cobrindo Cloud Flows (Automated, Instant, Scheduled), Desktop Flows (RPA), Process Mining, AI Builder, conectores personalizados e arquitetura de governança/DLP. |
| **power-bi** | [`skills/programs/power-bi`](skills/programs/power-bi/SKILL.md) | Atua como especialista em Microsoft Power BI e Microsoft Fabric, cobrindo modelagem dimensional (Star Schema), linguagem DAX avançada, Power Query (M), RLS/OLS, Dataflows/Datamarts e otimização de performance. |
| **program-cheat-engine** | [`skills/programs/program-cheat-engine`](skills/programs/program-cheat-engine/SKILL.md) | Especialista em desenvolvimento de scripts Auto Assembler e Lua para Cheat Engine 7.5 e 7.7. Fornece padrões de injeção de código, manipulação de memória e técnicas de conversão e compatibilidade de scripts entre as versões 7.5 e 7.7. |
| **program-containers** | [`skills/programs/containers`](skills/programs/containers/SKILL.md) | Especialista em tecnologias de containers (Docker, Podman, CRI-O, Buildah, Kubernetes), padrões OCI, registries seguros, hardening e orquestração gerenciada/serverless em nuvem. |
| **program-github** | [`skills/programs/github`](skills/programs/github/SKILL.md) | Atua como especialista na plataforma GitHub, cobrindo repositórios, branching strategies, Pull Requests, Issues, Projects v2, Packages (GHCR), Codespaces, segurança avançada (Dependabot, CodeQL, Secret Scanning), CLI (`gh`), API REST/GraphQL e GitHub Pages. |
| **program-github-actions** | [`skills/programs/github-actions`](skills/programs/github-actions/SKILL.md) | Atua como especialista em GitHub Actions e CI/CD, cobrindo workflows, reusable workflows, composite actions, matrix strategies, environments, OIDC, caching, container jobs e padrões avançados de automação. |
| **program-moodle** | [`skills/programs/moodle`](skills/programs/moodle/SKILL.md) | Atua como especialista sênior em desenvolvimento e customização do Moodle LMS, cobrindo arquitetura de plugins (Frankenstyle), APIs principais (DB, Form, Page, Output), controle de acessos, Web Services, Hooks modernos e API de privacidade. |
| **program-moodle-dba** | [`skills/programs/moodle-dba`](skills/programs/moodle-dba/SKILL.md) | Atua como Administrador de Banco de Dados (DBA) sênior especialista em Moodle LMS, cobrindo modelagem XMLDB, otimização de consultas (EXPLAIN), indexação segura, transações delegadas, particionamento de logs e tuning de MySQL e PostgreSQL. |
| **program-moodle-design** | [`skills/programs/moodle-design`](skills/programs/moodle-design/SKILL.md) | Atua como especialista em design de interfaces (UI), desenvolvimento de temas, templates Mustache, estilização SCSS, customização de formatos de curso e otimização de UX/acessibilidade no Moodle LMS. |
| **program-moodle-infra** | [`skills/programs/moodle-infra`](skills/programs/moodle-infra/SKILL.md) | Atua como especialista em infraestrutura, dimensionamento, alta disponibilidade, performance tuning (OPcache, PHP, MySQL/Postgres), MUC (Redis/Memcached), cron em lote e armazenamento distribuído no Moodle LMS. |
| **program-moodle-plugins** | [`skills/programs/moodle-plugins`](skills/programs/moodle-plugins/SKILL.md) | Atua como especialista no ciclo de vida, anatomia, configurações administrativas (settings.php), rotinas de backup/restauração, testes e publicação de plugins para o Moodle LMS. |


### 🧩 Padrões de Projeto (Design Patterns - GoF)
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **dp-abstract-factory** | [`skills/patterns/dp-abstract-factory`](skills/patterns/creational/dp-abstract-factory/SKILL.md) | Padrão de Projeto Criacional: Permite produzir famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. |
| **dp-adapter** | [`skills/patterns/dp-adapter`](skills/patterns/structural/dp-adapter/SKILL.md) | Padrão de Projeto Estrutural: Permite que objetos com interfaces incompatíveis colaborem entre si. |
| **dp-bridge** | [`skills/patterns/dp-bridge`](skills/patterns/structural/dp-bridge/SKILL.md) | Padrão de Projeto Estrutural: Divide uma classe grande ou um conjunto de classes intimamente ligadas em duas hierarquias separadas — abstração e implementação — que podem ser desenvolvidas independentemente. |
| **dp-builder** | [`skills/patterns/dp-builder`](skills/patterns/creational/dp-builder/SKILL.md) | Padrão de Projeto Criacional: Permite construir objetos complexos passo a passo. Permite produzir diferentes tipos e representações de um objeto usando o mesmo código de construção. |
| **dp-chain-of-responsibility** | [`skills/patterns/dp-chain-of-responsibility`](skills/patterns/behavioral/dp-chain-of-responsibility/SKILL.md) | Padrão de Projeto Comportamental: Permite passar requisições por uma corrente de manipuladores. Ao receber uma requisição, cada manipulador decide se processa a requisição ou a passa para o próximo manipulador. |
| **dp-command** | [`skills/patterns/dp-command`](skills/patterns/behavioral/dp-command/SKILL.md) | Padrão de Projeto Comportamental: Transforma uma solicitação em um objeto independente que contém toda a informação sobre a solicitação, permitindo parametrizar, enfileirar ou desfazer operações. |
| **dp-composite** | [`skills/patterns/dp-composite`](skills/patterns/structural/dp-composite/SKILL.md) | Padrão de Projeto Estrutural: Permite compor objetos em estruturas de árvore e trabalhar com essas estruturas como se fossem objetos individuais. |
| **dp-decorator** | [`skills/patterns/dp-decorator`](skills/patterns/structural/dp-decorator/SKILL.md) | Padrão de Projeto Estrutural: Permite acoplar novos comportamentos a objetos ao colocá-los dentro de invólucros (wrappers) de objetos reais. |
| **dp-facade** | [`skills/patterns/dp-facade`](skills/patterns/structural/dp-facade/SKILL.md) | Padrão de Projeto Estrutural: Fornece uma interface simplificada para uma biblioteca, um framework, ou qualquer outro conjunto complexo de classes. |
| **dp-factory-method** | [`skills/patterns/dp-factory-method`](skills/patterns/creational/dp-factory-method/SKILL.md) | Padrão de Projeto Criacional: Fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. |
| **dp-flyweight** | [`skills/patterns/dp-flyweight`](skills/patterns/structural/dp-flyweight/SKILL.md) | Padrão de Projeto Estrutural: Permite ajustar mais objetos na quantidade disponível de RAM ao compartilhar partes comuns de estado entre múltiplos objetos em vez de manter todos os dados em cada objeto. |
| **dp-iterator** | [`skills/patterns/dp-iterator`](skills/patterns/behavioral/dp-iterator/SKILL.md) | Padrão de Projeto Comportamental: Permite percorrer elementos de uma coleção sem expor sua representação subjacente (lista, pilha, árvore, etc.). |
| **dp-mediator** | [`skills/patterns/dp-mediator`](skills/patterns/behavioral/dp-mediator/SKILL.md) | Padrão de Projeto Comportamental: Reduz as dependências caóticas entre objetos. Restringe comunicações diretas entre objetos e os força a colaborar apenas através de um objeto mediador. |
| **dp-memento** | [`skills/patterns/dp-memento`](skills/patterns/behavioral/dp-memento/SKILL.md) | Padrão de Projeto Comportamental: Permite salvar e restaurar o estado anterior de um objeto sem revelar os detalhes de sua implementação. |
| **dp-observer** | [`skills/patterns/dp-observer`](skills/patterns/behavioral/dp-observer/SKILL.md) | Padrão de Projeto Comportamental: Permite definir um mecanismo de assinatura para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando. |
| **dp-prototype** | [`skills/patterns/dp-prototype`](skills/patterns/creational/dp-prototype/SKILL.md) | Padrão de Projeto Criacional: Permite copiar objetos existentes sem tornar seu código dependente de suas classes. |
| **dp-proxy** | [`skills/patterns/dp-proxy`](skills/patterns/structural/dp-proxy/SKILL.md) | Padrão de Projeto Estrutural: Fornece um substituto ou um espaço reservado para outro objeto. Um proxy controla o acesso ao objeto original, permitindo fazer algo antes ou depois que a requisição chegue a ele. |
| **dp-singleton** | [`skills/patterns/dp-singleton`](skills/patterns/creational/dp-singleton/SKILL.md) | Padrão de Projeto Criacional: Garante que uma classe tenha apenas uma instância, enquanto provê um ponto de acesso global para essa instância. |
| **dp-state** | [`skills/patterns/dp-state`](skills/patterns/behavioral/dp-state/SKILL.md) | Padrão de Projeto Comportamental: Permite que um objeto altere seu comportamento quando seu estado interno muda. O objeto parecerá ter mudado de classe. |
| **dp-strategy** | [`skills/patterns/dp-strategy`](skills/patterns/behavioral/dp-strategy/SKILL.md) | Padrão de Projeto Comportamental: Define uma família de algoritmos, coloca cada um deles em uma classe separada, e faz seus objetos intercambiáveis. |
| **dp-template-method** | [`skills/patterns/dp-template-method`](skills/patterns/behavioral/dp-template-method/SKILL.md) | Padrão de Projeto Comportamental: Define o esqueleto de um algoritmo na superclasse mas deixa as subclasses sobrescreverem etapas específicas do algoritmo sem modificar sua estrutura. |
| **dp-visitor** | [`skills/patterns/dp-visitor`](skills/patterns/behavioral/dp-visitor/SKILL.md) | Padrão de Projeto Comportamental: Permite separar algoritmos dos objetos nos quais eles operam. |

### ⚙️ Auxiliares e Templates
| Habilidade | Caminho da Skill | Descrição / Caso de Uso |
| :--- | :--- | :--- |
| **documentation-designer** | [`skills/general/documentation-designer`](skills/general/engineering-practices/documentation-designer/SKILL.md) | Auxilia na elaboração de documentação técnica rica e no desenho de diagramas estruturais, de dados, estratégicos e técnicos utilizando toda a sintaxe do Mermaid.js. |
| **template-skill** | [`skills/general/template-skill`](skills/general/engineering-practices/template-skill/SKILL.md) | Um template básico que demonstra como estruturar uma habilidade (skill) personalizada para agentes de IA. |

### 🛠️ Scripts Utilitários
- **`scripts/pdf_to_markdown.py`**: Converte livros e documentos PDF de referência para arquivos Markdown (`.md`) estruturados, preservando sumários (TOC), marcadores de páginas e blocos de código para auxiliar a IA na criação de novas skills.
  - Exemplo: `python scripts/pdf_to_markdown.py "caminho/para/livro.pdf"`
  - Exemplo TOC: `python scripts/pdf_to_markdown.py "caminho/para/livro.pdf" --toc-only`
  - Exemplo Pasta: `python scripts/pdf_to_markdown.py --dir "caminho/para/pasta_pdfs"`

## Licença

Este repositório está sob a licença [GPLv3](LICENSE). Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.


