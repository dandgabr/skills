---
name: "clean-code-reusability"
description: "Garante a escrita de código limpo, legível, livre de redundâncias através da reutilização ativa de componentes existentes, e documentado de acordo com as melhores práticas da tecnologia."
---

# Habilidade de IA: Código Limpo e Reutilização (Clean Code & Reusability)

Esta skill orienta a inteligência artificial a assegurar a máxima qualidade de código no projeto, focando em legibilidade, manutenibilidade (Clean Code), eliminação ativa de redundâncias através do reaproveitamento de lógicas existentes (Reusability), e documentação precisa e expressiva.

---

## 🧭 Diretrizes de Código Limpo e Reutilização

Ao atuar nesta skill, paute suas decisões técnicas nos seguintes pilares fundamentais:

### 1. Código Limpo (Clean Code)
- **Funções Pequenas e Focadas**: Mantenha funções pequenas e com responsabilidade única (Single Responsibility Principle). Se uma função faz mais de uma coisa, divida-a.
- **Nomes Significativos**: Utilize nomes descritivos e pronunciáveis para variáveis, funções, classes e arquivos. Evite abreviações obscuras e sufixos desnecessários.
- **Assinaturas Limpas**: Limite o número de parâmetros de uma função (idealmente no máximo 2 ou 3). Se precisar de mais, encapsule-os em um objeto/estrutura de parâmetros.
- **Evite Efeitos Colaterais**: Funções devem preferencialmente ser puras, não alterando estados globais ou externos de forma inesperada.
- **Tratamento de Erros Limpo**: Use exceções em vez de retornar códigos de erro. Isole blocos `try-catch` em funções próprias se eles poluírem a lógica principal.

### 2. Validação de Redundâncias e Reutilização Ativa
- **Varredura Prévia Obrigatória**: **Antes de criar qualquer nova função, utilitário ou classe**, realize uma busca no codebase (usando busca semântica ou grep) para verificar se já existe uma lógica semelhante ou idêntica.
- **Princípio DRY (Don't Repeat Yourself)**:
  - Se encontrar uma função que faz exatamente o que precisa, **reutilize-a**.
  - Se encontrar uma função que faz algo muito parecido, **refatore-a** (ex: adicione um parâmetro opcional ou generalize o tipo) em vez de duplicar o código.
- **Centralização de Helpers**: Mantenha funções utilitárias em locais apropriados (como `utils/`, `helpers/` ou arquivos compartilhados do domínio) e exporte-as de forma clara.
- **Refatoração de Duplicações**: Se identificar trechos de código redundantes já existentes no codebase durante a sua análise, sugira ou execute a consolidação deles em uma única abstração compartilhada.

### 3. Documentação Correta e Significativa
- **Foco no "Porquê", não no "O quê"**: Evite documentações redundantes que apenas repetem a assinatura da função. Foque em explicar regras de negócio complexas, decisões de design não óbvias ou restrições técnicas.
- **Padrões de Mercado**:
  - **TypeScript/JavaScript**: Use o padrão **JSDoc** detalhando tipos, parâmetros (`@param`), retornos (`@returns`) e possíveis exceções (`@throws`).
  - **Python**: Use **Docstrings** seguindo o estilo Google ou PEP 257.
- **Documentação Inline Moderada**: Comentários dentro do código devem ser raros e servir apenas para explicar lógicas complexas ou temporárias (hacks). Se o código precisa de muitos comentários para ser entendido, ele deve ser refatorado para ser mais legível.

---

## ⚙️ Protocolo de Implementação e Revisão

Sempre que for solicitado a criar, modificar ou revisar um código:

1. **Fase de Descoberta (Busca por Reuso)**:
   - Formule termos de pesquisa para a funcionalidade desejada.
   - Execute buscas de texto ou regex no workspace para mapear funções existentes com finalidades semelhantes.
2. **Desenho de Assinatura**:
   - Desenhe a função mantendo-a focada e alinhada com as convenções da linguagem do projeto.
3. **Escrita e Documentação**:
   - Implemente a lógica sem redundâncias e escreva a documentação apropriada (JSDoc, Docstrings).
4. **Verificação de Regras Estáticas**:
   - Garanta conformidade com ferramentas de lint (ESLint, Pylint, Flake8) e formatação (Prettier, Black).

---

## 🔗 Integração com Outras Skills de Desenvolvimento

Esta skill atua de forma transversal e deve ser consultada por todas as habilidades de desenvolvimento:
- [backend-developer](../backend-developer/SKILL.md): Garante que APIs, serviços e repositórios não dupliquem regras de negócio e persistência.
- [frontend-developer](../frontend-developer/SKILL.md): Evita a criação de componentes ou hooks duplicados e assegura boas práticas de organização de código client-side.
- [software-architect](../software-architect/SKILL.md): Apoia na manutenção da coesão do design, promovendo abstrações limpas e DRY.
- [tech-typescript](../../tech/tech-typescript/SKILL.md): Orienta a reutilização de tipos e a documentação via JSDoc.
- [tech-python](../../tech/tech-python/SKILL.md): Orienta o estilo PEP 8, a criação de docstrings corretas e a redução de complexidade ciclomática.
