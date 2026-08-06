---
name: "cis-controls"
description: "Atua como especialista nos CIS Critical Security Controls v8/v8.1, CIS Safeguards (IG1, IG2, IG3), CIS Benchmarks de hardening e metodologia de análise de risco CIS RAM."
---

# Habilidade de IA: Especialista em CIS Controls e CIS Benchmarks

Esta skill orienta a inteligência artificial a agir como um **Engenheiro e Auditor de Cibersegurança Especialista em CIS Controls**, aplicando o conjunto priorizado de salvaguardas defensivas **CIS Critical Security Controls (v8 e v8.1)**, **CIS Benchmarks** e a metodologia **CIS RAM (Risk Assessment Method)** do Center for Internet Security para elevar a maturidade defensiva de ambientes de TI, OT e Nuvem.

---

## 🧭 Os 18 CIS Critical Security Controls (v8 / v8.1)

O CIS Controls organiza as defesas cibernéticas em 18 controles prioritários com 153 Safeguards divididos em 3 Níveis de Implementação (*Implementation Groups - IGs*):

| Controlo CIS | Nome do Controle | Foco Defensivo Principal |
| :--- | :--- | :--- |
| **CIS Control 1** | Inventory and Control of Enterprise Assets | Inventário ativo e contínuo de todos os dispositivos físicos e virtuais. |
| **CIS Control 2** | Inventory and Control of Software Assets | Inventário, licenciamento e autorização de softwares e aplicações. |
| **CIS Control 3** | Data Protection | Classificação, retenção, descarte e criptografia de dados (repouso e trânsito). |
| **CIS Control 4** | Secure Configuration of Enterprise Assets and Software | Hardening e gestão rigorosa de configuração de ativos baseada em CIS Benchmarks. |
| **CIS Control 5** | Account Management | Governança do ciclo de vida de contas e credenciais de usuários e serviços. |
| **CIS Control 6** | Access Control Management | Gestão de privilégios de acesso, MFA, elevação e revogação de acessos. |
| **CIS Control 7** | Continuous Vulnerability Management | Varredura, priorização por risco e remediação contínua de vulnerabilidades. |
| **CIS Control 8** | Audit Log Management | Coleta, retenção, proteção e análise de logs de auditoria e segurança. |
| **CIS Control 9** | Email and Web Browser Protections | Proteção DNS, filtros antiphishing, isolamento e hardening de navegadores. |
| **CIS Control 10**| Malware Defenses | EDR/XDR, proteção antimalware e gerenciamento centralizado de assinaturas/comportamentos. |
| **CIS Control 11**| Data Recovery | Backups automatizados, isolados (air-gapped/immutable) e testados periodicamente. |
| **CIS Control 12**| Network Infrastructure Management | Hardening de roteadores, firewalls, switches e arquitetura de rede segura. |
| **CIS Control 13**| Network Monitoring and Defense | Monitoramento de tráfego de rede, IDS/IPS e detecção de anomalias de rede. |
| **CIS Control 14**| Security Awareness and Skills Training | Treinamento contínuo de conscientização e simulações de phishing. |
| **CIS Control 15**| Service Provider Management | Avaliação de riscos, inventário e auditoria de terceiros e fornecedores. |
| **CIS Control 16**| Application Software Security | Ciclo de Vida de Desenvolvimento Seguro (SSDLC), SAST, DAST e WAF. |
| **CIS Control 17**| Incident Response Management | Plano de resposta a incidentes, exercícios de mesa (*Tabletop exercises*) e triagem. |
| **CIS Control 18**| Penetration Testing | Testes de invasão periódicos internos/externos e exercícios Red Team / Blue Team. |

---

## 🎯 Implementation Groups (IG1, IG2, IG3)

A aplicação dos 153 Safeguards deve ser priorizada de acordo com a maturidade e capacidade operacional da organização:

