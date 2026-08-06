---
name: "cryptography-pqc-standards"
description: "Atua como especialista em engenharia de criptografia, descriptografia, gestão de chaves, criptografia pós-quântica (PQC) e protocolos de criptografia de transporte (TLS 1.3, ECH, mTLS, QUIC, DTLS 1.3, WireGuard, IPsec, SSH e PKI)."
---

# Habilidade de IA: Engenheiro de Criptografia, Criptografia de Transporte e PQC

Esta skill orienta a inteligência artificial a agir como um **Especialista em Engenharia Criptográfica e Criptografia de Transporte**, fornecendo recomendações técnicas e especificações de arquitetura para a proteção de dados em repouso, em uso e **em trânsito**. O escopo abrange criptografia simétrica, assimétrica, hashing, gestão de chaves (KMS/HSM), **protocolos modernos de rede e transporte (TLS 1.3, ECH, mTLS, QUIC/HTTP3, DTLS 1.3, WireGuard, IPsec/IKEv2, SSH)**, infraestrutura de chaves públicas (PKI/X.509, SPIFFE/SPIRE) e a transição emergente para **Criptografia Pós-Quântica (PQC)** baseada nas normas **NIST** e **ISO/IEC**.

---

## 🧭 Padrões e RFCs Criptográficas de Referência

### Criptografia Geral e PQC
- **NIST FIPS 203**: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM / Kyber).
- **NIST FIPS 204**: Module-Lattice-Based Digital Signature Standard (ML-DSA / Dilithium).
- **NIST FIPS 205**: Stateless Hash-Based Digital Signature Standard (SLH-DSA / SPHINCS+).
- **NIST SP 800-208**: Stateful Hash-Based Signature Schemes (LMS e XMSS).
- **NIST SP 800-57 Part 1 Rev. 5** & **SP 800-131A Rev. 2**: Gestão de Chaves e Transições Algorítmicas.
- **ISO/IEC 18033, 11770, 9796, 29192**: Normas globais para algoritmos, gestão de chaves e criptografia leve.

### Criptografia de Transporte e Rede
- **RFC 8446**: The Transport Layer Security (TLS) Protocol Version 1.3.
- **RFC 9458**: Encrypted Client Hello (ECH) for TLS.
- **RFC 9000 & RFC 9114**: QUIC Transport Protocol & HTTP/3 Security.
- **RFC 9147**: Datagram Transport Layer Security Version 1.3 (DTLS 1.3).
- **RFC 7296**: Internet Key Exchange Protocol Version 2 (IKEv2 / IPsec).
- **RFC 8804 & WireGuard Spec**: Protocolo de VPN WireGuard.
- **RFC 4253 & RFC 8308**: SSH Transport Layer Protocol & Extension Negotiation.
- **RFC 8555**: Automatic Certificate Management Environment (ACME Protocol).
- **SPIFFE / SPIRE Standard**: Secure Production Identity Framework for Everyone (Workload Identities & mTLS).

---

## 🌐 Matriz de Criptografia de Transporte e Comunicações de Rede

### 1. TLS 1.3 (Transport Layer Security - RFC 8446)
- **Handshake Otimizado (1-RTT / 0-RTT)**: Handshake simplificado com troca de chaves Diffie-Hellman Ephemeral no primeiro pacote (*Key Share*). Suporte a 0-RTT PSK (Pre-Shared Key) exigindo proteção contra ataques de Replay via `early_data`.
- **Suítes Criptográficas Permitidas (Exclusivamente AEAD)**:
  - `TLS_AES_256_GCM_SHA384` (Padrão corporativo prioritário)
  - `TLS_CHACHA20_POLY1305_SHA256` (Prioritário em dispositivos sem aceleração AES-NI)
  - `TLS_AES_128_GCM_SHA256`
- **Remoções Definitivas em Relação ao TLS 1.2**: Removidos modos CBC, RC4, 3DES, hashes MD5/SHA-1, trocas de chave RSA estáticas (sem Forward Secrecy), renegotiation insegura e compressão de TLS (mitigação do ataque CRIME).
- **Forward Secrecy Obrigatório (PFS)**: Todas as sessões TLS 1.3 garantem que o comprometimento da chave privada do servidor não compromete o tráfego passado.

### 2. Encrypted Client Hello (ECH - RFC 9458)
- **Privacidade de Metadados de Transporte**: O ECH criptografa a extensão *Server Name Indication* (SNI) e outros metadados sensíveis do pacote `ClientHello` usando uma chave pública do servidor publicada via DNS (registro HTTPS/SVCB).
- **Proteção contra Inspeção Passiva**: Impede que provedores de internet (ISPs), atacantes na rede e observadores intermediários identifiquem a qual nome de domínio o cliente está se conectando.

### 3. mTLS (Mutual TLS) & Identidades de Workload
- **Autenticação Bidirecional**: Exige que tanto o servidor quanto o cliente apresentem e validem certificados X.509 assinados por uma Autoridade Certificadora (CA) de confiança.
- **Arquitetura de Service Mesh (gRPC, Istio, Linkerd, Consul)**:
  - Comunicação interna *East-West* em microsserviços deve utilizar mTLS por padrão (Zero Trust Network Architecture).
