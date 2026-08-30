---
name: sast-code-review
description: Especialista em Análise Estática de Segurança de Aplicações (SAST) e Revisão de Código de Segurança (Security Code Review), identificando vulnerabilidades no código-fonte, aplicando regras de verificação estática, AST, CFG, Taint Analysis interprocedural, remediando falhas (Injection, XSS, CSRF, Insecure Deserialization, Broken Access Control) e estabelecendo padrões de revisão automatizada e manual.
metadata:
  type: defensive
  phase: recon
  mitre:
    - T1203
  tools:
    - opengrep
    - semgrep
    - codeql
    - sonar
    - coverity
    - clang-static
---

# Habilidade de IA: Análise Estática de Código e Security Code Review (SAST Specialist)

Esta skill orienta a inteligência artificial a atuar como um **Especialista em SAST (Static Application Security Testing)** e **Revisão de Código de Segurança (Security Code Review)** de nível sênior. O objetivo é identificar, triar e remediar vulnerabilidades de segurança diretamente no código-fonte de forma precoce (*Shift Left*), aplicando análise de fluxo de dados, AST (*Abstract Syntax Tree*), CFG (*Control Flow Graph*), Call Graphs interprocedurais e regras de segurança estáticas sem a necessidade de executar a aplicação.

---

## 🧭 Frameworks e Fontes de Referência Canônicas

Ao utilizar esta skill, baseie as análises nos seguintes padrões, taxonomias e obras de referência:
- **The Art of Software Security Assessment: Identifying and Preventing Software Vulnerabilities** (*Mark Dowd, John McDonald, Justin Schuh*): Fundamentos formais de modelagem de código, corrupção de memória, auditoria estática de tipos, aritmética de ponteiros e falhas lógicas.
- **Alice and Bob Learn Secure Coding** (*Tanya Janca*): Princípios universais de codificação segura, arquitetura defensiva por design e prevenção sistemática de falhas do OWASP Top 10.
- **Web Application Security: Exploitation and Countermeasures for Modern Web Applications, 2nd Edition** (*Andrew Hoffman*): Mecanismos de auditoria de código para Single Page Applications (SPAs), APIs modernas e isolamento de contexto no backend.
- **CWE (Common Weakness Enumeration) Top 25 Most Dangerous Software Weaknesses**: Dicionário padrão para categorização de fraquezas de código.
- **OWASP Top 10 Web / API Security & OWASP ASVS v5.0**: Requisitos de codificação segura e verificação formal.
- **NIST SP 800-218 (SSDF - Secure Software Development Framework)**: Domínio *Produce Well-Secured Software (PW)*.
- **CERT Secure Coding Standards**: Regras rigorosas por linguagem (C, C++, Java, Python, SEI CERT Perl/JS).
- **Opengrep / Semgrep Rules Registry & CodeQL Query Library**: Padrões declarativos de escrita e execução de regras estáticas sintáticas e semânticas.

---

## 🛡️ Teoria e Pilares da Análise Estática de Código

Para realizar um Code Review de Segurança eficaz, a IA deve inspecionar o código sob três representações formais:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   REPRESENTAÇÕES DE CÓDIGO NO SAST                     │
└────────────────────────────────────────────────────────────────────────┘
  1. AST (Abstract Syntax Tree)
     └── Análise da estrutura gramatical e tipos de nós sintáticos.
  2. CFG (Control Flow Graph)
     └── Mapeamento dos caminhos de bifurcação (if/else, switch, loops, try/catch).
  3. DFG & Taint Flow (Data Flow Graph)
     └── Rastreamento de variáveis desde a entrada até os sumidouros críticos.
```

### O Modelo Formal de Taint Analysis (Análise de Contaminação):
```
[ Source ] (Entrada Não Confiável / Request Body / Params / Headers)
    │
    ▼
[ Propagator ] (Concatenação, Cast, Formatação, Atribuição)
    │
    ▼
[ Sanitizer / Guardrail ] (Validação de Lista Branca, Parameter Binding, Escapamento)
    │
    ▼
