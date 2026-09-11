---
name: program-ai-memory-learning-maintenance
description: Especialista na manutenção, consolidação e curadoria da base de conhecimento do ai-memory, cobrindo consolidação de observações em wiki, auto-aprimoramento de sessões, auditoria (linting), expurgo de páginas frias e processamento de feedback.
metadata:
  type: management
  phase: maintenance
  tools:
    - ai-memory
---

<!-- ai-memory-managed: routing-skill -->

# ai-memory Learning, Consolidation & Knowledge Maintenance

Esta skill orienta os procedimentos de governança, consolidação e limpeza da base de conhecimento do [ai-memory](https://github.com/akitaonrails/ai-memory). Permite transformar observações brutas de sessões anteriores em conhecimento estruturado, identificar contradições e eliminar dados obsoletos.

---

## 🧰 Ferramentas deste Cluster

- `memory_consolidate`: Compila observações brutas de uma sessão concluída em páginas temáticas de wiki sob demanda.
- `memory_auto_improve`: Revisa sessões recentes em busca de lições aprendidas e propostas de regras duráveis para o projeto.
- `memory_lint`: Audita a base de conhecimento do projeto em busca de contradições, regras defasadas e páginas marcadas via feedback.
- `memory_forget_sweep`: Realiza limpeza de páginas com TTL expirado e decaimento de páginas episódicas não fixadas (*dry-run* suportado).
- `memory_feedback`: Registra sinalização de páginas úteis (`helpful`), inúteis (`not_helpful`), defasadas (`stale`) ou erradas (`wrong`).

---

## 🧹 Práticas de Manutenção e Curadoria

1. **Tratamento de Páginas Sinalizadas (`feedback_flagged`)**:
   - Páginas que receberam sinalização de `stale` ou `wrong` aparecem destacadas no relatório de `memory_lint`. Priorize atualizar o conteúdo da página para restaurar sua precisão técnica; atualizar o documento limpa a flag automaticamente.
2. **Auto-Aprimoramento e Aprendizado Contínuo**:
   - Ao final de tarefas complexas ou ciclos de desenvolvimento, acione `memory_auto_improve` para extrair lições duráveis aprendidas durante a execução.
3. **Segurança e Prévia (Dry-Run)**:
   - Para operações de expurgo com `memory_forget_sweep`, execute sempre primeiro com simulação (*dry run*) para inspecionar o que seria afetado antes de confirmar a exclusão.