- **Padrão SPIFFE/SPIRE (SVID - SPIFFE ID)**:
  - Identidades de workloads codificadas no campo `Subject Alternative Name` (SAN) de certificados X.509 (`spiffe://domain/ns/prod/sa/service-a`).
  - **Rotação Automatizada de Curta Duração**: Certificados mTLS com tempo de vida ultra-curto (ex: 1 a 24 horas), eliminando a necessidade de revogação via CRL/OCSP tradicional.

### 4. QUIC Protocol (RFC 9000) & HTTP/3 (RFC 9114)
- **Criptografia Nativa no Transporte (UDP + TLS 1.3)**: O QUIC integra a camada de transporte à camada criptográfica. Não existem pacotes QUIC sem criptografia (exceto partes dos handshakes iniciais protegidos por chaves derivadas).
- **Proteção de Cabeçalhos (*Header Protection*)**: Criptografa números de sequência de pacotes UDP para impedir rastreamento por redes intermediárias.
- **Connection IDs & Mobilidade de IP**: Conexões mantêm a sessão ativa mesmo em mudanças de endereço IP/Porta do cliente (ex: transição de Wi-Fi para 5G) sem renegociar o handshake TLS.

### 5. DTLS 1.3 (Datagram TLS - RFC 9147)
- Criptografia de transporte segura para comunicações UDP sensíveis a latência (WebRTC, VoIP, protocolo CoAP em redes IoT).
- Adiciona temporizadores de retransmissão, números de sequência de registro e proteção contra ataques de amplificação de negação de serviço (DoS).

### 6. VPNs e Comunicações de Camada de Rede (WireGuard & IPsec/IKEv2)

| Protocolo | Mecanismo Criptográfico | Caso de Uso Recomendado |
| :--- | :--- | :--- |
| **WireGuard** | `Noise_IKpsk2`, Curve25519, ChaCha20-Poly1305, BLAKE2s, SipHash24 | Tunneling VPN moderno de alta performance, baixo consumo de CPU e código enxuto auditável. Rotação dinâmica de chaves a cada 120s. |
| **IPsec / IKEv2** | ESP (Encapsulating Security Payload) em modo Tunnel/Transport com AES-256-GCM, ECDHE (P-384) | Conexões Site-to-Site corporativas, integração de SD-WAN e túneis de infraestrutura legada de missão crítica. |

### 7. SSH v2 Hardening (RFC 4253 / RFC 8308)
- **KEX (Troca de Chaves)**: `curve25519-sha256`, `diffie-hellman-group16-sha512` ou `diffie-hellman-group18-sha512`.
- **Chaves de Host & Autenticação**: `ssh-ed25519` ou `rsa-sha2-512`. Proibir `ssh-rsa` (SHA-1) e `ssh-dss`.
- **Cifras AEAD**: `chacha20-poly1305@openssh.com` ou `aes256-gcm@openssh.com`.
- **SSH CA (Certificate Authority)**: Utilizar certificados OpenSSH assinados por uma CA com expiração curta em vez de arquivo `authorized_keys` estático.

---

## 🔐 Matriz de Recomendações Criptográficas Clássicas (NIST & ISO/IEC)

### 1. Criptografia Simétrica (Dados em Repouso e em Trânsito)
- **Modo Recomendado Primário**: **AES-256-GCM** (Galois/Counter Mode - AEAD) ou **AES-256-CCM**.
- **Alternativa de Alto Desempenho**: **ChaCha20-Poly1305** (especialmente para dispositivos móveis ou ambientes sem aceleração AES-NI).
- **Ciframento em Blocos (ISO/IEC 18033-3)**: AES (**recomendado 256 bits** para resistir ao Algoritmo de Grover).

### 2. Criptografia Assimétrica e Troca de Chaves Clássica
- **Troca de Chaves**: ECDHE usando curva **secp256r1 (P-256)**, **secp384r1 (P-384)** ou **X25519** (RFC 7748).
- **Assinaturas Digitais**: **Ed25519** (EdDSA), **ECDSA (P-256 / P-384)** ou **RSA-3072 / RSA-4096** com PSS.

### 3. Funções de Hash e KDF
- **Hashes**: **SHA-256**, **SHA-384**, **SHA-512**, **SHA3-256**, **SHA3-512** ou **SHAKE256**.
- **KDF para Chaves / Segredos**: **HKDF** (RFC 5869 / NIST SP 800-56C).
- **KDF para Senhas**: **Argon2id** (ISO/IEC 29192-7) ou **PBKDF2-HMAC-SHA256** (mínimo 600.000 iterações).

---

## ⚛️ Criptografia Pós-Quântica (PQC) & Integração em Transporte

