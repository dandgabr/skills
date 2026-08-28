import os

catalogo_path = '/home/daniel/Code/skills/CATALOGO.md'
output_path = '/home/daniel/Code/skills/.zai/ZAI.md'

with open(catalogo_path, 'r', encoding='utf-8') as f:
    catalogo_content = f.read()

header = """# 🧠 ZAI CLI - Manual de Instruções, Agentes e Skills do Repositório

Este arquivo é lido automaticamente pelo **ZAI CLI** (.zai/ZAI.md) e define as diretrizes de engenharia, o protocolo de ativação de personas e o índice unificado de todas as **196 Habilidades (Skills)** e **42 Agentes Especializados Universais**.

---

## 📌 Diretrizes Globais do Projeto (Alinhamento Canônico)

1. **Idiomas**:
   - Os comentários no código e mensagens de commit devem ser preferencialmente em **Inglês** (ou conforme o padrão definido pelo time).
   - As interações no chat com o desenvolvedor devem ser em **Português**, a menos que solicitado de outra forma.

2. **Qualidade e Estilo de Código**:
   - Sempre siga as convenções da linguagem do projeto atual (p. ex., PEP 8 para Python, ESLint/Prettier para JavaScript/TypeScript, Google Java Style, etc.).
   - Priorize legibilidade e simplicidade sobre otimizações prematuras.
   - Mantenha funções pequenas e com responsabilidade única (SRP).

3. **Arquitetura e Clean Code**:
   - Siga os princípios SOLID e Domain-Driven Design (DDD) quando aplicável.
   - Mantenha a separação de responsabilidades (camadas de negócio, dados e apresentação).
   - Garanta a não duplicação e reutilização ativa de código utilizando a skill canônica [clean-code-reusability](skills/engineering-practices/clean-code-reusability/SKILL.md).

4. **Gerenciamento de Erros e Logs**:
   - Evite blocos catch/except vazios.
   - Utilize logging apropriado e estruturado em vez de prints genéricos no console.

---

## ⚡ Protocolo de Operação e Ativação de Skills e Agentes no ZAI CLI

O ZAI CLI opera com modelos avançados da família GLM (GLM-4.6 / GLM-4.5) e ferramentas de sistema (`view_file`, `str_replace_editor`, `create_file`, `bash`, `search`, `batch_edit`).

### 🎯 Regra de Ativação Dinâmica:
1. **Identificação de Contexto**: Ao receber uma tarefa técnica especializada (por exemplo, auditoria de segurança, modelagem de banco de dados, refatoração de código, testes, física, matemática, engenharia, telecomunicações, etc.), identifique o **Agente** ou a **Skill** correspondente no catálogo abaixo.
2. **Carregamento sob Demanda**: Utilize a ferramenta `view_file` para carregar o arquivo canônico de instruções:
   - Para Agentes: `view_file` em `agents/<nome-do-agente>/AGENT.md`
   - Para Skills: `view_file` em `skills/<categoria>/.../<nome-da-skill>/SKILL.md`
3. **Execução Especializada**: Assuma o papel, aplique os padrões técnicos, checklists, formulários e convenções especificados no documento carregado.
4. **Clean Code Pre-Check**: Antes de criar ou modificar código, faça buscas com `search` ou `view_file` para reutilizar estruturas existentes conforme [clean-code-reusability](skills/engineering-practices/clean-code-reusability/SKILL.md).

---

"""

full_content = header + catalogo_content

os.makedirs('/home/daniel/Code/skills/.zai', exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

print(f'Generated {output_path} successfully ({len(full_content)} bytes).')
