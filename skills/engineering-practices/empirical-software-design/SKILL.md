---
name: empirical-software-design
description: Especialista em Design Empírico de Software e Refatoração Incremental estilo Tidy First (Kent Beck). Cobre estrutura vs comportamento (tidying separado de mudança), teoria econômica do design (opções reais, custo de mudança), acoplamento e coesão, o repertório de tidyings (guard clauses, extrair variável/função, inline, juntar/quebrar, moving features), e a decisão Quando fazer Tidy (Now? Never? Later?).
---

# Habilidade de IA: Design Empírico de Software (Tidy First / Empirical Software Design)

Esta skill orienta a inteligência artificial a melhorar o design de código de forma **incremental, pequena e reversível**, separando mudanças de estrutura de mudanças de comportamento, baseada na obra *Tidy First? A Personal Exercise in Empirical Software Design* (Kent Beck).

---

## 🎯 1. Princípio Central: Separe Estrutura de Comportamento

- **Mudança de comportamento** = alterar o que o sistema faz (novas regras, features, fixes).
- **Mudança de estrutura (tidying)** = alterar como o código está organizado **sem alterar seu comportamento** (extrair função, renomear, mover código).
- **Nunca misture os dois no mesmo commit/mudança**. Primeiro tidy, depois a mudança de comportamento ("Tidy First?"), ou tidy depois ("Tidy After?"), mas identifique explicitamente qual está fazendo.
- Benefício: diffs pequenos, revisão trivial, bisect confiável, conflitos de merge minimizados.

---

## 💰 2. Teoria Econômica do Design

Software design é, antes de tudo, um **exercício econômico**: minimize o custo total futuro.

- **Custo humano ≠ custo hoje**: o custo de uma mudança inclui o tempo de quem lê, entende e modifica depois. Pagar um pouco agora (tidy) pode reduzir muito o custo amanhã.
- **Opções reais (Real Options)**: manter flexibilidade tem valor — como uma opção financeira, adiar decisões irreversíveis e simplificar reversíveis cria valor. Não centralize cedo demais nem espalhe prematuramente.
- **`Custo(mudança) = Σ esforço(ler, entender, editar, testar)`**: otimize para o leitor futuro, não para o escritor de hoje.
- **Opção vs obrigação**: cada acoplamento cria obrigação; cada abstração bem colocada cria opção. Prefira designs que aumentem opções a médio prazo.
- **Escala de tempo**: tidyings levam segundos/minutos; designs estruturais levam dias; otimize a taxa de mudança agregada, não cada linha.

---

## 🧲 3. Acoplamento e Coesão (Teoria do Design)

- **Acoplamento**: quanto mudar um elemento força mudar outros. Reduza acoplamento para reduzir custo de mudança.
- **Coesão**: elementos que mudam juntos devem viver juntos. Aumente coesão agrupando por razões de mudança.
- **Regra prática de design local**: prefira o design que torna a próxima mudança mais barata — julgue cada decisão no contexto, empiricamente ("empirical software design"), sem dogmas como "menos linhas é melhor".
- **Sem Best Practices universais**: o que é bom design depende do fluxo de mudanças do sistema específico. Observe onde o código muda com frequência e co-losine (couple/cohesion) de acordo.

---

## 🧰 4. Repertório de Tidyings (catálogo de micro-refatorações)

Execute tidyings em minutos, um por commit:

| Tidying | Descrição resumida |
| :--- | :--- |
| **Guard Clause** | Saia cedo das condições inválidas para achatar aninhamento. |
| **Extract Variable / Function** | Nomeie expressões e passos para comunicar intenção. |
| **Inline Variable / Function** | Remova indireções sem valor de comunicação. |
| **Join Function** | Una funções chamadas só uma vez, uma só vez, juntas. |
| **Block Commentary** | Marque blocos com comentários transicionais que depois viram funções. |
| **Explicit Parameters** | Substitua réplicas de params implícitos (globais/campos) por parâmetros explícitos. |
| **Normalize Symbols** | Padronize nomes para o mesmo conceito (um conceito, um nome). |
| **New Interface (Old Implementation)** | Introduza a interface-alvo e delegue, migrando usos gradualmente. |
| **Move Function/Field** | Realoque para perto dos dados/behaviors com que muda junto. |
| **Combine Similar Shapes** | Una estruturas semelhantes em uma (cuidado: só se o custo de generalizar < manter duas). |
| **Helper Function & Helper Relation** | Extraia repetição para helpers; aproxime helper de quem o usa. |
| **Reorder Logic (read top-down)** | Coloque o caso principal primeiro e pormenores depois. |
| **Extract Constant** | Magic numbers/strings viram constantes nomeadas. |

---

## 🤔 5. Decisão: Quando Fazer Tidy?

Aplique a árvore de decisão antes de qualquer mudança:

1. **Será que vale a pena tidyar?** (custo do tidy × economia futura)
2. **Tidy agora (Now), depois (Later), ou nunca (Never)?**
   - **Now**: o tidy é pequeno (minutos) e destrava a mudança imediata.
   - **Later**: necessário, mas grande/inseguro agora — anote (TODO/issue) e faça depois, em passo próprio.
   - **Never**: tidy que não paga o custo (código prestes a morrer, área estável, deep freeze).
3. **Pergunte sempre: este tidy me aproxima ou me afasta do comportamento alvo?**
4. **Limite**: tidyings opcionalmente em lote, mas **nunca** misture tidy + feature no mesmo diff. Se o tidy virar avalanche, corte-o e faça só o essencial.

---

## 🔄 6. Protocolo de Execução (para IA em codebases reais)

1. **Leia para entender onde muda**: identifique o ponto de mudança requisitado e o entorno acoplado.
2. **Liste tidyings candidatos**: baratos, locais, que facilitam a mudança.
3. **Classifique cada um**: Now / Later / Never, com justificativa econômica curta.
4. **Execute tidyings "Now"** em commits separados (`refactor:`), comportamento preservado (testes verdes).
5. **Implemente a mudança de comportamento** em commit próprio (`feat:`/`fix:`).
6. **Comunicue**: em revisões, explique 1) o que muda, 2) o que foi tidado antes/depois e por quê.
7. **Nunca** aproveite o tidy para mudar comportamento "de passagem".

---

## 🔗 Integração com Outras Skills

- [clean-code-reusability](../clean-code-reusability/SKILL.md): clean code dá o vocabulário; Tidy First dá o *ritmo* e a economia das mudanças.
- [software-architect](../../roles/software-architect/SKILL.md): tidyings micro alimentam decisões macro do arquiteto com dados de mudança real.
- [sast-code-review](../../security/appsec/sast-code-review/SKILL.md): revise tidyings garantindo que nenhum controle de segurança foi afrouxado.
- [framework-testing](../../framework/framework-testing/SKILL.md): testes verdes são a pré-condição de qualquer tidy (rede de segurança).
- [lang-python](../../languages/lang-python/SKILL.md), [lang-java](../../languages/lang-java/SKILL.md), [lang-typescript](../../languages/lang-typescript/SKILL.md), [lang-go](../../languages/lang-go/SKILL.md), [lang-csharp](../../languages/lang-csharp/SKILL.md): aplique tidyings idiomáticos da linguagem em uso.