---
name: "harness-orchestrator-governor"
description: "Configuração e distribuição da governança multi-agente (concorrência + rate-limit) para OpenCode, Antigravity e outros harnesses."
type: "harness"
harness: "all"
---

# Configurações — Orquestrador Multi-Agente

## 🎯 Propósito
Empacota e distribui a governança de concorrência e rate-limit do multi-agent-orchestrator,
replicável em qualquer harness/PC, sem segredos e sem caminhos absolutos de máquina.

## 🛠️ Arquivos
- [governor.sh](governor.sh): Ledger de slots com `flock()` — core compartilhado.
- [hook.sh](hook.sh): Hook de lifecycle para Google Antigravity.
- [gate.ts](gate.ts): Plugin para OpenCode.
- [antigravity.hooks.example.json](antigravity.hooks.example.json): Template de `hooks.json`.
- [opencode.jsonc.example](opencode.jsonc.example): Config mínima para OpenCode.
- [README.md](README.md): Passo a passo de instalação por harness.

## 🧰 Harnesses atendidos
- OpenCode (via plugin `gate.ts`)
- Google Antigravity (via `hook.sh` + `hooks.json`)
- Qualquer harness que exponha hooks de lifecycle (padrão `invoke_subagent`/`task`)

## 🔐 Segurança
- Nenhum segredo é armazenado; use placeholders `/path/to/...` e `{env:VAR}`.
- Use caminhos relativos e variáveis de ambiente, nunca caminhos absolutos de máquina.
