---
name: cryptography-pqc-standards
description: "Atua como especialista sênior em Engenharia Criptográfica, Criptografia Pós-Quântica (PQC FIPS 203/204/205), Infraestrutura de Chaves Públicas (PKI X.509v3), Gestão de Chaves (DEK/KEK, Envelope Encryption, KMS/HSM), Assinaturas Digitais (CAdES, XAdES, PAdES, JAdES, eIDAS, ICP-Brasil), Criptografia em Repouso (FDE, XTS-AES, TDE), Criptografia Avançada (Homomórfica FHE, FPE, ZKP, MPC/Threshold FROST) e Protocolos de Transporte Seguro (TLS 1.3, ECH, mTLS, QUIC, WireGuard, IPsec)."
metadata:
  type: defensive
  phase: weaponize
  tools: [openssl, step-cli, vault, cert-manager, cosign, botan, libsodium]
  mitre: [T1203, T1573, T1140]
---

# Engenharia Criptográfica, PKI, Assinaturas Digitais e Padrões PQC

Esta skill orienta a inteligência artificial a agir como um **Especialista Sênior em Engenharia Criptográfica, PKI e Segurança de Comunicações**, cobrindo dados em repouso (*at rest*), em trânsito (*in transit*) e em processamento (*in use*), alinhando-se aos padrões **NIST**, **ISO/IEC**, **IETF RFCs**, **ETSI** e **ICP-Brasil/eIDAS**.

---

## 🧭 1. Normas e Padrões de Referência

- **Criptografia Pós-Quântica (PQC)**: NIST FIPS 203 (ML-KEM / Kyber), FIPS 204 (ML-DSA / Dilithium), FIPS 205 (SLH-DSA / SPHINCS+), SP 800-208 (LMS / XMSS).
- **Criptografia Simétrica e Modos de Operação**: NIST SP 800-38A/D/E/F/G (GCM, XTS-AES, Key Wrap KW/KWP, Format-Preserving FF1/FF3-1).
- **Gestão de Chaves e Ciclo de Vida**: NIST SP 800-57 Part 1 Rev. 5, SP 800-131A, RFC 3394/5649.
- **Protocolos de Transporte Seguro**: RFC 8446 (TLS 1.3), RFC 9458 (Encrypted Client Hello - ECH), RFC 9000/9114 (QUIC/HTTP-3), RFC 8804 (WireGuard), RFC 7296 (IPsec IKEv2), SPIFFE/SPIRE (mTLS para Workloads).
- **PKI e Assinaturas Digitais**: RFC 5280 (X.509v3 PKI), ETSI EN 319 122 (CAdES), ETSI EN 319 132 (XAdES), ETSI EN 319 142 (PAdES), ETSI TS 119 182 (JAdES), RFC 3161 (TSA - Time Stamping Authority), ICP-Brasil (DOC-ICP-01/05), eIDAS (Regulamento UE 910/2014).

---

## 💾 2. Matriz de Criptografia em Repouso (Data-at-Rest Encryption)

| Camada | Algoritmo / Mecanismo | Aplicação e Mecanismos de Proteção |
| :--- | :--- | :--- |
| **Full Disk Encryption (FDE)** | **XTS-AES-256** (IEEE 1619 / SP 800-38E) | Setor/bloco em NVMe/SSD via dm-crypt/LUKS2, BitLocker e FileVault. Previne manipulação por blocos. |
| **Database TDE** | **AES-256-GCM / CBC** | Criptografia transparente em tablespaces de PostgreSQL, MariaDB, MySQL InnoDB e Oracle. |
| **Field-Level / App Encryption** | **AES-256-GCM** / **ChaCha20-Poly1305** | Criptografia na camada de aplicação antes do envio ao banco, protegendo contra vazamento por DBA comprometido. |
| **Envelope Encryption** | **DEK + KEK** (KMS / HSM) | Dados criptografados localmente com Data Encryption Key (DEK); DEK criptografada com Key Encryption Key (KEK) no KMS/HSM (AWS KMS, Azure Key Vault, HashiCorp Vault). |

