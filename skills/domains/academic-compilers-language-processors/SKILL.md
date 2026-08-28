---
name: academic-compilers-language-processors
description: Especialista em Engenharia de Compiladores e Processadores de Linguagem baseado na obra Compilers Principles, Techniques, and Tools (Dragon Book - Aho, Lam, Sethi, Ullman). Cobre Análise Léxica (Flex/Lex, DFAs), Análise Sintática (Bison/Yacc, LL(k), LR(1), LALR), Análise Semântica (Tabelas de Símbolos, Inferência de Tipos), Representação Intermediária (Three-Address Code, SSA Form), Otimização de Código e Geração de Código Nativo/LLVM IR.
---

# Engenharia de Compiladores e Processadores de Linguagem (Dragon Book)

Esta skill estabelece a arquitetura completa de pipelines de tradução de código-fonte de alto nível para representações intermediárias e código de máquina otimizado.

---

## 🔄 1. Pipeline de Compilação

```
Código-Fonte ──> [ Análise Léxica (Tokens) ] ──> [ Análise Sintática (AST) ]
             ──> [ Análise Semântica (Tipos) ] ──> [ Geração de Código Intermediário (SSA/IR) ]
             ──> [ Otimizações de Fluxo de Controle e Dados ] ──> [ Geração de Código Alvo ]
```

---

## ⚙️ 2. Representação Intermediária em Single Static Assignment (SSA)

No formato SSA, cada variável é atribuída exatamente uma vez, e funções $\phi$ (Phi-nodes) são inseridas nos pontos de junção do fluxo de controle:

```llvm
; Exemplo de LLVM IR gerado para cálculo condicional
entry:
  %cmp = icmp sgt i32 %a, %b
  br i1 %cmp, label %then, label %else

then:
  %res1 = add i32 %a, 10
  br label %merge

else:
  %res2 = sub i32 %b, 5
  br label %merge

merge:
  %res = phi i32 [ %res1, %then ], [ %res2, %else ]
  ret i32 %res
```
