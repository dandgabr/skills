---
name: "cryptography-pqc-standards"
description: "Atua como especialista em engenharia de criptografia, descriptografia, gestão de chaves (DEK/KEK/Envelope Encryption), criptografia em repouso (FDE, XTS-AES, TDE), criptografia avançada (Homomórfica, FPE, Searchable Encryption, ZKP, MPC/Threshold), criptografia pós-quântica (PQC) e protocolos de criptografia de transporte (TLS 1.3, ECH, mTLS, QUIC, DTLS 1.3, WireGuard, IPsec, SSH e PKI)."
---

# Habilidade de IA: Engenheiro de Criptografia, Gestão de Chaves, Criptografia em Repouso, Avançada e PQC

Esta skill orienta a inteligência artificial a agir como um **Especialista em Engenharia Criptográfica, Criptografia de Dados e Comunicações**, fornecendo recomendações técnicas e especificações de arquitetura para a proteção de dados em repouso (at rest), em trânsito (in transit) e em processamento/uso (in use/computation). 

O escopo abrange criptografia simétrica e assimétrica clássica, **criptografia em repouso e armazenamento (FDE, XTS-AES, TDE, SSE)**, **hierarquia e gestão de chaves (DEK, KEK, Envelope Encryption, KMS, HSM, Key Wrapping)**, **tecnologias avançadas e modernas (Criptografia Homomórfica FHE/PHE, Format-Preserving Encryption FF1/FF3-1, Searchable Encryption, ZKP/zk-SNARKs, Threshold Signatures/FROST, MPC)**, **protocolos modernos de transporte (TLS 1.3, ECH, mTLS, QUIC, WireGuard, IPsec, SSH)**, infraestrutura PKI/X.509 e a transição para **Criptografia Pós-Quântica (PQC - FIPS 203/204/205)** baseada nas normas **NIST**, **ISO/IEC** e referências técnicas de mercado (como *Serious Cryptography* por Jean-Philippe Aumasson).

---

## 🧭 Padrões, RFCs e Especificações de Referência

### Criptografia Geral, Gestão de Chaves e Armazenamento (At-Rest & Advanced)
- **NIST SP 800-38E**: Recommendation for Block Cipher Modes of Operation: The XTS-AES Mode for Confidentiality on Storage Devices.
- **NIST SP 800-38F**: Recommendation for Block Cipher Modes of Operation: Methods for Key Wrapping (AES-KW, AES-KWP).
- **NIST SP 800-38G Rev. 1**: Recommendation for Block Cipher Modes of Operation: Methods for Format-Preserving Encryption (FF1 e FF3-1).
- **NIST SP 800-57 Part 1 Rev. 5** & **SP 800-131A Rev. 2**: Recomendação para Gestão de Chaves Criptográficas e Transições Algorítmicas.
- **NIST SP 800-108 Rev. 1**: Recommendation for Key Derivation Using Pseudorandom Functions.
- **RFC 3394 & RFC 5649**: Advanced Encryption Standard (AES) Key Wrap & Key Wrap with Padding Algorithm.
- **IEEE 1619**: Standard for Cryptographic Protection of Data on Block-Oriented Storage Devices (XTS Mode).
- **ISO/IEC 18033 (Partes 1-7)** & **ISO/IEC 11770**: Algoritmos de criptografia e gestão de chaves.
- **RFC 9591 / FROST Spec**: Flexible Round-Optimized Schnorr Threshold Signatures.

### Criptografia Pós-Quântica (PQC)
- **NIST FIPS 203**: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM / Kyber).
- **NIST FIPS 204**: Module-Lattice-Based Digital Signature Standard (ML-DSA / Dilithium).
- **NIST FIPS 205**: Stateless Hash-Based Digital Signature Standard (SLH-DSA / SPHINCS+).
- **NIST SP 800-208**: Stateful Hash-Based Signature Schemes (LMS e XMSS).

