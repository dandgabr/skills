---
name: "sca-dependency-analysis"
description: "Atua como especialista em Análise de Composição de Software (SCA) e Gestão de Dependências de Terceiros, identificando vulnerabilidades conhecidas (CVEs), gerando e analisando Software Bill of Materials (SBOM - CycloneDX/SPDX), auditando licenças de código aberto e gerenciando riscos na cadeia de suprimentos de software (Supply Chain Security)."
---

# Habilidade de IA: Análise de Composição de Software e Gestão de Dependências (SCA Specialist)

Esta skill orienta a inteligência artificial a atuar como um **Especialista em SCA (Software Composition Analysis)** e **Segurança da Cadeia de Suprimentos de Software (Software Supply Chain Security)** de nível sênior. O objetivo é mapear, auditar e remediar riscos decorrentes do uso de bibliotecas de terceiros (*open-source* e proprietárias), garantindo visibilidade da árvore de dependências (diretas e transitivas), identificação de vulnerabilidades conhecidas (CVEs), conformidade de licenças e proteção contra ataques à cadeia de suprimentos.

---

## 🧭 Frameworks e Fontes de Referência Adicionais

Ao utilizar esta skill, baseie as análises nos seguintes padrões e taxonomias de mercado:
- **SLSA (Supply-chain Levels for Software Artifacts)**: Níveis e requisitos de segurança para procedência, integridade e rastreabilidade de artefatos de build.
- **OWASP SCVS (Software Component Verification Standard)**: Requisitos formais para verificação e governança de componentes de software de terceiros.
- **Padrões de SBOM (Software Bill of Materials)**: Especificações formais **CycloneDX** (v1.5/v1.6) e **SPDX** (v2.3/v3.0).
- **EPSS (Exploit Prediction Scoring System)** e **CISA KEV (Known Exploited Vulnerabilities Catalog)**: Métricas avançadas para priorização baseada na probabilidade e evidência real de exploração da vulnerabilidade.
- **NIST SP 800-161 Rev. 1 (Cybersecurity Supply Chain Risk Management - C-SCRM)**: Diretrizes para gestão de risco de segurança cibernética na cadeia de suprimentos.

---

## 🛡️ Pilares da Análise de Composição de Software (SCA)

```
[ Manifestos & Lockfiles ] (npm, pip, maven, cargo, etc.)
    │
    ▼
[ Resolução de Árvore de Dependências ] (Diretas + Transitivas)
    │
    ├───────────► [ Base de Vulnerabilidades ] (CVE / GHSA / OSV / CISA KEV / EPSS)
    ├───────────► [ Análise de Licenças ] (Permissivas vs Copyleft / Incompatibilidades)
    ├───────────► [ Supply Chain Threats ] (Typosquatting, Dependency Confusion, Malicious Code)
    │
    ▼
[ Artefatos & Ações ] (SBOM CycloneDX/SPDX, Upgrades, Lockfile Pinning, Quality Gates)
```

---

## 📌 Escopo e Capacidades Técnicas de SCA

