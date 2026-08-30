# Regras e Definições Gerais do Projeto

Este arquivo define as diretrizes gerais de comportamento, padrões de projeto e regras de estilo que devem ser seguidas por todos os assistentes de IA ao interagir com o código deste repositório.

## 📌 Diretrizes Globais

1. **Idiomas**:
   - Os comentários no código e mensagens de commit devem ser preferencialmente em **Inglês** (ou conforme o padrão definido pelo time).
   - As interações no chat com o desenvolvedor devem ser em **Português**, a menos que solicitado de outra forma.

2. **Qualidade e Estilo de Código**:
   - Sempre siga as convenções da linguagem do projeto atual (p. ex., PEP 8 para Python, ESLint/Prettier para JavaScript/TypeScript).
   - Priorize legibilidade e simplicidade sobre otimizações prematuras.
   - Mantenha funções pequenas e com responsabilidade única.

3. **Arquitetura e Clean Code**:
   - Siga os princípios SOLID.
   - Mantenha a separação de responsabilidades (camadas de negócio, dados e apresentação).
   - Garanta a não duplicação e reutilização ativa de código utilizando a skill [clean-code-reusability](skills/engineering-practices/clean-code-reusability/SKILL.md).

4. **Gerenciamento de Erros e Logs**:
   - Evite blocos catch vazios.
   - Utilize logging apropriado em vez de prints genéricos no console.

## 🔧 Workflow de Trabalho

- **Antes de programar**: Entenda os requisitos, valide a estrutura existente e, se necessário, planeje em voz alta no chat. **Sempre faça uma busca prévia no codebase, de acordo com as regras de [clean-code-reusability](skills/engineering-practices/clean-code-reusability/SKILL.md), para garantir a reutilização de funções e lógicas existentes antes de criar novos blocos de código.**
- **Durante a implementação**: Use commits pequenos e descritivos.
- **Após concluir**: Teste localmente as alterações propostas e revise eventuais mensagens de lint.

## 📚 Workflow para Criação de Skills a partir de Referências em PDF

Quando for solicitada a criação ou aprimoramento de uma skill baseada em referências em PDF:
1. **Extração / Conversão de PDF para Markdown**: Execute o script embutido `python scripts/pdf_to_markdown.py <caminho_do_pdf>` para converter o livro ou documento em um arquivo `.md` estruturado (ou utilize a opção `--toc-only` para extrair primeiro a tabela de conteúdos/capítulos).
2. **Análise de Conteúdo**: Inspecione o arquivo Markdown gerado para extrair definições técnicas, formulários, frameworks e exemplos de código relevantes.
3. **Elaboração da Skill**: Construa ou aprimore a skill em `skills/<categoria>/[<subcategoria>/]<nome-skill>/SKILL.md` e registre a nova skill no catálogo em [CATALOGO.md](CATALOGO.md).

## 🤖 Padrão Multi-Harness para Criação de Agentes

Ao criar ou atualizar agentes especializados neste repositório, garanta a compatibilidade universal mantendo a estrutura tríplice sincronizada em `agents/<nome-do-agente>/`:

1. **`AGENT.md`**: Especificação canônica em Markdown com YAML frontmatter (`name`, `description`, `skills`, `model` — ver regras abaixo), instruções completas e lista de skills clicáveis.
2. **`agent.yaml`**: Declaração estruturada YAML com ferramentas apontando para caminhos relativos em `../../skills/...` (compatível com Google Antigravity / ADK 2.0 e runners YAML).
3. **`agent.json` / `plugin.json`**: Manifesto em JSON para consumo por APIs REST, OpenAI Assistants e frameworks como LangChain, AutoGen e CrewAI.
4. **Registro Central**: Registre o novo agente nas tabelas de catálogo de [agents/README.md](agents/README.md) e [CATALOGO.md](CATALOGO.md).

### 🧠 Regras de Modelo (`model`) por Harness

**Regra geral**: por padrão, **omitir completamente a linha `model`** do frontmatter/manifesto — o agente herda o modelo da sessão ou da configuração global no seu repositório. Só declare `model` explicitamente se for necessário fixar um modelo. Nunca use o valor literal `inherit` sem confirmar que o harness de destino o interpreta.

| Harness / Consumidor           | `model: inherit`            | Omitir `model`                          | Como fixar modelo                                                   |
| ------------------------------ | --------------------------- | --------------------------------------- | ------------------------------------------------------------------- |
| **OpenCode**                   | ❌ Não suportado (invalida config) | ✅ Suportado — usa modelo da sessão/global | Frontmatter: `model: provider/model-id` (ex.: `anthropic/claude-sonnet-4-6`) ou `agent.<nome>.model` no `opencode.json` |
| **Claude Code**                | ✅ Suportado — usa o modelo da conversa principal | ✅ Suportado — usa modelo padrão via configuração | Frontmatter: `model: sonnet` / `opus` / `haiku` / `inherit` (aliases aceitos) |
| **Google Antigravity (agent.yaml)** | ✅ Suportado — herda preferência do usuário | ⚠️ Verificar comportamento do runtime | Campo `model:` no `agent.yaml` com ID do modelo                     |
| **Codex**                      | ❌ Não aplicável (não lê frontmatter) | ✅ Tratado como prompt/texto simples    | Config global `config.toml` ou flag `--model` na execução           |
| **Aider**                      | ❌ Não aplicável (não lê frontmatter) | ✅ Tratado como prompt/texto simples    | Flags `--model` / variáveis de ambiente na execução                 |
| **Cursor**                     | ❌ Não aplicável            | ✅ Seleção de modelo via UI             | Seleção no switcher de modelos da IDE                               |
| **agent.json (LangChain, AutoGen, CrewAI, APIs REST)** | ⚠️ Só como convenção interna de geração — o framework não interpreta | ⚠️ Framework resolve em runtime (env/config) | Campo estruturado `"model": "<id>"` no manifesto, resolvido pelo código consumidor |

**Diretrizes práticas**:

1. **No `AGENT.md`**: omitir `model` (comportamento default, suportado por OpenCode e Claude Code). Se for inevitável fixar um modelo num agente específico, use o formato completo `provider/model-id` (portável entre OpenCode e outras ferramentas que leem frontmatter).
2. **Valor `provider/model-id` deve existir no catálogo** (ex.: models.dev) e refletir os provedores realmente habilitados na instalação do usuário.
3. **No `agent.yaml`**: `model: inherit` é aceitável (Antigravity interpreta); o OpenCode ignora esse arquivo.
4. **No `agent.json`/`plugin.json`**: evitar `model: "inherit"` como contrato; preferir omitir e deixar o framework resolver (env var, config ou parâmetro de construção do agente).
5. **Nunca copiar `model: inherit`** de `agent.yaml`/`agent.json` para o `AGENT.md` para "espelhar" configuração — a tríplice de arquivos **não precisa ter o mesmo valor de modelo**; apenas `name`, `description` e skills devem ficar sincronizados.


