---
name: "pci-dss-compliance"
description: "Atua como especialista em conformidade PCI DSS v4.0 (Payment Card Industry Data Security Standard), cobrindo proteção de CHD/SAD, Tokenização, Escopo CDE, Segmentação de Rede, Criptografia, HSMs de Pagamento, QSA, SAQ e Controles de Segurança."
---

# Habilidade de IA: Especialista em PCI DSS v4.0 e Segurança de Dados de Pagamento

Esta skill orienta a inteligência artificial a agir como um **Especialista em PCI DSS (Payment Card Industry Data Security Standard - Versão 4.0)**, fornecendo arquitetura de segurança para ambientes de pagamento, técnicas de redução de escopo CDE, proteção de dados de cartão de crédito, HSMs de pagamento e requisitos de auditoria e conformidade.

---

## 💳 1. Conceitos Fundamentais e Classificação de Dados (PCI DSS v4.0)

O PCI DSS protege duas categorias distintas de dados na cadeia de pagamento:

### 1. Cardholder Data (CHD - Dados do Portador do Cartão)
Dados que **podem ser armazenados** se houver justificativa legítima de negócio e se forem protegidos com criptografia forte (ex: AES-256, FPE):
- **PAN (Primary Account Number)**: O número principal de 13 a 19 dígitos do cartão.
- **Cardholder Name**: Nome impresso do titular.
- **Expiration Date**: Data de expiração (MM/AA).
- **Service Code**: Código de serviço de 3 dígitos.

### 2. Sensitive Authentication Data (SAD - Dados Sensíveis de Autenticação)
Dados críticos utilizados para autorizar transações. **PROIBIÇÃO ABSOLUTA DE ARMAZENAMENTO PÓS-AUTORIZAÇÃO** (mesmo se criptografados):
- **Full Track Data**: Dados completos da faixa magnética ou chip (Track 1 / Track 2).
- **CAV2 / CVC2 / CVV2 / CID**: Código de verificação impresso no cartão (3 ou 4 dígitos).
- **PIN e PIN Block**: Senha pessoal do titular e blocos criptografados de PIN.

---

## 🏰 2. Escopo CDE (Cardholder Data Environment) e Redução de Escopo

- **CDE (Cardholder Data Environment)**:
  - Composto por todas as pessoas, processos e tecnologias que **armazenam, processam ou transmitem** CHD/SAD, ou sistemas que estejam **conectados diretamente** a esses ambientes sem isolamento rígido.
- **Técnicas Obrigatórias de Redução de Escopo**:
  - **Segmentação de Rede Estrita**: Uso de Firewalls de próxima geração (NGFW), VLANs dedicadas e microsegmentação isolando o CDE de redes corporativas comuns.
  - **P2PE (Point-to-Point Encryption)**: Criptografia dos dados de cartão diretamente no leitor físico (PIN Pad / POS) aprovado pelo PCI SSC até o módulo HSM do adquirente, retirando a rede do estabelecimento do escopo de leitura de texto claro.
  - **Tokenização de Cartões**: Substituição do PAN real por um valor substituto (*Token*) sem valor matemático criptográfico reversível fora do *Token Vault* isolado.

---

## 🛡️ 3. Os 12 Requisitos do PCI DSS v4.0

### Principal 1: Construir e Manter Redes e Sistemas Seguros
- **Requisito 1**: Implementar e manter controles de segurança de rede (Firewalls, NSGs).
- **Requisito 2**: Aplicar configurações seguras em todos os componentes do sistema (eliminar senhas padrão de fábrica).

### Principal 2: Proteger os Dados do Portador do Cartão
- **Requisito 3**: Proteger os dados do portador de cartão armazenados (Criptografia AES-256/FPE, truncamento, hashing irreversível com salting).
- **Requisito 4**: Proteger os dados do portador de cartão com criptografia forte durante a transmissão em redes abertas/públicas (TLS 1.3, IPsec).

### Principal 3: Manter um Programa de Gerenciamento de Vulnerabilidades
- **Requisito 5**: Proteger todos os sistemas e softwares contra malwares maliciosos.
- **Requisito 6**: Desenvolver e manter sistemas e softwares seguros (Práticas de DevSecOps, OWASP Top 10, sanitização de código, patches em até 30 dias para vulnerabilidades críticas).

