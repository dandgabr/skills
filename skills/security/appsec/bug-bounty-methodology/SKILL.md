---
name: bug-bounty-methodology
description: Especialista em Metodologias de Bug Bounty e Caça a Vulnerabilidades em Larga Escala baseado na obra Bug Bounty Bootcamp (Vickie Li). Cobre reconhecimento ativo/passivo de subdomínios, descoberta de ativos ocultos, port scanning distribuído, automação de fuzzing de parâmetros, exploração de falhas lógicas e estruturação de relatórios de impacto profissional (PoC, CVSS v3.1/v4.0, remediação).
---

# Metodologias e Padrões de Bug Bounty

Esta skill estabelece os procedimentos formais para reconhecimento automatizado, mapeamento de superfície de ataque, identificação de vulnerabilidades de alto impacto e submissão responsável de relatórios em programas de **Bug Bounty** (HackerOne, Bugcrowd, Intigriti), com base no livro **Bug Bounty Bootcamp** de Vickie Li.

---

## 🎯 1. Fluxo Metodológico do Bug Bounty

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Reconhecimento Amplo (Subdomínios, ASN, WHOIS, CIDR)     │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 2. Probing e Descoberta de Serviços (HTTP/S, Portas, Tecn.) │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 3. Mapeamento de Conteúdo e Endpoints (JS Mining, Wayback)  │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 4. Testes de Vulnerabilidades Lógicas e de Negócio          │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ 5. Elaboração de Relatório de Alto Impacto (Triagem & PoC)  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 2. Reconhecimento Avançado e Descoberta de Superfície

### A. Enumeração de Subdomínios (Horizontal & Vertical)
- **Passivo**: Certificate Transparency (crt.sh), VirusTotal, Shodan, Censys, AlienVault OTX, SecurityTrails.
- **Ativo / Brute-force**: Wordlists contextualizadas com resolvers rápidos e verificação de Wildcard DNS.
- **Permutações**: Resolução de variações comuns (`api-`, `dev-`, `staging-`, `-internal`).

### B. JavaScript Mining e Extração de Endpoints
- Download e análise estática de todos os bundles JS da aplicação.
- Regex para extração de rotas não documentadas, chaves de API expostas, segredos de staging e endpoints de microsserviços.

---

## 💥 3. Vulnerabilidades Críticas de Maior Recompensa

| Vulnerabilidade | Vetor Principal | Abordagem de Teste |
| :--- | :--- | :--- |
| **IDOR / BOLA** | `/api/v1/documents/{docId}` | Criação de duas contas de usuários (A e B). Troca de tokens/IDs para verificar se usuário B lê/altera recursos de A. |
| **Race Conditions** | Cupons, resgates, transferências | Disparo simultâneo de requisições HTTP em paralelo usando HTTP/2 Single-Packet Attack para induzir condições de corrida antes do lock de banco. |
| **SSRF (Server-Side Request Forgery)** | Webhooks, importação de imagens/PDFs | Injeção de URLs de loopback (`127.0.0.1`, `169.254.169.254` para metadados de Cloud AWS/GCP/Azure) ou servidores controlados (Collaborator/Interactsh). |
| **Bypass de Lógica de Negócio** | Checkout, fluxos multi-etapas | Pular etapas no fluxo de pagamento, manipular parâmetros de preço em requisições, alterar campos de permissão em `PATCH`. |
| **Subdomain Takeover** | CNAMEs apontando para serviços desativados | Verificação de registros DNS apontando para buckets S3, GitHub Pages, Heroku ou Azure App Services não registrados. |

---

## 📝 4. Padrão de Relatório Profissional de Vulnerabilidade (HackerOne / Bugcrowd)

Para maximizar a pontuação na triagem e evitar disputas de severidade:

1. **Título Descritivo**: `[Vulnerabilidade] em [Componente/Endpoint] permite [Impacto de Negócio]`  
   *(Ex: "IDOR em /api/v1/invoices permite a qualquer usuário autenticado baixar notas fiscais de outras empresas")*
2. **Severidade & Vetor CVSS**: Cálculo transparente baseado em CVSS v3.1 / v4.0.
3. **Resumo do Impacto**: Explicação em termos executivos do risco financeiro, reputacional ou regulatório (LGPD/GDPR).
4. **Passo a Passo de Reprodução (Step-by-Step PoC)**:
   - Requisições HTTP completas (cURL ou raw HTTP).
   - Dados de duas contas de teste distintas.
5. **Prova de Conceito (Evidência)**: Prints, logs ou gravação de tela com impacto restrito (sem explorar massivamente outros usuários).
6. **Recomendação de Remediação**: Código ou configuração sugerida para resolver a causa raiz.