### Criptografia de Transporte e Comunicações
- **RFC 8446**: Transport Layer Security (TLS) Protocol Version 1.3.
- **RFC 9458**: Encrypted Client Hello (ECH) for TLS.
- **RFC 9000 & RFC 9114**: QUIC Transport Protocol & HTTP/3 Security.
- **RFC 9147**: Datagram Transport Layer Security Version 1.3 (DTLS 1.3).
- **RFC 7296**: Internet Key Exchange Protocol Version 2 (IKEv2 / IPsec).
- **RFC 8804 & WireGuard Spec**: Protocolo de VPN WireGuard.
- **RFC 4253 & RFC 8308**: SSH Transport Layer Protocol & Extension Negotiation.
- **SPIFFE / SPIRE Standard**: Workload Identities & mTLS.

## 💾 Matriz de Criptografia em Repouso (Data-at-Rest Encryption)

| Camada | Mecanismo Criptográfico / Algoritmo | Descrição e Caso de Uso |
| :--- | :--- | :--- |
| **Full Disk Encryption (FDE)** | **XTS-AES-256** (IEEE 1619 / SP 800-38E) | Proteção em nível de bloco/setor de disco físico ou NVMe. Utiliza um *tweak* (número do setor/bloco) para evitar ataques de substituição e rearranjo de blocos. Implementado em **LUKS2** (dm-crypt), **BitLocker** e **FileVault**. |
| **Database TDE (Transparent)** | **AES-256-CBC / AES-256-GCM** | Criptografia em nível de página/tablespace no motor do banco de dados (ex: PostgreSQL, MySQL/InnoDB TDE, Oracle TDE, SQL Server TDE). Transparente para as aplicações. |
| **Field-Level / Application Encryption** | **AES-256-GCM** ou **ChaCha20-Poly1305** | Criptografia no lado da aplicação antes do armazenamento no BD. Garante proteção *End-to-End* contra comprometimento do DBA ou vazamento de backups do banco de dados. |
| **Object & Cloud Storage** | **AWS**: SSE-S3 / SSE-KMS / SSE-C<br>**GCP**: GMEK / CMEK / CSEK<br>**Azure**: MMK / CMK / CPK | Proteção de objetos em buckets e blobs de nuvem (**AWS S3**, **GCP Cloud Storage Buckets**, **Azure Blob Storage**). Suporta chaves gerenciadas pelo provedor (SSE-S3, GMEK, MMK), chaves gerenciadas pelo cliente via Cloud KMS (SSE-KMS, CMEK, CMK) e chaves fornecidas pelo cliente por requisição (SSE-C, CSEK, CPK) para total Zero-Trust. |

---

## 🔑 Hierarquia e Gestão de Chaves (DEK, KEK e Envelope Encryption)

### 1. Padrão Envelope Encryption (Criptografia em Envelope)
A criptografia direta de grandes volumes de dados usando chaves mestras centralizadas é ineficiente e cria riscos de vazamento. O padrão **Envelope Encryption** separa a criptografia dos dados da proteção das chaves:

1. **DEK (Data Encryption Key)**:
   - Chave simétrica efêmera (AES-256-GCM) gerada localmente por objeto, arquivo ou registro para criptografar os dados em alta velocidade.
   - A DEK plana é descartada da memória imediatamente após a criptografia/descriptografia.
2. **KEK (Key Encryption Key)**:
   - Chave de proteção gerenciada dentro do KMS/HSM.
   - Utilizada exclusivamente para criptografar (*wrap*) e descriptografar (*unwrap*) as DEKs das aplicações.
3. **MEK / Root Key (Master Encryption Key)**:
   - Chave raiz mantida no nível mais elevado do HSM físico (FIPS 140-3 Level 3 ou Level 4). Nunca sai do hardware.

```
       +---------------------------------------------+
       |   HSM / KMS (FIPS 140-3 Level 3)           |
       |   +---------------------------------------+ |
       |   | Root Key (MEK) -> Criptografa KEK     | |
       |   +---------------------------------------+ |
       |   | Key Encryption Key (KEK)              | |
       +---+------------------+----------------------+
                              | (Wrap / Unwrap DEK)
                              v
       +---------------------------------------------+
       |   Aplicação / Microserviço                   |
       |   - Gera DEK Simétrica (AES-256)             |
       |   - Criptografa Payload com DEK              |
       |   - Armazena: [ Payload Criptografado ] +    |
       |               [ DEK Criptografada (EncDEK) ]  |
       +---------------------------------------------+
```

