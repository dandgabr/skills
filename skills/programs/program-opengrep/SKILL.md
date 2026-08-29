---
name: program-opengrep
description: Guia Definitivo e Padrões de Engenharia para Opengrep (opengrep.dev), cobrindo o motor open-source de análise estática de código (SAST), sintaxe completa de regras em YAML, padrões sintáticos e semânticos, modo Taint Analysis avançado, CLI, testes de regras, integração em CI/CD com exportação SARIF e governança de código seguro.
metadata:
  type: defensive
  phase: testing
  mitre:
    - T1203
  tools:
    - opengrep
    - semgrep
---

# Habilidade de IA: Guia e Engenharia com Opengrep (SAST Engine)

Esta skill fornece orientação canônica, comandos operacionais e padrões de engenharia para o uso do **Opengrep** ([opengrep.dev](https://www.opengrep.dev/)), um motor open-source de análise estática de código (SAST) de alta performance, compatível com a sintaxe de regras declarativas do Semgrep OSS, projetado para identificar vulnerabilidades, aplicar boas práticas de arquitetura e automatizar verificações de segurança no ciclo de vida de desenvolvimento (SDLC).

---

## 🧭 Visão Geral e Filosofia do Opengrep

O Opengrep analisa código-fonte através da correspondência de árvores sintáticas abstratas (AST - *Abstract Syntax Tree*), permitindo que desenvolvedores e analistas de segurança escrevam regras que se parecem com o próprio código-fonte, evitando a complexidade e a fragilidade de expressões regulares puras.

### Vantagens Chave:
1. **Sintaxe Semântica Amigável**: As regras usam a sintaxe da própria linguagem de destino com operadores especiais como reticências (`...`) e metavariáveis (`$VAR`).
2. **Alta Performance**: Motor compilado em código nativo rápido, capaz de escanear milhões de linhas de código em segundos.
3. **Modo Taint Analysis Nativo**: Rastreamento interprocedural de fluxo de dados contaminados (*Sources* ➔ *Propagators* ➔ *Sanitizers* ➔ *Sinks*).
4. **Interoperabilidade Total**: Compatibilidade nativa com regras legadas em YAML e formato de saída padrão SARIF (*Static Analysis Results Interchange Format*).

---

## 💻 Comandos da CLI do Opengrep

### 1. Instalação e Verificação
```bash
# Executar verificação de versão e integridade
opengrep --version

# Exibir ajuda e catálogo de opções
opengrep --help
```

### 2. Comandos de Varredura (`opengrep scan`)
```bash
# Varredura básica utilizando conjunto de regras local ou automático
opengrep scan --config auto .

# Varredura apontando para um diretório ou arquivo de regras YAML específico
opengrep scan --config ./rules/security.yaml src/

# Varredura com múltiplos conjuntos de regras
opengrep scan --config ./rules/sast/ --config ./rules/custom/ src/

# Filtragem por severidade mínima (INFO, WARNING, ERROR)
opengrep scan --config auto --severity ERROR .

# Forçar código de saída não-zero em caso de vulnerabilidades encontradas (ideal para CI/CD Quality Gate)
opengrep scan --config auto --error .

# Exclusão e inclusão de diretórios/arquivos específicos
opengrep scan --config auto --exclude "tests/" --exclude "vendor/" --exclude "*.min.js" .
```

### 3. Formatos de Saída e Exportação
```bash
# Exportar relatório em formato JSON estruturado
opengrep scan --config auto --json --output opengrep-report.json .

# Exportar relatório no padrão OASIS SARIF (para ingestão no GitHub Security Tab / SonarQube / DefectDojo)
opengrep scan --config auto --sarif-output=opengrep.sarif .

# Modo silencioso apenas com o resumo final
opengrep scan --config auto --quiet .
```

### 4. Testes de Regras Personalizadas (`opengrep test`)
```bash
# Executar a suíte de testes unitários de regras YAML contra arquivos de teste
opengrep test ./rules/
```

---

## 📜 Sintaxe de Criação de Regras Declarativas em YAML

Todas as regras do Opengrep seguem o esquema padrão YAML, divididas em regras de casamento de padrões sintáticos (*Pattern Matching*) ou regras de rastreamento de contaminação (*Taint Mode*).

### 1. Operadores Fundamentais de Casamento
- **Reticências (`...`)**: Corresponde a zero ou mais argumentos, instruções, expressões ou parâmetros.
- **Metavariáveis (`$VAR`)**: Captura e referencia qualquer variável, função ou expressão no código. Todas as ocorrências do mesmo nome de metavariável dentro de um padrão devem casar com o mesmo valor literal/simbólico.

### 2. Exemplo: Detecção de Command Injection com Padrões Simples
```yaml
rules:
  - id: nodejs-command-injection-child-process
    languages:
      - javascript
      - typescript
    message: "Possível injeção de comandos detectada. O uso de child_process.exec com dados dinâmicos pode permitir execução arbitrária de código no sistema operacional. Utilize execFile ou spawn com lista de argumentos fixa."
    severity: ERROR
    metadata:
      cwe: "CWE-78: Improper Neutralization of Special Elements used in an OS Command"
      owasp: "A03:2021 - Injection"
      confidence: HIGH
      category: security
    patterns:
      - pattern: child_process.exec($CMD, ...)
      - pattern-not: child_process.exec("...", ...)
      - pattern-not: child_process.exec(`...`, ...)
```

### 3. Exemplo: Taint Analysis Completa em Python (SQL Injection)
No modo `taint`, o Opengrep rastreia a origem dos dados até o ponto de consumo crítico:
```yaml
rules:
  - id: python-flask-sql-injection-taint
    mode: taint
    languages:
      - python
    message: "SQL Injection detectado: entrada não confiável originada da requisição Flask alcança a execução de query SQL sem parametrização."
    severity: ERROR
    metadata:
      cwe: "CWE-89: SQL Injection"
      owasp: "A03:2021 - Injection"
      category: security
    
    # 1. Origens de dados não confiáveis
    pattern-sources:
      - pattern: flask.request.args.get(...)
      - pattern: flask.request.form[...]
      - pattern: flask.request.json[...]
      - pattern: flask.request.headers.get(...)
      - pattern: flask.request.get_json(...)
    
    # 2. Propagação através de concatenações ou formatações de string
    pattern-propagators:
      - pattern: $TARGET = f"...{$SOURCE}..."
        from: $SOURCE
        to: $TARGET
      - pattern: $TARGET = "...".format(..., $SOURCE, ...)
        from: $SOURCE
        to: $TARGET
      - pattern: $TARGET = $A + $SOURCE
        from: $SOURCE
        to: $TARGET

    # 3. Sanitizadores (Neutralizam a contaminação)
    pattern-sanitizers:
      - pattern: int(...)
      - pattern: float(...)
      - pattern: uuid.UUID(...)
      - pattern: sqlalchemy.text(...)

    # 4. Sumidouros críticos (Sinks)
    pattern-sinks:
      - pattern: $DB.session.execute($QUERY, ...)
      - pattern: $CURSOR.execute($QUERY, ...)
      - pattern: sqlite3.connect(...).cursor().execute($QUERY, ...)
```

---

## 🧪 Estrutura de Testes Unitários de Regras

Para garantir que uma regra não produza falsos positivos nem perca casos reais, crie um arquivo de teste com a mesma extensão da linguagem ao lado do arquivo `.yaml` de regras.

### Exemplo de Teste Unitário (`nodejs-command-injection.js`):
```javascript
const child_process = require('child_process');

function testVulnerable(req, res) {
    let userInput = req.query.cmd;
    // ruleid: nodejs-command-injection-child-process
    child_process.exec("ping -c 1 " + userInput, (err, stdout) => {
        console.log(stdout);
    });
}

function testSafe() {
    // ok: nodejs-command-injection-child-process
    child_process.exec("ls -la /tmp", (err, stdout) => {
        console.log(stdout);
    });
}
```
Ao executar `opengrep test ./rules/`, o motor valida que a linha comentada com `// ruleid:` dispara o alerta e a linha com `// ok:` é ignorada.

---

## 🚀 Integração em Pipelines de CI/CD

### 1. Workflow do GitHub Actions com SARIF Upload
```yaml
name: Opengrep Security Scan

on:
  push:
    branches: [ "main", "develop" ]
  pull_request:
    branches: [ "main" ]

jobs:
  opengrep:
    name: Opengrep SAST Scan
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
      actions: read

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Install Opengrep
        run: |
          curl -fsSL https://github.com/opengrep/opengrep/releases/latest/download/opengrep-linux-x86_64 -o /usr/local/bin/opengrep
          chmod +x /usr/local/bin/opengrep

      - name: Run Opengrep SAST
        run: |
          opengrep scan --config auto --sarif-output=results.sarif --error .

      - name: Upload SARIF to GitHub Security Tab
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif
```

### 2. Configuração de Pre-commit Hook
Adicione ao arquivo `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/opengrep/opengrep
    rev: v1.0.0
    hooks:
      - id: opengrep
        args: ['scan', '--config', 'auto', '--error']
```

---

## 🔗 Integração com Outras Skills do Repositório

- **[sast-code-review](../../security/appsec/sast-code-review/SKILL.md)**: Aplica a taxonomia de vulnerabilidades e boas práticas de triagem em conjunto com o motor Opengrep.
- **[program-github-actions](../github-actions/SKILL.md)**: Automação completa de workflows, caching de binários e Quality Gates no GitHub Actions.
- **[devsecops-engineer](../../security/ops-architecture/devsecops-engineer/SKILL.md)**: Governança centralizada de esteiras de segurança e métricas de correção.
