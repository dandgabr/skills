---
name: program-ai-memory-handoff
description: Especialista no ciclo de continuidade de sessões (Handoffs) com o ai-memory, cobrindo consumo de handoffs pendentes em SessionStart, criação de bastões de transição para a próxima sessão e descarte de handoffs expirados.
metadata:
  type: management
  phase: governance
  tools:
    - ai-memory
---

<!-- ai-memory-managed: routing-skill -->

# ai-memory Session Continuity & Handoffs

Esta skill orienta a passagem de bastão (*handoff*) entre sessões e agentes de IA utilizando o [ai-memory](https://github.com/akitaonrails/ai-memory). Os handoffs são transitórios e de uso único, destinados a preservar o estado mental e os próximos passos para a sessão seguinte, não devendo ser confundidos com documentação perene de wiki.

---

## 🧰 Ferramentas deste Cluster

- `memory_handoff_accept`: Consome o handoff pendente quando o usuário questiona "onde paramos?" e o bloco injetado no início da sessão não estiver visível.
- `memory_handoff_begin`: Cria um handoff conciso de transição quando a sessão está sendo encerrada ou quando o usuário pede explicitamente para salvar o contexto para a próxima execução.
- `memory_handoff_cancel`: Invalida um handoff pendente criado por engano através do seu `handoff_id` exato.

---

## 🔄 Ciclo de Vida do Handoff

1. **Injeção Automática no Início da Sessão**:
   - Os hooks de ciclo de vida (`session-start`) buscam e consomem automaticamente o handoff pendente, injetando-o no contexto inicial do modelo com a marcação `📥 ai-memory: pending handoff`.
   - Se essa mensagem já constar no contexto, responda a partir dela diretamente e **não** chame `memory_handoff_accept` novamente (pois handoffs são de uso único).
2. **Criação ao Fim da Sessão**:
   - Chame `memory_handoff_begin` apenas no encerramento da conversa ou por solicitação explícita.
   - Mantenha o sumário ultra-conciso (2 a 3 frases) e concentre os detalhes nos pontos de dúvidas abertas (*open questions*) e próximos passos (*next steps*).
3. **Compartilhamento**:
   - Por padrão, o handoff pertence ao operador que o gerou. Utilize `shared: true` apenas quando solicitado expressamente que qualquer operador do projeto possa receber a transição.