### 2. Normas de Key Wrapping (AES-KW & AES-KWP)
- **AES-KW (NIST SP 800-38F / RFC 3394)**: Algoritmo determinístico com autenticação sintética para encapsular chaves simétricas de 128, 192 ou 256 bits usando AES sem necessidade de IV explícito.
- **AES-KWP (NIST SP 800-38F / RFC 5649)**: Variação com suporte a *padding* para proteger segredos de tamanhos arbitrários ou não múltiplos de 64 bits (ex: chaves RSA ou dados de configuração).

### 3. Ciclo de Vida da Chave (NIST SP 800-57 Part 1)
- **Geração**: Utilizar geradores de números pseudo-aleatórios criptográficos (CSPRNG) alimentados por fontes de entropia do SO (`/dev/urandom`, `getrandom()`, `CryptGenRandom()`) ou HSMs.
- **Rotação de Chaves (Key Rotation)**:
  - **Rotação de KEK**: Rotação periódica (ex: a cada 12 meses) sem a necessidade de re-criptografar todos os dados armazenados; basta fazer o *re-wrapping* das DEKs existentes com a nova versão da KEK.
  - **Re-encryption de DEK**: Re-criptografia em segundo plano dos payloads para trocar DEKs antigas em atendimento a políticas de compliance.
- **Crypto-Shredding (Destruição Criptográfica)**:
  - Apagamento definitivo e irrecuperável da KEK ou DEK associada a um usuário/tenant específico. Torna os dados criptografados permanentemente inacessíveis, garantindo o "Direito ao Esquecimento" exigido pela LGPD / GDPR.

---

## 🧠 Criptografia Avançada, Computação Segura e Privacidade

### 1. Criptografia Homomórfica (Homomorphic Encryption - HE)
Permite executar operações matemáticas e computações diretamente sobre dados criptografados sem a necessidade de descriptografá-los previamente:

- **FHE (Fully Homomorphic Encryption)**: Suporta adições e multiplicações arbitrárias sobre dados cifrados (Esquemas: **BGV**, **BFV**, **CKKS** para números reais/ponto flutuante, **TFHE** para circuitos booleanos rápidos). Permite processar dados sensíveis (ex: histórico médico, score de crédito) em nuvens não confiáveis com privacidade total.
- **PHE (Partially Homomorphic Encryption)**: Suporta apenas um tipo de operação (ex: **Paillier** para adição de valores cifrados; **RSA não-preenchido** / **ElGamal** para multiplicação). Alta eficiência comparada ao FHE.
- **SHE (Somewhat Homomorphic Encryption)**: Suporta um número limitado e pré-determinado de adições e multiplicações antes que o ruído criptográfico invalide a mensagem.

### 2. Format-Preserving Encryption (FPE - NIST SP 800-38G Rev. 1)
- **Algoritmos FF1 e FF3-1**: Criptografam dados estruturados (como números de cartão de crédito - PAN de 16 dígitos, CPF, SSN ou datas) produzindo um texto cifrado que **preserva exatamente a mesma sintaxe, tipo de caractere e tamanho** do dado original.
- **Caso de Uso**: Permite proteger dados de PII em bancos de dados legados ou sistemas terceiros sem a necessidade de alterar *schemas* de tabelas, validações de tamanho ou tipos de colunas em banco de dados.

### 3. Searchable Encryption (Criptografia Pesquisável)
- **SSE (Symmetric Searchable Encryption)** & **PEKS (Public Key Encryption with Keyword Search)**: Permite que um servidor ou banco de dados execute buscas por palavras-chave ou consultas por intervalo sobre documentos/registros criptografados **sem que o servidor aprenda o conteúdo em texto claro** do banco ou das palavras pesquisadas.
- Utiliza índices invertidos criptografados (trapdoors) para responder a buscas booleanas mantendo vazamento de metadados minimizado.

