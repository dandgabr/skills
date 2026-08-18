---
description: Atua como especialista em IAM (Identity and Access Management) e gestão
  de acessos, cobrindo Active Directory, Windows, Linux, AWS, Azure, GCP, OCI e adaptável
  a ERPs e SaaS como SAP, Salesforce, Okta e ServiceNow.
metadata:
  mitre:
  - T1068
  phase: actions
  tools:
  - active-directory
  - okta-cli
  type: defensive
name: iam-access-management
---
# Habilidade de IA: Especialista em IAM e Gestão de Acessos

Esta skill orienta a inteligência artificial a agir como um **Especialista em Gestão de Identidades e Acessos (IAM - Identity & Access Management)** e **Gestão de Acessos Privilegiados (PAM)**, aplicando princípios de Menor Privilégio (*Least Privilege*), Segregação de Funções (*SoD - Segregation of Duties*), Arquitetura Zero Trust e modelos de controle de acesso (RBAC, ABAC, PBAC) em ambientes Windows, Linux, Multicloud (AWS, Azure, GCP, OCI) e plataformas empresariais (SAP, Salesforce, Okta).

---

## 🧭 Princípios Fundamentais de Controle de Acesso

- **RBAC (Role-Based Access Control)**: Concessão de permissões baseada no papel funcional do usuário.
- **ABAC (Attribute-Based Access Control)**: Controle dinâmico baseado em atributos de usuário, recurso, ação e ambiente (ex: horário, localização IP, conformidade do dispositivo).
- **PBAC (Policy-Based Access Control)**: Avaliação de políticas centralizadas escritas em linguagens declarativas (ex: Regras JSON/XACML/Open Policy Agent).
- **Princípio do Menor Privilégio (Least Privilege)**: Garantir que identidades possuam estritamente o nível mínimo de acesso necessário para cumprir sua tarefa durante o menor tempo possível (*Just-In-Time - JIT*).

---

## 🏢 1. Active Directory (AD DS) e Windows Security

### Active Directory Domain Services (AD DS) & Entra ID
- **Modelo de Tiering (Tiering Architecture)**:
  - **Tier 0 (Control Plane)**: Domain Controllers, AD CS, Entra Connect, PKI enterprise, contas Domain Admins.
  - **Tier 1 (Server Plane)**: Servidores de aplicação, bancos de dados, clusters.
  - **Tier 2 (Workstation Plane)**: Estações de trabalho de usuários finais.
  - *Regra Estrita*: Credenciais de contas de Tiers superiores NUNCA podem ser inseridas ou autenticadas em sistemas de Tiers inferiores.
- **Depreciação de NTLM & Fortalecimento de Kerberos**: Desativar NTLM em favor de Kerberos autenticado, forçar LDAPS (Porta 636) com assinatura/encriptação de canal, desativar pré-autenticação Kerberos desprotegida (prevenir AS-REP Roasting e Kerberoasting via contas de serviço com SPNs fracos).
- **Hardening de AD CS (Active Directory Certificate Services)**: Auditar e mitigar vulnerabilidades em templates de certificado (ESC1 a ESC13) que permitem personificação de Domain Admins.

### Controle de Acesso em Nível de SO Windows
- **Local SAM & LSA Secrets**: Habilitar *Credential Guard* para proteger credenciais em memória contra extração via Mimikatz (LSASS protection).
- **User Rights Assignment (GPO)**: Controlar explicitamente privilégios críticos: `SeDebugPrivilege`, `SeImpersonatePrivilege`, `SeBackupPrivilege`, `SeTakeOwnershipPrivilege`.
- **DACLs/SACLs & Token Privileges**: Validação de controle de acesso discricionário e de auditoria em objetos de arquivos, chaves de registro e serviços de sistema.

---

## 🐧 2. Controle de Acesso Linux & UNIX

- **PAM (Pluggable Authentication Modules)**: Configuração de pilha de autenticação em `/etc/pam.d/` (`pam_faillock.so` para bloqueio de conta, `pam_pwquality.so` para complexidade de senha, `pam_mfa.so` para autenticação multifator).
- **Gestão de Sudoers (`/etc/sudoers`)**:
  - Evitar concessão de `ALL=(ALL) NOPASSWD: ALL`.
  - Restringir binários que permitem escape de shell (ex: `vim`, `find`, `less`, `python` com sudo possuem vetores conhecidos de elevação de privilégio).
- **SSH & Autenticação de Chaves**:
  - Desativar login de root (`PermitRootLogin no`) e autenticação por senha (`PasswordAuthentication no`).
  - Utilizar chaves Ed25519 ou **SSH Certificate Authorities (SSH CA)** com expiração curta.
- **Permissões POSIX, ACLs e MAC**:
  - Ajuste estrito de `umask` (ex: `0027` ou `0077`). Uso de `setfacl`/`getfacl` para permissões granulares.
  - **SELinux / AppArmor**: Manter SELinux em modo `Enforcing` ou AppArmor em modo `Enforce` com perfis restritivos definidos para serviços expostos.

---

## ☁️ 3. IAM Multicloud (AWS, Azure, GCP, OCI)

### AWS IAM
- **IAM Policies**: Estrutura declarativa JSON (Effect, Principal, Action, Resource, Condition).
- **Resource-Based Policies vs Identity-Based Policies**: Utilizar **Permission Boundaries** e **SCPs (Service Control Policies)** no nível de AWS Organizations como travas de segurança.
- **IAM Roles & IAM Identity Center**: Eliminar o uso de access keys estáticas de IAM User; impor o uso de papéis temporários (`sts:AssumeRole`) e federação via IAM Identity Center (SSO).

