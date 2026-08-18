---
name: "iam-access-power-platform"
description: "Atua como especialista em IAM (Identity and Access Management) do Microsoft Power Platform, Power Apps e Dataverse, cobrindo Security Roles, Privileges, Business Units, Teams (Owner/Access/Group), Column-Level Security, Hierarchy Security, DLP Policies, Environment Roles, Managed Environments e ALM Security."
metadata:
  mitre:
  - T1078
  - T1098
  phase: actions
  tools:
  - power-platform-admin-center
  - pac-cli
  - dataverse-web-api
  type: defensive
---
# Habilidade de IA: Especialista em Gestão de Acessos e IAM no Microsoft Power Platform, Power Apps e Dataverse

Esta skill orienta a inteligência artificial a agir como um **Especialista em Gestão de Identidades e Controle de Acesso (IAM) no Microsoft Power Platform, Power Apps e Dataverse**, fornecendo arquitetura de segurança multi-camada, governança de privilégios, modelagem de Business Units e Teams, proteção em nível de coluna, políticas DLP e segurança para pipelines de ALM.

---

## 🏛️ 1. Arquitetura Multi-Camada de Segurança no Power Platform

A segurança no Microsoft Power Platform é estruturada em uma defesa em profundidade (*Defense in Depth*) dividida em 5 níveis hierárquicos:

```text
+-----------------------------------------------------------------------+
| 1. Tenant Level (Microsoft Entra ID, Licenciamento, Conditional Access)|
+-----------------------------------------------------------------------+
                                  |
                                  v
+-----------------------------------------------------------------------+
| 2. Environment Level (Environment Admin, Maker, SysAdmin, IP Firewall)|
+-----------------------------------------------------------------------+
                                  |
                                  v
+-----------------------------------------------------------------------+
| 3. Dataverse Level (RBAC: Business Units, Teams, Security Roles)      |
+-----------------------------------------------------------------------+
                                  |
                                  v
+-----------------------------------------------------------------------+
| 4. Record Level (Ownership, Access Levels, POA Table & Sharing)       |
+-----------------------------------------------------------------------+
                                  |
                                  v
+-----------------------------------------------------------------------+
| 5. Column Level (Column Security Profiles / Field-Level Security)     |
+-----------------------------------------------------------------------+
```

### Funções Nativas do Ambiente (Environment Roles)
- **Environment Admin**: Permissão total de administração do ambiente (criar recursos, gerenciar usuários, aplicar DLP), mas não concede acesso automático aos dados do Dataverse a menos que a função `System Administrator` seja atribuída.
- **Environment Maker**: Permissão para criar novos recursos (Canvas Apps, Model-Driven Apps, Power Automate Flows, Custom Connectors), mas sem acesso aos dados de outros usuários.
- **System Administrator**: Acesso total de leitura, escrita, customização e administração de todos os dados e tabelas do Dataverse no ambiente.
- **System Customizer**: Permissões para customizar tabelas, formulários e fluxos, mas com acesso limitado a dados de negócios em comparação ao `System Administrator`.

---

## 🛡️ 2. Modelo de Segurança do Dataverse: Funções, Privilégios e Escopos

O Dataverse utiliza um modelo de **Controle de Acesso Baseado em Funções (RBAC)** altamente granular.

### Matriz de Privilégios por Tabela (Record-Level Privileges)

Para cada tabela no Dataverse, 8 privilégios fundamentais podem ser configurados:

| Privilégio | Descrição Técnica |
| :--- | :--- |
| **Create** | Permissão para instanciar novos registros na tabela. |
| **Read** | Permissão para consultar e visualizar o conteúdo do registro. |
| **Write** | Permissão para atualizar e modificar atributos de um registro existente. |
| **Delete** | Permissão para remover permanentemente um registro. |
| **Append** | Permissão para associar o registro atual a outro registro pai (anexar registro filho). |
| **Append To** | Permissão para permitir que outros registros filhos sejam anexados ao registro atual. |
| **Assign** | Permissão para transferir a propriedade (*Ownership*) de um registro para outro usuário/equipe. |
| **Share** | Permissão para conceder acesso visual ou de escrita de um registro a outro usuário mantendo a propriedade. |

> **Nota sobre Append / Append To**: Para criar um relacionamento entre dois registros (ex: adicionar uma Nota a uma Conta), o usuário deve ter privilégio `Append` na Nota e privilégio `Append To` na Conta.

---

### Níveis de Acesso / Escopos de Profundidade (Access Levels)

Os privilégios são associados a níveis de escopo que determinam o alcance da permissão na árvore organizacional:

```text
[ Global / Organization ] ──> Acesso a todos os registros do ambiente.
        |
        v
[ Deep / Parent: Child BUs ] ──> Acesso na BU do usuário e em todas as BUs filhas subordinadas.
        |
        v
[ Local / Business Unit ] ──> Acesso estrito aos registros mantidos na mesma BU do usuário.
        |
        v
[ Basic / User ] ──> Acesso exclusivo a registros pertencentes ao usuário ou compartilhados com ele/suas equipes.
        |
        v
[ None ] ──> Nenhum acesso permitido.
```

