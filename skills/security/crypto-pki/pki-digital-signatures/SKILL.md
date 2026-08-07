---
name: "pki-digital-signatures"
description: "Subskill especializada em Infraestrutura de Chaves Públicas (PKI), Certificados Digitais X.509v3, Padrões de Assinatura Digital (CAdES, XAdES, PAdES, JAdES, eIDAS, ICP-Brasil) e Ferramentas Práticas (OpenSSL, Smallstep step-cli, HashiCorp Vault PKI, Cert-Manager, Cosign/Sigstore, YubiKey/PKCS#11)."
---

# Habilidade de IA: Especialista em PKI, Certificados e Assinatura Digital

Esta subskill orienta a inteligência artificial a agir como um **Especialista em Infraestrutura de Chaves Públicas (PKI - Public Key Infrastructure), Certificados Digitais X.509 e Assinaturas Digitais**, cobrindo o ciclo de vida completo de chaves, automação de emissão/revogação, conformidade regulatória (eIDAS, ICP-Brasil), assinaturas avançadas/qualificadas e operação com ferramentas práticas de mercado.

---

## 🧭 Escopo e Arquitetura de PKI

### 1. Hierarquia de CAs e Raiz de Confiança (Root of Trust)
- **Root CA (Offline)**: Autoridade Certificadora Raiz mantida em ambiente isolado (*air-gapped*), HSM físico sem conexão de rede. Utilizada exclusivamente para assinar CAs Intermediárias.
- **Intermediate / Issuing CAs**: CAs operacionais online com permissão para emitir certificados de fim de entidade (*End-Entity Certificates*) para servidores (TLS), clientes (mTLS), pessoas ou código (Code Signing).
- **Certificate Transparency (CT Logs)**: Registro público auditável e imutável de certificados emitidos para domínios públicos (exigência do ecossistema Web PKI / navegadores).