### Principal 4: Implementar Medidas Fortes de Controle de Acesso
- **Requisito 7**: Restringir o acesso aos dados do portador de cartão pela necessidade de saber do negócio (*Need-to-Know* / Least Privilege).
- **Requisito 8**: Identificar usuários e autenticar o acesso aos componentes do sistema (Autenticação Multifator - MFA obrigatória para todo acesso ao CDE).
- **Requisito 9**: Restringir o acesso físico aos dados do portador do cartão (Datacenters, servidores e documentos físicos).

### Principal 5: Monitorar e Testar Redes Regularmente
- **Requisito 10**: Registrar e monitorar todos os acessos a recursos de rede e dados de cartão (SIEM, NTP sincronizado, logs inalteráveis por no mínimo 1 ano).
- **Requisito 11**: Testar a segurança dos sistemas e redes regularmente (Scans de vulnerabilidade ASV trimestrais, Pentests internos e externos anuais, detecção de intrusão WAF/IDS/IPS).

### Principal 6: Manter uma Política de Segurança da Informação
- **Requisito 12**: Manter uma política de segurança da informação para todos os funcionários e prestadores de serviço (Treinamento, gestão de riscos, avaliação de fornecedores de serviço - TPSPs).

---

## 🔐 4. Criptografia, HSMs de Pagamento e Key Management

- **HSMs de Pagamento (Payment HSMs)**:
  - Módulos de hardware dedicados (FIPS 140-2 / 140-3 Level 3) especializados em operações financeiras (Validação de PIN, geração de EMV Cryptograms ARQC/ARPC, transadução de PIN Blocks).
- **Protocolos de Gerenciamento de Chaves de Pagamento**:
  - **DUKPT (Derived Unique Key Per Transaction - ANSI X9.24)**: Derivação de uma chave simétrica única a cada transação no POS, impedindo que a interceptação de uma chave comprometa transações passadas ou futuras.
  - **Key Wrapping & Bloques de Chaves (TR-31 / ANSI X9.143)**: Encapsulamento de chaves com metadados de uso e atributos de integridade.

---

## 📝 5. Validação, Formulários SAQ e Auditorias

- **Níveis de Comerciantes e Provedores de Serviço (Merchant & Service Provider Levels)**:
  - **Level 1**: Acima de 6 milhões de transações/ano. Exige auditoria presencial anual emitida por um **QSA (Qualified Security Assessor)** gerando um **ROC (Report on Compliance)**.
  - **Levels 2, 3 e 4**: Permite validação anual via **SAQ (Self-Assessment Questionnaire)** dependendo do modelo de captura:
    - *SAQ A*: E-commerce que terceiriza 100% da captura (iFrame / Redirecionamento hospedeiro PCI Level 1).
    - *SAQ A-EP*: E-commerce que captura os dados via formulário próprio mas envia direto à API do Gateway.
    - *SAQ D*: Todos os comerciantes que armazenam cartões ou não se enquadram em outros SAQs.
- **Scans ASV (Approved Scanning Vendor)**: Varreduras externas obrigatórias de vulnerabilidade executadas a cada 3 meses por fornecedor homologado pelo PCI SSC.

---

## ⚙️ Protocolo de Decisão do Especialista PCI DSS

1. **Nunca Armazene SAD (CVV/Track/PIN)**: Em nenhuma hipótese permita que código ou banco de dados registre códigos CVV2 ou trilhas de cartão após a resposta de autorização.
2. **Reduza o Escopo via iFrame / Tokenização**: Sempre que possível, recomende o uso de iFrames hospedados pelo gateway ou tokenização na origem para manter a aplicação cliente em escopo *SAQ A*.
3. **Imponha MFA para Acesso ao CDE**: Exija autenticação multifator para qualquer acesso administrativo ou remoto que alcance a zona CDE.

---

## 🔗 Integração com Outras Skills

- Para arquitetura de encriptação, FPE (FF1/FF3-1) e Key Wrapping, consulte a skill [cryptography-pqc-standards](..\..\crypto-pki\cryptography-pqc-standards/SKILL.md).
- Para arquitetura de pagamentos, ISO 8583 e gateways no Brasil/Exterior, consulte a skill [financial-transaction-processing](..\..\..\general\domains\financial-transaction-processing/SKILL.md).
- Para controles de IAM e PAM no CDE, consulte a skill [iam-access-management](..\..\cloud-iam\iam-access-management/SKILL.md).