---

### Herança de Privilégios em Equipes (Member's Privilege Inheritance)

Ao atribuir um Security Role a um usuário ou equipe, configura-se a forma de herança:

- **Direct User (Basic) access level and Team privileges (Padrão)**: O usuário recebe os privilégios diretamente + privilégios das equipes das quais é membro. Pode criar registros em seu próprio nome.
- **Team privileges only**: O usuário obtém privilégios **apenas** quando atua como membro de uma equipe. Impede a criação de registros em nome individual se não houver privilégio direto de usuário. Ideal para segregação estrita de funções (*SoD - Segregation of Duties*).

---

## 🏢 3. Business Units (BUs) e Arquitetura de Equipes (Teams)

### Hierarquia de Business Units
- **Root Business Unit**: Criada automaticamente com o ambiente. Não pode ser desativada nem excluída.
- **Child Business Units**: Subestruturas organizacionais criadas para segregar dados por departamento, região geográfica ou unidade de negócios.
- **Matrix Business Units / Modern Hierarchy**: Suporte ao acesso de dados em múltiplas BUs sem necessidade de mover a conta do usuário de sua BU principal.

---

### Tipos de Equipes no Dataverse (Teams Architecture)

1. **Owner Teams (Equipes Proprietárias)**:
   - Podem ser proprietárias de registros diretamente (`OwnerId`).
   - Possuem Security Roles associadas. Qualquer registro pertencente à Owner Team fica acessível a todos os seus membros de acordo com as funções da equipe.

2. **Access Teams (Equipes de Acesso)**:
   - **Não possuem registros próprios** e **não possuem Security Roles diretas**.
   - Utilizadas para compartilhamento dinâmico e temporário de registros individuais utilizando *Access Team Templates*.
   - Evitam o inchaço da tabela de segurança `PrincipalObjectAccess` (POA).

3. **Group Teams (Microsoft Entra ID Group Teams)**:
   - **Entra ID Security Groups** ou **Microsoft 365 Groups** vinculados a Security Roles do Dataverse.
   - **Provisionamento JIT (Just-In-Time)**: Quando um usuário entra no grupo do Entra ID, ele ganha acesso automático aos recursos do Dataverse sem necessidade de gerenciamento manual de papéis no Power Platform Admin Center.

```text
Entra ID Security Group ──(Sincronização Automática)──> Dataverse Group Team ──(Security Role)──> Acesso ao Dataverse
```

---

## 🔒 4. Column-Level Security e Hierarchy Security

### Column-Level Security (Perfil de Segurança de Colunas / FLS)
Quando privilégios em nível de tabela não são suficientes para proteger atributos sensíveis (ex: Salário, CPF, Dados Médicos):

1. Ativa-se a propriedade **IsSecured** no campo/coluna da tabela no Dataverse.
2. Cria-se um **Column Security Profile**.
3. Define-se permissões explícitas de **Create**, **Read** e **Update** para o campo.
4. Atribui-se o perfil a Usuários ou Group Teams.

```text
Tabela: Funcionário
 ├── Nome (Acesso padrão via Security Role)
 ├── Cargo (Acesso padrão via Security Role)
 └── Salário [IsSecured = True] ──> Column Security Profile (Permissão de Leitura exclusiva do RH)
```

---

### Hierarchy Security (Segurança por Hierarquia)

Estende o modelo de acesso baseado na estrutura de liderança ou cargos organizacionais:

- **Manager Hierarchy**: Utiliza o campo `ParentSystemUserId` (Gerente). Um gerente obtém acesso de leitura/escrita aos registros de seus subordinados diretos e acesso de leitura estendido aos subordinados indiretos até a profundidade configurada.
- **Position Hierarchy**: Define estruturas de cargos (*Positions*) independentes do organograma de gerenciamento direto.

---

## ⚡ 5. Gerenciamento da Tabela PrincipalObjectAccess (POA) e Performance

A tabela **POA (PrincipalObjectAccess)** armazena instâncias de compartilhamento explícito e implícito de registros.

### Cuidados e Mitigação de Inchaço (POA Bloat)
- **Problema**: O uso excessivo do privilégio `Share` em milhões de registros individuais faz a tabela POA crescer exponencialmente, degradando a performance de consultas SQL subjacentes.
- **Boas Práticas de IAM no Dataverse**:
  - Evitar compartilhamento registro a registro via código ou fluxo manual.
  - Substituir compartilhamentos manuais por **Owner Teams** ou **Access Team Templates**.
  - Utilizar hierarquias de **Business Units** bem desenhadas para que a visibilidade ocorra naturalmente via privilégios de escopo (`Business Unit` ou `Parent: Child BUs`).

---

## 📱 6. Segurança no Power Apps (Canvas Apps vs Model-Driven Apps)