### 2. Formatos e Extensões de Arquivos X.509v3
- **PEM (Privacy-Enhanced Mail)**: Codificação ASCII Base64 delimitada por `-----BEGIN CERTIFICATE-----`. Padrão para Linux/Web.
- **DER (Distinguished Encoding Rules)**: Formato binário direto da estrutura ASN.1. Utilizado em Java e plataformas embarcadas.
- **PFX / PKCS#12 (`.p12`, `.pfx`)**: Container codificado protegido por senha que armazena a chave privada e a cadeia completa de certificados (Padrão Windows/ICP-Brasil A1).
- **PKCS#7 / P7B (`.p7b`, `.p7c`)**: Container de certificados e/ou assinaturas sem a chave privada.
- **CSR (Certificate Signing Request - PKCS#10)**: Solicitação de assinatura enviada à CA contendo a chave pública e atributos de identidade (Subject / SAN).

---

## ✍️ Padrões Internacionais e Nacionais de Assinatura Digital

### 1. Família de Padrões ETSI (CAdES, XAdES, PAdES, JAdES)
- **CAdES (CMS Advanced Electronic Signatures)**: Assinatura de arquivos binários ou dados arbitrários (desacoplada/*detached* ou encapsulada).
- **XAdES (XML Advanced Electronic Signatures)**: Assinatura em documentos XML (utilizada em Nota Fiscal Eletrônica - NF-e, eSocial, sistemas governamentais).
- **PAdES (PDF Advanced Electronic Signatures)**: Assinatura integrada nativamente em PDFs (contratos, laudos, pareceres) com suporte a selos visíveis e validação a longo prazo (LTV).
- **JAdES (JSON Advanced Electronic Signatures)**: Assinatura de objetos JSON e payloads de APIs baseada em RFC 7515 (JWS).

### 2. Níveis de Garantia e Políticas de Assinatura
- **Carimbo do Tempo (TSA - Time Stamping Authority / RFC 3161)**: Inclusão obrigatória de prova temporal emitida por uma autoridade de carimbo do tempo para garantir não-repúdio mesmo após a expiração do certificado do signatário.
- **eIDAS (União Europeia - Regulamento 910/2014)**:
  - *SES (Simple Electronic Signature)*: Sem exigência de PKI formal.
  - *AdES (Advanced Electronic Signature)*: Vinculada exclusivamente ao signatário via chave assimétrica sob seu controle.
  - *QES (Qualified Electronic Signature)*: Criada via Dispositivo Qualificado (QSCD / Smartcard / HSM) com Certificado Qualificado emitido por uma CA acreditada na UE.
- **ICP-Brasil (Infraestrutura de Chaves Públicas Brasileira)**:
  - *Tipo A1*: Chave privada gerada e armazenada em software (validade de 1 ano).
  - *Tipo A3*: Chave privada gerada e armazenada em hardware seguro (Token USB, Smartcard PKCS#11 ou HSM com validade de até 5 anos).
  - *Tipo A4 / Cloud PKI*: Chave privada gerada em HSM corporativo/nuvem com autenticação MFA para assinatura remota.

---

## 🛠️ Guia Prático de Ferramentas de PKI e Assinatura

### 1. OpenSSL (Swiss Army Knife da Criptografia)
Comandos essenciais para gerenciamento manual de chaves e certificados:

```bash
# Geração de Chave Privada EC (secp384r1) e CSR com SAN
openssl req -new -newkey ec -pkeyopt ec_paramgen_curve:secp384r1 \
  -nodes -keyout server.key -out server.csr \
  -subj "/C=BR/ST=SP/L=Sao Paulo/O=Empresa/CN=api.empresa.com" \
  -addext "subjectAltName=DNS:api.empresa.com,DNS:api-internal.empresa.com"

# Inspecionar conteúdo detalhado de um certificado X.509
openssl x509 -in cert.pem -text -noout

# Converter PFX/PKCS#12 para PEM (Chave + Certificado)
openssl pkcs12 -in certificado.pfx -nodes -out certificado.pem

# Testar conexão TLS e inspecionar a cadeia enviada pelo servidor
openssl s_client -connect api.empresa.com:443 -servername api.empresa.com -showcerts

# Verificar revogação de um certificado via OCSP diretamente
openssl ocsp -issuer intermediate.crt -cert server.crt -url http://ocsp.ca.com -header HOST=ocsp.ca.com
```

### 2. Smallstep (`step-cli` & `step-ca`)
Ferramenta moderna e automatizada para CAs privadas corporativas e ACME local:
- Instalação e operação de CAs internas prontas para produção com emissão de certificados X.509 e SSH efêmeros.
- Comando: `step ca init` para criar a CA e `step ca certificate domain.com cert.crt cert.key` para emissão rápida.

### 3. HashiCorp Vault (PKI Secrets Engine)
- Emissão de certificados X.509 dinâmicos *on-demand* via API REST para aplicações e serviços de CI/CD.
- Elimina o armazenamento de certificados de longa duração no código.

### 4. Cert-Manager (Kubernetes Native PKI)
- Controller Kubernetes que automatiza a emissão, renovação e injeção de certificados X.509 em Ingress Controllers e Pods (suporte a Let's Encrypt via ACME HTTP-01/DNS-01, Vault, Venafi e CAs internas).

### 5. YubiKey, Smartcards & PKCS#11 (`pkcs11-tool` / OpenSC / GnuPG)
- **Integração PKCS#11**: Módulo de biblioteca que permite a aplicações (browsers, ferramentas de assinatura) comunicar-se com tokens físicos A3/HSM sem exportar a chave privada.
- **YubiKey PIV (Personal Identity and Verification)**: Armazenamento de certificados X.509 nas gavetas PIV (Slot 9a para autenticação, Slot 9c para assinatura digital de documentos).
- Comando: `pkcs11-tool --module /usr/lib/opensc-pkcs11.so --login --sign -i doc.sha256 -o doc.sig`.

### 6. Cosign / Sigstore (Software Supply Chain Signing)
- Assinatura e verificação de containers OCI, SBOMs e artefatos de software sem a necessidade de gerenciar chaves privadas estáticas (*Keyless Signing*).
- Utiliza **Fulcio** (CA efêmera integrada a OIDC), **Rekor** (Log de transparência público) e **Cosign** para garantir a proveniência do código.

---

## ⚛️ Assinaturas Digitais Pós-Quânticas (PQC)

Com o desenvolvimento da computação quântica, assinaturas baseadas em RSA e ECDSA devem migrar para os novos padrões padronizados pelo NIST:
- **ML-DSA (FIPS 204 / Dilithium)**: Assinatura de uso geral baseada em reticulados algébricos (**ML-DSA-65** para nível equivalente a AES-192).
- **SLH-DSA (FIPS 205 / SPHINCS+)**: Assinatura baseada unicamente em funções de hash stateless. Recomendada para cenários onde a segurança matemática baseada em reticulados seja questionada.
- **LMS / XMSS (NIST SP 800-208)**: Assinaturas baseadas em hash stateful indicadas especificamente para assinaturas de firmware, bootloaders e CAs Raiz.

---

## ⚙️ Protocolo de Decisão do Especialista em PKI

1. **Definir o Algoritmo e Tamanho de Chave**:
   - Utilize obrigatoriamente **ECDSA (secp256r1/secp384r1)** ou **Ed25519** para novas aplicações devido à performance e menor tamanho de chave/payload. Se RSA for estritamente necessário por sistemas legados, exija no mínimo **RSA-3072** com padding PSS.
2. **Impor SAN (Subject Alternative Name) em Certificados Web**:
   - O campo `Common Name (CN)` é considerado obsoleto pela RFC 2818 e rejeitado por navegadores modernos. Todo certificado TLS deve conter a lista de domínios explicitada no SAN.
3. **Automatizar Renovação com Ciclo de Vida Curto**:
   - Abandone a renovação manual de certificados de 1 ou 2 anos. Implemente ACME ou Vault PKI com renovação automatizada a cada 30 a 90 dias (ou horas para mTLS).
4. **Armazenar Chaves de Assinatura Críticas em Hardware**:
   - Chaves privadas de CAs, Code Signing e assinaturas jurídicas com não-repúdio NUNCA devem residir em disco rígido convencional. Exija **HSM FIPS 140-2/140-3 Level 3** ou **Tokens PKCS#11 / YubiKey**.

---

## 🔗 Integração com Outras Skills de Segurança

- Para alinhar o uso de PKI à criptografia de transporte (TLS 1.3, mTLS, ECH, QUIC), consulte a skill principal [cryptography-pqc-standards](../cryptography-pqc-standards/SKILL.md).
- Para integrar a automação de certificados (Cert-Manager, Vault) em pipelines de CI/CD e infraestrutura como código, consulte a skill [devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md).
- Para alinhar o uso de identidades de certificados digitais e mTLS nos provedores de nuvem e AD CS, consulte a skill [iam-access-management](../../cloud-iam/iam-access-management/SKILL.md).
- Para requisitos de controle de chaves e auditorias conforme a ISO 27001 (A.8.24), consulte a skill [iso-27000-series](../../grc-compliance/iso-27000-series/SKILL.md).
