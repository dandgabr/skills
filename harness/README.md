# 🧰 Configurações de Harness

Este diretório centraliza, documenta e distribui as **configurações por harness**
(OpenCode, Claude Code/Desktop, Google Antigravity, Cursor, Cline, Z.ai). Cada harness tem
um `HARNESS.md` canônico + arquivos `.example` (SEM segredos) no formato nativo.

## 🤖 Harnesses Suportados

| Harness | Arquivo de config | Status |
| :--- | :--- | :--- |
| [**OpenCode**](opencode/HARNESS.md) | `opencode.jsonc.example` | ✅ Estrutura pronta |
| [**Claude Code / Desktop**](claude-code/HARNESS.md) | `.mcp.json.example` | ✅ Estrutura pronta |
| [**Google Antigravity**](antigravity/HARNESS.md) | `mcp_config.json.example` | ✅ Estrutura pronta |
| [**Cursor / Cline / Z.ai**](cursor/HARNESS.md) | `.mcp.json.example` | ✅ Estrutura pronta |
| [**Orquestrador Multi-Agente**](orchestrator/HARNESS.md) | `governor.sh` + `hook.sh` + `gate.ts` | ✅ Governança + rate-limit |

## 📁 Estrutura

```text
harness/
├── README.md                  # Este guia
├── _template/                 # Template universal (HARNESS.md, schemas, templates)
├── opencode/                  # opencode.jsonc.example + HARNESS.md
├── claude-code/               # .mcp.json.example + HARNESS.md
├── antigravity/               # mcp_config.json.example + HARNESS.md
├── cursor/                    # .mcp.json.example + HARNESS.md
├── orchestrator/              # Governança multi-agente (governor.sh, hook.sh, gate.ts)
└── shared/                    # env.example, skills.json.example, plugins.json.example
```

## 🔐 Segurança
- **NUNCA** commitar config real com segredos — apenas arquivos `.example`/`.template`.
- Use interpolação `{env:VAR}` / `${VAR}` para valores sensíveis.
- Use caminhos relativos à raiz do repositório (regra do `AGENTS.md`).
