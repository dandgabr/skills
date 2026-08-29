---
name: software-supply-chain-security
description: "Especialista em Segurança da Cadeia de Suprimentos de Software (Software Supply Chain Security), Análise de Composição de Software (SCA) e Gestão de Dependências baseado em Cassie Crossley e NIST SSDF / SP 800-161. Cobre geração e auditoria de SBOM (CycloneDX v1.5/v1.6 e SPDX v2.3/v3.0), VEX, proveniência SLSA v1.0, assinatura criptográfica com Sigstore/Cosign e in-toto, mitigação de vulnerabilidades (CVEs, GHSA, EPSS, CISA KEV), auditoria de licenças de código aberto (GPL, AGPL, Apache, MIT), pinning de lockfiles, análise de alcançabilidade (call-graph reachability), e defesa contra typosquatting e dependency confusion."
metadata:
  type: defensive
  phase: recon
  tools: [owasp-dependency-check, syft, grype, trivy, snyk, cosign, slsa-verifier]
  mitre: [T1195, T1195.001, T1195.002, T1140]
---

# Segurança da Cadeia de Suprimentos de Software (Supply Chain Security & SCA)

Esta skill estabelece as diretrizes canônicas para auditoria, proteção, gestão de vulnerabilidades em bibliotecas de terceiros (*Software Composition Analysis - SCA*), análise de alcançabilidade (*Reachability Analysis*), conformidade de licenças e verificação da integridade de ponta a ponta na cadeia de suprimentos de software e firmware, fundamentada na obra de **Cassie Crossley** (*Software Supply Chain Security: Securing the End-to-end Supply Chain for Software, Firmware, and Hardware*), no framework **SLSA (Supply-chain Levels for Software Artifacts v1.0)**, no **NIST SP 800-161 Rev. 1** e no **NIST SSDF (SP 800-218)**.

---

## 🛡️ 1. Pilares da Cadeia de Suprimentos de Software

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. Fonte & Upstream (Manifestos, Lockfiles, Dependências Diretas/Trans) │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
┌──────────────────────────────────▼─────────────────────────────────────┐
│ 2. Pipeline de Build CI/CD (Hermetic Builds, Runners Efêmeros, SLSA)   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
┌──────────────────────────────────▼─────────────────────────────────────┐
│ 3. Pacotes & Artefatos (SBOM CycloneDX/SPDX, Assinatura Sigstore/Cosign)│
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
┌──────────────────────────────────▼─────────────────────────────────────┐
│ 4. Runtime & Deploy (Admission Controllers, VEX, Attestation, Guardrail)│
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🔬 2. Metodologia Avançada de Software Composition Analysis (SCA)

O SCA não se resume a buscar versões em uma lista de strings. Uma análise moderna de SCA opera em quatro níveis de profundidade:

### 2.1 Resolução de Grafos e Dependências Transitivas
- **Dependência Direta**: Declarada explicitamente no manifesto do projeto (`package.json`, `pom.xml`, `pyproject.toml`).
- **Dependência Transitiva (Indireta)**: Dependências das dependências, que compõem mais de 80% do código de terceiros em aplicações modernas.
- **Lockfile Pinning & Imutabilidade**: Em pipelines automatizados, exija sempre a resolução travada por hashes criptográficos (`npm ci`, `poetry install --sync`, `cargo build --locked`) para impedir a substituição silenciosa de pacotes (*Lockfile Poisoning*).

### 2.2 Análise de Alcançabilidade (Reachability Analysis)
- Uma vulnerabilidade em uma biblioteca de terceiros só é explorável se a aplicação invocar a função, classe ou método vulnerável.
- **Classificação**:
  - *Presente no Pacote*: O arquivo `.jar` ou pacote npm está na pasta `node_modules` / `target`.
  - *Alcançável via Call-Graph*: O código proprietário executa chamadas que chegam até o método vulnerável da biblioteca.
- Ferramentas de SCA com suporte a *Reachability* (como OWASP Dependency-Check com analisadores avançados ou Snyk/Trivy) reduzem em até 70% o ruído de alertas que não requerem parada imediata de produção.

### 2.3 Priorização Multidimensional: CVSS + EPSS + CISA KEV
A IA deve calcular o risco real com base na tríade de inteligência de ameaças:
1. **CVSS v3.1 / v4.0 (Severidade Intrínseca)**: Mede o impacto teórico em confidencialidade, integridade e disponibilidade (CIA).
2. **EPSS (Exploit Prediction Scoring System - FIRST)**: Mede a probabilidade estatística (percentual de 0% a 100%) de que a CVE seja explorada na internet nos próximos 30 dias. Vulnerabilidades com EPSS > 0.36 devem ser tratadas com prioridade imediata.
3. **CISA KEV (Known Exploited Vulnerabilities Catalog)**: Catálogo oficial de vulnerabilidades com evidência ativa de exploração por grupos criminosos (*Wild Exploits*). Se uma CVE estiver no CISA KEV, sua remediação é mandatória independente do score CVSS.

---

## 📦 3. Padrões de SBOM (Software Bill of Materials) e VEX

