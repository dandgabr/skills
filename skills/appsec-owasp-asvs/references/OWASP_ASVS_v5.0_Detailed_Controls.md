# OWASP ASVS v5.0.0 Detailed Verification Requirements

Este documento atua como a base de dados técnica de referência de segurança para todas as auditorias, revisões de código e propostas arquiteturais. Todos os controles abaixo correspondem às 17 categorias do **OWASP ASVS v5.0.0**.

---

## 📊 Níveis de Verificação ASVS
- **Nível 1 (Oportunista):** Foco em vulnerabilidades facilmente exploráveis. Automatizável em CI/CD.
- **Nível 2 (Padrão):** O padrão recomendado para a maioria das aplicações de negócios que processam dados sensíveis ou pessoais (PII).
- **Nível 3 (Avançado):** Exigido para sistemas críticos de alta segurança (p. ex., infraestrutura crítica, transações financeiras de alto risco, dados médicos).

---

## V1: Encoding and Sanitization (Codificação e Sanitização)
*Objetivo:* Garantir que todas as saídas de dados sejam devidamente codificadas para o seu respectivo contexto (HTML, JavaScript, SQL, LDAP, etc.) antes de serem interpretadas pelo destino.
- **ASVS 1.1.1 (CWE-79):** Codificar contextualmente todas as entradas do usuário refletidas em páginas web (HTML body, atributos, tags `<script>`, etc.) usando bibliotecas consolidadas (ex: OWASP Java Encoder, DOMPurify).
- **ASVS 1.1.2 (CWE-116):** Sanitizar strings contra injeção de parâmetros em comandos de sistema e scripts de shell usando APIs de escape robustas.
- **ASVS 1.1.3 (CWE-93):** Validar e sanitizar caracteres de quebra de linha (`CRLF`) antes de gravar dados em cabeçalhos HTTP ou arquivos de logs, mitigando HTTP Response Splitting e Log Injection.

---

## V2: Validation and Business Logic (Validação e Lógica de Negócio)
*Objetivo:* Validar toda e qualquer entrada de dados estruturalmente antes do processamento e garantir que os fluxos lógicos não possam ser burlados ou abusados.
- **ASVS 2.1.1 (CWE-20):** Validar todas as entradas usando listas de permissão estritas (allow-list/whitelist). Definir tipos de dados, comprimentos máximos/mínimos e expressões regulares rígidas.
- **ASVS 2.1.2 (CWE-89):** Utilizar queries parametrizadas (Prepared Statements) ou ORMs seguros por padrão para interagir com o banco de dados. Nunca concatenar dados do usuário diretamente em strings SQL.
- **ASVS 2.1.3 (CWE-20):** Validar dados em ambos os lados: frontend (usabilidade) e backend (segurança obrigatória).
- **ASVS 2.2.1 (CWE-840):** Garantir que transações lógicas sigam etapas estritas na ordem correta, prevenindo o desvio de etapas de checkout, checkout sem pagamento, etc.
- **ASVS 2.2.2 (CWE-601):** Impedir redirecionamentos abertos (Open Redirect) validando que todas as URLs de destino pertençam a uma lista branca de domínios confiáveis.

---

## V3: Web Frontend Security (Segurança do Frontend Web)
*Objetivo:* Proteger o cliente contra ataques no navegador por meio de políticas e cabeçalhos de segurança rígidos.
- **ASVS 3.1.1 (CWE-1021):** Implementar a política `Content-Security-Policy (CSP)` estrita para restringir a origem de execução de scripts e recursos (`script-src 'self' 'nonce-...'`).
- **ASVS 3.1.2 (CWE-1021):** Configurar cabeçalhos de proteção contra Clickjacking (`Frame-Options: DENY` ou `SAMEORIGIN`, ou diretiva `frame-ancestors` na CSP).
- **ASVS 3.1.3 (CWE-523):** Configurar cabeçalhos HTTP Strict Transport Security (`HSTS`) com expiração de pelo menos um ano (`max-age=31536000; includeSubDomains; preload`).
- **ASVS 3.2.1 (CWE-918):** Restringir a comunicação de scripts frontend (CORS) permitindo apenas origens autorizadas explícitas em vez do curinga `*` em ambientes autenticados.

---

