---
name: "template-skill"
description: "Um template básico que demonstra como estruturar uma habilidade (skill) personalizada para agentes de IA."
---

# Template de Habilidade Personalizada (Skill)

Esta é uma descrição estruturada de como uma habilidade deve ser documentada.

## 🎯 Objetivo da Skill
Descreva claramente o que esta skill faz, quais problemas ela resolve e por que ela é útil para o assistente.

## 🛠️ Instruções de Uso para a IA

1. **Contexto de Ativação**:
   - Ative esta skill sempre que o usuário solicitar uma tarefa relacionada ao escopo definido no frontmatter.
   
2. **Passo a Passo de Execução**:
   - Passo 1: Analise os arquivos e entradas.
   - Passo 2: Execute os scripts auxiliares se necessário (localizados em `./scripts/`).
   - Passo 3: Valide os resultados contra os exemplos em `./examples/`.

## 📚 Estrutura Interna da Skill
- [SKILL.md](SKILL.md): Este arquivo principal de regras e instruções.
- **`scripts/`**: Scripts executáveis (p. ex., Python, Node.js) que ajudam o agente a automatizar testes ou tarefas.
- **`examples/`**: Arquivos contendo boas práticas, snippets de código padrão ou casos de teste.
- **`resources/`**: Ativos diversos que servem de apoio (planilhas, imagens de referência, JSONs de configuração).
- **`references/`**: Documentação técnica de APIs, bibliotecas ou conceitos teóricos extensos.
