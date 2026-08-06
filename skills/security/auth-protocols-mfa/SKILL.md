---
name: "auth-protocols-mfa"
description: "Atua como especialista em protocolos de autenticação e autorização (RADIUS, TACACS+, Kerberos, OAuth 2.0, OpenID Connect, SAML 2.0, SCIM 2.0, WebAuthn/FIDO2, LDAP, EAP, JWT) e arquitetura de Autenticação Multifator (MFA, Passkeys, TOTP, MFA Resistente a Phishing e Acesso Adaptativo)."
---

# Habilidade de IA: Especialista em Protocolos de Autenticação, Autorização e MFA

Esta skill orienta a inteligência artificial a agir como um **Especialista em Engenharia de Identidades, Protocolos de Autenticação, Autorização e Mecanismos de Autenticação Multifator (MFA)**, cobrindo o funcionamento profundo de protocolos de rede e aplicação (**RADIUS, TACACS+, Kerberos, OAuth 2.0, OIDC, SAML 2.0, SCIM 2.0, WebAuthn/FIDO2, LDAP, EAP**), a especificação de tokens (JWT, JWS, JWE) e a implementação de MFA moderno resistente a phishing (*Phishing-Resistant MFA*) segundo as normas **NIST SP 800-63-3/4** e **CISA**.

---

## 🧭 Matriz de Protocolos de Autenticação e Autorização

### 1. Protocolos de Infraestrutura e Gerenciamento de Rede (AAA)
- **RADIUS (Remote Authentication Dial-In User Service - RFC 2865, RFC 2866)**:
  - Protocolo AAA (Authentication, Authorization, Accounting) sobre UDP (Portas 1812/1813).
  - Criptografia baseada no segredo compartilhado (*Shared Secret*) usando MD5 (Fraco).
  - **RadSec (RFC 6614)**: RADIUS encapsulado sobre TLS 1.3 / TCP (Porta 2083) para proteção de tráfego AAA em redes não confiáveis.
- **TACACS+ (Terminal Access Controller Access Control System Plus - RFC 8907)**:
  - Protocolo corporativo da Cisco sobre TCP (Porta 49).
  - **Diferencial em Relação ao RADIUS**: Separação estrita de Autenticação, Autorização e Billing/Accounting. Criptografa **todo o corpo do pacote IP** (não apenas a senha). Permite autorização de comandos individuais por linha de comando em roteadores/switches.
- **EAP (Extensible Authentication Protocol - RFC 3748)**:
  - Framework de autenticação de camada L2/802.1X.
  - *EAP-TLS (RFC 5216)*: Autenticação mTLS baseada em certificados de cliente/servidor (Mais seguro).
  - *PEAP (Protected EAP) & EAP-TTLS*: Criação de um túnel TLS para transportar credenciais internas (MS-CHAPv2).

### 2. Autenticação Baseada em Domínio Corporativo
- **Kerberos v5 (RFC 4120)**:
  - Protocolo de autenticação de rede de ticket único baseado em criptografia simétrica e servidor KDC (Key Distribution Center - composto por AS - Authentication Server e TGS - Ticket Granting Service).
  - **Fluxo do Protocolo**:
    1. `AS-REQ / AS-REP`: O usuário envia solicitação autenticada e recebe o **TGT (Ticket Granting Ticket)** encriptado com a chave do KDC (krbtgt).
    2. `TGS-REQ / TGS-REP`: O usuário apresenta o TGT válido para solicitar um **ST (Service Ticket / Ticket de Serviço)** para acessar um recurso específico.
    3. `AP-REQ / AP-REP`: O usuário apresenta o Service Ticket diretamente ao servidor de aplicação.
  - **Mitigação de Ataques**: Bloqueio de Kerberoasting (forçar SPNs fortes com AES-256 e senhas complexas) e AS-REP Roasting (exigir pré-autenticação Kerberos obrigatória).
- **LDAP / LDAPS (Lightweight Directory Access Protocol - RFC 4511)**:
  - Protocolo de consulta e alteração a serviços de diretório sobre TCP (Porta 389).
  - **LDAPS**: Consulta segura envelopada em TLS (Porta 636) com bind autenticado obrigatório.