### 3.1 Formatos Oficiais
- **CycloneDX (OWASP Foundation)**: Especializado em segurança de aplicações, inventário de dependências diretas e transitivas, serviços de nuvem, formulação de VEX (*Vulnerability Exploitability eXchange*) e formulários de conformidade.
- **SPDX (Linux Foundation / ISO/IEC 5962:2021)**: Padrão internacional para conformidade de licenças de código aberto e proveniência de arquivos e pacotes.

### 3.2 Requisitos Mínimos da NTIA (Minimum Elements for SBOM)
1. **Nome do Fornecedor / Autor (Supplier Name)**.
2. **Nome do Componente (Component Name)**.
3. **Versão do Componente (Component Version)**.
4. **Identificadores Únicos**: Package URL (`purl`) e Common Platform Enumeration (`CPE`).
5. **Relação de Dependência**: Direta vs. Transitiva (*DependsOn*).
6. **Autor dos Metadados do SBOM**.
7. **Timestamp de Geração**.

### 3.3 Formulários VEX (Vulnerability Exploitability eXchange)
O VEX permite que os mantenedores declarem formalmente se uma vulnerabilidade descoberta em uma dependência afeta ou não a aplicação:
- `not_affected`: O código vulnerável não é importado nem executado (com justificativa: `code_not_reachable`, `vulnerable_code_cannot_be_controlled_by_adversary`, `inline_mitigations_already_exist`).
- `affected`: A vulnerabilidade é explorável no contexto da aplicação.
- `fixed`: A vulnerabilidade foi corrigida na versão atual.
- `under_investigation`: Em análise pelo time de segurança.

---

## 📜 4. Auditoria de Licenças de Código Aberto (OSS License Compliance)

| Categoria de Licença | Exemplos | Impacto / Restrições |
| :--- | :--- | :--- |
| **Permissivas** | MIT, Apache 2.0, BSD-2/3-Clause, ISC | Permite uso comercial e código fechado com preservação do aviso de copyright. |
| **Copyleft Fraco** | LGPL v2.1/v3, MPL 2.0, EPL 2.0 | Modificações na própria biblioteca devem ser abertas; o código cliente pode ser proprietário se linkado dinamicamente. |
| **Copyleft Forte (Viral)** | GPL v2/v3, AGPL v3 | Obriga que qualquer software derivado ou distribuído que use a biblioteca tenha seu código-fonte integralmente aberto sob a mesma licença. |

---

## 🔒 5. Proveniência SLSA e Assinatura Criptográfica (Sigstore / Cosign)

### 5.1 Níveis SLSA v1.0
- **SLSA Build L1**: Processo de build automatizado gerando atestado de proveniência básico.
- **SLSA Build L2**: Build executado em runner CI/CD gerenciado com controle de versão e proveniência assinada criptograficamente.
- **SLSA Build L3**: Build hermético e efêmero em ambiente isolado, prevenindo adulterações e garantindo reprodutibilidade estrita.

### 5.2 Assinatura de Imagens e Anexação de SBOM
```bash
# Assinar imagem de contêiner usando OIDC (Keyless via Sigstore)
cosign sign --yes ghcr.io/empresa/app:v1.0.0

# Anexar e assinar o SBOM CycloneDX à imagem no registro OCI
cosign attach sbom --sbom sbom.cyclonedx.json ghcr.io/empresa/app:v1.0.0
cosign sign --yes --attachment sbom ghcr.io/empresa/app:v1.0.0

# Verificar assinatura no Kubernetes Admission Controller
cosign verify --certificate-identity-regexp "https://github.com/empresa/.*" \
              --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
              ghcr.io/empresa/app:v1.0.0
```

---

## 🛑 6. Proteção contra Vetores Específicos de Supply Chain

1. **Dependency Confusion**: Registre escopos privados `@empresa` no registro público (npm/PyPI) ou configure o gerenciador de pacotes para consultar exclusivamente o registry privado interno para pacotes corporativos.
2. **Typosquatting**: Utilize ferramentas de verificação de similaridade fonética e de string em pipelines de PR antes de aceitar novas bibliotecas.
3. **Comprometimento de Conta de Mantenedor (Account Takeover)**: Utilize ferramentas que avaliem o *Scorecard da OpenSSF* (MFA de mantenedor, proteção de branches, atividade recente de commits).

---

## 🔗 Integração com Outras Skills do Repositório

- **[program-owasp-dependency-check](../../programs/program-owasp-dependency-check/SKILL.md)**: Guia operacional completo da ferramenta OWASP Dependency-Check (CLI, Maven, Gradle e NVD API v2).
- **[sast-code-review](../sast-code-review/SKILL.md)**: Complementa a análise de bibliotecas com a auditoria de vulnerabilidades no código proprietário.
- **[devsecops-engineer](../../ops-architecture/devsecops-engineer/SKILL.md)**: Orquestração de pipelines de SCA, geração de SBOMs e Quality Gates no CI/CD.
- **[program-containers](../../programs/containers/SKILL.md)**: Auditoria e assinatura de imagens de contêiner e pacotes base de sistema operacional.