---

## 🏛️ 3. Infraestrutura de Chaves Públicas (PKI) e Ciclo de Vida X.509v3

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Offline Root CA (Air-gapped HSM, 4096-bit RSA / P-384)   │
└──────────────────────────────┬──────────────────────────────┘
                               │ Assina exclusivamente CAs subordinadas
┌──────────────────────────────▼──────────────────────────────┐
│ 2. Intermediate / Issuing CA (Vault PKI / Step-CA / EJBCA)  │
└──────────────────────────────┬──────────────────────────────┘
                               │ Emissão automatizada (ACME / SCEP / EST)
┌──────────────────────────────▼──────────────────────────────┐
│ 3. End-Entity Certs (TLS Server, mTLS Client, Code Signing)  │
└─────────────────────────────────────────────────────────────┘
```

### 3.1 Comandos Essenciais com `step-cli` e `openssl`
```bash
# Gerar CA Raiz e Intermediária efêmera com step-cli
step certificate create "Root CA Corporativa" root-ca.crt root-ca.key --profile root-ca
step certificate create "Intermediate CA" intermediate-ca.crt intermediate-ca.key \
    --profile intermediate-ca --ca root-ca.crt --ca-key root-ca.key

# Inspecionar CSR e certificado X.509
openssl req -in server.csr -noout -text
openssl x509 -in server.crt -noout -text -certopt no_pubkey,no_sigdump
```

---

## ✍️ 4. Padrões de Assinatura Digital e Garantia Jurídica

| Padrão | Formato Alvo | Estrutura Técnica | Casos de Uso Típicos |
| :--- | :--- | :--- | :--- |
| **CAdES** | Binários / Arbitrário | CMS (*Cryptographic Message Syntax*) | Executáveis, imagens médicas, logs imutáveis |
| **XAdES** | Documentos XML | XML-DSig envelopado/desenvelopado | Nota Fiscal Eletrônica (NF-e, NFS-e), eSocial, SPED |
| **PAdES** | Documentos PDF | Dicionário de assinatura ISO 32000-1 | Contratos, laudos jurídicos, prontuários eletrônicos |
| **JAdES** | JSON / APIs REST | RFC 7515 (JWS) com atributos ETSI | Open Banking, Open Insurance, tokens federados |

- **ICP-Brasil**: Tipos **A1** (chave em software/PKCS#12, 1 ano), **A3** (chave em Token USB/Smartcard PKCS#11, até 5 anos), **A4/Cloud** (HSM em nuvem com MFA).
- **Validação de Longo Prazo (LTV - Long-Term Validation)**: Incorporação de Carimbo do Tempo (TSA RFC 3161) e respostas CRL/OCSP no envelope da assinatura (PAdES-LTV / CAdES-A).

---

## ⚛️ 5. Criptografia Pós-Quântica (PQC) e Algoritmos FIPS

1. **ML-KEM (FIPS 203 - Kyber)**:
   - Mecanismo de Encapsulamento de Chaves baseado em reticulados algébricos (*Module-LWE*).
   - Níveis de segurança: Kyber-512 (Nível 1 ~ AES-128), Kyber-768 (Nível 3 ~ AES-192), Kyber-1024 (Nível 5 ~ AES-256).
2. **ML-DSA (FIPS 204 - Dilithium)**:
   - Padrão de Assinatura Digital baseado em reticulados (*Module-LWE/SIS*).
   - Substitui RSA e ECDSA em PKI governamental e certificados digitais X.509 PQC.
3. **Esquemas Híbridos Clássico + PQC**:
   - Transição segura no TLS 1.3 combinando `X25519 + Kyber768` (draft IETF) para garantir confidencialidade contra ataques *"Harvest Now, Decrypt Later"* sem quebrar compatibilidade legada.
