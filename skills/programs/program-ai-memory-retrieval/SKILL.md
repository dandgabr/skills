---
name: program-ai-memory-retrieval
description: Especialista em consultas e recuperação de memória de longo prazo no ai-memory, cobrindo buscas semânticas (FTS5 + vetor + grafo), histórico de decisões de arquitetura, gotchas, procedimentos, briefings estruturados e recuperação de observações de sessões.
metadata:
  type: management
  phase: discovery
  tools:
    - ai-memory
---

<!-- ai-memory-managed: routing-skill -->

# ai-memory Retrieval & Discovery

Esta skill orienta o processo de leitura e consulta ao sistema de memória de longo prazo [ai-memory](https://github.com/akitaonrails/ai-memory), permitindo que agentes resgatem contexto prévio, decisões arquiteturais, armadilhas técnicas (*gotchas*) e diretrizes consolidadas antes de propor mudanças no código.

---

## 🧰 Ferramentas deste Cluster

- `memory_query`: Busca na wiki do projeto atual por decisões prévias, regras, procedimentos e anotações. Combina FTS5, casamento de entidades e ranking por autoridade de fontes.
- `memory_recent`: Lista as páginas mais recentemente atualizadas para uma checagem rápida de atividades do projeto.
- `memory_read_page`: Carrega o corpo completo de uma página específica após um resultado de busca ou acesso por caminho exato.
- `memory_read_session_observations`: Lê as observações brutas capturadas por hooks em uma sessão (prompts, ferramentas, saídas).
- `memory_status`: Relata o estado de saúde, contagem de observações e tamanho da base de conhecimento.
- `memory_briefing`: Retorna um snapshot estruturado (sem chamada LLM) com métricas de 7d/30d, regras e páginas recentes.
- `memory_explore`: Gera um resumo discursivo calibrado pelo tempo de inatividade para ambientação rápida.

---

## 🎯 Escopo de Projeto e Repositório

Ao utilizar clientes estáticos ou quando não houver marcador de sessão herdado:
- Se houver um `.ai-memory.toml` na raiz do subprojeto/repositório, utilize o `workspace` e `project` declarados nele.
- Para consultas abrangentes entre múltiplos projetos da máquina, utilize `global: true` no `memory_query` (sem especificar `workspace` ou `project`).
- Páginas expiradas por TTL são excluídas por padrão; inclua `include_expired: true` apenas quando o usuário solicitar explicitamente auditoria histórica.

---

## 🔍 Diretrizes de Consulta Eficiente

1. **Antes de Propor Arquiteturas ou Refatorações**:
   - Sempre faça uma busca preliminar com `memory_query` para verificar se a decisão técnica já foi discutida ou se há um ADR registrado.
2. **Trechos de Busca vs. Conteúdo Integral**:
   - A ferramenta `memory_query` retorna *snippets* (trechos destacados). Se o título ou caminho da página for relevante (ex.: `decisions/*`, `_rules/*`, `gotchas/*`), use `memory_read_page` para ler o documento na íntegra.
3. **Avaliação Crítica de Evidências**:
   - Trate o conteúdo resgatado da memória como histórico valioso, porém sempre valide com o estado atual do repositório e com as instruções atuais do usuário.
4. **Feedback de Utilidade**:
   - Quando uma página consultada for extremamente útil ou se estiver obsoleta/incorreta, acione `memory_feedback` com os sinais `helpful`, `stale` ou `wrong` para enriquecer a curadoria contínua da memória.