### 3. Protocolos Web de Identidade, Autorização e Federação
- **SAML 2.0 (Security Assertion Markup Language)**:
  - Padrão baseado em XML para Single Sign-On (SSO) corporativo e federação de identidades.
  - **Componentes**: Identity Provider (IdP), Service Provider (SP), Assertions assinaladas digitalmente (XML Signature).
  - **Fluxos**: SP-Initiated SSO vs IdP-Initiated SSO. Bindings (HTTP Redirect para requisições, HTTP POST para envio de asserções).
  - **Segurança**: Validação rigorosa de assinatura XML, recepção em URLs HTTPS explícitas e validação de timestamp/expiração contra vulnerabilidades de XML Signature Wrapping (XSW).
- **OAuth 2.0 (Framework de Autorização - RFC 6749, RFC 6750)**:
  - Protocolo de **Autorização delegada** (NÃO é um protocolo de autenticação por si só).
  - **Grant Types Recomendados**:
    - **Authorization Code Flow com PKCE (RFC 7636)**: Obrigatório para Single Page Applications (SPAs), aplicativos móveis e aplicações nativas. Impede interceptação de código de autorização usando `code_verifier` e `code_challenge` (S256).
    - **Client Credentials Flow**: Comunicação M2M (Machine-to-Machine) de serviço para serviço.
    - **Device Authorization Grant (RFC 8628)**: Para dispositivos sem navegador ou com entrada limitada (Smart TVs, CLI).
  - **Extensões de Segurança**: **DPoP (Demonstrating Proof-of-Possession - RFC 9449)** para vincular access tokens à chave privada do cliente, impedindo roubo e reuso de tokens de acesso.
  - *Fluxos Descontinuados*: Implicit Grant e Resource Owner Password Credentials (ROPC) estão **proibidos** pela especificação OAuth 2.1 Security Best Current Practice.
- **OpenID Connect (OIDC Core 1.0)**:
  - Camada de **Identidade** construída sobre a infraestrutura do OAuth 2.0.
  - Introduz o **ID Token** (JWT assinado pelo IdP contendo *claims* do usuário como `sub`, `iss`, `aud`, `exp`, `iat`) e o endpoint `/userinfo`.
  - **OIDC Discovery**: Resolução dinâmica de configurações do IdP via `/.well-known/openid-configuration` e chave pública via JWKS (`/jwks.json`).
- **SCIM 2.0 (System for Cross-domain Identity Management - RFC 7643, RFC 7644)**:
  - Padrão REST/JSON para **provisionamento e sincronização automatizada de contas** entre o IdP central e aplicações SaaS.
  - Recursos principais: `/Users` e `/Groups` suportando operações CRUD completas, filtragem (`filter=userName eq "user@domain.com"`) e atualizações parciais otimizadas (`PATCH`).

### 4. Padrões de Tokens e Estrutura de Assinatura
- **JWT (JSON Web Token - RFC 7519)**: Estrutura composta por três partes separadas por pontos: `Header.Payload.Signature` em Base64URL.
- **JWS (JSON Web Signature - RFC 7515)**: Garantia de integridade e autenticidade usando HMAC (ex: HS256) ou assinaturas assimétricas (ex: RS256, ES256, EdDSA).
- **JWE (JSON Web Encryption - RFC 7516)**: Criptografia do payload do token para garantir confidencialidade.
- *Vulnerabilidades Frequentes*: Validação falha do algoritmo `alg: "none"`, substituição inadvertida de chaves assimétricas por simétricas (algoritmo HS256 assinado com chave pública RS256) e falta de validação das *claims* `iss`, `aud` e `exp`.

---

## 🔑 Autenticação Multifator (MFA) e FIDO2 / WebAuthn

O NIST SP 800-63B classifica os fatores de autenticação em três categorias lógicas:
1. **Algo que você sabe (Knowledge)**: Senhas, PINs, perguntas de segurança (Fator fraco).
2. **Algo que você tem (Possession)**: Tokens FIDO2/Hardware, chaves criptográficas, apps TOTP, Smartcards.
3. **Algo que você é (Inherence)**: Biometria física (Impressão digital, FaceID, Íris).

