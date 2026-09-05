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

## 🤝 Orquestração Multiagente, Descoberta Sob Demanda e Protocolo TOON

Esta seção estabelece o padrão universal para orquestração, delegação e cooperação entre múltiplos agentes de IA. Por ser genérica, esta especificação se aplica a qualquer harness, framework ou ferramenta (OpenCode, Google Antigravity, Claude Code, Cursor, Aider, LangChain, CrewAI, etc.).

### 1. Descoberta Inicial em Memória (Single Scan per Session)
Como os repositórios de agentes e skills são vivos e dinâmicos:
- **Execução no 1º turno da sessão**: No primeiro comando de uma nova sessão, o agente orquestrador inspeciona o ambiente e indexa os agentes e skills disponíveis.
- **Cache de sessão**: Esse inventário é mantido no contexto/memória da sessão ativa.
- **Proibição de re-scanning repetitivo**: Fica estritamente vedada a execução de novas varreduras em disco (`find`, `ls` recursivo, etc.) para redescobrir agentes/skills a cada novo comando subsequente, a menos que o usuário declare explicitamente que adicionou ou alterou um agente ou skill durante a conversa.

### 2. Priorização: Especialistas Existentes e Ativação de Skills
- **Delegação a agentes especializados**: Ao receber ou decompor uma demanda, verifique no catálogo indexado se já existe um agente concebido para a área (ex.: DBA, DevOps, QA/Testes, Segurança, Frontend, Backend, etc.). Se existir, delegue preferencialmente a ele em vez de criar um agente novo ou assumir o papel de forma genérica.
- **Consulta mandatória a Skills**: Antes de executar procedimentos técnicos, arquiteturais ou de codificação, o agente responsável deve obrigatoriamente carregar a skill correspondente (`SKILL.md`) do catálogo e seguir suas prescrições.
- **Reaproveitamento de instâncias ativas**: Em ferramentas com suporte a instâncias concorrentes/subagentes persistentes, reutilize instâncias em estado ocioso (`idle`) antes de instanciar novas entidades.

### 3. Decomposição e Paralelização Concorrente
- **Paralelismo ativo**: Sempre que uma tarefa puder ser decomposta em subtarefas independentes (ex.: desenvolvimento simultâneo de módulos desacoplados, implementação de código vs. escrita de suíte de testes, análise estática vs. revisão de infraestrutura), divida a execução e acione os agentes em paralelo para acelerar o ciclo de entrega.
- **Isolamento de contexto**: Subtarefas paralelas devem ter limites bem definidos de escopo e arquivos para evitar sobreposições e condições de corrida.

### 4. Protocolo Hiper-Eficiente de Troca de Informação: TOON
Para economizar tokens, diminuir a latência e eliminar o excesso sintático de formatos verbosos de JSON conversacional, a comunicação, handoff e conciliação entre agentes deve adotar o protocolo **TOON (Token-Oriented Object Notation / Compact Pipe-Separated Attributes)**:

#### Formato Canônico do Payload TOON:
```text
@FROM: <agente-emissor>
@TO: <agente-destinatario-ou-orchestrator>
@STATUS: <OK | CONFLICT | BLOCKED | NEED_INFO>
@CTX: <identificador-conciso-do-contexto-ou-tarefa>
@FILES: <arquivo1:linhas>;<arquivo2:linhas>
@SUMMARY: <resumo-ultra-compacto-das-alteracoes-ou-decisao>
@ACTION_NEEDED: <proximo-passo-objetivo-ou-requisicao-de-consenso>
```

#### Regras de Resolução de Conflitos e Handoff:
1. **Handoff de Conclusão**: Ao concluir sua subtarefa, cada agente transmite o payload TOON reportando os arquivos modificados e seu status.
2. **Resolução de Conflitos**: Se forem identificadas inconsistências de contratos (ex.: incompatibilidade entre endpoint e cliente, divergência em modelo de dados ou contratos de tipos), os agentes envolvidos devem trocar payloads em TOON focados no desacordo até estabelecerem um consenso alinhado.
3. **Síntese Final**: O orquestrador consolida as entregas validadas e emite a resposta final compilada para o usuário.

## 🔄 Ciclo de Vida e Evolução Contínua de Agentes e Skills

Para garantir que o ecossistema de conhecimento permaneça atualizado, robusto e em constante evolução, todo agente que atua no repositório deve adotar uma postura proativa de manutenção e expansão:

### 1. Portabilidade Universal e Caminhos Relativos
- **Proibição de caminhos absolutos**: Todo arquivo, link, documentação ou manifesto criado ou atualizado deve utilizar estritamente **caminhos relativos** a partir da raiz do repositório (ex.: `skills/<categoria>/<nome>/SKILL.md`, `agents/<nome>/`, `CATALOGO.md`).
- Caminhos absolutos específicos de máquina (ex.: `/home/...`, `/Users/...`, `C:\...`) são proibidos nos arquivos rastreados pelo repositório, garantindo portabilidade em qualquer ambiente, sistema operacional ou contêiner.

### 2. Atualização e Aprimoramento Contínuo (Feedback Loop)
- **Incorporação de novos conhecimentos**: Sempre que a resolução de uma demanda produzir novos aprendizados técnicos, correções de bugs complexos, runbooks aperfeiçoados ou novos padrões recomendados, atualize a skill correspondente (`SKILL.md` e referências associadas).
- **Evitar degradação ou obsolescência**: Ao notar que uma skill ou agente possui bibliotecas defasadas, instruções obsoletas ou falta de casos de uso modernos, proponha ou aplique a atualização incremental seguindo o padrão de progressive disclosure.

### 3. Criação de Novos Ativos Especializados
Quando uma demanda abordar um domínio ou tecnologia ainda não atendida no catálogo:
- **Criação de Nova Skill**:
  1. Estruture a pasta em `skills/<categoria>/[<subcategoria>/]<nome-skill>/`.
  2. Crie o arquivo canônico `SKILL.md` com YAML frontmatter (`name`, `description` em terceira pessoa) e corpo instrucional objetivo.
  3. Registre a nova skill nas tabelas do catálogo unificado em `CATALOGO.md`.
- **Criação de Novo Agente**:
  1. Siga o padrão multi-harness em `agents/<nome-do-agente>/` gerando a tríplice canônica: `AGENT.md`, `agent.yaml` e `agent.json`.
  2. Registre o novo agente em `CATALOGO.md` e `agents/README.md`.
- **Validação de Qualidade**:
  - Antes de finalizar qualquer adição ou modificação, execute os testes ou scripts de validação (`python scripts/validate_skills.py`, se disponível) para certificar a integridade de frontmatter, sintaxe e referências.
