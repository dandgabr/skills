# 🎛️ Governança do Orquestrador Multi-Agente

Este diretório empacota a lógica de **concorrência real + rate-limit governance** que faz o
[`multi-agent-orchestrator`](../../agents/core-orchestration/multi-agent-orchestrator/AGENT.md)
funcionar de forma confiável, replicável em qualquer harness/PC.

## 🎯 O que resolve
Sem governança, disparar múltiplos subagentes satura a cota da API e gera erros **429/Too
Many Requests**. Esta implementação mantém um **ledger de slots em disco** com `flock()`,
garantindo que orquestrador + subagentes nunca ultrapassem o limite de paralelismo
(por padrão `5` contando o orquestrador).

## 📦 Arquivos

| Arquivo | Papel | Usado por |
| :--- | :--- | :--- |
| [`governor.sh`](governor.sh) | Ledger de slots com `flock()` (core, autônomo) | OpenCode + Antigravity |
| [`hook.sh`](hook.sh) | Hook de lifecycle que bridgea para o governor | Google Antigravity |
| [`gate.ts`](gate.ts) | Plugin que engancha o `task` tool | OpenCode |
| [`antigravity.hooks.example.json`](antigravity.hooks.example.json) | Template de `hooks.json` (sem segredos) | Google Antigravity |
| [`opencode.jsonc.example`](opencode.jsonc.example) | Config mínima OpenCode para o governor | OpenCode |

> Os scripts são idênticos aos canônicos em `scripts/`, porém **parametrizados e sem
> caminhos absolutos de máquina** (prefixos de home de usuário ou til nos paths), tornando-os
> portáveis entre PCs e harnesses. A resolução de paths é relativa ao próprio script ou via
> env vars.

---

## 🧰 Instalação — Google Antigravity

1. Copie `governor.sh` e `hook.sh` para um destino estável (ex.: `~/.config/ai-orchestrator/`):
   ```bash
   mkdir -p ~/.config/ai-orchestrator
   cp governor.sh hook.sh ~/.config/ai-orchestrator/
   chmod +x ~/.config/ai-orchestrator/governor.sh ~/.config/ai-orchestrator/hook.sh
   ```
2. Use [`antigravity.hooks.example.json`](antigravity.hooks.example.json) como base para o
   bloco `orchestrator-governor` do seu `~/.gemini/config/hooks.json`. Troque
   `/path/to/hook.sh` pelo caminho real e `{env:...}` pelos valores do ambiente do seu PC.
3. (Opcional) Defina `ORCH_MAX_CONCURRENT` no ambiente para ajustar o teto de paralelismo.

## 🧰 Instalação — OpenCode

1. Copie `gate.ts` e `governor.sh`:
   ```bash
   mkdir -p ~/.config/opencode/plugins ~/.config/ai-orchestrator
   cp gate.ts ~/.config/opencode/plugins/orchestrator-gate.ts
   cp governor.sh ~/.config/ai-orchestrator/
   chmod +x ~/.config/ai-orchestrator/governor.sh
   ```
2. O plugin é auto-descoberto de `~/.config/opencode/plugins/*.ts`. Reinicie o OpenCode.
3. Garanta as permissões do `orchestrator_governor` (veja
   [`opencode.jsonc.example`](opencode.jsonc.example)) e defina `ORCH_GOVERNOR` apontando
   para o `governor.sh` se ele não estiver no caminho padrão.

---

## ⚙️ Variáveis de ambiente
| Variável | Default | Descrição |
| :--- | :--- | :--- |
| `ORCH_MAX_CONCURRENT` | `5` | Teto de paralelismo (contando o orquestrador) |
| `ORCH_GOVERNOR` | auto-resolvido | Caminho para o `governor.sh` |
| `GOVERNOR_STATE_DIR` | `$XDG_RUNTIME_DIR`/`/tmp` | Diretório do ledger de slots |

## 🧪 Validação
```bash
bash -n governor.sh hook.sh
bash ../../scripts/orchestrator-governor.test.sh   # suíte de validação do ledger
bash ../../scripts/orchestrator-governor.check.sh  # health check (wiring + runtime)
```

## 🔐 Segurança
- **Nenhum segredo** é armazenado nestes arquivos. Tokens/serviços (`ai-memory.internal`,
  credenciais) são apenas placeholders (`/path/to/...`, `{env:VAR}`) a preencher por PC.
- Use **caminhos relativos** e env vars de ambiente, nunca caminhos absolutos de máquina.