```
+-----------------------------------------------------------------------------------+
| HIERARQUIA DE FORÇA E RESISTÊNCIA DE MFA (NIST AAL1 a AAL3)                       |
+-----------------------------------------------------------------------------------+
| NÍVEL 3 (AAL3) - RESISTENTE A PHISHING (Phishing-Resistant MFA)                    |
| - FIDO2 / WebAuthn / Passkeys (Hardware Security Keys e Platform Authenticators)  |
| - Certificados de Cliente mTLS (Smartcards PKCS#11, YubiKey PIV)                 |
+-----------------------------------------------------------------------------------+
                                         ^
                                         |
+-----------------------------------------------------------------------------------+
| NÍVEL 2 (AAL2) - MFA CONVENCIONAL SEGURO                                         |
| - TOTP / HOTP via Aplicativo Autenticador (RFC 6238 / RFC 4226 - Google Auth/Authy)|
| - Push Notifications com Correspondência de Número (Number Matching)             |
+-----------------------------------------------------------------------------------+
                                         ^
                                         |
+-----------------------------------------------------------------------------------+
| FATORES FRACOS / DEPRECIADOS (VULNERÁVEIS A AITM E SIM SWAPPING)                  |
| - SMS OTP / Chamada de Voz (Vulnerável a SIM Swap e ataques SS7)                  |
| - Push Notification Simples sem contexto (Vulnerável a MFA Fatigue Bombing)       |
| - Links de Autenticação por E-mail / Perguntas Secretas                           |
+-----------------------------------------------------------------------------------+
```

### WebAuthn (W3C) & FIDO2 / Passkeys
- **Arquitetura**: Construído sobre criptografia assimétrica de chave pública de ponta a ponta. O autenticador (Hardware Key como YubiKey ou Autenticador de Plataforma como Windows Hello, TouchID, FaceID) gera um par de chaves único para cada origem (origem Web vinculada ao domínio).
- **Vínculo com o Domínio (Origin Binding)**: O navegador injeta o domínio real da aplicação no desafio do WebAuthn. Caso o usuário caia em um site de phishing (ex: `login-empresa.com` em vez de `empresa.com`), a assinatura do WebAuthn falhará, **tornando o ataque de Phishing/AitM impossível**.
- **Passkeys (Syncable Credentials)**: Credenciais FIDO2 sincronizadas com segurança através da nuvem do ecossistema do usuário (Apple Keychain, Google Password Manager, Bitwarden) com proteção criptográfica de ponta a ponta.
- **Diferenças de Configuração**:
  - *User Presence (UP)*: Exige toque físico no dispositivo para provar presença humana.
  - *User Verification (UV)*: Exige PIN ou biometria local no autenticador para liberar a chave (Garante MFA completo em um único fluxo FIDO2).
  - *Resident Key / Discoverable Credential*: Permite login sem digitar nome de usuário (passwordless).

---

## ⚙️ Protocolo de Decisão do Engenheiro de Autenticação

Ao desenhar, revisar ou integrar arquiteturas de login e autorização:

1. **Adote Phishing-Resistant MFA por Padrão**:
   - Exija **FIDO2 / WebAuthn / Passkeys** ou mTLS para todos os acessos administrativos, privilegiados (PAM) e colaboradores internos.
2. **Utilize OIDC para Autenticação e OAuth 2.0 para Autorização**:
   - Nunca utilize apenas OAuth 2.0 para identificar usuários sem a camada OIDC. Exija **PKCE** em todas as aplicações clientes.
3. **Validação Rigorosa de Tokens JWT**:
   - Valide explicitamente as *claims* `iss` (emissor confiável), `aud` (sua aplicação como público-alvo) e `exp` (expiração). Force a verificação da assinatura com algoritmo estrito e proíba `alg: "none"`.
4. **Implemente Acesso Condicional e Baseado em Risco**:
   - Combine o fator de autenticação com pontuação contínua de risco (IP Reputacional, Localização geográfica impossível, conformidade de dispositivo via EDR/MDM, detecção de comportamento).

---

## 🔗 Integração com Outras Skills de Segurança

- Para alinhar os certificados e assinaturas digitais de mTLS, WebAuthn e Smartcards à arquitetura de PKI, consulte a skill [pki-digital-signatures](../pki-digital-signatures/SKILL.md).
- Para aplicar controles de acesso e IAM no Active Directory, Windows, Linux, AWS, Azure, GCP, OCI, SAP e Salesforce, consulte a skill [iam-access-management](../iam-access-management/SKILL.md).
- Para alinhar os requisitos de autenticação digital às diretrizes do NIST (SP 800-63-3/4 IAL, AAL, FAL), consulte a skill [nist-frameworks-csf](../nist-frameworks-csf/SKILL.md).
- Para validar a implementação segura de APIs REST e prevenção de falhas de autenticação de APIs (OWASP API2:2023 - Broken Authentication), consulte a skill [pentester-owasp-api-security-2023](../pentester-owasp-api-security-2023/SKILL.md).
- Para auditar implementações de JWT e mecanismos de login no código-fonte, consulte a skill [sast-code-review](../sast-code-review/SKILL.md).
