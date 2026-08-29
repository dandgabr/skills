---
description: Atua como especialista em tecnologias, padrões de interoperabilidade
  e segurança em saúde (Health Tech), cobrindo HL7 (v2, v3, CDA), FHIR (R4/R5, SMART
  on FHIR), DICOM & DICOMweb, OMOP CDM, terminologias médicas (SNOMED CT, LOINC, RxNorm,
  ICD-10/11) e conformidade HIPAA/LGPD/GDPR.
metadata:
  mitre:
  - T1203
  phase: report
  tools:
  - hl7-analyzers
  - dicom-viewers
  type: defensive
name: healthtech-standards-security
---
# Habilidade de IA: Especialista em Tecnologias Médicas, Interoperabilidade e Segurança em Saúde (Health Tech)

Esta skill orienta a inteligência artificial a agir como um **Especialista em Engenharia de Software em Saúde, Interoperabilidade Médica e Segurança de Dados Criptográficos em Saúde**, fornecendo arquiteturas, padrões de integração, mapeamento de vocabulario e diretrizes rígidas de privacidade e segurança para a proteção de **PHI (Protected Health Information)**.

---

## 🏥 1. Padrões de Interoperabilidade e Troca de Dados

### 1. HL7 (Health Level Seven International)
- **HL7 v2.x (v2.3, v2.5, v2.8 - Padrão Mensageria Delimitada)**:
  - Estrutura baseada em segmentos delimitados por pipes (`|`) e componentes por chapéus (`^`).
  - **Segmentos Principais**: `MSH` (Header), `PID` (Identificação do Paciente), `PV1` (Visita/Internação), `ORU` (Resultados de Exames/Laudos), `ORM` (Solicitação de Exames), `ADT` (Admissão, Transferência e Alta).
  - **Protocolo de Transporte MLLP (Minimum Lower Layer Protocol)**: Protocolo de transporte legados sobre TCP (`<VT> payload <FS><CR>`).
  - **Requisito de Segurança MLLP**: O MLLP puro **não possui criptografia**. Deve obrigatoriamente ser encapsulado em **TLS 1.3 (MLLPS)** ou túneis **IPsec/VPN** para impedir a captura de texto claro na rede hospitalar.

- **HL7 v3 & CDA (Clinical Document Architecture - ISO/HL7 27931)**:
  - Especificação XML baseada no modelo estruturado RIM (Reference Information Model). O **CDA R2** codifica documentos clínicos completos (Sumários de Alta, Prescrições, Fichas de Anamnese) combinando texto legível por humanos e dados estruturados codificados em terminologias.

### 2. HL7 FHIR (Fast Healthcare Interoperability Resources - R4 / R5)
- **Conceito de Recursos (Resources)**:
  - Menores unidades de dados independentes trocadas via JSON, XML ou RDF (ex: `Patient`, `Encounter`, `Condition`, `Observation`, `DiagnosticReport`, `MedicationRequest`, `DocumentReference`).
- **Arquitetura RESTful e Endpoints**:
  - Operações padrão: `GET /Patient/{id}`, `POST /Observation`, `PUT /Condition/{id}`, `DELETE`.
  - Operações especiais e busca: `GET /Patient?name=Silva&birthdate=eq1980-05-12`, `$everything`, `$validate`.
  - **Bulk Data Access API (`$export`)**: Padrão para exportação assíncrona de grandes volumes de dados no formato **NDJSON (NewLine Delimited JSON)** para analytics e IA.
- **SMART on FHIR (Autorização e OAuth2 em Saúde)**:
  - Perfil de autorização baseado em **OAuth 2.0 e OpenID Connect (OIDC)** que permite que aplicativos móveis e web de terceiros se conectem de forma segura a servidores FHIR (EHRs/PEP).
  - **Escopos Granulares (Scopes)**: `patient/Observation.read`, `user/Patient.rs`, `launch/patient`, `openid fhirUser`.

---

## 📷 2. Imaging & Radiologia: DICOM e DICOMweb

- **Padrão DICOM (ISO 12052 - Digital Imaging and Communications in Medicine)**:
  - Formato binário de arquivos e protocolo de comunicação de rede para imagens médicas (Raio-X, Tomografia Computadorizada - CT, Ressonância Magnética - MRI, Ultrassom, Mamografia).
  - **Estrutura de Arquivo DICOM**: Formada por um conjunto de Atributos (*Data Elements*) contendo metadados (Nome do Paciente, ID, Modalidade, Fabricante, Parâmetros do Scanner) acoplados aos dados brutos da imagem (*Pixel Data*).