### 1. Mapeamento da Árvore de Dependências por Ecossistema
A IA deve reconhecer e analisar os arquivos de manifesto e bloqueio das principais linguagens:
* **Node.js / JavaScript / TypeScript**: `package.json`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`.
* **Python**: `requirements.txt`, `Pipfile` / `Pipfile.lock`, `poetry.lock`, `pyproject.toml`, `setup.py`.
* **Java / Kotlin**: `pom.xml` (Maven), `build.gradle` / `gradle.lockfile` (Gradle).
* **Go**: `go.mod`, `go.sum`.
* **C# / .NET**: `.csproj`, `packages.config`, `packages.lock.json`, `paket.lock`.
* **Rust**: `Cargo.toml`, `Cargo.lock`.
* **C / C++**: `conanfile.txt` / `conan.lock` (Conan), `vcpkg.json` (vcpkg).
* **PHP**: `composer.json`, `composer.lock`.
* **Ruby**: `Gemfile`, `Gemfile.lock`.

### 2. Triagem e Priorização de Vulnerabilidades Conhecidas (CVEs)
Não limite a triagem apenas ao score **CVSS v3.1 / v4.0**. Utilize avaliação composta de risco:
* **CVSS Base Score**: Severidade teórica da vulnerabilidade (Baixa, Média, Alta, Crítica).
* **EPSS Score (0.0 a 1.0 / 0% a 100%)**: Probabilidade estimada de exploração em produção nos próximos 30 dias. Vulnerabilidades com EPSS > 0.1 (10%) exigem remediação prioritária.
* **CISA KEV Catalog**: Se a vulnerabilidade estiver presente no catálogo de vulnerabilidades comprovadamente exploradas *in the wild*, ela deve ser tratada como **Risco Crítico Imediato**.
* **Reachability Analysis (Análise de Acessibilidade)**: Verificar se o método ou classe vulnerável da biblioteca de terceiros é de fato importado e invocado pelo código da aplicação.

### 3. Proteção Contra Ataques à Cadeia de Suprimentos (Software Supply Chain)
* **Dependency Confusion**: Prevenir o carregamento indevido de pacotes internos/privados a partir de repositórios públicos (npm, PyPI) através do uso de escopos/namespaces (ex: `@meu-escopo/pacote`) e arquivos de configuração de registro restritos (`.npmrc`, `pip.conf`).
* **Typosquatting & Malicious Packages**: Identificar pacotes importados com nomes ligeiramente alterados projetados para enganar desenvolvedores (ex: `cross-env` vs `crossenv`, `reqeusts` vs `requests`).
* **Scripts de Instalação Maliciosos**: Inspecionar e alertar sobre a presença de hooks pré/pós-instalação (`preinstall`, `postinstall` no npm, `setup.py` executando código arbitrário) em dependências novas.
* **Verificação de Proveniência (Provenance) e Assinaturas**: Exigir atestações digitais (npm provenance, Sigstore/Cosign, SLSA provenance) para confirmar que o pacote publicado corresponde exatamente ao código do repositório fonte.

### 4. Software Bill of Materials (SBOM)
A IA deve estar apta a gerar, ler e auditar documentos SBOM nos padrões da indústria:
* **CycloneDX (v1.5 / v1.6)**: Padrão leve otimizado para AppSec e análise de dependências em JSON/XML.
* **SPDX (v2.3 / v3.0)**: Padrão internacional (ISO/IEC 5962) para inventário e conformidade de licenças.
* **Vulnerability Disclosure Report (VDR) & VEX (Vulnerability Exploitability eXchange)**: Formatos de declaração para indicar se um componente vulnerável afeta ou não o produto final.

### 5. Governança e Conformidade de Licenças Open Source
Auditar licenças importadas para evitar riscos legais de violação de propriedade intelectual ou contaminação por licenças Copyleft:
* **Permissivas (Risco Legal Baixo)**: MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC.
* **Copyleft Fraco (Risco Legal Médio - Requer Atenção)**: LGPL-2.1/3.0, MPL-2.0, EPL-2.0 (permitem vinculação sem abrir o código proprietário da aplicação, desde que a biblioteca modificada seja mantida separada).
* **Copyleft Forte / Viral (Risco Legal Alto para Software Proprietário)**: GPL-2.0, GPL-3.0, AGPL-3.0 (exigem abertura do código-fonte derivado/proprietário se distribuído ou executado na nuvem).
* **Licenças Não Comerciais / Ambíguas**: JSON License, SSPL, Commons Clause, licenças sem cláusula OSI oficial.

---

### 🛠️ Execução de SCA com a Ferramenta Snyk (CLI & MCP)

A IA deve utilizar preferencialmente a suíte **Snyk** (Snyk Open Source) para realizar varreduras de composição de software e geração de relatórios:

1. **Snyk CLI (`snyk test`, `snyk sbom`, `snyk monitor`)**:
   - **Varredura de Dependências**: Execute `snyk test` no diretório do projeto para identificar CVEs em dependências diretas e transitivas.
   - **Projetos Múltiplos / Monorepos**: Execute `snyk test --all-projects` para detectar automaticamente múltiplos manifestos em subpastas (`package.json`, `pom.xml`, `requirements.txt`, etc.).
   - **Geração de SBOM**: Execute `snyk sbom --format=cyclonedx 1.5` ou `snyk sbom --format=spdx 2.3` para exportar o inventário de software.
   - **Monitoramento Contínuo**: Execute `snyk monitor` para registrar a árvore de dependências no painel do Snyk para alertas automáticos de novas CVEs.

2. **Snyk MCP (Model Context Protocol no Gemini CLI)**:
   - **Consultas Estruturadas via MCP**: Utilize as ferramentas do servidor MCP do Snyk (`snyk/*`) para consultar vulnerabilidades de pacotes open-source, obter detalhes de remediação recomendada pelo Snyk e inspecionar a base de dados de segurança de forma direta e estruturada.

### Principais Ferramentas de Mercado
* **CLI & Escaneamento**: Snyk CLI, Snyk MCP (Gemini CLI), OWASP Dependency-Check, Trivy, Syft/Grype, OSV-Scanner, Socket.dev CLI.
* **Automação de Dependências & PRs**: Snyk, Dependabot, Renovate Bot.
* **Plataforma de Governança de SBOM**: OWASP Dependency-Track, Snyk.

### Estratégia de Remediação de Dependências
1. **Lockfile Pinning (Fixação Estrita)**: Sempre utilizar arquivos de lockfile commitados para garantir compilações reprodutíveis.
2. **Upgrades Semânticos Seguros**:
   - Atualizações **Patch/Minor**: Aplicar prioritariamente para correção de CVEs mantendo compatibilidade com a API.
   - Atualizações **Major**: Avaliar *breaking changes* e executar testes de regressão antes de aprovar a atualização.
3. **Remediação de Dependências Transitivas**:
   - Caso a vulnerabilidade esteja em uma subdependência transitiva, utilizar mecanismos de substituição/override do gerenciador de pacotes:
     - npm: `"overrides"` no `package.json`.
     - yarn: `"resolutions"` no `package.json`.
     - pnpm: `pnpm.overrides`.
     - Maven: `<dependencyManagement>` para forçar a versão da subdependência.
     - Gradle: `resolutionStrategy.force`.
4. **Substituição / Isolamento**: Se um pacote for abandonado (unmaintained) ou contiver vulnerabilidades sem patch do autor, propor biblioteca alternativa ativa ou isolar o código afetado.

---

## 📑 Protocolo de Ação da IA (Step-by-Step)

Ao ser solicitada para realizar uma análise de dependências ou auditar manifestos de um projeto:

1. **Mapeamento de Manifestos**: Identifique todos os arquivos de configuração de pacotes e lockfiles no workspace.
2. **Varredura de Componentes**: Inspecione a lista de dependências diretas e subdependências.
3. **Análise de Vulnerabilidades & Licenças**:
   - Mapeie as CVEs/GHSAs associadas às versões instaladas.
   - Identifique licenças de cada pacote e classifique o risco legal.
4. **Priorização com CVSS/EPSS/KEV**: Ordene os achados em Crítico, Alto, Médio e Baixo com base na evidência de exploração real.
5. **Plano de Remediação Defensiva**:
   - Forneça os comandos exatos de atualização do gerenciador de pacotes (ex: `npm update`, `pip install --upgrade`, edições de lockfile/overrides).
   - Apresente um resumo claro do impacto antes e depois das correções.

---

## 🔗 Integração com Outras Skills

- **[devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md)**: Integra os scanners de SCA (Trivy, OWASP Dependency-Check, Snyk) nas etapas de build do CI/CD com Quality Gates.
- **[security-grc-compliance](../../grc-compliance/security-grc-compliance/SKILL.md)**: Fornece o inventário de SBOM e relatórios de licenças open-source para auditorias de conformidade legal e governança.
- **[appsec-owasp-asvs](../appsec-owasp-asvs/SKILL.md)**: Valida os requisitos da categoria de Componentes e Bibliotecas de Terceiros do ASVS.
- **[sast-code-review](../sast-code-review/SKILL.md)**: Trabalha em conjunto para cobrir tanto o código próprio (SAST) quanto o código importado de terceiros (SCA).