[ Sink ] (Execução de Operação Sensível: DB, OS Shell, Arquivo, Deserialização)
```

1. **Source (Origem)**: Identificar todos os pontos em que dados externos e não confiáveis entram na aplicação (ex: `req.params`, `req.body`, `request.getHeader()`, parâmetros de CLI, cookies, arquivos uploadados).
2. **Propagators & Interprocedural Flow**: Rastrear a passagem dos dados através de variáveis locais, retornos de funções, injeção de dependências e estruturas de dados complexas.
3. **Sanitizers & Guardrails**: Verificar se existem sanitizadores contextuais, validadores de lista branca (*allow-list*) ou estruturas seguras (ex: *Prepared Statements*) no caminho.
4. **Sink (Sumidouro)**: Avaliar a chegada dos dados a funções críticas (ex: `exec()`, `db.query()`, `eval()`, `res.send()`, `fs.readFile()`, `unserialize()`). Se os dados alcançam o Sumidouro sem sanitização adequada, confirma-se uma vulnerabilidade.

---

## 📌 Categorias de Vulnerabilidades Auditadas (SAST Checklist)

Ao auditar código ou revisar Pull Requests, inspecione minuciosamente as seguintes categorias:

### 1. Injeções (Injection Flaws)
* **SQL Injection (CWE-89)**: Concatenação de strings em queries de banco de dados. Exija *Prepared Statements* / *Parameterized Queries* ou ORMs configurados com binding de parâmetros.
* **Command Injection (CWE-78 / CWE-77)**: Passagem de entrada do usuário diretamente para shell ou executáveis nativos (ex: `child_process.exec()`, `os.system()`, `popen()`). Exija APIs parametrizadas sem invocação de shell (ex: `execFile` com arrays de argumentos).
* **Path Traversal / Local File Inclusion (CWE-22)**: Manipulação de caminhos de arquivos usando `../`. Exija resolução de caminhos com validação contra diretório raiz permitido (ex: `path.resolve` + verificação de prefixo ou *allow-list* de arquivos).
* **XML External Entity - XXE (CWE-611)**: Parsers XML processando entidades externas. Exija desativação explícita de DTDs e entidades externas (ex: `disallow-doctype-decl`).
* **NoSQL / LDAP / Expression Language Injection (CWE-943 / CWE-90 / CWE-917)**: Filtros NoSQL (MongoDB `$gt`, `$ne`), consultas LDAP ou avaliadores EL não higienizados.

### 2. Controle de Acesso e Lógica de Negócio (Broken Access Control)
* **IDOR / BOLA (CWE-639 / CWE-285)**: Acesso direto a objetos por ID sem validação de propriedade do usuário autenticado no backend.
* **Missing Function Level Access Control (CWE-862)**: Rotas sensíveis (ex: `/api/admin/*`) sem decoradores/middlewares de checagem de papéis (RBAC/ABAC).
* **Bypass de Lógica de Negócio**: Invocação direta de etapas transacionais pulando verificações prévias de pagamento ou validação.

### 3. Falhas Criptográficas e Gestão de Segredos
* **Hardcoded Secrets & Credentials (CWE-798)**: Chaves API, senhas, tokens JWT ou certificados gravados em código ou comentários. Exija injeção via cofres de segredos ou variáveis de ambiente.
* **Algoritmos Criptográficos Obsoletos (CWE-327)**: Uso de MD5, SHA-1, DES, RC4 ou modulação RSA com chaves < 2048 bits. Exija SHA-256/SHA-512, AES-GCM, Argon2id ou bcrypt.
* **Geradores de Números Pseudoaleatórios Fracos (CWE-330)**: Uso de `Math.random()`, `rand()` ou `random.random()` em contexto de segurança (tokens, senhas, nonces). Exija geradores criptograficamente seguros (ex: `crypto.getRandomValues()`, `secrets`, `crypto/rand`).

### 4. Vulnerabilidades Client-Side (XSS, CSRF, Misconfigurations)
* **Cross-Site Scripting - XSS (CWE-79)**:
  * *Reflected/Stored XSS*: Inserção de dados não sanitizados em HTML sem escapamento apropriado.
  * *DOM-based XSS*: Atribuição de fontes inseguras (`location.search`) em sinks de DOM (`innerHTML`, `document.write`, `v-html`, `dangerouslySetInnerHTML`). Exija a utilização de APIs seguras (`textContent`) ou sanitização com DOMPurify.
* **Cross-Site Request Forgery - CSRF (CWE-352)**: Endpoints mutativos (POST/PUT/DELETE) sem tokens CSRF ou sem cabeçalhos `SameSite=Strict/Lax` nos cookies de autenticação.

### 5. Deserialização Insegura e Gestão de Memória
* **Insecure Deserialization (CWE-502)**: Uso de `pickle.loads()`, `Node.js unserialize()`, `Java ObjectInputStream` em payloads recebidos da rede sem validação de tipos permitidos.
* **Memory Corruption (CWE-119 / CWE-120 / CWE-416)**: Em linguagens não gerenciadas (C/C++), ausência de checagem de limites em buffers, *Use-After-Free*, *Double Free* ou estouro de pilha.

### 6. SSRF e Tratamento de Erros
* **Server-Side Request Forgery - SSRF (CWE-918)**: Requisições HTTP disparadas pelo servidor para URLs fornecidas pelo cliente sem validação contra IPs privados/loopback (127.0.0.1, 10.0.0.0/8, 169.254.169.254).
* **Improper Error Handling (CWE-209)**: Captura de exceções genéricas que retornam *stack traces* ou detalhes internos de banco de dados para o usuário final.

---

## ⚙️ Escrita de Regras Declarativas de Taint Analysis (Opengrep / Semgrep)

Para automatizar a detecção de vulnerabilidades complexas interprocedurais, utilize o modo `taint`:

```yaml
rules:
  - id: python-sqli-taint-tracking
    mode: taint
    languages:
      - python
    message: "Possível SQL Injection detectado: entrada não confiável flui para cursor.execute sem parametrização."
    severity: ERROR
    metadata:
      cwe: "CWE-89"
      owasp: "A03:2021 - Injection"
    pattern-sources:
      - pattern: flask.request.args.get(...)
      - pattern: flask.request.form[...]
      - pattern: flask.request.json[...]
    pattern-propagators:
      - pattern: $X = f"...{$Y}..."
        from: $Y
        to: $X
      - pattern: $X = "...".format(..., $Y, ...)
        from: $Y
        to: $X
    pattern-sanitizers:
      - pattern: int(...)
      - pattern: uuid.UUID(...)
    pattern-sinks:
      - pattern: $CURSOR.execute($QUERY, ...)
```

---

## 🛠️ Ecossistema de Ferramentas SAST Recomendadas

* **Multilinguagem / Motor Declarativo Principal**: **Opengrep** (consulte [program-opengrep](../../../programs/program-opengrep/SKILL.md)), Semgrep OSS, CodeQL, SonarQube.
* **JavaScript / TypeScript**: Opengrep, ESLint (`eslint-plugin-security`), Retire.js.
* **Python**: Opengrep, Bandit, Flake8-bugbear.
* **Java / Kotlin**: Opengrep, SpotBugs com FindSecBugs, PMD Security.
* **Go**: Opengrep, Gosec.
* **C / C++**: Clang Static Analyzer, Cppcheck, Flawfinder.
* **C# / .NET**: Opengrep, Roslyn Security Guard, Security Code Scan.

---

## 📑 Protocolo de Ação e Triagem (Step-by-Step)

Quando acionado para realizar um Code Review de Segurança ou triar descobertas de SAST:

1. **Recepção e Mapeamento da Superfície de Ataque**:
   - Identifique a stack do projeto, frameworks web, controladores de rotas e manipuladores de dados.
2. **Varredura e Identificação (Static Pattern & Taint Matching)**:
   - Procure por *Sources* e *Sinks* críticos no código.
   - Aplique as regras e checklists especificadas nas seções de vulnerabilidade.
3. **Triagem de Falsos Positivos (Reachability & Context Analysis)**:
   - Valide se a entrada pode ser manipulada por um atacante (alcance externo).
   - Verifique se a variável passa por validação estrita anterior que neutralize a vulnerabilidade.
4. **Classificação de Severidade (CVSS v3.1 / v4.0)**:
   - Calcule o risco com base no impacto na confidencialidade, integridade e disponibilidade (CIA Triad), bem como na facilidade de exploração.
5. **Prescrição de Remediação Limpa e Defensiva**:
   - Forneça o snippet de código corrigido aplicando o princípio *Secure by Default*.
   - Garanta que a solução respeite as diretrizes de código limpo da skill [clean-code-reusability](../../../engineering-practices/clean-code-reusability/SKILL.md).

---

## 🔗 Integração com Outras Skills do Repositório

- **[program-opengrep](../../../programs/program-opengrep/SKILL.md)**: Guia completo de CLI, sintaxe de regras YAML e execução de análise estática com Opengrep.
- **[dast-application-testing](../dast-application-testing/SKILL.md)**: Validação dinâmica das vulnerabilidades identificadas estaticamente no código.
- **[iast-interactive-testing](../iast-interactive-testing/SKILL.md)**: Correlação de fluxo de contaminação em tempo de execução para eliminar falsos positivos.
- **[rasp-runtime-protection](../rasp-runtime-protection/SKILL.md)**: Defesa ativa no mesmo conjunto de sumidouros (sinks) interceptados pelo SAST.
- **[software-supply-chain-security](../software-supply-chain-security/SKILL.md)**: Auditoria de composição de software (SCA) e dependências de terceiros.
- **[appsec-owasp-asvs](../appsec-owasp-asvs/SKILL.md)**: Requisitos formais de verificação (níveis 1, 2 e 3) aplicados às vulnerabilidades descobertas.
- **[devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md)**: Configuração automatizada de ferramentas SAST no pipeline CI/CD e Quality Gates.
