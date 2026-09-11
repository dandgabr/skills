---
name: "harness-opencode"
description: "Configuração de referência para o harness OpenCode, cobrindo MCPs, permissões, agentes e boas práticas."
type: "harness"
harness: "opencode"
---

# Configurações — OpenCode

## 🎯 Propósito
Documenta e distribui a configuração para o harness **OpenCode** (`opencode.json` /
`opencode.jsonc`).

## 🛠️ Arquivos
- [opencode.jsonc.example](opencode.jsonc.example): Exemplo de config sem segredos.

## 🔧 Uso
1. Copie `opencode.jsonc.example` → `opencode.jsonc` no diretório do projeto.
2. Substitua valores `{env:VAR}` pelas variáveis reais (nunca commitar tokens).
3. Registre a config resultante APENAS via bloco `mcp` no seu `opencode.json`. Nunca
   versionar config com segredos.

## 🧭 Schema
Consulte [`../_template/opencode.schema.json`](../_template/opencode.schema.json).