## V4: API and Web Service (APIs e Web Services)
*Objetivo:* Garantir a integridade, autenticação e controle de taxa de barramentos de API REST, SOAP, GraphQL ou canais WebSocket.
- **ASVS 4.1.1 (CWE-20):** Validar payloads de entrada contra um Schema JSON/XML explícito antes do processamento.
- **ASVS 4.1.2 (CWE-770):** Implementar Rate Limiting (limitação de taxa) por IP e por token de usuário para mitigar ataques de negação de serviço (DoS) a nível de aplicação.
- **ASVS 4.2.1 (CWE-943):** Desativar a introspecção de consultas no GraphQL (Introspection Query) em ambientes de produção.
- **ASVS 4.2.2 (CWE-285):** Garantir que requisições WebSocket passem por validações de origem (Origin Header Check) e autorização contínua de conexão.

---

## V5: File Handling (Manipulação de Arquivos)
*Objetivo:* Proteger o servidor contra execução de código remoto (RCE) e negação de serviço resultantes de upload/download de arquivos maliciosos.
- **ASVS 5.1.1 (CWE-434):** Armazenar arquivos carregados por usuários fora do diretório raiz da web (web root) e sem permissão de execução em nível de servidor/SO.
- **ASVS 5.1.2 (CWE-434):** Renomear arquivos carregados no servidor usando geradores de nomes seguros aleatórios (ex: UUIDv4) para evitar sobrescritas e Path Traversal.
- **ASVS 5.1.3 (CWE-434):** Validar os tipos de arquivos inspecionando a assinatura mágica de bytes (Magic Numbers/File Signatures) do arquivo, em vez de depender exclusivamente da extensão fornecida no formulário HTTP.
- **ASVS 5.2.1 (CWE-400):** Limitar o tamanho máximo de uploads para evitar estouros de disco e exaustão de memória no parser do servidor (Zip Bomb, etc.).

---

## V6: Authentication (Autenticação)
*Objetivo:* Assegurar a robustez na verificação de identidade dos usuários, gerenciando senhas e MFA com práticas modernas.
- **ASVS 6.1.1 (CWE-521):** Exigir senhas com comprimento mínimo de 12 caracteres (e máximo de pelo menos 64 caracteres) sem restrições de complexidade arbitrárias que dificultem o uso de gerenciadores de senhas.
- **ASVS 6.1.2 (CWE-521):** Validar senhas contra listas de senhas fracas conhecidas, vazadas ou dicionários de termos comuns durante o cadastro e alteração de senha.
- **ASVS 6.2.1 (CWE-307):** Hash de senhas usando algoritmos modernos resistentes a ataques de GPU offline com custo adaptável: Argon2id (recomendado), scrypt ou bcrypt com fatores adequados.
- **ASVS 6.3.1 (CWE-308):** Oferecer e incentivar o uso de Autenticação Multifator (MFA) baseada em padrões seguros, preferencialmente FIDO2/WebAuthn ou geradores TOTP (RFC 6238), em detrimento de SMS/E-mail.

---

## V7: Session Management (Gerenciamento de Sessão)
*Objetivo:* Garantir o ciclo de vida seguro de tokens e cookies de sessão, impedindo sequestro ou vazamento de estado de login.
- **ASVS 7.1.1 (CWE-613):** Gerar IDs de sessão com alta entropia usando geradores de números pseudo-aleatórios criptograficamente seguros (CSPRNG) com no mínimo 128 bits de entropia.
- **ASVS 7.1.2 (CWE-613):** Implementar tempos limite (timeouts) de sessão inativa (ex: 15-30 minutos) e expiração de sessão absoluta (ex: 24 horas).
- **ASVS 7.2.1 (CWE-1004):** Adicionar as diretivas `HttpOnly`, `Secure` e `SameSite=Lax` (ou `SameSite=Strict`) em todos os cookies que carregam identificadores de sessão.
- **ASVS 7.2.2 (CWE-384):** Destruir a sessão existente no servidor e gerar um novo ID de sessão imediatamente após qualquer mudança de estado de privilégio (ex: de anônimo para autenticado, autenticação em duas etapas concluída).

---