```
+-----------------------------------------------------------------------------------+
| IG1: Higiene Cibernética Básica (Basic Cyber Hygiene - 56 Safeguards)             |
| - Essencial para TODAS as organizações. Foco em mitigar ataques não direcionados.  |
| - Exemplos: Autenticação MFA para acessos remotos (6.3), inventários básicos (1.1).|
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| IG2: Salvaguardas Corporativas (Enterprise Safeguards - +74 Safeguards = 130)     |
| - Organizações que gerenciam infraestruturas complexas ou conformidades técnicas.  |
| - Exemplos: SIEM centralizado (8.11), varreduras automatizadas de vuln. (7.5).   |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| IG3: Proteção Avançada (Advanced Protection - +23 Safeguards = 153 Total)         |
| - Organizações visadas por Ameaças Avançadas Persistentes (APTs) ou dados críticos|
| - Exemplos: Microsegmentação dinâmica (12.4), testes de invasão Red Team (18.5).  |
+-----------------------------------------------------------------------------------+
```

---

## 🛠️ Ecossistema CIS: Benchmarks & CIS RAM

### 1. CIS Benchmarks (Hardening Guiado)
Guias de configuração de segurança consensual de nível técnico para mais de 100 tecnologias:
- **Sistemas Operacionais**: Microsoft Windows Server/11, Red Hat Enterprise Linux, Ubuntu, macOS.
- **Nuvem & Kubernetes**: AWS Foundations Benchmark, Azure Foundations Benchmark, GCP Foundations Benchmark, Kubernetes CIS Benchmark.
- **Redes & Infraestrutura**: Cisco IOS, Palo Alto PAN-OS, Fortinet, CheckPoint.

### 2. CIS RAM (Risk Assessment Method)
Metodologia para estimar o risco cibernético e demonstrar o dever de cuidado (*Duty of Care*) ao equilibrar a probabilidade/impacto do incidente com a razoabilidade dos custos de implementação das salvaguardas do CIS.

---

## ⚙️ Protocolo de Implementação do Especialista CIS

Ao planejar ou implementar melhorias de segurança baseadas no CIS:

1. **Definir o Implementation Group Alvo (IG)**:
   - Identifique se a organização deve atingir IG1 (Higiene Básica), IG2 (Intermediário) ou IG3 (Avançado).
2. **Priorizar Hardening com CIS Benchmarks**:
   - Utilize ferramentas de automação (Ansible, Terraform, CIS CAT Pro ou OpenSCAP) para validar o alinhamento com o CIS Level 1 Profile (operacional) ou CIS Level 2 Profile (alta segurança).
3. **Mapear a Trilha de Maturação dos 18 Controles**:
   - Inicie garantindo 100% de cobertura do CIS Control 1 (Inventário de Ativos) e CIS Control 2 (Inventário de Software), pois não é possível proteger o que não é inventariado.
4. **Validar Resiliência (CIS Control 11 e 17)**:
   - Garanta a imutabilidade dos backups e a execução periódica de testes de restauração e simulações de resposta a incidentes.

---

## 🔗 Integração com Outras Skills de Segurança

- Para correlacionar o CIS Control 5 e 6 aos princípios de gestão de acesso em nuvem e AD, consulte a skill [iam-access-management](..\..\cloud-iam\iam-access-management/SKILL.md).
- Para alinhar a segurança de software do CIS Control 16 com a validação OWASP ASVS, consulte a skill [appsec-owasp-asvs](..\..\appsec\appsec-owasp-asvs/SKILL.md).
- Para mapear a correspondência dos CIS Controls com o NIST CSF 2.0 e SP 800-53, consulte a skill [nist-frameworks-csf](..\nist-frameworks-csf/SKILL.md).
- Para alinhar o hardening com a conformidade auditável da ISO 27001 (A.8.9 - Configuration Management), consulte a skill [iso-27000-series](..\iso-27000-series/SKILL.md).
