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
   - Garanta a não duplicação e reutilização ativa de código utilizando a skill [clean-code-reusability](file:///B:/Code/skills/skills/clean-code-reusability/SKILL.md).

4. **Gerenciamento de Erros e Logs**:
   - Evite blocos catch vazios.
   - Utilize logging apropriado em vez de prints genéricos no console.

## 🔧 Workflow de Trabalho

- **Antes de programar**: Entenda os requisitos, valide a estrutura existente e, se necessário, planeje em voz alta no chat. **Sempre faça uma busca prévia no codebase, de acordo com as regras de [clean-code-reusability](file:///B:/Code/skills/skills/clean-code-reusability/SKILL.md), para garantir a reutilização de funções e lógicas existentes antes de criar novos blocos de código.**
- **Durante a implementação**: Use commits pequenos e descritivos.
- **Após concluir**: Teste localmente as alterações propostas e revise eventuais mensagens de lint.