## V8: Authorization (Autorização e Controle de Acesso)
*Objetivo:* Impor o princípio do menor privilégio e negação por padrão em todas as transações, recursos lógicos e objetos.
- **ASVS 8.1.1 (CWE-276):** Adotar política de Deny-By-Default (Negação por Padrão). Todas as rotas e funções do sistema devem exigir autorização explícita, a menos que marcadas publicamente.
- **ASVS 8.1.2 (CWE-639):** Mitigar Broken Object Level Authorization (BOLA/IDOR) validando a cada requisição se o usuário autenticado de fato possui o direito de ler, atualizar ou excluir o registro correspondente no banco de dados.
- **ASVS 8.2.1 (CWE-285):** Centralizar os controles de acesso em um serviço ou módulo único na arquitetura do sistema para evitar implementações ad-hoc inconsistentes.

---

## V9: Self-contained Tokens (Tokens Autocontidos / JWT)
*Objetivo:* Garantir a integridade, confidencialidade e revogabilidade de tokens de portador assinados digitalmente.
- **ASVS 9.1.1 (CWE-347):** Validar a assinatura de tokens JWT usando algoritmos assimétricos seguros (RS256, ES256) em vez de algoritmos simétricos fracos, e rejeitar explicitamente o algoritmo `none`.
- **ASVS 9.1.2 (CWE-613):** Definir e verificar obrigatoriamente a data de expiração (`exp`) do token JWT, mantendo a vida útil do token o mais curta possível.
- **ASVS 9.2.1 (CWE-287):** Implementar um mecanismo para revogar ou invalidar tokens antes da expiração natural em caso de logout ou redefinição de credenciais (ex: mantendo uma lista de revogação/blocklist rápida no Redis).

---

## V10: OAuth and OIDC (OAuth e OpenID Connect)
*Objetivo:* Validar fluxos de federação de identidade e delegação de autoridade entre a aplicação e provedores de identidade externos.
- **ASVS 10.1.1 (CWE-20):** Validar estritamente a URL de redirecionamento (`redirect_uri`) contra uma lista exata e estática cadastrada no Identity Provider, impedindo desvios para domínios maliciosos.
- **ASVS 10.1.2 (CWE-352):** Utilizar o parâmetro `state` ou o mecanismo PKCE (Proof Key for Code Exchange) para prevenir ataques de Cross-Site Request Forgery (CSRF) e roubo de código de autorização em fluxos OAuth.
- **ASVS 10.2.1 (CWE-287):** Verificar a assinatura e as claims do ID Token (`iss`, `aud`, `exp`, `nonce`) localmente ou via endpoint de introspecção antes de aceitar a identidade do usuário.

---

## V11: Cryptography (Criptografia)
*Objetivo:* Garantir que dados confidenciais sejam protegidos com criptografia forte e chaves bem gerenciadas.
- **ASVS 11.1.1 (CWE-327):** Utilizar algoritmos criptográficos robustos padrão de mercado (ex: AES-GCM, ChaCha20-Poly1305) com chaves de no mínimo 128 bits (preferencialmente 256 bits).
- **ASVS 11.1.2 (CWE-328):** Desativar o uso de algoritmos criptográficos obsoletos, inseguros ou quebrados (ex: DES, 3DES, RC4, MD5, SHA1).
- **ASVS 11.2.1 (CWE-320):** Implementar o armazenamento de chaves criptográficas fora do código-fonte da aplicação (ex: em AWS KMS, HashiCorp Vault, Azure Key Vault) e garantir que segredos nunca sejam comitados em repositórios de controle de versão.
- **ASVS 11.2.2 (CWE-320):** Implementar processes e mecanismos automatizados de rotação periódica de chaves criptográficas.

---

## V12: Secure Communication (Comunicação Segura)
*Objetivo:* Assegurar a proteção de todos os canais de rede externos e internos contra interceptação e espionagem de tráfego.
- **ASVS 12.1.1 (CWE-319):** Criptografar toda a comunicação de rede usando TLS 1.2 ou TLS 1.3 por padrão, desabilitando explicitamente versões antigas do protocolo (SSLv3, TLS 1.0, TLS 1.1).
- **ASVS 12.1.2 (CWE-319):** Configurar conjuntos de cifras (cipher suites) de alta segurança que suportem Forward Secrecy (ex: ECDHE-RSA-AES256-GCM-SHA384).
- **ASVS 12.2.1 (CWE-295):** Validar rigorosamente os certificados TLS no lado do cliente em conexões externas (p. ex., chamadas HTTP de microsserviços), verificando a cadeia de confiança, expiração e revogação.

