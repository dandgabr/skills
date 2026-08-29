---
name: program-owasp-dependency-check
description: Guia Definitivo e Padrões de Engenharia para OWASP Dependency-Check (owasp.org/www-project-dependency-check), cobrindo Software Composition Analysis (SCA), CLI, plugins Maven e Gradle, GitHub Actions, integração com NVD API v2, banco de dados centralizado de CVEs, sintaxe completa de suppressions.xml, CPE hints e Quality Gates baseados em CVSS.
metadata:
  type: defensive
  phase: testing
  mitre:
    - T1195.001
    - T1195.002
  tools:
    - owasp-dependency-check
    - maven
    - gradle
---

# Habilidade de IA: Guia e Engenharia com OWASP Dependency-Check (SCA Tool)

Esta skill fornece orientação técnica canônica, comandos operacionais e padrões de engenharia para o **OWASP Dependency-Check** ([owasp.org/www-project-dependency-check](https://owasp.org/www-project-dependency-check/)), a ferramenta open-source padrão para **Software Composition Analysis (SCA)**, projetada para identificar vulnerabilidades conhecidas (CVEs) em bibliotecas e componentes de terceiros em projetos de software.

---

## 🧭 Visão Geral e Funcionamento do Dependency-Check

O OWASP Dependency-Check coleta evidências sobre as dependências do projeto (Vendor, Product, Version) a partir de manifestos, nomes de arquivos, hashes e metadados de pacotes, mapeia essas informações para identificadores de **CPE (Common Platform Enumeration)** e consulta as bases da **NVD (National Vulnerability Database)** e **GitHub Security Advisory (GHSA)** para relatar CVEs associadas.

```
┌────────────────────────────────────────────────────────────────────────┐
│               FLUXO DE ANÁLISE DO OWASP DEPENDENCY-CHECK               │
└────────────────────────────────────────────────────────────────────────┘
  [ 1. Coleta de Evidências ]
         │  (Analisa JARs, package.json, pom.xml, go.mod, arquivos binários)
         ▼
  [ 2. Mapeamento de CPE ]
         │  (Gera identificadores: cpe:2.3:a:apache:log4j:2.14.1:*:*:*:*:*:*:*)
         ▼
  [ 3. Consulta NVD API v2 & Cache Local ]
         │  (Verifica banco de dados H2 local ou PostgreSQL centralizado)
         ▼
  [ 4. Aplicação de Supressões (suppressions.xml) ]
         │  (Descarta falsos positivos e vulnerabilidades com mitigação aceita)
         ▼
  [ 5. Avaliação de Quality Gate (failBuildOnCVSS) ]
            (Falha a compilação caso CVSS >= Limiar definido)
```

---

## 💻 Modos de Integração e Execução

### 1. Linha de Comando (CLI)

```bash
# Execução básica com exportação em múltiplos formatos (HTML, JSON, SARIF)
dependency-check.sh \
    --project "EcommerceApp" \
    --scan "./src" \
    --scan "./lib" \
    --out "./reports" \
    --format "ALL" \
    --nvdApiKey "SEU_NVD_API_KEY" \
    --failOnCVSS 7.0

# Execução utilizando arquivo de supressão de falsos positivos
dependency-check.sh \
    --project "EcommerceApp" \
    --scan "./target" \
    --suppression "./config/dependency-check-suppressions.xml" \
    --format "HTML" \
    --out "./reports"
```

---

### 2. Integração com Apache Maven (`pom.xml`)

Adicione o plugin `dependency-check-maven` no bloco `<build><plugins>`:

```xml
<plugin>
    <groupId>org.owasp</groupId>
    <artifactId>dependency-check-maven</artifactId>
    <version>10.0.3</version>
    <configuration>
        <!-- Chave de API NVD v2 obrigatória para evitar rate-limits -->
        <nvdApiKey>${env.NVD_API_KEY}</nvdApiKey>
        
        <!-- Arquivo de supressão de falsos positivos -->
        <suppressionFiles>
            <suppressionFile>${project.basedir}/config/dependency-check-suppressions.xml</suppressionFile>
        </suppressionFiles>
        
        <!-- Falhar a compilação do Maven se houver vulnerabilidade High/Critical -->
        <failBuildOnCVSS>7.0</failBuildOnCVSS>
        
        <!-- Formatos de saída gerados -->
        <formats>
            <format>HTML</format>
            <format>JSON</format>
            <format>SARIF</format>
        </formats>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>check</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

#### Comandos de Execução no Maven:
```bash
# Executar a verificação avulsa
mvn org.owasp:dependency-check-maven:check

# Executar apenas a atualização do banco de dados NVD em cache
mvn org.owasp:dependency-check-maven:update-only
```

---

### 3. Integração com Gradle (`build.gradle`)

```groovy
plugins {
    id 'org.owasp.dependencycheck' version '10.0.3'
}

dependencyCheck {
    nvd {
        apiKey = System.getenv('NVD_API_KEY')
    }
    suppressionFile = 'config/dependency-check/suppressions.xml'
    failBuildOnCVSS = 7.0f
    formats = ['HTML', 'JSON', 'SARIF']
    analyzers {
        assemblyEnabled = false
        nodeAudit {
            enabled = true
        }
    }
}
```

#### Comando de Execução no Gradle:
```bash
./gradlew dependencyCheckAnalyze
```

---

## 🔑 Configuração da NVD API v2 e Banco Centralizado

Devido às restrições estritas de taxa (*Rate Limiting*) introduzidas na NVD API v2 do NIST, a obtenção de uma **NVD API Key** gratuita é mandatória para evitar erros `403 Forbidden` ou downloads que ultrapassam 40 minutos em pipelines CI/CD.

### Configuração de Banco de Dados Centralizado (PostgreSQL / MySQL)
Em pipelines corporativos com múltiplos runners concorrentes, configure o Dependency-Check para utilizar um banco relacional centralizado em vez de arquivos H2 individuais:

```xml
<configuration>
    <databaseProperties>
        <driver>org.postgresql.Driver</driver>
        <url>jdbc:postgresql://db-sec.empresa.local:5432/dependencycheck</url>
        <user>dc_user</user>
        <password>${env.DB_PASSWORD}</password>
    </databaseProperties>
</configuration>
```

---

## 🛡️ Gestão de Falsos Positivos e Arquivo de Supressão (`suppressions.xml`)

O arquivo de supressão permite ignorar CVEs que não afetam a aplicação (por exemplo, quando o método vulnerável não é executado ou o CPE casou incorretamente com uma biblioteca homônima).

### Sintaxe Completa do Arquivo `dependency-check-suppressions.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<suppressions xmlns="https://jeremylong.github.io/DependencyCheck/dependency-suppression.1.4.xsd">

    <!-- 1. Supressão de falso positivo por CPE incorreto -->
    <suppress>
        <notes><![CDATA[
            Falso positivo: O componente interno 'auth-module' foi incorretamente 
            identificado como o produto legado Apache Auth.
        ]]></notes>
        <packageUrl regex="true">^pkg:maven/com\.empresa/auth-module@.*$</packageUrl>
        <cpe>cpe:/a:apache:auth</cpe>
    </suppress>

    <!-- 2. Supressão de CVE específica com data de expiração (Until) -->
    <suppress until="2026-12-31Z">
        <notes><![CDATA[
            CVE-2022-1471 no SnakeYaml: Avaliada pelo time de AppSec. A aplicação não 
            utiliza deserialização genérica não confiável. Mitigação aceita até a migração v2.0.
        ]]></notes>
        <packageUrl regex="true">^pkg:maven/org\.yaml/snakeyaml@.*$</packageUrl>
        <vulnerabilityName>CVE-2022-1471</vulnerabilityName>
    </suppress>

    <!-- 3. Supressão por hash SHA-1 de arquivo binário específico -->
    <suppress>
        <notes><![CDATA[
            Supressão para binário de testes interno legado.
        ]]></notes>
        <sha1>66734244CE86857018B023A8C56AE0635C56B6A1</sha1>
        <cve>CVE-2020-99999</cve>
    </suppress>

</suppressions>
```

---

## 🚀 Integração em CI/CD (GitHub Actions Workflow)

```yaml
name: SCA Dependency-Check Scan

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  dependency_check:
    name: OWASP Dependency-Check (SCA)
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Run OWASP Dependency-Check
        uses: dependency-check/Dependency-Check_Action@10.0.3
        with:
          project: 'EcommerceBackend'
          path: '.'
          format: 'SARIF'
          args: >
            --nvdApiKey ${{ secrets.NVD_API_KEY }}
            --failOnCVSS 7
            --suppression config/dependency-check-suppressions.xml

      - name: Upload SARIF to GitHub Security Tab
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: 'reports/dependency-check-report.sarif'
```

---

## 🔗 Integração com Outras Skills do Repositório

- **[software-supply-chain-security](../../security/appsec/software-supply-chain-security/SKILL.md)**: Teoria de gestão de dependências, SBOM (CycloneDX/SPDX), VEX e priorização por EPSS/CISA KEV.
- **[sast-code-review](../../security/appsec/sast-code-review/SKILL.md)**: Complementa o SCA auditando falhas no código proprietário.
- **[devsecops-engineer](../../security/ops-architecture/devsecops-engineer/SKILL.md)**: Orquestração de pipelines CI/CD e Quality Gates corporativos.
- **[program-github-actions](../github-actions/SKILL.md)**: Configuração de workflows automatizados e upload de SARIF no GitHub.