### 4. Zero-Knowledge Proofs (ZKP - Provas de Conhecimento Zero)
Protocolos criptográficos onde uma parte (*Prover*) pode provar para outra parte (*Verifier*) que uma determinada afirmação é verdadeira sem revelar nenhuma informação além da própria veracidade da afirmação:

- **zk-SNARKs (Succinct Non-Interactive Argument of Knowledge)**: Provas não-interativas extremamente pequenas e de verificação rápida. Utilizado em moedas de privacidade (Zcash), L2 Scaling em Ethereum (ZK-Rollups) e sistemas de identidade anônima. Algoritmos: Groth16, PLONK (exigem *trusted setup* ou setup transparente).
- **zk-STARKs (Scalable Transparent ARguments of Knowledge)**: Não exigem *trusted setup* inicial e são inerentemente resistentes a computadores quânticos (baseados em funções de hash).
- **Protocolo de Schnorr e Transformação de Fiat-Shamir**: Converte provas de conhecimento zero interativas de posse de uma chave discreta em assinaturas digitais ou provas não-interativas.

### 5. Criptografia Limiar (Threshold Cryptography), Secret Sharing & MPC
- **Shamir's Secret Sharing (SSS)**: Algoritmo para dividir um segredo $S$ em $n$ partes (shares), sendo necessárias no mínimo $k$ partes ($k \le n$) para reconstruir o segredo. Qualquer combinação com menos de $k$ partes revela zero informação sobre $S$.
- **Threshold Signatures (TSS / FROST / Threshold ECDSA)**: Permite que um grupo de $n$ partes assine conjuntamente uma mensagem se pelo menos $k$ partes colaborarem. A chave privada completa **nunca é remontada em um único servidor ou memória**. Exemplo: **FROST** (RFC 9591) para assinaturas Schnorr.
- **MPC (Multi-Party Computation)**: Computação multipartidária segura onde múltiplos participantes computam conjuntamente uma função sobre suas entradas mantendo essas entradas totalmente privadas entre si.

---

## 🌐 Matriz de Criptografia de Transporte e Comunicações de Rede

### 1. TLS 1.3 (Transport Layer Security - RFC 8446)
- **Handshake Otimizado (1-RTT / 0-RTT)**: Troca de chaves Ephemeral (ECDHE) no primeiro pacote. Suporte a 0-RTT PSK exigindo mitigação contra ataques de Replay via `early_data`.
- **Suítes Criptográficas Permitidas (Exclusivamente AEAD)**:
  - `TLS_AES_256_GCM_SHA384` (Padrão corporativo prioritário)
  - `TLS_CHACHA20_POLY1305_SHA256` (Dispositivos sem suporte a AES-NI)
  - `TLS_AES_128_GCM_SHA256`
- **Remoções Definitivas**: Removidos modos CBC, RC4, 3DES, MD5/SHA-1, trocas RSA estáticas e compressão TLS.

### 2. Encrypted Client Hello (ECH - RFC 9458)
- Criptografa a extensão *Server Name Indication* (SNI) e metadados do pacote `ClientHello` usando a chave pública do servidor exposta em registros DNS (HTTPS/SVCB). Impede o rastreamento do domínio acessado por observadores de rede.

### 3. mTLS (Mutual TLS) & Identidades de Workload
- **Autenticação Bidirecional**: Autenticação com certificados X.509 em ambas as pontas.
- **Padrão SPIFFE/SPIRE (SVID)**: Identidades de workloads em microserviços codificadas no campo `Subject Alternative Name` (SAN) de certificados com rotação ultra-curta (1h a 24h).

