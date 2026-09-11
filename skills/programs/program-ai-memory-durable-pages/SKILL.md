---
name: program-ai-memory-durable-pages
description: Especialista em mutações deliberadas e escrita de páginas duráveis na wiki do ai-memory, cobrindo anotações permanentes, decisões arquiteturais (ADR), regras de escopo global e remoção precisa de páginas obsoletas.
metadata:
  type: management
  phase: implementation
  tools:
    - ai-memory
---

<!-- ai-memory-managed: routing-skill -->

# ai-memory Durable Pages & Wiki Management

Esta skill orienta a gravação deliberada e estruturada de conhecimento perene na wiki do [ai-memory](https://github.com/akitaonrails/ai-memory). Gravações deliberadas devem ser utilizadas para armazenar lições aprendidas, regras definitivas e ADRs, diferenciando-se das capturas automáticas de logs e ferramentas feitas pelos hooks.

---

## 🧰 Ferramentas deste Cluster

- `memory_write_page`: Cria ou atualiza uma página durável na wiki do projeto ou no escopo global.
- `memory_delete_page`: Remove páginas obsoletas ou revogadas através do caminho relativo exato.

---

## 📝 Convenções de Escrita e Títulos

1. **Convenção de Título H1**:
   - Inicie o corpo do documento (`body`) com o título em `# Título da Página` na primeira linha. O `ai-memory` infere o título automaticamente a partir desse cabeçalho, evitando problemas de escape de caracteres na chamada de ferramentas.
2. **Caminhos Canônicos Recomendados**:
   - `notes/<topico>.md`: Anotações gerais de engenharia e contexto de negócio.
   - `decisions/<topico>.md`: Decisões arquiteturais com estrutura ADR.
   - `concepts/<topico>.md`: Modelos de domínio, entidades e arquitetura conceitual.
   - `_rules/<topico>.md`: Diretrizes e políticas de projeto.
3. **Páginas Temporárias com TTL (`expires_at`)**:
   - Se uma informação tiver validade limitada (ex.: migração temporária, credencial de teste ou sprint pontual), defina `expires_at` (RFC3339 ou formato `YYYY-MM-DD`). A página será ocultada após a data e limpa no próximo ciclo de esquecimento (*forget sweep*).

---

## 🏛️ Registro de Decisões de Arquitetura (ADR)

Para registrar decisões técnicas com durabilidade garantida, utilize `path: "decisions/<slug>.md"`, marque `pinned: true` e utilize a estrutura canônica:

```markdown
# [Título da Decisão]

**Status:** accepted <!-- proposed | accepted | superseded by [[decisions/outro]] -->

## Contexto
Qual problema forçou a tomada de decisão e quais restrições eram relevantes.

## Decisão
O que foi decidido, declarado de forma afirmativa e objetiva.

## Consequências
Vantagens obtidas, desvantagens assumidas e alternativas rejeitadas (com justificativa para evitar retrabalho futuro).
```

---

## 🌐 Preferências e Regras Globais (`scope: "global"`)

Quando um padrão técnico for transversal e aplicável a **todos os projetos** da máquina (ex.: convenções de commits, preferência por ferramentas ou regras de segurança da máquina):
- Chame `memory_write_page` com o parâmetro `scope: "global"`.
- O conteúdo é armazenado no escopo reservado `_global` e retornado automaticamente em consultas em qualquer subprojeto como `global_scope_hits`.