### Canvas Apps Security
- **Compartilhamento de App**: Atribuição de permissões no app (*Can View* ou *Can Edit*).
- **Contexto do Usuário (User Context)**: O Canvas App é executado sob a identidade do usuário logado. Compartilhar o aplicativo **não concede acesso aos dados**. O usuário precisa ter permissões correspondentes na fonte de dados (Dataverse, SharePoint, SQL).
- **Implicitly Shared Connections**: Conexões reutilizáveis (ex: SQL com conta de serviço). Exigem extrema cautela para evitar escalação de privilégios inadvertida.

### Model-Driven Apps Security
- **Vínculo a Security Roles**: A visibilidade e a capacidade de execução de um Model-Driven App são vinculadas diretamente às Security Roles atribuídas ao usuário. Se a função do usuário não estiver associada ao App Module, o aplicativo não será exibido no portal.

---

## 🌐 7. Governança, DLP Policies e Managed Environments

### Data Loss Prevention (DLP) Policies
As políticas de prevenção contra perda de dados controlam o fluxo de dados entre conectores no ambiente:

- **Grupos de Conectores**:
  - **Business**: Conectores corporativos aprovados (ex: Dataverse, SQL Server, Office 365 Outlook).
  - **Non-Business**: Conectores pessoais ou de uso geral (ex: Twitter/X, Google Drive pessoal).
  - **Blocked**: Conectores cujo uso é estritamente proibido no ambiente.
- **Regra Fundamental**: Conectores no grupo *Business* **não podem trocar dados** com conectores do grupo *Non-Business*.
- **Connector Action Control & Endpoint Filtering**: Permite bloquear ações específicas (ex: permitir leitura mas bloquear escrita em um conector HTTP) ou restringir domínios/endpoints de destino.

### Isolamento e Segurança de Redes
- **Tenant Isolation**: Bloqueia conexões de inbound e outbound com outros tenants do Entra ID não confiáveis.
- **IP Firewall**: Restringe o acesso aos ambientes do Dataverse apenas a faixas de IP corporativos autorizados.

---

## 🤖 8. IAM em ALM (Application Lifecycle Management) e Service Principals

Para implantar soluções sem interrupções e sem depender de contas humanas:

1. **Application Users no Dataverse**:
   - Criação de um *App Registration* no Microsoft Entra ID (Service Principal).
   - Cadastro como **Application User** no Dataverse (não consome licença do Power Apps).
   - Atribuição de Security Roles customizadas (ex: *Deployment Administrator*) para execução de pipelines de CI/CD via Azure DevOps ou GitHub Actions (`pac cli`).
2. **Environment Variables & Connection References**:
   - Manutenção de conexões de produção associadas a Service Principals dedicados em vez de contas de desenvolvedores.

---

## ⚙️ Protocolo de Decisão do Engenheiro de IAM do Power Platform

1. **Aplique o Princípio do Menor Privilégio**:
   - Nunca atribua `System Administrator` a usuários finais ou contas de serviço em produção.
   - Utilize a função nativa `Basic User` ou `App Opener` como base para criação de papéis customizados.
2. **Priorize Entra ID Group Teams**:
   - Evite associar Security Roles diretamente a usuários individuais. Centralize a gestão de acessos em grupos do Entra ID para governança automatizada.
3. **Evite a Tabela POA**:
   - Modele o acesso por Business Units e equipes proprietárias em vez de usar compartilhamento de registros individuais (`Share`).
4. **Audite Periodicamente no Microsoft Purview**:
   - Ative a auditoria no Dataverse (*Audit Log*) para monitorar alterações em Security Roles, acessos a tabelas sensíveis e exclusões de registros.

---

## 🔗 Integração com Outras Skills de IAM e Nuvem

- Para governança global de IAM, princípios de RBAC/ABAC/PBAC e federação OIDC/SAML/SCIM, consulte a skill [iam-access-management](../iam-access-management/SKILL.md).
- Para integração profunda com Microsoft Entra ID, Acesso Condicional, PIM e Managed Identities, consulte a skill [iam-access-azure](../iam-access-azure/SKILL.md).
- Para controle de acessos em ambientes multicloud e AWS IAM Center, consulte a skill [iam-access-aws](../iam-access-aws/SKILL.md).
- Para Workload Identity Federation e controle de acesso no Google Cloud, consulte a skill [iam-access-gcp](../iam-access-gcp/SKILL.md).
- Para compartimentos e políticas de IAM na Oracle Cloud Infrastructure, consulte a skill [iam-access-oci](../iam-access-oci/SKILL.md).
- Para matriz de controles de segurança em nuvem (CCM v4), consulte a skill [csa-cloud-security](../csa-cloud-security/SKILL.md).
- Para automação de fluxos com conectores e governança no Power Automate, consulte a skill [power-automate](../../../programs/power-automate/SKILL.md).
- Para desenvolvimento e componentização frontend em Power Apps, consulte a skill [frontend-developer](../../../general/roles/frontend-developer/SKILL.md).
- Para boas práticas de reutilização e código limpo, consulte a skill [clean-code-reusability](../../../general/engineering-practices/clean-code-reusability/SKILL.md).