### 4. QUIC (RFC 9000), DTLS 1.3 (RFC 9147), WireGuard e IPsec
- **QUIC / HTTP3**: UDP com TLS 1.3 nativo e criptografia de cabeçalho (*Header Protection*).
- **WireGuard**: VPN enxuta baseada em `Noise_IKpsk2`, Curve25519, ChaCha20-Poly1305 e BLAKE2s. Rotação dinâmica de chaves a cada 120s.
- **IPsec / IKEv2**: ESP com AES-256-GCM e ECDHE (P-384) para conexões Site-to-Site.

---

## ⚛️ Criptografia Pós-Quântica (PQC)

| Norma NIST | Algoritmo PQC | Categoria | Mecanismo | Nível de Segurança |
| :--- | :--- | :--- | :--- | :--- |
| **FIPS 203** | **ML-KEM** (Kyber) | KEM (Troca de Chaves) | Reticulados Algébricos | **ML-KEM-768** / **ML-KEM-1024** |
| **FIPS 204** | **ML-DSA** (Dilithium) | Assinatura Digital | Reticulados Algébricos | **ML-DSA-65** / **ML-DSA-87** |
| **FIPS 205** | **SLH-DSA** (SPHINCS+) | Assinatura Digital | Hash-Based Stateless | **SLH-DSA-SHA2-128f** / **SHAKE-256f** |
| **SP 800-208**| **LMS** / **XMSS** | Assinatura Stateful | Hash-Based Stateful | Bootloaders, Firmware & Root CAs |

- **Troca de Chaves Híbrida PQC (TLS 1.3 / SSH)**: Combina curvas elípticas clássicas com ML-KEM (ex: `X25519_MLKEM768`) para prevenir o ataque *"Store Now, Decrypt Later"*.

---

## 🚫 Algoritmos e Configurações Obsoletas / Proibidas

- **Transporte**: SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1, DTLS 1.0, SSHv1.
- **Criptografia Simétrica & Modos**: ECB mode para payloads > 1 bloco, CBC sem autenticação HMAC, RC4, 3DES, DES, Blowfish, ciframentos com chaves < 128 bits.
- **Assimétrica / Hashing / MACs**: RSA < 2048 bits (recomendado $\ge 3072$), DSA, ECDSA p-192, MD5, SHA-1 para assinaturas, HMAC com truncamento excessivo de tag.

---

## ⚙️ Protocolo de Implementação e Decisão Arquitetural

1. **Proteção em Repouso**: Impor **XTS-AES-256** para criptografia de disco/volumes e **AES-256-GCM** com **Envelope Encryption (DEK/KEK)** para dados em nível de aplicação e bancos de dados.
2. **Preservação de Formato e Busca**: Avaliar **FPE (FF1)** quando houver restrição rígida de schema para cartões/PII e **Searchable Encryption** para buscas em dados encriptados sem exposição de texto claro.
3. **Gestão de Chaves em Nuvem/On-Prem**: Integrar KMS com suporte a HSM FIPS 140-3 Level 3, aplicando rotação automática de KEK e capacidade de *Crypto-Shredding*.
4. **Cripto-Agilidade e Transição PQC**: Adotar suítes híbridas (`X25519_MLKEM768`) nas conexões de transporte e validar a compatibilidade de tamanhos de chaves PQC na infraestrutura.

---

## 🔗 Integração com Outras Skills de Segurança

- Para detalhes sobre infraestrutura X.509, ACME, HSMs PKCS#11 e assinaturas digitais (CAdES, XAdES, PAdES, eIDAS, ICP-Brasil), consulte a skill [pki-digital-signatures](../pki-digital-signatures/SKILL.md).
- Para adequação de criptografia e gestão de chaves aos controles organizacionais ISO/IEC 27001 (A.8.24), consulte a skill [iso-27000-series](../../grc-compliance/iso-27000-series/SKILL.md).
- Para alinhar a proteção de chaves e segredos em nuvem (AWS KMS, Azure Key Vault, GCP KMS) aos controles da CSA CCM v4 (CEK & DSP), consulte a skill [csa-cloud-security](../../cloud-iam/csa-cloud-security/SKILL.md).
- Para integrar KMS e segredos em pipelines de CI/CD e infraestrutura de containers, consulte a skill [devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md).
