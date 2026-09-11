---
name: "harness-cursor"
description: "Configuração de referência para Cursor / Cline / Z.ai, cobrindo mcpServers e boas práticas de .mcp.json."
type: "harness"
harness: "cursor"
---

# Configurações — Cursor / Cline / Z.ai

## 🎯 Propósito
Documenta e distribui a configuração para **Cursor**, **Cline** e **Z.ai** (`.mcp.json`).

## 🛠️ Arquivos
- [.mcp.json.example](.mcp.json.example): Exemplo de config sem segredos.

## 🔧 Uso
1. Copie `.mcp.json.example` → `.mcp.json` no diretório do projeto.
2. Formato `mcpServers` com `command: string` + `args` ou `url`. Use variáveis `{env:VAR}`.

## 🔑 Segurança
- `.mcp.json` reais NÃO devem ser commitados. Apenas o sufixo `.example` é rastreado.
