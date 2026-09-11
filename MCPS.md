# 🔌 Catálogo Central de Servidores MCP (Model Context Protocol)

Este documento consolida o inventário canônico de **Servidores MCP** disponíveis neste
repositório, no mesmo padrão multi-harness de skills e agentes.

---

## 📊 Dashboard do Repositório de MCPs

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                        ESTATÍSTICAS GERAIS — SERVIDORES MCP                          │
├────────────────────────────────────────┬─────────────────────────────────────────────┤
│ 🔌 Servidores MCP Registrados           │ 0                                            │
│ 🧩 Template Universal (multi-harness)   │ 1                                            │
└────────────────────────────────────────┴─────────────────────────────────────────────┘
```

> 📦 Novo servidor? Duplique o template em [`mcps/_template/`](mcps/_template/MCP.md) e
> registre a entrada na tabela abaixo + no discovery `.agents/mcps.json`.

---

## 🔌 Servidores MCP Registrados

| # | Categoria | Servidor | Markdown (Universal) | JSON (APIs/OpenCode) | `mcp_config.json` (Claude/Antigravity/Cline) | Descrição e Especialidade |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `_template` | **mcp-template** | [`MCP.md`](mcps/_template/MCP.md) | [`mcp.json`](mcps/_template/mcp.json) | [`mcp_config.json`](mcps/_template/mcp_config.json) | Template universal de um servidor MCP para registro e documentação neste repositório. |

---

## 🗂️ Categorias de Servidores MCP

| Categoria | Descrição | Status |
| :--- | :--- | :--- |
| `dev-tools` | Ferramentas de desenvolvimento, codebase, testes e automação (ex.: AutoDoc MCP, Playwright MCP) | Estrutura criada — vazio |
| `databases` | Acesso e interação com bancos de dados SQL/NoSQL (ex.: sqlite-mcp, postgres-mcp) | Estrutura criada — vazio |
| `cloud-infra` | Provisionamento e operação em AWS, Azure, GCP, OCI e cloud-edge (ex.: Cloudflare) | Estrutura criada — vazio |
| `security` | Segurança ofensiva/defensiva, análise estática/dinâmica e APIs de threat intel | Estrutura criada — vazio |
| `observability` | Métricas, logs, traces e telemetria (ex.: OpenTelemetry MCP) | Estrutura criada — vazio |
| `ai` | LLMs, embeddings, RAG, MLOps e agentes de IA | Estrutura criada — vazio |
| `data` | Engenharia de dados, pipelines, Data Mesh e streaming | Estrutura criada — vazio |

---

## ⚙️ Como Utilizar

1. **Copie o template**: `mcps/_template/` → `mcps/<categoria>/<nome-mcp>/`.
2. **Preencha os manifestos**: `MCP.md` (especificação canônica), `mcp.json` (APIs/OpenCode) e
   `mcp_config.json` (Claude Desktop, Antigravity, Cline).
3. **Registre** no `CATALOGO.md` e nesta tabela.
4. **Discovery**: adicione o caminho em `.agents/mcps.json`.
5. **Valide** com `python scripts/validate_skills.py` (se aplicável).

> ⚠️ **Nunca armazene segredos/tokens** nos manifestos. Use interpolação `{env:VAR}` /
> `${VAR}` ou variáveis de ambiente.
