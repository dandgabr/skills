---
name: multi-agent-orchestration-supervision
description: "Especialista em Orquestração, Supervisão e Governança de Sistemas Multi-Agente. Focado em ancoragem de objetivos iniciais, detecção contínua de desvio de escopo (Agent Drift e Role Drift), intervenção proativa (Self-Correction), contenção gradual e aplicação de kill-switch/terminação segura de agentes não-conformes."
---

# Multi-Agent Orchestration, Supervision & Drift Governance

Esta skill estabelece a metodologia de supervisão, coordenação e controle de qualidade operacional sobre frotas de agentes autônomos em sistemas multi-agente hierárquicos e distribuídos.

---

## 🎯 1. Princípios Fundamentais do Supervisor

1. **Ancoragem de Intenção (Intent Grounding)**:
   - Todo fluxo de trabalho começa com a extração e fixação do problema original do usuário em um contrato de intenção explícito.
   - O contrato deve conter: Objetivo Primário, Restrições Inegociáveis, Entregáveis Esperados e Critérios de Parada.
2. **Vigilância Ativa de Execução (Observation Loop)**:
   - O supervisor não executa o trabalho braçal de domínio, mas acompanha as chamadas de ferramentas, mensagens emitidas e arquivos modificados pelos subagentes.
3. **Princípio da Intervenção Mínima Eficiente**:
   - Ajustar primeiro com orientação contextual (*re-prompting*).
   - Conter em seguida (limitar permissões ou pausar execução).
   - Terminar (*kill*) apenas quando houver persistência de desvio, loop infinito ou risco operacional.

---

## 🔍 2. Taxonomia de Desvios (Agent Drift)

O supervisor deve monitorar continuamente os seguintes modos de falha:

| Categoria de Desvio | Sintoma Observável | Causa Raiz Típica | Ação Recomendada |
| :--- | :--- | :--- | :--- |
| **Role Drift** | Subagente de pesquisa tentando editar arquivos de produção; agente de frontend refatorando migrações de banco. | Alucinação de fronteira ou instrução de sistema permissiva. | Bloqueio imediato da ação e reiteração do escopo restrito do papel. |
| **Scope Drift** | Subagente expandindo a tarefa para refatorar módulos não solicitados ou criar funcionalidades não pedidas. | Otimização prematura ou perda da ancoragem de intenção. | Reprompt para abortar tarefas laterais e focar estritamente na meta. |
| **Loop / Deadlock Drift** | Subagente repetindo a mesma chamada de ferramenta com parâmetros idênticos ou alternando em ciclo sem progresso. | Falha em interpretar erros da ferramenta ou contexto poluído. | Cancelamento da operação, limpeza de contexto e fornecimento de estratégia alternativa. |
| **Hallucinated Progress** | Subagente emitindo status de conclusão sem que os arquivos físicos ou asserções tenham sido validados. | Resposta bajuladora (*sycophancy*) ou ausência de oráculo de validação. | Rejeição do status, exigência de evidência concreta de teste/execução. |

---

## 🛑 3. Protocolo de Contenção Gradual e Kill-Switch

Quando um agente demonstrar desvio, o supervisor aplica uma escala de resposta de 3 níveis:

### Nível 1: Intervenção Orientativa (Nudge & Realignment)
- **Mensagem Corretiva**: Emitir um comando de correção direta citando a intenção original.
  ```text
  [ALERTA DE DESVIO] Sua última ação divergiu do objetivo inicial.
  Objetivo Atual: <intenção-ancorada>
  Ação Incorreta: Tentativa de refatorar código fora do escopo.
  Instrução: Interrompa essa alteração e retome estritamente a tarefa delegada.
  ```

### Nível 2: Contenção de Estado e Rollback (Quarantine & Rollback)
- Reverter arquivos ou modificações incorretas geradas pelo subagente desviante.
- Limpar a memória recente contaminada ou reenviar uma síntese enxuta da tarefa.

### Nível 3: Terminação Forçada (Kill-Switch)
- Se o agente insistir no comportamento errôneo após intervenção de Nível 1:
  1. Executar a chamada de encerramento imediato (`manage_subagents: kill` ou cancelamento de tarefa).
  2. Registrar o log do desvio para auditoria pós-morte.
  3. Reatribuir a demanda a uma nova instância zerada ou assumir a condução.

---

## 📡 4. Protocolo de Comunicação TOON com Heartbeat

Na comunicação com subagentes delegados, o supervisor exige o envio de telemetria estruturada via protocolo **TOON**:

```text
@FROM: <subagente>
@TO: orchestrator
@STATUS: <OK | BLOCKED | DRIFT_DETECTED | DONE>
@CTX: <id-tarefa-ancorada>
@PROGRESS: <resumo-do-avanço-realizado>
@NEXT_ACTION: <próxima-chamada-pretendida>
```

Se um subagente não responder ao supervisor em tempo hábil ou emitir ações discrepantes do `@CTX`, o processo de terminação é acionado preventivamente.
