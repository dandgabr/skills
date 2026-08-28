---
name: software-supply-chain-security
description: Especialista em Segurança da Cadeia de Suprimentos de Software (Software Supply Chain Security), Firmware e Hardware baseado na obra de Cassie Crossley. Cobre geração e validação de SBOM (CycloneDX/SPDX), proveniência SLSA, assinatura criptográfica de artefatos (Sigstore/Cosign), gestão de dependências upstream, segurança de CI/CD e conformidade com a Ordem Executiva US EO 14028 e NIST SSDF.
---

# Segurança da Cadeia de Suprimentos de Software (Supply Chain Security)

Esta skill estabelece diretrizes para auditar, proteger e verificar a integridade de todo o ciclo de vida do software, firmware e dependências de terceiros, baseando-se no livro **Software Supply Chain Security: Securing the End-to-End Supply Chain for Software, Firmware, and Hardware** de Cassie Crossley.

---

## 🛡️ 1. Pilares da Cadeia de Suprimentos Segura

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Fonte e Código Upstream (Repositórios, Dependências, IDE)│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 2. Pipeline de Build & CI/CD (Hermetic Builds, Runners, SLSA)│
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 3. Pacotes & Artefatos (SBOM, Assinatura Sigstore/Cosign)   │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 4. Runtime & Implantação (Admission Controllers, Firmware)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 2. Padrões de Software Bill of Materials (SBOM)

### Formatos Oficiais
- **CycloneDX (OWASP)**: Focado em segurança de aplicações, inventário de vulnerabilidades (VEX), dependências, serviços e formulários regulatórios.
- **SPDX (Linux Foundation / ISO/IEC 5962:2021)**: Focado em conformidade de licenças de código aberto e proveniência de arquivos.

### Campos Obrigatórios em um SBOM Válido (NTIA Minimum Elements)
1. **Nome do Fornecedor / Autor (Supplier Name)**.
2. **Nome do Componente (Component Name)**.
3. **Versão do Componente (Component Version)**.
4. **Identificadores Únicos**: Package URL (purl) e Common Platform Enumeration (CPE).
5. **Relação de Dependência (Dependency Relationship)**: Direta vs Transitiva.
6. **Autor do SBOM (Author of SBOM Data)**.
7. **Timestamp de Geração**.

---

## 🔒 3. Proveniência e Framework SLSA (Supply-chain Levels for Software Artifacts)

| Nível SLSA | Requisitos Chave | Benefício |
| :--- | :--- | :--- |
| **SLSA 1** | Processo de build automatizado; geração de proveniência básica. | Visibilidade de como o binário foi construído. |
| **SLSA 2** | Build executado em serviço de CI/CD gerenciado com controle de versão; proveniência assinada pelo serviço de build. | Impede modificações no artefato pós-build. |
| **SLSA 3** | Plataforma de build isolada e efêmera; proveniência não falsificável e rastreabilidade total do código-fonte. | Proteção contra adulteração de pipelines de build e runners comprometidos. |

---

## ✍️ 4. Assinatura e Verificação de Imagens e Artefatos (Sigstore / Cosign)

### Fluxo de Assinatura sem Chaves (Keyless Signing com OIDC)
1. O pipeline de CI/CD (GitHub Actions / GitLab CI) autentica-se com um provedor OIDC (Sigstore Fulcio).
2. Fulcio emite um certificado X.509 de curta duração (10 minutos) atrelado à identidade do repositório/workflow.
3. O binário/imagem é assinado pelo Cosign.
4. A assinatura e a transparência são registradas no log público imutável **Rekor**.
5. No cluster Kubernetes, um Admission Controller (ex: Kyverno ou Policy Controller) valida a assinatura e rejeita qualquer imagem não assinada antes da execução do Pod.

---

## 📋 5. Checklist de Verificação da Cadeia de Suprimentos

- [ ] **1. Dependências de Terceiros**:
  - Scanning diário de CVEs via [`skills/security/appsec/sca-dependency-analysis/SKILL.md`](../sca-dependency-analysis/SKILL.md).
  - Bloqueio de *Dependency Confusion* e *Typosquatting* via registries privados e scoping de pacotes.
- [ ] **2. Segredos e Pipelines de CI/CD**:
  - Proibir segredos em texto plano; utilizar OIDC para autenticação com provedores de nuvem (AWS/GCP/Azure).
  - Runners efêmeros e isolados para builds sensíveis.
- [ ] **3. Geração Automática de SBOM**:
  - Emissão de SBOM CycloneDX/SPDX em toda release em formato `.json` assinado.
- [ ] **4. Firmware e Hardware**:
  - Verificação de Secure Boot, validação de hashes de firmware e conformidade com especificações de hardware seguro.
