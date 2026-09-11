# 🛠️ Time de Desenvolvimento (Workflow por Fases)

Este diretório empacota o fluxo canônico de **desenvolvimento por fases** do
`time_desenvolvimento`, replicável em **OpenCode** e **Google Antigravity**.

## 🎯 O que resolve
Centraliza — de forma declarativa e portável — **quem** analisa, revisa, implementa,
testa, protege e documenta cada fase de desenvolvimento, garantindo que nenhuma etapa do
fluxo seja pulada e que a qualidade/segurança sejam verificadas continuamente.

## 📦 Arquivos

| Arquivo | Papel | Usado por |
| :--- | :--- | :--- |
| [`HARNESS.md`](HARNESS.md) | Documentação canônica do fluxo | Todos |
| [`time-desenvolvimento.prompt.md`](time-desenvolvimento.prompt.md) | Persona supervisor do time | OpenCode + Antigravity |
| [`opencode.jsonc.example`](opencode.jsonc.example) | Config OpenCode (agente supervisor + permissões) | OpenCode |
| [`antigravity.hooks.example.json`](antigravity.hooks.example.json) | Hooks/agentes p/ Google Antigravity | Google Antigravity |

## 🧭 Fluxo (resumo)

```text
project-reviewer (plano)
  → software-architect + security-specialist (revisão)
  → [backend] backend-developer | [frontend] frontend-developer | [UI] ui-ux-designer
  → [repo] vcs-repository-specialist | [github] github-specialist | [db] dba-specialist
  → QA sempre (qa-testing-specialist)
  → dev executa a fase (backend/frontend)
  → QA gera/valida testes em paralelo
  → security-specialist + code-optimizer revisam; dev corrige
  → project-reviewer gera relatório final
  → ai-memory-specialist documenta; documenter atualiza docs
```

## 🧰 Instalação — Google Antigravity

1. Copie `antigravity.hooks.example.json` como base para o bloco `time-desenvolvimento`
   do seu `~/.gemini/config/hooks.json`. Troque `/path/to/time-desenvolvimento/hook.sh`
   pelo caminho real (ou use o hook do `orchestrator-governor`) e `{env:...}` pelos valores
   do ambiente.
2. Registre o prompt `time-desenvolvimento.prompt.md` como instrução/persona do agente.
3. (Opcional) Defina `ORCH_MAX_CONCURRENT` para ajustar o teto de paralelismo.

## 🧰 Instalação — OpenCode

1. Copie `opencode.jsonc.example` → `opencode.jsonc` no seu projeto, ou mescle o bloco
   `agent`/`instructions`/`permission` no seu `~/.config/opencode/opencode.json`.
2. Garanta que o agente supervisor esteja disponível e as permissões de `task` /
   `orchestrator_governor*` concedidas.
3. Referencie `time-desenvolvimento.prompt.md` em `instructions`.

## 🔗 Integrações transversais
- **Orquestração**: governada pelo [`multi-agent-orchestrator`](../../agents/core-orchestration/multi-agent-orchestrator/AGENT.md) e pelo governor em [`../orchestrator/`](../orchestrator/README.md).
- **Documentação**: `ai-memory-specialist` + `documenter`.
- **Banco de dados**: `dba-specialist`.

## 🧪 Validação
```bash
bash -n hook.sh                                  # se um hook local for criado
python -m json.tool opencode.jsonc.example
python -m json.tool antigravity.hooks.example.json
bash ../../scripts/validate_harness.py
```

## 🔐 Segurança
- **Nenhum segredo** é armazenado; use placeholders `/path/to/...`, `{env:VAR}`.
- Use **caminhos relativos** e env vars, nunca caminhos absolutos de máquina.