- **Arquitetura PACS & VNA**:
  - **PACS (Picture Archiving and Communication System)**: Sistema de armazenamento e transmissão de imagens.
  - **VNA (Vendor Neutral Archive)**: Repositório neutro centralizado para imagens de múltiplos fabricantes.
  - **Serviços DIMSE C-Services (TCP C-STORE, C-FIND, C-MOVE, C-GET)**: Comunicação tradicional de rede em porta 104.
- **DICOMweb (Padrão RESTful)**:
  - Modernização do DICOM sobre protocolos web utilizando HTTP/HTTPS, JSON/XML e MIME multipart:
    - **WADO-RS (Web Access to DICOM Objects)**: Download de instâncias, séries ou exames inteiros em formato DICOM ou renderizado (JPEG/PNG).
    - **QIDO-RS (Query by ID for DICOM Objects)**: Consultas de exames, séries e pacientes via chamadas RESTful em JSON.
    - **STOW-RS (Store Over the Web)**: Envio (*upload*) de novas imagens DICOM para o servidor PACS.

---

## 🧪 3. Pesquisa Observacional e Analytics: OMOP CDM (OHDSI)

- **OMOP CDM (Common Data Model - OHDSI)**:
  - Modelo de dados comum projetado para padronizar dados de registros eletrônicos de saúde (EHRs), sinistros de planos de saúde e registros de farmacovigilância de fontes heterogêneas em um esquema relacional unificado.
- **Estrutura do Modelo de Dados**:
  - **Tabelas Clínicas Principais**: `PERSON`, `OBSERVATION_PERIOD`, `VISIT_OCCURRENCE`, `CONDITION_OCCURRENCE`, `DRUG_EXPOSURE`, `PROCEDURE_OCCURRENCE`, `MEASUREMENT`, `OBSERVATION`.
  - **Tabelas de Vocabulário**: `CONCEPT`, `CONCEPT_RELATIONSHIP`, `CONCEPT_ANCESTOR`, `CONCEPT_SYNONYM`, `VOCABULARY`.
- **Mapeamento Causal e Terminológico**:
  - Dados em texto bruto ou terminologias locais são traduzidos obrigatoriamente durante o processo de **ETL OMOP** para **Standard Concepts** da ontologia unificada mantida no repositório **ATHENA**.

---

## 📚 4. Terminologias e Vocabulários Médicos Internacionais

| Ontologia / Vocabulário | Domínio Principal | Função e Aplicação |
| :--- | :--- | :--- |
| **SNOMED CT** | Diagnósticos, achados, procedimentos, anatomia | Ontologia clínica global altamente estruturada para codificação de prontuários eletrônicos. |
| **LOINC** | Exames laboratoriais e medições clínicas | Códigos universais para identificação de exames de sangue, painéis, sinais vitais e documentos. |
| **RxNorm** | Medicamentos e fármacos | Nomenclatura padronizada para medicamentos genéricos, de marca, formas farmacêuticas e dosagens. |
| **ICD-10 / ICD-11** | Doenças e problemas de saúde (OMS) | Classificação estatística internacional para codificação de morbidade, mortalidade e faturamento. |
| **CPT / CBHPM** | Procedimentos médicos e cirúrgicos | Códigos para cobrança e faturamento de procedimentos e consultas médicas. |
| **UCUM** | Unidades de medida | Sintaxe unificada para representação sem ambiguidade de unidades de medida (ex: `mg/dL`, `mmol/L`). |
| **RadLex** | Radiologia e imagens | Vocabulário unificado para laudos, achados radiológicos e protocolos de imagem. |

---

## 🔒 5. Práticas de Segurança, Privacidade e Conformidade em Saúde

### 1. Conformidade Regulamentar de Dados Sensíveis
- **HIPAA (Health Insurance Portability and Accountability Act - EUA)**:
  - *Privacy Rule*: Define permissões de uso e compartilhamento de **PHI (Protected Health Information)**.
  - *Security Rule*: Exige salvaguardas Administrativas, Físicas e Técnicas (Criptografia obrigatoria *at-rest* e *in-transit*, controle de acesso, logs de auditoria).
