---
name: program-ai-memory-routing-install
description: Especialista na instalação, atualização, inspeção e reparo das diretrizes e skills gerenciadas de roteamento do ai-memory em projetos e ambientes de agentes de IA.
metadata:
  type: management
  phase: operations
  tools:
    - ai-memory
---

<!-- ai-memory-managed: routing-skill -->

# ai-memory Routing & Skills Installation

Esta skill orienta a instalação e manutenção das regras de roteamento e pacotes de habilidades do [ai-memory](https://github.com/akitaonrails/ai-memory) nos ambientes e projetos locais.

---

## 🧰 Ferramentas deste Cluster

- `memory_install_self_routing`: Retorna o bloco canônico de instruções, marcadores de integridade e payloads de skills gerenciadas para clientes que não suportam escrita direta pelo servidor MCP.

---

## 📦 Marcadores de Integridade Gerenciados

Para permitir atualizações idempotentes sem corromper regras customizadas pelo desenvolvedor, o ecossistema ai-memory utiliza delimitadores estritos:

1. **Bloco de Instruções (`AGENTS.md` / `GEMINI.md`)**:
   - Início: `<!-- ai-memory:start -->`
   - Fim: `<!-- ai-memory:end -->`
   - Somente o conteúdo entre esses dois delimitadores (em linhas isoladas) é substituído durante atualizações.
2. **Habilidades Gerenciadas (`SKILL.md`)**:
   - Marcador de posse: `<!-- ai-memory-managed: routing-skill -->`
   - Somente arquivos que contenham essa marcação explícita são sobrescritos de forma segura.
