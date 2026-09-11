---
name: "harness-time-desenvolvimento"
description: "Fluxo canônico de desenvolvimento por fases (time de desenvolvimento): planejamento, revisão, implementação, QA e documentação. Replicável em OpenCode e Google Antigravity."
type: "harness"
harness: "all"
---

# Configurações — Time de Desenvolvimento (Workflow por Fases)

## 🎯 Propósito
Empacota e distribui o fluxo padronizado de **desenvolvimento por fases** do
`time_desenvolvimento`. Define, de forma declarativa e portável, quem analisa, revisa,
implementa, testa e documenta cada fase, replicável em **OpenCode** e **Google
Antigravity** sem segredos e sem caminhos absolutos de máquina.

Este harness traduz a política global `_rules/development-workflow-policy.md`
(disponível no ai-memory, escopo global) em artefatos executáveis por harness.

## 🧭 Fluxo Canônico (Regras do `time_desenvolvimento`)

1. **Análise e Plano** — `project-reviewer` analisa a demanda e cria o plano de fases.
2. **Revisão do Plano** — `software-architect` + `security-specialist` revisam o plano.
   - Envolve backend? → `backend-developer` revisa.
   - Envolve frontend? → `frontend-developer` revisa.
   - Envolve interface? → `ui-ux-designer` revisa.
   - Envolve repositório? → `vcs-repository-specialist`; versionamento GitHub → `github-specialist`.
3. **QA sempre envolvido** — `qa-testing-specialist` participa de todo o planejamento.
3. **Quarentena por Fases** — todo plano é separado em **fases**; cada fase é planejada
   individualmente com dev (back e/ou front), `security-specialist` e `qa-testing-specialist`.
4. **Implementação** — o agente de desenvolvimento respectivo (`backend-developer` ou
   `frontend-developer`) executa a fase.
5. **QA em paralelo** — enquanto o dev implementa, `qa-testing-specialist` gera e valida
   os testes contra o que foi entregue (testes gerados durante o dev, nunca depois).
6. **Banco de dados** — qualquer fase que envolva banco de dados invoca `dba-specialist`.
7. **Revisão pós-implementação** — `security-specialist` + `code-optimizer` revisam a
   entrega; os problemas encontrados são corrigidos automaticamente pelos agentes de
   desenvolvimento.
8. **Conclusão da Fase** — fase encerrada → `project-reviewer` gera o relatório final.
9. **Documentação no ai-memory** — cada fase é documentada no ai-memory por
   `ai-memory-specialist`; ao validar a passagem para a próxima fase, `documenter` atualiza
   toda a documentação gerada.

> A orquestração de todos os agentes acima é supervisionada pelo
> [`multi-agent-orchestrator`](../../agents/core-orchestration/multi-agent-orchestrator/AGENT.md).

## 🛠️ Arquivos
- [time-desenvolvimento.prompt.md](time-desenvolvimento.prompt.md): Prompt canônico
  multiharness (persona do supervisor do time de desenvolvimento).
- [opencode.jsonc.example](opencode.jsonc.example): Config para OpenCode (agentes,
  permissões e instruções do fluxo).
- [antigravity.hooks.example.json](antigravity.hooks.example.json): Hooks e agentes para
  Google Antigravity.
- [README.md](README.md): Passo a passo de instalação por harness.

## 🧰 Harnesses atendidos
- **OpenCode** (via `opencode.jsonc.example` + instruções).
- **Google Antigravity / ADK 2.0** (via `antigravity.hooks.example.json` + agents).
- Qualquer harness que expõe hooks de lifecycle / agentes.

## 🔐 Segurança
- **Nenhum segredo é armazenado**; use placeholders `/path/to/...` e `{env:VAR}`.
- Use **caminhos relativos** e variáveis de ambiente, nunca caminhos absolutos de máquina.
- Siga as regras de `model` do `AGENTS.md`: **omitir** `model` em manifestos por padrão.