---

## V13: Configuration (Configuração Segura)
*Objetivo:* Garantir o endurecimento (hardening) da infraestrutura e dos servidores nos quais a aplicação é executada.
- **ASVS 13.1.1 (CWE-16):** Desativar recursos, serviços e portas não utilizados em containers e servidores de produção.
- **ASVS 13.1.2 (CWE-489):** Desativar ferramentas de depuração (debug) e console interativos de desenvolvedor em produção.
- **ASVS 13.2.1 (CWE-2):** Substituir todas as credenciais padrões e de fábrica de dependências externas (como bancos de dados, servidores de fila, ferramentas de cache) antes do primeiro deploy.

---

## V14: Data Protection (Proteção de Dados e Privacidade)
*Objetivo:* Garantir que dados confidenciais e PII de usuários sejam guardados com segurança de ponta a ponta e descartados conforme conformidades (LGPD/GDPR).
- **ASVS 14.1.1 (CWE-311):** Criptografar dados sensíveis de usuários em repouso nos bancos de dados corporativos (p. ex., CPF, e-mail, cartão de crédito, telefones) usando criptografia simétrica com chaves gerenciadas de forma independente.
- **ASVS 14.1.2 (CWE-538):** Garantir a não-exposição de dados sensíveis na URL (Query String) e impedir o cache no navegador dessas páginas configurando os cabeçalhos `Cache-Control: no-store` e `Pragma: no-cache`.
- **ASVS 14.2.1 (CWE-244):** Limpar buffers de memória RAM que contenham dados confidenciais (p. ex., senhas e chaves criptográficas decifradas) assim que seu processamento termine, evitando vazamento por meio de falhas de leitura fora de limites.

---

## V15: Secure Coding and Architecture (Codificação e Arquitetura Seguras)
*Objetivo:* Garantir que o design do sistema apoie a defesa em profundidade e mitigue o risco de dependências de terceiros vulneráveis.
- **ASVS 15.1.1 (CWE-1104):** Manter uma lista de dependências externas (Software Bill of Materials - SBOM) atualizada e submeter todos os pacotes de bibliotecas de terceiros a scanners automatizados de análise de composição de software (SCA) no CI/CD para detectar e bloquear pacotes vulneráveis.
- **ASVS 15.2.1 (CWE-1008):** Organizar o software em zonas de confiança isoladas e desacopladas, impedindo que o comprometimento de um componente de baixo privilégio forneça acesso imediato a dados críticos do sistema.

---

## V16: Security Logging and Error Handling (Logs de Segurança e Tratamento de Erros)
*Objetivo:* Assegurar a auditoria e detecção precoce de atividades maliciosas sem expor dados confidenciais nos arquivos de registro.
- **ASVS 16.1.1 (CWE-778):** Registrar eventos de segurança significativos contendo metadados contextualizados estruturados (Log JSON) incluindo: quem realizou a ação (ID de usuário), quando (timestamp padronizado ISO 8601), o que (ID do evento/ação) e o resultado (sucesso ou falha).
- **ASVS 16.1.2 (CWE-117):** Garantir a sanitização de logs de forma a não gravar PII (LGPD), senhas em texto puro, chaves criptográficas ou tokens de sessão.
- **ASVS 16.2.1 (CWE-209):** Tratar todas as exceções do sistema e retornar mensagens genéricas de falhas aos usuários finais, armazenando stack traces completos e erros nativos apenas no sistema de logs internos de acesso restrito.

---

## V17: WebRTC (Web Real-Time Communication)
*Objetivo:* Proteger canais de mídia ponto a ponto em tempo real contra espionagem e rastreamento indesejado.
- **ASVS 17.1.1 (CWE-200):** Ocultar os endereços IP locais dos usuários em conexões WebRTC usando mDNS para resolução de ICE Candidates, impedindo o rastreamento físico de rede do usuário.
- **ASVS 17.1.2 (CWE-319):** Exigir criptografia ponta a ponta robusta em todas as transmissões de WebRTC por meio dos protocolos DTLS (Datagram Transport Layer Security) e SRTP (Secure Real-time Transport Protocol).
- **ASVS 17.2.1 (CWE-285):** Garantir que os servidores de sinalização do WebRTC exijam autenticação e autorização prévia antes de permitir o tráfego de mensagens de SDP (Session Description Protocol).