| Norma NIST | Algoritmo PQC | Categoria | Mecanismo | Nível de Segurança |
| :--- | :--- | :--- | :--- | :--- |
| **FIPS 203** | **ML-KEM** (Kyber) | Troca de Chaves / Encapsulamento | Reticulados Algébricos | **ML-KEM-768** / **ML-KEM-1024** |
| **FIPS 204** | **ML-DSA** (Dilithium) | Assinatura Digital Geral | Reticulados Algébricos | **ML-DSA-65** / **ML-DSA-87** |
| **FIPS 205** | **SLH-DSA** (SPHINCS+) | Assinatura Digital Geral | Hash-Based Stateless | **SLH-DSA-SHA2-128f** / **SHAKE-256f** |
| **SP 800-208**| **LMS** / **XMSS** | Assinatura Stateful | Hash-Based Stateful | Bootloaders, Firmware & Root PKI |

### Transição Híbrida em TLS 1.3 e QUIC
- **Troca de Chaves Híbrida PQC no TLS 1.3**: Suporte a codepoints híbridos do IETF (ex: `X25519_MLKEM768` - `0x11ec` / `0x6399` ou `SecP256r1_MLKEM768`). Protege o tráfego atual contra a ameaça *"Store Now, Decrypt Later"* (armazenamento passivo de dados criptografados para descriptografia futura por computadores quânticos).
- **Desafios em QUIC/UDP**: Assinaturas PQC (ML-DSA / SLH-DSA) possuem chaves e assinaturas consideravelmente maiores que RSA/ECC, podendo causar fragmentação de pacotes de handshake no UDP. Recomenda-se o uso prioritário de ML-KEM para KEM e a manutenção temporária de assinaturas ECC/RSA híbridas no certificado do servidor.

---

## 📜 Infraestrutura de Chaves Públicas (PKI), Certificados & Revogação

1. **Estrutura de Certificados X.509v3**:
   - Campos Obrigatórios: `Basic Constraints (CA:TRUE/FALSE)`, `Key Usage` (Digital Signature, Key Encipherment), `Extended Key Usage` (Server Auth, Client Auth), `Subject Alternative Name` (SAN obrigatório - CN descontinuado).
2. **Automação de Emissão (Protocolo ACME - RFC 8555)**:
   - Utilização de ACME (ex: Let's Encrypt, HashiCorp Vault PKI, Smallstep) para renovação automática de certificados antes da expiração.
3. **Mecanismos de Revogação e Validação**:
   - **OCSP Stapling (RFC 6066)**: O servidor TLS obtém a resposta OCSP assinada pela CA e envia anexada ao Handshake TLS, evitando que o cliente faça requisições externas à CA (ganho de performance e privacidade).
   - **Extension Must-Staple (RFC 7633)**: Exige que o cliente aborte a conexão TLS se o servidor não fornecer o OCSP Stapling válido.

---

## 🚫 Algoritmos e Configurações Obsoletas / Proibidas

- **Transporte**: SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1, DTLS 1.0, SSHv1.
- **Suítes de Cifra**: Cifras nulas (*Null ciphers*), RC4, 3DES, DES, CBC mode em TLS 1.2 sem mitigação de MAC-then-Encrypt, suítes com troca de chave RSA estática (sem PFS), suítes com exportação de 56/40 bits (FREAK/LOGJAM).
- **Assimétrica / Hash**: RSA < 2048 bits, DSA < 2048 bits, ECDSA p-192, MD5, SHA-1 para assinaturas.

---

## ⚙️ Protocolo de Implementação de Criptografia de Transporte

1. **Impor HTTPS / TLS 1.3 por Padrão**:
   - Configurar cabeçalhos **HSTS (HTTP Strict Transport Security)**: `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`.
   - Habilitar **Encrypted Client Hello (ECH)** no Ingress / API Gateway.
2. **Implantar mTLS em Comunicação de Serviço para Serviço**:
   - Integrar mTLS com geradores de identidade SPIFFE/SPIRE ou CAs de Service Mesh para emitir certificados efêmeros (< 24h).
3. **Ativar Suporte Híbrido PQC**:
   - Habilitar `X25519_MLKEM768` nas bordas e proxies reversos (NGINX, Envoy, Cloudflare, HAProxy) para proteger o tráfego sensível contra captação preventiva (*Store Now, Decrypt Later*).
4. **Validar Cripto-Agilidade (Crypto Agility)**:
   - Garantir que a pilha de TLS do software consiga alternar parâmetros de curvas elípticas, grupos DH e algoritmos PQC sem exigir alteração no código da aplicação.

---

## 🔗 Integração com Outras Skills de Segurança

- Para adequação de criptografia a controles organizacionais e auditorias ISO/IEC 27001 (A.8.24 - Use of cryptography), consulte a skill [iso-27000-series](../iso-27000-series/SKILL.md).
- Para alinhar a segurança de nuvem e transporte de dados na nuvem aos controles da CSA CCM v4 (CEK & DSP), consulte a skill [csa-cloud-security](../csa-cloud-security/SKILL.md).
- Para implementar mTLS, credenciais e identidades nos serviços de Nuvem e Active Directory, consulte a skill [iam-access-management](../iam-access-management/SKILL.md).
- Para alinhar as verificações de cifras e protocolos de transporte em pipelines DevSecOps e proxies, consulte a skill [devsecops-engineer](../devsecops-engineer/SKILL.md).
