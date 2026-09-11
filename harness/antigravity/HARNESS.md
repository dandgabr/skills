---
name: "harness-antigravity"
description: "Configuração de referência para Google Antigravity (AGY), cobrindo mcpServers e customizações."
type: "harness"
harness: "antigravity"
---

# Configurações — Google Antigravity (AGY)

## 🎯 Propósito
Documenta e distribui a configuração para **Google Antigravity** (`mcp_config.json`).

## 🛠️ Arquivos
- [mcp_config.json.example](mcp_config.json.example): Exemplo de config sem segredos.

## 🔧 Uso
1. Copie `mcp_config.json.example` → `mcp_config.json` global ou de plugin.
2. O formato usa a chave `mcpServers` com `command: string` (local) ou `serverUrl`
   (remoto) e `env`.

## 🔑 Segurança
- `mcp_config.json` reais NÃO devem ser commitados. Apenas o sufixo `.example` é rastreado.
- Use o `mcp_config.json` global do ambiente (ex.: `~/.gemini/config/mcp_config.json`) como ponto de integração.
