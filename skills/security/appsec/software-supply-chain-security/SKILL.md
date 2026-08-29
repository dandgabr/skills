---
name: software-supply-chain-security
description: "Especialista em Segurança da Cadeia de Suprimentos de Software (Software Supply Chain Security), Análise de Composição de Software (SCA) e Gestão de Dependências baseado em Cassie Crossley e NIST SSDF / SP 800-161. Cobre geração e auditoria de SBOM (CycloneDX v1.5/v1.6 e SPDX v2.3/v3.0), VEX, proveniência SLSA v1.0, assinatura criptográfica com Sigstore/Cosign e in-toto, mitigação de vulnerabilidades (CVEs, GHSA, EPSS, CISA KEV), auditoria de licenças de código aberto (GPL, AGPL, Apache, MIT), pinning de lockfiles, e defesa contra typosquatting e dependency confusion."
metadata:
  type: defensive
  phase: recon
  tools: [syft, grype, trivy, snyk, owasp-dependency-check, cosign, slsa-verifier]
  mitre: [T1195, T1195.001, T1195.002, T1140]
---

# Segurança da Cadeia de Suprimentos de Software (Supply Chain Security & SCA)

Esta skill estabelece as diretrizes canônicas para auditoria, proteção, gestão de vulnerabilidades em bibliotecas de terceiros (*Software Composition Analysis - SCA*) e verificação da integridade de ponta a ponta na cadeia de suprimentos de software e firmware, fundamentada na obra de **Cassie Crossley**, no framework **SLSA (Supply-chain Levels for Software Artifacts)**, **NIST SP 800-161 Rev. 1** e **NIST SSDF (SP 800-218)**.

---

## 🛡️ 1. Pilares da Cadeia de Suprimentos de Software

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Fonte & Upstream (Manifestos, Lockfiles, Dependências)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 2. Pipeline de Build CI/CD (Hermetic Builds, Runners, SLSA) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 3. Pacotes & Artefatos (SBOM, Assinatura Sigstore/Cosign)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 4. Runtime & Deploy (Admission Controllers, VEX, Attestation)│
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 2. Padrões de SBOM (Software Bill of Materials) e VEX

### 2.1 Formatos Oficiais
- **CycloneDX (OWASP)**: Especializado em segurança de aplicações, inventário de dependências diretas e transitivas, serviços de nuvem, formulação de VEX (*Vulnerability Exploitability eXchange*) e formulários de conformidade.
- **SPDX (Linux Foundation / ISO/IEC 5962:2021)**: Padrão internacional para conformidade de licenças de código aberto e proveniência de arquivos e pacotes.

### 2.2 Requisitos Mínimos (NTIA Minimum Elements)
1. **Nome do Fornecedor / Autor (Supplier Name)**.
2. **Nome do Componente (Component Name)**.
3. **Versão do Componente (Component Version)**.
4. **Identificadores Únicos**: Package URL (`purl`) e Common Platform Enumeration (`CPE`).
5. **Relação de Dependência**: Direta vs Transitiva (*DependsOn*).
6. **Autor dos Dados do SBOM**.
7. **Timestamp de Geração**.

### 2.3 Geração Automatizada de SBOM
```bash
# Gerar SBOM CycloneDX JSON via Syft
syft packages dir:. -o cyclonedx-json=sbom.cyclonedx.json

# Gerar SBOM SPDX JSON via Trivy
trivy fs --format spdx-json --output sbom.spdx.json .
```

---

## 🔍 3. Análise de Composição de Software (SCA) & Gestão de CVEs

### 3.1 Mapeamento da Árvore de Dependências por Ecossistema
- **Node.js / JS / TS**: `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.
- **Python**: `pyproject.toml`, `poetry.lock`, `requirements.txt`, `Pipfile.lock`.
- **Java / Kotlin**: `pom.xml` (Maven), `build.gradle` / `gradle.lockfile` (Gradle).
- **Go**: `go.mod`, `go.sum`.
- **Rust**: `Cargo.toml`, `Cargo.lock`.
- **C/C++**: `vcpkg.json`, `conanfile.txt` / `conan.lock`.

### 3.2 Priorização Baseada em Risco Real: CVSS + EPSS + CISA KEV
Não priorize remediações apenas pelo score bruto de CVSS. Utilize a fórmula multidimensional de risco:
- **CVSS v3.1 / v4.0**: Mede a severidade intrínseca da falha técnica.
- **EPSS (Exploit Prediction Scoring System)**: Mede a probabilidade estatística (0.0 a 1.0) de haver exploração nos próximos 30 dias.
- **CISA KEV (Known Exploited Vulnerabilities)**: Catálogo oficial de vulnerabilidades com evidência confirmada de exploração em ambientes reais.

---

## 📜 4. Auditoria de Licenças de Código Aberto (OSS License Compliance)

| Categoria de Licença | Exemplos | Impacto / Restrições |
| :--- | :--- | :--- |
| **Permissivas** | MIT, Apache 2.0, BSD-2/3-Clause, ISC | Permite uso comercial e código fechado com menção de copyright. |
| **Copyleft Fraco** | LGPL v2.1/v3, MPL 2.0, EPL 2.0 | Modificações na própria biblioteca devem ser abertas; o código cliente pode ser proprietário se linkado dinamicamente. |
| **Copyleft Forte (Viral)** | GPL v2/v3, AGPL v3 | Obriga que qualquer software derivado ou distribuído que use a biblioteca tenha seu código-fonte integralmente aberto. |

---

## 🔒 5. Proveniência SLSA e Assinatura Criptográfica (Sigstore / Cosign)

### 5.1 Níveis SLSA v1.0
- **SLSA Build L1**: Processo de build automatizado gerando atestado de proveniência básico.
- **SLSA Build L2**: Build executado em runner CI/CD gerenciado com controle de versão e proveniência assinada criptograficamente.
- **SLSA Build L3**: Build hermético e efêmero em ambiente isolado, prevenindo adulterações e garantindo reprodutibilidade estrita.

### 5.2 Assinatura de Imagens de Contêiner e Atestados
```bash
# Assinar imagem de contêiner usando OIDC (Keyless via Sigstore)
cosign sign --yes ghcr.io/empresa/app:v1.0.0

# Anexar e assinar o SBOM à imagem no registry
cosign attach sbom --sbom sbom.cyclonedx.json ghcr.io/empresa/app:v1.0.0
cosign sign --yes --attachment sbom ghcr.io/empresa/app:v1.0.0

# Verificar assinatura no Kubernetes Admission Controller
cosign verify --certificate-identity-regexp "https://github.com/empresa/.*" \
              --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
              ghcr.io/empresa/app:v1.0.0
```

---

## 🛑 6. Proteção contra Vetores Específicos de Supply Chain

1. **Dependency Confusion**: Registre escopos privados `@empresa` no registro público (npm/PyPI) ou configure o gerenciador de pacotes para nunca consultar o registro público para escopos corporativos.
2. **Typosquatting**: Utilize ferramentas de verificação de similaridade de strings em pipelines de PR antes de instalar novas dependências.
3. **Lockfile Poisoning**: Execute sempre `npm ci` / `poetry install --sync` / `cargo build --locked` em pipelines de CI/CD para impedir a resolução dinâmica de versões não homologadas.
