---
description: Atua como auditor especialista e arquiteto de SGSI/PIMS especialista
  em toda a família ISO/IEC 27000, incluindo ISO/IEC 27001:2022, 27002:2022, 27005,
  27017, 27018, 27032, 27035, 27036 e ISO/IEC 27701.
metadata:
  mitre:
  - T1068
  phase: report
  tools:
  - iso-checklists
  type: defensive
name: iso-27000-series
---
# Habilidade de IA: Especialista na Família ISO/IEC 27000

Esta skill orienta a inteligência artificial a agir como um **Auditor Líder e Consultor Especialista na Família ISO/IEC 27000**, estruturando, implementando, avaliando e auditando **Sistemas de Gestão de Segurança da Informação (SGSI / ISMS)** e **Sistemas de Gestão da Informação de Privacidade (PIMS)** segundo os padrões internacionais estabelecidos pela ISO (International Organization for Standardization) e IEC (International Electrotechnical Commission).

---

## 🧭 Visão Geral da Família ISO/IEC 27000

A série ISO/IEC 27000 estabelece o ecossistema internacional definitivo para governança, gestão de risco, controle e auditabilidade de segurança da informação e privacidade:

| Norma ISO/IEC | Título e Foco Principal |
| :--- | :--- |
| **ISO/IEC 27001:2022** | Requisitos do Sistema de Gestão de Segurança da Informação (SGSI) + Anexo A (93 Controles). |
| **ISO/IEC 27002:2022** | Código de prática e diretrizes detalhadas para a implementação dos 93 controles de segurança. |
| **ISO/IEC 27000:2020** | Visão geral, conceitos e vocabulário fundamental do SGSI. |
| **ISO/IEC 27003** | Orientações para o planejamento e implementação passo a passo do SGSI. |
| **ISO/IEC 27004** | Monitoramento, medição, análise, avaliação e métricas de eficácia do SGSI. |
| **ISO/IEC 27005:2022** | Gestão de riscos de segurança da informação alinhada à ISO 31000. |
| **ISO/IEC 27006 / 27007**| Requisitos para organismos de certificação e diretrizes para auditoria de SGSI. |
| **ISO/IEC 27017** | Controles de segurança da informação específicos para serviços em nuvem (Provedor e Cliente). |
| **ISO/IEC 27018** | Proteção de Dados Pessoais Identificáveis (PII) em nuvens públicas atuando como processador. |
| **ISO/IEC 27031** | Prontidão das Tecnologias de Informação e Comunicação (TIC) para Continuidade de Negócios. |
| **ISO/IEC 27032** | Diretrizes gerais para cibersegurança e proteção do espaço cibernético. |
| **ISO/IEC 27035** | Gestão de Incidentes de Segurança da Informação (Planejamento, Resposta e Lições Aprendidas). |
| **ISO/IEC 27036** | Segurança da Informação nos relacionamentos com fornecedores e Cadeia de Suprimentos (*Supply Chain*). |
| **ISO/IEC 27701:2019** | Extensão da ISO 27001/27002 para Gestão da Informação de Privacidade (PIMS - LGPD/GDPR). |

---

## 🏛️ Estrutura da ISO/IEC 27001:2022

### Cláusulas Normativas (Requisitos Auditáveis de 4 a 10)
- **Cláusula 4 - Contexto da Organização**: Determinar escopo do SGSI, partes interessadas e requisitos internos/externos.
- **Cláusula 5 - Liderança**: Comprometimento da alta direção, Política de Segurança da Informação, papéis e responsabilidades.
- **Cláusula 6 - Planejamento**: Identificação e tratamento de riscos, objetivos de segurança da informação e planejamento de mudanças.
- **Cláusula 7 - Apoio**: Recursos, competência, conscientização, comunicação e informação documentada.
- **Cláusula 8 - Operação**: Planejamento e controle operacional, avaliação de risco de segurança da informação e tratamento de risco.
- **Cláusula 9 - Avaliação do Desempenho**: Monitoramento, medição, análise, auditoria interna e análise crítica pela direção (*Management Review*).
- **Cláusula 10 - Melhoria**: Não conformidades, ações corretivas e melhoria contínua do SGSI.

---

## 🔒 Anexo A da ISO/IEC 27001:2022 & ISO/IEC 27002:2022 (93 Controles)

A versão 2022 reestruturou os controles em **4 Categorias Temáticas** e introduziu **11 Novos Controles**:

```
+-----------------------------------------------------------------------------------+
| 1. Controles Organizacionais (Organizational Controls - 37 Controles)             |
|    - Políticas, papéis, segregação de funções, gestão de ativos, uso aceitável,  |
|      inteligência de ameaças (A.5.7), segurança em nuvem (A.5.23), fornecedores. |
+-----------------------------------------------------------------------------------+
| 2. Controles de Pessoas (People Controls - 8 Controles)                            |
|    - Triagem antecedente, termos de contratação, conscientização, processo disciplinar|
+-----------------------------------------------------------------------------------+
| 3. Controles Físicos (Physical Controls - 14 Controles)                           |
|    - Perímetros físicos, controle de acesso físico, monitoramento (A.7.4), utilidades |
+-----------------------------------------------------------------------------------+
| 4. Controles Tecnológicos (Technological Controls - 34 Controles)                 |
|    - IAM, gestão de privilégios, criptografia, prev. vazamento dados (DLP - A.8.12),|
|      gerenciamento de configuração (A.8.9), deleção segura de dados (A.8.10),     |
|      mascaramento de dados (A.8.11), desenvolvimento seguro (A.8.25-A.8.30).       |
+-----------------------------------------------------------------------------------+
```

### Os 11 Novos Controles da Versão 2022:
1. **A.5.7 - Threat Intelligence** (Inteligência sobre ameaças)
2. **A.5.23 - Information security for use of cloud services** (Segurança para uso de serviços em nuvem)
3. **A.5.30 - ICT readiness for business continuity** (Prontidão de TIC para continuidade de negócios)
4. **A.7.4 - Physical security monitoring** (Monitoramento de segurança física)
5. **A.8.9 - Configuration management** (Gerenciamento de configurações)
6. **A.8.10 - Information deletion** (Eliminação de informações)
7. **A.8.11 - Data masking** (Mascaramento de dados)
8. **A.8.12 - Data leakage prevention** (Prevenção contra vazamento de dados - DLP)
9. **A.8.16 - Monitoring activities** (Atividades de monitoramento e análise anômala)
10. **A.8.23 - Web filtering** (Filtragem web)
11. **A.8.28 - Secure coding** (Codificação segura de aplicações)

---

## ⚙️ Protocolo de Execução do Auditor e Especialista ISO

Quando solicitado a desenhar, preparar a certificação ou auditar uma organização:

1. **Construir a Declaração de Aplicabilidade (SoA - Statement of Applicability)**:
   - Avalie cada um dos 93 controles do Anexo A da ISO 27001:2022, justificando a inclusão ou exclusão com base na avaliação de riscos (ISO 27005).
2. **Aplicar a Matriz de Atributos da ISO 27002:2022**:
   - Classifique cada controle selecionado por: *Control Type* (Preventivo, Detectivo, Corretivo), *Information Security Properties* (Confidencialidade, Integridade, Disponibilidade), *Cybersecurity Concepts* (Identify, Protect, Detect, Respond, Recover) e *Operational Capabilities*.
3. **Mapear a Extensão de Privacidade (ISO/IEC 27701)**:
   - Se a organização processar Dados Pessoais (PII), estenda o SGSI para PIMS incorporando os controles específicos de PII Controller (Cláusula 7) ou PII Processor (Cláusula 8).
4. **Validar Auditoria Interna e Análise Crítica (Cláusulas 9.2 e 9.3)**:
   - Garanta que evidências documentadas de auditorias internas recentes e reuniões de análise crítica pela direção estejam disponíveis antes do estágio 2 da auditoria de certificação.

---

## 🔗 Integração com Outras Skills de Segurança

- Para alinhamento dos controles tecnológicos ISO 27002 (A.8.24) às melhores práticas criptográficas e quânticas, consulte a skill [cryptography-pqc-standards](../../crypto-pki/cryptography-pqc-standards/SKILL.md).
- Para detalhamento dos controles de acesso ISO 27002 (A.5.15 a A.5.18, A.8.2 a A.8.5), consulte a skill [iam-access-management](../../cloud-iam/iam-access-management/SKILL.md).
- Para alinhamento com requisitos de nuvem específicos da CSA CCM v4, consulte a skill [csa-cloud-security](../../cloud-iam/csa-cloud-security/SKILL.md).
- Para alinhamento do SGSI com a governança geral corporativa, consulte a skill [security-grc-compliance](../security-grc-compliance/SKILL.md).
- Para alinhamento dos requisitos de privacidade ISO 27701 com LGPD e GDPR, consulte a skill [security-privacy](../security-privacy/SKILL.md).
