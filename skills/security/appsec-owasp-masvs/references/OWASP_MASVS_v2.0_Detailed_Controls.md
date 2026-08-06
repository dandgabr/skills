# OWASP MASVS v2.0.0 Detailed Verification Requirements

Este documento atua como a base de dados técnica de referência de segurança para auditorias, testes de invasão e revisões de código de aplicações móveis (Android e iOS). Todos os controles abaixo correspondem às 7 categorias do **OWASP MASVS (Mobile Application Security Verification Standard) v2.0.0** integrado ao **MASTG (Mobile Application Security Testing Guide)**.

---

## 📊 Perfis de Segurança MASVS v2.0.0

- **MASVS-L1 (Standard Security):** Requisitos essenciais de segurança aplicáveis a todas as aplicações móveis. Foco na proteção contra ataques comuns e vazamentos de dados.
- **MASVS-L2 (Defense-in-Depth / High Security):** Requisitos avançados para aplicações móveis que tratam de dados altamente sensíveis (fintechs, bancos, saúde, identificação digital).
- **MASVS-R (Resilience Against Reverse Engineering and Tampering):** Requisitos de resiliência contra engenharia reversa, análise dinâmica e manipulação (root/jailbreak, hooking com Frida, deobfUScação). Combinado como **MASVS-L1-R** ou **MASVS-L2-R**.

---

## MASVS-STORAGE: Secure Storage (Armazenamento Seguro)
*Objetivo:* Garantir que dados sensíveis, credenciais e chaves armazenadas no dispositivo móvel estejam protegidos contra acessos não autorizados por outros aplicativos, malwares ou extrações físicas de memória.

- **MASVS-STORAGE-1:** Armazenar credenciais, tokens de acesso e dados confidenciais estritamente em contêineres de armazenamento seguro gerenciados pelo sistema operacional (**Android Keystore / EncryptedSharedPreferences** no Android; **iOS Keychain / Data Protection API** no iOS).
- **MASVS-STORAGE-2:** Impedir a exposição de dados sensíveis em logs de desenvolvimento, mensagens de debug do sistema (Logcat/Console) ou relatórios de crash de terceiros (Crashlytics, Sentry).
- **MASVS-STORAGE-3:** Impedir o vazamento de dados sensíveis por meio do armazenamento temporário, cache de respostas HTTP, registros de preenchimento automático (Autofill), screenshots da aplicação ou cópias da área de transferência (Clipboard).
- **MASVS-STORAGE-4:** Não armazenar dados sensíveis no armazenamento externo/público do dispositivo (como diretórios SD Card compartilhados) onde outros apps possuem permissão de leitura.

---

## MASVS-CRYPTO: Cryptography (Criptografia Móvel)
*Objetivo:* Garantir que operações criptográficas no app sigam os padrões modernos da indústria e utilizem chaves seguras protegidas por hardware.

- **MASVS-CRYPTO-1:** Utilizar exclusivamente primitivas e algoritmos criptográficos fortes e padrão da indústria (ex: AES-GCM-256, ChaCha20-Poly1305, RSA-2048+, ECDSA P-256), evitando o uso de algoritmos obsoletos (DES, RC4, MD5, SHA1).
- **MASVS-CRYPTO-2:** Proibir o uso de chaves criptográficas estáticas codificadas no código-fonte do app (*hardcoded keys*), em arquivos de propriedades ou em bibliotecas nativas compiladas (`.so` / `.dylib`).
- **MASVS-CRYPTO-3:** Gerar chaves criptográficas utilizando geradores de números pseudo-aleatórios criptograficamente seguros (CSPRNG) e garantir que as chaves fiquem protegidas por módulos de hardware (**Android KeyStore / Secure Element / StrongBox**; **iOS Secure Enclave**).
- **MASVS-CRYPTO-4:** Garantir que IVs (Vetores de Inicialização) e Nonces sejam únicos para cada operação de cifragem e gerados usando CSPRNG.

---

## MASVS-AUTH: Authentication and Session Management (Autenticação e Sessão)
*Objetivo:* Assegurar a robustez na verificação de identidade dos usuários locais e na gestão de sessões remotas via APIs móveis.

- **MASVS-AUTH-1:** Implementar autenticação remota segura utilizando protocolos modernos baseados em tokens (OAuth 2.0 com **PKCE - Proof Key for Code Exchange** e OpenID Connect).
- **MASVS-AUTH-2:** Ao utilizar biometria local (Fingerprint, FaceID, TouchID), exigir a API oficial do sistema (**Android BiometricPrompt**; **iOS LocalAuthentication**) e vincular a chave no KeyStore/Keychain à necessidade de autenticação biométrica (`setUserAuthenticationRequired(true)`).
- **MASVS-AUTH-3:** Invalidar tokens de sessão local e remotamente durante o logout e impor limites de expiração de sessão inativa e absoluta.
- **MASVS-AUTH-4:** Garantir que o aplicativo lide adequadamente com a invalidação de chaves biométricas quando o usuário cadastrar novos dedos ou rostos no sistema operacional.

