---
name: "harness-claude-code"
description: "Configuração de referência para Claude Code / Claude Desktop, cobrindo mcpServers e boas práticas de .mcp.json."
type: "harness"
harness: "claude-code"
---

# Configurações — Claude Code / Claude Desktop

## 🎯 Propósito
Documenta e distribui a configuração para **Claude Code** e **Claude Desktop**
(`.mcp.json`, `.claude.json`).

## 🛠️ Arquivos
- [.mcp.json.example](.mcp.json.example): Exemplo de config sem segredos.

## 🔧 Uso
1. Copie `.mcp.json.example` → `.mcp.json` no diretório do projeto.
2. Use variáveis `{env:VAR}`; nunca versionar tokens.
3. O formato exige a chave `mcpServers` com `command: string` e `args: []`.

## 🔑 Segurança
- `.mcp.json` reais NÃO devem ser commitados (reforço no `.gitignore`). Apenas o
  sufixo `.example` é rastreado.
