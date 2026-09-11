---
name: "mcp-template"
description: "Template universal de um servidor MCP (Model Context Protocol) para registro neste repositório."
type: "mcp"
---

# Template de Servidor MCP (Model Context Protocol)

Especificação canônica de um servidor MCP para os harnesses que este repositório exporta
(OpenCode, Claude Code, Google Antigravity, Cursor, Cline, LangChain, AutoGen, CrewAI etc.).

## 🎯 Propósito
Um servidor MCP expõe ferramentas, recursos e prompts externos para o agente consumidor.
Este documento define os metadados multiplataforma de um servidor registrado.

## 🛠️ Instruções de Utilização

1. **Cópia do template**: duplique esta pasta (`mcps/<categoria>/<nome-mcp>/`).
2. **Preencha o frontmatter** com `name` (minúsculas, hifenizado) e `description` em terceira pessoa.
3. **Registre** a entrada no catálogo `MCPS.md` e no discovery `.agents/mcps.json`.
4. **Mantenha sincronizados** os metadados entre os três manifestos (apenas `name` e `description` precisam ser idênticos; parâmetros de execução variam por harness).

## 📚 Estrutura Interna
- [MCP.md](MCP.md): Este arquivo canônico de especificação e metadados.
- [mcp.json](mcp.json): Manifesto estruturado para APIs REST, OpenCode e frameworks multi-agente.
- [mcp_config.json](mcp_config.json): Configuração de execução compatível com Claude Desktop / Antigravity / Cline.

---

## 🔃 Regras de Configuração por Harness

| Harness / Consumidor | Arquivo preferido | Campo de transporte | Observação |
| :--- | :--- | :--- | :--- |
| OpenCode | `opencode.json` → bloco `mcp` / `mcp.json` | `command[]` (local) ou `url` (remote) | `type` é obrigatório |
| Claude Desktop / Claude Code | `mcp_config.json` / `.mcp.json` | `command` (string) ou `url` | formato `mcpServers` |
| Google Antigravity | `mcp_config.json` (global ou plugin) | `command` (string) ou `serverUrl` | seção `mcpServers` |
| Cline / Cursor | `.mcp.json` | `command`/`url` | formato `mcpServers` |
| LangChain / AutoGen / APIs REST | `mcp.json` (estruturado) | resolvido em runtime | contrato via código consumidor |
