---
name: "harness-configuration-template"
description: "Template universal de um bloco de configuração de harness (OpenCode, Claude Code, Antigravity, Cursor) para registro neste repositório."
type: "harness"
harness: "generic"
---

# Template de Configuração de Harness

Especificação canônica de um bloco de configuração de harness para os consumidores deste
repositório. Cada pasta de harness contém um `HARNESS.md` canônico + arquivos `.example`
no formato nativo do harness.

## 🎯 Propósito
Centralizar, documentar e distribuir as configurações reais de cada harness
(`opencode.jsonc`, `.mcp.json`, `mcp_config.json`, etc.) de forma portável e sem segredos.

## 🛠️ Instruções de Utilização

1. **Cópia do template**: duplique esta pasta (`harness/<nome-harness>/`).
2. **Preencha o frontmatter** com `name` (minúsculas, hifenizado), `description` em
   terceira pessoa e `harness` (identificador do harness).
3. **Crie os arquivos `.example`** no formato nativo do harness, SEMPRE sem segredos,
   usando `{env:VAR}` / `${VAR}` para valores sensíveis.
4. **Registre** a entrada no catálogo `CATALOGO.md`, no `README.md` e no discovery
   `.agents/harness.json`.
5. **Valide** com `python scripts/validate_harness.py` (quando aplicável).

## 📚 Estrutura Interna
- [HARNESS.md](HARNESS.md): Este arquivo canônico de especificação e metadados.
- `*.example`: Arquivos de configuração reais com valores interpolados (nunca tokens).
- `*.schema.json`: Schemas locais de validação quando útil.

---

## 🔃 Regras de Configuração por Harness

| Harness / Consumidor | Arquivo de config | Formato de transporte MCP | Observação |
| :--- | :--- | :--- | :--- |
| OpenCode | `opencode.json` / `opencode.jsonc` | `command[]` (local) ou `url` (remote), campo `type` | `type` é obrigatório |
| Claude Desktop / Claude Code | `.mcp.json` / `.claude.json` | `command: string` ou `url` | chave `mcpServers` |
| Google Antigravity | `mcp_config.json` | `command: string` ou `serverUrl` | chave `mcpServers` |
| Cursor / Cline / Z.ai | `.mcp.json` | `command`/`url` | chave `mcpServers` |

---

## 🔐 Segurança (obrigatório)
- **NUNCA** armazene segredos/tokens em nenhum arquivo rastreado. Use `{env:VAR}` / `${VAR}`.
- Use **caminhos relativos** à raiz do repositório; nunca caminhos absolutos de máquina
  (ex.: prefixos de home de usuário ou til) — regra do `AGENTS.md`.
- Documente as variáveis de ambiente esperadas em `harness/shared/env.example`.