---

## MASVS-NETWORK: Network Communication (Comunicação de Rede)
*Objetivo:* Assegurar a confidencialidade e integridade de todos os dados transmitidos pela rede entre o app móvel e os serviços backend.

- **MASVS-NETWORK-1:** Criptografar todo o tráfego de rede usando TLS 1.2 ou TLS 1.3 por padrão. Desativar explicitamente o tráfego em texto puro HTTP no arquivo de configuração do sistema (**Android Network Security Configuration** `cleartextTrafficPermitted="false"`; **iOS App Transport Security - ATS**).
- **MASVS-NETWORK-2:** Validar rigorosamente a cadeia de certificados TLS, o nome do host e desativar qualquer opção de aceitação de certificados autoassinados ou desabilitação de verificação em produção.
- **MASVS-NETWORK-3:** Em aplicações de alto risco (MASVS-L2), implementar **Certificate Pinning** (fixação de certificados/chaves públicas) usando mecanismos nativos do SO ou bibliotecas consolidadas (OkHttp `CertificatePinner`, TrustKit) para evitar ataques Man-in-the-Middle (MitM) via CA maliciosa no dispositivo.

---

## MASVS-PLATFORM: Platform Interaction (Interação com a Plataforma)
*Objetivo:* Proteger o aplicativo contra vetor de ataques baseados em mecanismos de Comunicação Inter-Processos (IPC), WebViews e permissões do sistema.

- **MASVS-PLATFORM-1:** Solicitar apenas as permissões de sistema estritamente necessárias (*Princípio do Menor Privilégio*) e validar a concessão de permissões em tempo de execução.
- **MASVS-PLATFORM-2:** Proteger os componentes de IPC expostos no Android (Activities, Services, Broadcast Receivers, Content Providers) marcando `android:exported="false"` a menos que explicitamente destinados a acesso por outros apps.
- **MASVS-PLATFORM-3:** Validar rigorosamente todas as entradas de dados recebidas via IPC, Intents, Deep Links e Universal Links antes de processá-las ou repassá-las ao backend.
- **MASVS-PLATFORM-4:** Endurecer a configuração de **WebViews**: desativar suporte a arquivos locais (`setAllowFileAccess(false)`), desativar acessos entre origens e não expor interfaces JavaScript inseguras (`addJavascriptInterface`) sem anotações rígidas e restrições.

---

## MASVS-CODE: Code Quality and Build Settings (Qualidade de Código e Build)
*Objetivo:* Garantir que a aplicação seja compilada com todas as proteções ativas do sistema e sem artefatos ou símbolos de depuração.

- **MASVS-CODE-1:** Compilar o aplicativo com as proteções de compilador do sistema ativadas (ASLR, PIE, Stack Canaries, ARC no iOS).
- **MASVS-CODE-2:** Garantir que o código compilado final seja gerado no modo **Release** sem flags de depuração ativas (`android:debuggable="false"` no Android; compilação em `Release` no iOS).
- **MASVS-CODE-3:** Remover código de teste, backdoors de desenvolvimento, logs de debug e código não utilizado do pacote de distribuição final.
- **MASVS-CODE-4:** Manter todas as dependências de terceiros (SDKs Android, Pods iOS, Swift Packages) atualizadas e verificar vulnerabilidades conhecidas por meio de análise de composição de software (SCA).

---

## MASVS-RESILIENCE: Resilience (Resiliência contra Engenharia Reversa e Adulteração)
*Objetivo:* (Exigido para perfil **MASVS-R / MASVS-L2-R**) Dificultar ativamente a análise dinâmica, engenharia reversa, uso de frameworks de hooking e adulteração do aplicativo móvel.

- **MASVS-RESILIENCE-1 (Root / Jailbreak Detection):** Detectar se o aplicativo está sendo executado em um ambiente desprotegido, com acesso root/jailbreak ativo (Android Magisk, RootBeer; iOS Cydia, ElleKit) e reagir de forma segura terminando a execução ou restringindo funcionalidades.
- **MASVS-RESILIENCE-2 (Anti-Debugging & Dynamic Analysis):** Implementar mecanismos para detectar e impedir a conexão de depuradores (*debuggers* ptrace, lldb) e frameworks de instrumentação dinâmica (**Frida**, Xposed, Substrate).
- **MASVS-RESILIENCE-3 (Integrity & Anti-Tampering):** Verificar a integridade do código-fonte e da assinatura digital do APK/IPA (ex: **Google Play Integrity API**; **iOS App Attest / DeviceCheck**) para detectar modificações não autorizadas ou *re-signing* do pacote.
- **MASVS-RESILIENCE-4 (Obfuscation):** Aplicar técnicas de ofuscação avançadas de código (R8/ProGuard, DexGuard, OLLVM) para encriptar strings sensíveis, renomear identificadores e achatar o fluxo de controle (*Control Flow Flattening*).
