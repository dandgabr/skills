---
description: Atua como especialista em Microsoft Entra ID (Azure AD) e Azure IAM,
  cobrindo Azure RBAC, Custom Roles, PIM (Privileged Identity Management), Conditional
  Access, Managed Identities, ABAC e Entra ID Governance.
metadata:
  mitre:
  - T1068
  phase: actions
  tools:
  - entra-id-analyzer
  - bloodhound
  type: defensive
name: iam-access-azure
---
# Habilidade de IA: Especialista em Gestão de Acessos no Azure e Microsoft Entra ID

Esta skill orienta a inteligência artificial a agir como um **Especialista em Gestão de Identidades e Controle de Acesso no Microsoft Azure e Microsoft Entra ID (antigo Azure Active Directory)**, fornecendo arquitetura de segurança, governança de papéis, automação de acessos temporários (JIT) e políticas de Acesso Condicional.

---

## 🎯 1. Hierarquia de Escopos e Azure RBAC (Role-Based Access Control)

### Estrutura de Escopos Herdados
As permissões concedidas em um nível superior são herdadas automaticamente por todos os níveis inferiores:

```text
Root Management Group
  └── Tenant Root Group
        └── Management Groups (ex: Prod, Non-Prod, SharedServices)
              └── Subscriptions (ex: Sub-AppA-Prod)
                    └── Resource Groups (ex: rg-appa-sp-prod)
                          └── Resources (ex: vm-appa-01, keyvault-appa-prod)
```

### Tipos de Atribuição de Função (Role Assignments)
- **Built-in Roles (Funções Nativas)**:
  - *Owner*: Acesso total aos recursos, incluindo capacidade de delegar acessos a terceiros.
  - *Contributor*: Acesso total para criar e gerenciar recursos, sem permissão para conceder acessos.
  - *Reader*: Acesso somente leitura a metadados e recursos.
  - *User Access Administrator*: Permissão para gerenciar atribuições de acesso sem acesso direto ao plano de dados.
- **Custom Roles (Funções Personalizadas)**:
  - Definição em JSON separando ações de plano de controle (`Actions` e `NotActions`) e ações de plano de dados (`DataActions` e `NotDataActions`).

```json
{
  "Name": "Virtual Machine Operator",
  "IsCustom": true,
  "Description": "Permite reiniciar e monitorar VMs sem alterar configurações de rede ou disco.",
  "Actions": [
    "Microsoft.Compute/virtualMachines/read",
    "Microsoft.Compute/virtualMachines/start/action",
    "Microsoft.Compute/virtualMachines/restart/action"
  ],
  "NotActions": [],
  "DataActions": [],
  "AssignableScopes": [
    "/subscriptions/11111111-2222-3333-4444-555555555555"
  ]
}
```

---

## ⚡ 2. Políticas de Acesso Condicional (Conditional Access)

Motor de decisão Zero Trust do Entra ID que avalia sinais em tempo real antes de emitir tokens de autenticação:

- **Sinais Avaliados**:
  - Usuário e pertencimento a grupos.
  - Localização (IPs confiáveis / *Named Locations* e geofencing).
  - Estado e conformidade do dispositivo (Dispositivo associado ao Entra ID / Gerenciado pelo Microsoft Intune).
  - Nível de Risco da Sessão e do Usuário (*Entra ID Protection* - Risco Baixo, Médio, Alto).
  - Aplicação de destino (SaaS, Azure Management, APIs de terceiros).
- **Controles de Concessão (Grant Controls)**:
  - Exigir MFA (Autenticação Multifator) ou credencial FIDO2 / Passkey resistente a phishing.
  - Exigir dispositivo em conformidade (*Require compliant device*).
  - Bloquear acesso totalmente.

---

## 🛡️ 3. Microsoft Entra ID Governance & PIM (Privileged Identity Management)

- **Just-In-Time (JIT) Role Elevation**:
  - Eliminação de atribuições permanentes de papéis altamente privilegiados (*Global Administrator*, *Privileged Role Administrator*, *Subscription Owner*).
  - As identidades são mantidas como **Elegíveis** (*Eligible*), exigindo ativação sob demanda com:
    - Justificativa de negócio e número de chamado (ITSM/Jira).
    - Aprovação por um gestor designado.
    - Duração máxima limitada (ex: de 1 a 8 horas).
    - Desencadeamento de alerta de e-mail e auditoria imediata no Log Analytics.
- **Access Reviews (Análises de Acesso)**:
  - Recertificação periódica automatizada de membros em grupos sensíveis e papéis do Entra ID / Azure Recursos com remoção automática de contas inativas ou transferidas.

---

## 🤖 4. Identidades Gerenciadas (Managed Identities) e Entra Workload ID

- **System-Assigned Managed Identity**:
  - Identidade vinculada diretamente a um único recurso Azure (ex: VM, App Service, Function). Ciclo de vida estritamente acoplado ao recurso; ao deletar o recurso, a identidade é removida automaticamente.
- **User-Assigned Managed Identity**:
  - Recurso independente que pode ser compartilhado entre múltiplos componentes de uma aplicação (ex: um pool de nós em AKS ou conjunto de VMs).
- **Entra Workload ID & Workload Identity Federation**:
  - Autenticação sem credenciais estáticas (*Keyless*) para microsserviços fora do Azure (ex: GitHub Actions, workloads no AWS EKS ou GCP) estabelecendo confiança federada OpenID Connect (OIDC).

---

## 🔍 5. Auditoria, Diagnóstico e KQL Queries

- **Consultas KQL no Azure Monitor Log Analytics (AuditLogs & SigninLogs)**:
```kusto
// Identificar alterações de atribuições de papéis no Azure RBAC nas últimas 24h
AzureActivity
| where TimeGenerated > ago(24h)
| where OperationNameValue == "MICROSOFT.AUTHORIZATION/ROLEASSIGNMENTS/WRITE"
| project TimeGenerated, Caller, ActivityStatusValue, Properties
```

---

## ⚙️ Protocolo de Decisão do Engenheiro IAM Azure

1. **Elimine Atribuições Diretas a Usuários**: Atribua papéis Azure RBAC e Entra Roles **exclusivamente a Grupos de Segurança** (Security Groups) com membros gerenciados de forma dinâmica ou via PIM.
2. **Priorize Managed Identities**: Proíba a criação de App Registrations com Client Secrets para serviços que rodam nativamente no Azure.
3. **Imponha PIM em Nível de Subscription**: Nenhuma conta humana deve ter papel `Owner` ou `Contributor` permanente em Subscriptions de Produção.

---

## 🔗 Integração com Outras Skills

- Para integrar automações do Power BI e Power Automate com Entra ID, consulte as skills [power-bi](../../../programs/power-bi/SKILL.md) e [power-automate](../../../programs/power-automate/SKILL.md).
- Para diretrizes de governança geral de identidades e PAM, consulte a skill [iam-access-management](../iam-access-management/SKILL.md).
- Para alinhar o IAM ao CIS Microsoft Azure Foundations Benchmark, consulte a skill [cis-controls](../../grc-compliance/cis-controls/SKILL.md).
