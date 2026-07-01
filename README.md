# Repositório de Skills e Customizações

Este repositório serve como uma pasta genérica centralizada para carregar habilidades (skills), instruções de agentes e definições de projetos para assistentes de programação de IA em CLI e IDEs.

A estrutura foi projetada para ser modular, extensível e compatível com as especificações de customização baseadas em agentes.

## 📁 Estrutura de Pastas

```text
├── README.md             # Este guia explicativo
├── AGENTS.md             # Regras gerais do projeto, estilo e restrições
├── skills.json           # Registro de caminhos de skills externas e heranças
├── skills/               # Diretório contendo as skills (regras de contexto)
│   ├── software-architect/ # Skill principal de Arquiteto de Software
│   ├── documentation-designer/ # Skill auxiliar de desenhos e diagramas (Mermaid)
│   ├── dp-*/             # 22 Skills de Padrões de Projeto (Design Patterns do GoF)
│   └── template-skill/   # Exemplo/Template de skill
└── agents/               # Diretório contendo os agentes configurados (ADK 2.0)
    ├── documenter/       # Agente Documentador e Designer
    └── software-architect/ # Agente Arquiteto de Software
```

## 🛠️ Como Utilizar

### 1. Regras do Projeto (`AGENTS.md`)
Escreva no arquivo [AGENTS.md](AGENTS.md) as regras de comportamento gerais que todos os agentes que carregam essa pasta devem seguir (p. ex., guias de estilo de código, convenções de arquitetura, padrões de commit).

### 2. O Ecossistema de Arquitetura, Design Patterns e Documentação
Neste repositório, as decisões de engenharia estão modularizadas e integradas:
- **[software-architect](skills/software-architect/SKILL.md)**: Atua como a skill coordenadora. Quando o agente precisa propor decisões de baixo nível, aplicar DDD ou realizar modelagem lógica, ele carrega essa skill.
- **[documentation-designer](skills/documentation-designer/SKILL.md)**: Skill auxiliar especializada em documentar sistemas e desenhar fluxogramas, diagramas de classe e sequências usando a sintaxe clássica do Mermaid.js.
- **[Design Patterns (dp-*)](skills/dp-factory-method/SKILL.md)**: Habilidades de apoio específicas para cada um dos 22 padrões clássicos de projeto. A skill de arquiteto direciona a invocação dessas skills de forma condicional dependendo do cenário.

### 3. Criando uma Nova Habilidade (Skill)
Para criar uma nova skill, adicione uma pasta sob `skills/` seguindo a estrutura do [template-skill](skills/template-skill/).
O arquivo principal é o `SKILL.md`, que precisa iniciar com um cabeçalho frontmatter em YAML:

```yaml
---
name: "Nome da Skill"
description: "Descrição de quando a IA deve ativar e usar esta skill"
---
# Instruções da Skill
Escreva aqui as diretrizes detalhadas de execução para esta skill específica.
```

### 4. Gerenciando Dependências e Heranças (`skills.json`)
O arquivo [skills.json](skills.json) permite registrar caminhos para outras pastas de skills (p. ex., de repositórios compartilhados do time) ou excluir skills específicas que você não deseja que sejam carregadas.
