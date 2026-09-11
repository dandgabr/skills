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

---

## ⛓️ 5. Governança de Concorrência e Prevenção de Rate-Limit

O supervisor é responsável por proteger a sessão contra estouro de quota dos provedores (`429 Too Many Requests`, `RPM/TPM exceeded`, `tokens per minute`). Para isso, mantém a concorrência sob controle:

### 5.1 Ledger de Subagentes

Mantenha um registro vivo com o estado de cada subagente:

| Estado | Significado |
| :--- | :--- |
| `ACTIVE` | Em execução em paralelo neste momento. |
| `QUEUED` | Delegado, mas aguardando um slot de concorrência abrir. |
| `DONE` | Concluiu com sucesso. |
| `FAILED` | Falhou sem sintoma de rate-limit (lógica, loop, drift). |
| `PAUSED` | Falhou por rate-limit; aguarda relançamento quando houver folga. |

### 5.2 Teto de Paralelismo (Concurrency Cap)

- **Regra central**: nunca deixe mais de **5 agentes ativos** simultaneamente **contando com o próprio supervisor** (ou seja, supervisor + no máximo **4 subagentes** em `ACTIVE`).
- Para delegar, calcule `ativos = 1 (você) + nº de subagentes ACTIVE`. Enquanto `ativos >= 5`, **não** dispare novos subagentes: mova a tarefa para `QUEUED` e aguarde um sinal de `DONE`/`FAILED`/`PAUSED` para liberar o próximo da fila (FIFO).

### 5.3 Falha por Rate-Limit → Kill, Espera e Relaçamento

Sintomas de rate-limit: `429`, `HTTP 429`, `Too Many Requests`, `Rate limit`, `Quota exceeded`, `RPM exceeded`, `TPM exceeded`, `tokens per minute exceeded` (em mensagens de erro, cabeçalhos de resposta ou status de ferramenta).

Ao detectar um desses sintomas num subagente ativo:
1. **Kill** a instância imediatamente (kill-switch) e marque-a como `PAUSED`, **preservando** a descrição da subtarefa e seu `@CTX` para retry.
2. **Espere** enquanto o total ativo (você + demais ACTIVE) permanecer em 5; não relance ainda.
3. Quando o total ativo cair **abaixo de 5**, **relance** a tarefa pausada (nova instância zerada) aplicando *backoff exponencial* entre tentativas: ≈2s na 1ª, 4s, 8s, 16s, 32s, até um teto de 60s. Zerar o estado da tarefa para `ACTIVE` ao relançar.
4. Esgotado um limite razoável de tentativas consecutivas (ex.: 5), reportar o `FAILED` definitivo ao usuário e continuar o restante da fila.

### 5.4 Escopo do Retry

- **Somente** falhas com sintoma de rate-limit entram no fluxo de `PAUSED`/retry.
- Qualquer outra falha (drift, loop, erro de lógica) segue o protocolo padrão de **Nível 1/2/3 da seção 3**, sendo tratada como `FAILED` sem relaçamento automático.

---

## 📐 6. Exemplo de Decisão de Escalonamento

Dada uma fila de 6 subtarefas independentes e o teto de 5:

1. Você + 4 subagentes iniciados = 5 ativos. As 2 restantes ficam `QUEUED`.
2. Um dos subagentes ativos cai com `429`. Você o mata → `PAUSED`. Ativos = 4.
3. Libera a próxima `QUEUED` como `ACTIVE` (ativos = 5) **e** relança a `PAUSED` (ativos = 6? **não**: aplica nova espera até ativos < 5).

> **Ajuste do teto**: o valor 5 é o default (`MAX_CONCURRENT = 5`, contando com o orquestrador). Se o provedor em uso tiver limite menor (ex.: 3 RPM), reduza o teto proporcionalmente. O teto pode ser parametrizado via variável de ambiente `ORCH_MAX_CONCURRENT` quando o harness permitir.