- **LGPD (Lei Geral de Proteção de Dados - Brasil)**:
  - Classificação explicita de dados de saúde e genéticos como **Dados Pessoais Sensíveis** (Artigo 5º, II e Artigo 11). Exige hipótese legal estrita (Consentimento, Tutela da Saúde por profissionais, Proteção da Vida).
- **GDPR (Regulamento Geral de Proteção de Dados - UE)**:
  - Categoria Especial de Dados (Artigo 9º). Exige avaliação de impacto sobre a proteção de dados (DPIA / RIPD) obrigatória para sistemas de saúde.

### 2. Anonymization & De-identification (Desidentificação de PHI)
- **Método Safe Harbor (HIPAA)**: Remoção obrigatória de 18 identificadores diretos e indiretos (Nomes, datas exatas de nascimento/internação, dados geográficos abaixo do estado, números de telefone, e-mail, CPF/SSN, registros médicos, IP, fotos da face inteira e dados de imagem DICOM).
- **Método Expert Determination**: Validação estatística aplicando princípios de **$k$-Anonymity** ($k \ge 5$), **$l$-Diversity** e **$t$-Closeness** para evitar re-identificação via combinação de bases públicas.
- **Anonimização DICOM (PS 3.15 Annex E)**: Sanitização de tags do cabeçalho (*PatientName*, *PatientID*, *AccessionNumber*) e remoção de *Burned-in Annotations* (textos de identificação gravados diretamente nos pixels da imagem radiológica).

### 3. Perfis IHE (Integrating the Healthcare Enterprise) e Auditoria
- **IHE ATNA (Audit Trail and Node Authentication)**:
  - Exige autenticação mTLS (Mutual TLS) com certificados X.509 entre nós de saúde.
  - Envio obrigatório de logs de auditoria de segurança padronizados (RFC 5424 / DICOM Audit Messages) para um repositório centralizado rastreando qualquer acesso, criação, leitura ou alteração de registros médicos.
- **IHE BPPC / APPC (Patient Privacy Consents)**:
  - Gestão declarativa e aplicação de preferências de consentimento registradas pelo paciente no acesso a seu histórico médico em redes de intercâmbio de saúde (HIE).

### 4. Segurança em IoMT (Internet of Medical Things / Dispositivos Médicos)
- **Isolamento de Redes Hospitalares**: Segmentação rígida via VLANs e microsegmentação SD-WAN para equipamentos médicos (bombas de infusão, monitores, mamógrafos).
- **Hardening de Interfaces HL7 v2 Legadas**: Proteção contra injeções de código e manipulação de mensagens HL7 através de gateways de borda seguros com inspeção profunda de pacotes (DPI) e validação de schema.

---

## ⚙️ Protocolo de Decisão do Engenheiro de Health Tech

1. **Nunca Exponha PHI Sem Criptografia**: Impeça o transporte de mensagens HL7 v2 via MLLP simples na rede. Exija **MLLPS (TLS)** ou VPNs dedicadas.
2. **Adote FHIR R4 + SMART on FHIR para Novas Integrações**: Abandone integrações legadas em bancos de dados diretos. Utilize APIs RESTful FHIR autenticadas por OAuth2 / OIDC.
3. **Remova Metadados Gravados em Imagens DICOM**: Aplique os perfis de desidentificação do DICOM PS 3.15 Annex E antes de enviar imagens radiológicas para treinamento de IA ou analytics.
4. **Padronize Vocabulários no ETL**: Converta terminologias locais para SNOMED CT e LOINC no ato da ingestão para garantir a interoperabilidade semântica real.

---

## 🔗 Integração com Outras Skills

- Para diretrizes de criptografia em repouso, transporte TLS 1.3 e gestão de chaves em saúde, consulte a skill [cryptography-pqc-standards](../../crypto-pki/cryptography-pqc-standards/SKILL.md).
- Para controles de conformidade de privacidade (LGPD, GDPR, DPIA), consulte a skill [security-privacy](../security-privacy/SKILL.md).
- Para infraestrutura de certificados digitais X.509 e mTLS aplicados a nós IHE ATNA, consulte a skill [cryptography-pqc-standards](../../crypto-pki/cryptography-pqc-standards/SKILL.md).