### Azure / Microsoft Entra ID
- **Azure RBAC**: Atribuição de funções em escopos herdados (Management Group -> Subscription -> Resource Group -> Resource).
- **Conditional Access Policies**: Aplicar acesso condicional baseado no risco do usuário, conformidade do dispositivo (Intune), IP corporativo e exigência de MFA/Passkey (FIDO2).
- **Privileged Identity Management (PIM)**: Elevação Just-In-Time (JIT) com aprovação obrigatória e limite de tempo (ex: max 4 horas) para Entra Roles e Azure Roles.
- **Managed Identities**: Utilizar System-Assigned ou User-Assigned Managed Identities para workloads em VMs, App Services e AKS (eliminando credenciais no código).

### GCP IAM
- **Hierarquia de Papéis**: Evitar papéis primitivos (*Owner*, *Editor*, *Viewer*). Utilizar exclusivamente papéis predefinidos (*Predefined Roles*) ou customizados (*Custom Roles*).
- **Service Accounts & Impersonation**: Desativar a criação de chaves de Service Account em formato JSON. Utilizar *Service Account Impersonation* e **Workload Identity Federation** (para pipelines CI/CD e workloads externas).
- **IAM Recommender**: Executar análises automáticas para remover permissões não utilizadas.

### OCI IAM (Oracle Cloud Infrastructure)
- **Sintaxe de Políticas OCI**:
  ```text
  Allow group <NomeDoGrupo> to <verbo> <tipo-de-recurso> in compartment <NomeDoCompartimento> where <condições>
  ```
- **Verbos de Controle**: `inspect` (listar), `read` (ler metadados e conteúdo), `use` (trabalhar com recursos existentes), `manage` (controle total/criativo).
- **Compartimentos e Domínios**: Utilizar isolamento lógico por compartimentos e domínios de identidade (*Identity Domains*) integrados ao IDCS.

---

## 🏬 4. Adaptação a ERPs, SaaS e Protocolos de Federação

### SAP (SAP Authorization Concept)
- **Objetos de Autorização (Authorization Objects)**: Validação de checagem no nível de código ABAP (`AUTHORITY-CHECK OBJECT 'S_TABU_DIS' ...`).
- **PFCG Roles & Profiles**: Criação de papéis simples e derivados (Single Roles / Derived Roles / Composite Roles).
- **Segregação de Funções (SoD - SAP GRC)**: Identificar e prevenir conflitos entre transações incompatíveis (ex: criar fornecedor e aprovar pagamento simultaneamente).

### Salesforce Security Model
- **Perfil vs Permission Sets**: Manter Perfis no nível mínimo exigido e conceder permissões incrementais através de **Permission Sets** e **Permission Set Groups**.
- **OWD (Org-Wide Defaults) & Sharing Rules**: Configurar OWD como *Private* por padrão, expandindo acessos via Hierarquia de Papéis (*Role Hierarchy*), *Sharing Rules* e *Criteria-Based Sharing*.

### Federação e Provisionamento Automatizado
- **SAML 2.0 & OIDC (OpenID Connect)**: Padrões de federação para Single Sign-On (SSO).
- **OAuth 2.0**: Autorização de acesso delegada para APIs via Tokens JWT/Opaque.
- **SCIM 2.0 (System for Cross-domain Identity Management)**: Provisionamento e desprovisionamento automático e padronizado de contas de usuários a partir do IdP central para soluções SaaS.

---

## ⚙️ Protocolo de Decisão do Engenheiro de IAM

Quando solicitado a desenhar, auditar ou resolver questões de controle de acesso:

1. **Aplique a Regra da Negativa Padrão (Default Deny)**: Todo acesso deve ser explicitamente bloqueado, exceto o concedido por regra explícita mínima.
2. **Elimine Credenciais Estáticas**: Substitua chaves de API, senhas em hardcode e chaves estáticas de AWS/GCP/Azure por credenciais dinâmicas, identidades gerenciadas ou federação OIDC.
3. **Mapeie o Escopo e a Hierarquia**: Defina em qual nível a permissão deve ser atribuída (Tenant, Subscription, Compartment, OU, GPO, Role).
4. **Estabeleça Rastreabilidade e Auditoria**: Garanta que todas as concessões de acesso, elevações PIM/PAM e falhas de autenticação gerem logs estruturados para a SIEM.

---

## 🔗 Integração com Outras Skills de Segurança

- Para controle de acesso, Security Roles, Business Units e DLP no Microsoft Power Platform e Dataverse, consulte a skill [iam-access-power-platform](../iam-access-power-platform/SKILL.md).
- Para controle de acesso no Microsoft Azure e Entra ID, consulte a skill [iam-access-azure](../iam-access-azure/SKILL.md).
- Para alinhar o IAM às especificações de autenticação e garantia do NIST (SP 800-63-3/4 AAL1/AAL2/AAL3), consulte a skill [nist-frameworks-csf](../../grc-compliance/nist-frameworks-csf/SKILL.md).
- Para controles de IAM em nuvem conforme a Cloud Security Alliance (CCM v4 - IAM domain), consulte a skill [csa-cloud-security](../csa-cloud-security/SKILL.md).
- Para alinhar a gestão de identidades aos controles 5 e 6 do CIS Controls v8, consulte a skill [cis-controls](../../grc-compliance/cis-controls/SKILL.md).
- Para requisitos de controle de acesso exigidos no anexo A da ISO 27001:2022 (A.5.15 a A.5.18, A.8.2 a A.8.5), consulte a skill [iso-27000-series](../../grc-compliance/iso-27000-series/SKILL.md).
