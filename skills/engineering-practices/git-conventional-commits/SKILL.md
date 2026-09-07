---
name: git-conventional-commits
description: "Padroniza a elaboração de commits atômicos e histórico de controle de versão utilizando a especificação Conventional Commits v1.0.0 (feat, fix, refactor, perf, test, docs, breaking changes) com inspeção orientada a git diff."
---

# Git Conventional Commits v1.0.0 Engineering

Esta skill estabelece o padrão rigoroso de elaboração de mensagens de commit e gestão de histórico git seguindo a especificação **Conventional Commits v1.0.0**.

---

## 📜 1. Estrutura Canônica da Mensagem

```text
<tipo>[escopo opcional]: <descrição concisa no imperativo>

[corpo opcional detalhado explicando a motivação e contexto do 'porquê']

[rodapé(s) opcional(is) para breaking changes e links de issue/PR]
```

---

## 🏷️ 2. Tipos Canônicos de Commit

| Tipo | Finalidade e Impacto no Versionamento Semântico | Exemplo |
| :--- | :--- | :--- |
| **`feat`** | Nova funcionalidade para o usuário ou consumidor da API (dispara MINOR). | `feat(auth): add passkey authentication support` |
| **`fix`** | Correção de defeito/bug para o usuário ou sistema (dispara PATCH). | `fix(payment): prevent duplicate webhook processing` |
| **`refactor`**| Refatoração interna que não altera comportamento externo nem conserta bug. | `refactor(orders): extract discount calculation to domain entity` |
| **`perf`** | Melhoria de desempenho, latência ou uso de memória. | `perf(cache): use Redis pipeline for bulk token validation` |
| **`test`** | Adição ou correção de suítes de testes (sem alterar código de produção). | `test(fuzz): add property-based tests for currency conversion` |
| **`docs`** | Alterações exclusivas na documentação ou comentários. | `docs(readme): update multi-agent orchestration instructions` |
| **`style`** | Ajustes de formatação, lint e espaçamento (sem impacto funcional). | `style(linter): apply prettier formatting across components` |
| **`build`** | Mudanças em build systems ou dependências externas (Maven, Gradle, npm). | `build(deps): bump spring-boot from 3.2.1 to 3.3.0` |
| **`ci`** | Alterações em scripts e configurações de CI/CD (GitHub Actions, GitLab CI). | `ci(actions): add mutation score check gate to pipeline` |
| **`chore`** | Tarefas de manutenção rotineiras que não modificam código src ou tests. | `chore: clean temporary cache files` |

---

## 💥 3. Breaking Changes
- Adicionar exclamação `!` logo após o tipo/escopo para alertar quebra de compatibilidade (dispara MAJOR):
  ```text
  feat(api)!: change user endpoint response payload structure

  BREAKING CHANGE: The 'userId' field has been renamed to 'id' in the JSON response.
  ```

---

## 🛠️ 4. Fluxo de Inspeção e Elaboração de Commit
1. **Inspecionar Área de Staging**: Rodar `git diff --cached` para analisar os arquivos e blocos adicionados.
2. **Classificar a Natureza**: Escolher o tipo e escopo semântico correto.
3. **Escrever Mensagem no Modo Imperativo**: Escrever "add", "fix", "update" (e não "added", "fixing", "fixes").
